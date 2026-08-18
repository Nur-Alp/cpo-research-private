# Manufacturing evidence boundary matrix — production proof status

**Status:** Private acquisition control; not a production-readiness score
**As of:** 2026-08-12
**Scope:** Scale-out optical engines and switch-side CPO

See the [manufacturing-to-model handoff](manufacturing-production-handoff-2026-08-12.md)
for the single production-denominator rule and stage-by-stage model treatment.

This matrix is the handoff between retained engineering evidence and the
commercial model. “Development” and “engineering” records identify a process
or failure mechanism; they do not unlock a production input. A field becomes
model-eligible only when the record is matched to the named product boundary
and includes a numerator, denominator, date/lot and disposition rule.

| Boundary | Retained evidence | Boundary classification | What it proves | What remains missing | Model treatment | Next decision-changing record |
|---|---|---|---|---|---|---|
| PIC / engine yield | imec interface and coupler development runs (`PAP-043`, `CLM-421`–`CLM-423`); IBM full-module test vehicles (`PAP-042`, `CLM-479`–`CLM-482`) | Development / research vehicle | Coupling geometry, voids, warpage and known-good-component testing are material controls | Product-matched starts, stage yields, escapes, lot distribution and final accepted-engine denominator | `Y_die`, `Y_engine`: **blocked**; sensitivity only | Named 200G/lane engine lot record with starts → accepted engines |
| Fibre attach | Fibre-attach experiments (`PAP-015`); Intel prototype FAU/edge controls (`PAP-036`, `CLM-491`–`CLM-494`) | Development / prototype | Fibre count, edge quality, warpage and contamination can drive attach risk | First-pass attach, recovery, scrap, cycle time, alignment tolerance and lot/site | `Y_attach`, `R_rework`, `C_attach`: **blocked** | Production attach-control report with attempts, recoveries and scrap |
| Package / thermal assembly | Intel thermal-flow loss and mitigation (`PAP-036`, `CLM-492`–`CLM-494`); IBM reflow sequence (`PAP-042`, `CLM-480`–`CLM-482`) | Prototype / research vehicle | Thermal exposure and reflow sequence can create delamination and package loss | Matched production population, Cpk, cross-site repeatability, accepted optical/electrical output and cost | `Y_pkg`, thermal reserve: **blocked**; process-risk flag only | OSAT qualification or production record tied to exact CPO engine |
| Test / known-good die | Teradyne/ficonTEC wafer-probe and production-test routes (`CMP-049`, `CMP-052`, `CLM-393`–`CLM-396`, `CLM-432`–`CLM-434`) | Supplier capability / route | Wafer-level and multi-insertion test can be integrated into the flow | Customer/product identity, test seconds, coverage, utilization, escapes and cost per good unit | `Y_test`, `C_test`: **blocked** | Customer installation or test report with throughput and coverage denominator |
| Burn-in / qualification | Aehr wafer-level burn-in order (`CMP-056`, `CLM-518`); IBM JEDEC stress sequence (`PAP-042`, `CLM-479`–`CLM-482`) | Supplier signal / research vehicle | Burn-in and environmental qualification are identifiable process gates | Named product, sample population, conditions, pass/fail distribution, FIT and failure modes | `Y_accept`, reliability reserve: **blocked** | Product qualification report with lot/revision and pass/fail results |
| Rework / scrap | IBM process iterations (`PAP-042`, `CLM-479`–`CLM-482`); Intel failure analysis (`PAP-036`) | Research / prototype | Failure analysis can identify preventable defects and process levers | Recovery fraction, labour/equipment time, salvage, scrap and post-rework reliability | `R_rework`, `C_rework`: **blocked** | Production disposition log tied to the same engine lot |
| Detachable service boundary | Lightmatter detachable FAU / known-good engine route (`CMP-050`, `CLM-401`–`CLM-405`) | Company design claim | A service boundary can isolate some light-source or interface failures | Installed-base exposure, MTTR, spare ratio, returned-unit disposition and warranty ownership | Service model: **scenario only** | Field-service record for a named CPO SKU |
| Field reliability / warranty | Historical Broadcom TH5 reliability and Meta lab evidence (`CMP-063`, `CMP-064`, `CLM-532`–`CLM-533`); Dell warranty policy (`CMP-058`, `CLM-520`) | Historical / policy, not TH6 field data | Reliability testing and warranty boundaries exist as concepts | TH6/Spectrum-X field returns, exposure hours, failure modes, repairs and reserve | `W`, MTTR, field FIT: **blocked** | Named CPO fleet service or warranty disclosure |
| Supplier economics | Lumentum laser route (`CMP-067`), SENKO connector route (`CMP-068`), Coherent capacity agreement (`CMP-069`) | Route / broad commercial disclosure | Candidate supplier roles and capacity relationships are identifiable | Exact SKU allocation, qualified share, ASP, price-down, warranty/capex allocation and product margin | `P`, `Q`, `M`, supplier share: **blocked** | Attributable contract, filing or product-specific supplier disclosure |

## Current interpretation

The strongest retained evidence is process and qualification evidence, not
high-volume manufacturing evidence. IBM's full-module test vehicles make the
known-good, reflow and JEDEC boundaries concrete. Intel's prototype makes
thermal-loss and delamination mechanisms concrete. NVIDIA's “100% yield”
language is insertion-point/denominator bounded, and Broadcom's device-hour
and Meta material is historical TH5/lab evidence rather than TH6 field data.
None clears the complete chain:

```text
starts → screened components → attached/packaged engines → final-test pass
→ rework recovery → accepted/shipped units → field returns and warranty
```

Accordingly, all production-yield, warranty, ASP, supplier-share and
product-margin inputs remain **open/blocked**, not zero. The private model may
use labelled ranges for sensitivity analysis, but no company-specific profit
leader can be promoted until a matched record supplies the missing denominators.

## Release control

This matrix is private and must not be copied into the public Quarto report.
Public output may state the evidence gap and cite the original public source,
but must not expose private source archives, analyst material, or unverified
production numbers.

## Related controls

- [Manufacturing production-evidence checklist](manufacturing-production-evidence-checklist.md)
- [Manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md)
- [Manufacturing-economics evidence review](manufacturing-economics-evidence-review-2026-08-11.md)
- [Cost-per-qualified-good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
