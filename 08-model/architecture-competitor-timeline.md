# Architecture competitor timeline — evidence states

**Status:** Private chronological comparison; not a market forecast  
**As of:** 2026-08-13  
**Purpose:** Compare CPO, LPO/RTLR, NPO/OBO and high-rate InP/TFLN modular routes by product/qualification/customer evidence rather than generic market forecasts.

## State labels

`0 concept`, `1 device/component`, `2 integrated system/demo`, `3 product/production claim`, `4 commercial proof` (exact customer, accepted denominator and repetition). A state is architecture/domain-specific and cannot transfer across lane rates or to a different product family.

| Architecture / boundary | Evidence sequence retained | Current state | What would advance it | What would weaken the CPO case |
|---|---|---:|---|---|
| Retimed/advanced pluggable, 102.4T Ethernet | 102.4T demos and RTLR standards-level hot-plug comparator | 2 | Qualified production with same-system power/service data | If modular 200G/400G systems meet electrical/power/service needs |
| LPO, 100G Ethernet | Measured 51.2T system and limited production-context evidence | 2–3 | Named customer, accepted denominator and repetition | If LPO preserves module service while closing power gap |
| LPO/RTLR, 200G Ethernet | Conditional models and defined RTLR interface | 1–2 | Measured complete system, qualification and customer use | If it meets 200G margin at acceptable power/service |
| NPO/OBO, 224G-class | Standards/framework and early route evidence | 0–1 | Qualified replaceable near-package product with interop/service record | If it delivers a lower-integration alternative to CPO |
| Switch CPO, 100G Ethernet | TH5 partner-reported production baseline | 3 | Exact customer/unit/repeat and field data | Historical state does not decide 200G economics |
| Switch CPO, 200G Ethernet | NVIDIA production route and Broadcom TH6 product/sampling route | 3 | Exact customer SKU, accepted numerator and repeat delivery | If signals resolve to samples, non-CPO or no repeatable service/yield |
| InP advanced pluggable, 400G/lane | TEC-less transmission demonstration at 500m / 20–80°C | 1 | Complete module power, qualification, customer product | If it qualifies at a modular boundary and narrows CPO need |
| TFLN advanced pluggable, 400G/lane | 225GBd/420.5Gb/s net-PAM4 transmission evidence | 1 | Qualified module/chassis and economic comparison | Same as above |

## Update rule

Only add an event when it changes one of: exact product definition, measured
system boundary, qualification, named customer, accepted denominator, repeat
delivery, or same-system alternative comparison. Record the date, source ID,
lane rate, topology, state before/after and unresolved fields. Do not use a
market forecast as an event.

Related controls: [adoption timeline](adoption-timeline.md), [common boundary scorecard](../02-architecture/system-boundary-comparison-scorecard.md), and [400G counterexample scorecard](400g-lane-counterexample-scorecard.md).
