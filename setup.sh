#!/bin/bash
# ============================================================
# Agentes de Marketing — instalação completa (Mac)
# Instala TODAS as skills da Madu no Claude em um só comando.
#
# Uso:
#   git clone https://github.com/ScaleBusiness/agentes-madu.git ~/.claude/skills-madu
#   bash ~/.claude/skills-madu/setup.sh
#
# Atualização futura:
#   git -C ~/.claude/skills-madu pull && bash ~/.claude/skills-madu/setup.sh
# ============================================================

REPO="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
REMOTION_DEST="$HOME/projeto-remotion-madu"
AVISOS=0

echo ""
echo "============================================="
echo "  Agentes de Marketing — Instalação"
echo "============================================="
echo ""

# ── Pré-requisitos ───────────────────────────────

echo ">> Homebrew..."
if ! command -v brew &>/dev/null; then
    echo "   Instalando (pode pedir a senha do Mac)..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    [ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "   OK"
fi

echo ">> ffmpeg..."
command -v ffmpeg &>/dev/null && echo "   OK" || brew install ffmpeg

echo ">> Python 3..."
command -v python3 &>/dev/null && echo "   OK ($(python3 --version))" || brew install python3

echo ">> Node.js (para o Remotion)..."
if ! command -v node &>/dev/null; then
    echo "   Instalando Node.js..."
    brew install node
fi
echo "   OK ($(node --version))"

# ── Copiar todas as skills ───────────────────────

SKILLS=(
    brenda
    kelly-madu
    edite-pro-madu
    editordevideos-madu
    quebra-de-objecoes-madu
    ckm-design
    remotion-legendas-marca-texto
    remotion-madu-reels
)

echo ""
echo ">> Copiando skills para o Claude..."
mkdir -p "$SKILLS_DIR"
for skill in "${SKILLS[@]}"; do
    if [ -d "$REPO/$skill" ]; then
        cp -R "$REPO/$skill" "$SKILLS_DIR/"
        echo "   ✓ $skill"
    else
        echo "   ! $skill não encontrada no repositório"
        AVISOS=$((AVISOS+1))
    fi
done

# ── Ambiente Python para a edite-pro-madu ───────

echo ""
echo ">> Ambiente Python (transcrição e legendas)..."
VENV="$SKILLS_DIR/edite-pro-madu/.venv"
python3 -m venv "$VENV" && \
"$VENV/bin/pip" install -q --upgrade pip && \
"$VENV/bin/pip" install -q faster-whisper pillow
"$VENV/bin/python3" -c "import faster_whisper, PIL" &>/dev/null \
    && echo "   OK" || { echo "   AVISO: bibliotecas não instalaram. Mande um print para o suporte."; AVISOS=$((AVISOS+1)); }

echo ">> Baixando modelo de voz (uma vez só, ~1,5 GB)..."
"$VENV/bin/python3" -c "from faster_whisper import WhisperModel; WhisperModel('medium', device='cpu', compute_type='int8')" &>/dev/null \
    && echo "   OK" || { echo "   AVISO: modelo será baixado na primeira edição."; AVISOS=$((AVISOS+1)); }

# ── Projeto Remotion ─────────────────────────────

echo ""
echo ">> Projeto Remotion (Madu)..."
if [ -d "$REMOTION_DEST" ]; then
    echo "   Já existe em $REMOTION_DEST — atualizando arquivos..."
    cp -Rf "$REPO/projeto-remotion-madu/." "$REMOTION_DEST/"
    cd "$REMOTION_DEST" && npm install --silent && cd -
    echo "   OK"
elif [ -d "$REPO/projeto-remotion-madu" ]; then
    cp -r "$REPO/projeto-remotion-madu" "$REMOTION_DEST"
    cd "$REMOTION_DEST" && npm install --silent && cd -
    echo "   OK em $REMOTION_DEST"
else
    echo "   AVISO: pasta projeto-remotion-madu não encontrada no repositório."
    AVISOS=$((AVISOS+1))
fi

# ── Resultado ─────────────────────────────────────

echo ""
echo "============================================="
if [ $AVISOS -eq 0 ]; then
    echo "  TUDO PRONTO!"
else
    echo "  QUASE PRONTO ($AVISOS aviso(s) acima)"
fi
echo "============================================="
echo ""
echo "Skills instaladas em: $SKILLS_DIR"
echo ""
echo "Como usar no Claude:"
echo "  /edite-pro-madu    → editar Reels com trilha, legendas e efeitos"
echo "  /kelly-madu        → criar conteúdo para o Instagram"
echo "  /quebra-de-objecoes-madu → contornar objeções e reativar alunas"
echo "  /brenda            → atendimento e suporte"
echo "  /ckm-design        → design de materiais"
echo ""
echo "Para atualizar no futuro:"
echo "  git -C ~/.claude/skills-madu pull && bash ~/.claude/skills-madu/setup.sh"
echo ""
