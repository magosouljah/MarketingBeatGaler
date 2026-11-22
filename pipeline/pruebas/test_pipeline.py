"""Prueba de circuito: los seis modulos enlazan y el informe sale de datos marcados como PRUEBA."""
import csv
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import pipeline  # noqa: E402

CIRCUITO = AQUI / 'circuito'


class Circuito(unittest.TestCase):
    def test_datos_reales_enlazan(self):
        self.assertEqual(pipeline.comprobar(pipeline.RAIZ), [])

    def test_datos_de_prueba_enlazan(self):
        self.assertEqual(pipeline.comprobar(CIRCUITO), [])

    def test_no_hay_resultados_de_prueba_entre_los_reales(self):
        for fila in pipeline.leer(pipeline.RAIZ, pipeline.M5, 'resultados.csv'):
            self.assertEqual(fila['origen'], 'real')
            self.assertFalse(fila['pieza'].startswith('PRUEBA'))

    def test_recorrido_completo(self):
        texto = pipeline.aprender(CIRCUITO, 'PRUEBA-X-001')
        self.assertIn('DATOS DE PRUEBA', texto)
        self.assertIn('prueba menos contraste = +15.0', texto)   # instagram, cuerpo-a, ultima lectura
        self.assertIn('prueba menos contraste = -2.0', texto)    # tiktok
        self.assertIn('PRUEBA-P-0004', texto)                    # excluida por mala ejecucion
        self.assertIn('instagram/cuerpo-b: no hay prueba y contraste', texto)
        self.assertIn('mas de 12 horas de diferencia', texto)
        self.assertIn('PENDIENTE', texto)                        # nunca concluye solo

    def test_arbol_cuenta_hojas(self):
        self.assertIn('Hojas: 5 | ancladas: 1 (20.0%)', pipeline.arbol(CIRCUITO, 'PRUEBA-M-001'))

    def test_un_enlace_roto_se_detecta(self):
        with tempfile.TemporaryDirectory() as tmp:
            copia = Path(tmp) / 'c'
            shutil.copytree(CIRCUITO, copia)
            ruta = copia / pipeline.M4 / 'piezas.csv'
            filas = list(csv.reader(ruta.open(encoding='utf-8')))
            filas[1][1] = 'PRUEBA-G-999'
            csv.writer(ruta.open('w', encoding='utf-8', newline='')).writerows(filas)
            self.assertTrue(any('PRUEBA-G-999' in e for e in pipeline.comprobar(copia)))

    def test_una_hoja_sin_cierre_se_detecta(self):
        with tempfile.TemporaryDirectory() as tmp:
            copia = Path(tmp) / 'c'
            shutil.copytree(CIRCUITO, copia)
            ruta = copia / pipeline.M2 / 'nodos.csv'
            filas = list(csv.reader(ruta.open(encoding='utf-8')))
            filas[1][6] = ''
            csv.writer(ruta.open('w', encoding='utf-8', newline='')).writerows(filas)
            self.assertTrue(any('no declara en que termina' in e for e in pipeline.comprobar(copia)))


if __name__ == '__main__':
    unittest.main()
