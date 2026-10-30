#!/usr/bin/env python3
import json
import random
from pathlib import Path

def get_random_hook(matrix_path, category=None):
    with open(matrix_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    cat = category if category in data else random.choice(list(data.keys()))
    hook = random.choice(data[cat])
    return cat, hook

if __name__ == "__main__":
    p = Path(__file__).resolve().parent.parent / "templates" / "hook_matrix_ar.json"
    cat, h = get_random_hook(str(p))
    print(f"[{cat}] -> {h}")
