"""Edição dinâmica estilo Captions: zoom de corte por frase + punch nas palavras-destaque (só tela cheia)."""
import json,subprocess
bl=json.load(open('trabalho/legendas.json'))['blocos']
dest=[b for b in json.load(open('trabalho/leg-cheia.json'))['blocos']+json.load(open('trabalho/leg-dividida.json'))['blocos'] if '*' in b['t']]
DUR=float(subprocess.run(['ffprobe','-v','quiet','-show_entries','format=duration','-of','csv=p=0','00-limpo.mp4'],capture_output=True,text=True).stdout)
# nível por frase: alterna 1.00 / 1.10 a cada início de frase (bloco que começa com maiúscula)
ivs=[]; nivel=1.0; ini=0.0
for b in bl:
    if b['t'][:1].isupper() and b['i']-ini>1.5:
        ivs.append((ini,b['i'],nivel)); ini=b['i']; nivel=1.10 if nivel==1.0 else 1.0
ivs.append((ini,DUR+1,nivel))
# punch nas palavras-destaque: 1.18 durante o bloco
for b in dest: ivs.append((b['i'],b['f'],1.18))
ivs.sort(key=lambda x:(-x[2]==1.18, x[0]))
# expressão: punches têm prioridade
punch=[x for x in ivs if x[2]==1.18]; base=[x for x in ivs if x[2]!=1.18]
e='1'
for a,b,z in reversed(base): e=f"if(between(it,{a:.2f},{b:.2f}),{z},{e})"
for a,b,z in reversed(punch): e=f"if(between(it,{a:.2f},{b:.2f}),{z},{e})"
vf=f"fps=30,zoompan=z='{e}':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*0.28':d=1:s=1080x1920:fps=30,format=yuv420p"
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','00-limpo.mp4','-vf',vf,'-an','-c:v','libx264','-preset','medium','-crf','17','trabalho/zoom.mp4'],check=True)
print('zoom ok', len(base),'frases', len(punch),'punches')
