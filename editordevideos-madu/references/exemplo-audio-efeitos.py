import subprocess
import json
JJ=json.load(open('trabalho/janelas.json')); DUR=JJ['DUR']+3.0
tel=tuple(JJ['tel'])                      # "e a orientação dele foi colocá-la no berço... até cansar e dormir" = voz de memória
eco=[tuple(x) for x in JJ['eco']]     # "por um único motivo" · "no momento certo"
whoosh=[v[0] for v in JJ['J'].values()]
g=lambda iv:'+'.join(f'between(t,{a},{b})' for a,b in iv)
fc=[f"[0:a]apad=pad_dur=4,asplit=3[d][t][e]",
    f"[d]volume='if({g([tel])},0,1)':eval=frame[dry]",
    f"[t]highpass=f=450,lowpass=f=2800,acompressor=threshold=0.1:ratio=4,volume='if({g([tel])},1.35,0)':eval=frame[tel]",
    f"[e]aecho=0:1:180|360|540:0.45|0.28|0.15,volume='if({g([(a,b+0.9) for a,b in eco])},1,0)':eval=frame[eco]"]
# whoosh sintetizado: ruído rosa filtrado com subida e descida
ws=[]
for k,t in enumerate(whoosh):
    fc.append(f"anoisesrc=color=pink:d=0.5:a=0.6,bandpass=f=1800:width_type=o:w=2,afade=t=in:d=0.28:curve=exp,afade=t=out:st=0.28:d=0.22,volume=0.22,adelay={int((t-0.3)*1000)}|{int((t-0.3)*1000)}[w{k}]")
    ws.append(f"[w{k}]")
fc.append(f"[dry][tel][eco]{''.join(ws)}amix=inputs={3+len(ws)}:normalize=0:duration=first,atrim=0:{DUR},loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','00-limpo.mp4','-filter_complex',';'.join(fc),'-map','[a]','-ac','2','-ar','48000','-c:a','aac','-b:a','192k','trabalho/audio-fx.m4a'],check=True)
print('audio ok')
