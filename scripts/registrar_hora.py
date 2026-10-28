# Hook de la skill (UserPromptSubmit y Stop): anota la hora de cada mensaje de la sesión en
# <cwd>/.construir-estandar/eventos.jsonl. No escribe nada en pantalla y nunca bloquea.
import json, os, sys, datetime
try:
    d = json.load(sys.stdin)
    base = os.path.join(d.get('cwd') or os.getcwd(), '.construir-estandar')
    os.makedirs(base, exist_ok=True)
    ev = {'ts': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
          'evento': d.get('hook_event_name', ''), 'sesion': d.get('session_id', '')}
    with open(os.path.join(base, 'eventos.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(ev, ensure_ascii=False) + '\n')
    if ev['evento'] == 'UserPromptSubmit':
        with open(os.path.join(base, 'ultima-sesion'), 'w') as f:
            f.write(ev['sesion'])
except Exception:
    pass
sys.exit(0)
