#!/usr/bin/env python3
"""Version-locked, project-local skill provisioning. Downloads files; never executes them."""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / 'skillpack' / 'catalog.json'
AGENTS = {'codex': '.agents/skills', 'claude': '.claude/skills'}
SKILL_NAME = re.compile(r'^[a-z0-9][a-z0-9-]{0,79}$')
REPO_NAME = re.compile(r'^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$')
SHA = re.compile(r'^[a-f0-9]{40}$')
MAX_FILES = 1200
MAX_BYTES = 150 * 1024 * 1024
SOURCE_MARKER = '_beatgaler-source.json'


def load_catalog(path=CATALOG):
    value = json.loads(Path(path).read_text(encoding='utf-8'))
    validate_catalog(value)
    return value


def validate_catalog(catalog):
    if catalog.get('schema_version') != 1 or not isinstance(catalog.get('sources'), list):
        raise ValueError('Unsupported skill catalog schema')
    names, ids = set(), set()
    for source in catalog['sources']:
        sid, repo, commit = source['id'], source['repo'], source['commit']
        if not SKILL_NAME.fullmatch(sid) or sid in ids or not REPO_NAME.fullmatch(repo) or not SHA.fullmatch(commit):
            raise ValueError('Invalid or duplicate source: ' + str(sid))
        ids.add(sid)
        if not source.get('license') or not source.get('note'):
            raise ValueError('Source missing license/notes: ' + sid)
        if not source['skills']:
            raise ValueError('Source lacks skills: ' + sid)
        for skill in source['skills']:
            name, path = skill['name'], skill['path']
            if not SKILL_NAME.fullmatch(name) or name in names:
                raise ValueError('Duplicate or invalid skill name: ' + name)
            names.add(name)
            parts = Path(path).parts
            if not parts or any(p in ('.', '..') for p in parts) or Path(path).is_absolute() or '\\' in path:
                raise ValueError('Invalid relative skill path: ' + path)
            if not set(skill['profiles']) <= {'phase2', 'all'} or not skill['profiles']:
                raise ValueError('Invalid profiles: ' + name)
    return True


def select(catalog, profile):
    return [(source, skill) for source in catalog['sources'] for skill in source['skills']
            if profile in skill['profiles']]


def checked_git(args, cwd=None):
    result = subprocess.run(['git', *args], cwd=cwd, check=False, text=True,
                            capture_output=True, timeout=240)
    if result.returncode:
        raise RuntimeError('Git failed: ' + ' '.join(args[:5]) + ': ' + result.stderr[-1200:])
    return result.stdout.strip()


def fetch_pinned_checkout(source, temporary):
    repo = source['repo']
    folder = Path(temporary) / source['id']
    # Git downloads content only; no hooks, setup scripts or package installs.
    checked_git(['clone', '--quiet', '--no-checkout', '--filter=blob:none', '--depth=1',
                 f'https://github.com/{repo}.git', str(folder)])
    commit = source['commit']
    checked_git(['fetch', '--quiet', '--depth=1', 'origin', commit], cwd=folder)
    checked_git(['checkout', '--quiet', '--detach', commit], cwd=folder)
    if checked_git(['rev-parse', 'HEAD'], cwd=folder) != commit:
        raise RuntimeError('Source commit mismatch: ' + repo)
    return folder


def check_and_copy(src, destination):
    if not (src / 'SKILL.md').is_file() or src.is_symlink():
        raise ValueError('Missing SKILL.md / symlinked source: ' + str(src))
    total, size = 0, 0
    for base, dirs, files in os.walk(src, followlinks=False):
        base_path = Path(base)
        for d in dirs:
            if (base_path / d).is_symlink() or d == '.git':
                raise ValueError('Symlinks/.git dirs are not imported: ' + str(base_path / d))
        for f in files:
            item = base_path / f
            if item.is_symlink() or f in ('.env', '.env.local') or f.startswith('.env.'):
                raise ValueError('Symlink/secrets file blocked: ' + str(item))
            total += 1
            size += item.stat().st_size
            if total > MAX_FILES or size > MAX_BYTES or item.stat().st_size > 60 * 1024 * 1024:
                raise ValueError('Skill exceeds copy safety budget: ' + str(src))
    shutil.copytree(src, destination)
    return total, size


