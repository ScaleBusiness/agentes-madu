import json,subprocess
JJ=json.load(open('trabalho/janelas.json')); J=JJ['J']; tp=JJ['tp']; tp['hábitos']=tp['habitos']
cenas=[('cenas/cena1-6849011.mp4',*J['pediatra'],0.5),('cenas/cena2-6466354.mp4',*J['busca'],0.5),
       ('cenas/cena3-7558921.mp4',*J['estudo'],0.5),('cenas/cena4-7280809.mp4',*J['maes'],0.30),
       ('cenas/cena5-7280832.mp4',*J['zona'],0.35)]
rodas=[('trabalho/roda0.png',J['roda'][0],tp['ritmo']),('trabalho/roda1.png',tp['ritmo'],tp['ninho']),
       ('trabalho/roda2.png',tp['ninho'],tp['afeto']),('trabalho/roda3.png',tp['afeto'],tp['hábitos']),
       ('trabalho/roda4.png',tp['hábitos'],J['roda'][1])]
DUR=float(subprocess.run(['ffprobe','-v','quiet','-show_entries','format=duration','-of','csv=p=0','00-limpo.mp4'],capture_output=True,text=True).stdout)
args=['ffmpeg','-y','-loglevel','error','-i','trabalho/zoom.mp4','-i','00-limpo.mp4']
for f,*_ in cenas: args+=['-i',f]
for f,*_ in rodas: args+=['-loop','1','-t',f'{DUR:.2f}','-i',f]
fc=[f'[0:v]fps=30[base]','[1:v]fps=30,crop=1080:960:0:40[madu]',
    f'color=c=black:s=1080x1920:r=30:d={DUR:.2f}[blk]','[blk][madu]overlay=0:960[s0]']
k=0; janelas=[]
for i,(f,a,b,yc) in enumerate(cenas,2):
    L=b-a+0.2
    fc.append(f'[{i}:v]trim=0:{L:.2f},setpts=PTS-STARTPTS+{a}/TB,fps=30,scale=1080:960:force_original_aspect_ratio=increase,crop=1080:960:(iw-1080)/2:(ih-960)*{yc}[c{i}]')
    fc.append(f"[s{k}][c{i}]overlay=0:0:eof_action=pass:enable='between(t,{a},{b})'[s{k+1}]"); k+=1; janelas.append((a,b))
for j,(f,a,b) in enumerate(rodas):
    idx=2+len(cenas)+j
    fc.append(f'[{idx}:v]fps=30,format=yuv420p[r{j}]')
    fc.append(f"[s{k}][r{j}]overlay=0:0:enable='between(t,{a},{b})'[s{k+1}]"); k+=1
janelas.append(tuple(J['roda']))
en='+'.join(f'between(t,{a},{b})' for a,b in janelas)
fc.append(f"[base][s{k}]overlay=0:0:enable='{en}'[v]")
args+=['-filter_complex',';'.join(fc),'-map','[v]','-map','1:a','-c:a','copy','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-t',f'{DUR:.2f}','trabalho/composto.mp4']
subprocess.run(args,check=True); print('composto ok')
