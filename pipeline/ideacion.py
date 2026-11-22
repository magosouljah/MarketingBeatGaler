#!/usr/bin/env python3
"""Chequeos mecánicos de ideación V1.2; NO juzga calidad creativa."""
import argparse
import csv
import json
import re
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESERVA = ROOT / 'evaluacion' / 'referencias-historicas.json'
CLAVES = ('id', 'territorio', 'nucleo', 'situacion', 'deseo', 'estimulo',
          'por_que', 'pago', 'apoyo', 'presencia')
PRESENCIAS = {'ninguna', 'discreta', 'indirecta', 'directa'}


def normalizar(s):
    s = unicodedata.normalize('NFKD', s.casefold())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def comprobar(datos):
    """Valida estructura, diversidad declarada y trazabilidad, sin usar ejemplos previos."""
    errores = []
    if not isinstance(datos, dict):
        return ['La raíz debe ser un objeto JSON.']
    if datos.get('version') != '1.2':
        errores.append('Falta version 1.2.')
    if datos.get('cuenta') not in ('1', '2'):
        errores.append('cuenta debe ser 1 o 2.')
    candidatos = datos.get('candidatos')
    if not isinstance(candidatos, list):
        return errores + ['candidatos debe ser una lista.']
    if not 15 <= len(candidatos) <= 20:
        errores.append('Se requieren 15–20 situaciones iniciales, no guiones.')
    ids, situaciones, nucleos, territorios = set(), set(), set(), set()
    with (ROOT / '1-investigacion' / 'evidencia.csv').open(encoding='utf-8', newline='') as fh:
        evidencias = {row['id'] for row in csv.DictReader(fh)}
    for i, c in enumerate(candidatos, 1):
        if not isinstance(c, dict):
            errores.append(f'Candidato {i}: no es objeto.')
            continue
        prefijo = f'Candidato {i}'
        for k in CLAVES:
            if not isinstance(c.get(k), str) or not c[k].strip():
                errores.append(f'{prefijo}: falta {k}.')
        ident = c.get('id', '')
        if not re.fullmatch(r'I-\d{2}', str(ident)):
            errores.append(f'{prefijo}: id debe ser I-01, I-02, etc.')
        if ident in ids:
            errores.append(f'{prefijo}: id repetido.')
        ids.add(ident)
        for nombre, registro, v in (('situacion', situaciones, c.get('situacion', '')),
                                     ('nucleo', nucleos, c.get('nucleo', ''))):
            key = normalizar(v) if isinstance(v, str) else ''
            if key and key in registro:
                errores.append(f'{prefijo}: {nombre} duplicado.')
            registro.add(key)
        if isinstance(c.get('territorio'), str):
            territorios.add(normalizar(c['territorio']))
        if c.get('presencia') not in PRESENCIAS:
            errores.append(f'{prefijo}: presencia inválida.')
        apoyo = c.get('apoyo', '')
        if isinstance(apoyo, str) and not (apoyo == 'supuesto' or
                                            re.fullmatch(r'EV-\d{4}( EV-\d{4})*', apoyo)):
            errores.append(f'{prefijo}: apoyo debe ser EV-0000 o supuesto.')
        elif isinstance(apoyo, str) and apoyo != 'supuesto':
            for ev in apoyo.split():
                if ev not in evidencias:
                    errores.append(f'{prefijo}: evidencia inexistente {ev}.')
    if len(territorios - {''}) < 5:
        errores.append('Explorar al menos cinco territorios de vida diferentes.')
    finales = datos.get('finalistas')
    if not isinstance(finales, list) or len(finales) != 3 or len(set(map(str, finales))) != 3:
        errores.append('finalistas debe contener tres IDs distintos.')
    else:
        por_id = {c.get('id'): c for c in candidatos if isinstance(c, dict)}
        if not set(finales) <= ids:
            errores.append('Hay finalistas sin candidato.')
        elif len({normalizar(por_id[x]['territorio']) for x in finales
                  if isinstance(por_id[x].get('territorio'), str)}) < 3:
            errores.append('Los tres finalistas deben cubrir situaciones de tres territorios distintos.')
    return errores


def revisar_historial(datos, reserva=RESERVA):
    """Solo para un segundo paso/revisor. Avisos de semejanza, no dictamen de creatividad."""
    hist = json.loads(reserva.read_text(encoding='utf-8'))['situaciones']
    advertencias = []
    for c in datos.get('candidatos', []):
        if not isinstance(c, dict):
            continue
        texto = normalizar(c.get('nucleo', '') + ' ' + c.get('situacion', '') +
                           ' ' + c.get('estimulo', ''))
        for ref in hist:
            patron = normalizar(ref['nucleo'])
            if not patron or not texto:
                continue
            tokens = set(texto.split())
            termino = set(patron.split())
            cobertura = len(tokens & termino) / len(termino) if termino else 0
            parecido = SequenceMatcher(None, normalizar(c.get('nucleo', '')), patron).ratio()
            if (parecido >= 0.77 or (len(termino) >= 4 and cobertura >= 0.85)):
                advertencias.append(f"{c.get('id', '?')}: revisar posible repetición de {ref['id']} (no es prueba semántica).")
                break
    return advertencias


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('accion', choices=['comprobar', 'revisar'])
    ap.add_argument('archivo', type=Path)
    args = ap.parse_args(argv)
    try:
        datos = json.loads(args.archivo.read_text(encoding='utf-8'))
        errores = comprobar(datos)
        if errores:
            for e in errores:
                print('ERROR:', e)
            return 1
        print('ESTRUCTURA: PASS (no evalúa calidad creativa).')
        if args.accion == 'revisar':
            avisos = revisar_historial(datos)
            for a in avisos:
                print('AVISO:', a)
            print(f'REVISIÓN: {len(avisos)} posibles similitudes; revisar manualmente.')
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
