"""
Unit tests for hook randomizer
"""
import unittest
import tempfile
import json
from pathlib import Path
from scripts.hook_randomizer import get_random_hook

class TestHookRandomizer(unittest.TestCase):
    def test_random_hook(self):
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json", encoding="utf-8") as f:
            json.dump({"problem_hook": ["Why do ads fail?"]}, f)
            fname = f.name
        try:
            cat, h = get_random_hook(fname, "problem_hook")
            self.assertEqual(cat, "problem_hook")
            self.assertEqual(h, "Why do ads fail?")
        finally:
            Path(fname).unlink(missing_ok=True)

if __name__ == "__main__":
    unittest.main()
