#!/usr/bin/env python3
"""Public DoctrineOS L1 index compiler.

Purpose:
- Generate public-safe `.doctrine` companion envelopes for repository files.
- Preserve source path, SHA-256, size, and projection boundary.
- Keep source files in place.
- Avoid embedding raw source body by default; L1 proves integrity, not semantic extraction.
- Emit manifest and doctor receipts under public-evidence/.

This compiler carries the public Doctrine Protocol shape without implementation-specific payloads.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / ".doctrine-index"
EVIDENCE_ROOT = ROOT / "public-evidence"
MANIFEST_PATH = OUT_ROOT / "MANIFEST.json"
CERT_SENTINEL = "PUBLIC_DOCTRINE_L1_CERTIFICATE_JSON"

SKIP_DIRS = {
    ".git",
    ".pytest_cache",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "node_modules",
    ".doctrine-index",
    ".doctrineos",
}

SENTINEL_NAMES = [
    "PUBLIC_DOCTRINE_L1_MANIFEST_JSON",
    "PUBLIC_DOCTRINE_L1_SOURCE_JSON",
    "PUBLIC_DOCTRINE_L1_BOUNDARY_JSON",
    "PUBLIC_DOCTRINE_L1_DOCTOR_JSON",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("\\", "/")


def slug(path_rel: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", path_rel.replace("/", "__"))


def block(name: str, payload: Dict[str, Any]) -> str:
    return f"<<<{name}>>>\n" + json.dumps(payload, indent=2, sort_keys=True) + f"\n<<<END_{name}>>>\n"


def iter_files(include_hidden: bool = False) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(ROOT):
        current = Path(dirpath)
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS and (include_hidden or not d.startswith("."))
        ]
        for filename in filenames:
            if not include_hidden and filename.startswith("."):
                continue
            path = current / filename
            if path == Path(__file__).resolve():
                continue
            if ".git" in path.parts:
                continue
            yield path


def companion_path(source: Path) -> Path:
    return OUT_ROOT / f"{slug(rel(source))}.doctrine"


def render(source: Path) -> Tuple[str, Dict[str, Any]]:
    data = source.read_bytes()
    source_rel = rel(source)
    out_rel = rel(companion_path(source))
    source_sha = sha256_bytes(data)
    now = utc_now()
    record_id = f"public_doctrine_l1_{source_sha[:16]}"

    front = "\n".join([
        "DOCTRINE FILE",
        "version: 1.0.0",
        f"body_id: {record_id}",
        "schema_version: public_doctrine_l1_index_v1",
        "record_type: public_repo_file_companion",
        f"source_path: {source_rel}",
        f"source_sha256: {source_sha}",
        "projection_class: public_safe_index",
        "validation_state: generated_unverified",
        "",
        f"# Public Doctrine L1 Companion — `{source_rel}`",
        "",
        "## Definition",
        "Public-safe L1 `.doctrine` companion envelope for a DoctrineOS repository file.",
        "",
        "## Usage",
        "Use this companion to verify source path, SHA-256, size, projection boundary, and filetype envelope integrity without exposing implementation-specific payloads.",
        "",
        "## ID",
        record_id,
        "",
        "## Claims supported",
        "",
        "```text",
        "source path recorded",
        "source SHA-256 recorded",
        "source file preserved in place",
        "public-safe L1 companion envelope generated",
        "```",
        "",
        "## Claims not supported",
        "",
        "```text",
        "semantic extraction complete",
        "implementation-specific payload present",
        "public release beyond repository contents approved",
        "```",
        "",
    ]) + "\n"

    payloads = {
        "PUBLIC_DOCTRINE_L1_MANIFEST_JSON": {
            "status": "ACTIVE",
            "schema_version": "public_doctrine_l1_index_v1",
            "record_id": record_id,
            "compiled_at_utc": now,
            "source_path": source_rel,
            "companion_path": out_rel,
        },
        "PUBLIC_DOCTRINE_L1_SOURCE_JSON": {
            "status": "ACTIVE",
            "source_path": source_rel,
            "source_sha256": source_sha,
            "source_size_bytes": len(data),
            "source_embedded": False,
        },
        "PUBLIC_DOCTRINE_L1_BOUNDARY_JSON": {
            "status": "ACTIVE",
            "projection_class": "public_safe_index",
            "extension_payload_included": False,
            "semantic_embedding_deferred": True,
        },
        "PUBLIC_DOCTRINE_L1_DOCTOR_JSON": {
            "status": "ACTIVE",
            "required_sentinels": SENTINEL_NAMES,
            "required_certificate": CERT_SENTINEL,
        },
    }

    sentinel_text = ""
    for name in SENTINEL_NAMES:
        sentinel_text += block(name, payloads[name]) + "\n"

    pre_cert = front + sentinel_text
    cert = {
        "status": "ACTIVE",
        "certificate_policy": "payload_sha256_excluding_this_certificate",
        "payload_sha256_excluding_this_certificate": sha256_text(pre_cert),
        "source_path": source_rel,
        "source_sha256": source_sha,
        "companion_path": out_rel,
        "compiled_at_utc": now,
    }
    final = pre_cert + block(CERT_SENTINEL, cert)
    record = {
        "source_path": source_rel,
        "source_sha256": source_sha,
        "source_size_bytes": len(data),
        "companion_path": out_rel,
        "companion_sha256": sha256_text(final),
        "projection_class": "public_safe_index",
    }
    return final, record


def compile_repo(apply: bool, include_hidden: bool = False) -> Dict[str, Any]:
    files = sorted(iter_files(include_hidden=include_hidden), key=lambda p: rel(p))
    records: List[Dict[str, Any]] = []
    errors: List[Dict[str, str]] = []
    changed = 0
    for source in files:
        try:
            text, record = render(source)
            out = companion_path(source)
            if not out.exists() or out.read_text(encoding="utf-8") != text:
                changed += 1
            if apply:
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(text, encoding="utf-8")
            records.append(record)
        except Exception as exc:
            errors.append({"source_path": rel(source), "error": str(exc)})

    manifest = {
        "schema_version": "public_doctrine_l1_manifest_v1",
        "updated_at_utc": utc_now(),
        "record_count": len(records),
        "error_count": len(errors),
        "ok": not errors,
        "records": records,
        "errors": errors,
    }
    manifest["manifest_sha256_excluding_self"] = sha256_text(json.dumps({k: v for k, v in manifest.items() if k != "manifest_sha256_excluding_self"}, sort_keys=True))
    if apply:
        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "ok": not errors,
        "source_file_count": len(files),
        "compiled_record_count": len(records),
        "changed_count": changed,
        "manifest_path": rel(MANIFEST_PATH),
        "errors": errors,
    }


def parse_blocks(text: str) -> Dict[str, str]:
    pattern = re.compile(r"<<<([A-Z0-9_]+)>>>(.*?)<<<END_\1>>>", re.DOTALL)
    return {name: body.strip() for name, body in pattern.findall(text)}


def doctor_file(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    json_ok = True
    errors: List[str] = []
    parsed: Dict[str, Any] = {}
    for name, body in blocks.items():
        try:
            parsed[name] = json.loads(body)
        except Exception as exc:
            json_ok = False
            errors.append(f"{name}: {exc}")
    missing = [name for name in SENTINEL_NAMES + [CERT_SENTINEL] if name not in parsed]
    cert_ok = False
    if CERT_SENTINEL in parsed:
        cert_start = text.index(f"<<<{CERT_SENTINEL}>>>")
        actual = sha256_text(text[:cert_start])
        expected = parsed[CERT_SENTINEL].get("payload_sha256_excluding_this_certificate")
        cert_ok = actual == expected
        if not cert_ok:
            errors.append("certificate hash mismatch")
    ok = json_ok and not missing and cert_ok
    return {
        "path": rel(path),
        "ok": ok,
        "json_ok": json_ok,
        "missing": missing,
        "certificate_hash_matches": cert_ok,
        "errors": errors,
        "sha256": sha256_bytes(path.read_bytes()),
    }


def doctor_all() -> Dict[str, Any]:
    companions = sorted(OUT_ROOT.glob("*.doctrine"))
    results = [doctor_file(path) for path in companions]
    failures = [r for r in results if not r["ok"]]
    receipt = {
        "receipt_id": "PUBLIC_DOCTRINE_L1_DOCTOR",
        "created_at_utc": utc_now(),
        "ok": not failures,
        "compiled_count": len(companions),
        "ok_count": len(results) - len(failures),
        "failure_count": len(failures),
        "failures": failures,
        "results": results,
    }
    receipt["receipt_sha256"] = sha256_text(json.dumps(receipt, sort_keys=True))
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description="Public DoctrineOS L1 index compiler/doctor.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("compile")
    c.add_argument("--apply", action="store_true")
    c.add_argument("--include-hidden", action="store_true")
    d = sub.add_parser("doctor")
    d.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if args.cmd == "compile":
        out = compile_repo(apply=args.apply, include_hidden=args.include_hidden)
    else:
        out = doctor_all()
        if args.write:
            EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
            (EVIDENCE_ROOT / "PUBLIC_DOCTRINE_L1_DOCTOR.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if out.get("ok") else 2


if __name__ == "__main__":
    raise SystemExit(main())
