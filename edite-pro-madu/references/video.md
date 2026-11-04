# Vídeo da Madu · medidas (1080 × 1920)

Fonte: Playbook Visual da Madu, seção 10 (`assets/playbook/`), corrigido pela Sarah em 14/10/2026 no Reel "Acolher o choro".

## Paleta

Azul Noite #1F4B7A (texto) · Pêssego #FFDBD5 (marca-texto e caixa da palavra-chave) · Névoa #EEF6FB (fundo do fechamento) · branco.

## Tela

| Item | Valor |
|---|---|
| Velocidade | 1,3× (take regravado com setpts + atempo; tempos ÷ 1,3 no Root) |
| Junção da dividida | 880 (apoio em cima em largura total, mescla por máscara 810 → 1000, sem faixa) |
| Madu na dividida | desce `VIDEO_Y_DIV` ≈ 690 (rosto no bruto em y 333–942; o cabelo fica abaixo da legenda) |
| Legenda na dividida | base presa em y 872 (topo = 872 − 100 × linhas) |
| Legenda na tela cheia | topo y 1045: alto do busto, abaixo do queixo, acima do microfone |
| Chamada final | topo y 1050, Madu ampliada +12% |
| Transição de corte | zoom +5% e desfoque de 4 px que somem em 6 quadros |
| Troca de tela | 0,34 s; a legenda some durante a troca |

## Legenda

Inter 800, 68 px, entrelinha 100 px, letras −1,6 px, Azul Noite, brilho branco difuso (`0 0 18px #fff…`). Palavra falada com marca-texto Pêssego levemente inclinado. Destaque (uma palavra de peso por frase) em Playfair Display itálico 400, 88 px. Máximo 2 linhas (~20 caracteres por linha). Entra crescendo de 90% a 100% em 5 quadros.

## Materiais da Madu como apoio

Páginas inteiras dos planos de sono (proporção 1076 × 1521) sobre fundo névoa, uma página ou duas em leque. Usar páginas ainda não mostradas em Reels ([imagens.md](imagens.md)).

## Capa (arquivo à parte, `CapaMaduAcolher.jsx`)

- Criança coerente com o gancho no alto (rosto inteiro, y ≈ 240–450), máscara até ~780.
- Degradê branco suave (sem borda) de y 500 a 1020, opacidade 0,93 no meio.
- Gancho com a frase inteira em y 650: linha 1 Inter 800 74 px; linha 2 Playfair itálico 100 px sobre Pêssego, inclinada −1,2°.
- Madu embaixo com o fundo real, rosto começando em y ≈ 1090 (`ROSTO_Y`), dentro do recorte 4:5 do perfil (y 285–1635).
- Mostrar 3–4 opções de quadro da Madu (olhos abertos, expressão natural) e a Sarah escolhe. Aprovada em 14/10: quadro 37,9 s.
