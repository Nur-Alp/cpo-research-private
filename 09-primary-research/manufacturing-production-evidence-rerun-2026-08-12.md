# Manufacturing production-evidence rerun — 12 August 2026

**Status:** Private retrieval audit; no production or profit-pool upgrade
**Question:** Did the latest primary manufacturing/test records supply a
product-matched production denominator for scale-out optical engines or
switch-side CPO?

## Evidence reviewed

| Record | Boundary actually disclosed | What it adds | Why it does not clear production economics |
|---|---|---|---|
| Teradyne Photon 100 / `CMP-049` | Wafer, optical-engine and CPO-package test insertions; automated optical/electrical instrumentation | Confirms that scalable test architecture is being designed for high-volume SiPh/CPO workflows and identifies test time, alignment, thermal handling and coverage as cost gates | Supplier product positioning; no customer lot, test seconds, throughput, escape rate, yield, utilization or cost per accepted engine |
| Teradyne/ficonTEC double-sided probe system / `CMP-052` | Production-oriented wafer-probe cell for hybrid-bonded PIC/EIC wafers | Confirms a production-capable test-cell route exists and narrows the wafer-test control point | Availability announcement; no installed customer, measured wafer yield, Cpk, test time, utilization or downstream engine yield |
| IBM ECTC full-module vehicles / `PAP-035` | Reflow-compatible PIC/PWG/ferrule assemblies and JEDEC stress testing | Establishes relevant package, optical-link and environmental qualification mechanisms | Research vehicle; no exact CPO SKU, accepted-lot denominator, final-engine yield, field returns or cost |
| Intel CPO prototype / `PAP-036` | Thermal-flow loss, delamination mechanism and process mitigation | Establishes a concrete package-loss failure mode and process lever | Prototype-specific observations; no production population, cross-site repeatability, cost or customer qualification |
| TSMC COUPE / `PRI-030` | 200G modulation and greater-than-99% 3D-stacking yield on engineering samples; 2026 production milestone | Strengthens the process-control and packaging-readiness route | Yield boundary is engineering-sample 3D stacking, not complete optical-engine yield; no customer SKU, accepted output or economics |
| Aehr August 2026 follow-on order / `CMP-080` | Lead silicon-photonics customer ordered another nine-blade automated wafer-level burn-in system for production capacity expansion | Upgrades the evidence that production-scale SiPh reliability screening is being installed | Customer, optical product, CPO SKU, wafer starts, pass/fail, accepted output, utilisation and economics remain undisclosed |
| Aehr FY2026 results / `FIL-016` | Lead SiPh customer is described as ramping; an additional global networking customer forecasts more burn-in systems for hyperscale capacity | Independently reinforces that wafer-level SiPh screening demand is moving beyond a one-off equipment order | No customer, product architecture, SKU, wafer/test/output denominator, yield, cost or system-CPO linkage is disclosed |

## Required production denominator

No reviewed record supplies the full chain below for a named 200G/lane or
400G/lane product:

```text
lot/date/revision → starts → screened die → attached/packaged engines
→ final-test pass → rework disposition → customer-accepted units
→ field exposure/returns → attributable price and cost
```

Therefore the following model cells remain blocked:

- die, attach, package, test and final accepted-engine yield;
- test seconds, throughput, utilization, false rejects and escapes;
- rework recovery, scrap and post-rework reliability;
- burn-in/FIT, MTTR, spare ratio and warranty reserve;
- supplier ASP, share, price-down and product margin.

## Decision impact

The evidence upgrades the **manufacturing diligence map**, not the commercial
conclusion. Aehr's August follow-on order is a stronger production-scale
screening signal than a capability announcement, but it is still not a
product-matched CPO denominator. Production-oriented test infrastructure is a
necessary condition for scale; it is not evidence that NVIDIA
`SN6810-LD`/`SN6800-LD`, Broadcom `BCM78919`, or any supplier has achieved
repeatable profitable production.

The FY2026 Aehr result adds `FIL-016` / `CLM-562` as an independent capacity
direction check. It is still a negative/qualification audit, not evidence that
production data do not exist privately.

Related controls: [manufacturing-to-model handoff](manufacturing-production-handoff-2026-08-12.md), [production evidence boundary matrix](manufacturing-evidence-boundary-matrix-2026-08-12.md), [manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md), and [public-release manifest](../00-scope/public-release-manifest-2026-08-12.md).
