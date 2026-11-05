---
name: remotion-madu-reels
description: Editar vídeos da Madu Drummond no Remotion com apoio visual acima da apresentadora desde a abertura, movimento suave e a tipografia de vídeo aprovada por Sarah. Usar nas amostras e Reels da Madu; não aplicar este visual a outras marcas automaticamente.
---

# Edição Remotion da Madu

Padrão definido por Sarah em 01/10/2026. Leia [direção visual e referência](references/direcao-visual.md) antes de escolher o layout.

- Inspecione a composição atual, o vídeo original e a referência enviada. Preserve versões anteriores para comparação.
- Madu permanece visível embaixo. Vídeo ou foto relacionado ao assunto permanece acima dela, desde o primeiro quadro. Para o relato atual, abrir com bebê chorando.
- Inter é a base dos textos; Playfair Display **Italic real, peso 400** destaca palavras significativas. O playbook orienta a paleta, mas não substitui essas fontes de vídeo por Raleway ou Scripter.
- Use a skill `remotion-legendas-marca-texto` para texto Azul Noite e realce Pêssego na palavra falada. Sem caixa escura envolvendo a frase inteira.
- Enquadrar a Madu mais de perto, com pouco espaço acima da cabeça. O degradê fica somente na divisão central entre as telas, nunca cobrindo o corpo na parte inferior. Manter movimentos suaves e não cortar a cabeça.
- O gancho “Deixe seu bebê chorar até dormir” pertence somente à capa separada. No vídeo completo, a legenda começa na primeira palavra: “Quando minha primeira filha nasceu...”. Não ocultar os segundos iniciais da transcrição para mostrar título. Preservar a explicação de que o conselho recebido gerou trauma.
- Na capa, escolher um quadro real da gravação com olhos abertos e expressão natural. Remover rótulos extras, inclusive “O CONSELHO QUE RECEBI”; manter somente o gancho aprovado. Não alterar artificialmente o rosto nem congelar toda a fala de abertura.
- Ampliar o gancho para a capa do Reels: na V6, Inter 108 px e Playfair Display Italic 128 px; na frase mais longa da edição completa, Inter 98 px e Playfair Display Italic 112 px, preservando as medidas menores das legendas. Manter ambos os rostos livres e conferir recorte/legibilidade. O gancho deve ser coerente com a fala, sem citações inventadas.
- A junção central não pode revelar uma linha horizontal ou borda reta. Preferir máscaras graduais nas próprias imagens; terminar cada imagem em transparência antes da sua borda física. Não confiar em uma camada de degradê parcialmente transparente para esconder um corte duro.
- Gancho e legendas nunca podem cobrir o rosto do bebê nem o da apresentadora. Usar a área central de texto, ajustar o enquadramento do apoio e conferir começo, fim e troca entre gancho e legenda.
- Legibilidade é obrigatória em todo o título e em todas as legendas. Ampliar a área clara do degradê quando a imagem de apoio reduzir o contraste; na abertura atual, a imagem superior desaparece completamente em y=705, antes da primeira linha azul. Conferir a frase inteira, sem cobrir os rostos nem criar uma linha na junção.
- Não exibir o rótulo “Imagem ilustrativa” sobre o apoio. Manter a fonte e o caráter ilustrativo documentados no relatório da edição.
- Escolher e sincronizar cada apoio pela frase da transcrição, não por intervalos fixos nem por palavras isoladas. Na fala sobre não tocar na filha ou ir até o berço, mostrar bebê chorando dentro do berço com atmosfera escura; nunca ilustrar essa passagem com colo. Reservar colo, amamentação e carinho para falas compatíveis. Variar cenas e evitar repetir a mesma foto de mãe triste.
- Legenda de uma linha ocupa a posição superior do bloco de duas linhas; não centralizar verticalmente mais abaixo. A área clara deve manter ambas as linhas legíveis, sem lacuna translúcida no meio.
- Use clipes de apoio pertinentes e documente a fonte. Preserve a voz original; deixe o apoio sem áudio, salvo pedido específico. Não confunda imagem ilustrativa com registro da família.
- Para o vídeo completo atual, usar 1,3×; Sarah considerou 1,2× lento em 02/10/2026. Sarah autorizou toda a gravação, com remoção de respiros e pausas excessivas, sem suprimir conteúdo da fala. Alternar fotos e vídeos pertinentes durante todo o relato. Em outros pedidos, respeitar o escopo e o ritmo definidos. Aceleração deve preservar o timbre e os tempos das legendas devem ser convertidos pela mesma velocidade.
- Cortar apenas com contexto e palavras completas. Identificar pausas não autoriza remover todas. O relato de uma orientação recebida não pode ser transformado em recomendação da Madu.
- Reutilize o projeto Remotion e carregue `remotion-best-practices` para APIs e renderização. Animações dependem do quadro; não usar animações CSS temporizadas.
- Verifique primeiro um quadro da abertura e outro no meio, incluindo contraste, fontes reais e limite de duas linhas. Depois renderize apenas o escopo autorizado, confira reprodução, áudio, duração e ausência de congelamentos.
- Salve no projeto local solicitado e entregue os caminhos e a prévia. Esta skill não autoriza upload, publicação ou edição do vídeo completo quando o pedido é uma amostra.
