#!/usr/bin/env python3
"""Validate layer-by-layer attribution for the switch-CPO supplier map."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "07-companies/six-company-content-attribution-register.md"
SKUS = ROOT / "08-model/switch-cpo-sku-content-reconciliation.md"
AUDIT = ROOT / "08-model/supplier-attribution-audit-2026-08-12.md"


def section(text: str, heading: str, next_heading: str) -> str:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    return text[start:end if end != -1 else None]


def require(text: str, phrase: str, label: str, failures: list[str]) -> None:
    if phrase not in text:
        failures.append(f"{label}: missing layer/control: {phrase}")


def main() -> None:
    failures: list[str] = []
    register = REGISTER.read_text()
    skus = SKUS.read_text()
    audit = AUDIT.read_text()

    nvidia = section(register, "## NVIDIA Spectrum-X Ethernet Photonics", "## Broadcom TH6-Davisson / BCM78919")
    broadcom = section(register, "## Broadcom TH6-Davisson / BCM78919", "## Coherent")

    for label, content, required_layers in (
        (
            "NVIDIA content map", nvidia,
            ("Switch ASIC / SerDes", "PIC / optical-engine fabrication", "EIC / driver / TIA",
             "Laser / external light", "Fibre attach", "Package", "Connector / service boundary", "Test"),
        ),
        (
            "Broadcom content map", broadcom,
            ("Switch ASIC / SerDes", "PIC / optical-engine", "EIC / driver / TIA",
             "Laser / external light", "Fibre attach / faceplate connectivity", "Package",
             "Connector / service boundary", "Test"),
        ),
    ):
        for layer in required_layers:
            require(content, layer, label, failures)
        for status in ("Confirmed", "Open"):
            require(content, status, label, failures)

    for phrase in (
        "Confirmed role", "Route / candidate", "Outside switch-CPO boundary",
        "Confirmed role” never means confirmed revenue, supplier share, ASP, final-engine yield or margin",
        "No company should be assigned CPO revenue, product gross margin or a profit-pool leadership score",
        "Cross-company layer control matrix", "Economic attribution",
        "NVIDIA Spectrum-X Ethernet Photonics", "Broadcom TH6-Davisson / `BCM78919`",
        "Coherent component/engine routes", "Lumentum external-light route",
        "TSMC COUPE process route", "Marvell / Celestial Photonic Fabric",
        "The economic column stays open for all six companies.",
    ):
        require(register, phrase, REGISTER.name, failures)

    for phrase in (
        "SN6810", "SN6800", "TH6-Davisson", "BCM78919", "Prohibited transfers",
        "Commercial-proof gate remains open for both.",
    ):
        require(skus, phrase, SKUS.name, failures)

    for phrase in (
        "Attribution-evidence hierarchy", "Exact product owner", "Product-linked route",
        "Family/technology route", "Demonstration / candidate", "Exact economic attribution",
        "Neither can\nbe promoted into exact-SKU supplier allocation or a model input.",
    ):
        require(audit, phrase, AUDIT.name, failures)

    if failures:
        print("FAIL: supplier-content attribution validation")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: NVIDIA and Broadcom switch-CPO maps retain every value-chain layer and economic-attribution boundary.")


if __name__ == "__main__":
    main()
