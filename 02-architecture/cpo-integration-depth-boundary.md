# CPO Integration-Depth Boundary

**Status:** Architecture diligence rule; not a power ranking

**Scope:** Switch-side CPO, NPO and optical-I/O implementations

**Last updated:** 2026-08-07

## Decision question

When does co-packaging produce a real system-power and profit-pool advantage, rather than merely moving a conventional electrical interface closer to the host?

## Core rule

> Do not compare products merely because both are called CPO. First map which functions remain on each side of the electrical boundary: host SerDes/DSP, driver, TIA, clock/data recovery, optical modulation/detection, laser control, thermal tuning and external-light management.

`PAP-001` argues that a CPO architecture retaining a conventional electrical-interface boundary can leave high-energy functions on both sides of it. That is a useful diligence mechanism, not a measured universal result. The actual outcome depends on the function split, lane rate, process node, electrical reach, loss budget and optical-engine architecture.

## Evidence boundary

| Architecture label | What it can establish | What it cannot establish alone |
|---|---|---|
| LPO | Linear electrical drive at the module/engine boundary | A CPO-like system-power result outside its qualified channel-loss and return-loss boundary |
| NPO | A nearer, potentially replaceable optics boundary | A ratified interoperable interface, complete service economics or deeper host/engine co-design |
| Socketed CPO | A separately testable, potentially replaceable engine boundary | That socketability removes fibre-attach, thermal, yield or field-service risk |
| CPO with conventional CEI/XSR boundary | A shortened electrical path and possible lower loss/power | Elimination of duplicated/equalisation functions or a complete system-power advantage |
| Deep electronic–photonic integration | Potentially fewer parasitics and fewer boundary functions | Production yield, testability, thermal reliability, repairability or economic superiority |

## External-light sensitivity: a specific example, not a product metric

`PAP-001` models a 102.4T WDM configuration with sixteen 6.4T tiles. Under its specified link-budget assumptions, each ELS package requires 21.8 dBm output, 24.5 dBm laser-chip output and approximately 18 W; the model therefore totals 288 W for sixteen ELS packages.

This number is useful because it makes the laser, TEC, splitter and loss budget visible. It is **not** an input to the current 102.4T power model and must not be treated as a current vendor result. The paper assumes a 0.2-dBm TP2 target, 21.6-dB SiPh loss, 30% laser wall-plug efficiency, its stated coupling/fibre losses and its own CWDM4 distribution scheme. A current 200G- or 400G-per-lane engine can differ materially.

## Required reconciliation for every power claim

1. Is host SerDes power included? If yes, identify the electrical reach and equalisation.
2. Are driver, TIA, CDR, DSP/FEC, laser control and thermal tuning included?
3. Is external laser electrical input included, and are TEC, splitter, fibre-distribution and optical-loss assumptions stated?
4. Does the comparison use equal aggregate bandwidth, port count, lane rate, reach, BER/FEC, ambient/cooling and optical attach rate?
5. Is the engine socketed, field-replaceable, or inseparable from the host package?
6. Does the claimed benefit survive final-engine yield, test, rework, warranty and capital cost?

## Investment implication

The value pool cannot be assigned from an integration label. A supplier earns durable profit only if its chosen boundary yields a better **qualified total cost**, not simply a shorter electrical trace. Deeper integration may create valuable IP and lower energy, but can also shift yield, test, repair and warranty risk toward the supplier or platform owner. The investment model must therefore pair any power claim with the manufacturing and serviceability gates in [CPO Packaging, Fibre-Attach and Serviceability Benchmark](../03-components/packaging-reliability-benchmark.md) and [External-Light Serviceability Boundary](../03-components/external-light-serviceability-boundary.md).

## Source

- `PAP-001`: Min Tan et al., [*Co-packaged optics (CPO): status, challenges, and solutions*](../01-sources/papers/PAP-001-tan-cpo-status-challenges-solutions-2023.pdf), *Frontiers of Optoelectronics* 16, 2023, DOI `10.1007/s12200-022-00055-y`. Review source and author architecture view; all numerical ELS values above are its stated illustrative model, not observed product data.
