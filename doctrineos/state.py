import json
from pathlib import Path
from typing import Any, Dict, List


class StateStore:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.data: Dict[str, Any] = {"actions": []}
        if self.path.exists():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))

    def record_action(self, receipt_path: str, command: str, allowed: bool) -> None:
        actions: List[Dict[str, Any]] = self.data.setdefault("actions", [])
        actions.append({
            "receipt_path": receipt_path,
            "command": command,
            "allowed": allowed,
        })
        self.save()

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")

    def snapshot(self) -> Dict[str, Any]:
        return dict(self.data)
