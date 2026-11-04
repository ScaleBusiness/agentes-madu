"""Narrativa do Método: monta legendas, janelas de tela dividida, zoom, áudio e composição a partir do corte atual."""
import json,re,subprocess,sys
L=json.load(open('trabalho/legendas.json')); P=L['palavras']
norm=lambda s: re.sub(r'[^\wà-ú]','',s.lower())
W=[norm(w['w']) for w in P]
def t(frase,fim=False,depois=0):
    a=[norm(x) for x in frase.split()]
    for i in range(len(P)):
        if P[i]['s']>=depois and W[i:i+len(a)]==a:
            return round(P[i+len(a)-1]['e'] if fim else P[i]['s'],2)
    sys.exit('NÃO ACHEI: '+frase)
DUR=float(subprocess.run(['ffprobe','-v','quiet','-show_entries','format=duration','-of','csv=p=0','00-limpo.mp4'],capture_output=True,text=True).stdout)
J={}
J['pediatra']=(t('e a orientação dele foi'), t('até ela cansar e dormir',True)+0.1)
J['busca']=(t('Como muitas mães'), t('desandava de novo',True)+0.1)
J['estudo']=(t('Decidi me especializar'), t('e neurociência',True)+0.1)
J['maes']=(t('Mães que chegavam'), t('o suficiente',True)+0.1)
J['roda']=(t('que nasceu o método'), t('sono positivos',True)+0.1) if False else None
ini_roda=t('Eu começo entendendo'); fim_roda=t('hábitos positivos',True)+0.1
J['roda']=(ini_roda,fim_roda)
J['zona']=(fim_roda, t('de descanso',True)+0.1)
tp={'ritmo':t('ritmo sereno'),'ninho':t('ninho perfeito'),'afeto':t('afeto e emoções'),'habitos':t('hábitos positivos')}
tel=(t('e a orientação dele foi'), J['pediatra'][1])
eco=[(t('por um único motivo'), t('único motivo',True)+0.05),(t('no momento certo'), DUR)]
GANCHO_ATE=round(t('e a orientação dele foi'),2)
json.dump({'J':J,'tp':tp,'tel':tel,'eco':eco,'DUR':DUR,'GANCHO_ATE':GANCHO_ATE},open('trabalho/janelas.json','w'),indent=1)
print(json.dumps({'J':J,'tp':tp,'tel':tel,'eco':eco,'DUR':DUR,'gancho_ate':GANCHO_ATE},indent=0))
