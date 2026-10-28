# Convierte la ficha .md (formato Ficha Ejecutable) en HTML con Poppins 11 incrustada, para imprimir a PDF con Chrome.
# Uso: python3 ficha_a_pdf_html.py <ficha.md> <carpeta-fuentes> > ficha.html
# El PDF no muestra versión, fechas ni historial: solo el título del estándar.
import re, html, sys, base64
src=open(sys.argv[1],encoding='utf-8').read().split('\n')
sp=sys.argv[2]  # carpeta con Poppins-Regular.ttf y Poppins-Bold.ttf
TITULO=next((l.strip().title() for l in src if l.startswith('FICHA EJECUTABLE')),'Ficha Ejecutable')
# DROP_HEADER: el PDF no muestra versión, fechas ni historial de cambios (viven solo en el .md)
_a=next((k for k,l in enumerate(src) if l.startswith('VERSIÓN:')),None)
if _a is not None:
    _b=next(k for k in range(_a,len(src)) if src[k].startswith('═'))
    del src[_a:_b]
def b64(f): return base64.b64encode(open(f,'rb').read()).decode()
def esc(t): return html.escape(t,quote=False)
CAPS=lambda s: s.strip() and not re.search(r'[a-záéíóúñ]',s) and len(re.findall(r'[A-ZÁÉÍÓÚÑ]',s))>=4
ITEM=re.compile(r'^(?P<pre>[│ ]*)(?P<mk>[├└]─|•|☐|☑|\d+\.|P:|R:|→)\s+(?P<tx>.*)$')
def is_title(l,after_rule):
    s=l.strip()
    if after_rule: return True
    if l.startswith((' ','│','├','└','•','☐','☑')): return False
    if re.match(r'^\d+\. ',l): return False
    if re.match(r'^(CHECKLIST |FASE |Hito \d)',l): return True
    return bool(CAPS(l)) and not l.startswith('→')
