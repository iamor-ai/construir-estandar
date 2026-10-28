#!/bin/bash
# Genera el PDF de una ficha. Uso: generar_pdf.sh <ficha.md> <salida.pdf>
# Requiere Google Chrome instalado: en macOS (/Applications) o en Windows (con Git Bash).
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
python3 -I "$DIR/scripts/ficha_a_pdf_html.py" "$1" "$DIR/fuentes" > "$TMP/ficha.html"

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
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$SALIDA" "file:///${HTML#/}" 2>&1 | grep -o "[0-9]* bytes written" || true
rm -rf "$TMP"
