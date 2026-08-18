#!/usr/bin/env python3
"""Traceability checks for the private NVIDIA and Broadcom proof dossiers."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOSSIERS = ROOT / "07-companies/commercial-proof-dossiers"
SEARCH_AUDIT = ROOT / "09-primary-research/sku-customer-search-audit-2026-08-11.md"
SOURCES = ROOT / "01-sources"
LEDGER = SOURCES / "claim-ledger.csv"

REQUIRED = {
    "commercial-proof-decision-memo.md": [
        "Decision in one page",
        "Exact CPO SKU",
        "Exact customer tied to exact CPO SKU",
        "Repeat shipment / expansion",
        "Supplier-content chain",
        "What would change the decision",
        "no public record clears the full commercial-proof gate",
    ],
    "nvidia-spectrum-x-photonics.md": [
        "Current answer",
        "Product boundary",
        "Supplier-content map",
        "Commercial-proof gate",
        "Timing implication and falsification",
        "controlled naming cross-reference",
        "No — not on the public record retained here.",
    ],
    "broadcom-th6-davisson.md": [
        "Current answer",
        "Product boundary",
        "Supplier-content map",
        "Commercial-proof gate",
        "Timing implication and falsification",
        "No — not on the public record retained here.",
    ],
}

# These fields are the minimum definition of a commercial numerator. Their
# presence ensures a readable narrative cannot silently omit the actual
# deployment test the dossier is meant to answer.
COMMERCIAL_GATE_FIELDS = (
    "Exact customer",
    "Acceptance / qualification date",
    "Units / ports / systems",
    "Repeat shipment / expansion",
    "Field service / reliability",
)

# Content is an economic boundary. Each dossier must say where the disclosure
# ends instead of treating a platform name as a bill of materials.
CONTENT_BOUNDARY_FIELDS = (
    "ASIC",
    "SerDes",
    "EIC",
    "PIC",
    "Laser",
    "Fibre",
    "Package",
    "test",
)


def expand_claim_references(text: str) -> set[str]:
    claims = set(re.findall(r"CLM-\d{3}", text))
    for start, end in re.findall(r"CLM-(\d{3})\s*[–-]\s*CLM-(\d{3})", text):
        claims.update(f"CLM-{number:03d}" for number in range(int(start), int(end) + 1))
    return claims


def main() -> None:
    failures: list[str] = []
    ledger_ids = set(re.findall(r"^(CLM-\d{3}),", LEDGER.read_text(), flags=re.MULTILINE))

    for filename, required_text in REQUIRED.items():
        path = DOSSIERS / filename
        text = path.read_text()
        for item in required_text:
            if item not in text:
                failures.append(f"{filename}: missing required section or conclusion: {item}")

        for field in COMMERCIAL_GATE_FIELDS:
            if field not in text:
                failures.append(f"{filename}: commercial-proof gate omits {field}")

        if filename != "commercial-proof-decision-memo.md":
            for field in CONTENT_BOUNDARY_FIELDS:
                if field.lower() not in text.lower():
                    failures.append(f"{filename}: supplier-content map omits {field} boundary")

        for source_id in set(re.findall(r"(?:CMP|PRI)-\d{3}", text)):
            if not list(SOURCES.rglob(f"{source_id}-*")):
                failures.append(f"{filename}: no retained source card or archive for {source_id}")

        for claim_id in expand_claim_references(text):
            if claim_id not in ledger_ids:
                failures.append(f"{filename}: claim not found in ledger: {claim_id}")

        for forbidden in ("CPO revenue forecast", "CPO EPS forecast", "is a verified volume leader"):
            if forbidden in text:
                failures.append(f"{filename}: unsupported conclusion wording: {forbidden}")

    audit_text = SEARCH_AUDIT.read_text()
    for item in (
        "SKU-bound customer search audit", "SN6810", "SN6800", "TH6-Davisson", "BCM78919",
        "named customer + accepted units/ports + repeat shipment", "No current result clears the commercial-proof gate.",
    ):
        if item not in audit_text:
            failures.append(f"{SEARCH_AUDIT.name}: missing reproducibility control: {item}")
    for claim_id in expand_claim_references(audit_text):
        if claim_id not in ledger_ids:
            failures.append(f"{SEARCH_AUDIT.name}: claim not found in ledger: {claim_id}")

    if failures:
        print("FAIL: commercial-proof dossier validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)

    print("PASS: commercial-proof dossiers have required gates, retained source IDs and ledger claim IDs.")


if __name__ == "__main__":
    main()
