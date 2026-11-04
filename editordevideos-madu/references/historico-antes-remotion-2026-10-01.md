---
name: editordevideos-madu
description: >
  Editor de Reels e TikTok da Madu Drummond (Método Sleepy), com a identidade visual dela
  (Raleway, Azul Noite, Pêssego, cartelas numeradas). Mesmo motor da /editordevideos da SB:
  transcreve, traz o gancho para a abertura, tira os respiros, acelera, confere se nenhuma palavra
  foi cortada e entrega pronto para postar. Use sempre que a Madu (ou a Sarah, para a Madu) pedir:
  editar vídeo, editar reels, legendar, vídeo pronto para postar, cortar vídeo, vídeo da Madu.
argument-hint: "caminho/do/video.mp4 [inteiro | reels | completo]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
---

# Editor de Vídeos · Madu Drummond — Reels e TikTok

Transforma um vídeo gravado em conteúdo pronto para postar. O melhor gancho quase nunca é a
primeira frase: está no meio da fala. A skill encontra essa frase, coloca na abertura e limpa o
ritmo sem cortar nenhuma palavra.

**Motor:** `~/.claude/skills/editordevideos-madu/motor/` · **Fontes:** legenda base `assets/Inter-VF.ttf` (Inter 800) · gancho e cartelas `assets/Raleway-VF.ttf` (Raleway 600) · **destaques: Playfair Display Italic 400** via Google Fonts (gratuita · `family=Playfair+Display:ital,wght@1,400`) — Inter e Raleway OFL
**Protocolo estratégico (categorias de trecho, enxugamento, depoimentos, legenda do post):**
`references/protocolo-estrategico.md` — ler antes de escolher gancho em depoimento ou compilado.

```bash
MOTOR=~/.claude/skills/editordevideos-madu/motor
PY=~/.claude/skills/editordevideos-madu/.venv/bin/python3; [ -x "$PY" ] || PY=python3
```
Todos os comandos abaixo usam `$PY $MOTOR/...` (o ambiente `.venv` é criado pelo instalador das
mentoradas; na máquina da Sarah o `python3` do sistema já tem tudo).

---

## 🔴 PADRÃO VIGENTE — CONSOLIDADO (30/09/2026 · SUPERSEDE tudo abaixo sobre cor, fonte e posição)

### Tipografia

| Elemento | Especificação |
|---|---|
| **Legenda base** | **Inter 800** · 96px · BRANCA `#FFFFFF` · sem contorno · sombra mínima só (`0 1px 3px rgba(0,0,0,0.40)`) — nunca pesada · letras −6% · espaço entre palavras normal |
| **Palavra-destaque** | **Playfair Display Italic · peso 400 (Fino)** · `#FFDBD5` (rosa/creme) · ~3,5× a legenda base (~336px) · minúsculas · sem contorno · estilo Captions · Google Fonts gratuita |
| **Gancho (cartela)** | **Raleway 600** · branco · faixa arredondada Azul Drummond `#1F4B7A` · palavra-destaque no gancho também em Playfair Italic 400 `#FFDBD5` |
| **CTA final** | cartela sem número · mesmo visual do gancho |

**Como usar o destaque:** marcar com `*palavra*` no JSON → o motor renderiza em Playfair Display Italic 400, ~3,5× maior, cor `#FFDBD5`. Não é destaque inline (mesmo tamanho): é a palavra em escala gigante quebrando o ritmo visual, exatamente como o Captions app faz.

**Regra do destaque:** 1-3 palavras no **fim** da legenda — ex.: `"não poder fazer *nada*."`, `"um grande *trauma*"`. Nunca no meio da frase, nunca artigo/preposição, nunca dois destaques no mesmo bloco, nunca mais de 3 palavras.

**Google Fonts:** `https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400`

**Máx. 3 fontes por peça:** Inter 800 (legenda base) + Raleway 600 (gancho/CTA) + Playfair Italic 400 (destaques).

