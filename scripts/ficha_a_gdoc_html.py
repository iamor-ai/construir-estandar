# Convierte la ficha .md en HTML con estilos en línea para crear el Google Doc con el conector de Drive
# (create_file, contentMimeType text/html). Formato: Poppins; títulos en negrita; Encabezado 1 = 14 pt,
# Encabezado 2 = 12 pt, texto = 11 pt. Contenido igual que el PDF: solo el título, sin versión ni fechas.
# Uso: python3 ficha_a_gdoc_html.py <ficha.md> <carpeta-fuentes> > ficha-gdoc.html
import re, subprocess, sys, os
aqui = os.path.dirname(os.path.abspath(__file__))
h = subprocess.run([sys.executable, '-I', os.path.join(aqui, 'ficha_a_pdf_html.py'), sys.argv[1], sys.argv[2]],
                   capture_output=True, text=True, check=True).stdout
cuerpo = h.split('<body>', 1)[1].rsplit('</body>', 1)[0]
F = "font-family:Poppins,sans-serif;"
H1 = F + "font-size:14pt;font-weight:700;margin:18pt 0 8pt 0;"
H2 = F + "font-size:12pt;font-weight:700;margin:18pt 0 6pt 0;"
P = F + "font-size:11pt;margin:3pt 0;"
B = F + "font-size:11pt;font-weight:700;margin:10pt 0 4pt 0;"
TD = F + "font-size:11pt;border:1px solid #d5d8de;padding:4pt 6pt;vertical-align:top;"
TH = TD + "font-weight:700;background:#eef1f6;"
primero = [True]
def titulo(m, seccion):
    t = m.group(1)
    if primero[0] and t.upper().startswith('FICHA EJECUTABLE'):
        primero[0] = False
        return f'<h1 style="{H1}">{t}</h1>'
    return f'<h2 style="{H2}">{t}</h2>' if seccion else f'<p style="{B}">{t}</p>'
# Título de sección: entre dos líneas (═══ TÍTULO ═══) o justo después de una línea.
cuerpo = re.sub(r'<hr>\s*<p class="t">(.*?)</p>\s*<hr>', lambda m: titulo(m, True), cuerpo)
cuerpo = re.sub(r'<hr>\s*<p class="t">(.*?)</p>', lambda m: titulo(m, True), cuerpo)
cuerpo = re.sub(r'(</h1>)\s*<p class="t">(.*?)</p>', lambda m: m.group(1) + f'<h2 style="{H2}">{m.group(2)}</h2>', cuerpo)
cuerpo = re.sub(r'<p class="t">(.*?)</p>', lambda m: titulo(m, False), cuerpo)
cuerpo = cuerpo.replace('<hr>', '')
cuerpo = re.sub(r'<p class="[^"]*">', f'<p style="{P}">', cuerpo)
cuerpo = re.sub(r'<span class="m">(.*?)</span>', r'\1 ', cuerpo)
cuerpo = cuerpo.replace('<table>', '<table style="border-collapse:collapse;width:100%;">')
cuerpo = cuerpo.replace('<th>', f'<th style="{TH}">').replace('<td>', f'<td style="{TD}">')
print(f'<html><head><meta charset="utf-8"></head><body style="{F}font-size:11pt;">{cuerpo}</body></html>')
