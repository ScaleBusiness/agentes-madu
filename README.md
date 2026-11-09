# Agentes de Marketing · Madu Drummond

Skills do Claude para o time de marketing da Madu. Preparado pela Sarah Brandão · Scale Business Academy.

## Como instalar (para a Madu)

**Opção 1 — pelo Claude (mais simples):**
Arraste o arquivo `LEIA-ME.md` para dentro do Claude Code e escreva `instalar`.

**Opção 2 — pelo Terminal (2 comandos):**

```bash
git clone https://github.com/ScaleBusiness/agentes-madu.git ~/.claude/skills-madu
git -C ~/.claude/skills-madu lfs pull
bash ~/.claude/skills-madu/setup.sh
```

O script instala tudo: FFmpeg, Python, Node.js, as 8 skills, o projeto Remotion e gera a chave SSH para o Hostinger.

## Como atualizar

```bash
git -C ~/.claude/skills-madu pull && git -C ~/.claude/skills-madu lfs pull && bash ~/.claude/skills-madu/setup.sh
```

## Skills disponíveis

| Skill | O que faz |
|---|---|
| `/edite-pro-madu` | Edita Reels: corte, trilha, legendas com marca-texto, efeitos |
| `/kelly-madu` | Cria conteúdo para o Instagram (posts, carrosséis, legendas) |
| `/quebra-de-objecoes-madu` | Contorna objeções, "Lembrei de Você" e reativa alunas |
| `/brenda` | Atendimento e suporte às clientes |
| `/ckm-design` | Design de materiais visuais |
| `/editordevideos-madu` | Editor de vídeos com Python/FFmpeg |
| `/remotion-madu-reels` | Composições Remotion dos Reels aprovados |
| `/remotion-legendas-marca-texto` | Legendas com marca-texto sincronizado |

## Requisitos

- Mac com macOS 12 ou mais recente
- Claude Desktop Pro com a aba Code ativada
- Terminal (já vem no Mac)
- Conta no GitHub (para git clone)

## Servidor Hostinger

O setup gera uma chave SSH (`~/.ssh/id_ed25519_madu`) e mostra a chave pública para adicionar em:
`hpanel.hostinger.com → VPS → Configurações → Chaves SSH → + Chave SSH`

Depois de adicionar, testar com: `ssh madudrummond`

Dúvidas? Fala com a Sarah.
