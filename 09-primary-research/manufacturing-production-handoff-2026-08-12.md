# Manufacturing-to-model handoff — 12 August 2026

**Status:** Private evidence control; no production-readiness ranking
**Scope:** 200G/lane and 400G/lane scale-out optical engines and switch CPO

## Why this handoff exists

The retained evidence answers whether a process mechanism or test flow is
technically plausible. It does not answer whether a named engine can be
produced repeatedly, serviced in the field and sold at an attributable margin.
This handoff prevents research-vehicle results and supplier capability claims
from entering the economic model as production data.

The [12 August production-evidence rerun](manufacturing-production-evidence-rerun-2026-08-12.md)
reconfirms that production-oriented test infrastructure is not the same as a
product-matched production denominator.

## Gate-by-gate classification

| Stage | Strongest retained evidence | Evidence class | What can be concluded | Missing production denominator | Model treatment |
|---|---|---|---|---|---|
| Known-good die / incoming screen | IBM full-module test vehicles; Teradyne/ficonTEC wafer-probe routes (`PAP-035`, `CMP-052`) | Research vehicle / supplier capability | Pre-screening is a required control and can move defects earlier | Starts, screened units, false rejects/escapes, lot and revision | `Y_die` and test cost blocked; process requirement only |
| PIC / laser integration | PIC and external-light demonstrations; NVIDIA screening and late fibre-attach process claim; Lumentum component-level accelerated UHP-laser programme (`CMP-051`, `CMP-067`, `CMP-082`) | Product/process claim; supplier-reported device qualification | The architecture separates optical integration and light-source screening; a CPO-targeted external-laser supplier reports accelerated device-level qualification | Exact product, input count, stage yield, ELSFP/module configuration and qualified output | Component reliability signal only; `Y_laser`, module yield and warranty cost remain blocked |
| Fibre attach / connector | IBM/Intel fibre-array and ferrule test vehicles; detachable FAU concepts (`PAP-035`, `PAP-036`, `CMP-050`) | Research vehicle / design claim | Alignment, warpage, contamination and service boundary are material | Attempts, first-pass attach, recovery, scrap, cycle time and mating-life | `Y_attach`, rework and service cost blocked |
| Package / thermal assembly | Intel thermal-loss and delamination mitigation; IBM reflow/stress sequence (`PAP-035`, `PAP-036`) | Prototype / research vehicle | Process order and thermal exposure can create large loss mechanisms | Matched lot population, Cpk, accepted optical/electrical output and cross-site repeatability | Process-risk flag only; no package yield |
| Wafer / engine / package test | Teradyne multi-insertion test flow; Photon 100’s wafer → engine/package → CPO-module insertion map; IBM optical/electrical characterization (`CMP-049`, `CMP-084`, `PAP-035`) | Supplier capability / research vehicle | Multiple test insertion points are necessary and late discovery can be costly | Seconds, coverage, utilization, escapes, retest and cost per accepted engine | `Y_test` and `C_test` blocked |
| Burn-in / qualification | Aehr wafer-level burn-in order; IBM JEDEC stress sequence; Lumentum UHP accelerated-test summary (`CMP-056`, `PAP-035`, `CMP-082`) | Supplier signal / research vehicle / supplier-reported component test | Burn-in and environmental qualification are identifiable gates; a laser supplier reports a bounded accelerated-device result | Named module/system, raw sample/lot distribution, stress profile, pass/fail, field FIT and failure disposition | Reliability reserve and acceptance yield blocked |
| Rework / scrap | IBM process iterations; Intel failure analysis (`PAP-035`, `PAP-036`) | Research vehicle | Defects can be diagnosed and process levers exist | Recovery fraction, labour/equipment time, salvage and post-rework reliability | `R_rework` and `C_rework` blocked |
| Customer acceptance / field service | Dell warranty policy; historical Broadcom/Meta lab evidence (`CMP-058`, `CMP-063`, `CMP-064`) | Policy / historical adjacent boundary | Service and reliability must be treated as separate economic domains | Exact CPO SKU, exposure hours, returns, MTTR, spares and warranty reserve | `W`, MTTR and field FIT blocked |
| Supplier economics | NVIDIA route map; Lumentum, Coherent, TSMC and connector/OSAT signals | Route / broad commercial disclosure | Candidate control points can be mapped | Exact SKU allocation, share, ASP, price-down, margin and capex | `P`, `Q`, `M`, `R`, `C` blocked |

## Unlock rule

No manufacturing value enters the company model until a single product-matched
record supplies:

```text
lot/date/revision → starts → screened → attached/packaged
→ final-test pass → rework disposition → accepted/shipped
→ field exposure/returns → attributable cost and price
```

A numerator without its denominator is not a yield. A process capability claim
without a product identity is not supplier share. A warranty policy without
field exposure is not a failure rate. A complete-engine ASP without a layer
map is not attributable PIC, laser, package or test revenue.

## Current decision

The public record supports a plausible manufacturing pathway and identifies the
critical cost and service failure modes. It does not establish a production
cost leader, final-engine yield leader or CPO profit-pool leader. The private
model therefore keeps all production yield, warranty, ASP, supplier-share and
product-margin cells **blocked**, while allowing labelled sensitivity analysis.

Related controls: [manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md), [production evidence boundary matrix](manufacturing-evidence-boundary-matrix-2026-08-12.md), [cost per qualified good engine](../08-model/manufacturing-cost-per-good-engine-gate.md), and [profit-pool input reconciliation](../08-model/profit-pool-input-reconciliation-2026-08-12.md).
