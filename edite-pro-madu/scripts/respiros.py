"""Mede fala e silêncio de cada corte com régua sensível (pega S, F, X: energia aguda) para tirar só respiro.
Uso: python3 respiros.py   (lê CORTES_TEXTO de montar_legendas.py)"""
import subprocess, numpy as np, importlib.util, os
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('m', os.path.join(AQUI, 'montar_legendas.py')); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
SR = 32000; PASSO = 0.01
def carrega(take):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(AQUI, f'../public/reel-playbook/video/take-{take}.mp4'),
                          '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32)
def voz(x, t0, t1):
    """True por janela de 10 ms se há voz: volume geral > -48 dB OU energia aguda (3-10 kHz) > -58 dB."""
    n = int(PASSO * SR); out = []
    for t in np.arange(t0, t1, PASSO):
        seg = x[int(t * SR):int(t * SR) + n]
        if len(seg) < n: out.append(False); continue
        geral = 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9)
        F = np.abs(np.fft.rfft(seg * np.hanning(n))); f = np.fft.rfftfreq(n, 1 / SR)
        agudo = 20 * np.log10(np.sqrt(np.mean(F[(f > 3000) & (f < 10000)] ** 2)) / n + 1e-12)
        out.append(geral > -48 or agudo > -58)
    return np.array(out)
if __name__ == '__main__':
    cache = {}
    for k, (tk, de, ate) in enumerate(m.CORTES_TEXTO):
        x = cache.setdefault(tk, carrega(tk))
        v = voz(x, de, ate); ts = de + np.arange(len(v)) * PASSO
        on = ts[v]; ini, fim = (on[0], on[-1] + PASSO) if len(on) else (None, None)
        # silêncios internos > 0,30 s
        sil, a = [], None
        for t, vv in zip(ts, v):
            if not vv and a is None: a = t
            if vv and a is not None:
                if t - a > 0.30 and a > ini: sil.append((round(a, 2), round(t, 2)))
                a = None
        print(f"corte {k:2d} {tk} {de:6.2f}-{ate:6.2f} | voz {ini:.2f}-{fim:.2f} | folga início {ini-de:.2f} fim {ate-fim:.2f} | respiros internos: {sil}")
