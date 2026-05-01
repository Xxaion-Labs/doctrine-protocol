import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from .doctrine import Doctrine


STATUS_PASS = "PASS"
STATUS_FAIL = "FAIL"
STATUS_WARN = "WARN"
STATUS_BLOCKED = "BLOCKED"


def status_word(ok: bool) -> str:
    return STATUS_PASS if ok else STATUS_FAIL


def collect_validation(doctrine: Doctrine) -> Dict[str, Any]:
    diagnostics = doctrine.filetype_diagnostics or {}
    validation_errors = doctrine.validate()
    sentinel_errors = list(diagnostics.get("sentinel_errors", []))
    all_errors: List[Any] = list(validation_errors) + sentinel_errors
    ok = not validation_errors and not sentinel_errors
    return {
        "ok": ok,
        "validation_errors": validation_errors,
        "sentinel_errors": sentinel_errors,
        "all_errors": all_errors,
        "filetype_diagnostics": diagnostics,
    }


def doctor_payload(path: str, doctrine: Doctrine) -> Dict[str, Any]:
    validation = collect_validation(doctrine)
    return {
        "ok": validation["ok"],
        "path": path,
        "name": doctrine.name,
        "id": doctrine.id,
        "validation_errors": validation["validation_errors"],
        "filetype_diagnostics": validation["filetype_diagnostics"],
    }


def markdown_report(path: str, doctrine: Doctrine, mode: str) -> str:
    validation = collect_validation(doctrine)
    diagnostics = validation["filetype_diagnostics"]
    sentinels = diagnostics.get("sentinels", []) or []
    sentinel_errors = validation["sentinel_errors"]
    validation_errors = validation["validation_errors"]
    ok = bool(validation["ok"])

    lines = [
        f"# DoctrineOS {mode.title()} Report — `{path}`",
        "",
        "## Summary",
        "",
        f"- overall: **{status_word(ok)}**",
        f"- filetype: `{diagnostics.get('filetype', '.doctrine')}`",
        f"- name: `{doctrine.name}`",
        f"- id: `{doctrine.id}`",
        f"- sentinel_count: `{diagnostics.get('sentinel_count', 0)}`",
        f"- sentinel_json: **{status_word(bool(diagnostics.get('sentinel_json_ok', True)))}**",
        "",
        "## Checks",
        "",
        f"- {status_word(not validation_errors)} `doctrine_validation`",
        f"- {status_word(not sentinel_errors)} `sentinel_diagnostics`",
        f"- {status_word(bool(diagnostics.get('utf8_text_supplied', True)))} `utf8_text_supplied`",
        f"- {STATUS_WARN} `implementation_specific_extensions_not_enforced_public_subset`",
        "",
        "## Sentinels",
        "",
    ]

    if sentinels:
        for sentinel in sentinels:
            name = sentinel.get("name", "UNKNOWN_JSON")
            json_ok = bool(sentinel.get("json_ok"))
            lines.append(f"- {status_word(json_ok)} `{name}` lines `{sentinel.get('start_line')}-{sentinel.get('end_line')}`")
    else:
        lines.append(f"- {STATUS_WARN} no JSON sentinels found")

    lines += ["", "## Errors", ""]
    if validation_errors:
        for item in validation_errors:
            lines.append(f"- {STATUS_FAIL} validation: `{item}`")
    if sentinel_errors:
        for item in sentinel_errors:
            lines.append(f"- {STATUS_FAIL} sentinel: `{item}`")
    if not validation_errors and not sentinel_errors:
        lines.append("- none")

    lines += [
        "",
        "## Proof boundaries",
        "",
        "### What this proves",
        "",
        "- DoctrineOS parsed the file as UTF-8 text.",
        "- Markdown sections and metadata were inspected.",
        "- JSON sentinel diagnostics were evaluated.",
        "- Public mount/inspect compatibility was checked inside the documented public subset.",
        "",
        "### What this does not prove",
        "",
        "- It does not enforce implementation-specific extension requirements.",
        "- It does not prove external runtime payload validity.",
        "- It does not prove completeness of any downstream application layer.",
        "- It does not approve non-public material for public release.",
        "",
        "## Next safe actions",
        "",
    ]
    if ok:
        lines.append("- Continue with public-safe mount, inspect, or Workbench projection.")
    else:
        lines.append("- Repair the listed FAIL diagnostics before using this file as a valid public fixture.")
    return "\n".join(lines) + "\n"


