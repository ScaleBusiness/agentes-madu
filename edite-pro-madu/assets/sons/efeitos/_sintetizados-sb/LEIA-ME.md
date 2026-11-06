# Efeitos sonoros SB · motion design para Reels

Pacote de efeitos sonoros para edição de Reels em estilo motion design (palavras passando, cartões aparecendo, digitação, linhas se desenhando).

- Formato: WAV, 48 kHz, 24-bit, mono.
- Volume: todos ajustados para o mesmo volume percebido (loudness momentânea máxima ≈ -16 LUFS) e com teto de pico em -1 dBTP. Sons muito curtos (cliques, teclas, pops) param no teto de pico antes de atingir o alvo, por isso soam naturalmente mais discretos.
- Todos começam e terminam em silêncio (fade curto), sem estalo na emenda.
- Gerador: `../gerar_efeitos.py` (seed fixa; rodar de novo produz os mesmos arquivos).
- Demo: `../demo-efeitos.mp3` (45,83 s), todos os sons na ordem abaixo, com 0,70 s de silêncio entre eles.

## Catálogo

| # | Arquivo | Duração (s) | Quando usar | Início no demo (s) |
|---|---|---|---|---|
| 1 | `whoosh-rapido-01.wav` | 0,38 | Palavra ou cartão passando rápido; troca de tela curta | 0,00 |
| 2 | `whoosh-rapido-02.wav` | 0,44 | Palavra ou cartão passando rápido; troca de tela curta | 1,08 |
| 3 | `whoosh-rapido-03.wav` | 0,48 | Palavra ou cartão passando rápido; troca de tela curta | 2,22 |
| 4 | `whoosh-longo-01.wav` | 1,00 | Transição ampla entre cenas; bloco grande atravessando a tela | 3,40 |
| 5 | `whoosh-longo-02.wav` | 1,17 | Transição ampla entre cenas; bloco grande atravessando a tela | 5,10 |
| 6 | `swoosh-reverso-01.wav` | 0,55 | Entrada de palavra (o corte seco coincide com a palavra aparecendo) | 6,97 |
| 7 | `swoosh-reverso-02.wav` | 0,75 | Entrada de palavra (o corte seco coincide com a palavra aparecendo) | 8,22 |
| 8 | `pop-suave-01.wav` | 0,30 | Cartão, balão ou ícone aparecendo | 9,67 |
| 9 | `pop-suave-02.wav` | 0,30 | Cartão, balão ou ícone aparecendo | 10,67 |
| 10 | `pop-suave-03.wav` | 0,30 | Cartão, balão ou ícone aparecendo | 11,67 |
| 11 | `clique-ui-01.wav` | 0,06 | Clique em botão, cursor selecionando, toque em interface | 12,67 |
| 12 | `clique-ui-02.wav` | 0,06 | Clique em botão, cursor selecionando, toque em interface | 13,43 |
| 13 | `clique-ui-03.wav` | 0,06 | Clique em botão, cursor selecionando, toque em interface | 14,19 |
| 14 | `tecla-digitacao-01.wav` | 0,09 | Digitação: sortear uma variação por letra (nunca repetir a mesma em sequência) | 14,95 |
| 15 | `tecla-digitacao-02.wav` | 0,09 | Digitação: sortear uma variação por letra (nunca repetir a mesma em sequência) | 15,74 |
| 16 | `tecla-digitacao-03.wav` | 0,09 | Digitação: sortear uma variação por letra (nunca repetir a mesma em sequência) | 16,53 |
| 17 | `tecla-digitacao-04.wav` | 0,09 | Digitação: sortear uma variação por letra (nunca repetir a mesma em sequência) | 17,32 |
| 18 | `tecla-digitacao-05.wav` | 0,09 | Digitação: sortear uma variação por letra (nunca repetir a mesma em sequência) | 18,11 |
| 19 | `tecla-digitacao-06.wav` | 0,09 | Digitação: sortear uma variação por letra (nunca repetir a mesma em sequência) | 18,90 |
| 20 | `envio-mensagem-01.wav` | 0,44 | Mensagem enviada, prompt disparado, formulário enviado | 19,69 |
| 21 | `notificacao-sutil-01.wav` | 1,40 | Notificação, venda chegando, mensagem recebida | 20,83 |
| 22 | `notificacao-sutil-02.wav` | 1,40 | Notificação, venda chegando, mensagem recebida | 22,93 |
| 23 | `impacto-grave-01.wav` | 1,35 | Palavra grande entrando, número de destaque, virada de cena | 25,03 |
| 24 | `impacto-grave-02.wav` | 1,55 | Palavra grande entrando, número de destaque, virada de cena | 27,08 |
| 25 | `subida-riser-01.wav` | 1,60 | Tensão antes de revelação (o corte final coincide com o corte de cena) | 29,33 |
| 26 | `subida-riser-02.wav` | 1,95 | Tensão antes de revelação (o corte final coincide com o corte de cena) | 31,63 |
| 27 | `brilho-shimmer-01.wav` | 0,95 | Destaque, brilho em palavra-chave, check aparecendo | 34,28 |
| 28 | `brilho-shimmer-02.wav` | 1,10 | Destaque, brilho em palavra-chave, check aparecendo | 35,93 |
| 29 | `desenho-linha-01.wav` | 0,65 | Linha, sublinhado ou gráfico se desenhando | 37,73 |
| 30 | `desenho-linha-02.wav` | 0,85 | Linha, sublinhado ou gráfico se desenhando | 39,08 |
| 31 | `transicao-escuro-01.wav` | 2,10 | Entrada em cena preta, pausa dramática | 40,63 |
| 32 | `check-confirmacao-01.wav` | 0,70 | Item concluído, check de lista, confirmação positiva | 43,43 |
| 33 | `check-confirmacao-02.wav` | 0,70 | Item concluído, check de lista, confirmação positiva | 44,83 |

## Dicas de uso

- **Digitação:** sortear entre `tecla-digitacao-01` a `-06` a cada letra, variando o volume em ±2 dB; evitar repetir a mesma variação duas vezes seguidas.
- **swoosh-reverso** e **subida-riser** terminam secos: alinhar o FINAL do arquivo com o quadro em que a palavra entra ou a cena corta.
- **impacto-grave:** o grave aparece melhor em fone e caixa; no alto-falante do celular fica o transiente e a saturação. Não empilhar dois impactos no mesmo segundo.
- **whoosh:** alinhar o ponto mais alto do som (meio do arquivo) com o momento de maior velocidade do movimento na tela.

## Licença

Sons produzidos pela Scale Business Academy por síntese; uso e distribuição livres nos produtos SB.
