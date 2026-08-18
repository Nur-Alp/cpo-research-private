# CPO profit-pool input reconciliation

**Status:** Private control ledger; not a forecast or public evidence
**Owner:** Nur Alpys
**As of:** 2026-08-12
**Purpose:** Reconcile the layer sensitivity, profit-pool bridge and input-gate register at one product boundary.

## Decision boundary

The controlled unit is **one qualified 6.4-Tb/s-class optical engine (32 ×
200G lanes)** unless an exact product record states otherwise. The Broadcom
TH6-Davisson disclosure of sixteen engines is an architecture reference, not a
volume or price input. NVIDIA's 32-engine reference architecture is kept
separate from Broadcom's 16-engine architecture. A complete-engine supplier
must not also receive the same engine's PIC, laser, package or test value as a
second revenue line.

## Reconciled input ledger

| Layer / variable | Physical boundary | Current illustrative range or value | Source / claim anchor | Status | Overlap control | Evidence that unlocks a company input |
|---|---|---:|---|---|---|---|
| PIC / optical-engine design and assembly | PIC plus assembly only, or complete engine if explicitly sold as one unit | $250 / $500 / $900 per qualified engine | `engine-layer-sensitivity-ranges.md`; CLM-235, CLM-076 | Nur Alpys assumption; architecture facts are separate | If complete engine is priced here, remove PIC, package and test from other supplier revenue lines | Product BOM, transfer price, qualified share, final-engine yield, product margin |
| External laser / ELSFP | Detachable light source or ELSFP module, excluding PIC and package | $100 / $250 / $500 | CMP-016, CMP-018, CLM-071, CLM-076 | Nur Alpys assumption; product boundary observed, economics blocked | Count once as a laser-only boundary; do not add it to a complete-engine ASP | Exact laser count, SKU allocation, realised price, lifetime, warranty and supplier share |
| Fibre attach / connector / interposer / package | Physical coupling, attach, interposer and package process only | $75 / $200 / $350 | CMP-051, CMP-057, PAP-028, PAP-044 | Nur Alpys assumption; process routes observed, production economics blocked | Exclude PIC, laser, final test and platform assembly; assign pass-through separately | Named attach/OSAT role, cycle time, first-pass yield, rework, loss and margin |
| Test / burn-in / qualification | Test and qualification service/content per accepted engine | $25 / $75 / $150 | CMP-049, CMP-052, PAP-035, PAP-036 | Nur Alpys assumption; test need observed, cost blocked | Test revenue is not package revenue; do not infer accepted units from test capacity | Test seconds, coverage, escape rate, utilisation, burn-in burden, warranty allocation |
| Eligible content per engine | Sum of the four non-overlapping rows above | $450 / $1,025 / $1,900 | `engine-layer-sensitivity-ranges.md` | Derived scenario total, not ASP | Use only when every component is assigned one boundary and no complete-engine price is also used | Product-matched BOM and realised transfer prices for every layer |
| Relevant systems (`S`) | Annual systems in a defined SKU/domain | 10,000 in the harness | `profit-pool-scenario-bridge.md` | Nur Alpys denominator assumption | Never combine with a market-share estimate or another domain's denominator | Customer/manufacturer denominator and year |
| Adoption (`A`) | Share of `S` using the defined CPO architecture | 5% / 25% / 50% | `profit-pool-scenario-bridge.md` | Scenario assumption; no market-share claim | Must be tied to the same SKU and year as `S` | Customer production numerator plus denominator |
| Engines/system (`E`) | Optical engines in the exact product | 16 for TH6; 32 for NVIDIA reference | CLM-076, CLM-235 | Reported architecture fact, not volume | Select one exact SKU; never mix 16 and 32 in one case | Product architecture or teardown for the same SKU |
| Qualified supplier share (`Q`) | Portion of eligible content retained by the named supplier | 25% / 50% / 75% | `engine-layer-sensitivity-ranges.md` | Nur Alpys assumption; qualification blocked | Share applies to one boundary only, not to all layers automatically | Named qualification, repeat orders, second-source evidence |
| Product gross margin (`M`) | Margin on the defined supplied layer | 15% / 35% / 50% | `profit-pool-scenario-bridge.md` | Nur Alpys assumption; consolidated margins excluded | Never substitute company gross margin or segment margin | Product-level disclosure or directly comparable primary evidence |
| Yield / rework (`Y`) | Cost and loss between attempted and accepted good engine | $10 / $25 / $50 per supplied engine | `manufacturing-cost-per-good-engine-gate.md` | Scenario assumption; production yield blocked | Do not subtract yield twice: once in good-engine count and again as a full revenue loss | Lot-level yield waterfall, rework rate and cost per good engine |
| Warranty / support (`W`) | Field replacement and support burden per good engine | $8 / $15 / $30 | `profit-pool-scenario-bridge.md` | Scenario assumption; field data blocked | Keep separate from manufacturing rework and capex | Field returns, service contract and replacement records |
| Cannibalised legacy GP (`K`) | Gross profit displaced by legacy optics/DSP/AEC or other content | $5 / $10 / $25 | `profit-pool-scenario-bridge.md` | Scenario assumption; transition evidence blocked | Apply once per supplied engine; do not subtract from both revenue and margin | Product transition, price-down and displaced-content evidence |
| R&D / qualification (`R`) | Incremental operating expense attributable to the defined product | Not populated | `optical-engine-profit-pool-input-gates.md` | Blocked | Excluded from gross profit; subtracted only in operating-profit bridge | Filing or product-linked primary research |
| Attributable capex (`C`) | Incremental capacity, packaging, attach and test investment | Not populated | `optical-engine-profit-pool-input-gates.md` | Blocked | Excluded from gross profit and operating profit; subtracted only in cash bridge | Project-linked capex and capacity allocation |

