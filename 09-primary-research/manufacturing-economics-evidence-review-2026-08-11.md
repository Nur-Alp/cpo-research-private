# Manufacturing-economics evidence review — 11 August 2026

**Status:** Private negative-evidence review; no forecast, publication or investment ranking implied  
**Decision question:** Does the public record support a credible cost-per-qualified-engine or packaging-profit conclusion for 200G/lane-and-later scale-out CPO?

## Result

**No.** The retained record establishes credible *process mechanisms*—known-good testing, detachable interfaces, wafer-level test and burn-in routes, reflow/thermal qualification approaches, and bounded loss measurements. It does not disclose the commercial manufacturing chain required to calculate the cost of a good engine or identify who retains its margin.

The model therefore remains blocked for every company. A supplier cannot be ranked on PIC energy, best-channel loss, a trade-show design, a capacity announcement, consolidated gross margin, or a general statement that “rework is difficult.”

## Gate-by-gate audit

| Required economic field | Strongest retained evidence | What it proves | Missing decisive evidence | Status |
|---|---|---|---|---|
| Exact engine / system boundary | TH6-Davisson has 16 × 6.4T engines; Spectrum-X SN6810 has 32 × 3.2T engines (`CLM-076`, `CLM-515`) | Content denominators exist for two platform architectures | Actual CPO deployment configuration and a product-matched engine BOM | Partial, not economic |
| Good-die / attach / package / final-test yield | NVIDIA’s screening language; imec development runs; IBM full-module test vehicles (`CLM-406`–`CLM-410`, `CLM-421`–`CLM-423`, `CLM-479`–`CLM-482`) | Screening, development yield and reliability mechanisms exist | Lot-level stage yields, correlation, process capability, accepted-engine numerator | Open |
| Rework and scrap recovery | OIF connection-count sensitivity; detachable/known-good concepts (`CLM-397`–`CLM-400`, `CLM-401`–`CLM-405`) | Rework and early screening are structurally material | Recovery fraction, labour/equipment time, salvage value and scrap cost | Open |
| Test / burn-in throughput | Teradyne/ficonTEC production-test announcement and Aehr capacity signal (`CLM-432`–`CLM-434`, `CLM-518`) | Equipment routes exist for wafer-level and multi-insertion testing | Customer installation, test seconds, coverage, escape rate, utilization and cost per good die/engine | Open |
| Qualification / reliability | IBM’s OTV and stated JEDEC stress sequence (`CLM-357`–`CLM-359`, `CLM-479`–`CLM-482`) | A full-module research reliability boundary is inspectable | Sample/pass-fail distributions, production qualification, field failures and warranty reserve | Open |
| Service / replacement | ELSFP and detachable optical routes (`CLM-077`, `CLM-237`, `CLM-401`–`CLM-405`) | Serviceability architecture can be designed | Engine replacement workflow, MTTR, spares, returned-unit disposition and service cost | Open |
| Revenue / share / ASP / margin | Platform and component routes; public consolidated financial baselines | Candidate control points and corporate capacity are known | Product-specific contract price, qualified share, gross margin, price-down and cancellation terms | Open |

## Evidence-quality exclusions

The review tested fresh public search results for an actual production-yield or return-cost numerator. None met the source standard.

| Excluded lead category | Why excluded from the model |
|---|---|
| General CPO explainers and vendor testing overviews | Restate known engineering constraints but do not reveal a named product, measured production denominator, method or economic boundary. |
| Secondary numerical yield claims without primary lot data | A percentage without a defined engine, denominator, date, method, sample population and primary record cannot enter an evidence-gated model. |
| Trade-show and product-capability announcements | Can identify a diligence lead, but do not establish a qualified design win, volume, yield, price or margin. |
| Unattributed market rumours of CPO units, ASP or margins | Cannot clear customer, supplier-share or profit-capture gates; they must not be used as scenario facts. |

## What would change the decision

The first decision-changing source should be a customer, platform owner, OSAT, engine supplier or test-equipment user record that supplies **at least one measured numerator and its denominator** at the same physical boundary. Examples:

1. final accepted optical-engine yield, first-pass yield and rework recovery by a defined lot/process;
2. automated attach/test cycle time and test coverage, plus a throughput or utilization denominator;
3. qualification sample population, conditions, pass/fail results and failure analysis;
4. field-return, repair/replace, MTTR or warranty-reserve data for a named CPO SKU; or
5. a supplier/customer contract or filing with CPO-specific content, price, share and margin boundary.

Until then, all yield, rework, warranty, ASP and product-margin cells remain **blank/blocked**, not zero and not implicit assumptions. The scenario bridge may illustrate arithmetic only after inputs are visibly labelled as assumptions; it cannot produce a company forecast.

## Full-paper cross-check — IBM and Intel

The retained full papers were re-read page by page on 12 August. IBM's `PAP-035` makes the known-good/test boundary more concrete than its abstract: the two module sequences contain inspection and test steps, and the paper says pre-tested known-good die and components are important for high yield. It also demonstrates one-to-three reflows and a JEDEC test-vehicle sequence. It does **not** quantify screen coverage, escapes, final-test yield, rework recovery, burn-in throughput or accepted units (`CLM-479`–`CLM-482`).

Intel's `PAP-036` makes the thermal-yield boundary more concrete: its prototype reports roughly 50% pre-screen substrate loss and roughly 90% cumulative loss in an earlier thermal flow, then reports no delamination after lower-thermal-exposure process optimisation. This is useful failure-analysis and process-window evidence, but its paper supplies neither matched lot denominators nor a production yield, complete-link acceptance, rework rate, customer qualification or cost record (`CLM-491`–`CLM-494`). The detailed separation is maintained in the [manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md).

## Controls updated by this review

- [Manufacturing production-evidence checklist](manufacturing-production-evidence-checklist.md)
- [Cost-per-qualified-good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md)
- [Optical-engine yield-waterfall template](../08-model/engine-yield-waterfall-template.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [Evidence gate register](../08-model/evidence-gate-register.md)
- [Manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md)
