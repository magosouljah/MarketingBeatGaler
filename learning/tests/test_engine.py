import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from learning import engine


class LearningEngineTests(unittest.TestCase):
    def test_repository_audits(self):
        engine.audit()

    def test_rejection_is_not_approved(self):
        case = engine.load_case('orbit-initial-rejection')
        self.assertFalse(case['human_approved'])
        self.assertEqual(len([c for c in case['checks'] if c['status'] == 'fail']), 2)

    def test_invalid_ids_rejected(self):
        with self.assertRaises(ValueError):
            engine.case_file('../DIRECCION')

    def test_direction_tampering_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / '.github').mkdir()
            (root / '.github/direccion.sha256').write_text((engine.ROOT / '.github/direccion.sha256').read_text())
            (root / 'DIRECCION.md').write_text('Changed without approval')
            with patch.object(engine, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'DIRECCION.md changed'):
                    engine.audit()

    def test_promote_requires_new_verified_case(self):
        proposal = engine.read_json(engine.proposal_file('orbit-initial-rejection--orbit-depth'))
        engine.validate_proposal(proposal)
        with self.assertRaises(ValueError):
            engine.promote(proposal['id'], 'orbit-initial-rejection')

    def test_review_creates_reproducible_report_and_proposals(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / 'cases').mkdir()
            original = json.loads((engine.BASE / 'cases/orbit-initial-rejection.json').read_text())
            (base / 'cases/orbit-initial-rejection.json').write_text(json.dumps(original))
            with patch.object(engine, 'BASE', base):
                engine.review('orbit-initial-rejection')
                self.assertTrue((base / 'reviews/orbit-initial-rejection.json').exists())
                self.assertEqual(len(list((base / 'proposals').glob('*.json'))), 2)
                engine.review('orbit-initial-rejection')

    def test_promotion_requires_owner_approval_and_passing_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / 'cases').mkdir()
            initial = engine.read_json(engine.BASE / 'cases/orbit-initial-rejection.json')
            verified = {
                'id': 'orbit-second-test', 'account': 'account-1', 'project': 'first-ad',
                'human_approved': False,
                'validates_proposal': 'orbit-initial-rejection--orbit-depth',
                'checks': [{'id': 'orbit-depth', 'status': 'pass', 'evidence': 'Render at https://example.com/approved-preview.mp4 and review'}]
            }
            (base / 'cases/orbit-initial-rejection.json').write_text(json.dumps(initial))
            (base / 'cases/orbit-second-test.json').write_text(json.dumps(verified))
            with patch.object(engine, 'BASE', base):
                engine.review('orbit-initial-rejection')
                with self.assertRaisesRegex(ValueError, 'Creative approval'):
                    engine.promote('orbit-initial-rejection--orbit-depth', 'orbit-second-test')
                verified['human_approved'] = True
                verified['approval_evidence'] = 'Owner approved in conversation with verified link'
                (base / 'cases/orbit-second-test.json').write_text(json.dumps(verified))
                engine.promote('orbit-initial-rejection--orbit-depth', 'orbit-second-test')
                lesson = base / 'lessons/account-1/orbit-depth.md'
                self.assertTrue(lesson.exists())
                self.assertIn('Validated prevention rule', lesson.read_text())


if __name__ == '__main__':
    unittest.main()
