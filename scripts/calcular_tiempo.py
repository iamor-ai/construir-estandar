# Calcula el tiempo de trabajo de un estándar a partir de <cwd>/.construir-estandar/eventos.jsonl.
# Uso: python3 calcular_tiempo.py "<Nombre del estándar>" <version> <caso A|B|C> <correo> <tramo>
#   tramo: creacion (inicio -> ficha-cerrada) | herramientas (herramientas -> fin)
# Imprime un CSV: una fila por etapa del tramo, una fila de total y la columna dias_corridos
# (días corridos entre la marca 'inicio' y la marca 'fin' del estándar, en todo el registro).
# Cada fila redondea a minutos; el total se calcula con los segundos.
# Regla: los lapsos de más de 10 minutos sin mensajes cuentan como pausa y no se suman.
import json, os, sys, datetime

PAUSA = 10 * 60
ORDEN = ['inicio', 'bloque1', 'bloque2', 'bloque3', 'bloque4', 'ficha', 'validacion',
         'ficha-cerrada', 'herramientas', 'fin']
TRAMOS = {'creacion': ('inicio', 'ficha-cerrada'), 'herramientas': ('herramientas', 'fin')}


def cargar(ruta):
    if not os.path.exists(ruta):
        sys.exit(f'ERROR: no hay registro de tiempo en {ruta}. El hook no anotó la sesión.')
    evs = [json.loads(l) for l in open(ruta, encoding='utf-8') if l.strip()]
    for e in evs:
        e['t'] = datetime.datetime.fromisoformat(e['ts'])
    return evs


def es_marca(e, nombre):
    return e.get('evento') == 'etapa' and e.get('estandar') == nombre


def calcular(evs, nombre, tramo):
    ini, fin = TRAMOS[tramo]
    dentro = ORDEN[ORDEN.index(ini):ORDEN.index(fin)]
    segundos = {etapa: 0.0 for etapa in dentro}
    for s in {e.get('sesion') for e in evs if es_marca(e, nombre)} - {None, ''}:
        serie = sorted((e for e in evs if e.get('sesion') == s), key=lambda e: e['t'])
        cur = prev = None  # etapa activa y hora del evento anterior
        for e in serie:
            if cur and prev and (e['t'] - prev).total_seconds() <= PAUSA:
                segundos[cur] += (e['t'] - prev).total_seconds()
            if es_marca(e, nombre):
                cur = e['etapa'] if e['etapa'] in dentro else None
            prev = e['t']
    marcas = [e for e in evs if es_marca(e, nombre)]
    t_ini = min((e['t'] for e in marcas if e['etapa'] == ini), default=None)
    t_fin = max((e['t'] for e in marcas if e['etapa'] == fin), default=None)
    return dentro, segundos, t_ini, t_fin


def dias_corridos(evs, nombre):
    marcas = [e for e in evs if es_marca(e, nombre)]
    a = min((e['t'] for e in marcas if e['etapa'] == 'inicio'), default=None)
    b = max((e['t'] for e in marcas if e['etapa'] == 'fin'), default=None)
    return (b.date() - a.date()).days if a and b else ''


if __name__ == '__main__':
    if len(sys.argv) < 6:
        print('Uso: calcular_tiempo.py <nombre> <version> <caso> <correo> <tramo>', file=sys.stderr)
        sys.exit(2)
    nombre, version, caso, correo, tramo = sys.argv[1:6]
    evs = cargar(os.path.join(os.getcwd(), '.construir-estandar', 'eventos.jsonl'))
    dentro, segundos, t_ini, t_fin = calcular(evs, nombre, tramo)
    dias = dias_corridos(evs, nombre)
    f = lambda t: t.strftime('%Y-%m-%d') if t else ''
    q = lambda s: '"' + str(s).replace('"', '""') + '"'
    print('estandar,version,caso,tramo,etapa,creado_por,fecha_inicio,fecha_termino,minutos_de_trabajo,dias_corridos')
    base = [q(nombre), q(version), q(caso), q(tramo)]
    for etapa in dentro:
        print(','.join(base + [q(etapa), q(correo), f(t_ini), f(t_fin), str(round(segundos[etapa] / 60)), str(dias)]))
    total = sum(segundos.values())
    print(','.join(base + [q('total'), q(correo), f(t_ini), f(t_fin), str(round(total / 60)), str(dias)]))
