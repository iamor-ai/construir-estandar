# Calcula el tiempo de trabajo de un estándar a partir de <cwd>/.construir-estandar/eventos.jsonl.
# Uso: python3 calcular_tiempo.py "<Nombre del estándar>" <version> <caso A|B|C> <correo> <tramo>
#   tramo: creacion (inicio -> ficha-cerrada) | herramientas (herramientas -> fin)
# Imprime un CSV de dos líneas (encabezado + registro) listo para subir a Drive como Sheet.
# Regla: los lapsos de más de 20 minutos sin mensajes cuentan como pausa y no se suman.
import json, os, sys, datetime
PAUSA = 20 * 60
nombre, version, caso, correo, tramo = sys.argv[1:6]
ini, fin = {'creacion': ('inicio', 'ficha-cerrada'), 'herramientas': ('herramientas', 'fin')}[tramo]
evs = [json.loads(l) for l in open(os.path.join(os.getcwd(), '.construir-estandar', 'eventos.jsonl'), encoding='utf-8') if l.strip()]
for e in evs: e['t'] = datetime.datetime.fromisoformat(e['ts'])
marcas = [e for e in evs if e.get('evento') == 'etapa' and e.get('estandar') == nombre]
sesiones = {e['sesion'] for e in marcas if e['sesion']}
# Intervalos activos del tramo: desde cada marca de inicio de tramo (o etapa intermedia) hasta la marca de fin.
orden = ['inicio','bloque1','bloque2','bloque3','bloque4','ficha','validacion','ficha-cerrada','herramientas','fin']
dentro = set(orden[orden.index(ini):orden.index(fin)])
total = 0; t0 = t1 = None
for s in sesiones:
    serie = sorted([e for e in evs if e['sesion'] == s], key=lambda e: e['t'])
    activo = False; prev = None
    for e in serie:
        if e.get('evento') == 'etapa' and e.get('estandar') == nombre:
            if activo and prev is not None and (e['t'] - prev).total_seconds() <= PAUSA:
                total += (e['t'] - prev).total_seconds()
            activo = e['etapa'] in dentro
            prev = e['t'] if activo else None
            if activo: t0 = min(t0, e['t']) if t0 else e['t']
            if e['etapa'] == fin: t1 = max(t1, e['t']) if t1 else e['t']
            continue
        if activo:
            if prev is not None and (e['t'] - prev).total_seconds() <= PAUSA:
                total += (e['t'] - prev).total_seconds()
            prev = e['t']; t1 = max(t1, e['t']) if t1 else e['t']
minutos = round(total / 60)
f = lambda t: t.strftime('%Y-%m-%d') if t else ''
print('estandar,version,caso,tramo,creado_por,fecha_inicio,fecha_termino,minutos_de_trabajo')
q = lambda s: '"' + str(s).replace('"', '""') + '"'
print(','.join([q(nombre), q(version), q(caso), q(tramo), q(correo), f(t0), f(t1), str(minutos)]))
