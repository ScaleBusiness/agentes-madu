"""Legendas para Reels (sem libass): gera blocos a partir da transcrição e grava via overlay de PNG.

1) python3 legendar.py gerar    video.mp4 legendas.json   -> transcreve o vídeo LIMPO e monta os blocos
2) python3 legendar.py remontar video.mp4 legendas.json --corrigir "errado=certo"  (sem retranscrever)
3) python3 legendar.py gravar   video.mp4 legendas.json saida.mp4 --estilo instagram|tiktok [--titulo "TEXTO"]
   instagram = só legenda, minúsculas, contorno preto (mais legível)
   tiktok    = título fixo no topo com fundo escuro + legenda menor (mais alta, fora da descrição do app)
"""
import json, os, subprocess, sys, tempfile, argparse
from PIL import Image, ImageDraw, ImageFont

_AQUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.environ.get("FONTE_LEGENDA", os.path.join(_AQUI, "..", "assets", "Raleway-VF.ttf"))

# ── Identidade visual Madu Drummond (Playbook Visual · branding/10-playbook-visual-madu-drummond.html)
AZUL_NOITE = (31, 75, 122)       # #1F4B7A · texto principal / contorno / caixa do gancho
AZUL_DRUMMOND = (77, 130, 181)   # #4D82B5 · círculo do número
PESSEGO = (255, 219, 213)
AMEIXA = (132, 98, 140)          # #84628C · opção 'roxo' da legenda        # #FFDBD5 · palavra de destaque (*assim*)
BRANCO = (255, 255, 255)
PESO = 600                       # Raleway SemiBold · nunca 700+ (regra SB)
PILARES = {1: (11, 173, 237), 2: (242, 165, 145), 3: (135, 200, 180), 4: (132, 98, 142)}  # --md-pN-forte

PROPRIOS = {"Sleepy", "Madu", "Ritmo", "Ninho", "Afeto", "Hábitos", "Zona", "Método", "Estados"}

def fonte(tam, peso=PESO):
    f = ImageFont.truetype(FONTE, tam)
    try:
        f.set_variation_by_axes([peso])
    except Exception:
        pass  # fonte estática: usa o peso do arquivo
    return f

def _pedacos(linha):
    """'faça *JAMAIS* isso' -> [('faça ', False), ('JAMAIS', True), (' isso', False)]"""
    out, dest = [], False
    for k, parte in enumerate(linha.split("*")):
        if parte:
            out.append((parte, dest))
        dest = not dest
    return out

FONTE_SCRIPT = os.path.join(_AQUI, "..", "assets", "AnotherShabby-Regular.ttf")  # playbook: Another Shabby original (Sarah 30/09)
FONTE_ROTULO = os.path.join(_AQUI, "..", "assets", "PatrickHandSC-Regular.ttf")  # Scripter (web) · só rótulo curto em CAIXA ALTA
PESSEGO_FORTE = (242, 165, 145)  # #F2A591 · palavra-destaque na legenda (lê sobre branco e sobre azul)
# Cor da legenda (Madu 28/09: "azul, roxo ou branco" · NUNCA branco com contorno — polui)
COR_LEGENDA = os.environ.get("COR_LEGENDA", "branco")  # Sarah 30/09 (final): legenda BRANCA; azul não se lê sobre a roupa colorida

FONTE_LEG = os.path.join(_AQUI, "..", "assets", "Inter-VF.ttf")  # legenda: Inter Bold (Sarah 28/09 · fonte do print do Captions)
TRACK_LEG = -0.06  # letras coladas como no print do Captions (só entre letras; espaço entre palavras fica normal)
TAM_LEG = 118  # Sarah 30/09: 96 ficou pequeno demais
MAX_LINHA_LEG = 13

def fonte_legenda(tam):
    f = ImageFont.truetype(FONTE_LEG, tam)
    try:
        f.set_variation_by_axes([32, 750])  # calibrado lado a lado com o print do Captions (Sarah 30/09)
    except Exception:
        pass
    return f

