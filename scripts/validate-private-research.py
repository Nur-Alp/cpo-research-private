#!/usr/bin/env python3
"""Run every current private CPO evidence-control check.

Use this before a research handoff or any future publication review.  It does
not render or publish public Quarto output.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    "audit_evidence.py",
    "validate-commercial-proof-dossiers.py",
    "validate-supplier-content-map.py",
    "validate-private-decision-layer.py",
    "validate-quarterly-review.py",
    "validate-economic-gates.py",
    "validate-analyst-estimate-boundary.py",
    "validate-manufacturing-boundaries.py",
    "validate-architecture-boundary.py",
    "validate-tco-sensitivity.py",
    "validate-profit-pool-sensitivity.py",
    "audit-commercial-proof-readiness.py",
)


def main() -> None:
    for check in CHECKS:
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / check)], cwd=ROOT)
        if result.returncode:
            sys.exit(result.returncode)
    print("PASS: all private CPO evidence, decision, economics and architecture controls passed.")


if __name__ == "__main__":
    main()
