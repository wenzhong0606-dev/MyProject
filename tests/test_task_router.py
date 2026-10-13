import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from task_router import load, resolve

class TaskRouterTests(unittest.TestCase):
    def test_every_route_resolves(self):
        routes, _, _ = load()
        for task in routes:
            with self.subTest(task=task):
                result = resolve(task)
                self.assertTrue(result["stage_readmes"])
                for path in result["stage_readmes"] + result["candidate_artifacts"]:
                    self.assertTrue((ROOT / path).is_file(), path)
    def test_unknown_task_rejected(self):
        with self.assertRaises(ValueError):
            resolve("something-unknown")
    def test_ui_routing_contains_prototype(self):
        self.assertTrue(any("interaction-spec" in f for f in resolve("ui")["candidate_artifacts"]))

if __name__ == "__main__":
    unittest.main()
