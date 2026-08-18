# CPO decision-output completion audit

**Owner:** Nur Alpys  
**Status:** In progress; completion is not claimed  
**Scope:** 2026–2032 CPO decision question, with the current workstream focused on scale-out optical engines/PICs  
**Last updated:** 2026-08-12

## Purpose

This audit tests whether the project has actually produced the twelve outputs required by [research-question.md](../00-scope/research-question.md). A framework, company announcement or source count is not sufficient evidence of completion. Each output needs a decision-ready artifact, traceable sources/claims, and explicit treatment of unresolved gates.

## Requirement-by-requirement status

| # | Required output | Authoritative artifact | Current status | What still prevents completion |
|---:|---|---|---|---|
| 1 | Architecture trigger matrix | [102.4T CPO vs advanced pluggables](../02-architecture/102.4t-cpo-vs-advanced-pluggables.md); [linear-drive boundary benchmark](../02-architecture/linear-drive-boundary-benchmark.md) | Partially complete | Matched 200G/lane and 400G/lane end-to-end measurements, reach, FEC, temperature, service and TCO remain incomplete. PAP-044 now supplies a full measured 400-Gbps optical-engine comparator, but not a matched 400G/lane CPO/LPO system. |
| 2 | Technical and commercial viability gates | [Evidence-gate register](evidence-gate-register.md); [critical-path milestone tracker](critical-path-milestone-tracker.md); [commercial-proof dossiers](../07-companies/commercial-proof-dossiers/README.md) | Partially complete | NVIDIA now has a disclosed `SN6800` / `SN6810` product boundary, but no architecture clears the full product, manufacturing, commercial and financial bundle. |
| 3 | Annual 2026–2032 probability-weighted adoption timeline | [Adoption timeline](adoption-timeline.md); [commercial-proof probability priors](commercial-proof-probability-priors.md) | Commercial-proof priors populated; adoption-share forecast incomplete | The binary commercial-proof event now has bounded analyst ranges, but system denominators, customer production numerators, qualification, yield, service economics and matched alternatives are still insufficient for adoption-share percentages. Secondary limited-volume reporting and TrendForce's corroborating press-center record do not clear the numerator (`NWS-011`, `NWS-012`, `CLM-411`–`CLM-420`). |
| 4 | Critical-path milestone tracker | [Critical-path milestone tracker](critical-path-milestone-tracker.md) | Partially complete | Milestones are defined, but most customer SKU, repeat shipment, yield and economics milestones remain open. |
| 5 | Manufacturing, yield, reliability and serviceability model | [Cost-per-qualified-good-engine gate](manufacturing-cost-per-good-engine-gate.md); [engine yield waterfall](engine-yield-waterfall-template.md); [yield-claim reconciliation](yield-claim-reconciliation.md); [service/failure-domain model](service-and-failure-domain-cost-model.md); [fibre-count sensitivity](fibre-count-yield-sensitivity.md); [laser delivered-power waterfall](laser-delivered-power-waterfall.md); [production evidence boundary matrix](../09-primary-research/manufacturing-evidence-boundary-matrix-2026-08-12.md) | Framework and sensitivities complete; production model incomplete | PAP-030, PAP-035 and PAP-044 improve component/full-module boundaries, but final-engine yield, Cpk, test/rework, warranty, field failure, replacement-cost and delivered-power distributions are not public. |
| 6 | Total-cost-per-delivered-bit comparison | [TCO-per-delivered-bit gate](tco-per-delivered-bit-gate.md); [power-to-cost sensitivity](tco-power-cost-sensitivity.md) | Gate and operating-cost sensitivity complete; comparison incomplete | Product ASP, good-unit yield, host power, service cost, capex and matched CPO/LPO/NPO/copper boundaries remain open. |
| 7 | Value-chain profit-pool map | [CPO content-attribution map](cpo-content-attribution-map.md); [optical-engine profit-pool gates](optical-engine-profit-pool-input-gates.md); [layer-level economics sensitivity](engine-layer-sensitivity-ranges.md) | Partially complete | Supplier content, ASP, share, price-down, cannibalisation and product margin are not attributable; the layer-level ranges are explicitly hypothetical sensitivities, not company inputs. |
| 8 | Company operational-leadership scorecard | [CPO Company Leadership Scorecard](../07-companies/leader-scorecard.md); [company evidence-gap matrix](../07-companies/company-evidence-gap-matrix.md) | Provisional qualitative ranking | Comparable qualification, yield, customer volume, reliability and supplier-share evidence is missing; numeric scores are intentionally unpopulated. |
| 9 | Company investment-attractiveness scorecard | [CPO earnings-materiality screen](cpo-earnings-materiality-screen.md); [core-company variant cards](../07-companies/variant-cards/core-company-variant-cards.md); [earnings/valuation bridge template](earnings-valuation-bridge-template.md) | Restricted-input framework complete; decision use incomplete | Six relative cards and layer sensitivities exist, but no analyst reports have yet been ingested into a reconciled CPO bridge; consensus, attributable CPO earnings, probability-weighted gross profit and downside cases remain unlinked to evidenced product economics. |
| 10 | Revenue, gross-profit, earnings and valuation bridge | [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md); [matched engine profit bridge](coherent-lumentum-matched-engine-profit-bridge.md); [analyst scenario model](analyst-variant/scenario-model-specification.md); [earnings/valuation bridge template](earnings-valuation-bridge-template.md) | Formula and restricted-input framework complete; company forecast incomplete | No defensible system denominator, supplier content/share, ASP, margin, yield/warranty, capex or cannibalisation bundle; analyst reports are awaiting ingestion. |
| 11 | Consensus and variant-perception tracker | [Expectations and variant-perception tracker](expectations-and-variant-perception-tracker.md); [analyst-estimate register](analyst-estimate-register.md) | Three-layer framework complete; analyst layer awaiting reports | Restricted consensus must be reconciled to product-specific economics, valuation and observable catalysts before a company decision is eligible. |
| 12 | Falsification dashboard and thesis-change log | [Falsification dashboard](falsification-dashboard.md); [critical-path milestone tracker](critical-path-milestone-tracker.md); [primary-research question bank](../09-primary-research/interview-question-bank.md) | Initial dashboard and dated baseline log complete; primary-research collection remains open | Future thesis changes still require product, customer, yield, service or economic evidence crossing the stated triggers. |

