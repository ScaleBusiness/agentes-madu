"""Cortes pela FALA (Sarah 20/10: "você não removeu o silêncio… olha para o lado, fica em silêncio, ou só respira — isso é regra").
A régua sensível (voz-<take>.npy) conta respiração como voz e unia pausas de até 0,30 s; aqui cada trecho é a própria palavra:
início e fim de cada palavra (Whisper medium) ajustados pelo volume real (> -45 dB, respiração fica de fora), folga curta
para não comer sílaba, e só se juntam palavras separadas por menos de JUNTA. Tudo o que não é palavra sai do vídeo.
Uso: from cortes_fala import cortes_por_fala; cortes = cortes_por_fala(TRECHOS, ws_por_take, caminho_do_take)"""
import subprocess
import numpy as np

SR, PASSO = 16000, 0.01
LIMIAR_DB = -45      # início da fala (sílaba fraca protegida também pelo início do Whisper)
LIMIAR_FIM_DB = -36  # fim da palavra: a respiração da Madu entre frases chega a -40 dB e prendia meio segundo (20/10)
BUSCA_ANTES, BUSCA_DEPOIS = 0.25, 0.12  # 20/10: o Whisper marcou "Comente" 0,2 s atrasado e o "Co" sumia
FOLGA_ANTES, FOLGA_DEPOIS = 0.03, 0.03
JUNTA = 0.10         # pausa menor que isto entre palavras fica (respiro natural de articulação); maior sai


def volume_db(mp4, agudo=False):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    n = int(PASSO * SR)
    k = len(x) // n
    seg = x[:k * n].reshape(k, n)
    db = 20 * np.log10(np.sqrt((seg ** 2).mean(axis=1)) + 1e-9)
    if not agudo:
        return db
    # energia em 3,5–8 kHz: o "s" de "fase" e o "c" de "comente" são fracos no volume geral mas fortes aqui
    F = np.abs(np.fft.rfft(seg * np.hanning(n), axis=1)); f = np.fft.rfftfreq(n, 1 / SR); banda = (f > 3500) & (f < 8000)
    hf = 20 * np.log10(np.sqrt((F[:, banda] ** 2).mean(axis=1)) / n + 1e-12)
    return db, hf


def ajusta(db, s, e):
    """primeiro e último quadro com fala de verdade perto da palavra (o Whisper às vezes marca 0,0 ou corta a cauda)"""
    a, b = int(max(0, s - BUSCA_ANTES) / PASSO), int(min(len(db) * PASSO, e) / PASSO)
    on = np.where(db[a:max(b, a + 1)] > LIMIAR_DB)[0]
    ini = (a + on[0]) * PASSO if len(on) else s
    # sílaba fraca no começo ("a-tender") fica abaixo do limiar: só trocamos o início do Whisper pelo volume
    # quando ele está claramente no silêncio (Whisper às vezes marca 0,0); 20/10: "atender" virou "tender"
    if ini - s <= 0.25:
        ini = min(ini, s)
    a2, b2 = int(max(s, ini) / PASSO), int((e + BUSCA_DEPOIS) / PASSO)
    on2 = np.where(db[a2:b2] > LIMIAR_FIM_DB)[0]
    fim = (a2 + on2[-1] + 1) * PASSO if len(on2) else e
    # o fim nunca fica antes do fim marcado pelo Whisper (o "s" final é fraco no volume: "fase" virava "fada", 20/10);
    # a pausa que sobrar depois sai na passada final (aperta)
    return ini, max(fim, e, ini + 0.08)


SILENCIO_DB, SILENCIO_HF, SILENCIO_MAX, MARGEM = -46, 0, 0.30, 0.12  # 21/10: margem 0,12 (o "C" de "Comente" começa 0,06 s antes do volume subir)
PONTA_MAX = 0.30  # silêncio na ponta do corte só sai se for longo (respiração antes da 1ª palavra); "s" final e consoante inicial (~0,15 s) ficam  # 20/10: o "s" de "fase" fica em -41..-47 dB; pausa/respiração abaixo
USA_MASCARA_PALAVRA = False  # testado 20/10: o Whisper estica palavras pela pausa e a máscara protegia silêncio


def aperta(db, hf, a, b, palavra=None):
    """passada final: dentro do corte, todo trecho abaixo de SILENCIO_DB por mais de SILENCIO_MAX sai (fica MARGEM de cada lado);
    pontas quietas também saem. Sarah 20/10: nenhuma pausa/respiração sobrando entre as frases."""
    i0, i1 = int(a / PASSO), min(len(db), int(b / PASSO))
    quieto = (db[i0:i1] < SILENCIO_DB) & (hf[i0:i1] < SILENCIO_HF)
    if palavra is not None:  # o que está dentro de uma palavra ("s" final, sílaba fraca) nunca conta como silêncio
        quieto &= ~palavra[i0:i1]
    partes, ini, k = [], a, 0
    while k < len(quieto):
        if quieto[k]:
            j = k
            while j < len(quieto) and quieto[j]:
                j += 1
            t0, t1 = (i0 + k) * PASSO, (i0 + j) * PASSO
            na_ponta = k == 0 or j == len(quieto)
            # só pausas no MEIO do corte saem; as pontas já respeitam o fim/início da palavra (21/10: "mudanças" perdia o "s")
            if (t1 - t0) > (PONTA_MAX if na_ponta else SILENCIO_MAX):
                if k > 0:
                    partes.append([ini, min(b, t0 + MARGEM)])
                ini = max(a, t1 - MARGEM) if j < len(quieto) else None
            k = j
        else:
            k += 1
    if ini is not None:
        partes.append([ini, b])
    return [p for p in partes if p[1] - p[0] > 0.06] or [[a, b]]


def cortes_por_fala(trechos, ws_por_take, caminho):
    cortes = []
    for take, de0, ate0 in trechos:
        db, hf = volume_db(caminho(take), agudo=True)
        palavra = np.zeros(len(db), dtype=bool)
        for w in ws_por_take[take]:
            if de0 - 1 <= w['s'] < ate0 + 1:
                palavra[int(w['s'] / PASSO):int(w['e'] / PASSO) + 1] = True
        spans = []
        for w in ws_por_take[take]:
            if not (de0 <= w['s'] < ate0):
                continue
            ini, fim = ajusta(db, w['s'], w['e'])
            c = [max(de0, ini - FOLGA_ANTES), min(ate0, fim + FOLGA_DEPOIS)]
            if spans and c[0] - spans[-1][1] < JUNTA:
                spans[-1][1] = max(spans[-1][1], c[1])
            else:
                spans.append(c)
        finos = [p for a, b in spans for p in aperta(db, hf, a, b, palavra if USA_MASCARA_PALAVRA else None)]
        cortes += [{'take': take, 'de': round(a, 3), 'ate': round(b, 3)} for a, b in finos]
    return cortes
