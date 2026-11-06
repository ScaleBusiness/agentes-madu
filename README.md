# Agentes de Marketing · Madu Drummond

Skills do Claude para o time de marketing da Madu.

## Instalação (primeira vez)

Cole os dois comandos abaixo no Terminal do seu Mac:

```bash
git clone https://github.com/ScaleBusiness/agentes-madu.git ~/.claude/skills-madu
bash ~/.claude/skills-madu/setup.sh
```

O script instala tudo automaticamente: FFmpeg, Python, Node.js, as 8 skills e o projeto Remotion para edição de Reels.

## Atualização

Sempre que a Sarah enviar atualizações, rode:

```bash
git -C ~/.claude/skills-madu pull && bash ~/.claude/skills-madu/setup.sh
```

## Skills disponíveis

| Skill | O que faz |
|---|---|
| `/edite-pro-madu` | Edita Reels: corte, trilha, legendas com marca-texto, efeitos |
| `/kelly-madu` | Cria conteúdo para o Instagram (posts, carrosséis, legendas) |
| `/quebra-de-objecoes-madu` | Contorna objeções, "Lembrei de Você" e reativa alunas |
| `/brenda` | Atendimento e suporte às clientes |
| `/ckm-design` | Design de materiais visuais |
| `/editordevideos-madu` | Editor de vídeos básico (versão anterior ao Edite Pro) |

## Requisitos

- Mac com macOS 12 ou mais recente
- Claude Desktop (ou Claude Code) instalado
- Terminal (já vem no Mac)

Dúvidas? Fala com a Sarah.
