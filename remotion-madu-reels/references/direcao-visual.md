# Direção visual de vídeo — 01/10/2026

Referência estrutural enviada: `/Users/sarahbrandao/Downloads/dr.jorgecavalcanti_Dd4CCRtRnwt.mp4`. A abertura combina imagem de apoio acima e apresentador abaixo, com legendas curtas e mudanças de escala. Sarah ampliou a regra: nos vídeos da Madu, manter o apoio acima durante todo o trecho. Não copiar o conteúdo, as cores amarelas nem a tipografia do vídeo de referência.

Referência de marca: `/Users/sarahbrandao/escritorioscalebusiness/produtos/mentoria-individual/Madu Drummond/Playbook visual/Playbook Visual - Madu Drummond.pdf`.
Cores: Azul Noite #1F4B7A; Céu #AEDDED; Névoa #EEF6FB; Pêssego #FFDBD5. O print enviado por Sarah em 01/10 às 21:01 mostra texto azul sobre fundo claro, com marca-texto pêssego por trás de palavras. Aplicar o destaque à fala, sem uma pílula escura para toda a legenda.

Base de composição em 1080 × 1920 (ajustar após inspecionar o rosto):
- Correção posterior de Sarah em 01/10: o degradê deve ficar na divisão central, Madu precisa aparecer mais próxima e o rótulo “Imagem ilustrativa” deve sair. Incluir gancho visual; preservar o estilo de legenda aprovado.
- Correção das 21:42: nenhuma linha visível na junção e nenhum texto sobre o rosto do bebê. Preservar o estilo de legendas aprovado.
- V6: desvanecer as próprias imagens com máscaras de transparência sobre #EEF6FB. O apoio termina visualmente em y=810; a imagem de Madu entra suavemente de y=800 a y=950. Não há borda física visível em y=920.
- Para destaque na capa: gancho centralizado em y=795, Inter 108 px e Playfair Display Italic 128 px. A imagem do bebê começa em y=0 com altura 920 px e deslocamento interno -100 px. A legenda mantém centro y=830 e as fontes menores aprovadas. Não colocar texto sobre os rostos.
- Base Inter 800 em torno de 66 px; palavras de destaque Playfair Display Italic 400 em torno de 82 px. Ajustar proporcionalmente ao layout e à largura real, não aumentar destaque 3,5× por padrão.
- Marca-texto #FFDBD5 com texto #1F4B7A; apenas a palavra ativa tem fundo. Não alterar fonte/peso no instante de ativar a palavra: isso muda largura e faz a legenda saltar.
- Ajustar a escala à imagem original, mantendo pouco espaço acima da cabeça. Na V4, escala 1,62–1,665, origem superior central e deslocamento vertical -180 px no painel de 1000 px. Pan horizontal até 10 px. Conferir visualmente antes de reutilizar esses números em outro vídeo.

A estética da amostra `src/MaduV6.tsx` foi aprovada por Sarah para aplicação ao vídeo inteiro. A composição completa está em `src/MaduCompleto.tsx`, no projeto `/Users/sarahbrandao/Documents/ChatGPT/Edição de Vídeos/meu-primeiro-projeto`. Cortes, palavras e apoios permanecem em `out/completo/timeline.json`.

Fontes locais: Inter-VF.ttf na pasta assets da skill original Madu; PlayfairDisplay-Italic.ttf em ~/Library/Fonts. Verificar formato real com file/fontTools: nesta máquina um arquivo chamado Inter-ExtraBold.otf contém HTML, não uma fonte. Usar arquivos válidos, carregar explicitamente e aguardar as fontes antes de renderizar.

## Ajustes de 02/10/2026

As instruções abaixo substituem os parâmetros anteriores quando houver conflito. Gancho apenas na capa separada; transcrição completa desde o primeiro quadro. Velocidade 1,3× com timbre preservado. Uma linha de legenda alinhada à primeira linha do bloco de duas; na composição atual, bloco em y=728. Faixa branca contínua entre y=705 e y=950, com transições fora do texto. Uma fusão direta dos dois vídeos por máscara de gradiente é outro acabamento possível; a montagem vigente utiliza a faixa branca para garantir o contraste do texto azul.

Cada plano deve ter trecho da fala e tempos registrados. No conselho do pediatra, mostrar bebê chorando no berço em atmosfera escura. Fotos com movimento são permitidas. Não usar colo nesse trecho; não repetir cenas de tristeza indiscriminadamente nas falas sobre estudo, rotina e acolhimento.
