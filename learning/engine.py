#!/usr/bin/env python3
"""Auditable feedback loop for BeatGaler. Python stdlib only; no AI claims."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / 'learning'
ACCOUNTS = {'account-1', 'account-2'}
SLUG = re.compile(r'^[a-z0-9][a-z0-9-]{1,79}$')


def fail(message):
    raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')


def case_file(case_id):
    if not SLUG.fullmatch(case_id):
        fail(f'Invalid case id: {case_id}')
    return BASE / 'cases' / f'{case_id}.json'


def proposal_file(proposal_id):
    if not SLUG.fullmatch(proposal_id):
        fail(f'Invalid proposal id: {proposal_id}')
    return BASE / 'proposals' / f'{proposal_id}.json'


def load_case(case_id):
    path = case_file(case_id)
    data = read_json(path)
    if data.get('id') != case_id or data.get('account') not in ACCOUNTS:
        fail(f'Bad case ID/account in {path}')
    if not isinstance(data.get('project'), str) or not data['project'].strip():
        fail(f'Missing project in {path}')
    checks = data.get('checks')
    if not isinstance(checks, list) or not checks:
        fail(f'Missing checks in {path}')
    seen = set()
    for check in checks:
        cid = check.get('id')
        if not isinstance(cid, str) or not SLUG.fullmatch(cid) or cid in seen:
            fail(f'Duplicate/invalid check id in {path}: {cid}')
        seen.add(cid)
        if check.get('status') not in ('pass', 'fail'):
            fail(f'Invalid status for {cid}')
        if not isinstance(check.get('evidence'), str) or not check['evidence'].strip():
            fail(f'Missing evidence for {cid}')
        if check['status'] == 'fail':
            for field in ('hypothesis', 'proposed_rule', 'acceptance_test'):
                if not isinstance(check.get(field), str) or not check[field].strip():
                    fail(f'Missing {field} for failed check {cid}')
    if data.get('human_approved') not in (True, False):
        fail(f'Missing boolean human_approved in {path}')
    return data


def make_proposal(source, check):
    return {
        'id': f"{source['id']}--{check['id']}",
        'source_case': source['id'],
        'account': source['account'],
        'check_id': check['id'],
        'problem_evidence': check['evidence'],
        'cause_hypothesis': check['hypothesis'],
        'candidate_rule': check['proposed_rule'],
        'acceptance_test': check['acceptance_test'],
        'state': 'proposed',
    }


def review(case_id):
    data = load_case(case_id)
    report = {'case_id': case_id, 'account': data['account'],
              'human_approved': data['human_approved'],
              'failed': [c['id'] for c in data['checks'] if c['status'] == 'fail'],
              'passed': [c['id'] for c in data['checks'] if c['status'] == 'pass']}
    write_json(BASE / 'reviews' / f'{case_id}.json', report)
    for check in data['checks']:
        if check['status'] == 'fail':
            proposal = make_proposal(data, check)
            path = proposal_file(proposal['id'])
            if path.exists() and read_json(path) != proposal:
                fail(f'Existing proposal changed: {path}; preserve history, create new case')
            write_json(path, proposal)
    print(f"Reviewed {case_id}: {len(report['failed'])} failed, {len(report['passed'])} passed; proposals are NOT validated lessons")


def promote(proposal_id, verified_case_id):
    proposal = read_json(proposal_file(proposal_id))
    validate_proposal(proposal)
    source = load_case(proposal['source_case'])
    verified = load_case(verified_case_id)
    if verified['id'] == source['id'] or verified['account'] != proposal['account']:
        fail('Verification must be a different case for the same account')
    if verified.get('validates_proposal') != proposal_id:
        fail('Verification case must explicitly cite the proposal')
    if not verified['human_approved'] or not verified.get('approval_evidence'):
        fail('Creative approval by the owner with evidence is required')
    check = next((c for c in verified['checks'] if c['id'] == proposal['check_id']), None)
    if not check or check['status'] != 'pass':
        fail('The same check must PASS in verification case')
    target = BASE / 'lessons' / proposal['account'] / f"{proposal['check_id']}.md"
    if target.exists():
        fail(f'Lesson exists: {target}; revise via a new proposal and review')
    body = (f"# {proposal['check_id']}\n\n"
            f"- Scope: `{proposal['account']}`\n"
            f"- Origin: `{source['id']}`\n"
            f"- Verified: `{verified['id']}`\n"
            f"- Owner approval: {verified['approval_evidence']}\n\n"
            f"## Problem observed\n{proposal['problem_evidence']}\n\n"
            f"## Hypothesized cause\n{proposal['cause_hypothesis']}\n\n"
            f"## Validated prevention rule\n{proposal['candidate_rule']}\n\n"
            f"## Verification required for future videos\n{proposal['acceptance_test']}\n\n"
            f"## Passing evidence\n{check['evidence']}\n")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding='utf-8')
    print(f'Validated lesson created: {target}')


def validate_proposal(p):
    if p.get('state') != 'proposed' or p.get('account') not in ACCOUNTS:
        fail('Invalid proposal state/account')
    expected_id = f"{p.get('source_case')}--{p.get('check_id')}"
    if p.get('id') != expected_id or not SLUG.fullmatch(expected_id):
        fail('Invalid proposal ID')
    source = load_case(p['source_case'])
    found = next((c for c in source['checks'] if c['id'] == p['check_id'] and c['status'] == 'fail'), None)
    if source['account'] != p['account'] or not found or p != make_proposal(source, found):
        fail('Proposal no longer matches source evidence')


def audit():
    protected = (ROOT / 'DIRECCION.md').read_bytes()
    actual = hashlib.sha256(protected).hexdigest()
    expected = (ROOT / '.github' / 'direccion.sha256').read_text().strip().split()[0]
    if actual != expected:
        fail('DIRECCION.md changed: explicit owner authorization and hash update required')
    for path in sorted((BASE / 'cases').glob('*.json')):
        load_case(path.stem)
    for path in sorted((BASE / 'proposals').glob('*.json')):
        p = read_json(path)
        validate_proposal(p)
        if path.stem != p['id']:
            fail(f'Proposal filename mismatch: {path}')
    print('AUDIT PASS: direction integrity, cases and proposals')


def status():
    audit()
    cases = len(list((BASE / 'cases').glob('*.json')))
    proposals = len(list((BASE / 'proposals').glob('*.json')))
    lessons = len(list((BASE / 'lessons').glob('**/*.md')))
    print(f'Cases: {cases} | Proposed (not validated): {proposals} | Validated lessons: {lessons}')
    print('Next: produce a verifiable new orbit test, log its evaluation, and request creative approval.')


def main():
    parser = argparse.ArgumentParser(description='BeatGaler audit-and-learn engine')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('audit')
    sub.add_parser('status')
    r = sub.add_parser('review')
    r.add_argument('case_id')
    p = sub.add_parser('promote')
    p.add_argument('proposal_id')
    p.add_argument('verified_case_id')
    args = parser.parse_args()
    try:
        if args.command == 'audit': audit()
        elif args.command == 'status': status()
        elif args.command == 'review': review(args.case_id)
        elif args.command == 'promote': promote(args.proposal_id, args.verified_case_id)
    except (ValueError, FileNotFoundError, KeyError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
