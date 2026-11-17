import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scorecard'))
import scorecard  # noqa: E402

ALL = ['animation=4', 'aesthetics=4', 'originality=4', 'consistency=4', 'broll=4', 'realism=4', 'finish=4']


class ScorecardTest(unittest.TestCase):
    def run_in_temp(self, fn):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            (base / 'criteria.json').write_text((scorecard.BASE / 'criteria.json').read_text(encoding='utf-8'), encoding='utf-8')
            with patch.object(scorecard, 'BASE', base):
                return fn(base)

    def test_criteria_weights_sum_100_and_scale_is_zero_to_five(self):
        data = scorecard.spec()
        self.assertEqual(sum(c['weight'] for c in data['criteria']), 100)
        self.assertEqual((data['scale']['min'], data['scale']['max']), (0, 5))
        self.assertEqual([c['weight'] for c in data['criteria']], [20, 20, 15, 15, 10, 10, 10])

    def test_weighted_total_over_100_with_decimals(self):
        def body(base):
            entry = scorecard.add('demo', 'account-1', 'v1', ['animation=5', 'aesthetics=2.5', 'originality=4', 'consistency=3',
                                                              'broll=1', 'realism=0', 'finish=5'], [], '', 'Owner, chat', '2026-01-01')
            # (20*5 + 20*2.5 + 15*4 + 15*3 + 10*1 + 10*0 + 10*5) / 100 / 5 * 100 = 63
            self.assertEqual(entry['total'], 63.0)
        self.run_in_temp(body)

    def test_not_applicable_redistributes_weight_proportionally(self):
        def body(base):
            pairs = ['animation=5', 'aesthetics=5', 'originality=5', 'consistency=5', 'broll=na', 'realism=0', 'finish=5']
            entry = scorecard.add('demo', 'account-1', 'v1', pairs, [], '', 'Owner, chat', '')
            self.assertIsNone(entry['scores']['broll'])
            self.assertEqual(entry['total'], round(80 / 90 * 100, 1))
            weights = scorecard.effective_weights(entry['scores'], scorecard.spec()['criteria'])
            self.assertNotIn('broll', weights)
            self.assertAlmostEqual(sum(weights.values()), 100, delta=0.3)
            self.assertEqual(weights['animation'], 22.2)
        self.run_in_temp(body)

    def test_versions_are_kept_per_video_and_compared(self):
        def body(base):
            scorecard.add('demo', 'account-1', 'v1', ALL, ['finish=bordes pixelados'], 'nota', 'Owner, chat', '2026-01-01')
            scorecard.add('demo', 'account-1', 'v2', ALL[:-1] + ['finish=5'], [], '', 'Owner, chat', '2026-01-02')
            scorecard.add('demo', 'account-1', 'v2', ALL[:-1] + ['finish=4.5'], [], '', 'Owner, chat', '2026-01-02')
            saved = json.loads((base / 'evaluations/demo.json').read_text(encoding='utf-8'))
            self.assertEqual([e['version'] for e in saved['evaluations']], ['v1', 'v2'])
            self.assertEqual(saved['evaluations'][0]['comments'], {'finish': 'bordes pixelados'})
            self.assertEqual(saved['evaluations'][1]['scores']['finish'], 4.5)
            scorecard.show(); scorecard.show('demo'); scorecard.compare('demo')
        self.run_in_temp(body)

    def test_rejects_bad_input(self):
        def body(base):
            bad = [(ALL[:-1], 'v1', 'x'), (ALL[:-1] + ['nope=3'], 'v1', 'x'), (ALL[:-1] + ['finish=5.1'], 'v1', 'x'),
                   (ALL[:-1] + ['finish=-1'], 'v1', 'x'), (ALL[:-1] + ['finish=bien'], 'v1', 'x'), (ALL, 'v1', ''), (ALL, '', 'x'),
                   ([p.split('=')[0] + '=na' for p in ALL], 'v1', 'x')]
            for pairs, version, evidence in bad:
                with self.assertRaises(ValueError):
                    scorecard.add('demo', 'account-1', version, pairs, [], '', evidence, '')
            with self.assertRaises(ValueError):
                scorecard.add('demo', 'account-1', 'v1', ALL, ['nope=texto'], '', 'x', '')
        self.run_in_temp(body)


if __name__ == '__main__':
    unittest.main()