## Arithmetic reconciliation

The three model documents must use the same identities:

```text
attempted engines = S × A × E
good engines = attempted engines × good-engine yield
supplied engines = good engines × Q
supplier revenue = supplied engines × eligible content per engine
gross profit = supplier revenue × M
              − supplied engines × (Y + W + K)
operating profit = gross profit − R
cash return = operating profit − C
```

The layer sensitivity uses the first four rows to construct an eligible-content
stress range. The scenario bridge uses a single `P` value for that boundary.
They are alternative views of the same content—not additive model branches.
When a product-specific complete-engine ASP becomes available, replace `P`
with that ASP and set the component rows to attribution-only; do not add the
component rows to `P` again.

## Current reconciliation result

- No company has a cleared `S`, `A`, `P`, `Q`, `M`, `Y`, `W`, `K`, `R` and `C`
  set for an exact switch-CPO product.
- Broadcom's 16-engine TH6 architecture and NVIDIA's 32-engine reference
  architecture are usable only as product-shape facts.
- All dollar ranges in the layer sensitivity and scenario bridge remain
  **Nur Alpys assumptions**. They are not analyst estimates, supplier quotes,
  observed ASPs, or company forecasts.
- The current conclusion therefore remains: **no proven CPO profit-pool
  leader**.

## Evidence replacement sequence

Replace assumptions in this order: exact SKU/customer denominator; exact
engine and service boundary; supplier qualification/share; realised price;
yield/rework/test; warranty and cannibalisation; product margin; attributable
R&D and capex. A later-stage record cannot cure an earlier missing denominator.

Related controls: [layer sensitivity ranges](engine-layer-sensitivity-ranges.md),
[profit-pool input gates](optical-engine-profit-pool-input-gates.md),
[scenario bridge](profit-pool-scenario-bridge.md), and [manufacturing cost per
qualified good engine](manufacturing-cost-per-good-engine-gate.md).
The denominator consistency check is recorded in the [profit-pool arithmetic
audit](profit-pool-arithmetic-audit-2026-08-12.md).

The [missing-input value-of-information register](missing-input-value-of-information.md)
is the controlling order for replacing assumptions. It converts the scenario
model's current output from a false-precision estimate into a ranked request
for the next decision-changing datum.
