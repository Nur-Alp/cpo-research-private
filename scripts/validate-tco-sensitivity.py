#!/usr/bin/env python3
"""Recompute the private 102.4T power-to-cost sensitivity tables.

This is intentionally narrow: it checks arithmetic and the stated boundary,
not whether the scenario assumptions are market facts.  The sensitivity remains
illustrative until the wider TCO gate has matched product inputs.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "08-model/tco-power-cost-sensitivity.md"
HOURS = 8_760
UTILISATION = 0.80
PRICES = {"$0.08/kWh": 0.08, "$0.12/kWh": 0.12, "$0.20/kWh": 0.20}


def number(value: str) -> float:
    return float(value.replace(",", "").replace("$", "").replace("W", "").replace("kWh", "").strip())


def close(actual: float, expected: float, tolerance: float = 1.0) -> bool:
    return abs(actual - expected) <= tolerance


def main() -> None:
    text = PATH.read_text()
    failures: list[str] = []

    if "Illustrative operating-cost sensitivity; not a TCO forecast" not in text:
        failures.append("missing illustrative-scenario boundary")
    if "TCO per delivered bit = not yet calculable" not in (ROOT / "08-model/tco-per-delivered-bit-gate.md").read_text():
        failures.append("TCO gate no longer preserves not-yet-calculable control")

    rows = re.findall(
        r"^\|\s*(CPO|LPO|Fully retimed)\s*\|\s*([\d,.]+) W\s*\|\s*([\d,.]+) kWh\s*\|\s*\$([\d,.]+)\s*\|\s*\$([\d,.]+)\s*\|\s*\$([\d,.]+)\s*\|$",
        text,
        re.MULTILINE,
    )
    if len(rows) != 3:
        failures.append(f"expected three annual-energy rows, found {len(rows)}")
    else:
        for architecture, watts, kwh, low, central, high in rows:
            watts_value = number(watts)
            expected_kwh = watts_value / 1_000 * HOURS * UTILISATION
            reported_kwh = number(kwh)
            if not close(reported_kwh, expected_kwh):
                failures.append(f"{architecture}: annual kWh {reported_kwh} != {expected_kwh:.2f}")
            for label, reported in zip(PRICES, (low, central, high)):
                expected_cost = expected_kwh * PRICES[label]
                if not close(number(reported), expected_cost):
                    failures.append(f"{architecture}: {label} cost {reported} != {expected_cost:.2f}")

    savings = re.findall(
        r"^\|\s*(LPO|Fully retimed)\s*\|\s*([\d,.]+) W\s*\|\s*([\d,.]+) kWh\s*\|\s*\$([\d,.]+)\s*\|\s*\$([\d,.]+)\s*\|\s*\$([\d,.]+)\s*\|\s*\$([\d,.]+)\s*\|$",
        text,
        re.MULTILINE,
    )
    if len(savings) != 2:
        failures.append(f"expected two savings rows, found {len(savings)}")
    else:
        for architecture, delta_watts, kwh, low, central, high, five_year in savings:
            expected_kwh = number(delta_watts) / 1_000 * HOURS * UTILISATION
            if not close(number(kwh), expected_kwh):
                failures.append(f"{architecture}: annual saving kWh does not match delta watts")
            for label, reported in zip(PRICES, (low, central, high)):
                if not close(number(reported), expected_kwh * PRICES[label]):
                    failures.append(f"{architecture}: {label} saving does not match stated power delta")
            if not close(number(five_year), expected_kwh * PRICES["$0.12/kWh"] * 5):
                failures.append(f"{architecture}: five-year saving does not match annual central-price saving")

    if failures:
        print("FAIL: TCO sensitivity validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: 102.4T power-to-cost arithmetic matches stated utilisation, hours and electricity-price assumptions.")


if __name__ == "__main__":
    main()
