import json
import tempfile
import unittest
from pathlib import Path
from skillpack import manager as m


class SkillPackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.checkout = self.root / 'checkout'
        self.src = self.checkout / 'skills' / 'example'
        self.src.mkdir(parents=True)
        (self.src / 'SKILL.md').write_text('---\nname: example\ndescription: Test skill\n---\nText\n')
        (self.src / 'runner.py').write_text('print("never auto execute")\n')
        self.source = {'id':'example','repo':'owner/repo','commit':'a'*40,'license':'MIT','note':'Test',
                       'skills':[{'name':'example','path':'skills/example','profiles':['phase2','all']}]}
        self.skill = self.source['skills'][0]

    def test_real_catalog_has_unique_skills(self):
        cat = m.load_catalog()
        self.assertGreaterEqual(len(cat['sources']), 6)
        self.assertGreaterEqual(len(m.select(cat, 'phase2')), 10)
        self.assertGreaterEqual(len(m.select(cat, 'all')), len(m.select(cat, 'phase2')))

    def test_unsafe_path_rejected(self):
        bad = {'schema_version':1,'sources':[dict(self.source)]}
        bad['sources'][0]['skills'] = [dict(self.skill, path='../DIRECCION.md')]
        with self.assertRaises(ValueError): m.validate_catalog(bad)

    def test_duplicate_name_rejected(self):
        bad = {'schema_version':1,'sources':[dict(self.source)]}
        bad['sources'][0]['skills'] = [self.skill, dict(self.skill)]
        with self.assertRaises(ValueError): m.validate_catalog(bad)

    def test_install_and_verify(self):
        status, n = m.write_skill(self.source, self.skill, self.checkout, 'codex', project=self.root)
        self.assertEqual(status, 'installed')
        self.assertGreater(n, 0)
        self.assertEqual(m.inspect_installed(self.skill, 'codex', self.root), 'installed')
        self.assertIn('never auto execute', (self.root / '.agents/skills/example/runner.py').read_text())
        self.assertEqual(m.write_skill(self.source,self.skill,self.checkout,'codex',project=self.root)[0],
                         'already-present')

    def test_no_overwrite_unmanaged(self):
        dest = self.root / '.agents/skills/example'
        dest.mkdir(parents=True)
        (dest / 'SKILL.md').write_text('local original')
        with self.assertRaisesRegex(ValueError, 'Unmanaged'):
            m.write_skill(self.source, self.skill, self.checkout, 'codex',
                          project=self.root, force=True)
        self.assertEqual((dest / 'SKILL.md').read_text(), 'local original')

    def test_detect_modified_file_and_restore_with_force(self):
        m.write_skill(self.source, self.skill, self.checkout, 'claude', project=self.root)
        dest = self.root / '.claude/skills/example/SKILL.md'
        dest.write_text('tampered')
        self.assertEqual(m.inspect_installed(self.skill, 'claude', self.root), 'modified')
        m.write_skill(self.source,self.skill,self.checkout,'claude',project=self.root,force=True)
        self.assertEqual(m.inspect_installed(self.skill, 'claude', self.root), 'installed')

    def test_symlink_denied(self):
        (self.src / 'outside').symlink_to(self.root)
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            m.write_skill(self.source,self.skill,self.checkout,'codex',project=self.root)
        self.assertFalse((self.root / '.agents/skills/example').exists())

    def test_installer_does_not_execute_scripts(self):
        (self.src / 'runner.py').write_text('raise RuntimeError("must never run")')
        m.write_skill(self.source,self.skill,self.checkout,'codex',project=self.root)
        self.assertTrue((self.root / '.agents/skills/example/runner.py').exists())

    def test_source_collision_rejected_even_with_force(self):
        m.write_skill(self.source,self.skill,self.checkout,'codex',project=self.root)
        meta = self.root / '.agents/skills/example/_beatgaler-source.json'
        content = json.loads(meta.read_text())
        content['repo'] = 'other/repo'
        meta.write_text(json.dumps(content))
        with self.assertRaisesRegex(ValueError, 'Source conflict'):
            m.write_skill(self.source,self.skill,self.checkout,'codex',project=self.root,force=True)


if __name__ == '__main__':
    unittest.main()
