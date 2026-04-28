import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from doctrine import Doctrine


def build_expected():
    nodes = []
    for path in sorted((ROOT / "nodes").glob("*.md")):
        doctrine = Doctrine.load(path)
        errors = doctrine.validate()
        nodes.append({
            "name": doctrine.name,
            "id": doctrine.id,
            "path": str(path.relative_to(ROOT)),
            "definition": doctrine.definition,
            "valid": not bool(errors),
            "errors": errors,
        })
    return {"nodes": nodes}


def main():
    registry_path = ROOT / "registry" / "index.json"
    current = json.loads(registry_path.read_text(encoding="utf-8"))
    expected = build_expected()
    if current != expected:
        print("registry/index.json is stale; run python tools/build_registry.py")
        print("expected:")
        print(json.dumps(expected, indent=2))
        return 1
    print("registry/index.json is current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