**NUNCA:** Scripter na legenda (substituído pela Playfair) · Damion · Another Shabby · Kaushan Script · peso 700+ nos textos da tela · azul na legenda ("não dá para ler" · roupa colorida da Madu) · branco com contorno/stroke ("polui" — Madu) · halo ou fundo escuro atrás da legenda · sombra pesada · identidade SB (marrom, dourado, roxo) · preto puro.

---

### Posicionamento — Inegociável

**Nada no rosto nem no pescoço da Madu.** Antes de editar, extrair um quadro de referência e medir onde cai o queixo:
```bash
ffmpeg -ss 3 -i video.mp4 -frames:v 1 -vf scale=540:-1 frame-ref.jpg && open frame-ref.jpg
```
Gancho e legenda ficam APENAS no tronco. Ao mudar enquadramento (em pé, câmera mais alta), remedir antes de definir os `y`.

**Padding lateral mínimo de 24px** em todos os textos — nunca texto tocando as bordas laterais. Largura útil de texto: 940px (de 1080px).

**Posições padrão (enquadramento dela sentada, câmera no peito · 9:16 · 1080×1920):**

| Elemento | `y` (px) | % do frame | Observação |
|---|---|---|---|
| Gancho (cartela Azul) | 1150 | ~36% | Peito/tronco superior · só nos primeiros ~5s |
| Cartelas de lista | 1230 | — | — |
| Legenda **sem gancho** | 1480 | ~68% | — |
| Legenda **com gancho presente** | 1300 | ~54% | ABAIXO do gancho · nunca sobrepor os dois |

Legenda começa quando o gancho sai (~5s) — o início do vídeo vira a capa do Reel.

---

### Alinhamento e ritmo de frase

- **Blocos curtos:** 2-5 palavras por bloco (`MAX_LINHA = 14`), como o Captions — nunca 8+ palavras em uma linha
- **Nunca terminar bloco** em preposição, artigo ou conjunção (de, a, o, e, mas, que, em, com, por, para, ao, da, do…)
- **Nunca viúva tipográfica:** última linha não pode ter 1 palavra solta — usar `|` para quebrar à mão:  
  ex.: `"Ninguém dorme|a noite *inteira*.|Nem o seu bebê."`
- **Linha longa:** reduzir tamanho de fonte só o necessário para caber nos 940px de largura útil
- **Caixa:** minúsculas na legenda; palavra que a Madu fala em CAIXA ALTA no original se mantém
- **Legenda-relâmpago (<0,6s):** juntar com a anterior
- **Segurar legenda** até a palavra que fecha a frase antes de trocar

---

### Entrada visual e edição dinâmica (sempre · estilo Captions)

- Entrada de cada legenda com **pop** (86% → 107% → 102% → 100% em 3 quadros)
- Zoom alternado 1,00 / 1,10 a cada frase + punch 1,18 nas palavras-destaque (`motor/dinamico_zoom.py`, âncora vertical 0,28)
- Voz "de memória" (telefone: passa-faixa 450-2800 Hz) quando ela reproduz a fala de outra pessoa
- Eco curto em 1-2 frases-chave e no fecho
- Whoosh sintetizado em cada entrada de tela dividida
- Áudio: receita em `references/exemplo-audio-efeitos.py`
- Velocidade: **1,25 a 1,3** (ela fala devagar) · `silencio_db` **−47** (voz baixa, média −43,6 dB)

**ANTES de editar: abrir o roteiro no Notion** (Calendário de Conteúdo da Madu) — o **Gancho** da página vira o gancho
ESCRITO na tela (faixa Azul Drummond) e o **CTA** vira a chamada final (cartela com texto começando por `>`, mesmo
visual do gancho, com o vídeo congelado +3s). O corte segue os blocos do roteiro, com as frases dela.
Fonte da verdade do visual: o **PDF** `Madu Drummond/Playbook visual/` (não só o HTML da pasta branding).

