import sys
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from init_project import create_project, validate_name

@unittest.skipIf(os.environ.get('INIT_PROJECT_CHILD_VALIDATION') == '1',\n                 '生成项目内部校验时跳过脚手架递归测试')\nclass InitProjectTests(unittest.TestCase):
    def test_invalid_name(self):
        for name in ("../bad", "有空格", "", "1bad"):
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    validate_name(name)

    def test_creates_project_and_validates(self):
        with tempfile.TemporaryDirectory() as td:
            dest = Path(td) / "example"
            outcome = create_project(name="example", target=dest, product="设备资产管理",
                                     stack="Java 21", repo_url="https://github.com/example/example",
                                     branch="main")
            self.assertEqual(outcome["validation"], "passed")
            self.assertIn("设备资产管理", (dest / "README.md").read_text(encoding="utf-8"))
            self.assertIn("Java 21", (dest / "docs/governance/project-profile.md").read_text(encoding="utf-8"))
            self.assertIn("当前仓库为独立业务项目", (dest / "AGENTS.md").read_text(encoding="utf-8"))
            self.assertTrue((dest / "docs/deliverables/manifest.json").is_file())
            with self.assertRaises(FileExistsError):
                create_project(name="example", target=dest, product="设备资产管理",
                               stack="", repo_url="", branch="main")

    def test_dry_run_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as td:
            dest = Path(td) / "not-created"
            outcome = create_project(name="preview", target=dest, product="ERP", stack="",
                                     repo_url="", branch="main", dry_run=True)
            self.assertEqual(outcome["mode"], "dry-run")
            self.assertFalse(dest.exists())

    def test_reject_source_nested_target(self):
        with self.assertRaises(ValueError):
            create_project(name="bad-target", target=ROOT / "generated", product="EAM",
                           stack="", repo_url="", branch="main", dry_run=True)

if __name__ == "__main__":
    unittest.main()