blocks=[]  # (kind, depth, marker, text)
i=0; after_rule=False; flow=False
while i<len(src):
    l=src[i]
    if l.startswith('═'):
        blocks.append(('rule',0,'','')); after_rule=True; i+=1; continue
    if not l.strip():
        blocks.append(('gap',0,'','')); flow=False; i+=1; continue
    if l.startswith('|'):
        rows=[]
        while i<len(src) and src[i].startswith('|'): rows.append(src[i]); i+=1
        blocks.append(('table',0,'',rows)); continue
    sandwiched = i+1<len(src) and src[i+1].startswith('═') and i>0 and src[i-1].startswith('═')
    if is_title(l,sandwiched):
        txt=l.strip()
        if txt.count('(')>txt.count(')') and i+1<len(src):
            i+=1; txt+=' '+src[i].strip()
        # título puede ocupar varias líneas solo si no hay otra cosa; aquí una línea
        blocks.append(('title',0,'',txt)); after_rule=False; i+=1; continue
    after_rule=False
    if re.search(r'→|↓',l) and (l.startswith('Co-creación') or l.startswith('Kickoff') or flow or l.startswith(' ')) and not l.startswith('→'):
        flow=True
    if flow or (l.startswith(' '*8) and not ITEM.match(l)):
        blocks.append(('flow',0,'',l.strip())); flow=True; i+=1; continue
    m=ITEM.match(l)
    if m and not (m.group('mk')=='•' and False):
        pre=m.group('pre'); mk=m.group('mk')
        depth=(len(pre)//3+1) if mk in ('├─','└─') else 0
        if mk in ('☐','☑') or re.match(r'\d+\.',mk) or mk in ('P:','R:','•','→'): depth=0
        blocks.append(('item',depth,mk,m.group('tx').strip())); i+=1; continue
    # continuación o párrafo
    t=re.sub(r'^[│ ]+','',l).strip()
    prev=blocks[-1] if blocks else None
    newpara = bool(re.match(r'^(VERSIÓN|FECHA [A-ZÁÉÍÓÚ]+):',l))
    last=src[i-1] if i>0 else ''
    indented = l.startswith((' ','│'))
    joinable = indented or last.endswith(' ') or (last.rstrip() and last.rstrip()[-1] not in '.:?!)')
    if prev and prev[0] in('item','para') and not newpara and joinable:
        k,d,mk,tx=prev; blocks[-1]=(k,d,mk,tx+' '+t)
    else:
        blocks.append(('para',0,'',t))
    i+=1
# post: etiquetas en negrita para encabezados de rol / VERSIÓN etc.
out=[]; n=len(blocks)
def inline(t):
    t=esc(t)
    return t
def nextkind(k):
    j=k+1
    while j<n and blocks[j][0]=='gap': j+=1
    return blocks[j] if j<n else None
for k,(kind,depth,mk,tx) in enumerate(blocks):
    if kind=='rule': out.append('<hr>')
    elif kind=='gap': continue
    elif kind=='title': out.append(f'<p class="t">{inline(tx)}</p>')
    elif kind=='table':
        rows=tx
        cells=lambda r:[c.strip() for c in r.strip().strip('|').split('|')]
        h=cells(rows[0]); body=[cells(r) for r in rows[2:]]
        out.append('<table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in h)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in body)+'</tbody></table>')
    elif kind=='flow': out.append(f'<p class="flow">{inline(tx)}</p>')
    elif kind=='para':
        nk=nextkind(k)
        bold = nk and nk[0]=='item' and nk[2] in('├─','└─') and len(tx)<260 or re.match(r'^(VERSIÓN|FECHA)',tx)
        if re.match(r'^(VERSIÓN|FECHA [A-ZÁÉÍÓÚ]+):',tx):
            lab,rest=tx.split(':',1); out.append(f'<p class="p"><b>{inline(lab)}:</b>{inline(rest)}</p>')
        elif bold and len(tx)>=110 and ' — ' in tx:
            a,b=tx.split(' — ',1); out.append(f'<p class="p"><b>{inline(a)}</b> — {inline(b)}</p>')
        elif bold: out.append(f'<p class="p"><b>{inline(tx)}</b></p>')
        else: out.append(f'<p class="p">{inline(tx)}</p>')
    elif kind=='item':
        if mk in('├─','└─'):
            out.append(f'<p class="i d{depth}"><span class="m">–</span>{inline(tx)}</p>')
        elif mk=='•': out.append(f'<p class="i d0"><span class="m">•</span>{inline(tx)}</p>')
        elif mk in('☐','☑'): out.append(f'<p class="i d0"><span class="m">{mk}</span>{inline(tx)}</p>')
        elif mk in('P:','R:'): out.append(f'<p class="i d0 q"><b>{mk}</b> {inline(tx)}</p>')
        elif mk=='→': out.append(f'<p class="p">→ {inline(tx)}</p>')
        else: out.append(f'<p class="i d0"><span class="m">{mk}</span>{inline(tx)}</p>')
css=f"""
@font-face{{font-family:'Poppins';font-weight:400;src:url(data:font/ttf;base64,{b64(sp+'/Poppins-Regular.ttf')})}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(data:font/ttf;base64,{b64(sp+'/Poppins-Bold.ttf')})}}
@page{{size:A4;margin:18mm 16mm 18mm 16mm;@bottom-center{{content:counter(page);font-family:Poppins;font-size:11pt}}}}
body{{font-family:'Poppins',sans-serif;font-size:11pt;line-height:1.5;color:#1d1d1f;font-weight:400}}
p{{margin:0}} b{{font-weight:700}}
.t{{font-weight:700;margin:16pt 0 5pt;break-after:avoid}}
.p{{margin:4pt 0}}
.i{{display:block;position:relative;margin:2pt 0;padding-left:16pt}}
.i .m{{position:absolute;left:0}}
.d1{{margin-left:0}} .d2{{margin-left:18pt}} .d3{{margin-left:36pt}} .d4{{margin-left:54pt}}
.q{{margin-top:6pt}}
.flow{{margin:2pt 0 2pt 12pt}}
hr{{border:0;border-top:1px solid #c9ccd3;margin:12pt 0}}
table{{border-collapse:collapse;width:100%;margin:8pt 0}}
tr{{break-inside:avoid}}
th,td{{border:1px solid #d5d8de;padding:5pt 7pt;vertical-align:top;text-align:left;font-size:11pt}}
th{{background:#eef1f6;font-weight:700}}
"""
print(f"<!doctype html><html lang='es'><head><meta charset='utf-8'><title>{esc(TITULO)}</title><style>{css}</style></head><body>"+'\n'.join(out)+"</body></html>")
