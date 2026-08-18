#!/usr/bin/env python3
"""Validate traceability and minimum decision controls for private CPO outputs."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "01-sources"
LEDGER = SOURCES / "claim-ledger.csv"
DOCUMENTS = {
    ROOT / "07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md": [
        "Commercial-proof gate", "Supplier-content map", "No — not on the public record retained here."
    ],
    ROOT / "07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md": [
        "Commercial-proof gate", "Supplier-content map", "No — not on the public record retained here."
    ],
    ROOT / "03-components/pic-technology-decision-scorecard.md": [
        "Monolithic InP transmitter", "Silicon photonics + external laser",
        "TEC-less InP advanced-pluggable PIC",
        "Heterogeneous/2.5D SiPh engine", "3D CMOS microring / optical-I/O chiplet",
        "TFLN advanced-pluggable transmitter", "Comparable technology evidence — the fields that matter",
        "Modulator / transmitter evidence", "Receiver / link evidence", "Laser strategy",
        "Fibre coupling / service boundary", "Thermal boundary", "Testability / known-good path",
        "Final-engine yield / manufacturability", "Comparability controls", "Technology-to-company diligence mapping",
        "No route receives a commercial or profit-pool pass without a qualified-engine denominator",
        "No company ranking follows from this table.",
        "Route-control matrix", "Silicon photonics + external laser",
        "Thin-film lithium niobate", "Heterogeneous / 2.5D integration",
        "Hard rule:", "qualified, serviceable good engine"
        , "Promotion test: laboratory result to investable engine route",
        "Qualified good-engine output", "Attributable economics"
    ],
    ROOT / "00-scope/immediate-decision-dashboard.md": [
        "What can be decided now", "The investable PIC question", "Architecture decision rule",
        "NVIDIA", "Broadcom", "Coherent", "Lumentum", "Marvell", "TSMC",
        "No row clears an attributable CPO economics gate.",
        "Exact-SKU commercial-conversion control", "no proven CPO profit-pool\nleader"
    ],
    ROOT / "09-primary-research/nvidia-broadcom-commercial-conversion-dossier-2026-08-13.md": [
        "NVIDIA and Broadcom switch-CPO commercial-conversion dossier",
        "The required conversion chain", "NVIDIA Spectrum-X Ethernet Photonics",
        "Broadcom TH6-Davisson", "Supplier-allocation disposition",
        "Commercial-conversion watchlist", "Promotion and downgrade tests",
        "strategically promising, commercially early, no proven CPO profit-pool leader"
    ],
    ROOT / "08-model/exact-sku-commercial-proof-files-2026-08-13.md": [
        "Exact-SKU commercial-proof files", "NVIDIA `SN6810` / `SN6810-LD`",
        "NVIDIA `SN6800` / `SN6800-LD`", "Broadcom `BCM78919` / TH6-Davisson",
        "Mandatory negative controls", "Update protocol"
    ],
    ROOT / "09-primary-research/public-evidence-exhaustion-register-2026-08-13.md": [
        "Public-evidence exhaustion register", "Indirect-evidence mining protocol",
        "Search completion condition", "searched and remains non-public"
    ],
    ROOT / "00-scope/public-evidence-completion-standard-2026-08-13.md": [
        "Public-evidence completion standard", "Requirement-to-control map",
        "Minimum integrity thresholds", "Research-complete public-evidence system",
        "The next work is only evidence that can change one of those statements."
    ],
    ROOT / "07-companies/six-company-product-to-economics-proof-register-2026-08-13.md": [
        "Six-company product-to-economics proof register", "NVIDIA", "Broadcom",
        "Coherent", "Lumentum", "Marvell", "TSMC", "Readout", "Update rule"
    ],
    ROOT / "00-scope/public-evidence-completion-audit-2026-08-13.md": [
        "Public-evidence completion audit", "Audit method", "Integrity validation",
        "The **research system is complete as public evidence permits",
        "customer-volume leader"
    ],
    ROOT / "08-model/missing-input-value-of-information.md": [
        "Exact CPO SKU, named customer, accepted systems/ports and date",
        "Repeat order, expansion or second customer", "Final accepted-engine yield waterfall and rework",
        "Product gross margin and incremental capex/R&D", "Collection sequence",
        "No company receives numeric revenue, EPS, valuation or leadership output"
    ],
    ROOT / "08-model/architecture-competitor-timeline.md": [
        "State labels", "Switch CPO, 200G Ethernet", "InP advanced pluggable, 400G/lane",
        "TFLN advanced pluggable, 400G/lane", "market forecast as an event."
    ],
    ROOT / "08-model/disclosure-lag-model.md": [
        "Disclosure ladder", "Commercial proof", "Financial disclosure",
        "It does **not** infer that an undisclosed deployment exists",
        "silence is neither"
    ],
    ROOT / "08-model/manufacturing-cost-per-good-engine-gate.md": [
        "Cost-per-qualified-good-engine input classification", "Measured mechanism; cost unavailable",
        "Assumption range only", "cost per qualified good engine =", "which term to learn next"
    ],
    ROOT / "09-primary-research/public-manufacturing-readiness-dossier-2026-08-13.md": [
        "Executive decision", "Ranked readiness and constraint map",
        "coupled fibre-interface and final-engine qualification loop",
        "Most visible near-term manufacturing control point",
        "No supplier is a proven manufacturing-profit leader.",
        "What would change the ranking", "Immediate desk-research queue",
        "This is a private synthesis."
    ],
    ROOT / "09-primary-research/fibre-attach-serviceability-evidence-pack-2026-08-13.md": [
        "Four questions answered", "Can detachable FAUs/connectors materially reduce late-stage scrap",
        "What attachment/coupling methods are realistically manufacturable",
        "Which company controls each boundary?", "What would show that the constraint moved",
        "Attachment/service architecture ranking", "No public source provides the matched production record",
        "This pack therefore strengthens the PIC/engine thesis"
    ],
    ROOT / "09-primary-research/package-test-qualification-evidence-pack-2026-08-13.md": [
        "Test-flow map: wafer → engine → package → module → burn-in",
        "Actual production tooling/capacity versus measured yield/cost",
        "Late-defect cost map", "Control-point and value-capture map",
        "How to determine whether package/test has overtaken fibre attach",
        "No retained public record clears these tests.",
        "coupled late-defect-cost problem"
    ],
    ROOT / "08-model/qualified-engine-loss-and-late-defect-model-2026-08-13.md": [
        "Current bottleneck verdict", "Common loss waterfall", "Stage-change tests",
        "No row supports a supplier profit-pool conclusion.", "cost per accepted engine ="
    ],
    ROOT / "09-primary-research/osat-test-production-vs-tooling-scorecard-2026-08-13.md": [
        "OSAT and test evidence — production versus tooling scorecard",
        "No OSAT or test supplier is eligible", "Promotion test"
    ],
    ROOT / "07-companies/engine-control-maps/nvidia-spectrum-x-qualified-engine-control-map-2026-08-13.md": [
        "NVIDIA Spectrum-X qualified-engine control map", "Economic readout",
        "Upgrade requirement", "Public evidence does not show"
    ],
    ROOT / "07-companies/engine-control-maps/broadcom-th6-qualified-engine-control-map-2026-08-13.md": [
        "Broadcom TH6-Davisson qualified-engine control map", "Economic readout",
        "Upgrade requirement", "black box economically"
    ],
    ROOT / "02-architecture/failure-domain-replacement-scope-matrix-2026-08-13.md": [
        "Failure-domain and replacement-scope matrix", "Serviceability tests",
        "ELSFP:", "Engine replacement:", "Required restored-port evidence"
    ],
    ROOT / "03-components/qualified-engine-value-capture-conclusion-2026-08-13.md": [
        "Qualified-engine value-capture conclusion", "No layer has public evidence",
        "Company-view refresh", "Disconfirming evidence"
    ],
    ROOT / "07-companies/variant-cards/core-company-variant-cards.md": [
        "NVIDIA —", "Broadcom —", "Coherent —", "Lumentum —", "Marvell —", "TSMC —",
        "Direct CPO EPS sensitivity is **not eligible**", "**Evidence confidence:**",
        "**Likely value capture (gated):**",
    ],
    ROOT / "07-companies/six-company-content-attribution-register.md": [
        "NVIDIA Spectrum-X Ethernet Photonics", "Broadcom TH6-Davisson / BCM78919",
        "Coherent", "Lumentum", "TSMC", "Marvell / Celestial AI",
        "Confirmed role", "Route / candidate", "Open", "Outside switch-CPO boundary",
        "No company should be assigned CPO revenue",
    ],
    ROOT / "07-companies/leader-scorecard.md": [
        "not a company ranking", "SKU-bound NVIDIA dossier", "SKU-bound Broadcom dossier",
        "not deployed volume, qualified-engine performance, supplier profit or a public-equity conclusion",
        "No leader established",
    ],
    ROOT / "00-scope/current-decision-memo-2026-08-11.md": [
        "No. CPO is not yet investable as a standalone public-equity thesis on the retained evidence.",
        "Company decision cards", "2026–27 timing call", "The investable test",
        "strongest switch-CPO timing signal; no proven CPO volume leader; no proven CPO profit-pool leader; no standalone equity conclusion.",
    ],
    ROOT / "00-scope/final-conclusion-2026-08-10.md": [
        "Historical private working snapshot", "superseded for current decisions",
        "not a publication-ready conclusion or an investment conclusion",
        "No overall technical leader established.", "Not eligible as a current forecast.",
        "Current CPO decision memo", "No leader established.",
    ],
    ROOT / "08-model/switch-cpo-sku-content-reconciliation.md": [
        "SN6810", "SN6800", "TH6-Davisson", "BCM78919", "EIC / driver / TIA",
        "Prohibited transfers", "Commercial-proof gate remains open for both.",
        "No profit-pool ranking or EPS sensitivity is eligible.",
    ],
}
SOURCE_ID = re.compile(r"(?:CMP|PRI|PAP|STD|FIL|PRS|ANL)-\d{3}")
CLAIM_ID = re.compile(r"CLM-\d{3}")


def claims_from_text(text: str) -> set[str]:
    claims = set(CLAIM_ID.findall(text))
    for start, end in re.findall(r"CLM-(\d{3})\s*[–-]\s*CLM-(\d{3})", text):
        claims.update(f"CLM-{number:03d}" for number in range(int(start), int(end) + 1))
    return claims


def main() -> None:
    failures: list[str] = []
    with LEDGER.open(newline="") as handle:
        claims = {row["claim_id"]: row for row in csv.DictReader(handle)}
    source_log_ids = {
        row["source_id"]
        for row in csv.DictReader((SOURCES / "source-log.csv").open(newline=""))
    }

    for path, required in DOCUMENTS.items():
        text = path.read_text()
        for phrase in required:
            if phrase not in text:
                failures.append(f"{path.name}: missing required control: {phrase}")

        document_sources = set(SOURCE_ID.findall(text))
        for claim_id in claims_from_text(text):
            row = claims.get(claim_id)
            if row is None:
                failures.append(f"{path.name}: unknown claim ID {claim_id}")
                continue
            document_sources.update(SOURCE_ID.findall(row["source_id"]))

        for source_id in document_sources:
            retained = list(SOURCES.rglob(f"{source_id}-*"))
            if source_id not in source_log_ids and not retained:
                failures.append(f"{path.name}: source ID lacks a source-log row or retained companion: {source_id}")

        if "CPO revenue forecast" in text or "CPO EPS forecast" in text:
            failures.append(f"{path.name}: contains an unsupported numeric-forecast label")

    cards = (ROOT / "07-companies/variant-cards/core-company-variant-cards.md").read_text()
    required_card_fields = (
        "**Evidence confidence:**",
        "**Product boundary and observed facts:**",
        "**Customer / supplier evidence:**",
        "**Likely value capture (gated):**",
        "**Expectation versus variant:**",
        "**Earnings relevance:**",
        "**Catalyst / falsification:**",
    )
    for field in required_card_fields:
        found = cards.count(field)
        if found != 6:
            failures.append(f"core-company-variant-cards.md: expected exactly 6 {field} fields, found {found}")

    company_headers = ("NVIDIA", "Broadcom", "Coherent", "Lumentum", "Marvell", "TSMC")
    header_pattern = re.compile(r"^## ([^—\n]+) —", re.MULTILINE)
    headers = tuple(match.group(1).strip() for match in header_pattern.finditer(cards))
    if headers != company_headers:
        failures.append(
            "core-company-variant-cards.md: company-card headers must contain exactly "
            + ", ".join(company_headers)
        )

    if failures:
        print("FAIL: private CPO decision-layer validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: all decision-layer documents have required controls and traceable source/claim references.")


if __name__ == "__main__":
    main()
