"""Tres recorridos sintéticos: comprueban estructura, no creatividad ni rendimiento."""
import csv
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import ideacion


def lote(seed):
    areas = ['aprendizaje', 'relaciones', 'identidad', 'juego', 'carrera']
    ideas = []
    for i in range(15):
        ideas.append({
            'id': f'I-{i+1:02d}',
            'territorio': areas[i // 3],
            'nucleo': f'caso sintetico {seed} variante {i}',
            'situacion': f'situacion sintetica {seed} numero {i}',
            'deseo': 'satisfacer un deseo hipotetico',
            'estimulo': f'elemento observable hipotetico {seed} {i}',
            'por_que': 'hipotesis causal por contrastar, no un hecho',
            'pago': 'el desarrollo mostraria una explicacion',
            'apoyo': 'supuesto',
            'presencia': 'ninguna',
        })
    return {'version': '1.2', 'cuenta': '1', 'candidatos': ideas,
            'finalistas': ['I-01', 'I-05', 'I-10']}


class Ideas(unittest.TestCase):
    def test_tres_rondas_sinteticas(self):
        for semilla in ('alfa', 'beta', 'gamma'):
            with self.subTest(semilla=semilla):
                self.assertEqual(ideacion.comprobar(lote(semilla)), [])

    def test_no_acepta_tres_variantes_de_una_sola_situacion(self):
        datos = lote('A')
        for c in datos['candidatos']:
            c['nucleo'] = 'mismo conflicto renombrado'
        self.assertTrue(any('duplicado' in e for e in ideacion.comprobar(datos)))

    def test_tres_finalistas_necesitan_territorios_distintos(self):
        datos = lote('B')
        datos['finalistas'] = ['I-01', 'I-02', 'I-03']
        self.assertTrue(any('territorios' in e for e in ideacion.comprobar(datos)))

    def test_faltan_evidencia_y_causalidad(self):
        datos = lote('C')
        datos['candidatos'][0]['apoyo'] = ''
        datos['candidatos'][1]['por_que'] = ''
        self.assertTrue(any('apoyo' in e for e in ideacion.comprobar(datos)))
        self.assertTrue(any('por_que' in e for e in ideacion.comprobar(datos)))

    def test_evidencia_referenciada_existe(self):
        datos = lote('EV')
        datos['candidatos'][0]['apoyo'] = 'EV-9999'
        self.assertTrue(any('evidencia inexistente' in e for e in ideacion.comprobar(datos)))

    def test_revisor_detecta_repeticion_conocida(self):
        datos = lote('D')
        datos['candidatos'][0]['nucleo'] = 'artista pide beats urgentes'
        avisos = ideacion.revisar_historial(datos)
        self.assertTrue(any('HIST-01' in a for a in avisos))

    def test_generador_no_importa_historial(self):
        datos = lote('E')
        datos['candidatos'][0]['nucleo'] = 'artista pide beats urgentes'
        self.assertEqual(ideacion.comprobar(datos), [])


if __name__ == '__main__':
    unittest.main()
