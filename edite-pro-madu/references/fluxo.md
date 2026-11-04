# Fluxo da Edite Pro Madu (comandos)

`P` = `escritorioscalebusiness/edicao-de-videos/projeto-remotion` · `K` = `~/.claude/skills/edite-pro-madu`.

## F0 · Preparação

```bash
B=~/escritorioscalebusiness/edicao-de-videos/brutos/AAAA-MM-DD-madu-<video>; mkdir -p $B; cp ~/Downloads/IMG_XXXX.MOV $B/
ffmpeg -i $B/IMG_XXXX.MOV -c:v libx264 -crf 16 -preset fast -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k $P/public/madu-<video>/video/take-XXXX.mp4
ffmpeg -i take-XXXX.mp4 -filter_complex "[0:v]setpts=PTS/1.3[v];[0:a]atempo=1.3[a]" -map "[v]" -map "[a]" -r 30 -c:v libx264 -crf 17 -preset fast -pix_fmt yuv420p -c:a aac -b:a 192k take-XXXX-x1.3.mp4
```

Copiar `K/assets/modelo/MaduAcolher.jsx` e `CapaMaduAcolher.jsx` para `P/src/edite/madu-<video>/`, renomear, registrar no `Root.jsx` com `acelera(DADOS_1X, 1.3)` e abrir o Studio (`remotion-studio-3010`).

## F1 · Transcrição, cortes e legenda

1. faster-whisper `small`, `word_timestamps=True` → `trabalho-madu-<video>/transcricao/take-XXXX.json` (lista `{w,s,e}`).
2. Retranscrever com `initial_prompt='Hum, é, eh, então.'` e `condition_on_previous_text=False` para achar repetições e hesitações.
3. **Cortes pela fala (regra desde 20/10):** usar `edicao-de-videos/projeto-remotion/trabalho-madu-lote-20out/cortes_fala.py` (palavras + volume; respiração e olhada para o lado saem). A régua sensível abaixo serve só de apoio.
   `python3 K/scripts/medir.py 0.12` (copiar para `trabalho-…/` e ajustar o caminho do take) gera `voz.npy`.
4. `montar.py`: GAP 0,30 s, folga 0,06/0,08 s, `RETIRAR` para palavra que a Sarah mandar tirar (medir o volume a cada 10 ms e cortar no silêncio antes e depois da palavra), `GRUPOS` com a legenda revisada (`*destaque*`, `~palavra` escondida, `PALAVRA^3` junta 3 tokens). Rodar e conferir os avisos.
5. Checar se todo `G('…')` do JSX existe nos grupos (script em `edite-pro/references/fluxo.md`, F1).

## Rosto da Madu (antes de posicionar legenda)

```python
import Vision; from Foundation import NSURL
# para cada quadro (ffmpeg -vf fps=0.5): VNDetectFaceRectanglesRequest → y = 1920 - (origin.y + height) * 1920
```
Use o topo mínimo do rosto para `VIDEO_Y_DIV` (cabelo ≈ 110 px acima do rosto) e o queixo máximo para a legenda da tela cheia.

## F4 · Conferência

- Quadros: `node trabalho-…/quadros.mjs <Id> <pasta> 0.22 <quadros>` — rodar em lotes pequenos ou um a um (lotes grandes falham), e **apagar `$TMPDIR/remotion-webpack-bundle-*` depois de cada lote** (cada um ocupa GBs; o disco encheu em 14/10).
- Fala: montar a voz direto dos cortes (ffmpeg `atrim` + `concat` + `atempo=1.3`) e rodar `python3 K/scripts/confere_fala.py fala.wav dados.json 1.3`. Se o começo vier vazio, transcrever o trecho separado.

## F6 · Exportação com o piano

```bash
npx remotion render src/index.jsx <Id> out/<video>/final-bruto.mp4 --codec h264 --crf 17
M="$HOME/escritorioscalebusiness/edicao-de-videos/assets-edite/sons/trilhas/classica-drive/Lyrical Piano Advertising Background 2 Underscore.mp3"
ffmpeg -i final-bruto.mp4 -stream_loop -1 -i "$M" -filter_complex "[0:a]loudnorm=I=-15:TP=-1.5,asplit[v][sc];[1:a]loudnorm=I=-37:TP=-9,afade=t=in:d=1.5[m0];[m0][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[md];[v][md]amix=inputs=2:duration=first:normalize=0,afade=t=out:st=<dur-1.5>:d=1.5,alimiter=limit=0.85[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart renders/AAAA-MM-DD-madu-<video>.mp4
ffmpeg -i renders/…mp4 -vf scale=720:1280 -c:v libx264 -crf 23 -maxrate 2200k -bufsize 4400k -c:a aac -b:a 128k -movflags +faststart renders/…-celular.mp4
rm -rf $TMPDIR/remotion-webpack-bundle-*
```

Capa: `npx remotion still src/index.jsx Capa<Id> capa.png --props='{"madu":"<quadro>"}'` → JPG + recorte 4:5 (`crop 0,285,1080,1635`).
