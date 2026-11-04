# O que a Sarah já reprovou nos Reels da Madu

Vale junto com `~/.claude/skills/edite-pro/references/reprovacoes.md`.

| Nunca | Fala da Sarah / o que fazer |
|---|---|
| Repetir imagens de um Reel recente | "A gente vai postar um vídeo igual?" (14/10). Nada dos últimos 3–4 Reels; depois disso pode voltar, mas evitar. Conferir [imagens.md](imagens.md) |
| Editar fora da Edite Pro | "É para usar a Edit Pro… com os efeitos especiais, com as transições" (14/10) |
| Legenda na testa da Madu | "LEGENDA NÃO PODE FICAR NO ROSTO" (14/10). Medir o rosto e descer a Madu na dividida |
| Legenda embaixo na tela cheia | "LEGENDA PRECISA FICAR EM CIMA NO BUSTO (NÃO PODE FICAR EM BAIXO)" (14/10) |
| Letreiro grande no alto da tela cheia | Caía sobre o rosto da Madu (o rosto ocupa o alto). Só legenda no busto |
| Vazamento de luz por cima da imagem | "tire essa névoa horrorosa" (14/10) |
| Efeito sonoro nos cortes (swish, deslize) | "ESSE EFEITO SONORO FICOU RUIM" (14/10) |
| Música no mesmo volume da voz | "PRA QUÊ ESSA ALTURA??? NEM CONSIGO OUVIR A MADU" (14/10). Voz −15 LUFS, piano −37 LUFS com sidechain |
| Nome, idade ou assinatura da família à mostra (planos, prints) | "tomar muito cuidado para não mostrar informações sigilosas da família ou da criança nos vídeos e em nenhum material" (14/10). `scripts/anonimizar.py` + conferência visual |
| Recém-nascido ou criança acima de 4 anos | A Madu atende de 6 meses a 4 anos (14/10) |
| Capa com frase pela metade | "precisa ser a frase inteira" (14/10) |
| Capa com criança que não combina com o gancho | Gancho sobre choro → criança chorando ("mas tem que ser uma criança chorando") |
| Capa com frase sem contraste sobre a foto | Degradê branco atrás da frase ("não tá destacando a frase") |
| Close tão fechado que corta o rosto da criança | Escolher imagem em que o rosto cabe inteiro |
| Escolher o quadro da Madu sem mostrar | Mostrar opções lado a lado; ela escolhe |
| Gancho escrito sobre a abertura, faixa branca no meio do vídeo, legenda branca com contorno | Playbook seção 10 (reprovados em 30/09–08/10) |
| Mãe com cabelo colorido (azul, rosa…) | "não usar mães com cabelos coloridos" (20/10, Pexels 5303990 tirado do Vídeo 2). Mãe com aparência comum da cliente da Madu |
| Recém-nascido como "bebê de 6 meses" | Na dúvida da idade, não usar |
| Imagem que não combina com quem a fala descreve (criança no trecho sobre a mulher trabalhando) e imagem trocando a cada palavra | "os vídeos que você está colocando aí não estão coerentes com as falas… não faz o menor sentido" (20/10, Vídeo 2). Cada trecho mostra o sujeito da fala (fala da mulher = só a mulher); uma imagem por ideia, não por palavra; ação da imagem = ação dita ("quem levanta" = ela levantando, nunca dormindo) |
| Silêncio, respiração ou a Madu olhando para o lado entre as frases | "você não removeu o silêncio… isso é regra" (20/10). A régua sensível conta respiração como voz: cortar pela FALA, palavra a palavra (`trabalho-madu-lote-20out/cortes_fala.py`: palavras do Whisper medium + volume > -45 dB, folgas 0,03 s, junta só pausas < 0,10 s). Conferir no final: nenhum buraco > 0,35 s entre palavras e nenhuma sílaba comida ("atender" virou "tender" no 1º ajuste) |
| Sílaba ou consoante final comida ao apertar os cortes ("fase"→"fada", "Comente"→"Aumente") | Conferir SEMPRE com `scripts/checa_audio.py` + Whisper **medium** no áudio montado antes do render; o fim da palavra nunca fica antes do fim do Whisper; procurar o início até 0,25 s antes (20/10) |

- **Janela do take cortando a última palavra (21/10, achado na conferência).** A janela `(take, de, ate)` corta o corte em `ate`; quando a palavra final termina depois dele, some o fim ("acolhimento" virou "acolho"). Antes de renderizar, conferir cada janela: o `ate` precisa passar do fim da última palavra (Whisper `e`) com folga de ~0,4 s, sem alcançar a palavra seguinte. A passada final (`aperta`) tira o silêncio que sobrar.

- **Imagem de cima cortada (21/10, Vídeo 5: "precisa subir mais os vídeos das mães, estão cortados").** Na tela dividida só aparece de y 0 a ~800 do apoio (a máscara some entre 810 e 1000 e a legenda fica perto de 850). Medir o assunto no quadro com régua (linhas a cada 200 px) e escolher o `desce` para que o rosto **e** o bebê fiquem entre 0 e ~780: `desce ≈ topo da cabeça − 40`. Nunca deixar parede vazia em cima e o bebê escondido atrás da legenda.

- **Capa com a imagem de cima cortada (21/10: "NENHUMA! todas estão cortadas").** Na capa, o assunto de cima (rosto da mãe **e** o bebê) cabe inteiro entre y 285 (início do recorte 4:5) e ~700 (onde começa o degradê do gancho). Quadro vertical de vídeo raramente cabe: preferir foto horizontal reduzida (ex.: largura 1150) com o fundo da própria foto desfocado atrás, para não sobrar faixa vazia. Conferir na folha com as linhas do recorte antes de mostrar.
- **Legenda baixa demais (21/10, Reel dos soltos).** O padrão 1470 era da gravação com microfone no queixo; com 2 linhas a legenda descia até ~1670, em cima da legenda do post. Regra 08/10: o bloco da legenda termina antes de y 1480. Medir o queixo (Vision) e pôr a legenda logo abaixo dele. Vídeos 1 e 2 (microfone no queixo) corrigidos em 21/10: legenda 1270, CTA 1150. Padrão do `gerar_jsx.py` agora é 1270/1150.
- **Capa de bastidor (21/10, aprovada a ideia):** quadro inteiro da Madu na mesa com o fundo real, "Por dentro da / *Consultoria Sleepy*" no alto (dentro do 4:5) e o título com o destaque em pêssego na palavra-chave ("Seu primeiro / *plano de sono*").
- **Capa com espaço livre em cima e frase na testa da Madu (21/10: "SUBIR MAIS!!!!! … coloca a headline na testa da MADU. Não faz o menor sentido").** A imagem de cima sobe até a testa da pessoa ficar logo abaixo de y 285 (sem parede vazia em cima). A frase vai logo abaixo do assunto e termina **antes do cabelo da Madu**: nunca descer a frase para dar espaço à imagem; quem se ajusta é a imagem.