**Fontes do playbook (30/09):** títulos Raleway 600 · destaque/fim de frase = **Scripter** (`assets/Scripter-Regular.ttf`)
— font da marca comercial da Madu, NUNCA Damion, NUNCA Another Shabby (trial CC BY-NC) · apoio Montserrat.
Gancho em faixa **Azul Drummond** com Raleway branca.

**Edição dinâmica (estilo Captions) — sempre:**
- zoom de corte alternando 1,00 / 1,10 a cada frase + punch 1,18 nas palavras-destaque
  (`motor/dinamico_zoom.py`, âncora vertical 0,28 para não cortar a cabeça) — só na tela cheia;
- voz "de memória" (telefone: passa-faixa 450-2800 Hz) quando ela reproduz a fala de outra pessoa;
- eco curto em 1-2 frases-chave e no fecho;
- whoosh sintetizado (ruído rosa filtrado, sem download) em cada entrada de tela dividida;
- receita de áudio: `references/exemplo-audio-efeitos.py`.

## Padrão Madu (aplicar SEMPRE · regras de posição da Sarah 24/09 · visual APROVADO 25/09 · legenda refeita no estilo Captions a pedido da Madu 28/09)

**Identidade visual** (fonte: `Madu Drummond/branding/10-playbook-visual-madu-drummond.html`) — já
está dentro do motor, não precisa passar nada:

| Elemento | Como sai |
|---|---|
| Legenda | **estilo Captions (Madu 28/09):** **Inter peso 750, 96px, letras coladas −6% (espaço entre palavras normal)** — calibrada LADO A LADO com o print do Captions (Sarah 30/09, após reprovar a versão Bold 70px fina e pequena) · blocos curtos (`MAX_LINHA = 14`, 2-5 palavras por vez, como o Captions) · linha longa diminui a letra só o necessário para caber em 940px ·, **AZUL NOITE `#1F4B7A`, SEM contorno** — só um clarão branco difuso atrás (Sarah 30/09: branco sobre o fundo claro dela "NÃO DÁ PARA LER", contraste 2,2; Azul Noite 4-5,7) · Instagram em minúsculas (palavra em CAIXA ALTA se mantém: "comenta NOITE") |
| Palavra-destaque da legenda | `*palavra*` sai em **Playfair Display Italic 400 (Fino)**, cor `#FFDBD5` (rosa/creme), ~3,5× a legenda base, minúsculas, fim de frase — destaque por tamanho + fonte, estilo Captions. NUNCA Kaushan, NUNCA Damion, NUNCA Another Shabby, NUNCA Scripter na legenda |
| Gancho | bloco arredondado Azul Noite · texto Raleway branco · `*palavra*` em pincel Pêssego |
| Cartela de lista | pílula branca + círculo numerado Azul Drummond · **nome do item em pincel** Azul Noite · `--pilar 1-4` troca o círculo pela cor do pilar |
| CTA final | cartela sem número: `{"t": "Comenta *NOITE*"}` → "Comenta" em Raleway + NOITE em pincel |

**Marcar as palavras-destaque (trabalho do Claude, obrigatório):** depois de revisar a legenda,
editar o JSON e envolver em `*...*` **UMA palavra de peso a cada 2-3 blocos** (substantivo ou verbo
que carrega a ideia: *intensidade*, *livros*, *transição*, *nervoso*). Nunca artigo/preposição, nunca
duas no mesmo bloco, nunca frase inteira — "não é salada de fontes" (Madu). Só uma palavra por
marcação (o motor quebra a legenda por palavra).

**Cor da legenda:** padrão `azul` (Azul Noite). `COR_LEGENDA=branco` só existe para vídeo gravado em
fundo ESCURO — medir o contraste antes; nos cenários claros dela o branco reprova.

