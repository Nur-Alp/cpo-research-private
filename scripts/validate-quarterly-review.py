#!/usr/bin/env python3
"""Validate the private quarterly CPO evidence-review controls.

The check is intentionally conservative: it verifies the decision-changing
fields, not whether an announcement sounds supportive.  Source quality and
claim truth remain matters for the underlying evidence audit.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "08-model/critical-path-milestone-tracker.md"
GATES = ROOT / "08-model/evidence-gate-register.md"
DASHBOARD = ROOT / "08-model/falsification-dashboard.md"
QUEUE = ROOT / "09-primary-research/decision-changing-evidence-acquisition-queue.md"
CHANGE_REGISTER = ROOT / "09-primary-research/quarterly-evidence-change-register-2026-08-12.md"
EXTRACTION_PACK = ROOT / "09-primary-research/public-evidence-extraction-pack.md"
PROXY_WATCHLIST = ROOT / "09-primary-research/manufacturing-proxy-watchlist.md"
PATENT_PROTOCOL = ROOT / "09-primary-research/patent-and-standards-mining-protocol.md"


def require(text: str, phrase: str, label: str, failures: list[str]) -> None:
    if phrase not in text:
        failures.append(f"{label}: missing required control: {phrase}")


def main() -> None:
    failures: list[str] = []
    tracker = TRACKER.read_text()
    gates = GATES.read_text()
    dashboard = DASHBOARD.read_text()
    queue = QUEUE.read_text()
    change_register = CHANGE_REGISTER.read_text()
    extraction_pack = EXTRACTION_PACK.read_text()
    proxy_watchlist = PROXY_WATCHLIST.read_text()
    patent_protocol = PATENT_PROTOCOL.read_text()

    milestone_ids = re.findall(r"^\|\s*(MS-[A-Z0-9]+)\s*\|", tracker, re.MULTILINE)
    duplicates = sorted({item for item in milestone_ids if milestone_ids.count(item) > 1})
    if duplicates:
        failures.append(f"{TRACKER.name}: duplicate milestone IDs: {', '.join(duplicates)}")

    for milestone in ("MS-N01", "MS-N02", "MS-N03", "MS-N04", "MS-N05", "MS-N06", "MS-N07", "MS-N08"):
        require(tracker, milestone, TRACKER.name, failures)
    for field in (
        "state_before -> state_after",
        "source_id and claim_id",
        "what remains unproven",
        "Do not convert a vendor roadmap date into an observed date.",
    ):
        require(tracker, field, TRACKER.name, failures)

    for gate in (
        "Customer-confirmed production SKU, units, ports and deployment date",
        "Complete engine bill of materials and supplier responsibility map",
        "Final-engine yield waterfall, attach cycle time, rework and scrap",
        "Product ASP, realised CPO margin and price-down schedule",
        "Field reliability, engine replacement and warranty allocation",
    ):
        require(gates, gate, GATES.name, failures)

    for test in range(1, 11):
        require(dashboard, f"F-{test:02d}", DASHBOARD.name, failures)
    for field in (
        "Exact product/SKU and architecture boundary.",
        "Customer acceptance or qualification date.",
        "Units, ports, repeat shipment or expansion.",
        "Final-engine yield, test/rework, field failure or service cost.",
        "Supplier content, realised price, margin, capex or cannibalisation.",
    ):
        require(dashboard, field, DASHBOARD.name, failures)

    # Scheduled calls, conferences and roadmap dates are collection prompts,
    # not evidence. Keep explicit controls in the watchlist so a later update
    # cannot mistake an unchanged event link for a reported result.
    for field in (
        "do not treat the scheduled webcast as an outcome.",
        "do not treat the scheduled webcast as an outcome",
        "Recheck the official release, presentation, transcript and SEC filing after posting",
        "Recheck only after official materials are attached",
    ):
        require(queue, field, QUEUE.name, failures)

    for field in (
        "Required source locations by gate",
        "Exact SKU/customer/units/repeat",
        "Supplier content/share",
        "Yield/rework/test",
        "Required decision-impact order",
        "missing-input value-of-information register",
        "Do not add generic CPO coverage merely to increase source count.",
    ):
        require(change_register, field, CHANGE_REGISTER.name, failures)

    for field in (
        "Gate-by-gate search cards", "Source route checklist",
        "lawful public import/shipping records", "A proxy, patent, standard, job post or equipment order",
        "Intake result labels",
    ):
        require(extraction_pack, field, EXTRACTION_PACK.name, failures)

    for field in (
        "proxies cannot clear commercial, yield or economics gates",
        "Equipment order / installation", "Factory / capacity expansion", "Hiring",
        "hiring can indicate *preparation* for scale.",
    ):
        require(proxy_watchlist, field, PROXY_WATCHLIST.name, failures)

    for field in (
        "Patent search map", "Standards search map", "Promotion rule",
        "no patent or standard proves deployment or profit capture",
    ):
        require(patent_protocol, field, PATENT_PROTOCOL.name, failures)

    for field in (
        "Next quarterly review packet",
        "NVIDIA exact-SKU customer proof",
        "Broadcom exact-SKU customer proof",
        "Supplier-content attribution",
        "Manufacturing yield/service",
        "Matched architecture comparison",
        "Analyst overlay",
        "Quarterly sign-off:",
        "A scheduled event, unavailable page, unchanged roadmap or secondary repetition is a retrieval status",
    ):
        require(queue, field, QUEUE.name, failures)

    if failures:
        print("FAIL: quarterly CPO evidence-review validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: quarterly review has unique milestones, complete decision gates and falsification controls.")


if __name__ == "__main__":
    main()
