#!/usr/bin/env python3
"""Recompute the private optical-engine profit-pool sensitivity tables.

The figures tested here are explicitly illustrative assumptions.  This check
guards arithmetic, denominators and scenario boundaries; it does not validate
them as market estimates or authorise a company-level conclusion.
"""

from __future__ import annotations

import sys
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "08-model/profit-pool-scenario-bridge.md"
LAYER = ROOT / "08-model/engine-layer-sensitivity-ranges.md"


def require(text: str, fragment: str, failures: list[str], name: str) -> None:
    if fragment not in text:
        failures.append(f"{name}: missing `{fragment}`")


def main() -> None:
    bridge = BRIDGE.read_text()
    layer = LAYER.read_text()
    failures: list[str] = []

    # Fixed adoption sensitivity: $10k systems, 16 engines, $500 content and
    # 50% supplier share. Reported GP rounds to one decimal place in this table.
    fixed_adoptions = ("1", "5", "10", "25", "50", "100")
    for adoption in fixed_adoptions:
        a = Decimal(adoption) / 100
        supplied = Decimal("10000") * a * Decimal("16") * Decimal("0.5")
        revenue = supplied * Decimal("500")
        gross_profit = revenue * Decimal("0.35") - supplied * Decimal("50")
        require(bridge, f"| {adoption}% | ${revenue / Decimal('1000000'):.1f}M | ${gross_profit / Decimal('1000000'):.1f}M |", failures, "fixed sensitivity")

    # Scenario-only whole-engine bridge. Values are deliberately duplicated
    # here rather than parsed from prose so a changed table must reconcile.
    bridge_cases = (
        ("Bear", Decimal("10000"), Decimal(".05"), Decimal("16"), Decimal("250"), Decimal(".25"), Decimal(".15"), Decimal("50"), Decimal("30"), Decimal("25"), "$0.5M", "2,000", "−$0.135M"),
        ("Base", Decimal("10000"), Decimal(".25"), Decimal("16"), Decimal("500"), Decimal(".50"), Decimal(".35"), Decimal("25"), Decimal("15"), Decimal("10"), "$10.0M", "20,000", "$2.5M"),
        ("Bull", Decimal("10000"), Decimal(".50"), Decimal("16"), Decimal("900"), Decimal(".75"), Decimal(".50"), Decimal("10"), Decimal("8"), Decimal("5"), "$54.0M", "60,000", "$25.62M"),
    )
    for name, systems, adoption, engines, content, share, margin, yield_cost, warranty, cannibal, revenue_text, supplied_text, gp_text in bridge_cases:
        supplied = systems * adoption * engines * share
        revenue = supplied * content
        gross_profit = revenue * margin - supplied * (yield_cost + warranty + cannibal)
        require(bridge, revenue_text, failures, f"{name} bridge revenue")
        require(bridge, supplied_text, failures, f"{name} bridge supplied engines")
        require(bridge, gp_text, failures, f"{name} bridge gross profit")
        if name == "Bear" and gross_profit != Decimal("-135000"):
            failures.append("bear bridge arithmetic changed unexpectedly")
        if name == "Base" and gross_profit != Decimal("2500000"):
            failures.append("base bridge arithmetic changed unexpectedly")
        if name == "Bull" and gross_profit != Decimal("25620000"):
            failures.append("bull bridge arithmetic changed unexpectedly")

    # Layer model charges support/cannibalisation only to supplied good engines.
    layer_cases = (
        ("Bear", Decimal(".05"), Decimal("450"), Decimal(".25"), Decimal(".70"), Decimal(".15"), Decimal("40"), Decimal("30"), "8,000", "5,600", "1,400", "$0.63M", "−$0.0035M"),
        ("Base", Decimal(".25"), Decimal("1025"), Decimal(".50"), Decimal(".85"), Decimal(".35"), Decimal("20"), Decimal("15"), "40,000", "34,000", "17,000", "$17.43M", "$5.504M"),
        ("Bull", Decimal(".50"), Decimal("1900"), Decimal(".75"), Decimal(".95"), Decimal(".50"), Decimal("10"), Decimal("5"), "80,000", "76,000", "57,000", "$108.30M", "$53.295M"),
    )
    for name, adoption, eligible, share, good_yield, margin, warranty, cannibal, attempted_text, good_text, supplied_text, revenue_text, gp_text in layer_cases:
        attempted = Decimal("10000") * adoption * Decimal("16")
        good = attempted * good_yield
        supplied = good * share
        revenue = supplied * eligible
        gross_profit = revenue * margin - supplied * (warranty + cannibal)
        for fragment in (attempted_text, good_text, supplied_text, revenue_text, gp_text):
            require(layer, fragment, failures, f"{name} layer sensitivity")
        expected_gp = {"Bear": Decimal("-3500"), "Base": Decimal("5503750"), "Bull": Decimal("53295000")}[name]
        if gross_profit != expected_gp:
            failures.append(f"{name} layer arithmetic {gross_profit} != {expected_gp}")

    for text, label in ((bridge, "bridge"), (layer, "layer model")):
        require(text, "not a forecast", failures, label)
    require(bridge, "not observations", failures, "bridge assumption boundary")
    require(layer, "not an observed", failures, "layer-model assumption boundary")
    require(layer, "must be consolidated\nto avoid counting", failures, "layer model anti-double-counting control")
    require(bridge, "No partial technical denominator can be paired with an invented content", failures, "bridge model-entry control")

    if failures:
        print("FAIL: profit-pool sensitivity validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: profit-pool and layer-level scenario arithmetic, denominator controls and assumption boundaries reconcile.")


if __name__ == "__main__":
    main()
