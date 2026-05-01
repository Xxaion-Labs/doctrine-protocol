from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THIS_FILE = Path(__file__).resolve()
TEXT_SUFFIXES = {'.md', '.py', '.doctrine', '.glyph', '.txt', '.toml', '.yml', '.yaml', '.json'}

REQUIRED = {
    'TESSERACT.md': ['.glyph', 'A Tesseract', '⧉', '(digital)'],
    'README.md': ['.glyph', 'A Tesseract', '⧉'],
    'SPEC.md': ['.glyph', 'A Tesseract', 'Semantic Face', 'Machine Face', 'Mount Face', 'Proof Face'],
    'COMPATIBILITY.md': ['.glyph compatible', '.doctrine compatible'],
}

FORBIDDEN = [
    'Tesseract Sigil',
    'Doctrine Tesseract',
    'DoctrineOS Tesseract',
    'Doctrine marker',
    'Doctrine symbol',
    '.soul',
    '.sol',
]


def iter_text_files():
    skip_dirs = {'.git', '__pycache__', '.pytest_cache', '.doctrineos'}
    for path in ROOT.rglob('*'):
        if path.resolve() == THIS_FILE:
            continue
        if any(part in skip_dirs for part in path.parts):
            continue
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            yield path


def main() -> int:
    failures = []
    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f'missing required file: {rel}')
            continue
        text = path.read_text(encoding='utf-8')
        for needle in needles:
            if needle not in text:
                failures.append(f'{rel} missing required text: {needle}')
    for path in iter_text_files():
        text = path.read_text(encoding='utf-8', errors='ignore')
        rel = path.relative_to(ROOT).as_posix()
        for forbidden in FORBIDDEN:
            if forbidden in text:
                failures.append(f'{rel} contains forbidden text: {forbidden}')
    if failures:
        print('Glyph standard check failed:')
        for failure in failures:
            print(f'- {failure}')
        return 1
    print('Glyph standard check passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