**NUNCA:** branco com contorno/stroke ("polui" — Madu) · halo ou fundo escuro atrás da legenda · sombra pesada/dramática · Scripter na legenda (substituído pela Playfair Display) · Kaushan Script · Damion · Another Shabby · fonte 700+ fora da legenda base · preto puro · identidade SB (marrom, dourado, roxo) · texto no rosto ou pescoço da Madu · texto tocando as bordas laterais (padding mínimo 24px).

**Posição — texto NUNCA sobre o rosto nem no pescoço (regra inegociável Sarah 30/09).** Antes de editar,
extrair um quadro e conferir onde fica o queixo. Padrão do enquadramento dela (sentada, câmera no peito):
- gancho: `--titulo-ate 5 --y-titulo 1150` (só nos primeiros 5s, na altura do tronco/peito — ~36% do frame);
- cartelas: `--y-cartela 1230`;
- legenda sem gancho: `--y-legenda 1480` (~68% do frame);
- legenda com gancho presente: `--y-legenda 1300` (~54% do frame, ABAIXO do gancho — nunca sobrepor);
- legenda começa quando o gancho sai (tirar do JSON os blocos antes de ~5s, ou ~3s se não houver gancho escrito) — o começo do vídeo vira a CAPA do Reel;
- **padding lateral mínimo de 24px** em todos os textos — configurado no motor, nunca texto tocando as bordas.

**Ritmo da voz dela:** velocidade **1,25 a 1,3** (ela fala devagar) · `silencio_db` **−47** (voz baixa,
média −43,6 dB; −40 cortou ponta de palavra).

**Vídeo em formato de lista** ("5 coisas que…"): gancho escrito + uma cartela por item enquanto ela
explica ("1 · Luzes muito fortes") + CTA. Montar `cartelas.json` à mão com os tempos da legenda:
```json
{"blocos": [{"i": 5.0, "f": 10.02, "t": "1 · Luzes muito fortes"}, {"i": 82.68, "f": 84.87, "t": "Comenta *NOITE*"}]}
```

**Comando-padrão de gravação** (as duas versões):
```bash
for E in instagram tiktok; do
$PY $MOTOR/legendar.py gravar BASE.mp4 legendas.json "$OUT/NOME-$E.mp4" --estilo $E \
  --titulo "GANCHO com *destaque*" --titulo-ate 5 --y-titulo 1150 \
  --cartelas cartelas.json --y-cartela 1230 --y-legenda 1480
done
```
No padrão Madu o TikTok usa o mesmo gancho da abertura (não há título fixo no topo — cobriria o rosto).

**Linguagem nos textos da tela:** "consultora de sono infantil" (nunca "terapeuta"), grafia **Sleepy**,
"baseado na neurociência" (nunca "especialista em neurociência"), nunca atacar consultoria de sono.

**Onde ficam os vídeos (Sarah 30/09):** os ORIGINAIS ficam no Drive, na pasta "Vídeos originais"
(`https://drive.google.com/drive/folders/1FuKjg59NeUTsOjlckZMy2ZA7xMz8wwM-`), e os EDITADOS vão para a
subpasta "Vídeos editados" (`https://drive.google.com/drive/folders/19VcMz456eQx4Y59d5t15hNkIcDlP7QV6`).
Nada de vídeo fica guardado na pasta do computador — trabalhar no scratchpad e subir o resultado.
- Baixar original: `curl -sSL -o NOME.MOV "https://drive.usercontent.google.com/download?id=ID&export=download&confirm=t"`
  (o ID sai da busca do conector do Drive com `parentId = '<pasta>'`).
- Subir (vídeo > 10 MB): conector do Drive não aguenta; usar o Chrome da Sarah na pasta de destino —
  `split -b 9000000` no vídeo, criar um `<input type=file>` na página, enviar cada parte com `file_upload`,
  juntar as partes num `Blob` e disparar `dragenter/dragover/drop` com `DataTransfer` no centro da página.
  Conferir depois pelo conector se o `fileSize` bate byte a byte com o arquivo local.
  Para SUBSTITUIR vídeo já existente: mandar o antigo para a lixeira ANTES (`trash_file`) — senão o Drive abre
  a janela "Opções de upload" e engole os drops seguintes enquanto ela está aberta.