def _texto_len(d, t, f, track=0.0):
    if not track:
        return d.textlength(t, font=f)
    return sum(d.textlength(c, font=f) + (0 if c == ' ' else track * f.size) for c in t)

def script(tam):
    return ImageFont.truetype(FONTE_SCRIPT, tam)

_CARIMBOS = {}
ESC_CARIMBO = [1.0]  # multiplicador do carimbo (gancho/CTA usam maior)
def carimbo(texto, tam):
    """Destaque Madu (playbook): palavra em Scripter CAIXA ALTA, branca, dentro de faixa de pincel Azul Noite
    (como "EQUILÍBRIO DO SONO" no deck). Devolve (imagem RGBA, deslocamento da linha de base)."""
    import random
    chave = (texto, tam)
    if chave in _CARIMBOS:
        return _CARIMBOS[chave]
    f = ImageFont.truetype(FONTE_ROTULO, int(tam * 1.18))
    t = texto.upper().strip()
    d0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    l, tp, r, b = d0.textbbox((0, 0), t, font=f, anchor="ls")
    tw, th = r - l, b - tp
    txt = Image.new("RGBA", (tw + 4, th + 4), (0, 0, 0, 0))
    ImageDraw.Draw(txt).text((2 - l, 2 - tp), t, font=f, fill=BRANCO + (255,), anchor="ls")
    txt = txt.resize((int(txt.width * 0.86), txt.height), Image.LANCZOS)  # a Scripter da Madu é mais estreita
    px, py = int(tam * 0.30), int(tam * 0.16)
    W2, H2 = txt.width + 2 * px, txt.height + 2 * py
    band = Image.new("RGBA", (W2 + 20, H2 + 20), (0, 0, 0, 0))
    rnd = random.Random(t)
    pts = []
    for k in range(0, W2 + 1, 18):
        pts.append((10 + k, 10 + rnd.randint(0, int(py * 0.6))))
    pts.append((10 + W2 + rnd.randint(2, 8), 10 + H2 // 2))
    for k in range(W2, -1, -18):
        pts.append((10 + k, 10 + H2 - rnd.randint(0, int(py * 0.6))))
    pts.append((10 - rnd.randint(2, 8), 10 + H2 // 2))
    ImageDraw.Draw(band).polygon(pts, fill=AZUL_NOITE + (255,))
    band.alpha_composite(txt, (10 + px, 10 + py))
    band = band.rotate(-2, resample=Image.BICUBIC, expand=True)
    base = 10 + py + (-tp + 2)  # linha de base do texto dentro da faixa
    _CARIMBOS[chave] = (band, base + (band.height - (H2 + 20)) // 2)
    return _CARIMBOS[chave]

def _medir(d, pecas, fb, fd, track=0.0):
    return sum(carimbo(t, int(fb.size * ESC_CARIMBO[0]))[0].width + fb.size * 0.10 if dest else _texto_len(d, t, fb, track) for t, dest in pecas)

def _linha_rica(d, x, base, pecas, fb, fd, cor, cor_dest, track=0.0, alvo=None):
    """Desenha na linha de base: texto normal em fb (com espaçamento opcional), *destaque* em fd (pincel)."""
    for t, dest in pecas:
        if dest:  # carimbo Scripter em faixa de pincel (a sombra não desenha a faixa)
            im, bl = carimbo(t, int(fb.size * ESC_CARIMBO[0]))
            x += fb.size * 0.05
            if alvo is not None:  # sem alvo = camada de sombra: a faixa não projeta sombra
                alvo.alpha_composite(im, (int(x), int(base - bl + fb.size * 0.02)))
            x += im.width + fb.size * 0.05
        elif not track:
            d.text((x, base), t, font=fb, fill=cor + (255,), anchor="ls")
            x += d.textlength(t, font=fb)
        else:
            for c in t:
                d.text((x, base), c, font=fb, fill=cor + (255,), anchor="ls")
                x += d.textlength(c, font=fb) + (0 if c == ' ' else track * fb.size)

def _bloco_rico(d, linhas, fb, fd, y_centro, x_centro=None, esp_extra=0.0, track=0.0):
    """Posições (x, linha de base) de cada linha, centralizadas; devolve também a caixa ocupada."""
    ab, db = fb.getmetrics(); ad, dd = fd.getmetrics()
    out, altura = [], 0
    for ln in linhas:
        pc = _pedacos(ln)
        tem = any(dest for _, dest in pc)
        asc = max(ab, int(ad * 0.78)) if tem else ab
        desc = max(db, int(dd * 0.6)) if tem else db
        out.append([pc, asc, desc, _medir(d, pc, fb, fd, track)])
        altura += asc + desc
    esp = int(ab * (0.12 + esp_extra))
    altura += esp * (len(linhas) - 1)
    y = y_centro - altura // 2
    larg = max(o[3] for o in out)
    cx = x_centro if x_centro is not None else W // 2
    pos = []
    for pc, asc, desc, w in out:
        pos.append((pc, cx - w / 2, y + asc, w))
        y += asc + desc + esp
    return pos, (cx - larg / 2, y_centro - altura // 2, cx + larg / 2, y_centro + altura // 2)

def desenhar_legenda(linhas, f, y_centro, img, contorno=0, escala=1.0):
    """Legenda estilo Captions (Madu 28/09): SEM contorno, sombra suave e larga, *palavra* em fonte de pincel.
    COR_LEGENDA=branco (sombra Azul Noite · destaque pêssego) | azul (brilho branco · destaque ameixa) | roxo."""
    from PIL import ImageFilter
    T = int(TAM_LEG * escala)  # escala = animação de entrada (pop estilo Captions)
    f = fonte_legenda(T); fd = script(int(T * 1.3)); tr = TRACK_LEG
    if COR_LEGENDA in ("azul", "roxo"):
        cor = AZUL_NOITE if COR_LEGENDA == "azul" else AMEIXA
        cor_dest = cor  # destaque = mesma cor escura, diferenciado pela fonte de pincel (contraste garantido)
        camadas = [((255, 255, 255, 150), 18), ((255, 255, 255, 110), 6)]  # só um clarão difuso atrás, sem contorno — segura a leitura sobre mão/cabelo
    else:
        # Madu 28/09: branca e limpa como no Captions — sem borda, sem fundo escuro; só sombra curta e leve
        # Sarah 30/09 (final): BRANCA, destaque só pela fonte (Damion branca). Sem contorno e sem clarão (o clarão
        # branco deixava o vídeo "muito claro"). Leitura garantida por sombra projetada escura, curta e macia.
        cor, cor_dest = BRANCO, BRANCO
        camadas = [((20, 22, 30, 90), 16), ((20, 22, 30, 200), 5)]
    ds0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    pos, caixa = _bloco_rico(ds0, linhas, f, fd, y_centro, esp_extra=-0.08, track=tr)
    if caixa[2] - caixa[0] > 940:  # linha longa: diminui a letra só o necessário para caber na área segura
        tam = int(T * 940 / (caixa[2] - caixa[0]))
        f = fonte_legenda(tam); fd = script(int(tam * 1.3))
        pos, caixa = _bloco_rico(ds0, linhas, f, fd, y_centro, esp_extra=-0.08, track=tr)
    for cor_s, blur in camadas:  # sombra em duas camadas: larga (atmosfera) + curta (recorte)
        tmp = Image.new("RGBA", img.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(tmp)
        for pc, x, base, _w in pos:
            _linha_rica(ds, x, base + 4, pc, f, fd, cor_s[:3], cor_s[:3], tr)
        tmp.putalpha(tmp.getchannel("A").point(lambda v: v * cor_s[3] // 255))
        img.alpha_composite(tmp.filter(ImageFilter.GaussianBlur(blur)))
    d = ImageDraw.Draw(img)
    for pc, x, base, _w in pos:
        _linha_rica(d, x, base, pc, f, fd, cor, cor_dest, tr, alvo=img)

def desenhar_gancho(linhas, f, y_centro, img):
    """Gancho / CTA no visual da Madu (deck da Consultoria): cartão branco arredondado, Raleway 600 em Azul Noite,
    palavra-chave *assim* em Scripter CAIXA ALTA na faixa de pincel Azul Noite."""
    from PIL import ImageFilter
    d = ImageDraw.Draw(img)
    fd = script(int(f.size * 1.4))
    ESC_CARIMBO[0] = 1.45
    pos, (x0, y0, x1, y1) = _bloco_rico(d, linhas, f, fd, y_centro, esp_extra=0.22)
    px, py = 50, 38
    sombra = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle([x0 - px, y0 - py + 10, x1 + px, y1 + py + 10], radius=40, fill=AZUL_NOITE + (70,))
    img.alpha_composite(sombra.filter(ImageFilter.GaussianBlur(18)))
    d.rounded_rectangle([x0 - px, y0 - py, x1 + px, y1 + py], radius=40, fill=BRANCO + (246,))
    for pc, x, base, _w in pos:
        _linha_rica(d, x, base, pc, f, fd, AZUL_NOITE, AZUL_NOITE, alvo=img)
    ESC_CARIMBO[0] = 1.0

def desenhar_cartela(texto, f, y_centro, img, cor_num=AZUL_DRUMMOND):
    """Cartela: pílula branca + círculo numerado · o nome do item sai em fonte de pincel (Madu 28/09).
    '3 · Brinquedos com muita luz' -> círculo '3' + 'Brinquedos com muita luz' em pincel Azul Noite.
    Sem número (CTA): Raleway com *destaque* em pincel ('Comenta *NOITE*')."""
    d = ImageDraw.Draw(img)
    num, corpo = None, texto
    if "·" in texto and texto.split("·", 1)[0].strip().isdigit():
        num, corpo = texto.split("·", 1)[0].strip(), texto.split("·", 1)[1].strip()
    if num and "*" not in corpo:
        corpo = "*" + corpo + "*"  # item inteiro em pincel
    fb = f; fd = script(int(f.size * 1.2))
    linhas = quebrar_titulo(corpo.replace("*", "\x00"), 22)
    linhas = [ln.replace("\x00", "*") for ln in linhas]
    # reabre/fecha o * quando a quebra caiu no meio do destaque
    fix, aberto = [], False
    for ln in linhas:
        l2 = ("*" if aberto else "") + ln
        aberto = l2.count("*") % 2 == 1
        fix.append(l2 + ("*" if aberto else ""))
    linhas = fix
    lh_ref = fb.getmetrics()[0] + fb.getmetrics()[1]
    diam = max(lh_ref + 30, 104) if num else 0
    gap = 24 if num else 0
    px, py = 40, 24
    pos, (bx0, by0, bx1, by1) = _bloco_rico(d, linhas, fb, fd, y_centro)
    larg = bx1 - bx0
    total = diam + gap + larg + 2 * px
    x0 = (W - total) / 2
    caixa_h = max(by1 - by0 + 2 * py, diam + 16)
    d.rounded_rectangle([x0, y_centro - caixa_h / 2, x0 + total, y_centro + caixa_h / 2],
                        radius=int(min(caixa_h / 2, 48)), fill=BRANCO + (244,))
    if num:
        cx, cy = x0 + px + diam / 2 - 12, y_centro
        d.ellipse([cx - diam / 2, cy - diam / 2, cx + diam / 2, cy + diam / 2], fill=cor_num + (255,))
        fn = fonte(int(diam * 0.52))
        d.text((cx, cy), num, font=fn, fill=BRANCO + (255,), anchor="mm")
    desloc = (x0 + px + diam + gap - (12 if num else 0)) - bx0
    for pc, x, base, w in pos:
        _linha_rica(d, x - (larg - w) / 2 + desloc, base, pc, fb, fd, AZUL_NOITE, AZUL_NOITE if num else AZUL_DRUMMOND)
W, H = 1080, 1920
MAX_LINHA = 14  # Madu: blocos curtos (estilo Captions) para a letra continuar grande
MAX_DUR = 3.0
FRACAS = set("a o as os ao aos à às de da do das dos em no na nos nas e que para pra por com um uma "
             "se nesse nessa esse essa seu sua nosso nossa mais não é mas porque quando".split())

def transcrever(video):
    from faster_whisper import WhisperModel
    tmp = tempfile.mktemp(suffix=".wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-vn", "-ar", "16000",
                    "-ac", "1", tmp], check=True)
    m = WhisperModel("medium", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(tmp, language="pt", word_timestamps=True, beam_size=5)
    return [{"w": w.word.strip(), "s": w.start, "e": w.end} for s in segs for w in s.words]

def montar_blocos(pal):
    blocos, atual = [], []
    for i, w in enumerate(pal):
        if atual:
            texto = " ".join(x["w"] for x in atual + [w])
            gap = w["s"] - atual[-1]["e"]
            fim_frase = atual[-1]["w"][-1:] in ".?!"
            virgula = atual[-1]["w"][-1:] in ",;:" and len(" ".join(x["w"] for x in atual)) >= 12
            longo = len(texto) > 2 * MAX_LINHA
            demorado = w["e"] - atual[0]["s"] > MAX_DUR
            fecha_frase = w["w"][-1:] in ".?!," and w["e"] - atual[0]["s"] <= MAX_DUR + 0.8
            forcado = longo or (demorado and not fecha_frase)
            if gap > 0.35 or fim_frase or virgula or forcado:
                resto = []
                if forcado and not fim_frase and not virgula:
                    # não terminar legenda em palavra fraca (preposição, artigo, conjunção)
                    while len(atual) > 1 and atual[-1]["w"].lower().strip(".,;:!?") in FRACAS:
                        resto.insert(0, atual.pop())
                blocos.append(atual)
                atual = resto
        atual.append(w)
    if atual:
        blocos.append(atual)
    # legenda-relâmpago (<0,6s) se junta à anterior quando cabe em 2 linhas
    juntos = []
    for b in blocos:
        if juntos and (b[-1]["e"] - b[0]["s"] < 0.6) and \
                len(" ".join(x["w"] for x in juntos[-1] + b)) <= 2 * MAX_LINHA + 8:
            juntos[-1] = juntos[-1] + b
        else:
            juntos.append(b)
    blocos = juntos
    out = []
    for k, b in enumerate(blocos):
        ini = b[0]["s"]
        fim = b[-1]["e"] + 0.15
        if k + 1 < len(blocos) and blocos[k + 1][0]["s"] - b[-1]["e"] < 0.5:
            fim = blocos[k + 1][0]["s"]
        t = " ".join(x["w"] for x in b).rstrip(".,;:")
        if k == 0 or blocos[k - 1][-1]["w"][-1:] in ".?!":
            t = t[:1].upper() + t[1:]
        out.append({"i": round(ini, 3), "f": round(fim, 3), "t": t})
    return out

def quebrar(t, maxc=MAX_LINHA):
    if len(t) <= maxc:
        return [t]
    pal = t.split()
    melhor, dif = [t], 10**9
    for k in range(1, len(pal)):
        a, b = " ".join(pal[:k]), " ".join(pal[k:])
        d = abs(len(a) - len(b)) + (100 if max(len(a), len(b)) > maxc + 6 else 0)
        if d < dif:
            melhor, dif = [a, b], d
    return melhor

def quebrar_titulo(t, maxc=22):
    """Título do topo: quebra em quantas linhas precisar (até ~22 caracteres cada) para nunca sair da tela.
    '|' força a quebra (evitar viúva: "Ninguém dorme a noite *inteira*.|Nem o seu bebê.")."""
    if "|" in t:
        return [p.strip() for p in t.split("|") if p.strip()]
    linhas, atual = [], ""
    for p in t.split():
        if atual and len(atual) + 1 + len(p) > maxc:
            linhas.append(atual); atual = p
        else:
            atual = f"{atual} {p}".strip()
    if atual:
        linhas.append(atual)
    return linhas

def gravar(video, blocos, saida, estilo, titulo, y_titulo=400, y_cartela=1350,
           titulo_ate=None, cartelas=None, y_legenda=None, pilar=None):
    """estilo 'cartela' (Sarah, 24/09): sem legenda; cada bloco vira um texto curto em caixa escura
    (gancho, itens de lista, CTA), posicionado longe do rosto. y_titulo move o gancho fixo (ex.: 960 = meio).
    titulo_ate: o gancho some depois de N segundos (Sarah, 24/09: gancho só nos primeiros 5s).
    cartelas: lista {i,f,t} desenhada em caixa em y_cartela JUNTO com a legenda (destaque dos pontos: "1 · LUZ...").
    y_legenda: altura da legenda (padrão 1340 instagram / 1300 tiktok)."""
    tmp = tempfile.mkdtemp()
    f_leg = fonte(70 if estilo == "instagram" else 62)
    f_tit = fonte(70)
    f_car = fonte(58)
    y_leg = y_legenda or (1340 if estilo == "instagram" else 1300)
    cor_num = PILARES.get(pilar, AZUL_DRUMMOND)
    cartelas = cartelas or []
    if estilo == "cartela":
        cartelas, blocos = blocos, []

    dur = float(subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                                "-of", "csv=p=0", video], capture_output=True, text=True).stdout)
    fim_tit = dur if titulo_ate is None else titulo_ate
    cortes = {0.0, dur}
    if titulo:
        cortes.add(min(fim_tit, dur))
    for x in blocos + cartelas:
        cortes.update((max(0.0, min(x["i"], dur)), max(0.0, min(x["f"], dur))))
    for x in blocos:  # pop de entrada: 2 quadros menores/maiores antes de assentar
        cortes.update(min(dur, x["i"] + k / 30) for k in (1, 2, 3))
    cortes = sorted(cortes)

    def ativo(lista, m):
        return next((x for x in lista if x["i"] <= m < x["f"]), None)

    seq, cache = [], {}
    for a, b in zip(cortes, cortes[1:]):
        if b - a < 0.001:
            continue
        m = (a + b) / 2
        tit = titulo if (titulo and m < fim_tit) else None
        car, leg = ativo(cartelas, m), ativo(blocos, m)
        esc = 1.0
        if leg:
            dt = m - leg["i"]
            esc = 0.86 if dt < 1 / 30 else (1.07 if dt < 2 / 30 else (1.02 if dt < 3 / 30 else 1.0))
        chave = (tit, car and car["t"], leg and leg["t"], esc)
        if chave not in cache:
            img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            if tit:  # nunca sobre o rosto
                desenhar_gancho(quebrar_titulo(tit, 24), f_tit, y_titulo, img)
            if car and car["t"].startswith(">"):  # chamada grande (CTA): mesmo visual do gancho
                desenhar_gancho(quebrar_titulo(car["t"][1:], 24), f_tit, y_cartela, img)
            elif car:
                desenhar_cartela(car["t"], f_car, y_cartela, img, cor_num=cor_num)
            if leg:
                # Instagram em minúsculas, mas palavra-chave em CAIXA ALTA continua (ex.: "comenta NOITE")
                # nome próprio (Maiúscula no meio da frase ou da lista PROPRIOS) também fica
                pals = leg["t"].split()
                txt = " ".join(p if ((k > 0 and p.strip("*")[:1].isupper()) or p.strip("*.,;:!?") in PROPRIOS
                                     or (p.strip(".,;:!?*").isupper() and len(p.strip(".,;:!?*")) > 1)) else p.lower()
                               for k, p in enumerate(pals)) if estilo == "instagram" else leg["t"]
                linhas, aberto = [], False
                for ln in quebrar(txt, MAX_LINHA_LEG):
                    l2 = ("*" if aberto else "") + ln
                    aberto = l2.count("*") % 2 == 1
                    linhas.append(l2 + ("*" if aberto else ""))
                desenhar_legenda(linhas, f_leg, y_leg, img, escala=esc)
            f = os.path.join(tmp, f"l{len(cache):04d}.png")
            img.save(f)
            cache[chave] = f
        seq.append((cache[chave], b - a))
    lst = os.path.join(tmp, "seq.txt")
    with open(lst, "w") as fh:
        for f, d in seq:
            fh.write(f"file '{f}'\nduration {max(d, 0.034):.3f}\n")
        fh.write(f"file '{seq[-1][0]}'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video,
                    "-f", "concat", "-safe", "0", "-i", lst,
                    "-filter_complex", "[1:v]fps=30,format=rgba[l];[0:v][l]overlay=0:0:eof_action=pass:format=auto[v]",
                    "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", saida], check=True)
    srt = os.path.splitext(saida)[0] + ".srt"
    def ts(x):
        return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int(round(x%1*1000)):03d}"
    with open(srt, "w") as fh:
        for k, b in enumerate(blocos, 1):
            fh.write(f"{k}\n{ts(b['i'])} --> {ts(b['f'])}\n{b['t'].replace('*', '')}\n\n")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=["gerar", "remontar", "gravar"])
    ap.add_argument("--corrigir", action="append", default=[],
                    help='correção de grafia "errado=certo" (repetível), aplicada nas palavras')
    ap.add_argument("video"); ap.add_argument("legendas")
    ap.add_argument("saida", nargs="?")
    ap.add_argument("--estilo", default="instagram", choices=["instagram", "tiktok", "cartela"])
    ap.add_argument("--titulo", default="")
    ap.add_argument("--y-titulo", type=int, default=400, help="altura do centro do gancho fixo (960 = meio da tela)")
    ap.add_argument("--y-cartela", type=int, default=1350, help="altura das cartelas (estilo cartela ou --cartelas)")
    ap.add_argument("--titulo-ate", type=float, default=None, help="gancho some depois de N segundos (ex.: 5)")
    ap.add_argument("--cartelas", default="", help="JSON com blocos {i,f,t} de destaque exibidos junto com a legenda")
    ap.add_argument("--pilar", type=int, default=None, choices=[1, 2, 3, 4],
                    help="cor do círculo numerado = cor do pilar (1 Ritmo · 2 Ninho · 3 Afeto · 4 Hábitos); padrão Azul Drummond")
    ap.add_argument("--y-legenda", type=int, default=None, help="altura da legenda (padrão 1340 IG / 1300 TikTok)")
    a = ap.parse_args()
    if a.acao in ("gerar", "remontar"):
        pal = transcrever(a.video) if a.acao == "gerar" else json.load(open(a.legendas))["palavras"]
        for c in a.corrigir:
            errado, certo = c.split("=", 1)
            alvo = errado.lower().split()
            k = 0
            while k <= len(pal) - len(alvo):
                trecho = [w["w"].strip(".,;:!?").lower() for w in pal[k:k + len(alvo)]]
                if trecho == alvo:
                    ult = pal[k + len(alvo) - 1]
                    pont = ult["w"][len(ult["w"].rstrip(".,;:!?")):]
                    pal[k]["w"], pal[k]["e"] = certo + pont, ult["e"]
                    del pal[k + 1:k + len(alvo)]
                k += 1
        json.dump({"palavras": pal, "blocos": montar_blocos(pal)}, open(a.legendas, "w"),
                  ensure_ascii=False, indent=1)
        for b in json.load(open(a.legendas))["blocos"]:
            print(f"{b['i']:6.2f}-{b['f']:6.2f}  {b['t']}")
    else:
        gravar(a.video, json.load(open(a.legendas))["blocos"], a.saida, a.estilo, a.titulo,
               y_titulo=a.y_titulo, y_cartela=a.y_cartela, titulo_ate=a.titulo_ate,
               cartelas=json.load(open(a.cartelas))["blocos"] if a.cartelas else None,
               y_legenda=a.y_legenda, pilar=a.pilar)
        print("ok", a.saida)
