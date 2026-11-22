#!/usr/bin/env python3
"""Comprobaciones estructurales V1.3. NO evalúa fuerza psicológica ni creatividad."""
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
CLAVES_IDEA = ('id', 'nucleo', 'situacion', 'deseo', 'apoyo')
CLAVES_PROFUNDAS = ('id', 'relevancia', 'consecuencia', 'estimulo', 'por_que',
                   'pago', 'objecion', 'presencia')
PRESENCIAS = {'ninguna', 'discreta', 'indirecta', 'directa'}


def normalizar(s):
    s = unicodedata.normalize('NFKD', s.casefold())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def texto_valido(obj, campo):
    return isinstance(obj.get(campo), str) and bool(obj[campo].strip())


def comprobar(datos):
    """Verifica trazabilidad, candidatos y selección 0–3; no puede certificar calidad."""
    errores = []
    if not isinstance(datos, dict):
        return ['La raíz debe ser un objeto JSON.']
    if datos.get('version') != '1.3':
        errores.append('Se requiere version 1.3 (migrar lotes 1.2 antes de validarlos).')
    if datos.get('cuenta') not in ('1', '2'):
        errores.append('cuenta debe ser 1 o 2.')
    candidatos = datos.get('candidatos')
    if not isinstance(candidatos, list):
        return errores + ['candidatos debe ser una lista.']
    if not candidatos:
        errores.append('Registrar al menos una situación explorada; no existe cuota máxima.')
    ids, nucleos, situaciones = set(), set(), set()
    with (ROOT / '1-investigacion' / 'evidencia.csv').open(encoding='utf-8', newline='') as fh:
        evidencias = {fila['id'] for fila in csv.DictReader(fh)}
    for i, c in enumerate(candidatos, 1):
        lugar = f'Candidato {i}'
        if not isinstance(c, dict):
            errores.append(f'{lugar}: no es objeto.')
            continue
        for campo in CLAVES_IDEA:
            if not texto_valido(c, campo):
                errores.append(f'{lugar}: falta {campo}.')
        ident = c.get('id')
        if not isinstance(ident, str) or not re.fullmatch(r'I-\d{2,3}', ident):
            errores.append(f'{lugar}: id inválido (I-01, etc.).')
        if isinstance(ident, str):
            if ident in ids:
                errores.append(f'{lugar}: id repetido.')
            ids.add(ident)
        for campo, registro in (('nucleo', nucleos), ('situacion', situaciones)):
            valor = c.get(campo)
            clave = normalizar(valor) if isinstance(valor, str) else ''
            if clave and clave in registro:
                errores.append(f'{lugar}: {campo} duplicado literalmente.')
            if clave:
                registro.add(clave)
        apoyo = c.get('apoyo')
        if isinstance(apoyo, str) and apoyo.strip():
            if apoyo != 'supuesto' and not re.fullmatch(r'EV-\d{4}( EV-\d{4})*', apoyo):
                errores.append(f'{lugar}: apoyo debe ser EV-0000 o supuesto.')
            elif apoyo != 'supuesto':
                for ev in apoyo.split():
                    if ev not in evidencias:
                        errores.append(f'{lugar}: evidencia inexistente {ev}.')
    profundizaciones = datos.get('profundizaciones')
    if not isinstance(profundizaciones, list):
        return errores + ['profundizaciones debe ser una lista (puede estar vacía).']
    profundizados = set()
    for i, p in enumerate(profundizaciones, 1):
        lugar = f'Profundización {i}'
        if not isinstance(p, dict):
            errores.append(f'{lugar}: no es objeto.')
            continue
        for campo in CLAVES_PROFUNDAS:
            if not texto_valido(p, campo):
                errores.append(f'{lugar}: falta {campo}.')
        ident = p.get('id')
        if not isinstance(ident, str):
            errores.append(f'{lugar}: id debe ser texto.')
        else:
            if ident in profundizados:
                errores.append(f'{lugar}: id repetido.')
            profundizados.add(ident)
            if ident not in ids:
                errores.append(f'{lugar}: candidato inexistente {ident}.')
        if p.get('presencia') not in PRESENCIAS:
            errores.append(f'{lugar}: presencia inválida.')
    finales = datos.get('finalistas')
    if not isinstance(finales, list):
        errores.append('finalistas debe ser una lista, incluso cuando no haya ninguno.')
        return errores
    if len(finales) > 3:
        errores.append('Seleccionar como máximo tres finalistas; cero es válido.')
    if any(not isinstance(x, str) for x in finales) or len(set(map(str, finales))) != len(finales):
        errores.append('finalistas contiene IDs repetidos o inválidos.')
    for ident in finales:
        if not isinstance(ident, str):
            continue
        if ident not in ids:
            errores.append(f'Finalista {ident}: no existe entre los candidatos.')
        if ident not in profundizados:
            errores.append(f'Finalista {ident}: falta profundización causal.')
    if not finales and not texto_valido(datos, 'sin_finalistas_por_que'):
        errores.append('Sin finalistas: explicar por qué ninguna idea merece desarrollarse.')
    return errores


def revisar_historial(datos, reserva=RESERVA):
    """Solo revisión posterior; coincidencias textuales, NO juicio semántico."""
    hist = json.loads(reserva.read_text(encoding='utf-8'))['situaciones']
    advertencias = []
    for c in datos.get('candidatos', []):
        if not isinstance(c, dict):
            continue
        nucleo = c.get('nucleo') if isinstance(c.get('nucleo'), str) else ''
        situacion = c.get('situacion') if isinstance(c.get('situacion'), str) else ''
        texto = normalizar(nucleo + ' ' + situacion)
        for ref in hist:
            patron = normalizar(ref['nucleo'])
            if not patron or not texto:
                continue
            tokens, termino = set(texto.split()), set(patron.split())
            cobertura = len(tokens & termino) / len(termino)
            parecido = SequenceMatcher(None, normalizar(nucleo), patron).ratio()
            if parecido >= 0.77 or (len(termino) >= 4 and cobertura >= 0.85):
                advertencias.append(
                    f"{c.get('id', '?')}: revisar posible repetición de {ref['id']} (no es prueba semántica).")
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
        print('ESTRUCTURA: PASS (no evalúa creatividad ni valor psicológico).')
        if args.accion == 'revisar':
            avisos = revisar_historial(datos)
            for aviso in avisos:
                print('AVISO:', aviso)
            print(f'REVISIÓN: {len(avisos)} posibles similitudes; revisar manualmente.')
        return 0
    except (OSError, ValueError, KeyError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
