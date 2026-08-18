#!/usr/bin/env python3
"""Keep restricted analyst inputs traceable and out of unsupported CPO calls.

This is an evidence and publication-boundary control.  It deliberately does
not validate a valuation or make a forecast.  Run it before modelling work or
any future public-release review.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / "01-sources/analyst-estimates"
REGISTER = ROOT / "08-model/analyst-estimate-register.md"
BASELINE = ROOT / "08-model/public-financial-baseline-reconciliation.md"
SPECIFICATION = ROOT / "08-model/analyst-variant/scenario-model-specification.md"
WORKSPACE_GUIDE = ROOT / "08-model/analyst-variant/README.md"
CHECKLIST = ROOT / "08-model/analyst-variant/quarterly-refresh-checklist.md"
HANDOFF = ROOT / "08-model/analyst-variant/expectations-variant-quarterly-handoff-2026-08-13.md"
FISCAL_MAP = ROOT / "08-model/analyst-variant/fiscal-period-comparability-map-2026-08-13.md"


def require(text: str, phrase: str, label: str, failures: list[str]) -> None:
    if phrase not in text:
        failures.append(f"{label}: missing control: {phrase}")


def main() -> None:
    failures: list[str] = []
    library = (LIBRARY / "README.md").read_text()
    register = REGISTER.read_text()
    baseline = BASELINE.read_text()
    specification = SPECIFICATION.read_text()
    workspace_guide = WORKSPACE_GUIDE.read_text()
    checklist = CHECKLIST.read_text()
    handoff = HANDOFF.read_text()
    fiscal_map = FISCAL_MAP.read_text()

    for phrase in (
        "must remain private and must never be copied to the public Quarto website",
        "firm, report date, as-of date, access restriction, exact page/table",
        "Uploading a report, screenshot, table or model page.",
        "Treating an analyst estimate as a customer shipment, product yield, ASP, margin or other observed fact.",
        "`ANL-###-firm-company-asof-YYYY-MM-DD.ext`",
    ):
        require(library, phrase, "analyst-estimates/README.md", failures)

    for phrase in (
        "Estimate ID", "Source ID", "Firm / analyst", "Report date / as-of date",
        "Fiscal period", "Value / range / unit", "Accounting basis", "Report location",
        "Evidence classification", "Public-use status", "private-only",
        "derived-range-permitted", "publicly-citable",
        "Readiness matrix for a CPO investment sensitivity",
        "Consolidated baseline", "Exact CPO product boundary",
        "Customer volume and repeatability", "Supplier content/share",
        "EPS/valuation sensitivity", "Overlay release rule",
        "Until then, use analyst material to document expectations or sensitivity ranges",
        "Never combine GAAP and non-GAAP metrics without an explicit reconciliation row.",
        "A CPO-specific input must identify the product boundary.",
    ):
        require(register, phrase, REGISTER.name, failures)

    for phrase in (
        "values remain unpopulated until restricted analyst sources are ingested.",
        "no standalone target price.",
        "Every unobserved input is labelled `external estimate` or `Nur Alpys assumption`.",
        "Never use consolidated margin as fact",
        "Do not count platform revenue and optical-engine content in the same revenue bridge",
        "If a critical input is absent, show `not eligible` rather than zero.",
    ):
        require(specification, phrase, SPECIFICATION.name, failures)

    for phrase in (
        "should never contain copied report pages or screenshots.",
        "Reconcile each company’s baseline consensus.",
    ):
        require(workspace_guide, phrase, WORKSPACE_GUIDE.name, failures)

    for phrase in (
        "Flag estimates older than 90 days", "fiscal year, GAAP/non-GAAP basis, currency, stock splits and TSMC ADR/share conversion",
        "Compare prior-quarter consensus/variant inputs against reported company results.",
        "Record all changed, delayed or withdrawn conclusions",
    ):
        require(checklist, phrase, CHECKLIST.name, failures)

    for phrase in (
        "Expectations-versus-variant quarterly handoff",
        "Fix the clock", "Record observed outcome", "Refresh expectations",
        "Measure the change", "Recheck CPO gates", "Write the variant",
        "Release review", "Company update card: minimum quarterly fields",
        "Change taxonomy", "not a CPO consensus set",
        "no company has a reconciled CPO numerator, product economics",
    ):
        require(handoff, phrase, HANDOFF.name, failures)

    for phrase in (
        "No row below assigns a dollar, margin, unit, share or cash-flow amount to CPO.",
        "A company or segment metric is a **materiality denominator**, not a CPO numerator or a CPO product-margin proxy.",
        "An EPS or valuation sensitivity cannot be calculated until compatible tax rate, diluted shares, scenario output and accounting basis are present.",
        "The word **blocked** means “do not calculate”, not zero.",
        "fiscal-period comparability map",
    ):
        require(baseline, phrase, BASELINE.name, failures)

    for phrase in (
        "Fiscal-period comparability map", "NVIDIA", "Broadcom", "Coherent", "Lumentum", "Marvell", "TSMC",
        "Period test:", "Basis test:", "Currency/listing test:", "Share test:", "Boundary test:",
        "not yet a harmonised consensus or valuation dataset", "CPO EPS and valuation sensitivities remain **not eligible**",
    ):
        require(fiscal_map, phrase, FISCAL_MAP.name, failures)

    # The tracked library may contain only a guide and controlled, public-source
    # intake notes.  Restricted PDFs/XLSX/PPTX/screenshots belong locally in the
    # ignored library and must never be staged into a public report.
    permitted_suffixes = {".md"}
    tracked_like_files = [path for path in LIBRARY.iterdir() if path.is_file()]
    for path in tracked_like_files:
        if path.suffix.lower() not in permitted_suffixes:
            failures.append(
                f"analyst-estimates/{path.name}: restricted binary or spreadsheet is present; keep it ignored and verify it is excluded from public output"
            )

    if failures:
        print("FAIL: analyst-estimate boundary validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)

    print("PASS: analyst inputs remain restricted, traceable and blocked from unsupported public CPO valuation claims.")


if __name__ == "__main__":
    main()
