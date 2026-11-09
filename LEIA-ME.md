# Configuração dos Assistentes — Madu Drummond

**Para a Madu:** Abra o Claude Desktop, vá na aba **Code**, arraste este arquivo para dentro da conversa e escreva:

```
instalar
```

O Claude instala tudo automaticamente. Pode levar 10 a 15 minutos na primeira vez (baixa o modelo de voz, que tem 1,5 GB).

---

## Para o Claude

Você está configurando o ambiente completo da Madu Drummond no Mac dela.
Execute os passos abaixo em ordem, sem pedir confirmação, usando o Bash diretamente.
Informe o progresso a cada passo com uma linha curta.

### Passo 1 — Homebrew

```bash
if ! command -v brew &>/dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    [ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"
fi
```

### Passo 2 — Dependências base

```bash
command -v ffmpeg &>/dev/null || brew install ffmpeg
command -v python3 &>/dev/null || brew install python3
command -v node &>/dev/null || brew install node
command -v git &>/dev/null || brew install git
```

### Passo 3 — Git LFS

```bash
if ! git lfs version &>/dev/null; then
    brew install git-lfs
    git lfs install
fi
```

### Passo 4 — Clonar ou atualizar o repositório

```bash
REPO="$HOME/.claude/skills-madu"
if [ -d "$REPO/.git" ]; then
    git -C "$REPO" pull --rebase
else
    git clone https://github.com/ScaleBusiness/agentes-madu.git "$REPO"
fi
# Baixar mídias via LFS (efeitos de vídeo, trilhas, overlays)
git -C "$REPO" lfs pull
```

### Passo 5 — Instalar skills e dependências

```bash
bash "$HOME/.claude/skills-madu/setup.sh"
```

### Passo 6 — Restaurar linhas de Python e Remotion nas skills de vídeo

Após o setup.sh, adicione ao final de `~/.claude/skills/edite-pro-madu/SKILL.md` (somente se a linha ainda não existir):

```
## Ambiente local
- Python: ~/.claude/skills/edite-pro-madu/.venv/bin/python3
- Remotion: ~/projeto-remotion-madu
```

Faça o mesmo para `~/.claude/skills/editordevideos-madu/SKILL.md`.

### Passo 7 — Chave SSH para o servidor Hostinger

```bash
SSH_KEY="$HOME/.ssh/id_ed25519_madu"
if [ ! -f "$SSH_KEY" ]; then
    ssh-keygen -t ed25519 -C "madu@madudrummond.com" -f "$SSH_KEY" -N ""
fi
# Configurar o host no SSH config
grep -q "Host madudrummond" ~/.ssh/config 2>/dev/null || cat >> ~/.ssh/config <<'EOF'

Host madudrummond
    HostName 179.236.254.65
    User root
    IdentityFile ~/.ssh/id_ed25519_madu
    StrictHostKeyChecking no
EOF
```

Depois, **exiba a chave pública** com:

```bash
cat "$HOME/.ssh/id_ed25519_madu.pub"
```

E informe a Madu: **"Copie a linha acima e adicione em hpanel.hostinger.com → VPS → Configurações → Chaves SSH → + Chave SSH"**

### Passo 8 — Testar conexão com o servidor

Só rodar DEPOIS de a Madu confirmar que adicionou a chave no painel:

```bash
ssh -o ConnectTimeout=10 madudrummond "echo 'Conexão OK — servidor Hostinger pronto'" 2>&1
```

### Passo 9 — Pasta do negócio

```bash
mkdir -p "$HOME/negocio-madu"
# Se ainda não tiver o CLAUDE.md, copiar do repositório
[ -f "$HOME/negocio-madu/CLAUDE.md" ] || \
    cp "$HOME/.claude/skills-madu/_contexto/CLAUDE.md" "$HOME/negocio-madu/CLAUDE.md"
```

### Passo 10 — Resultado

Ao terminar, liste o que foi instalado:

```bash
echo "=== Skills instaladas ==="
ls ~/.claude/skills | grep -E "madu|brenda|ckm|remotion"
echo ""
echo "=== Remotion ==="
[ -d ~/projeto-remotion-madu ] && echo "OK em ~/projeto-remotion-madu" || echo "FALTOU"
echo ""
echo "=== Chave SSH ==="
[ -f ~/.ssh/id_ed25519_madu.pub ] && echo "OK — adicionar no painel Hostinger se ainda não fez" || echo "FALTOU"
echo ""
echo "=== Pasta do negócio ==="
ls ~/negocio-madu/
```

E informe a Madu:

> **Instalação concluída.** Agora:
> 1. Abra o Claude Desktop → **Novo projeto** → aponte para a pasta `~/negocio-madu`
> 2. As skills disponíveis são: `/edite-pro-madu`, `/kelly-madu`, `/quebra-de-objecoes-madu`, `/brenda`, `/ckm-design`
> 3. Para editar um Reel: escreva `/edite-pro-madu` e arraste o vídeo
> 4. Para publicar uma página no seu site: peça ao Claude e ele faz o deploy direto no servidor

---

## Para atualizar no futuro

Quando a Sarah enviar novidades, Madu abre o Claude Code e escreve:

```
atualizar assistentes
```

O Claude roda:

```bash
git -C ~/.claude/skills-madu pull --rebase && \
git -C ~/.claude/skills-madu lfs pull && \
bash ~/.claude/skills-madu/setup.sh
```