## Completion rule

The project is decision-ready only when outputs 1–12 have either:

1. a completed evidence-backed result; or
2. an explicit “no decision / not investable” conclusion supported by a documented missing gate and a concrete next evidence request.

“Partially complete” means the artifact exists but cannot yet support the final dated, probability-weighted investment judgement. It must not be presented as a finished research conclusion.

## Current highest-priority blockers

1. Customer confirmation connecting `SN6800`/`SN6810` or Broadcom `BCM78919` to accepted CPO units/ports and repeat deployment.
2. Complete engine BOM and supplier responsibility map.
3. Lot-level die-to-good-engine yield, fibre-attach/test cycle time and rework.
4. Qualification, field failure, replacement and warranty economics.
5. Matched CPO/LPO/NPO/copper TCO at 200G/lane and later 400G/lane.
6. Product ASP, supplier share, margin, price-down and cancellation terms.
7. Defined system denominators and consensus/valuation inputs.

The new [layer-level economics sensitivity](engine-layer-sensitivity-ranges.md)
improves the private stress-testing harness but does not clear any of these
gates. It is intentionally excluded from the public report and from company
base cases until product-linked evidence replaces its assumptions.

Several of these are generally inaccessible in public technical literature: customer-unit numerators, supplier pricing and margin terms, final-engine yield by lot, field-return distributions and warranty allocation. Their status should be recorded as **not publicly disclosed** unless a filing, customer statement or permitted primary interview supplies a bounded value; the absence of a public number is itself an evidence boundary, not a reason to invent a forecast.

See the [public-data boundary register](public-data-boundary-register.md) for the field-by-field treatment and the evidence that would change each status.

## Next audit update

Update this file whenever a new source clears or materially changes one of the gates. Every status change must cite the relevant source and claim IDs in the affected artifact; do not silently convert a company claim, model assumption or illustrative sensitivity into a cleared gate.
