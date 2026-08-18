# Manufacturing production-evidence checklist

**Status:** Private acquisition specification; no production claim implied  
**As of:** 2026-08-12  
**Purpose:** Define the minimum records needed to move from engineering/process evidence to a cost-per-qualified-good-engine model input.

## Required evidence bundle

One record does not need to answer every field, but every populated model input must be traceable to a product-matched record. The preferred boundary is a named 200G/lane switch-CPO engine or a directly separable PIC/laser/package subassembly.

| Gate | Required numerator | Required denominator and metadata | Minimum source quality | Model input unlocked only after match |
|---|---|---|---|---|
| Incoming / known-good screening | Passed and failed components by stage | Starts, screened units, lot/site/date, screen criteria and escape definition | Customer qualification, OSAT/test report or supplier production record | `Y_die`, `Y_laser`, `Y_screen` |
| Fibre attach | First-pass attaches, rework recoveries and scrap | Attach attempts, fibre/FAU count, cycle time, alignment tolerance, lot/date and operator/automation boundary | Production process-control report or customer qualification packet | `Y_attach`, `R_rework`, `C_attach` |
| Package / thermal assembly | Accepted packages after assembly and thermal/reflow steps | Packages started, process sequence, reflow/thermal conditions, failure disposition and site/date | OSAT production/qualification record | `Y_pkg`, thermal/rework cost |
| Optical/electrical final test | Pass, fail, retest and escape counts | Engines tested, test seconds, coverage, fixtures, limits, retest rules and lot/date | Test-equipment deployment record tied to product or customer | `Y_test`, `C_test` |
| Burn-in / qualification | Pass/fail and failure modes | Sample population, duration, temperature/humidity/cycling conditions, lot and revision | Customer qualification, reliability report or filing | `Y_accept`, reliability reserve |
| Customer acceptance / shipment | Accepted or shipped engines/systems | Exact SKU, customer, date/period, units/ports, repeat shipment and topology | Customer/OEM/operator statement, filing or procurement record | `S`, `A`, repeatability |
| Field service | Returns, repairs, replacements and MTTR | Installed base, exposure hours, failure mode, spare pool, repair boundary and warranty period | Service report, warranty filing or customer fleet data | `W`, MTTR/service cost |
| Economics | Supplier price/share and realised margin | Contract/product boundary, ASP, price-down, second source, warranty/capex allocation and fiscal period | Product filing, contract disclosure or attributable primary supply-chain record | `P`, `Q`, `M`, `C`, `R` |

## Rejection rules

Do not populate a production input from:

- a best-channel result without a lot distribution;
- a development-run percentage without stage and denominator;
- a “100% yield” statement without insertion point, escapes and final-acceptance denominator;
- a stress-test duration without sample population and pass/fail result;
- a test-equipment order without customer/product identity and achieved throughput;
- a capacity reservation without exact CPO product allocation;
- a consolidated company margin without product-level allocation; or
- a partner quotation, demonstration, sample or roadmap without accepted units and repeatability.

## Current status

No retained public record clears the complete bundle for NVIDIA Spectrum-X Ethernet Photonics, Broadcom TH6-Davisson, Coherent, Lumentum, TSMC or Marvell. The correct state for all production-yield, warranty, ASP, supplier-share and product-margin inputs remains **open/blocked**, not zero.

Use the [production-record intake schema](production-record-intake-schema-2026-08-13.md)
when evaluating a new source. It requires the physical boundary, numerator,
denominator, conditions, rework disposition, time period and cost boundary in
one place before a claimed result can affect the private model.

See the [manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md), the [production evidence boundary matrix](manufacturing-evidence-boundary-matrix-2026-08-12.md), [yield reconciliation](../08-model/yield-claim-reconciliation.md), [cost-per-good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md), and [commercial-proof decision memo](../07-companies/commercial-proof-dossiers/commercial-proof-decision-memo.md).
