# NPO Interoperability and Serviceability Boundary

**Status:** Standards-direction review; not a measured technology or adoption comparison
**Last updated:** 2026-08-07

## Core distinction

NPO is not merely “lighter CPO.” Its potential economic role is to place a **replaceable** optical module close enough to the host ASIC to shorten the electrical path, while retaining an exposed electrical interface that can be standardized and supplied across vendors.

Huawei’s May 2026 IEEE 400GPL contribution presents exactly this view: CPO has no exposed interoperable host-to-engine electrical boundary, while an NPO module does and therefore could need a new ultra-short attachment-unit interface.[CLM-091]

## What the proposal establishes

| Item | Evidence-supported conclusion | What remains unproven |
|---|---|---|
| Electrical boundary | The contribution proposes a short-reach host-to-NPO electrical interface and optional one-, two- and four-lane 400G objectives. [CLM-091] | Loss budget, signalling, test method, compliance points and deployed performance. |
| Interoperability | NPO has a plausible interoperable/module-replacement boundary that CPO lacks. [CLM-091] | A ratified IEEE interface, compatible products, actual multisourcing or interoperability. |
| Architecture motivation | The authors frame retimed pluggables, LPO and CPO as having distinct power/reach/serviceability trade-offs. [CLM-092] | A matched, measured FPP/LPO/NPO/CPO total-cost or reliability ranking. |

## Investment implication

NPO is a serious **CPO deferral** risk whenever a short-channel module can deliver the required lane rate, cooling and density while preserving replacement and multi-vendor benefits. It becomes a CPO complement rather than a substitute if the electrical path, thermal environment or package density still demands optical engines tightly integrated with the ASIC.

Neither outcome is proven by the standards contribution. The customer decision must be tested at a common boundary:

```text
same ASIC and lane rate
same switch/XPU topology and port count
same electrical channel and connector assumptions
same reach, BER/FEC, cooling, service and spare policy
all-in module/engine, installation and repair cost
```

## Required evidence before changing the adoption model

1. IEEE task-force adoption or another ratified/open NPO interface, not a single-company proposal.
2. A measured 400G-per-lane NPO electrical/optical system at a stated loss, return-loss, thermal and error-rate boundary.
3. Demonstrated replaceability, qualification, failure isolation and repair time.
4. Qualified multi-vendor host and NPO-module availability.
5. A matched NPO-versus-CPO total-cost model including yields, cooling, spares and capex.

## References

- Guangcan Mi and Xiang He, [*How NPO May Fit in IEEE 400GPL*](../01-sources/standards/STD-005-ieee-400gpl-npo-fit-2026.pdf), IEEE 400GPL Study Group contribution, May 2026.
- [Linear-Drive Boundary Benchmark](linear-drive-boundary-benchmark.md).
- [CPO Adoption Timeline Model](../08-model/adoption-timeline.md).
- [Claim ledger](../01-sources/claim-ledger.csv), CLM-091 and CLM-092.
