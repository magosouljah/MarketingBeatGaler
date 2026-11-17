#!/usr/bin/env python3
"""Evaluacion de la calidad tecnica y artistica del trabajo de la IA en cada video.

Siete criterios ponderados (criteria.json), cada uno de 0 a 5 con decimales; el resultado
se presenta sobre 100. Un criterio que no aplica se marca `na` y su peso se reparte en
proporcion entre los demas. Cada video guarda todas sus versiones evaluadas.

    python learning/scorecard/scorecard.py add fuck --account account-1 --version final \
        animation=4.5 aesthetics=4 originality=3.5 consistency=4 broll=na realism=4 finish=4.5 \
        --comment aesthetics="el bote dibujado se veia infantil" --note "comentario general" \
        --evidence "Propietario, sesion <url>, 2026-11-16"
    python learning/scorecard/scorecard.py show            # ultima version de cada video
    python learning/scorecard/scorecard.py show fuck       # detalle de un video
    python learning/scorecard/scorecard.py compare fuck    # versiones de un video, con diferencias

Las calificaciones son SOLO del propietario: el agente las transcribe tal cual, nunca las
rellena ni las estima.
"""
import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
NA = ('na', 'n/a', '-')


def spec():
    data = json.loads((BASE / 'criteria.json').read_text(encoding='utf-8'))
    ids = [c['id'] for c in data['criteria']]
    if len(ids) != len(set(ids)):
        raise ValueError('criteria.json: hay id repetidos')
    if abs(sum(c['weight'] for c in data['criteria']) - 100) > 1e-9:
        raise ValueError('criteria.json: los pesos deben sumar 100')
    return data


def total(scores, criteria):
    """Puntuacion sobre 100. Los criterios en None (no aplica) ceden su peso a los demas."""
    used = [(c['weight'], scores[c['id']]) for c in criteria if scores.get(c['id']) is not None]
    weight = sum(w for w, _ in used)
    if not weight:
        raise ValueError('Ningun criterio aplica: no hay nada que puntuar')
    return round(sum(w * s for w, s in used) / weight / 5 * 100, 1)


def effective_weights(scores, criteria):
    weight = sum(c['weight'] for c in criteria if scores.get(c['id']) is not None)
    return {c['id']: round(c['weight'] / weight * 100, 1) for c in criteria if scores.get(c['id']) is not None}


def video_file(video):
    return BASE / 'evaluations' / f'{video}.json'


def load(video):
    path = video_file(video)
    if not path.exists():
        raise ValueError(f'No hay evaluaciones de {video}')
    return json.loads(path.read_text(encoding='utf-8'))


def all_videos():
    return sorted((json.loads(p.read_text(encoding='utf-8')) for p in (BASE / 'evaluations').glob('*.json')),
                  key=lambda r: (r['evaluations'][-1].get('date') or '', r['video']))


def add(video, account, version, pairs, comments, note, evidence, date):
    data = spec()
    criteria = data['criteria']
    ids = [c['id'] for c in criteria]
    lo, hi = data['scale']['min'], data['scale']['max']
    scores = {}
    for pair in pairs:
        key, _, value = pair.partition('=')
        if key not in ids:
            raise ValueError(f'Criterio desconocido: {key}. Validos: {", ".join(ids)}')
        if value.lower() in NA:
            scores[key] = None
            continue
        try:
            number = float(value)
        except ValueError:
            raise ValueError(f'{key}: la calificacion debe ser un numero de {lo} a {hi}, o na') from None
        if not lo <= number <= hi:
            raise ValueError(f'{key}: la calificacion debe estar entre {lo} y {hi}')
        scores[key] = number
    missing = [i for i in ids if i not in scores]
    if missing:
        raise ValueError('Faltan criterios (usar na si no aplica): ' + ', '.join(missing))
    notes = {}
    for pair in comments:
        key, _, text = pair.partition('=')
        if key not in ids or not text.strip():
            raise ValueError(f'Comentario invalido: {pair}. Formato: criterio="texto"')
        notes[key] = text.strip()
    if not version:
        raise ValueError('Falta --version: que version del video se evalua')
    if not evidence:
        raise ValueError('Falta --evidence: donde y cuando lo respondio el propietario')
    entry = {'version': version, 'date': date, 'criteria_version': data['version'], 'scores': scores,
             'comments': notes, 'note': note, 'evidence': evidence, 'total': total(scores, criteria)}
    path = video_file(video)
    record = json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'video': video, 'account': account, 'evaluations': []}
    if record['account'] != account:
        raise ValueError(f"{video} pertenece a {record['account']}, no a {account}")
    record['evaluations'] = [e for e in record['evaluations'] if e['version'] != version] + [entry]
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f"Guardado {video} / {version}: {entry['total']:.1f} de 100")
    low = [c['label'] for c in criteria if scores[c['id']] is not None and scores[c['id']] <= data['low_threshold']]
    if low:
        print(f"Criterios en {data['low_threshold']} o menos (preguntar que fallo y registrar como caso): " + ', '.join(low))
    return entry


