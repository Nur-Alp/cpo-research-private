#!/usr/bin/env python3
"""Check that retained PDFs open and expose a non-empty page count."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    try:
        from pypdf import PdfReader
    except ImportError:
        print("FAIL: pypdf is required")
        return 2

    failures: list[str] = []
    opened = 0
    total_pages = 0
    paths = sorted((ROOT / "01-sources").rglob("*.pdf"))
    for path in paths:
        try:
            reader = PdfReader(str(path), strict=False)
            pages = len(reader.pages)
            opened += 1
            total_pages += pages
            if pages == 0:
                failures.append(f"{path.relative_to(ROOT)}: zero pages")
        except Exception as exc:  # report the file and continue
            failures.append(f"{path.relative_to(ROOT)}: {type(exc).__name__}: {exc}")

    print(f"pdf_files={len(paths)} opened={opened} total_pages={total_pages}")
    print(f"failures={len(failures)}")
    for failure in failures:
        print(f"FAIL: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
