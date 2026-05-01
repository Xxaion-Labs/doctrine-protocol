from __future__ import annotations

from dataclasses import dataclass
import json
import re
from typing import Any, Dict, List, Optional


START_RE = re.compile(r"^<<<([A-Z0-9_]+_JSON)>>>\s*$")


@dataclass
class SentinelBlock:
    name: str
    start_line: int
    end_line: int
    raw_json: str
    json_ok: bool
    payload: Any = None
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "json_ok": self.json_ok,
            "payload": self.payload,
            "error": self.error,
        }


class DoctrineFiletypeParser:
    """Public `.doctrine` filetype parser.

    Capped public subset:
    - UTF-8 text handled by callers.
    - Markdown remains readable.
    - JSON sentinel blocks are parsed when present.
    - Malformed sentinels are reported instead of silently ignored.
    - No private Xxen sentinel requirements are imposed.
    """

    @staticmethod
    def parse_sentinels(text: str) -> Dict[str, object]:
        lines = text.lstrip("\ufeff").splitlines()
        blocks: List[SentinelBlock] = []
        errors: List[Dict[str, object]] = []
        i = 0
        while i < len(lines):
            match = START_RE.match(lines[i])
            if not match:
                i += 1
                continue
            name = match.group(1)
            start_line = i + 1
            end_marker = f"<<<END_{name}>>>"
            body_lines: List[str] = []
            j = i + 1
            found_end = False
            while j < len(lines):
                if lines[j].strip() == end_marker:
                    found_end = True
                    break
                body_lines.append(lines[j])
                j += 1
            if not found_end:
                error = {"sentinel": name, "line": start_line, "error": "missing_end_marker"}
                errors.append(error)
                blocks.append(SentinelBlock(name, start_line, len(lines), "\n".join(body_lines), False, None, "missing_end_marker"))
                break
            raw = "\n".join(body_lines).strip()
            try:
                payload = json.loads(raw)
                blocks.append(SentinelBlock(name, start_line, j + 1, raw, True, payload, None))
            except Exception as exc:
                detail = str(exc)
                errors.append({"sentinel": name, "line": start_line, "error": "json_parse_failed", "detail": detail})
                blocks.append(SentinelBlock(name, start_line, j + 1, raw, False, None, detail))
            i = j + 1
        return {
            "sentinels": [block.to_dict() for block in blocks],
            "sentinel_count": len(blocks),
            "errors": errors,
            "ok": not errors,
        }

    @staticmethod
    def diagnostics(text: str) -> Dict[str, object]:
        parsed = DoctrineFiletypeParser.parse_sentinels(text)
        return {
            "filetype": ".doctrine",
            "utf8_text_supplied": isinstance(text, str),
            "sentinel_count": parsed["sentinel_count"],
            "sentinel_errors": parsed["errors"],
            "sentinel_json_ok": parsed["ok"],
            "sentinels": parsed["sentinels"],
        }