def fmt(value):
    return 'n/a' if value is None else f'{value:g}'


def table(criteria, columns, entries, delta=False):
    width = max(len(c['label']) for c in criteria + [{'label': 'TOTAL sobre 100'}])
    col = max(8, max(len(n) for n in columns))
    print(' ' * width + '  peso  ' + '  '.join(f'{n[:col]:>{col}}' for n in columns) + ('     cambio' if delta else ''))
    for c in criteria:
        vals = [e['scores'].get(c['id']) for e in entries]
        change = ''
        if delta and len(vals) > 1 and vals[0] is not None and vals[-1] is not None:
            change = f'{vals[-1] - vals[0]:>+11.1f}'
        print(f"{c['label']:<{width}}  {c['weight']:>3}%  " + '  '.join(f'{fmt(v):>{col}}' for v in vals) + change)
    change = f"{entries[-1]['total'] - entries[0]['total']:>+11.1f}" if delta and len(entries) > 1 else ''
    print(f"{'TOTAL sobre 100':<{width}}        " + '  '.join(f"{e['total']:>{col}.1f}" for e in entries) + change)


def show(video=None):
    data = spec()
    criteria = data['criteria']
    if video:
        record = load(video)
        entry = record['evaluations'][-1]
        weights = effective_weights(entry['scores'], criteria)
        print(f"{record['video']} ({record['account']}) - version {entry['version']} - {entry.get('date') or 'sin fecha'}")
        for c in criteria:
            score = entry['scores'].get(c['id'])
            share = f"{weights[c['id']]:g}%" if score is not None else 'no aplica'
            line = f"  {c['label']:<20} {fmt(score):>4} / 5   peso {share}"
            if entry['comments'].get(c['id']):
                line += f"   - {entry['comments'][c['id']]}"
            print(line)
        print(f"  TOTAL: {entry['total']:.1f} de 100")
        if entry.get('note'):
            print(f"  Nota: {entry['note']}")
        if len(record['evaluations']) > 1:
            print(f"  {len(record['evaluations'])} versiones evaluadas: usar `compare {video}`")
        return
    records = all_videos()
    if not records:
        print('Aun no hay videos evaluados.')
        return
    table(criteria, [r['video'] for r in records], [r['evaluations'][-1] for r in records])


def compare(video):
    record = load(video)
    entries = record['evaluations']
    table(spec()['criteria'], [e['version'] for e in entries], entries, delta=True)
    for e in entries:
        for key, text in e['comments'].items():
            print(f"  [{e['version']}] {key}: {text}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    a = sub.add_parser('add')
    a.add_argument('video'); a.add_argument('pairs', nargs='+', metavar='criterio=N|na')
    a.add_argument('--account', required=True); a.add_argument('--version', default='')
    a.add_argument('--comment', action='append', default=[], metavar='criterio="texto"')
    a.add_argument('--note', default=''); a.add_argument('--evidence', default=''); a.add_argument('--date', default='')
    s = sub.add_parser('show'); s.add_argument('video', nargs='?')
    c = sub.add_parser('compare'); c.add_argument('video')
    args = parser.parse_args()
    try:
        if args.command == 'add':
            add(args.video, args.account, args.version, args.pairs, args.comment, args.note, args.evidence, args.date)
        elif args.command == 'show':
            show(args.video)
        else:
            compare(args.video)
    except ValueError as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
