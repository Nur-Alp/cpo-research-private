# Manufacturing proof matrix — what is demonstrated versus what remains commercial risk

**Status:** Evidence-boundary control; not a production-readiness scorecard  
**Scope:** Scale-out optical engines and switch-side CPO  
**As of:** 2026-08-12

The [manufacturing-to-model handoff](../09-primary-research/manufacturing-production-handoff-2026-08-12.md)
is the controlling classification for research-vehicle, supplier-capability,
product-claim and production-proof evidence.

## Purpose

The manufacturing question is not whether an individual package, coupler or test flow can work. It is whether a defined engine can be built, screened, qualified, serviced and accepted repeatedly at a cost that leaves an attributable margin. This matrix prevents a demonstrated process mechanism from being entered as a production yield, warranty or profit-pool input.

## Evidence-matched manufacturing proof

| Manufacturing gate | What the retained full papers demonstrate | What the demonstration does **not** demonstrate | Current model treatment |
|---|---|---|---|
| Incoming-component inspection / known-good boundary | IBM's full-module test vehicles used component inspection or sampling to target specifications; both assembly sequences include a test step, and the authors state that pre-tested known-good die and components are important for high yield (`PAP-035`, pp. 4–6; `CLM-479`–`CLM-482`). | Screen coverage, false pass/fail, screened-component denominator, escape rate, final-engine yield or customer acceptance. | Keep `Y_die` and `Y_test` blank. Treat known-good testing as a required insertion point, not a yield value. |
| Fibre attach and edge quality | IBM assembled 12-channel PIC-to-polymer-waveguide-to-ferrule links at 50-µm PIC/PWG pitch in two assembly orders. Intel's prototype uses three fibre-array units and 56 couplers at 127-µm pitch; it identifies die-edge quality, PIC front-edge warpage, strain relief and contamination as fibre-attach controls (`PAP-035`, pp. 5–8; `PAP-036`, pp. 1–5; `CLM-491`). | Attach first-pass yield, alignment-time distribution, rework recovery, connector contamination rate, fibre-attach lifetime or cost per accepted engine. | Keep `Y_attach`, rework and connector/service costs blank. Use fibre count only in labelled sensitivities. |
| Package/thermal process window | Intel observed approximately 50% substrate loss in a solder-temperature pre-screen and approximately 90% cumulative loss after the earlier thermal-compression/attach route. After process optimisation reduced thermal exposure, the paper reports no delamination in that prototype flow and no additional delamination at the subsequent lid/ball steps (`PAP-036`, p. 5; `CLM-492`–`CLM-494`). | A production-lot yield, matched before/after sample denominators, process capability, cross-site reproducibility, full optical/electrical acceptance or product cost. | Record as a process-specific loss-and-mitigation signal, never as a generic CPO package yield. |
| Reflow / stress qualification | IBM reports one-to-three lead-free reflow cycles, pre-bake and JEDEC stress: −40°C to +125°C cycling up to 1,000 cycles, 85°C/85% RH up to 1,000 hours, low-temperature storage and high-temperature storage. It reports iterative process learning before later test vehicles met the stated stress boundary (`PAP-035`, pp. 6–8; `CLM-480`–`CLM-482`). | Customer qualification lot, pass/fail population, burn-in duration/coverage, FIT, field return, warranty reserve or service cost. | The qualification gate remains open; do not turn stress exposure into a reliability rate or margin adjustment. |
| Rework and scrap | Intel shows failure analysis and thermal-profile optimisation can prevent one delamination mechanism before later assembly steps. IBM describes replacement/enhancement of materials and process iterations during test-vehicle learning (`PAP-035`, pp. 4–7; `PAP-036`, pp. 4–5). | A unit rework route, recovery fraction, labour/equipment time, salvage value, scrap cost or effect of rework on reliability. | `R_rework` and `C_rework` remain blank. A defect avoided in a prototype is not recovered production yield. |
| Final test, burn-in and shipped-unit quality | IBM reports optical/electrical characterisation on test vehicles before and after assembly, reflow and stress. Intel uses X-ray, acoustic microscopy, optical inspection and cross-sections to diagnose prototype package integrity (`PAP-035`, pp. 4–7; `PAP-036`, pp. 4–5). | Test seconds, coverage, escapes, equipment utilization, burn-in screen, final-test pass rate, accepted-unit denominator or shipment quality. | Keep `Y_test`, `Y_accept`, `C_test` and warranty cells blank. |
| Field service boundary | IBM's ferrule/lid construction and Intel's fibre-array-unit route show physical integration choices; they do not establish a customer service procedure (`PAP-035`, pp. 5–8; `PAP-036`, pp. 5–6). | MTTR, spares, returned-unit repair, connector wear, field failure distribution, warranty ownership or replacement cost. | Use the separate [service and failure-domain cost model](service-and-failure-domain-cost-model.md); do not credit a packaging route with service economics. |

