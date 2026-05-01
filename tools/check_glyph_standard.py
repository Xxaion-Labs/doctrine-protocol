from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    'SOUL_PROTOCOL.md': ['.soul', 'A Soul Protocol object', '⧉', '(digital)'],
    'README.md': ['Soul Protocol', '.soul', 'A Soul Protocol object', '⧉'],
}
OLD_PUBLIC_TERMS = [
    '.glyph',
    'A Tesseract',
    'Tesseract-compatible',
    'Tesseract-aware',
    'DoctrineOS exists',
    'DoctrineOS is',
    'DoctrineOS currently',
]
SCAN_FILES = [
    'README.md',
    'SOUL_PROTOCOL.md',
    'VISION.md',
    'ARCHITECTURE.md',
    'ROADMAP.md',
    'SPEC.md',
    'COMPATIBILITY.md',
    'CHANGELOG.md',
]


def main() -> int:
    failures: list[str] = []

    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f'missing required file: {rel}')
            continue
        text = path.read_text(encoding='utf-8')
        for needle in needles:
            if needle not in text:
                failures.append(f'{rel} missing required text: {needle}')

    for rel in SCAN_FILES:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        for term in OLD_PUBLIC_TERMS:
            if term in text:
                failures.append(f'{rel} contains stale public wording: {term}')

    if failures:
        print('Soul Protocol standard check failed:')
        for failure in failures:
            print(f'- {failure}')
        return 1

    print('Soul Protocol standard check passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
