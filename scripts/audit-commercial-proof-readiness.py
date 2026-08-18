#!/usr/bin/env python3
"""Report—not manufacture—commercial-proof readiness for switch-side CPO.

This is intentionally separate from a structural validation pass. A dossier can be
well referenced and still be unfit to support a deployment or profit-pool call.
The audit checks the explicit, current evidence status in the two controlled
dossiers and emits a machine-readable release decision.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOSSIERS = ROOT / "07-companies" / "commercial-proof-dossiers"
LEDGER = ROOT / "01-sources" / "claim-ledger.csv"

COMPANIES = {
    "NVIDIA Spectrum-X Ethernet Photonics": {
        "file": "nvidia-spectrum-x-photonics.md",
        "rows": {
            "exact_cpo_sku": "Exact CPO SKU/configuration",
            "named_customer_exact_sku": "Exact customer CPO SKU/configuration",
            "accepted_or_qualified_date": "Acceptance / qualification date",
            "observed_unit_port_or_system_denominator": "Units / ports / systems",
            "repeat_shipment_or_expansion": "Repeat shipment / expansion",
            "field_service_reliability": "Field service / reliability",
            "supplier_economic_attribution": "Product-linked supplier allocation / economics",
        },
        "economics_phrase": "This dossier makes no CPO revenue, EPS, market-share, margin or supplier-allocation forecast.",
        "required_claims": {"CLM-514", "CLM-515", "CLM-519", "CLM-520", "CLM-521"},
    },
    "Broadcom TH6-Davisson": {
        "file": "broadcom-th6-davisson.md",
        "rows": {
            "exact_cpo_sku": "Exact CPO SKU/configuration",
            "named_customer_exact_sku": "Exact customer TH6 CPO SKU/configuration",
            "accepted_or_qualified_date": "Acceptance / qualification date",
            "observed_unit_port_or_system_denominator": "Units / ports / systems",
            "repeat_shipment_or_expansion": "Repeat shipment / expansion",
            "field_service_reliability": "Field service / reliability",
            "supplier_economic_attribution": "Product-linked supplier allocation / economics",
        },
        "economics_phrase": "This dossier makes no CPO revenue, EPS, market-share, margin or supplier-allocation forecast.",
        "required_claims": {"CLM-076", "CLM-077", "CLM-516", "CLM-517", "CLM-530"},
    },
}


def ledger_ids() -> set[str]:
    with LEDGER.open(newline="") as source:
        return {row["claim_id"] for row in csv.DictReader(source)}


def main() -> None:
    known_claims = ledger_ids()
    errors: list[str] = []
    result: dict[str, object] = {"as_of": "2026-08-12", "companies": {}, "release_ready": False}

    for company, checks in COMPANIES.items():
        text = (DOSSIERS / checks["file"]).read_text()
        criteria = {}
        for field, label in checks["rows"].items():
            matching_rows = [line for line in text.splitlines() if line.startswith("|") and f"| {label} |" in line]
            if len(matching_rows) != 1:
                errors.append(f"{company}: expected one controlled gate row for {label}; found {len(matching_rows)}")
                criteria[field] = False
                continue
            # Only a deliberate Pass label changes a gate. 'Partial', supplier
            # participation and vendor availability are not enough.
            criteria[field] = "**Pass:**" in matching_rows[0]
        if checks["economics_phrase"] not in text:
            errors.append(f"{company}: economic no-forecast boundary missing")
        missing_claims = sorted(checks["required_claims"] - known_claims)
        if missing_claims:
            errors.append(f"{company}: required ledger claims missing: {', '.join(missing_claims)}")
        result["companies"][company] = criteria

    if errors:
        print("FAIL: commercial-proof readiness audit cannot verify its controlled baseline")
        print("\n".join(f"- {error}" for error in errors))
        sys.exit(1)

    result["release_ready"] = all(all(criteria.values()) for criteria in result["companies"].values())
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["release_ready"]:
        print("REVIEW REQUIRED: every documented gate is marked Pass. Independently verify new source boundaries before any release decision.")
    else:
        print("NOT RELEASE READY: one or more customer, scale, repeat, service or supplier-economics gates remain unproven.")


if __name__ == "__main__":
    main()
