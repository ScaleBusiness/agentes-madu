# Editor de Vídeos SB — Guia de Instalação

## O que essa skill faz

Você grava o vídeo e o Claude entrega pronto para postar:

- encontra a frase mais forte da sua fala e coloca na abertura (o gancho);
- tira os respiros e as pausas longas, sem cortar nenhuma palavra;
- acelera levemente se você fala devagar, sem deixar a voz fina;
- deixa o vídeo no formato vertical das redes (1080×1920), com zoom leve nos cortes;
- entrega **duas versões com legenda**: uma para o **Instagram** e outra para o **TikTok** (com título no topo);
- corta também **Reels curtos** de 30 a 60 segundos com as melhores ideias do vídeo.

Seus vídeos ficam no seu computador. Não precisa de nenhuma chave de API.

---

## Antes de começar

- Um **Mac** (o Windows ainda não foi testado).
- Uma conta paga do **Claude** (Pro ou superior) com o **Claude Code** — pelo Terminal ou pela aba **Code** do aplicativo Claude.
- Uns 3 GB livres no computador e internet para a instalação.

---

## Instalação (uma vez só · ~10 minutos)

1. Descompacte a pasta **editordevideos-madu** que você recebeu.
2. Abra o aplicativo **Terminal** (aperte `Cmd + Espaço`, digite *Terminal* e dê Enter).
3. Digite `bash ` (com um espaço no final), **arraste o arquivo `setup-mentorado.sh`** da pasta para dentro do Terminal e aperte **Enter**.
4. Se ele pedir, digite a **senha do seu Mac** (as letras não aparecem enquanto você digita — é normal) e aperte Enter.
5. Espere aparecer **TUDO PRONTO!**

---

## Como usar

1. Abra o Claude Code.
2. Escreva `/editordevideos-madu` e **arraste o vídeo** para a conversa.
3. Se quiser só uma parte, diga: *"só o vídeo inteiro"* ou *"só os Reels curtos"*. Sem pedido, ele faz os dois.
4. Os vídeos prontos aparecem numa pasta **editados**, ao lado do vídeo original.

Quer mudar algo? É só pedir: *"usa outro gancho"*, *"troca o título do TikTok"*, *"deixa mais rápido"*, *"sem zoom"*.

---

## Problemas comuns

| O que aparece | O que fazer |
|---|---|
| `command not found: ffmpeg` | Rode o instalador de novo (passo 3). |
| `No module named faster_whisper` | Rode o instalador de novo (passo 3). |
| "OAuth token has expired" | Esse erro é do Claude, não da skill: escreva `/login` no Claude Code. |
| A primeira edição demora | Na primeira vez ele baixa o modelo de voz (~1,5 GB). Das próximas vezes é rápido. |
| O player mostra a versão antiga | Feche e abra o arquivo de novo. |

**Tempo de edição:** cerca de 2 a 3 minutos para cada minuto de vídeo.
