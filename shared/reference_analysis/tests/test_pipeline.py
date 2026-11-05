import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from learning import engine
from shared.reference_analysis import pipeline as p
from shared.reference_analysis.demo import generate


class ContractTests(unittest.TestCase):
    def test_reject_duplicate_and_reversed_timestamps(self):
        for times in ([0, 0], [1, 0], [float('nan')]):
            with self.subTest(times=times), self.assertRaises(ValueError):
                p.timestamps([{'best_effort_timestamp_time': t} for t in times])

    def test_incomplete_decode_rejected(self):
        with self.assertRaisesRegex(ValueError, 'count'):
            p.metrics(bytes([0, 1]), 1, [0, 1, 2])

    def test_metric_is_pixel_difference_not_motion(self):
        rows = p.metrics(bytes([0, 0, 255, 255]), 2, [5, 5.1])
        self.assertEqual(rows[1]['difference_mean'], 1)
        self.assertAlmostEqual(rows[1]['time_seconds'], .1)

    def test_estimates_cannot_be_labeled_measurements(self):
        note = {'id': 'camera', 'kind': 'measurement', 'start_frame': 0, 'end_frame': 1,
                'claim': 'Camera moves', 'evidence': 'frames', 'method': 'inference', 'uncertainty': 'unknown Z'}
        with self.assertRaises(ValueError): p.annotations_validate([note], 2)
        note['kind'] = 'hypothesis'
        p.annotations_validate([note], 2)
        note['end_frame'] = 2
        with self.assertRaises(ValueError): p.annotations_validate([note], 2)

    def test_trajectory_uses_vfr_timing(self):
        track = {'id': 'a', 'evidence': 'manual', 'uncertainty': 'one pixel',
                 'samples': [{'frame': 0, 'x': 0, 'y': 0}, {'frame': 1, 'x': .1, 'y': 0}, {'frame': 2, 'x': .5, 'y': 0}]}
        output = p.derive_tracks([track], [5, 5.1, 5.5])[0]
        self.assertEqual(output['kind'], 'estimate')
        self.assertAlmostEqual(output['segments'][0]['vx_per_second'], 1)
        self.assertAlmostEqual(output['segments'][1]['ax_per_second2'], 0)
        track['samples'][1]['frame'] = 0
        with self.assertRaises(ValueError): p.derive_tracks([track], [5, 5.1, 5.5])


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg integration requires installed tools')
class IntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        cls.source = generate(cls.root / 'fixture')
        cls.output = cls.root / 'analysis'
        cls.result = p.analyze(cls.source, cls.output, tracks=cls.source.parent / 'tracks.json')

    @classmethod
    def tearDownClass(cls): cls.temp.cleanup()

    def clone_output(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        folder = Path(temp.name) / 'output'
        shutil.copytree(self.output, folder)
        return folder

    def resign(self, folder):
        p.dump(folder / 'manifest.json', {file.relative_to(folder).as_posix(): p.digest(file)
                                         for file in folder.rglob('*') if file.is_file() and file.name != 'manifest.json'})

    def test_known_cut_hold_and_tracking(self):
        data = p.validate(self.output)
        self.assertNotIn(b'\r\n', (self.output / 'analysis.json').read_bytes())
        self.assertNotIn(b'\r\n', (self.output / 'report.md').read_bytes())
        self.assertEqual(len(data['frames']), 60)
        self.assertEqual([event['frame'] for event in data['cut_candidates']], [30])
        self.assertTrue(any('identical' in w for w in data['warnings']))
        self.assertEqual(data['frames'][30]['time_seconds'], 1)
        self.assertAlmostEqual(data['tracks'][0]['segments'][0]['vx_per_second'], .375, delta=.001)
        self.assertEqual(len(data['audio']), 1)

    def test_reproducible_analysis(self):
        output = self.root / 'repeat'
        other = p.analyze(self.source, output, tracks=self.source.parent / 'tracks.json')
        self.assertEqual(other, self.result)

    def test_missing_and_altered_frame_detected(self):
        for operation in ('delete', 'alter'):
            with self.subTest(operation=operation):
                folder = self.clone_output()
                frame = folder / 'frames/000002.png'
                if operation == 'delete': frame.unlink()
                else: frame.write_bytes(b'broken')
                with self.assertRaises(ValueError): p.validate(folder)

    def test_duplicate_record_and_wrong_pts_even_with_rehashed_manifest(self):
        for operation in ('duplicate', 'timestamp', 'classification'):
            with self.subTest(operation=operation):
                folder = self.clone_output()
                data = copy.deepcopy(self.result)
                if operation == 'duplicate': data['frames'][1] = data['frames'][0]
                elif operation == 'timestamp': data['frames'][1]['pts_seconds'] = .5
                else: data['cut_candidates'][0]['kind'] = 'measurement'
                p.dump(folder / 'analysis.json', data)
                self.resign(folder)
                with self.assertRaises(ValueError): p.validate(folder)

    def test_incomplete_report_detected(self):
        folder = self.clone_output()
        (folder / 'report.md').write_text('incomplete')
        self.resign(folder)
        with self.assertRaisesRegex(ValueError, 'Report'): p.validate(folder)

    def test_bad_inputs_and_resource_limits(self):
        bad = self.root / 'corrupt.mkv'
        bad.write_bytes(b'not a video')
        for source, kwargs in ((bad, {}), (self.source, {'max_frames': 5}), (self.source, {'max_seconds': .5}),
                               (self.source, {'max_bytes': 1})):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                p.analyze(source, self.root / 'never-published', **kwargs)
            self.assertFalse((self.root / 'never-published').exists())

    def test_existing_output_never_overwritten(self):
        with self.assertRaisesRegex(ValueError, 'exists'): p.analyze(self.source, self.output)

    def test_audio_start_offset_warning(self):
        delayed = self.root / 'delayed.mkv'
        p.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', self.source, '-itsoffset', '0.2', '-i', self.source,
               '-map', '0:v', '-map', '1:a', '-c', 'copy', delayed])
        result = p.analyze(delayed, self.root / 'delayed-analysis')
        self.assertAlmostEqual(result['audio'][0]['offset_from_video_seconds'], .2, places=2)
        self.assertTrue(any('50ms' in w for w in result['warnings']))

    def test_variable_frame_timing_preserved(self):
        vfr = self.root / 'vfr.mkv'
        p.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', self.source, '-an', '-vf',
               "select='not(eq(mod(n,3),1))'", '-fps_mode', 'vfr', '-c:v', 'ffv1', '-threads', '1', vfr])
        result = p.analyze(vfr, self.root / 'vfr-analysis')
        self.assertEqual(len(result['frames']), 40)
        self.assertAlmostEqual(result['frames'][1]['time_seconds'], .067, places=3)
        self.assertTrue(any('Variable' in w for w in result['warnings']))

    def test_fractional_fps_b_frames_and_nonzero_origin(self):
        source = self.root / 'b-frames.mp4'
        # Native encoder available in local and Ubuntu FFmpeg builds.
        p.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', self.source, '-an',
               '-vf', 'setpts=PTS+5/TB', '-c:v', 'mpeg4', '-bf', '2', '-threads', '1',
               '-fps_mode', 'passthrough', source])
        data = p.analyze(source, self.root / 'b-frames-analysis')
        self.assertEqual(len(data['frames']), 60)
        self.assertAlmostEqual(data['frames'][0]['pts_seconds'], 5)
        self.assertEqual(data['frames'][0]['time_seconds'], 0)
        fractional = self.root / 'fractional.mkv'
        p.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', self.source, '-an',
               '-vf', 'setpts=N/(30000/1001)/TB', '-r', '30000/1001', '-c:v', 'ffv1', '-threads', '1', fractional])
        result = p.analyze(fractional, self.root / 'fractional-analysis')
        self.assertEqual(result['video']['avg_frame_rate'], '30000/1001')
        self.assertEqual(len(result['frames']), 60)
        self.assertAlmostEqual(result['frames'][59]['time_seconds'], 59*1001/30000, delta=.002)

    def test_mid_decode_failure_never_publishes_partial_output(self):
        real_run = p.run
        def broken(args, timeout=120):
            if str(args[-1]).endswith('%06d.png'):
                raise ValueError('Injected PNG decoder failure')
            return real_run(args, timeout)
        output = self.root / 'partial-output'
        with patch.object(p, 'run', broken), self.assertRaisesRegex(ValueError, 'Injected'):
            p.analyze(self.source, output)
        self.assertFalse(output.exists())

    def test_engine_registration_and_failure_preserve_gates(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            folder = root / 'evidence'
            shutil.copytree(self.output, folder)
            with patch.object(engine, 'ROOT', root), patch.object(engine, 'BASE', root / 'learning'):
                case = p.register(folder, 'reference-test')
                self.assertFalse(case['human_approved'])
                engine.load_case(case['id'])
                with self.assertRaises(ValueError): p.register(folder, case['id'])
                diagnostic = root / 'failure.json'
                p.dump(diagnostic, {'check_id': 'camera-solve', 'evidence': 'Synthetic fixture cannot test orbit depth',
                                    'cause_category': 'evaluation-process', 'hypothesis': 'Fixture lacks perspective',
                                    'problem': 'Do not validate 3D with a 2D fixture', 'implementation': 'Use controlled 3D clip',
                                    'use_when': 'Testing camera hypotheses', 'avoid_when': 'Only testing timestamps',
                                    'acceptance_test': 'Retain ground truth and compare projected tracked points'})
                failed = p.record_failure('reference-failure', 'account-1', diagnostic)
                self.assertFalse(failed['human_approved'])
                proposal = engine.read_json(engine.proposal_file('reference-failure--camera-solve'))
                engine.validate_proposal(proposal)
                self.assertEqual(proposal['state'], 'proposed')
                with self.assertRaisesRegex(ValueError, 'Creative approval'):
                    verified = {**case, 'id': 'reference-new-test', 'validates_proposal': proposal['id'],
                                'checks': [{'id': 'camera-solve', 'status': 'pass', 'evidence': 'test only'}]}
                    engine.write_json(engine.case_file(verified['id']), verified)
                    engine.promote(proposal['id'], verified['id'])


if __name__ == '__main__': unittest.main()
