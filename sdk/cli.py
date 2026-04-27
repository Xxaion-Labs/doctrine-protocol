import argparse
import json
from pathlib import Path

from .doctrine import Doctrine


def cmd_validate(args):
    doctrine = Doctrine.load(args.path)
    errors = doctrine.validate()
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2))
        return 1
    print(json.dumps({"valid": True, "path": args.path, "name": doctrine.name, "id": doctrine.id}, indent=2))
    return 0


def cmd_mount(args):
    doctrine = Doctrine.load(args.path)
    mounted = doctrine.mount(strict=not args.no_strict)
    print(json.dumps(mounted, indent=2))
    return 0


def cmd_inspect(args):
    doctrine = Doctrine.load(args.path)
    print(json.dumps(doctrine.to_dict(), indent=2))
    return 0


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
    inspect.set_defaults(func=cmd_inspect)

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
