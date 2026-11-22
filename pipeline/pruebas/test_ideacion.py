"""Pruebas mecánicas V1.3: no predicen creatividad, retención ni visitas."""
import sys
import unittest
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
import ideacion


def lote(semilla, cantidad=4, finalistas=None):
    ideas = [{
        'id': f'I-{i+1:02d}',
        'nucleo': f'conflicto conceptual {semilla} {i}',
        'situacion': f'productor diferente en contexto {semilla} numero {i}',
        'deseo': 'algo que le importa a ese productor',
        'apoyo': 'supuesto',
        'territorio': 'un mismo territorio',  # no hay cuota de diversidad
    } for i in range(cantidad)]
    profundas = [{
        'id': 'I-01',
        'relevancia': 'una meta personal de ese productor',
        'consecuencia': 'un resultado concreto que afecta la meta',
        'estimulo': 'algo perceptible que revela la consecuencia',
        'por_que': 'el estímulo pone una meta importante en juego',
        'pago': 'el video desarrolla una respuesta verificable',
        'objecion': 'quizá la reacción no aparezca en ese público',
        'presencia': 'ninguna',
    }]
    return {'version': '1.3', 'cuenta': '1', 'candidatos': ideas,
            'profundizaciones': profundas,
            'finalistas': ['I-01'] if finalistas is None else finalistas,
            'sin_finalistas_por_que': ''}


class IdeacionV13(unittest.TestCase):
    def test_tres_rondas_sinteticas(self):
        for semilla in ('alfa', 'beta', 'gamma'):
            with self.subTest(semilla=semilla):
                self.assertEqual(ideacion.comprobar(lote(semilla)), [])

    def test_no_impone_15_ideas_ni_5_territorios(self):
        self.assertEqual(ideacion.comprobar(lote('pequena', cantidad=1)), [])
        self.assertEqual(ideacion.comprobar(lote('grande', cantidad=21)), [])

    def test_permite_tres_finalistas_de_mismo_territorio(self):
        datos = lote('mismo')
        for idx in (1, 2):
            profundo = dict(datos['profundizaciones'][0])
            profundo['id'] = f'I-{idx+1:02d}'
            datos['profundizaciones'].append(profundo)
        datos['finalistas'] = ['I-01', 'I-02', 'I-03']
        self.assertEqual(ideacion.comprobar(datos), [])

    def test_puede_rechazar_todo_con_justificacion(self):
        datos = lote('rechazo', finalistas=[])
        datos['profundizaciones'] = []
        datos['sin_finalistas_por_que'] = 'ningún estímulo tiene una consecuencia suficientemente relevante'
        self.assertEqual(ideacion.comprobar(datos), [])

    def test_no_puede_rechazar_todo_sin_razon(self):
        datos = lote('rechazo', finalistas=[])
        self.assertTrue(any('explicar por qué' in e for e in ideacion.comprobar(datos)))

    def test_finalista_requiere_cadena_causal(self):
        datos = lote('insuficiente')
        datos['profundizaciones'][0]['por_que'] = ''
        self.assertTrue(any('falta por_que' in e for e in ideacion.comprobar(datos)))

    def test_finalista_sin_profundizar_no_pasa(self):
        datos = lote('insuficiente')
        datos['finalistas'] = ['I-02']
        self.assertTrue(any('falta profundización causal' in e for e in ideacion.comprobar(datos)))

    def test_no_acepta_duplicados_exactos(self):
        datos = lote('duplicado')
        datos['candidatos'][1]['nucleo'] = datos['candidatos'][0]['nucleo']
        self.assertTrue(any('duplicado literalmente' in e for e in ideacion.comprobar(datos)))

    def test_rechaza_evidencia_inexistente(self):
        datos = lote('fuente')
        datos['candidatos'][0]['apoyo'] = 'EV-9999'
        self.assertTrue(any('evidencia inexistente' in e for e in ideacion.comprobar(datos)))

    def test_no_premia_menciones_del_producto(self):
        datos = lote('organico')
        datos['profundizaciones'][0]['presencia'] = 'discreta'
        self.assertEqual(ideacion.comprobar(datos), [])

    def test_historial_solo_se_consulta_en_revision(self):
        datos = lote('historial')
        datos['candidatos'][0]['nucleo'] = 'artista pide beats urgentes'
        self.assertEqual(ideacion.comprobar(datos), [])
        self.assertTrue(any('HIST-01' in a for a in ideacion.revisar_historial(datos)))

    def test_version_antigua_exige_migracion(self):
        datos = lote('version')
        datos['version'] = '1.2'
        self.assertTrue(any('version 1.3' in e for e in ideacion.comprobar(datos)))


if __name__ == '__main__':
    unittest.main()