**CONTRASTE (regra inegociável SB · Sarah 30/09):** fundo claro = texto escuro. Antes de gravar, medir a
razão de contraste (WCAG) de cada cor de texto contra a cor média da faixa da legenda (y 1380-1600) em 5-6
quadros do vídeo. Destaque e cartelas precisam de ≥ 3:1 em TODOS os quadros; cor abaixo disso não sai.
Referência medida nos vídeos dela: Azul Noite 4,17 · branco 2,18 · ameixa 2,38 · pêssego 1,15-1,70.

**Antes de entregar qualquer ajuste visual pedido com print de referência:** montar a imagem print × quadro
 renderizado, na mesma escala, e comparar peso, tamanho e espaçamento. Sem essa comparação, não entregar.

**Viúva no gancho:** use `|` para quebrar a linha à mão quando a última linha ficar com 1 palavra
(ex.: `"Ninguém dorme|a noite *inteira*.|Nem o seu bebê."`).

Antes (até 28/09) os vídeos ficavam em `Madu Drummond/Vídeos editados/<nome-do-vídeo>/`. Referência aprovada:
`Vídeos editados/IMG_8622/identidade-madu/`.

---

## O que a pessoa recebe

Para cada vídeo, uma pasta `editados/<nome-do-video>/` ao lado do original:

| Arquivo | O que é |
|---|---|
| `00-limpo.mp4` | vídeo inteiro limpo, **sem legenda** (base para os cortes) |
| `01-inteiro-instagram.mp4` · `01-inteiro-tiktok.mp4` | vídeo inteiro nas duas versões |
| `reel-N-<tema>-instagram.mp4` · `reel-N-<tema>-tiktok.mp4` | Reels curtos (30 a 60s) |
| `*.srt` | legenda em texto, para outras plataformas |
| `trabalho/` | transcrições e planos (não é entregável) |

**Modos:** `inteiro` (só o vídeo inteiro) · `reels` (só os curtos) · `completo` (padrão: os dois).

**Sem legenda:** uma versão só de cada vídeo, sem nenhum texto na tela — `01-inteiro.mp4` e
`reel-N-<tema>.mp4` (o `00-limpo.mp4` já é o vídeo inteiro sem legenda; copiar com o nome final).

---

## Passo 0 · Perguntar ANTES de começar (obrigatório · Sarah 23/09)

Sempre perguntar, numa mensagem só:
> "Vou entregar o vídeo inteiro editado e os Reels curtos. **Você quer com legenda ou sem legenda?**"

- **Com legenda** → duas versões de cada vídeo (Instagram e TikTok).
- **Sem legenda** → uma versão de cada, sem texto na tela.
- Se a pessoa já disse na mensagem (ex.: "sem legenda", "só o inteiro"), não perguntar de novo.
- Enquanto espera a resposta, já pode rodar o Passo 1 (transcrição) — ele é igual nos dois casos.
- A transcrição do vídeo limpo (Passo 4) roda **mesmo sem legenda**: é ela que confere se nenhuma
  palavra foi cortada.

### Os dois estilos de legenda (decisão Sarah · 23/09/2026)

| Plataforma | Estilo |
|---|---|
| **Instagram** | só legenda, embaixo, **minúsculas**, branca com contorno preto, 62px — a mais legível |
| **TikTok** | **título fixo no topo** (maiúsculas, fundo escuro translúcido) + legenda embaixo em maiúsculas normais, 54px, posicionada mais alta para fugir da descrição do app |

---

## Pré-requisitos (checar antes de começar)

```bash
ffmpeg -version | head -1 && $PY -c "import faster_whisper, PIL; print('ok')" && ls $MOTOR
```

Se faltar algo: `bash ~/.claude/skills/editordevideos-madu/setup-mentorado.sh`. Não precisa de chave de
API — a transcrição roda no computador e a análise é feita pelo próprio Claude. Na primeira
transcrição o modelo de voz (~1,5 GB) é baixado uma vez só.

