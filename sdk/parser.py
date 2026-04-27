from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional
import hashlib
import re


class DoctrineParser:
    """Parser for the public .doctrine/node format."""

    @staticmethod
    def parse(text: str, source: Optional[str] = None) -> Dict[str, object]:
        clean = text.lstrip("\ufeff")
        metadata = DoctrineParser.parse_metadata(clean)
        sections = DoctrineParser.parse_sections(clean)
        name = DoctrineParser.parse_name(clean, source=source, metadata=metadata)

        definition = sections.get("Definition")
        usage = sections.get("Usage")
        example = sections.get("Example")
        doctrine_id = sections.get("ID") or metadata.get("body_id") or DoctrineParser.short_hash(clean)

        return {
            "name": name,
            "definition": definition,
            "id": doctrine_id,
            "usage": usage,
            "example": example,
            "metadata": metadata,
            "sections": sections,
            "source": source,
        }

    @staticmethod
    def parse_metadata(text: str) -> Dict[str, str]:
        metadata: Dict[str, str] = {}
        for raw in text.splitlines()[:40]:
            line = raw.strip()
            if not line or line.startswith("#") or line == "---":
                continue
            if line.startswith("## "):
                break
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if not value:
                continue
            if re.match(r"^[A-Za-z_][A-Za-z0-9_-]*$", key):
                metadata[key] = value
        return metadata

    @staticmethod
    def parse_sections(text: str) -> Dict[str, str]:
        matches = list(re.finditer(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
        sections: Dict[str, str] = {}
        for index, match in enumerate(matches):
            title = match.group(1).strip()
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            body = text[start:end].strip()
            sections[title] = body
        return sections

    @staticmethod
    def parse_name(text: str, source: Optional[str], metadata: Dict[str, str]) -> str:
        node_match = re.search(r"^#\s*Node:\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if node_match:
            return node_match.group(1).strip()

        title_match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            if title:
                return title

        if metadata.get("body_id"):
            return metadata["body_id"]

        if source:
            return Path(source).stem

        return "doctrine"

    @staticmethod
    def short_hash(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
