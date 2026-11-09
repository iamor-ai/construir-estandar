#!/bin/bash
# Genera el PDF de una ficha. Uso: generar_pdf.sh <ficha.md> <salida.pdf>
# Requiere Google Chrome instalado: en macOS (/Applications) o en Windows (con Git Bash).
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"

# Busca el intérprete de Python (igual que el hook: Windows a veces no tiene 'python3')
PY=""
for p in python3 python py; do
  if command -v "$p" >/dev/null 2>&1; then
    if [ "$p" = "py" ]; then PY="py -3"; else PY="$p"; fi
    break
  fi
done
if [ -z "$PY" ]; then echo "FALTA_PYTHON"; exit 2; fi

$PY -I "$DIR/scripts/ficha_a_pdf_html.py" "$1" "$DIR/fuentes" > "$TMP/ficha.html"

# Busca Chrome en macOS y en Windows (Git Bash)
CHROME=""
for c in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/c/Program Files/Google/Chrome/Application/chrome.exe" \
  "/c/Program Files (x86)/Google/Chrome/Application/chrome.exe" \
  "$(cygpath -u "${LOCALAPPDATA:-/nonexistent}" 2>/dev/null)/Google/Chrome/Application/chrome.exe"; do
  if [ -x "$c" ]; then CHROME="$c"; break; fi
done
if [ -z "$CHROME" ]; then echo "FALTA_CHROME"; exit 3; fi

# En Windows, Chrome necesita rutas de Windows (C:/...) y no las de Git Bash (/c/...)
if command -v cygpath >/dev/null 2>&1; then
  HTML="$(cygpath -m "$TMP/ficha.html")"
  SALIDA="$(cygpath -m "$2")"
else
  HTML="$TMP/ficha.html"
  SALIDA="$2"
fi
rm -f "$2"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$SALIDA" "file:///${HTML#/}" 2>&1 | grep -o "[0-9]* bytes written" || true
rm -rf "$TMP"
# Si Chrome no escribió el archivo, el fallo tiene que verse: no se entrega un PDF que no existe
if [ ! -s "$2" ]; then echo "ERROR_PDF: Chrome no escribió el PDF en $2"; exit 4; fi
