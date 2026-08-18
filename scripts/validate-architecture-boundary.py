#!/usr/bin/env python3
"""Check that the CPO alternatives work remains a same-boundary comparison."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCORECARD = ROOT / "02-architecture/system-boundary-comparison-scorecard.md"
MATRIX = ROOT / "02-architecture/architecture-trigger-matrix.md"
LINEAR = ROOT / "02-architecture/linear-drive-boundary-benchmark.md"
NPO = ROOT / "02-architecture/npo-interoperability-boundary.md"
ACQUISITION = ROOT / "09-primary-research/matched-architecture-comparison-acquisition-spec.md"


def require(text: str, phrase: str, label: str, failures: list[str]) -> None:
    if phrase not in text:
        failures.append(f"{label}: missing {phrase}")


def main() -> None:
    failures: list[str] = []
    scorecard = SCORECARD.read_text()
    scorecard_plain = scorecard.replace("**", "")
    matrix = MATRIX.read_text()
    linear = LINEAR.read_text()
    npo = NPO.read_text()
    acquisition = ACQUISITION.read_text()

    for term in ("Retimed pluggable", "LPO", "NPO / OBO", "Switch-side CPO"):
        require(scorecard_plain, term, SCORECARD.name, failures)
    for term in (
        "Release-control matrix",
        "Same ASIC, ports and lane rate",
        "Final good-unit yield, rework and test",
        "Service workflow, MTTR, spares and warranty",
        "conditional coexistence thesis",
        "Electrical path and margin",
        "Power and cooling boundary",
        "Thermal load and package boundary",
        "Serviceability and replacement burden",
        "Qualification, yield and rework",
        "Total replacement burden",
        "same lane rate, port count, reach, error target, temperature, cooling boundary and service policy",
        "component pJ/bit figure",
        "If an input is unavailable, preserve it as open",
        "RTLR is a separate hybrid comparator",
        "RTLR (retimed transmitter / linear receiver) is not synonymous with LPO",
        "RTLR retains a modular repair boundary that CPO must overcome economically.",
    ):
        require(scorecard_plain, term, SCORECARD.name, failures)

    for term in ("No lane rate alone makes CPO inevitable.", "Electrical gate", "System gate", "Manufacturing gate", "Service gate", "Economic gate"):
        require(matrix, term, MATRIX.name, failures)
    for term in ("Measured result versus simulation or estimate.", "Power boundary: module-only, host plus module, or a complete system.", "must not be averaged"):
        require(linear, term, LINEAR.name, failures)
    for term in ("same ASIC and lane rate", "same switch/XPU topology and port count", "all-in module/engine, installation and repair cost"):
        require(npo, term, NPO.name, failures)
    for term in (
        "same-boundary", "Inlet power", "Yield / rework", "Service boundary", "Supplier structure",
        "A component pJ/bit figure", "Same 102.4T-class switch ASIC", "measured 212.5-GBd/400G end-to-end link",
        "No retained public source clears this specification.",
    ):
        require(acquisition, term, ACQUISITION.name, failures)

    if failures:
        print("FAIL: architecture boundary validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: retimed, LPO, NPO and CPO are compared on an explicit common system boundary.")


if __name__ == "__main__":
    main()
