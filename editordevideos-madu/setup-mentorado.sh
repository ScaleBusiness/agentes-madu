#!/bin/bash
# ============================================
# Editor de Vídeos SB — instalação automática (Mac)
# Rode dentro da pasta da skill:  bash setup-mentorado.sh
# ============================================

ORIGEM="$(cd "$(dirname "$0")" && pwd)"
DESTINO="$HOME/.claude/skills/editordevideos-madu"
AVISOS=0

echo ""
echo "========================================="
echo "  Editor de Vídeos SB — Instalação"
echo "========================================="
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
if ! command -v ffmpeg &> /dev/null; then
    echo "   Instalando (pode levar alguns minutos)..."
    brew install ffmpeg
else
    echo "   OK"
fi

echo ">> Python 3..."
if ! command -v python3 &> /dev/null; then
    brew install python3
else
    echo "   OK ($(python3 --version))"
fi

echo ">> Copiando a skill para o Claude..."
mkdir -p "$DESTINO"
if [ "$ORIGEM" != "$DESTINO" ]; then
    cp -R "$ORIGEM/." "$DESTINO/"
fi
echo "   OK"

echo ">> Ambiente da skill (transcrição e legendas)..."
python3 -m venv "$DESTINO/.venv" && \
"$DESTINO/.venv/bin/pip" install -q --upgrade pip && \
"$DESTINO/.venv/bin/pip" install -q faster-whisper pillow
if "$DESTINO/.venv/bin/python3" -c "import faster_whisper, PIL" &> /dev/null; then
    echo "   OK"
else
    echo "   AVISO: as bibliotecas não instalaram. Mande um print desta tela para o suporte."
    AVISOS=$((AVISOS+1))
fi

echo ">> Baixando o modelo de voz (uma vez só, ~1,5 GB)..."
"$DESTINO/.venv/bin/python3" -c "from faster_whisper import WhisperModel; WhisperModel('medium', device='cpu', compute_type='int8')" &> /dev/null \
    && echo "   OK" || { echo "   AVISO: o modelo será baixado na primeira edição."; AVISOS=$((AVISOS+1)); }

echo ""
echo "========================================="
if [ $AVISOS -eq 0 ]; then echo "  TUDO PRONTO!"; else echo "  QUASE PRONTO ($AVISOS aviso(s) acima)"; fi
echo "========================================="
echo ""
echo "Como usar:"
echo "  1. Abra o Claude Code (no Terminal: claude  —  ou a aba Code do app Claude)"
echo "  2. Escreva:  /editordevideos-madu  e arraste o vídeo para a conversa"
echo ""
