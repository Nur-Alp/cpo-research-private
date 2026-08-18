# HTML archive coverage — 2026-08-10

## Purpose

This report records retained HTML pages that do not have a same-stem local PDF or Markdown companion. It prevents a readable-PDF audit from silently treating raw HTML archives as equivalent to page-readable source documents.

The current scan found **32 HTML archives** without a same-stem PDF/Markdown companion. They are primarily SEC filings, investor/product pages and publisher/web archives. Their evidence should be used through the associated evidence notes, source log and canonical URL; the raw HTML is a preservation/indexing copy, not a substitute for a readable PDF.

## Handling rule

- Keep the raw HTML when it is the canonical filing or publisher archive.
- Use the linked evidence note or retained PDF when one exists elsewhere under a normalized name.
- Do not generate browser-print PDFs for SEC filings or dynamic pages merely to increase the PDF count; print artifacts can omit figures, tables, scripts or pagination and are not equivalent to the original source.
- If a source is needed for direct inspection, obtain the publisher PDF or an accessible author copy and add it as a distinct retained file after title-page and page-count verification.

## Current gaps requiring a readable source

The high-value academic gaps remain tracked separately in the [full-text download list](academic-full-text-download-list.md). PAP-032 remains inaccessible for the current cycle. The 2026 SPIE 224G/lane FOWLP paper is no longer abstract-only: its full PDF is retained as PAP-056. The HTML coverage scan does not upgrade PAP-032.

## Reproducibility

The scan can be repeated from the repository root:

```bash
python3 - <<'PY'
from pathlib import Path
for p in sorted(Path('01-sources').rglob('*.html')):
    if not p.with_suffix('.pdf').exists() and not p.with_suffix('.md').exists():
        print(p)
PY
```
