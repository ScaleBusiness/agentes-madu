---
name: editordevideos-madu
description: Editar vídeos da Madu Drummond com voz e sentido preservados, Inter e Playfair Display Italic, apoio visual acima da apresentadora e marca-texto sincronizado. Usar para vídeos, Reels, legendas e amostras da Madu; usar Remotion quando solicitado.
---

# Editor de vídeos — Madu Drummond

## Padrão vigente — Sarah, 01/10/2026

Esta entrada substitui as regras visuais conflitantes da versão anterior. O conteúdo anterior está preservado em `references/historico-antes-remotion-2026-10-01.md`, como histórico, não como padrão ativo.

- Inter é a fonte base. Playfair Display Italic real, peso 400, destaca palavras significativas. Para vídeos, não substituir por Raleway, Scripter ou fontes manuscritas do playbook.
- Composição dinâmica: apoio visual relacionado à fala acima; Madu abaixo, visível. No modelo atual, o apoio aparece desde o primeiro quadro e permanece durante toda a amostra. Abrir com bebê chorando no relato solicitado por Sarah.
- Marca-texto Pêssego #FFDBD5 acompanha a palavra falada, com texto Azul Noite #1F4B7A e fundo claro suficiente para contraste. Retirar a caixa escura envolvendo a frase. No máximo duas linhas e nenhuma legenda no rosto/pescoço.
- Madu em enquadramento próximo, com pouco espaço acima da cabeça. Degradê e legenda ficam na divisão central entre as telas, sem degradê cobrindo o corpo embaixo. Aplicar movimentos suaves por quadro, respeitando a cabeça.
- Gancho “Deixe seu bebê chorar até dormir” somente na capa separada. O vídeo recebe legendas desde a primeira palavra, sem ocultar a fala inicial. Preservar Inter, Playfair Display itálica e marca-texto por palavra. Uma linha sempre na posição superior do bloco de duas; contraste legível nas duas linhas.
- Na capa, escolher um quadro real da gravação com olhos abertos e expressão natural. Remover rótulos extras, inclusive “O CONSELHO QUE RECEBI”; manter somente o gancho aprovado. Não alterar artificialmente o rosto nem congelar toda a fala de abertura.
- Sincronizar os apoios pelas frases da transcrição. No relato de não tocar na filha nem ir até o berço, usar bebê chorando no berço em ambiente escuro; nunca colo. Variar cenas de mães aflitas, estudo e acolhimento conforme a fala. Registrar fontes e tempos.
- A junção entre os vídeos deve ser contínua, sem linha horizontal visível. Nenhum gancho ou legenda pode cobrir o rosto do bebê ou da Madu; reservar área livre e conferir durante o movimento.
- Não colocar “Imagem ilustrativa” sobre o vídeo. Documentar a origem do apoio no relatório local, sem sugerir que seja registro da família.
- Preservar a voz; manter o vídeo de apoio sem som, salvo pedido específico. Na edição completa atual, usar 1,3× com timbre preservado, conforme ajuste solicitado em 02/10/2026.
- Frases atribuídas a terceiros continuam sendo relatos, não recomendações. Não cortar automaticamente todas as pausas, não amputar palavras e não reorganizar o sentido.
- Entregar o escopo pedido: uma amostra de até 15 segundos não autoriza editar ou publicar a gravação inteira. Perguntas já respondidas sobre legendas, destino e formato não precisam ser repetidas.
- O destino atual é o projeto local de edição. Não subir ao Drive, enviar mensagens ou publicar por instruções antigas da skill.

## Fluxo

1. Inspecionar original, transcrição, referência visual e projeto existente. Para estratégia editorial mais ampla, ler [protocolo estratégico](references/protocolo-estrategico.md) apenas quando o pedido envolver seleção de gancho ou compilado.
2. Manter o motor Python/FFmpeg existente em `motor/` disponível para operações locais. A pasta `assets/` contém fontes e recursos; validar arquivos antes de usar. Não instalar ambientes nem trocar ferramentas que já funcionam sem necessidade.
3. Em Remotion, usar as skills `remotion-madu-reels`, `remotion-legendas-marca-texto` e `remotion-best-practices`. As novas skills estão em `~/.codex/skills/`; carregar os respectivos SKILL.md. Reutilizar a composição existente e preservar versões anteriores.
4. Revisar transcrição e tempos após a aceleração. O marca-texto usa os tempos reais das palavras, não uma duração média por palavra.
5. Conferir quadros da abertura, do meio e do fim e comparar com a referência; renderizar somente a entrega solicitada. Validar duração, legibilidade, som e ausência de congelamentos.
6. Entregar o arquivo local, a transcrição e o endereço de prévia quando disponível. Descrever o que foi testado e manter ajustes não aprovados como amostra para revisão.

