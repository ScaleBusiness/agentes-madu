"""Cortes + legendas do Reel "Acolher o choro" (Madu · Edite Pro, 14/10/2026).
Cortes = trechos de voz medidos com a régua sensível (medir.py), unindo pausas de até 0,30 s; folga 0,06 s antes e 0,08 s depois.
Sarah 14/10: tirar só a palavra "três" (silêncio antes 80,46–80,65 e pausa antes de "planos" 81,00–81,05).
Uso: python3 montar.py ../src/edite/madu-acolher/dados-madu-acolher.json"""
import json, os, re, sys, unicodedata
import numpy as np
AQUI = os.path.dirname(os.path.abspath(__file__))
ws = json.load(open(os.path.join(AQUI, 'transcricao/take-8651.json')))
v = np.load(os.path.join(AQUI, 'voz.npy')); P = 0.01
GAP, ANTES, DEPOIS = 0.30, 0.06, 0.08
RETIRAR = [(80.52, 81.03)]  # "três"

runs, a, last = [], None, None
for k, on in enumerate(v):
    t = k * P
    if on:
        if a is None: a = t
        elif t - last > GAP: runs.append([a, last + P]); a = t
        last = t
runs.append([a, last + P])
runs = [r for r in runs if r[1] - r[0] > 0.06]  # estalos soltos fora
cortes = []
for a, b in runs:
    de, ate = max(0, a - ANTES), b + DEPOIS
    for ra, rb in RETIRAR:
        if de < ra < ate:
            cortes.append([de, ra]); de = rb
    cortes.append([de, ate])
# junta cortes que se encostam por causa das folgas
fund = []
for c in cortes:
    if fund and c[0] <= fund[-1][1]: fund[-1][1] = max(fund[-1][1], c[1])
    else: fund.append(c)
cortes = fund

GRUPOS = [
    'Você não precisa deixar', 'seu filho *chorando*', 'para ele dormir melhor.',
    'Se você tem *medo*', 'de mexer no sono do seu filho,', 'porque não quer ver ele chorar,', 'eu te *entendo.*',
    'E esse medo', 'não é *exagero.*',
    'Me orientaram a deixar', 'a minha filha', 'chorando *sozinha*', 'até ela dormir.', 'E eu não consegui fazer.',
    'Esse medo costuma vir', 'com uma ideia', 'que existem só', '*dois caminhos.*',
    '~Que Ou você larga', 'seu bebê lá *sozinho*', 'no berço,', 'chorando até ele cansar.',
    'Ou as noites', 'vão continuar *ruins.*',
    'Mas existe', 'um *terceiro caminho.*',
    'Acolher o choro', 'não é a mesma coisa', 'que deixar a criança', '*chorando.*',
    'Acolher é ficar *perto,*', 'com calma,', 'sem *abandonar.*',
    'Eu não vou te prometer', 'que ele nunca vai chorar.', 'Toda mudança', 'vem um *protesto.*',
    'Mas o que eu te prometo', 'é que ele não vai passar', 'por isso *sozinho.*',
    'No Método *Sleepy,*', 'existe um pilar inteiro', 'para isso.', 'O *Afeto e Emoções.*',
    'A gente cuida', 'da *segurança emocional*', 'dele e da sua.',
    'E muitas vezes,', 'o plano traz', 'mais de um *caminho.*', 'Para vocês escolherem', 'o que faz sentido', 'para cada *família.*',
    'E se ele chorar', 'e não se acalmar no berço,', 'o colo não é *proibido.*',
    'Você pega,', 'acolhe com *tranquilidade*', 'e ajuda ele', 'voltar a dormir.',
    'Choro acolhido', 'não é *abandono.*',
    'Na Consultoria Sleepy,', 'em *45 dias,*', 'você recebe ~três', 'planos de sono', '*personalizado*', 'para a rotina do seu bebê', 'e da sua família.',
    'Para construir noites', 'mais *tranquilas*', 'e um sono', 'mais *sustentável.*',
    'Se você quer isso', 'para o seu filho,', 'comenta aqui', '*CONSULTORIA*^3', 'que eu te mando', 'as informações', 'pelo *direct.*',
]

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    return re.sub(r'[^a-z0-9]', '', ''.join(c for c in s if not unicodedata.combining(c)))

def posicao(t, lado='ini'):
    """tempo do bruto -> tempo no vídeo cortado. O Whisper às vezes marca a palavra dentro de uma pausa cortada:
    o início encosta no começo do trecho seguinte e o fim no fim do trecho anterior."""
    acc, prev_fim = 0.0, None
    for de, ate in cortes:
        if de - 0.02 <= t <= ate + 0.02: return acc + min(max(t, de), ate) - de
        if t < de: return acc if lado == 'ini' else (prev_fim if prev_fim is not None else acc)
        acc += ate - de; prev_fim = acc
    return acc

def main(saida):
    acc, saidas = 0.0, []
    for de, ate in cortes:
        saidas.append({'video': 'madu-acolher/video/take-8651.mp4', 'de': round(de, 3), 'ate': round(ate, 3), 'saida': round(acc, 3)}); acc += ate - de
    grupos, i, avisos = [], 0, []
    for g in GRUPOS:
        itens = []
        for tok in re.findall(r'\*[^*]+\*(?:\^\d)?|\S+', g):
            m = re.match(r'(.*?)\^(\d)$', tok); junta = int(m.group(2)) if m else 1
            if m: tok = m.group(1)
            destaque = tok.startswith('*')
            for parte in tok.strip('*').split(' '):
                bloco = ws[i:i + junta]; i += junta
                oculta = parte.startswith('~'); texto = parte.lstrip('~')
                if junta == 1 and norm(texto) != norm(bloco[0]['w']): avisos.append(f'"{texto}" × "{bloco[0]["w"]}" ({bloco[0]["s"]:.2f})')
                ini, fim = posicao(bloco[0]['s']), posicao(bloco[-1]['e'], 'fim')
                if fim < ini: fim = ini + 0.12
                if oculta: continue
                if ini is None or fim is None: avisos.append(f'"{texto}" fora dos cortes ({bloco[0]["s"]:.2f})'); continue
                itens.append({'texto': texto, 'inicio': round(ini, 3), 'fim': round(fim, 3), 'destaque': destaque})
        grupos.append({'inicio': itens[0]['inicio'], 'fim': itens[-1]['fim'], 'palavras': itens})
    if i != len(ws): avisos.append(f'{len(ws) - i} palavras sem grupo')
    json.dump({'duracao': round(acc, 3), 'cortes': saidas, 'grupos': grupos}, open(saida, 'w'), ensure_ascii=False, indent=1)
    print(f'{len(cortes)} cortes · duração 1x {acc:.2f}s (1,3x = {acc/1.3:.1f}s) · {len(grupos)} grupos')
    for a in avisos: print('AVISO', a)

if __name__ == '__main__':
    main(sys.argv[1])