## Translation matrix: evidence class to model eligibility

The same source can be highly useful for engineering diligence and still be
inadmissible as a financial input. This translation matrix is the required
handoff from the papers and company process disclosures into the private model.

| Evidence class | Example retained record | What may be concluded | Model treatment |
|---|---|---|---|
| Prototype process result | Intel thermal-flow loss and later delamination mitigation (`PAP-036`, `CLM-491`–`CLM-494`) | A specific assembly sequence has a demonstrated failure mode and a process lever that can reduce it | Use as a process-risk flag and diligence question; do not populate generic package yield or rework rate |
| Research test vehicle | IBM full-module reflow/JEDEC sequence and known-good-component workflow (`PAP-035`, `CLM-479`–`CLM-482`) | A test vehicle can expose optical/electrical and environmental qualification steps | Use to define required tests; do not infer customer qualification, burn-in cost, field FIT or accepted-engine yield |
| Interface/development yield | imec coupler or polymer-interface development-run percentages (`PAP-034`, `PAP-043`, `CLM-312`–`CLM-314`, `CLM-421`–`CLM-423`) | Coupling geometry, voids and warpage can materially affect yield | Use in architecture sensitivity only if unit, stage and denominator are retained; never transfer to final engine yield |
| Company process claim | NVIDIA known-good screening and “100% yield” wording (`CMP-051`, `CLM-406`–`CLM-410`) | Pre-screening and late fibre attach are part of the proposed production flow | Treat as a process hypothesis; keep `Y_die`, `Y_attach`, `Y_pkg`, `Y_test` and `Y_accept` blank |
| Product service boundary | Detachable FAU/ELSFP concepts (`CMP-050`, `CLM-401`–`CLM-405`; `CLM-076`–`CLM-077`) | Designers can isolate some optical/light-source failures from the fixed package | Use to define failure domains and service scenarios; do not assign MTTR, spare ratio, warranty or replacement cost |
| Production evidence | A named exact-SKU customer record with lot/acceptance and repeat shipment data | The physical and commercial denominator may be reconciled | Only this class can begin to populate `Y_accept`, `S`, repeatability and company-specific economics; supplier ASP/share and margin still require separate evidence |
| Production-screening demand | Aehr follow-on systems and FY2026 customer-ramp commentary (`CMP-080`, `FIL-016`, `CLM-549`, `CLM-562`) | Wafer-level screening capacity is being expanded for unnamed silicon-photonics customer programmes | Use as a capacity-ramp watchlist only; it cannot populate yield, test cost, output, customer acceptance or supplier economics |

### Hard handoff rule

No prototype, test-vehicle, development-yield, company process, or product
service statement can populate a production yield, warranty, ASP or margin
cell by itself. The model may use those records to define what must be measured
and to run labelled sensitivities, but the commercial bridge remains blocked
until the same product boundary supplies stage denominators and customer
acceptance.

## Decision rule

For any named company or architecture, a manufacturing-profit conclusion requires a matched record for **all** of these at the same engine boundary:

```text
starts → screened components → assembled engines → final-test pass
→ rework recovery → customer-accepted / shipped units → field returns
```

The record must state denominators, lot/date, operating and qualification conditions, failure disposition, test time and attributable cost boundary. The retained IBM and Intel work is strong technical evidence that these controls exist and can be engineered; it is not evidence that any supplier has cleared the chain above in production.

## Links

- [Production evidence boundary matrix](../09-primary-research/manufacturing-evidence-boundary-matrix-2026-08-12.md)
- [Manufacturing-economics evidence review](../09-primary-research/manufacturing-economics-evidence-review-2026-08-11.md)
- [Cost per qualified good optical engine](manufacturing-cost-per-good-engine-gate.md)
- [Yield-claim reconciliation](yield-claim-reconciliation.md)
- [Service and failure-domain cost model](service-and-failure-domain-cost-model.md)
- [Packaging, fibre-attach and serviceability benchmark](../03-components/packaging-reliability-benchmark.md)
