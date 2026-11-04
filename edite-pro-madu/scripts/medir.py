"""Régua sensível da Edite Pro (volume > -48 dB OU agudo 3-10 kHz > -58 dB) aplicada ao take inteiro da Madu."""
import subprocess, numpy as np, sys, json, os
SR = 32000; PASSO = 0.01
AQUI = os.path.dirname(os.path.abspath(__file__))
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(AQUI, '../public/madu-acolher/video/take-8651.mp4'),
                      '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
x = np.frombuffer(raw, dtype=np.float32)
n = int(PASSO * SR); win = np.hanning(n); f = np.fft.rfftfreq(n, 1 / SR); band = (f > 3000) & (f < 10000)
v = []
for i in range(0, len(x) - n, n):
    seg = x[i:i + n]
    geral = 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9)
    F = np.abs(np.fft.rfft(seg * win)); agudo = 20 * np.log10(np.sqrt(np.mean(F[band] ** 2)) / n + 1e-12)
    v.append(geral > -48 or agudo > -58)
v = np.array(v); np.save(os.path.join(AQUI, 'voz.npy'), v)
gap = float(sys.argv[1]) if len(sys.argv) > 1 else 0.25
runs, a, last = [], None, None
for k, on in enumerate(v):
    t = k * PASSO
    if on:
        if a is None: a = t
        elif t - last > gap: runs.append((a, last + PASSO)); a = t
        last = t
if a is not None: runs.append((a, last + PASSO))
for r in runs: print(f'{r[0]:6.2f} {r[1]:6.2f}')
