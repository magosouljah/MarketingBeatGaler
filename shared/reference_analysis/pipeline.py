"""Bounded, full-frame reference analysis. Python 3.10+, FFmpeg/ffprobe."""
import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VERSION = 1
LIMITATIONS = [
    'Cut candidates are grayscale difference heuristics: flashes and fast motion can trigger them.',
    'No semantic object, text, material, illumination, camera or 3D reconstruction is automatic.',
    'Identical thumbnails may indicate a hold, compression or lost detail, not a duplicated source frame.',
    'Stream timing offsets are technical warnings, not proof of perceptual audiovisual desynchronization.',
    'No automatic artistic approval; annotations and candidate rules require evidence and review.',
]


def dump(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8', newline='\n')


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def run(args, timeout=120):
    result = subprocess.run([str(a) for a in args], capture_output=True, timeout=timeout)
    if result.returncode:
        raise ValueError(f'{args[0]} failed: {result.stderr.decode("utf-8", errors="replace")[-3000:]}')
    return result.stdout


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Expected finite number')
    return value


def timestamps(frames):
    values = [float(f['best_effort_timestamp_time']) for f in frames]
    if not values or any(not math.isfinite(t) for t in values):
        raise ValueError('Missing/nonfinite frame timestamps')
    if any(b <= a for a, b in zip(values, values[1:])):
        raise ValueError('Duplicate or nonmonotonic presentation timestamps')
    return values


def metrics(data, size, times):
    if len(data) != size * len(times):
        raise ValueError('Decoded frame count differs from probed frame count')
    result = []
    previous = None
    for index, t in enumerate(times):
        pixels = data[index * size:(index + 1) * size]
        delta = sum(abs(a - b) for a, b in zip(previous, pixels)) / size / 255 if previous else 0
        result.append({'index': index, 'pts_seconds': t, 'time_seconds': t - times[0],
                       'luma_mean': sum(pixels) / size / 255,
                       'difference_mean': delta, 'thumbnail_sha256': hashlib.sha256(pixels).hexdigest()})
        previous = pixels
    return result


def annotations_validate(items, count):
    if not isinstance(items, list):
        raise ValueError('annotations must be a list')
    required = {'id', 'kind', 'start_frame', 'end_frame', 'claim', 'evidence', 'method', 'uncertainty'}
    seen = set()
    for item in items:
        if not isinstance(item, dict) or set(item) != required:
            raise ValueError('Annotation fields do not match contract')
        for key in ('id', 'claim', 'evidence', 'method', 'uncertainty'):
            if not isinstance(item[key], str) or not item[key].strip():
                raise ValueError(f'Annotation requires {key}')
        if item['id'] in seen or item['kind'] not in ('observation', 'estimate', 'interpretation', 'hypothesis'):
            raise ValueError('Duplicate annotation ID or invalid evidence kind')
        seen.add(item['id'])
        a, b = item['start_frame'], item['end_frame']
        if type(a) is not int or type(b) is not int or not 0 <= a <= b < count:
            raise ValueError('Annotation frame range invalid')
        # Free prose cannot be truth-checked by a schema. No user-authored measurement category.


def report_text(result):
    lines = ['# Reference Analysis V1', '',
             f"Source: `{result['source']['name']}`; SHA256 `{result['source']['sha256']}`.",
             f"Account: {result['account']}. Full source-frame coverage: {len(result['frames'])} frames.",
             '', '## Direct measurements', '',
             f"Video: {result['video']['width']}×{result['video']['height']}; reported average FPS {result['video']['avg_frame_rate']}.",
             f"Presentation span: {result['frames'][-1]['time_seconds']:.6f} s (first to last frame, not container duration).",
             'PTS are source presentation timestamps; local time subtracts the first video PTS.',
             'Luma/difference values describe 64×64 grayscale thumbnails, not object velocities.', '',
             '## Estimated temporal structure', '']
    for event in result['cut_candidates']:
        lines.append(f"- Candidate cut at frame {event['frame']} / {event['time_seconds']:.6f} s; validate visually.")
    if not result['cut_candidates']:
        lines.append('No candidate exceeded the configured threshold; this does not prove a continuous shot.')
    lines += ['', '## Audio stream timing', '', json.dumps(result['audio'], ensure_ascii=False),
              '', '## Human/agent annotations (not verified measurements)', '']
    for a in result['annotations']:
        lines += [f"- [{a['kind']}] {a['claim']} (frames {a['start_frame']}–{a['end_frame']}). Evidence: {a['evidence']}. Method: {a['method']}. Uncertainty: {a['uncertainty']}."]
    lines += ['', '## Estimated 2D trajectories', '',
              'Normalized coded-image coordinates (x right, y down); velocities use actual PTS. No inferred Z or camera pose.']
    for track in result['tracks']:
        lines.append(f"- {track['id']}: {len(track['samples'])} annotated samples; evidence: {track['evidence']}; uncertainty: {track['uncertainty']}.")
    lines += ['', '## Warnings', ''] + [f'- {w}' for w in result['warnings']]
    lines += ['', '## Limitations / next checks', ''] + [f'- {s}' for s in LIMITATIONS]
    lines += ['', 'Review every constituent movement independently: translation, scale, visible rotation, overlap/occlusion, apparent depth and camera hypotheses.',
              'Inspect timing/spacing, anticipation, arcs, overlapping action, typography, contrast, color, sound events and continuity on consecutive frames.',
              'For reconstruction compare aligned local times and aspect ratios, then render a small original blocking test before shading.']
    return '\n'.join(lines) + '\n'


def derive_tracks(tracks, times):
    if not isinstance(tracks, list):
        raise ValueError('Tracks must be a list')
    output, seen = [], set()
    for track in tracks:
        if set(track) != {'id', 'samples', 'evidence', 'uncertainty'}:
            raise ValueError('Track fields do not match contract')
        for key in ('id', 'evidence', 'uncertainty'):
            if not isinstance(track[key], str) or not track[key].strip():
                raise ValueError(f'Track requires {key}')
        if track['id'] in seen or not isinstance(track['samples'], list) or len(track['samples']) < 2:
            raise ValueError('Duplicate track or insufficient samples')
        seen.add(track['id'])
        previous, velocity = None, None
        segments = []
        for sample in track['samples']:
            if set(sample) != {'frame', 'x', 'y'} or type(sample['frame']) is not int or not 0 <= sample['frame'] < len(times):
                raise ValueError('Invalid track sample')
            for key in ('x', 'y'):
                if not 0 <= finite(sample[key]) <= 1:
                    raise ValueError('Coordinates must be normalized to [0,1]')
            if previous:
                if sample['frame'] <= previous['frame']:
                    raise ValueError('Track frames must increase; split at cuts and occlusions')
                dt = times[sample['frame']] - times[previous['frame']]
                vx, vy = (sample['x']-previous['x'])/dt, (sample['y']-previous['y'])/dt
                midpoint = (times[sample['frame']] + times[previous['frame']])/2
                segment = {'from_frame': previous['frame'], 'to_frame': sample['frame'],
                           'vx_per_second': vx, 'vy_per_second': vy}
                if velocity:
                    segment['ax_per_second2'] = (vx-velocity[0])/(midpoint-velocity[2])
                    segment['ay_per_second2'] = (vy-velocity[1])/(midpoint-velocity[2])
                velocity = vx, vy, midpoint
                segments.append(segment)
            previous = sample
        output.append({**track, 'kind': 'estimate', 'segments': segments})
    return output


def analyze(source, output, account='account-1', max_seconds=60, max_frames=1800,
            max_bytes=512 * 1024 * 1024, cut_threshold=0.22, annotations=None, tracks=None):
    source, output = Path(source).resolve(), Path(output).resolve()
    if not source.is_file():
        raise ValueError('Input must be an accessible local video file')
    if output.exists():
        raise ValueError('Output already exists; use a new run directory')
    if account not in ('account-1', 'account-2') or not 0 < cut_threshold < 1:
        raise ValueError('Invalid account or cut threshold')
    if source.stat().st_size > max_bytes:
        raise ValueError('Source exceeds byte budget')
    for tool in ('ffmpeg', 'ffprobe'):
        if not shutil.which(tool):
            raise ValueError(f'Required tool unavailable: {tool}')
    # Restrict protocols, forbid network inputs nested inside a local manifest.
    probe_args = ['ffprobe', '-v', 'error', '-protocol_whitelist', 'file,pipe', '-show_streams', '-show_format', '-of', 'json', source]
    raw_probe = run(probe_args)
    probe = json.loads(raw_probe)
    video = next((s for s in probe['streams'] if s['codec_type'] == 'video' and not s.get('disposition', {}).get('attached_pic')), None)
    if not video:
        raise ValueError('No video stream')
    duration = float(probe['format'].get('duration', video.get('duration', 'nan')))
    if not math.isfinite(duration) or not 0 < duration <= max_seconds:
        raise ValueError('Unknown duration or duration exceeds budget')
    if video['width'] * video['height'] > 3840 * 2160:
        raise ValueError('Video exceeds 4K pixel budget')
    stream = str(video['index'])
    frame_probe_args = ['ffprobe', '-v', 'error', '-protocol_whitelist', 'file,pipe', '-select_streams', stream,
                        '-read_intervals', f'%+#{max_frames + 2}', '-show_frames', '-show_entries',
                        'frame=best_effort_timestamp_time,pkt_duration_time', '-of', 'json', source]
    raw_frames = run(frame_probe_args)
    times = timestamps(json.loads(raw_frames)['frames'])
    if len(times) > max_frames or times[-1] - times[0] > max_seconds:
        raise ValueError('Frame/time budget exceeded; no silent temporal subsampling')
    notes = [] if annotations is None else json.loads(Path(annotations).read_text(encoding='utf-8'))
    annotations_validate(notes, len(times))
    track_data = derive_tracks([] if tracks is None else json.loads(Path(tracks).read_text(encoding='utf-8')), times)
    source_hash = digest(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.reference-', dir=output.parent) as temp:
        temp = Path(temp)
        (temp / 'frames').mkdir()
        commands = []
        base = ['ffmpeg', '-nostdin', '-v', 'error', '-xerror', '-threads', '1', '-protocol_whitelist', 'file,pipe', '-noautorotate', '-copyts', '-i', source,
                '-map', f'0:{stream}', '-an', '-sn', '-dn']
        cmd = base + ['-vf', 'scale=64:64,format=gray', '-fps_mode', 'passthrough', '-frames:v', str(max_frames + 1), '-f', 'rawvideo', 'pipe:1']
        commands.append([str(x) for x in cmd])
        rows = metrics(run(cmd), 4096, times)
        cmd = base + ['-vf', r'scale=w=min(640\,iw):h=-2', '-fps_mode', 'passthrough', '-frames:v', str(max_frames + 1), '-threads', '1', temp / 'frames/%06d.png']
        commands.append([str(x) for x in cmd])
        run(cmd)
        files = sorted((temp / 'frames').glob('*.png'))
        if len(files) != len(rows):
            raise ValueError('Extracted PNG count differs from presentation frame count')
        for row, file in zip(rows, files):
            row['file'] = f'frames/{file.name}'
            row['sha256'] = digest(file)
        cuts = [{'kind': 'estimate', 'frame': r['index'], 'time_seconds': r['time_seconds'],
                 'evidence': f"difference_mean={r['difference_mean']:.6f}", 'method': 'adjacent grayscale mean absolute difference'}
                for r in rows[1:] if r['difference_mean'] >= cut_threshold]
        audio = []
        warnings = []
        for s in probe['streams']:
            if s['codec_type'] == 'audio':
                start = float(s['start_time']) if 'start_time' in s else None
                offset = start - times[0] if start is not None else None
                audio.append({'stream_index': s['index'], 'start_pts_seconds': start,
                              'offset_from_video_seconds': offset, 'sample_rate': s.get('sample_rate')})
                if offset is None or abs(offset) > 0.05:
                    warnings.append(f"Audio stream {s['index']}: unknown or >50ms start offset; inspect intended alignment.")
        repeated = [r['index'] for a, r in zip(rows, rows[1:]) if a['thumbnail_sha256'] == r['thumbnail_sha256']]
        if repeated:
            warnings.append(f'{len(repeated)} consecutive identical grayscale thumbnails; inspect holds/duplicates.')
        intervals = [b - a for a, b in zip(times, times[1:])]
        if intervals and max(intervals) > min(intervals) * 1.5:
            warnings.append('Variable presentation intervals or gaps; source timing retained, not classified as missing frames.')
        if video.get('tags', {}).get('rotate') or any('rotation' in s for s in video.get('side_data_list', [])):
            warnings.append('Display rotation metadata present; PNGs preserve coded orientation (--noautorotate).')
        result = {'schema_version': VERSION, 'account': account,
                  'source': {'name': source.name, 'sha256': source_hash, 'bytes': source.stat().st_size},
                  'video': {k: video.get(k) for k in ('index', 'width', 'height', 'avg_frame_rate', 'r_frame_rate', 'time_base', 'sample_aspect_ratio', 'color_space', 'color_transfer')},
                  'container_duration_seconds': duration, 'sampling': 'all-presentation-frames',
                  'measurement_method': 'ffprobe best_effort_timestamp_time; FFmpeg grayscale 64x64 and coded-orientation PNG <=640px',
                  'cut_threshold': cut_threshold, 'frames': rows, 'audio': audio,
                  'cut_candidates': cuts, 'annotations': notes, 'tracks': track_data, 'warnings': warnings, 'limitations': LIMITATIONS}
        (temp / 'probe.json').write_bytes(raw_probe)
        (temp / 'frame-probe.json').write_bytes(raw_frames)
        dump(temp / 'analysis.json', result)
        (temp / 'report.md').write_text(report_text(result), encoding='utf-8', newline='\n')
        versions = {t: run([t, '-version']).decode('utf-8', errors='replace').splitlines()[0] for t in ('ffmpeg', 'ffprobe')}
        dump(temp / 'provenance.json', {'tools': versions, 'python': sys.version, 'source': str(source),
                                       'commands': commands, 'probe_command': [str(x) for x in probe_args],
                                       'frame_probe_command': [str(x) for x in frame_probe_args]})
        if digest(source) != source_hash:
            raise ValueError('Input changed during processing')
        dump(temp / 'manifest.json', {str(p.relative_to(temp)).replace('\\', '/'): digest(p)
                                     for p in sorted(temp.rglob('*')) if p.is_file()})
        validate(temp)
        temp.rename(output)
    return result


def validate(folder):
    folder = Path(folder)
    manifest = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    actual = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()} - {'manifest.json'}
    if set(manifest) != actual:
        raise ValueError('Output missing or unexpected files')
    required = {'analysis.json', 'report.md', 'probe.json', 'frame-probe.json', 'provenance.json'}
    if not required <= set(manifest):
        raise ValueError('Incomplete output contract')
    for name, sha in manifest.items():
        path = folder / name
        if not path.resolve().is_relative_to(folder.resolve()) or digest(path) != sha:
            raise ValueError(f'Invalid path or output hash mismatch: {name}')
    data = json.loads((folder / 'analysis.json').read_text(encoding='utf-8'))
    expected_keys = {'schema_version', 'account', 'source', 'video', 'container_duration_seconds', 'sampling',
                     'measurement_method', 'cut_threshold', 'frames', 'audio', 'cut_candidates', 'annotations',
                     'tracks', 'warnings', 'limitations'}
    if set(data) != expected_keys:
        raise ValueError('Analysis fields do not match V1 contract')
    if data['schema_version'] != VERSION or data['account'] not in ('account-1', 'account-2') or data['sampling'] != 'all-presentation-frames':
        raise ValueError('Invalid analysis version/account/sampling')
    rows = data['frames']
    times = timestamps(json.loads((folder / 'frame-probe.json').read_text(encoding='utf-8'))['frames'])
    if len(rows) != len(times):
        raise ValueError('Missing or duplicated frame records')
    expected_files = set()
    for index, (row, t) in enumerate(zip(rows, times)):
        if set(row) != {'index', 'pts_seconds', 'time_seconds', 'luma_mean', 'difference_mean', 'thumbnail_sha256', 'file', 'sha256'}:
            raise ValueError('Frame fields do not match measurement contract')
        name = f'frames/{index + 1:06d}.png'
        if row['index'] != index or row['file'] != name or finite(row['pts_seconds']) != t or abs(finite(row['time_seconds']) - (t-times[0])) > 1e-9:
            raise ValueError('Frame index/file/timestamp mismatch')
        if row['sha256'] != manifest.get(name):
            raise ValueError('Frame integrity mismatch')
        for key in ('difference_mean', 'luma_mean'):
            if not 0 <= finite(row[key]) <= 1:
                raise ValueError('Invalid normalized metric')
        expected_files.add(name)
    if expected_files != {p for p in manifest if p.startswith('frames/')}:
        raise ValueError('Frame sequence incomplete')
    annotations_validate(data['annotations'], len(rows))
    raw_tracks = [{k: track[k] for k in ('id', 'samples', 'evidence', 'uncertainty')} for track in data['tracks']]
    if derive_tracks(raw_tracks, times) != data['tracks']:
        raise ValueError('Track classification or kinematics mismatch')
    for event in data['cut_candidates']:
        if set(event) != {'kind', 'frame', 'time_seconds', 'evidence', 'method'}:
            raise ValueError('Cut fields do not match estimate contract')
        if event['kind'] != 'estimate' or type(event['frame']) is not int or not 0 < event['frame'] < len(rows):
            raise ValueError('Cut candidate must be an estimate at a valid frame')
        if event['time_seconds'] != rows[event['frame']]['time_seconds']:
            raise ValueError('Cut time mismatch')
    if (folder / 'report.md').read_text(encoding='utf-8') != report_text(data):
        raise ValueError('Report does not match structured data')
    return data


def register(folder, case_id):
    # Reuse the existing engine; never promote or set human approval.
    from learning import engine
    data = validate(folder)
    folder = Path(folder).resolve()
    if not folder.is_relative_to(engine.ROOT):
        raise ValueError('Versioned learning evidence must be inside the marketing repository')
    target = engine.case_file(case_id)
    if target.exists():
        raise ValueError('Case exists; preserve history and use a new ID')
    relative = folder.relative_to(engine.ROOT).as_posix()
    case = {'id': case_id, 'account': data['account'], 'project': 'reference-intelligence-v1',
            'human_approved': False, 'source': f"{relative}/analysis.json; source SHA256 {data['source']['sha256']}",
            'checks': [{'id': 'reference-integrity', 'status': 'pass',
                        'evidence': f'{relative}/manifest.json validated against all output files and source frame PTS.'}]}
    engine.write_json(target, case)
    engine.review(case_id)
    return case


def record_failure(case_id, account, diagnostic):
    from learning import engine
    target = engine.case_file(case_id)
    if target.exists() or account not in engine.ACCOUNTS:
        raise ValueError('Case exists or invalid account')
    note = json.loads(Path(diagnostic).read_text(encoding='utf-8'))
    fields = {'check_id', 'evidence', 'cause_category', 'hypothesis', 'problem', 'implementation', 'use_when', 'avoid_when', 'acceptance_test'}
    if set(note) != fields or any(not isinstance(v, str) or not v.strip() for v in note.values()):
        raise ValueError('Incomplete failure diagnostic')
    categories = {'reference-interpretation', 'tool-choice', 'implementation', 'technical-knowledge', 'ambiguous-instructions', 'evaluation-process'}
    if note['cause_category'] not in categories or not engine.SLUG.fullmatch(note['check_id']):
        raise ValueError('Invalid cause category/check ID')
    rule = '\n'.join(f'{key}: {note[key]}' for key in ('problem', 'implementation', 'use_when', 'avoid_when'))
    case = {'id': case_id, 'account': account, 'project': 'reference-intelligence-v1', 'human_approved': False,
            'checks': [{'id': note['check_id'], 'status': 'fail', 'evidence': note['evidence'],
                        'hypothesis': f"[{note['cause_category']}; unvalidated] {note['hypothesis']}",
                        'proposed_rule': rule, 'acceptance_test': note['acceptance_test']}]}
    engine.write_json(target, case)
    engine.review(case_id)
    return case


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    a = sub.add_parser('analyze')
    a.add_argument('source'); a.add_argument('output')
    a.add_argument('--account', choices=['account-1', 'account-2'], required=True)
    a.add_argument('--annotations')
    a.add_argument('--tracks')
    a.add_argument('--max-seconds', type=float, default=60)
    a.add_argument('--max-frames', type=int, default=1800)
    a.add_argument('--cut-threshold', type=float, default=0.22)
    v = sub.add_parser('validate'); v.add_argument('output')
    r = sub.add_parser('register'); r.add_argument('output'); r.add_argument('case_id')
    f = sub.add_parser('failure'); f.add_argument('case_id'); f.add_argument('diagnostic')
    f.add_argument('--account', choices=['account-1', 'account-2'], required=True)
    args = parser.parse_args()
    try:
        if args.command == 'analyze':
            analyze(args.source, args.output, args.account, args.max_seconds, args.max_frames,
                    cut_threshold=args.cut_threshold, annotations=args.annotations, tracks=args.tracks)
        elif args.command == 'validate': validate(args.output)
        elif args.command == 'failure': record_failure(args.case_id, args.account, args.diagnostic)
        else: register(args.output, args.case_id)
        print(f'{args.command}: PASS')
        return 0
    except (ValueError, OSError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