---

## MODO 1 — Vídeo inteiro limpo

### Passo 1 · Preparar e transcrever o original
```bash
V="/caminho/do/video.mp4"; N=$(basename "${V%.*}"); OUT="$(dirname "$V")/editados/$N"
mkdir -p "$OUT/trabalho"
ffprobe -v quiet -show_entries format=duration -show_entries stream=width,height -of csv=p=0 "$V"
ffmpeg -y -loglevel error -i "$V" -vn -ar 16000 -ac 1 "$OUT/trabalho/audio.wav"
$PY $MOTOR/transcrever.py "$OUT/trabalho/audio.wav" "$OUT/trabalho/palavras.json"
$PY $MOTOR/analisar.py "$V" "$OUT/trabalho/palavras.json"
```
O `analisar.py` mostra a transcrição com as pausas marcadas e sugere **velocidade** (alvo 170
palavras/min sem pausas, teto 1,25×) e **limiar de silêncio** (volume médio − 3 dB, entre −40 e −30).

### Passo 2 · Ler e decidir (o trabalho do Claude)
Ler a transcrição inteira e decidir, com o tempo exato de cada palavra:

1. **Gancho** — a frase que para o scroll. Precisa passar nos 4 testes:
   Clareza (faz sentido sozinha) · Força (curiosidade, identificação ou surpresa) ·
   Pertinência (é sobre o tema de quem fala) · Entrada limpa (começa em frase completa).
   Se a abertura original já é a frase mais forte, **não trocar**.
2. **O gancho sai do meio ou fica nos dois lugares?** Ler a frase que vem logo DEPOIS do gancho
   no original. Se ela depende do gancho para fazer sentido (Ex SB: "Então é uma escolha", depois de
   "Não dá para ter medo e fé ao mesmo tempo"), **manter nos dois lugares** — abre como chamada e
   volta como clímax. Se não depende, tirar do meio.
