# Pruebas de calcular_tiempo.py. Ejecutar desde la carpeta scripts/:
#   python3 -m unittest -v test_calcular_tiempo
#
# El registro de prueba (FIXTURE) tiene lapsos de tiempo conocidos, así que el resultado
# esperado se calcula a mano y está escrito abajo. Si el script cambia la regla o el
# cálculo, estas pruebas tienen que caer.
import datetime
import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import calcular_tiempo as ct

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'calcular_tiempo.py')
NOMBRE = 'Prueba'


def fila(ts, sesion, evento='mensaje', etapa=None, estandar=None):
    e = {'ts': ts, 'sesion': sesion, 'evento': evento}
    if etapa:
        e['etapa'] = etapa
    if estandar:
        e['estandar'] = estandar
    return e


def marca(ts, sesion, etapa, estandar=NOMBRE):
    return fila(ts, sesion, evento='etapa', etapa=etapa, estandar=estandar)


def cargar_eventos(lista):
    """Convierte la lista de dicts en eventos con 't' como datetime, igual que cargar()."""
    for e in lista:
        e['t'] = datetime.datetime.fromisoformat(e['ts'])
    return lista


# FIXTURE, sesión S1, estándar "Prueba". Los lapsos entre eventos consecutivos son:
#   09:00 marca inicio
#   09:05 mensaje           lapso 5 min   -> cuenta en 'inicio'
#   09:12 marca bloque1     lapso 7 min   -> cuenta en 'inicio'
#   09:30 mensaje           lapso 18 min  -> NO cuenta (pausa de 10 min)
#   09:35 marca bloque2     lapso 5 min   -> cuenta en 'bloque1'
#   10:00 mensaje           lapso 25 min  -> NO cuenta
#   10:03 marca ficha-cerrada  lapso 3 min -> cuenta en 'bloque2'
#   10:20 mensaje           sin etapa activa (ya cerró creación) -> no cuenta
# Esperado con pausa de 10 min:  inicio 12 · bloque1 5 · bloque2 3 · resto 0 · total 20.
FIXTURE_S1 = [
    marca('2026-11-01T09:00:00', 'S1', 'inicio'),
    fila('2026-11-01T09:05:00', 'S1'),
    marca('2026-11-01T09:12:00', 'S1', 'bloque1'),
    fila('2026-11-01T09:30:00', 'S1'),
    marca('2026-11-01T09:35:00', 'S1', 'bloque2'),
    fila('2026-11-01T10:00:00', 'S1'),
    marca('2026-11-01T10:03:00', 'S1', 'ficha-cerrada'),
    fila('2026-11-01T10:20:00', 'S1'),
]

# Una sesión de otro estándar con lapsos grandes: no debe alterar el resultado de NOMBRE.
FIXTURE_OTRO = [
    marca('2026-11-01T08:00:00', 'S3', 'inicio', estandar='Otro'),
    fila('2026-11-01T08:04:00', 'S3'),
    marca('2026-11-01T08:50:00', 'S3', 'bloque1', estandar='Otro'),
    marca('2026-11-01T11:00:00', 'S3', 'ficha-cerrada', estandar='Otro'),
]

ESPERADO_CREACION = {'inicio': 12, 'bloque1': 5, 'bloque2': 3, 'bloque3': 0,
                     'bloque4': 0, 'ficha': 0, 'validacion': 0}


def minutos_creacion(eventos):
    dentro, seg, _, _ = ct.calcular(cargar_eventos(list(eventos)), NOMBRE, 'creacion')
    return {etapa: round(seg[etapa] / 60) for etapa in dentro}, sum(seg.values()) / 60


class PausaYCalculo(unittest.TestCase):
    def test_pausa_es_diez_minutos(self):
        self.assertEqual(ct.PAUSA, 10 * 60)

    def test_minutos_por_etapa_con_fixture(self):
        por_etapa, _ = minutos_creacion(FIXTURE_S1)
        self.assertEqual(por_etapa, ESPERADO_CREACION)

    def test_total_con_fixture(self):
        _, total = minutos_creacion(FIXTURE_S1)
        self.assertAlmostEqual(total, 20, places=6)

    def test_lapso_de_25_minutos_no_cuenta(self):
        # Solo dos eventos separados por 25 min, con una marca activa: no suma nada.
        evs = [marca('2026-11-01T09:00:00', 'S1', 'bloque1'),
               fila('2026-11-01T09:25:00', 'S1')]
        por_etapa, total = minutos_creacion(evs)
        self.assertEqual(total, 0)

    def test_lapso_de_9_minutos_si_cuenta(self):
        evs = [marca('2026-11-01T09:00:00', 'S1', 'bloque1'),
               fila('2026-11-01T09:09:00', 'S1')]
        por_etapa, total = minutos_creacion(evs)
        self.assertEqual(por_etapa['bloque1'], 9)

    def test_otro_estandar_no_altera_el_resultado(self):
        base, _ = minutos_creacion(FIXTURE_S1)
        con_otro, _ = minutos_creacion(FIXTURE_S1 + FIXTURE_OTRO)
        self.assertEqual(base, con_otro)


class Dias(unittest.TestCase):
    def test_dias_corridos_entre_inicio_y_fin(self):
        evs = cargar_eventos([
            marca('2026-10-28T09:00:00', 'S1', 'inicio'),
            marca('2026-11-06T17:00:00', 'S1', 'fin'),
        ])
        self.assertEqual(ct.dias_corridos(evs, NOMBRE), 9)

    def test_sin_fin_no_hay_dias(self):
        evs = cargar_eventos([marca('2026-10-28T09:00:00', 'S1', 'inicio')])
        self.assertEqual(ct.dias_corridos(evs, NOMBRE), '')


class Cli(unittest.TestCase):
    def _correr(self, eventos, tramo='creacion'):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, '.construir-estandar'))
            with open(os.path.join(d, '.construir-estandar', 'eventos.jsonl'), 'w', encoding='utf-8') as f:
                for e in eventos:
                    f.write(json.dumps(e) + '\n')
            r = subprocess.run([sys.executable, SCRIPT, NOMBRE, '1.0', 'A', 'x@kodea.org', tramo],
                               cwd=d, capture_output=True, text=True)
            return r

    def test_csv_con_total_y_dias(self):
        eventos = FIXTURE_S1 + [marca('2026-11-06T17:00:00', 'S1', 'fin')]
        r = self._correr(eventos, tramo='creacion')
        self.assertEqual(r.returncode, 0, r.stderr)
        filas = r.stdout.strip().splitlines()
        self.assertEqual(filas[0].split(',')[-1], 'dias_corridos')
        total = [f for f in filas if '"total"' in f][0].split(',')
        self.assertEqual(total[8], '20')   # minutos_de_trabajo
        self.assertEqual(total[9], '5')    # 2026-11-01 -> 2026-11-06

    def test_sin_registro_da_error_claro(self):
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, SCRIPT, NOMBRE, '1.0', 'A', 'x@kodea.org', 'creacion'],
                               cwd=d, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn('no hay registro de tiempo', r.stderr)


if __name__ == '__main__':
    unittest.main()
