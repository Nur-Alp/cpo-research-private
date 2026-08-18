#!/usr/bin/env python3
"""Prevent the private CPO economic layer from silently becoming a fake forecast.

This is deliberately a structural control, not a financial-model validator.  It
checks that the current public evidence state (unallocated customer volume,
content, yield and margin) remains visible in the modelling files until a
matched primary record is added deliberately.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFIT = ROOT / "08-model/profit-pool-scenario-bridge.md"
GATES = ROOT / "08-model/optical-engine-profit-pool-input-gates.md"
EARNINGS = ROOT / "08-model/earnings-valuation-bridge-template.md"
BASELINE = ROOT / "08-model/public-financial-baseline-reconciliation.md"
MANUFACTURING_REVIEW = ROOT / "09-primary-research/manufacturing-economics-evidence-review-2026-08-11.md"
ECONOMIC_DISCLOSURE_AUDIT = ROOT / "09-primary-research/company-economic-disclosure-audit-2026-08-11.md"
YIELD_RECONCILIATION = ROOT / "08-model/yield-claim-reconciliation.md"
GOOD_ENGINE_GATE = ROOT / "08-model/manufacturing-cost-per-good-engine-gate.md"


def require(text: str, phrase: str, label: str, failures: list[str]) -> None:
    if phrase not in text:
        failures.append(f"{label}: missing control: {phrase}")


def main() -> None:
    failures: list[str] = []
    profit = PROFIT.read_text()
    gates = GATES.read_text()
    earnings = EARNINGS.read_text()
    baseline = BASELINE.read_text()
    manufacturing_review = MANUFACTURING_REVIEW.read_text()
    economic_disclosure_audit = ECONOMIC_DISCLOSURE_AUDIT.read_text()
    yield_reconciliation = YIELD_RECONCILIATION.read_text()
    good_engine_gate = GOOD_ENGINE_GATE.read_text()

    for phrase in (
        "Illustrative sensitivity (not a forecast)",
        "None of these assumptions is an observed company input.",
        "Replace every illustrative input before using the bridge for a company or valuation decision.",
        "Until steps 1–7 are evidenced, the bridge is a reusable calculation framework, not an investment conclusion.",
        "Six-company model-entry matrix",
        "No partial technical denominator can be paired with an invented content, share,",
        "Bear / base / bull range block (scenario-only)",
        "Nur Alpys sensitivities",
        "Supplier content/engine (`P`)",
        "Qualified supplier share (`Q`)",
        "Gross profit after `M`, `Y`, `W`, `K`",
        "does not identify a likely case",
    ):
        require(profit, phrase, PROFIT.name, failures)

    for company in ("NVIDIA", "Broadcom", "Coherent", "Lumentum", "Marvell", "TSMC"):
        require(profit, f"| {company} |", PROFIT.name, failures)
    if profit.count("| **Blocked** |") < 6:
        failures.append(
            f"{PROFIT.name}: six-company model-entry matrix must retain six blocked company states"
        )

    for variable in ("`S`", "`A`", "`P`", "`Q`", "`M`", "`Y`", "`W`", "`K`", "`R`", "`C`"):
        require(profit, f"| {variable}", PROFIT.name, failures)
    for state in (
        "Open; no adoption share cleared",
        "Open |",
        "Open; process examples are not production output",
    ):
        require(profit, state, PROFIT.name, failures)

    for phrase in (
        "A number can enter the base case only when all five conditions hold:",
        "No current company meets all five conditions for a numeric company revenue, gross-profit or free-cash-flow forecast.",
        "Supplier content cannot be counted simultaneously at the PIC, engine, module and platform layers.",
    ):
        require(gates, phrase, GATES.name, failures)

    for phrase in (
        "| Defined systems/year | — | — | — |",
        "| Supplier content/engine | — | — | — |",
        "| Product gross margin | — | — | — |",
        "| Yield/rework cost | — | — | — |",
        "| Warranty/support cost | — | — | — |",
        "| Valuation multiple | — | — | — |",
        "Until the [optical-engine profit-pool input gates]",
        "**not eligible**, not zero and not a hidden assumption.",
    ):
        require(earnings, phrase, EARNINGS.name, failures)

    for company in ("Broadcom", "NVIDIA", "Coherent", "Lumentum", "Marvell", "Celestica", "TSMC"):
        require(earnings, f"| {company} |", EARNINGS.name, failures)

    for company in ("NVIDIA", "Broadcom", "Coherent", "Lumentum", "Marvell", "TSMC"):
        require(baseline, f"| {company} |", BASELINE.name, failures)
    for phrase in (
        "No row below assigns a dollar, margin, unit, share or cash-flow amount to CPO.",
        "A fiscal label is retained exactly as reported.",
        "A company or segment metric is a **materiality denominator**, not a CPO numerator or a CPO product-margin proxy.",
        "The word **blocked** means “do not calculate”, not zero.",
        "Do not multiply CPO revenue by NVIDIA, Broadcom, Coherent, Lumentum, Marvell or TSMC consolidated gross margin",
    ):
        require(baseline, phrase, BASELINE.name, failures)

    if "CPO revenue forecast" in profit + gates + earnings + baseline:
        failures.append("economic-layer files contain an unsupported CPO revenue forecast label")

    for phrase in (
        "The model therefore remains blocked for every company.",
        "Lot-level stage yields, correlation, process capability, accepted-engine numerator",
        "Customer installation, test seconds, coverage, escape rate, utilization and cost per good die/engine",
        "Product-specific contract price, qualified share, gross margin, price-down and cancellation terms",
        "all yield, rework, warranty, ASP and product-margin cells remain **blank/blocked**",
    ):
        require(manufacturing_review, phrase, MANUFACTURING_REVIEW.name, failures)

    forbidden_model_inputs = (
        "Current manufacturing yield rates for CPO modules typically range from 60-75%",
        "CPO products carry a high average selling price",
        "double-digit operating margins",
    )
    for phrase in forbidden_model_inputs:
        if phrase in profit + gates + earnings + baseline + manufacturing_review:
            failures.append(f"economic layer contains unsupported manufacturing/economic claim: {phrase}")

    for company in ("NVIDIA", "Broadcom", "Coherent", "Lumentum", "Marvell", "TSMC"):
        require(economic_disclosure_audit, f"| {company} |", ECONOMIC_DISCLOSURE_AUDIT.name, failures)
    for phrase in (
        "**None.** The latest retained primary financial anchors",
        "CPO overlay remains **not eligible**",
        "Company-scale denominator only",
        "The sources above cannot be used to fill **any** of `supplier content`",
    ):
        require(economic_disclosure_audit, phrase, ECONOMIC_DISCLOSURE_AUDIT.name, failures)

    for phrase in (
        "They must not be placed in one waterfall without a denominator and process boundary.",
        "NVIDIA's 100% statement is particularly important to reconcile",
        "Do not substitute any of the rows above for `Y_die`, `Y_attach`, `Y_pkg`, `Y_test` or `Y_accept`",
        "Until such a record exists, preserve the yield claims as evidence-quality-bounded process signals",
    ):
        require(yield_reconciliation, phrase, YIELD_RECONCILIATION.name, failures)

    for phrase in (
        "This is a bookkeeping identity, not a forecast.",
        "It is not a supplier forecast and must not be read as final-engine yield.",
        "The roughly $518 spread between the low and high interface cases is a mechanical consequence of the formula",
        "An architecture should not receive a cost or profit-pool leadership score until it clears all of these gates:",
        "Customer/product identity, CPO allocation, wafer starts, seconds per wafer",
    ):
        require(good_engine_gate, phrase, GOOD_ENGINE_GATE.name, failures)

    if failures:
        print("FAIL: CPO economic-gate validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)

    print("PASS: economic scenario inputs remain explicitly illustrative or blocked; no company CPO forecast is populated.")


if __name__ == "__main__":
    main()
