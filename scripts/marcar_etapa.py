# Claude lo ejecuta al empezar cada etapa. Uso:
#   python3 marcar_etapa.py "<Nombre del estándar>" <etapa>
# etapa: inicio | bloque1 | bloque2 | bloque3 | bloque4 | ficha | validacion | ficha-cerrada | herramientas | fin
import json, os, sys, datetime
base = os.path.join(os.getcwd(), '.construir-estandar'); os.makedirs(base, exist_ok=True)
try: sesion = open(os.path.join(base, 'ultima-sesion')).read().strip()
except Exception: sesion = ''
ev = {'ts': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
      'evento': 'etapa', 'estandar': sys.argv[1], 'etapa': sys.argv[2], 'sesion': sesion}
with open(os.path.join(base, 'eventos.jsonl'), 'a', encoding='utf-8') as f:
    f.write(json.dumps(ev, ensure_ascii=False) + '\n')
print('ok')
