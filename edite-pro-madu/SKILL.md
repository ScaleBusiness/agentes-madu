---
name: edite-pro-madu
description: Edição premium de Reels da Madu Drummond (Consultoria Sleepy, sono infantil) no padrão do Playbook Visual dela, com o processo técnico da Edite Pro. Use quando a Sarah pedir "Edite Pro Madu", "editar o reel da Madu", "vídeo da Madu" ou qualquer Reel/capa da Madu. imagens de apoio que não repetem as dos últimos 3–4 Reels, crianças de 6 meses a 4 anos, legenda Azul Noite com marca-texto Pêssego no busto, piano calmo baixinho por baixo da voz, sem efeito sonoro e sem névoa.
---

# EDITE PRO · Madu Drummond

A Edite Pro (`/edite-pro`) dá o processo técnico (corte sem respiro, Studio aberto, conferência quadro a quadro, exportação). A identidade, a legenda, a capa e as regras de imagem vêm do **Playbook da Madu** e das decisões da Sarah registradas aqui. Modelo aprovado: Reel "Acolher o choro" (14/10/2026), composição em `assets/modelo/`.

## Mapa de Cenas · OBRIGATÓRIO antes de editar (regra SB 22/10 · todas as skills Pro desde 31/10)
Nome oficial: **Mapa de Cenas** (nunca "storyboard"). Sem Mapa de Cenas aprovado, a edição não começa.
1. Transcrever → cortar → dividir a fala em GANCHO → CONTEXTO → CONTEÚDO → CTA e depois em blocos, um por ideia.
2. Montar uma página (HTML, aberta no navegador) com **um quadro real do vídeo por bloco** e, em cada bloco: a fala, o que aparece na tela, o efeito, o material (com a origem), o som (qual e em que palavra), opções A e B só quando as duas são boas, e o aviso do que gastaria crédito de IA. Texto mostrado no tamanho e na cor reais sobre o quadro.
3. Material que falta aparece como "Falta: …" no bloco, nunca trocado pelo que estiver à mão.
4. Aprovação bloco a bloco → amostra de 8 a 15 s → vídeo inteiro.

## Antes de editar

1. Ler o hub da Madu na memória (`hub_madu.md`) e [video.md](references/video.md).
2. Ler [imagens.md](references/imagens.md): **a lista de imagens já usadas em Reels da Madu, em ordem**. Nada dos 3–4 Reels anteriores pode voltar.
3. Ler [reprovacoes.md](references/reprovacoes.md) e, de novo, antes de mostrar.
4. Abrir o Remotion Studio (`remotion-studio-3010`, projeto `edicao-de-videos/projeto-remotion/`) na composição do vídeo e manter aberto. Comandos em [fluxo.md](references/fluxo.md).
5. Pedir só o que faltar: bruto original (o da Drive "Vídeos originais", nunca uma versão já cortada), roteiro/palavra-chave do CTA (Notion), material citado.

## Regras da Madu (inegociáveis)

- **SIGILO DAS FAMÍLIAS (Sarah 14/10, vale para vídeo e para qualquer material):** nunca mostrar dado que identifique família ou criança: nomes (mãe, pai, criança, irmãos), idade, data de nascimento, assinatura de mensagem, número de telefone, foto de perfil. Antes de usar plano de sono, print de WhatsApp ou depoimento: `python3 scripts/anonimizar.py entrada.jpg saida-sigilo.jpg` (OCR do macOS acha os nomes e cobre), cortar assinatura e cabeçalho do print e **olhar a imagem inteira** antes de pôr no vídeo. Original com dado vai para `_com-dados-nao-usar/`, nunca entra no render. A foto do bebê na capa do Plano de Sono é arte padrão da Madu (não é cliente): pode aparecer.

- **Imagens não se repetem em Reels seguidos.** Uma imagem usada num Reel só pode voltar 3 ou 4 Reels depois; mesmo assim, evitar repetir sempre que houver opção nova (Sarah 14/10). Conferir [imagens.md](references/imagens.md) e acrescentar as usadas ao terminar.
- **Idade da criança: 6 meses a 4 anos.** Nunca recém-nascido e nunca criança que pareça ter mais de 4 anos (a Madu só atende até 4). Na dúvida, não usar.
- **A Sarah escolhe vendo.** Mostrar prancha com as imagens candidatas e pedir licença antes de baixar do Pexels.
- **Legenda NUNCA no rosto** (nem da Madu, nem da criança, nem nas transições):
  - tela cheia: **no alto do busto**, logo abaixo do queixo (medir com Vision em cada gravação). **O bloco inteiro (até 2 linhas, 100 px cada) termina antes de y 1480** (regra 08/10; Sarah cobrou em 21/10: "o que já falamos sobre isso???"). Referências: microfone no queixo 1270 · boneca no colo 1160–1180 · bastidor na mesa 1080. CTA idem (≈ 1060–1150). Nunca embaixo, no pé do quadro.
  - tela dividida: presa por baixo na junção (base y ≈ 872), com a Madu descida até o cabelo ficar abaixo da legenda (VIDEO_Y_DIV ≈ 690). Medir o rosto do bruto com Vision antes ([fluxo.md](references/fluxo.md)).
  - some durante a troca de tela.
