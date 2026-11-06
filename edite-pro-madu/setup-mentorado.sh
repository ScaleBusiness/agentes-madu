#!/bin/bash
# ============================================
# Edite Pro Madu — instalação automática (Mac)
# Rode dentro da pasta da skill:  bash setup-mentorado.sh
# ============================================

ORIGEM="$(cd "$(dirname "$0")" && pwd)"
SKILL_DEST="$HOME/.claude/skills/edite-pro-madu"
REMOTION_DEST="$HOME/projeto-remotion-madu"
AVISOS=0

echo ""
echo "==========================================="
echo "  Edite Pro Madu — Instalação"
echo "==========================================="
echo ""

echo ">> Homebrew..."
if ! command -v brew &> /dev/null; then
    echo "   Instalando o Homebrew (pode pedir a senha do seu Mac)..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    [ -x /opt/homebrew/bin/brew ] && eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo "   OK"
fi

echo ">> ffmpeg (corta e monta os vídeos)..."
command -v ffmpeg &>/dev/null && echo "   OK" || brew install ffmpeg

echo ">> Python 3..."
command -v python3 &>/dev/null && echo "   OK ($(python3 --version))" || brew install python3

echo ">> Node.js (para o Remotion)..."
if ! command -v node &>/dev/null; then
    echo "   Instalando Node.js..."
    brew install node
fi
echo "   OK ($(node --version))"

echo ">> Copiando a skill para o Claude..."
mkdir -p "$SKILL_DEST"
cp -R "$ORIGEM/." "$SKILL_DEST/"
echo "   OK"

echo ">> Ambiente Python (transcrição e legendas)..."
python3 -m venv "$SKILL_DEST/.venv" && \
"$SKILL_DEST/.venv/bin/pip" install -q --upgrade pip && \
"$SKILL_DEST/.venv/bin/pip" install -q faster-whisper pillow
"$SKILL_DEST/.venv/bin/python3" -c "import faster_whisper, PIL" &>/dev/null \
    && echo "   OK" || { echo "   AVISO: bibliotecas não instalaram. Mande um print para o suporte."; AVISOS=$((AVISOS+1)); }

echo ">> Baixando modelo de voz (uma vez só, ~1,5 GB)..."
"$SKILL_DEST/.venv/bin/python3" -c "from faster_whisper import WhisperModel; WhisperModel('medium', device='cpu', compute_type='int8')" &>/dev/null \
    && echo "   OK" || { echo "   AVISO: modelo será baixado na primeira edição."; AVISOS=$((AVISOS+1)); }

echo ">> Projeto Remotion (Madu)..."
if [ -d "$REMOTION_DEST" ]; then
    echo "   Já existe em $REMOTION_DEST"
else
    REPO_ROOT="$(dirname "$ORIGEM")"
    if [ -d "$REPO_ROOT/projeto-remotion-madu" ]; then
        cp -r "$REPO_ROOT/projeto-remotion-madu" "$REMOTION_DEST"
        cd "$REMOTION_DEST" && npm install --silent
        echo "   OK em $REMOTION_DEST"
    else
        echo "   AVISO: pasta projeto-remotion-madu não encontrada. Instale o repositório completo."
        AVISOS=$((AVISOS+1))
    fi
fi

echo ""
echo "==========================================="
if [ $AVISOS -eq 0 ]; then echo "  TUDO PRONTO!"; else echo "  QUASE PRONTO ($AVISOS aviso(s) acima)"; fi
echo "==========================================="
echo ""
echo "Como usar:"
echo "  1. Abra o Claude Code (no Terminal: claude — ou a aba Code do app Claude)"
echo "  2. Escreva: /edite-pro-madu e envie o vídeo"
echo ""