3. **Tropeços** — recomeços e falsas largadas saem (Ex SB: "Eu quero falar em confiança e eu quero
   falar de confiança" → fica só a segunda).
4. **Início e fim** — cortar "oi, gente", "então…" de abertura e despedida vazia no final.

### Passo 3 · Plano e renderização
Criar `"$OUT/trabalho/plano-inteiro.json"`:
```json
{
 "entrada": "/caminho/do/video.mp4",
 "saida": "/caminho/editados/NOME/00-limpo.mp4",
 "palavras": "/caminho/editados/NOME/trabalho/palavras.json",
 "blocos": [[INI_GANCHO, FIM_GANCHO], [INI_CORPO, FIM_CORPO]],
 "zoom_blocos": [1.14, null],
 "silencio_db": -35, "silencio_min": 0.25, "folga": 0.1,
 "velocidade": 1.1, "zoom": 1.10, "zoom_intervalo": 4.0
}
```
- `blocos` = trechos **na ordem de exibição**. Para tirar um trecho do meio, dividir o corpo em dois blocos.
- Limites de corte: início ~0,05s antes da primeira palavra; fim no meio da pausa seguinte — nunca
  colado na próxima palavra.
- `zoom_blocos`: gancho com zoom fixo de destaque (1.14); `null` = zoom alternado automático.
```bash
$PY $MOTOR/editar_reel.py "$OUT/trabalho/plano-inteiro.json"
```
O motor corta as pausas pelo volume do áudio, **protege toda palavra transcrita** (nunca corta dentro
de uma), aplica fade de 12 ms em cada corte, alterna zoom só em fim de frase ou vírgula (mínimo 4s
entre trocas), acelera sem afinar a voz e nivela o áudio no padrão das redes (−14 LUFS).

### Passo 4 · Conferência obrigatória (nunca pular)
```bash
$PY $MOTOR/legendar.py gerar "$OUT/00-limpo.mp4" "$OUT/trabalho/legendas-inteiro.json"
$PY $MOTOR/conferir.py "$OUT/trabalho/plano-inteiro.json" "$OUT/trabalho/palavras.json" "$OUT/trabalho/legendas-inteiro.json"
```
O vídeo pronto é retranscrito e comparado com o texto esperado. Para cada diferença: verificar se
existe corte naquele ponto. **Diferença perto de corte = palavra cortada → corrigir o plano e
renderizar de novo.** Diferença sem corte por perto = variação da transcrição, ignorar.
Ex SB: "para sempre" virou "para si" porque a voz baixa no fim da frase ficou abaixo do limiar.

---

## MODO 2 — Reels curtos (sempre a partir do `00-limpo.mp4`)

Os cortes saem do vídeo limpo, que já está sem respiros e acelerado — por isso `velocidade: 1.0`.

1. Transcrição do vídeo limpo = `trabalho/legendas-inteiro.json` (campo `palavras`) do Passo 4.
2. Escolher de 1 a 3 trechos de **30 a 60s**, cada um com **uma ideia completa**:
   começa em início de frase (sem "E", "Mas", "Então" soltos na largada) e **termina na conclusão
   da ideia** — nunca parar antes do fechamento.
3. Dentro de cada trecho, aplicar a regra do gancho do Passo 2 (trazer para a frente só se for mais
   forte que a abertura do trecho).
4. Plano por Reel (`trabalho/plano-reel-N.json`), com `"entrada"` = `00-limpo.mp4`,
   `"palavras"` = `trabalho/legendas-inteiro.json` (o motor lê o campo `palavras`), `"velocidade": 1.0`, e saída
   `trabalho/reel-N-base.mp4`. Rodar `editar_reel.py` e depois `legendar.py gerar` na base.

---

## Legendas e título (vale para os dois modos)

### Revisar o texto ANTES de gravar
Ler todos os blocos que o `gerar` imprimiu e corrigir:
- **grafia** (Ex SB: "inavalável" → "inabalável"), números escritos errado ("1 fé" → "uma fé"),
  nomes próprios, maiúsculas indevidas;
- aplicar sem retranscrever (aceita várias palavras e pode repetir `--corrigir`):
```bash
$PY $MOTOR/legendar.py remontar VIDEO.mp4 legendas.json --corrigir "inavalável=inabalável" --corrigir "em puro=impuro"
```
- Na dúvida se a palavra foi cortada ou só mal transcrita, transcrever o trecho isolado (original e
  editado) e comparar. Ex SB: "ou impuro" saiu "ou em puro" no vídeo inteiro, mas isolado veio
  certo → era leitura da transcrição, só corrigir a legenda.
O motor já quebra as legendas em até 2 linhas, nunca termina uma legenda em preposição, artigo ou
conjunção, junta legendas-relâmpago (<0,6s) e segura a legenda até a palavra que fecha a frase.

### Título do TikTok (criado pelo Claude)
- Sai das **palavras da própria pessoa** no vídeo — nunca inventar tese nova.
- Até ~35 caracteres, direto, sem ponto de exclamação.
- **Não repetir o gancho** literalmente (o gancho já está na fala) — complementar.
- Nunca promessa milagrosa; nunca atacar o que a pessoa vende.
- Ex SB: "FÉ NÃO É CONTROLE. É ENTREGA." · "ENTREGAR TAMBÉM É NEUROCIÊNCIA".

### Gravar as duas versões
```bash
$PY $MOTOR/legendar.py gravar BASE.mp4 legendas.json "$OUT/NOME-instagram.mp4" --estilo instagram
$PY $MOTOR/legendar.py gravar BASE.mp4 legendas.json "$OUT/NOME-tiktok.mp4" --estilo tiktok --titulo "TÍTULO"
```

### Conferência visual
Extrair 3 quadros de cada versão (início, meio, fim) e olhar: legenda legível, dentro da área
segura, título sem cortar, zoom sem cortar a cabeça.
```bash
for t in 1.5 10 25; do ffmpeg -y -loglevel error -ss $t -i ARQ.mp4 -frames:v 1 -vf scale=300:-1 q$t.jpg; done
```

---

## Relatório de entrega (no chat)

Para cada vídeo, curto e sem bastidor técnico:
- **Gancho usado** (frase exata) e se ficou também no meio, com o motivo em uma linha.
- **O que saiu:** tropeços, abertura/fechamento vazios, quantidade de pausas.
- **Velocidade** aplicada e **duração** antes → depois.
- **Reels curtos:** tema, duração e título do TikTok de cada um.
- **Conferência:** "nenhuma palavra cortada" (ou o que foi corrigido).
- Onde estão os arquivos.

Pedidos de ajuste (outro gancho, outro título, sem zoom, mais ou menos rápido) → mudar só o plano
ou o título e renderizar de novo aquele passo.

---

## Regras inegociáveis

- **Nunca cortar palavra.** A conferência do Passo 4 é obrigatória em todo vídeo.
- **Gancho vem da fala real** — nunca texto inventado sobre o vídeo.
- Vídeos de mentoria/sessão gravada: o gancho precisa ser sobre o tema de quem vai postar, não sobre
  o negócio de outra pessoa que aparece na conversa.
- Legenda revisada antes de gravar — erro de grafia na legenda derruba a percepção de valor.
- Português do Brasil com acentuação correta em legenda e título.
- O original nunca é alterado; tudo vai para `editados/`.

## Limitações atuais (dizer com honestidade quando perguntarem)

- Instalação exige Mac com Terminal (Homebrew, ffmpeg, Python). Windows ainda não testado.
- O ffmpeg do Homebrew não tem módulo de texto — por isso a legenda é desenhada como imagem e
  sobreposta (funciona igual para quem assiste).
- Capa do Reels e CTA animado não fazem parte do motor atual.
- **Vídeo gravado na horizontal** (ex.: 1280×720): o motor preenche a tela vertical cortando as
  laterais pelo centro — avisar a pessoa antes e conferir nos quadros se o rosto ficou no enquadramento.
- Transcrição: ~35s por minuto de vídeo; renderização: ~1 min por minuto de vídeo (Mac com chip M).


---

## Tela dividida com cenas de apoio (Sarah 30/09 · narrativa do método)

Quando a fala pede imagem (ex.: "o pediatra mandou deixar no berço chorando" → bebê chorando):
1. **Mapa antes de editar:** tabela momento × frase × cena, aprovada pela Sarah. Vídeo longo para Reels
   = corte de até ~1min30-3min com as frases da própria Madu (arco dor → busca → virada → método → fechamento).
2. **Cenas:** banco gratuito com licença comercial (Pexels). Miniatura: `https://images.pexels.com/videos/ID/pictures/preview-0.jpg`
   (ou `.jpeg`, `preview-1`); download: `https://www.pexels.com/download/video/ID/`. **Mostrar nome, origem e
   tamanho e pedir autorização antes de baixar.** Nunca vídeo de outro perfil, filme ou TV. Cena de choro: forte, não angustiante.
3. **Montagem:** cena em cima (1080×960) + Madu embaixo (recorte do vídeo limpo `crop=1080:960:0:40`), só nos
   trechos mapeados (4-12s cada). Legenda em duas camadas: tela cheia `--y-legenda 1480`; tela dividida
   `--y-legenda 1075` (na parede acima da cabeça dela — NUNCA sobre a cena de apoio, que varia de contraste).
4. **Método Sleepy:** usar a roda oficial dos 4 Pilares (`Materiais do método/WhatsApp Image 2026-09-08 at 17.05.36.jpeg`)
   e acender cada pilar com anel quando ela diz o nome (anel pêssego nos pilares escuros 1-2, Azul Noite nos claros 3-4).
Script de referência: `references/exemplo-tela-dividida-narrativa.py`.