<!-- regras-playbook-08out:LEG:BEGIN -->
## Regras de legibilidade (INEGOCIÁVEL · Sarah 08/10/2026)
Vale para toda peça com texto: carrossel, capa, stories, reels, vídeo, criativo, página, app e playbook. Origem: reprovações da Sarah entre 30/09 e 08/10. Lista completa: `metodo-scale-business/regras-playbook-visual-consolidadas-08out.md`.
1. **Contraste medido na área real.** Texto sobre foto ou vídeo: medir a cor média da faixa onde a palavra fica (5 a 6 quadros, no vídeo) e exigir 3:1 ou mais em todos. Texto de leitura: 4,5:1 ou mais. Medir contra a paleta não vale.
2. **Palavra de destaque nunca fica transparente, apagada ou misturada com a foto.** Efeito de movimento ou sombra só entra depois que a leitura está garantida, e nunca reduz o contraste da letra.
3. **Nunca texto, linha, moldura ou seta sobre o rosto.** O texto começa abaixo do queixo. Rodar `checar-rosto.py` em todo card com foto.
4. Fundo escuro leva texto claro; fundo claro leva texto escuro. Serifa fina sobre foto e rosa ou dourado claro sobre fundo claro são ilegíveis e proibidos.
5. Ao trocar a paleta de uma peça, medir o contraste de todos os elementos por script (botão, rótulos, nomes), não só do título.
6. **A paleta e o estilo saem do que a Sarah enviou** (Pantone, HEX, posts de referência). Nunca inventar cor. Cor que ela descartou não volta.
7. Antes de mostrar: olhar a peça renderizada (há divisão visível? o rosto está limpo? o texto está legível e fora das zonas?). Para a Sarah escolher entre opções, mostrar a **imagem** no chat; nunca só o nome ou a descrição da cor.
<!-- regras-playbook-08out:LEG:END -->

<!-- regras-playbook-08out:ESCOLHA:BEGIN -->
## Escolha visual = a Sarah VÊ antes de decidir (INEGOCIÁVEL · Sarah 08/10/2026)
> *"Eu não escolho pelo nome da cor, eu escolho pela cor que eu vejo."*
- **Nunca pedir à Sarah que escolha cor, paleta, fonte, foto, layout ou estilo sem mostrar a imagem NA MESMA mensagem.** Enviar a prancha ou a peça renderizada pelo SendUserFile (`display: render`) antes da pergunta.
- Nome de cor, código HEX, tabela, descrição ("laranja intenso", "verde vivo") ou caminho de arquivo **não contam como mostrar**.
- A imagem mostra a opção **aplicada em peças reais e legíveis** (capa, post de número, post de frase), uma ao lado da outra, na mesma escala, com o mesmo texto e a mesma foto. Só a cor muda.
- Vale também para handoff, resumo e pendência: se uma decisão visual ficar em aberto, a imagem vai junto ou o caminho dela fica registrado com a instrução "mostrar antes de perguntar".
- **Toda cor que aparece na faixa da paleta aparece aplicada em pelo menos uma das peças** (inclusive a de detalhe pontual). Cor que está na faixa e não aparece em nenhuma peça = a Sarah não consegue avaliar = prancha reprovada ("cadê o laranja aqui?", 08/10).
<!-- regras-playbook-08out:ESCOLHA:END -->

<!-- regras-playbook-08out:VIDEO_MADU:BEGIN -->
## Regras de vídeo e legenda (Sarah, 08/10/2026)
> **Na Madu vale o padrão de legenda desta própria skill** (seção "Padrão vigente": Inter 800 em Azul Noite, marca-texto Pêssego na palavra falada, Playfair Display itálico no destaque, brilho branco atrás; conferido nos Reels aprovados de 05 a 07/10). Referência visual oficial: seção 10 do Playbook da Madu (`Madu Drummond/Playbook visual/`). O padrão de Montserrat 700 abaixo é dos vídeos das outras mentoradas e NÃO substitui o dela. Zona de legenda, rosto, contraste, tela dividida, CTA e tira de quadros valem para a Madu.
- **A legenda nunca fica no canto inferior da tela:** ali ela cai sobre a legenda do post e a pessoa não lê nenhuma das duas. Proposta, a confirmar: a legenda não passa de y 1480 em 1080 × 1920 (valor do vídeo aprovado da Madu, que deixa cerca de 440 px livres embaixo).
- Gancho fixo só nos primeiros 5 s, abaixo do queixo, nunca sobre o rosto. Cartela e legenda também abaixo do queixo. A legenda do conteúdo começa cerca de 3 s depois do início, porque o começo vira a capa.
- Padrão de legenda (08/10, referência "um herói"): Montserrat 700 branca, cerca de 80 px, 1 a 3 palavras por vez, minúsculas como na fala, sem caixa, marca-texto nem contorno, sombra escura suave. Destaque em no máximo 1 palavra (Awesome ou Playfair em itálico). Na tela dividida, na junção do degradê, acima da cabeça. O 700 é exceção só da legenda de vídeo; peças estáticas e interface nunca passam de 600.
- Reprovados: marca-texto palavra a palavra, legenda pequena e fina, caixas brancas, faixa branca, serifa fina sobre foto, palavra dourada sobre o rosto.
- Contraste do texto sobre vídeo: medir a faixa onde ele fica em 5 a 6 quadros; 3:1 ou mais em todos.
- Tela dividida: as duas imagens em largura total, junção por degradê entre vídeo e vídeo; nunca faixa, linha nem vídeo encolhido com laterais desfocadas.
- CTA final em tela cheia, pessoa ampliada, texto sobre o busto, palavra-chave em destaque.
- Movimento: entrada com subida de 12 px (300 a 450 ms), fade de 200 ms entre blocos; nunca bounce, giro, glitch nem duas animações ao mesmo tempo.
- Antes de entregar: olhar uma tira de quadros e conferir que não há trecho parado; o vídeo já abre em movimento.
<!-- regras-playbook-08out:VIDEO_MADU:END -->
