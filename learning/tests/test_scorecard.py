import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scorecard'))
import scorecard  # noqa: E402


class ScorecardTest(unittest.TestCase):
    def run_in_temp(self, fn):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / 'questions.json').write_text((scorecard.BASE / 'questions.json').read_text(encoding='utf-8'), encoding='utf-8')
            with patch.object(scorecard, 'BASE', base):
                return fn(base)

    def test_question_ids_are_unique_and_scale_is_one_to_ten(self):
        spec = scorecard.questions()
        ids = [q['id'] for q in spec['questions']]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual((spec['scale']['min'], spec['scale']['max']), (1, 10))

    def test_add_stores_only_what_the_owner_answered(self):
        def body(base):
            scorecard.add('demo', 'account-1', 'v1', ['hook=8', 'pacing=5'], 'nota', 'Owner, chat', '2026-01-01')
            saved = json.loads((base / 'scores/demo.json').read_text(encoding='utf-8'))
            self.assertEqual(saved['scores'], {'hook': 8, 'pacing': 5})
            scorecard.show()
        self.run_in_temp(body)

    def test_rejects_unknown_aspect_out_of_range_and_missing_evidence(self):
        def body(base):
            for pairs, evidence in ((['nope=5'], 'x'), (['hook=11'], 'x'), (['hook=0'], 'x'), (['hook=7'], '')):
                with self.assertRaises(ValueError):
                    scorecard.add('demo', 'account-1', '', pairs, '', evidence, '')
        self.run_in_temp(body)


if __name__ == '__main__':
    unittest.main()
