#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import inspect
import json
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
TEST_PATH = ROOT / "tests" / "test_filetype.py"


def load_module(path: Path):
    sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location("doctrineos_filetype_tests", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module(TEST_PATH)
    tests = [
        (name, fn)
        for name, fn in inspect.getmembers(module, inspect.isfunction)
        if name.startswith("test_")
    ]
    results: List[Dict[str, Any]] = []
    for name, fn in tests:
        try:
            fn()
            results.append({"name": name, "ok": True})
        except Exception as exc:
            results.append({"name": name, "ok": False, "error": repr(exc), "traceback": traceback.format_exc()})
    receipt = {
        "tool": "scripts/run_filetype_tests.py",
        "test_file": str(TEST_PATH.relative_to(ROOT)),
        "test_count": len(results),
        "passed_count": sum(1 for r in results if r["ok"]),
        "failed_count": sum(1 for r in results if not r["ok"]),
        "ok": all(r["ok"] for r in results),
        "results": results,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
