"""Monta só o áudio dos cortes (1,3×) e mede buracos entre palavras + transcrição — conferência rápida antes do render."""
import json, subprocess, sys
from faster_whisper import WhisperModel
dados, P = json.load(open(sys.argv[1])), '../public/'
args, fil = [], []
for i, c in enumerate(dados['cortes']):
    args += ['-ss', str(c['de']), '-to', str(c['ate']), '-i', P + c['video']]
    fil.append(f'[{i}:a]')
fc = ''.join(fil) + f"concat=n={len(fil)}:v=0:a=1,atempo=1.3[a]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', *args, '-filter_complex', fc, '-map', '[a]', '-ac', '1', '-ar', '16000', '/tmp/chk.wav'])
m = WhisperModel('small', device='cpu', compute_type='int8')
segs, info = m.transcribe('/tmp/chk.wav', language='pt', word_timestamps=True)
ws = [w for s in segs for w in s.words]
gaps = [(round(ws[i+1].start - ws[i].end, 2), ws[i].word.strip() + '|' + ws[i+1].word.strip()) for i in range(len(ws) - 1) if ws[i+1].start - ws[i].end > 0.2]
print(round(info.duration, 1), 's · buracos >0,2s:', len(gaps), gaps)
print(' '.join(w.word.strip() for w in ws))
