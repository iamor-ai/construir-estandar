#!/bin/bash
# Genera el PDF de una ficha. Uso: generar_pdf.sh <ficha.md> <salida.pdf>
# Requiere Google Chrome instalado en /Applications.
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
python3 -I "$DIR/scripts/ficha_a_pdf_html.py" "$1" "$DIR/fuentes" > "$TMP/ficha.html"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then echo "FALTA_CHROME"; exit 3; fi
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$2" "file://$TMP/ficha.html" 2>&1 | grep -o "[0-9]* bytes written" || true
rm -rf "$TMP"