def emit_report(payload: Dict[str, Any], markdown: str, fmt: str) -> None:
    if fmt == "markdown":
        print(markdown, end="")
    else:
        print(json.dumps(payload, indent=2))


def cmd_validate(args):
    doctrine = Doctrine.load(args.path)
    validation = collect_validation(doctrine)
    diagnostics = validation["filetype_diagnostics"]
    all_errors = list(validation["validation_errors"]) + ["sentinel error: " + str(item) for item in validation["sentinel_errors"]]
    if all_errors:
        print(json.dumps({"valid": False, "errors": all_errors, "filetype_diagnostics": diagnostics}, indent=2))
        return 1
    print(json.dumps({"valid": True, "path": args.path, "name": doctrine.name, "id": doctrine.id, "filetype_diagnostics": diagnostics}, indent=2))
    return 0


def cmd_mount(args):
    doctrine = Doctrine.load(args.path)
    mounted = doctrine.mount(strict=not args.no_strict)
    print(json.dumps(mounted, indent=2))
    return 0


def cmd_inspect(args):
    doctrine = Doctrine.load(args.path)
    payload = doctrine.to_dict()
    validation = collect_validation(doctrine)
    payload["inspect_status"] = {
        "ok": validation["ok"],
        "status": status_word(validation["ok"]),
        "validation_errors": validation["validation_errors"],
        "sentinel_errors": validation["sentinel_errors"],
    }
    emit_report(payload, markdown_report(args.path, doctrine, "inspect"), args.format)
    return 0 if validation["ok"] else 1


def cmd_doctor(args):
    doctrine = Doctrine.load(args.path)
    payload = doctor_payload(args.path, doctrine)
    emit_report(payload, markdown_report(args.path, doctrine, "doctor"), args.format)
    return 0 if payload["ok"] else 1


def cmd_registry_build(args):
    nodes_dir = Path(args.nodes_dir)
    items = []
    for path in sorted(nodes_dir.glob("*.md")):
        doctrine = Doctrine.load(path)
        errors = doctrine.validate()
        items.append({
            "name": doctrine.name,
            "id": doctrine.id,
            "path": str(path),
            "definition": doctrine.definition,
            "valid": not bool(errors),
            "errors": errors,
        })
    output = {"nodes": items}
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps({"written": str(out_path), "count": len(items)}, indent=2))
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="doctrine", description="Doctrine Protocol CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate a doctrine file")
    validate.add_argument("path")
    validate.set_defaults(func=cmd_validate)

    mount = sub.add_parser("mount", help="Mount a doctrine file and print a mount receipt")
    mount.add_argument("path")
    mount.add_argument("--no-strict", action="store_true")
    mount.set_defaults(func=cmd_mount)

    inspect = sub.add_parser("inspect", help="Inspect parsed doctrine data")
    inspect.add_argument("path")
    inspect.add_argument("--format", choices=["json", "markdown"], default="json")
    inspect.set_defaults(func=cmd_inspect)

    doctor = sub.add_parser("doctor", help="Inspect .doctrine filetype diagnostics")
    doctor.add_argument("path")
    doctor.add_argument("--format", choices=["json", "markdown"], default="json")
    doctor.set_defaults(func=cmd_doctor)

    registry = sub.add_parser("registry", help="Registry commands")
    reg_sub = registry.add_subparsers(dest="registry_command", required=True)
    build = reg_sub.add_parser("build", help="Build registry/index.json from node files")
    build.add_argument("nodes_dir", nargs="?", default="nodes")
    build.add_argument("output", nargs="?", default="registry/index.json")
    build.set_defaults(func=cmd_registry_build)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
