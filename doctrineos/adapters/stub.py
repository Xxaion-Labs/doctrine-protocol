from pathlib import Path
from typing import Dict


class StubAdapter:
    def inspect_workspace(self, workspace: Path) -> Dict[str, object]:
        workspace = Path(workspace)
        if not workspace.exists():
            return {"status": "missing", "path": str(workspace), "entries": []}

        entries = []
        for item in sorted(workspace.iterdir(), key=lambda p: p.name)[:25]:
            entries.append({"name": item.name, "type": "dir" if item.is_dir() else "file"})
        return {"status": "ok", "path": str(workspace), "entries": entries}

    def echo(self, message: str) -> Dict[str, object]:
        return {"status": "ok", "message": message}