- **Visual da legenda (Playbook seção 10):** Inter 800, 68 px, Azul Noite #1F4B7A, brilho branco difuso atrás; marca-texto Pêssego #FFDBD5 na palavra falada; destaque em Playfair Display itálico 88 px; no máximo 2 linhas.
- **Sem névoa e sem swish/deslize nos cortes.** Vazamento de luz por cima da imagem = "névoa horrorosa"; swish/deslize nos cortes = "efeito sonoro ruim" (14/10). As transições ficam só no zoom + desfoque de 6 quadros em cada corte.
- **Curadoria de áudio (Sarah 14/10: "isso é para tudo"):** a skill escolhe a trilha pelo clima do vídeo. Para o conteúdo calmo da Madu, o piano abaixo é a aprovada e o ponto de partida; a skill pode variar entre trilhas calmas. Registrar em `trabalho-<video>/sons.md`. Regras em `edite-pro/references/fluxo.md`, F5.
- **Trilha aprovada (ponto de partida): piano calmo** (`assets-edite/sons/trilhas/classica-drive/Lyrical Piano Advertising Background 2 Underscore.mp3`), **baixinho**: voz normalizada em −15 LUFS, piano em −37 LUFS e abaixando ainda mais quando ela fala (sidechain). "Pra quê essa altura? Nem consigo ouvir a Madu" — a música nunca compete com a voz. Comando em [fluxo.md](references/fluxo.md).
- **Abertura:** a Madu já falando e em movimento, apoio em cima desde o quadro 0; sem gancho escrito por cima e sem quadro congelado.
- **Capa** (arquivo à parte, [video.md](references/video.md)): frase inteira do gancho, criança coerente com o gancho (se o gancho fala de choro, criança CHORANDO), degradê branco suave atrás da frase para contraste, frase longe da testa da Madu, quadro da Madu escolhido pela Sarah entre opções.
- **Chamada final:** tela cheia, Madu ampliada, "Comente / PALAVRA (Playfair sobre Pêssego) / complemento" no busto; depois a palavra-chave sozinha +1,2 s com a logo.
- **Fala:** corrigir só o que a Sarah mandar (ex.: tirar "três" de "três planos": a Consultoria é 2 planos + Plano de Fechamento). Nunca inventar palavra.
- **Aprovou, congela:** guardar cópia antes de cada rodada (`trabalho-<video>/<Arquivo>-antes-<assunto>.jsx`) e mudar só o pedido.

## Fluxo

| Etapa | Resultado | Onde |
|---|---|---|
| F0 Preparação | bruto em `brutos/AAAA-MM-DD-madu-<video>/`, take H.264 + `-x1.3`, Studio aberto | [fluxo.md](references/fluxo.md) |
| F1 Cortes e legenda | transcrição por palavra, régua sensível, `montar.py` (GRUPOS revisados) | `scripts/medir.py`, `scripts/montar.py` |
| F2 Imagens | candidatos novos (6m–4a) → prancha → Sarah escolhe → baixar → converter 1080 | [imagens.md](references/imagens.md) |
| F3 Composição | copiar `assets/modelo/MaduAcolher.jsx`, trocar DIVIDIDA/APOIO/G() | Studio |
| F4 Conferência | um quadro por frase + rosto nas transições + fala transcrita | `scripts/quadros.mjs`, `scripts/confere_fala.py` |
| F5 Capa | opções do quadro da Madu → Sarah escolhe | `assets/modelo/CapaMaduAcolher.jsx` |
| F6 Exportação | render sem trilha → mixagem com piano (sidechain) → final + celular + capa | [fluxo.md](references/fluxo.md) |

## Entrega

`edicao-de-videos/renders/AAAA-MM-DD-madu-<video>.mp4` + `-celular.mp4` + capa PNG/JPG/recorte 4:5. Mostrar no chat (SendUserFile). Ao aprovar: subir no Drive da Madu e acrescentar as imagens usadas em [imagens.md](references/imagens.md), na ordem de postagem. Nunca publicar (a Madu posta).

Invocação: `/edite-pro-madu`.
