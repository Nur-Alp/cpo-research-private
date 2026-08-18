#!/usr/bin/env python3
"""Ensure manufacturing evidence retains its physical and economic boundaries.

Prototype process data can be decision-relevant, but it must not silently
become a production-yield, warranty or profit-pool input.  This control checks
the current manufacturing review, yield reconciliation and service model for
the fields a later release would need to preserve.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "09-primary-research/manufacturing-economics-evidence-review-2026-08-11.md"
YIELD = ROOT / "08-model/yield-claim-reconciliation.md"
SERVICE = ROOT / "08-model/service-and-failure-domain-cost-model.md"
BENCHMARK = ROOT / "03-components/packaging-reliability-benchmark.md"
PROOF = ROOT / "08-model/manufacturing-proof-matrix.md"
CHECKLIST = ROOT / "09-primary-research/manufacturing-production-evidence-checklist.md"
INTAKE = ROOT / "09-primary-research/production-record-intake-schema-2026-08-13.md"


def require(text: str, phrase: str, label: str, failures: list[str]) -> None:
    if phrase not in text:
        failures.append(f"{label}: missing boundary: {phrase}")


def main() -> None:
    failures: list[str] = []
    review = REVIEW.read_text()
    yield_text = YIELD.read_text()
    service = SERVICE.read_text()
    benchmark = BENCHMARK.read_text()
    proof = PROOF.read_text()
    checklist = CHECKLIST.read_text()
    intake = INTAKE.read_text()

    for phrase in (
        "Good-die / attach / package / final-test yield",
        "Rework and scrap recovery",
        "Test / burn-in throughput",
        "Qualification / reliability",
        "Service / replacement",
        "Revenue / share / ASP / margin",
        "Lot-level stage yields, correlation, process capability, accepted-engine numerator",
        "Customer installation, test seconds, coverage, escape rate, utilization and cost per good die/engine",
        "field-return, repair/replace, MTTR or warranty-reserve data",
        "all yield, rework, warranty, ASP and product-margin cells remain **blank/blocked**",
    ):
        require(review, phrase, REVIEW.name, failures)

    for phrase in (
        "They must not be placed in one waterfall without a denominator and process boundary.",
        "Unit:", "Stage:", "Denominator:", "Sample and lot:", "Conditions:", "Failure disposition:",
        "Do not substitute any of the rows above for `Y_die`, `Y_attach`, `Y_pkg`, `Y_test` or `Y_accept`",
        "NVIDIA's 100% statement is particularly important to reconcile",
    ):
        require(yield_text, phrase, YIELD.name, failures)

    for phrase in (
        "Faceplate pluggable", "ELSFP / external light", "Socketable optical engine", "Fixed CPO package", "NPO/OBO module",
        "failure events\n= laser/ELS + fibre/connector + PIC/engine",
        "The model must preserve correlated failures.",
        "Failure-rate distributions", "MTTR, spare ratio", "field-return data",
        "not a qualitative claim converted into a margin adjustment.",
    ):
        require(service, phrase, SERVICE.name, failures)

    # PAP-015 is the strongest concrete fibre-attach process-control packet.
    # Its stated sample and measurement boundary must remain visible.
    for phrase in (
        "IBM passive fibre-array attach process control", "30 GlobalFoundries 45SPCLO mock-ups",
        "16-fibre 250 um-pitch FAUs", "1,178 observations", "production Cpk", "final attach yield",
        "No production-lot yield, sample-size/pass-fail distribution, automated cycle time, FIT",
        "No paper supplies final-package or final-engine yield.",
        "No paper reports Cpk, automated line volume, scrap cost or field return rate.",
        "The reviewed evidence supports packaging, fibre attach and serviceability as adoption-critical engineering constraints.",
    ):
        require(benchmark, phrase, BENCHMARK.name, failures)

    for phrase in (
        "pre-tested known-good die and components are important for high yield",
        "approximately 50% substrate loss", "approximately 90% cumulative loss",
        "no delamination in that prototype flow",
        "Screen coverage, false pass/fail", "A unit rework route, recovery fraction",
        "starts → screened components → assembled engines → final-test pass",
        "field returns",
        "not evidence that any supplier has cleared the chain above in production.",
    ):
        require(proof, phrase, PROOF.name, failures)

    for phrase in (
        "Manufacturing production-evidence checklist",
        "Required numerator",
        "Required denominator and metadata",
        "Incoming / known-good screening",
        "Fibre attach",
        "Package / thermal assembly",
        "Optical/electrical final test",
        "Burn-in / qualification",
        "Customer acceptance / shipment",
        "Field service",
        "Economics",
        "Do not populate a production input from:",
        "No retained public record clears the complete bundle",
        "open/blocked**, not zero",
    ):
        require(checklist, phrase, CHECKLIST.name, failures)

    for phrase in (
        "Production-record intake schema",
        "Product boundary", "Physical stage", "Manufacturing location and period",
        "Numerator", "Denominator", "Failure disposition", "Cost boundary",
        "Model eligibility by stage", "Fast rejection checklist",
        "Aehr’s `CMP-080`", "not a yield or CPO-economics input.",
    ):
        require(intake, phrase, INTAKE.name, failures)

    if failures:
        print("FAIL: manufacturing-boundary validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)

    print("PASS: manufacturing evidence preserves sample, process, service and economic boundaries; no production profit claim is implied.")


if __name__ == "__main__":
    main()
