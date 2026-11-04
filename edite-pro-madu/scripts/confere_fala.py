"""Confere se nenhuma palavra foi cortada: transcreve o áudio exportado e compara com o texto das legendas.
Uso: python3 confere_fala.py <audio.wav> <dados-reel.json> <velocidade>"""
import sys, json, re, unicodedata, difflib
from faster_whisper import WhisperModel
def norm(s):
    s = unicodedata.normalize('NFKD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]', '', s)
audio, dados, vel = sys.argv[1], sys.argv[2], float(sys.argv[3])
d = json.load(open(dados))
esperado = [(norm(p['texto']), p['inicio'] / vel) for g in d['grupos'] for p in g['palavras']]
esperado = [(w, t) for w0, t in esperado for w in w0.split()]
m = WhisperModel('small', device='cpu', compute_type='int8')
segs, _ = m.transcribe(audio, language='pt', word_timestamps=True, initial_prompt=' '.join(w for w, _ in esperado[:60]))
ouvido = [(norm(w.word).strip(), w.start, w.end) for s in segs for w in s.words if norm(w.word).strip()]
a = [w for w, _ in esperado]; b = [w for w, _, _ in ouvido]
cortes = [c['saida'] / vel for c in d['cortes'][1:]]
print('palavras esperadas', len(a), '· ouvidas', len(b))
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op == 'equal': continue
    t = esperado[i1][1] if i1 < len(esperado) else ouvido[j1][1]
    perto = min(cortes, key=lambda c: abs(c - t)); flag = ' ← PERTO DE CORTE' if abs(perto - t) < 0.6 else ''
    print(f"{t:6.2f}s {op:8s} esperado: {' '.join(a[i1:i2])!r:40s} ouvido: {' '.join(b[j1:j2])!r}{flag}")