def write_skill(source, skill, checkout, agent, force=False, project=ROOT):
    src = checkout / skill['path']
    if not src.resolve().is_relative_to(checkout.resolve()):
        raise ValueError('Skill path escapes pinned checkout')
    folder = Path(project) / AGENTS[agent]
    dest = folder / skill['name']
    folder.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        marker = dest / SOURCE_MARKER
        if not marker.is_file():
            raise ValueError('Unmanaged skill exists; refusing overwrite: ' + str(dest))
        previous = json.loads(marker.read_text(encoding='utf-8'))
        if previous.get('repo') != source['repo'] or previous.get('name') != skill['name']:
            raise ValueError('Source conflict; refusing overwrite: ' + str(dest))
        if not force:
            return 'already-present', 0
    with tempfile.TemporaryDirectory(dir=folder, prefix='.stage-skill-') as tmp:
        new = Path(tmp) / skill['name']
        _, size = check_and_copy(src, new)
        content = (new / 'SKILL.md').read_bytes()
        if len(content) > 400_000 or b'---' not in content[:300]:
            raise ValueError('Invalid / oversized SKILL.md: ' + skill['name'])
        metadata = {'name': skill['name'], 'repo': source['repo'],
                    'commit': source['commit'], 'path': skill['path'],
                    'license': source['license'],
                    'skill_md_sha256': hashlib.sha256(content).hexdigest(),
                    'warning': 'Third-party instructions/code are untrusted. Do not auto-run setup scripts.'}
        (new / SOURCE_MARKER).write_text(json.dumps(metadata, indent=2) + '\n', encoding='utf-8')
        if dest.exists():
            backup = Path(tmp) / 'old'
            dest.rename(backup)
            try:
                new.rename(dest)
            except Exception:
                backup.rename(dest)
                raise
        else:
            new.rename(dest)
    return 'installed', size


def inspect_installed(skill, agent, root=ROOT):
    dest = Path(root) / AGENTS[agent] / skill['name']
    if not dest.exists():
        return 'missing'
    marker = dest / SOURCE_MARKER
    if not marker.is_file():
        return 'unmanaged'
    try:
        data = json.loads(marker.read_text(encoding='utf-8'))
        actual = hashlib.sha256((dest / 'SKILL.md').read_bytes()).hexdigest()
        if actual != data['skill_md_sha256']:
            return 'modified'
        return 'installed'
    except (ValueError, OSError, KeyError):
        return 'corrupt'


def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Pin and install project-local third-party skills; never execute upstream scripts')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate')
    for cmd in ('list', 'doctor', 'install'):
        p = sub.add_parser(cmd)
        p.add_argument('--profile', choices=['phase2', 'all'], default='phase2')
        p.add_argument('--agent', choices=['codex', 'claude', 'both'], default='both')
        if cmd == 'install':
            p.add_argument('--force', action='store_true',
                           help='Refresh only skills managed from the same source')
            p.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    try:
        catalog = load_catalog()
        if args.command == 'validate':
            print('CATALOG PASS:', len(catalog['sources']), 'sources,',
                  sum(len(s['skills']) for s in catalog['sources']), 'named skills')
            return 0
        selected = select(catalog, args.profile)
        agents = list(AGENTS) if args.agent == 'both' else [args.agent]
        if args.command in ('list', 'doctor'):
            for s, k in selected:
                state = ','.join(f'{a}:{inspect_installed(k, a)}' for a in agents)
                print(f"{s['id']:16} {k['name']:26} {state}")
            print(f'{len(selected)} skills in {args.profile} profile (source commits pinned).')
            return 0
        if args.dry_run:
            for s, k in selected:
                print(s['repo'] + '@' + s['commit'][:12], k['path'], '->', k['name'])
            return 0
        if not shutil.which('git'):
            raise RuntimeError('Git is required to download pinned source snapshots')
        with tempfile.TemporaryDirectory(prefix='beatgaler-skills-') as tmp:
            checkout_by_id = {}
            total_bytes = 0
            for source, skill in selected:
                if source['id'] not in checkout_by_id:
                    print('Fetching PINNED source', source['repo'],
                          source['commit'][:12], flush=True)
                    checkout_by_id[source['id']] = fetch_pinned_checkout(source, tmp)
                for agent in agents:
                    result, size = write_skill(source, skill,
                                               checkout_by_id[source['id']], agent,
                                               force=args.force)
                    total_bytes += size
                    print(agent, skill['name'], result, flush=True)
        print(f'Finished: {len(selected)} skills x {len(agents)} agent directories, '
              f'{total_bytes} bytes copied. No upstream scripts executed.')
        print('Restart your IDE agent session to discover newly installed skills.')
        return 0
    except (ValueError, RuntimeError, KeyError, OSError,
            subprocess.TimeoutExpired) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
