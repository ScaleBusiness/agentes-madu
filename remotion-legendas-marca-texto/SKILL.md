---
name: remotion-legendas-marca-texto
description: Criar legendas no Remotion com marca-texto sincronizado palavra por palavra usando tempos de fala reais, Inter e Playfair Display Italic. Usar quando o pedido for destacar a palavra falada com fundo móvel ou realce por palavra.
---

# Legendas com marca-texto

Resultado: blocos legíveis de até duas linhas; uma faixa colorida aparece atrás da palavra enquanto ela é falada. Não pintar o fundo da frase inteira.

## Tempos e transcrição

Use palavras em JSON com `text`, `startMs`, `endMs`, `timestampMs` e `confidence` conforme Caption de @remotion/captions. Para renderização, derive páginas com `words` e marcação `emphasis`. O [componente reutilizável](assets/WordMarkerCaptions.tsx) define o esquema mínimo das páginas.

- Em vídeos Madu, mostrar a transcrição desde a primeira palavra; o gancho atual pertence apenas à capa separada. Uma linha ocupa a posição superior do bloco de duas, e ambas devem ter contraste constante.
- Revisar a transcrição antes de animar. Juntar tokens de uma mesma palavra (ex.: colocá + -la), mantendo o primeiro início e o último fim.
- Converter os tempos pelos cortes e pela velocidade real: num trecho contínuo `(tempoOriginal - inicioDoTrecho) / velocidade`. Se os tempos já são locais ao trecho, não subtrair o início novamente.
- Usar `startMs <= tempo < endMs` para o realce; em uma pausa não há palavra ativa. Nunca repartir a duração da frase igualmente pelo número de palavras: essa aproximação causa dessincronia.
- Os blocos podem ficar visíveis até o próximo bloco, mas o realce não deve continuar durante a pausa. Finalizar páginas em unidades de sentido e preservar até duas linhas.

## Visual

Inter para a base; Playfair Display Italic real em palavras significativas. Em vídeos Madu: Azul Noite #1F4B7A para o texto, Pêssego #FFDBD5 para o realce. Ajustar às instruções explícitas de outras marcas.

Use uma camada absoluta atrás de cada palavra, com largura automática do próprio texto. Ativar essa camada por quadro mantém os outros termos estáveis. Uma transição espacial entre palavras é opcional; se usada, medir posições reais e não animar através de linhas distintas.

Não alterar tamanho/peso quando a palavra se torna ativa. Nenhum fundo escuro envolvendo a frase. Texto não pode cobrir rosto/pescoço; reservar margem para a interface da plataforma. Quando o cenário não dá contraste, usar a área de transição prevista no layout. No padrão Madu, colocar a legenda no degradê central entre o apoio e a apresentadora; não cobrir o corpo dela com degradê inferior nem adicionar o cartão rejeitado.

O componente de referência usa medidas para o layout Madu 1080 × 1920. Ao reutilizar, adaptar posição, tamanho, largura e cores à composição; não tratar seus números como universais.

## Validação

Carregar e aguardar fontes locais válidas com @remotion/fonts. Verificar quadros antes, durante e depois de palavras selecionadas: no máximo um fundo ativo, sincronismo com timestamps, limite de duas linhas e nenhuma mudança de largura ao ativar. Rever o vídeo com áudio e verificar início/fim de frase. Manter JSON e transcrição salvos junto da edição.
