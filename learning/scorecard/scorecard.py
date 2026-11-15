#!/usr/bin/env python3
"""Cuestionario de calificación 1-10 que el propietario responde al cerrar cada video.

    python learning/scorecard/scorecard.py add add-finder --account account-1 --version "final v2" \
        pacing=7 sync=9 motion=8 --note "el cierre se siente corto" --evidence "sesion <url>, 2026-11-15"
    python learning/scorecard/scorecard.py show

Las calificaciones son SOLO del propietario: el agente las transcribe tal cual, nunca las
rellena ni las estima. Un aspecto sin responder queda fuera (no se inventa un valor).
"""
import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
LOW = 6  # de aqui hacia abajo hay que preguntar que fallo y registrarlo como caso


def questions():
    return json.loads((BASE / 'questions.json').read_text(encoding='utf-8'))


def add(video, account, version, pairs, note, evidence, date):
    spec = questions()
    ids = [q['id'] for q in spec['questions']]
    scores = {}
    for pair in pairs:
        key, _, value = pair.partition('=')
        if key not in ids:
            raise ValueError(f'Aspecto desconocido: {key}. Validos: {", ".join(ids)}')
        if not value.isdigit() or not spec['scale']['min'] <= int(value) <= spec['scale']['max']:
            raise ValueError(f'{key}: la calificacion debe ser un entero de 1 a 10')
        scores[key] = int(value)
    if not scores:
        raise ValueError('Sin calificaciones')
    if not evidence:
        raise ValueError('Falta --evidence: donde y cuando lo respondio el propietario')
    record = {'video': video, 'account': account, 'version': version, 'date': date,
              'questionnaire_version': spec['version'], 'scores': scores, 'note': note, 'evidence': evidence}
    path = BASE / 'scores' / f'{video}.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    low = [k for k in ids if k in scores and scores[k] <= LOW]
    print(f'Guardado {path.relative_to(BASE.parent.parent) if BASE.parent.parent in path.parents else path}')
    print(f'Promedio: {sum(scores.values()) / len(scores):.1f} ({len(scores)}/{len(ids)} aspectos)')
    if low:
        print('Aspectos en 6 o menos (preguntar que fallo y registrar como caso): ' + ', '.join(low))
    return record


def show():
    spec = questions()
    records = sorted((json.loads(p.read_text(encoding='utf-8')) for p in (BASE / 'scores').glob('*.json')),
                     key=lambda r: (r.get('date') or '', r['video']))
    if not records:
        print('Aun no hay videos calificados.')
        return
    width = max(len(q['label']) for q in spec['questions'])
    print(' ' * width + '  ' + '  '.join(f"{r['video'][:12]:>12}" for r in records) + '      media')
    for q in spec['questions']:
        vals = [r['scores'].get(q['id']) for r in records]
        got = [v for v in vals if v is not None]
        mean = f'{sum(got) / len(got):.1f}' if got else '-'
        print(f"{q['label']:<{width}}  " + '  '.join(f"{(v if v is not None else '-'):>12}" for v in vals) + f'  {mean:>9}')
    print(f"{'Promedio':<{width}}  " + '  '.join(f"{sum(r['scores'].values()) / len(r['scores']):>12.1f}" for r in records))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    a = sub.add_parser('add')
    a.add_argument('video'); a.add_argument('pairs', nargs='+', metavar='aspecto=N')
    a.add_argument('--account', required=True); a.add_argument('--version', default='')
    a.add_argument('--note', default=''); a.add_argument('--evidence', default=''); a.add_argument('--date', default='')
    sub.add_parser('show')
    args = parser.parse_args()
    try:
        if args.command == 'add':
            add(args.video, args.account, args.version, args.pairs, args.note, args.evidence, args.date)
        else:
            show()
    except ValueError as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
