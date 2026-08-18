#!/usr/bin/env python3
"""Audit source/claim IDs and relative Markdown links in the private CPO study."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ID_RE = re.compile(r"\b(?:PAP|CMP|PRI|STD|FIL|NWS|VID|PRS|WHT|ARC|MKT)-\d{3}\b")
SOURCE_ID_FROM_NAME_RE = re.compile(r"^(?:PAP|CMP|PRI|STD|FIL|NWS|VID|PRS|WHT|ARC|MKT)-\d{3}")
CLAIM_ID_RE = re.compile(r"\bCLM-\d{3}\b")
BLOCKED_ARCHIVE_RE = re.compile(
    r"<title>\s*(?:access denied|radware captcha page)|<h1>\s*access denied|"
    r"request denied|captcha\.perfdrive\.com",
    re.IGNORECASE,
)
LINK_RE = re.compile(r"\]\((?!https?://|#)([^)]+)\)")
LOCAL_PATH_RE = re.compile(
    r"(?:^|\s)((?:00-scope|01-sources|02-architecture|03-components|04-packaging|"
    r"05-standards|06-industry-map|07-companies|08-model|09-primary-research|"
    r"10-drafts|11-figures|scripts)/[^\s,;`)]*)"
)
SOURCE_HEADERS = [
    "source_id", "title", "author", "organisation", "publication_date",
    "access_date", "source_type", "company", "technology_area", "priority",
    "sequence", "review_mode", "review_status", "main_claim", "important_numbers",
    "assumptions", "limitations", "relevance", "confidence", "citation", "notes",
]
CLAIM_HEADERS = [
    "claim_id", "claim", "claim_type", "source_id", "exact_wording",
    "comparison_baseline", "independent_support", "contradicting_evidence",
    "confidence", "status", "thesis_area", "last_updated", "notes",
]


def csv_ids(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    return [row[0] for row in rows[1:] if row and row[0]]


def check_csv_width(path: Path, failures: list[str], expected_headers: list[str]) -> list[list[str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        failures.append(f"{path.relative_to(ROOT)} is empty")
        return []
    if rows[0] != expected_headers:
        failures.append(f"{path.relative_to(ROOT)} header does not match the required schema")
    expected = len(expected_headers)
    for line_no, row in enumerate(rows[1:], 2):
        if len(row) != expected:
            failures.append(
                f"{path.relative_to(ROOT)} row {line_no} has {len(row)} fields; expected {expected}"
            )
    return rows


def main() -> int:
    source_ids = csv_ids(ROOT / "01-sources/source-log.csv")
    claim_ids = csv_ids(ROOT / "01-sources/claim-ledger.csv")
    source_set = set(source_ids)
    claim_set = set(claim_ids)
    failures: list[str] = []

    source_rows = check_csv_width(ROOT / "01-sources/source-log.csv", failures, SOURCE_HEADERS)
    claim_rows = check_csv_width(ROOT / "01-sources/claim-ledger.csv", failures, CLAIM_HEADERS)

    for line_no, row in enumerate(source_rows[1:], 2):
        if len(row) == len(SOURCE_HEADERS) and (not row[0] or not row[1] or not row[6] or not row[19]):
            failures.append(f"source-log row {line_no} is missing a required ID, title, source type, or citation")
        if len(row) == len(SOURCE_HEADERS):
            for local_path in LOCAL_PATH_RE.findall(row[19]):
                if not (ROOT / local_path).exists():
                    failures.append(f"source-log row {line_no} cites missing local path {local_path}")
    for line_no, row in enumerate(claim_rows[1:], 2):
        if len(row) == len(CLAIM_HEADERS):
            if not row[0] or not row[1] or not row[3] or not row[9] or not row[10]:
                failures.append(f"claim-ledger row {line_no} is missing a required ID, claim, source, status, or thesis area")
            if row[8] not in {"High", "Medium", "Low"}:
                failures.append(f"claim-ledger row {line_no} has invalid confidence {row[8]!r}")
            if row[9] not in {"Open", "Reviewed", "Archived"}:
                failures.append(f"claim-ledger row {line_no} has invalid status {row[9]!r}")

    for label, ids in (("source", source_ids), ("claim", claim_ids)):
        duplicates = sorted({item for item in ids if ids.count(item) > 1})
        if duplicates:
            failures.append(f"duplicate {label} IDs: {', '.join(duplicates)}")

    with (ROOT / "01-sources/claim-ledger.csv").open(newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        next(reader, None)
        for line_no, row in enumerate(reader, 2):
            if len(row) < 4:
                failures.append(f"claim ledger row {line_no} has fewer than four fields")
                continue
            for source_id in SOURCE_ID_RE.findall(row[3]):
                if source_id not in source_set:
                    failures.append(f"claim ledger row {line_no} cites missing source {source_id}")

    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8", errors="ignore")
        for source_id in sorted(set(SOURCE_ID_RE.findall(text))):
            if source_id not in source_set:
                failures.append(f"{markdown}: cites missing source {source_id}")
        for claim_id in sorted(set(CLAIM_ID_RE.findall(text))):
            if claim_id not in claim_set:
                failures.append(f"{markdown}: cites missing claim {claim_id}")
        for match in LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if target and not (markdown.parent / target).exists():
                failures.append(f"{markdown}: missing relative link {target}")

    # A raw webpage archive is preservation, not a reader-friendly source by
    # itself. Every retained HTML source must have a same-ID Markdown evidence
    # note or PDF companion in its folder. This keeps the private library usable
    # without requiring an editor to inspect source code.
    for archive in (ROOT / "01-sources").rglob("*.html"):
        match = SOURCE_ID_FROM_NAME_RE.match(archive.name)
        if not match:
            continue
        source_id = match.group(0)
        companions = [
            path for path in archive.parent.glob(f"{source_id}-*")
            if path != archive and path.suffix.lower() in {".md", ".pdf"}
        ]
        if not companions:
            failures.append(
                f"{archive.relative_to(ROOT)} has no same-ID Markdown or PDF companion"
            )
            continue

        # A network block page is not source content. It may be retained only
        # as a documented publisher-access attempt alongside a readable source
        # card or PDF that explicitly labels the access limitation.
        archive_text = archive.read_text(encoding="utf-8", errors="ignore")
        if BLOCKED_ARCHIVE_RE.search(archive_text):
            companion_text = "\n".join(
                path.read_text(encoding="utf-8", errors="ignore")
                for path in companions
                if path.suffix.lower() == ".md"
            ).lower()
            if not re.search(r"access|captcha|block|restrict|subscription", companion_text):
                failures.append(
                    f"{archive.relative_to(ROOT)} is a blocked access page without a companion access limitation"
                )

    print(f"source_rows={len(source_ids)} unique_sources={len(source_set)}")
    print(f"claim_rows={len(claim_ids)} unique_claims={len(claim_set)}")
    print(f"failures={len(failures)}")
    for failure in failures:
        print(f"FAIL: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
