from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Union

from .parser import DoctrineParser
from .validator import DoctrineValidator
from .mount import MountReceipt


@dataclass
class Doctrine:
    name: str
    definition: Optional[str] = None
    id: Optional[str] = None
    usage: Optional[str] = None
    example: Optional[str] = None
    metadata: Dict[str, str] = field(default_factory=dict)
    sections: Dict[str, str] = field(default_factory=dict)
    source: Optional[str] = None
    filetype_diagnostics: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Union[str, Path]) -> "Doctrine":
        path = Path(path)
        if not path.exists() and path.suffix == "":
            candidate = path.with_suffix(".doctrine")
            if candidate.exists():
                path = candidate
        return cls.from_text(path.read_text(encoding="utf-8-sig"), source=str(path))

    @classmethod
    def from_text(cls, text: str, source: Optional[str] = None) -> "Doctrine":
        parsed = DoctrineParser.parse(text, source=source)
        return cls(**parsed)

    @classmethod
    def compose(cls, doctrines: Iterable["Doctrine"], name: str = "composed") -> "Doctrine":
        items = list(doctrines)
        sections: Dict[str, str] = {}
        metadata: Dict[str, str] = {"composed": "true", "count": str(len(items))}
        definitions: List[str] = []
        usages: List[str] = []
        examples: List[str] = []
        ids: List[str] = []

        for item in items:
            prefix = item.name
            if item.definition:
                definitions.append(f"{prefix}: {item.definition}")
            if item.usage:
                usages.append(f"{prefix}: {item.usage}")
            if item.example:
                examples.append(f"# {prefix}\n{item.example}")
            if item.id:
                ids.append(str(item.id))
            for key, value in item.sections.items():
                sections[f"{prefix}.{key}"] = value

        return cls(
            name=name,
            definition="\n".join(definitions) or None,
            id=" + ".join(ids) if ids else name,
            usage="\n".join(usages) or None,
            example="\n\n".join(examples) or None,
            metadata=metadata,
            sections=sections,
            source="compose",
            filetype_diagnostics={"composed": True, "count": len(items)},
        )

    def validate(self) -> List[str]:
        return DoctrineValidator.validate(self)

    def mount(self, strict: bool = True) -> Dict[str, Any]:
        errors = self.validate()
        sentinel_errors = list((self.filetype_diagnostics or {}).get("sentinel_errors", []))
        if sentinel_errors:
            errors.extend(["sentinel error: " + str(item) for item in sentinel_errors])
        if strict and errors:
            raise ValueError("Doctrine validation failed: " + "; ".join(errors))
        receipt = MountReceipt.from_doctrine(self, errors=errors)
        return receipt.to_dict()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "definition": self.definition,
            "id": self.id,
            "usage": self.usage,
            "example": self.example,
            "metadata": dict(self.metadata),
            "sections": dict(self.sections),
            "source": self.source,
            "filetype_diagnostics": dict(self.filetype_diagnostics or {}),
        }

    def to_prompt_context(self) -> str:
        lines = [f"# Doctrine: {self.name}"]
        if self.definition:
            lines += ["", "## Definition", self.definition]
        if self.usage:
            lines += ["", "## Usage", self.usage]
        for key, value in self.sections.items():
            lines += ["", f"## {key}", value]
        return "\n".join(lines).strip() + "\n"
