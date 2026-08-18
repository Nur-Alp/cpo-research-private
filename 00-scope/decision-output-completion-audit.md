# CPO Decision-Output Completion Audit

**Owner:** Nur Alpys
**As of:** 2026-08-12
**Purpose:** Test the current library against the required decision outputs in [CPO Research Question and Decision Scope](research-question.md). This is an evidence audit, not a claim that the study is complete.

The detailed model-level audit and gate-by-gate links are maintained in [08-model/decision-output-completion-audit.md](../08-model/decision-output-completion-audit.md). This scope-level page remains the executive audit.

For the complete objective audit, including supplier, PIC, manufacturing,
alternatives and analyst-layer requirements, see [objective completion audit](objective-completion-audit-2026-08-12.md).

The current provisional answer is summarized in the dated [Current CPO Decision Memo](current-decision-memo-2026-08-11.md); it is deliberately not a completion claim or investment recommendation.

## Overall finding

The research has a credible technical/economic framework and several evidence-matched company dossiers. It is **not yet capable of a dated probability-weighted investment conclusion**. The missing evidence is concentrated in customer deployment, final-engine manufacturing, total cost, product economics, and market expectations—not basic CPO explanation.

The source/claim referential-integrity audit is now clean (`01-sources/evidence-integrity-audit-2026-08-09.md`), and a primary-research question bank is ready. On 12 August, Lumentum's FY2026 Q4 release added an initial ELS-module order to the external-light route record (`FIL-014`; `CLM-531`), but did not identify a customer, product, quantity, price, margin, yield or warranty boundary. Those controls improve traceability and evidence collection but do not clear the substantive economic gates.

## Required-output status

| Required output | Current status | Evidence now available | What prevents completion |
|---|---|---|---|
| 1. Architecture trigger matrix | Evidence-gated matrix added; not numerically complete | Lane/domain trigger matrix now separates 100G, 200G, 400G and accelerator scale-up; a four-way retimed/LPO/NPO/CPO scorecard makes the common electrical, power/cooling, thermal, service, qualification and replacement boundary explicit. | Matched all-in CPO/LPO/NPO/copper technical and economic comparison at a shared domain. |
| 2. Technical/commercial viability gates | Partial | Gate definitions and company-specific blocks are explicit. | Final engine yield, thermal/reliability, service, customer qualification and total-cost evidence. |
| 3. 2026-2032 probability-weighted adoption timeline | Not numerically eligible | Evidence-calibrated state/milestone model. | System numerator/denominator, customer confirmation and economic gates. |
| 4. Critical-path milestone tracker | Partial | Architecture-specific milestones and dated management targets exist. | Observed customer, qualification, production, yield and field milestones. |
| 5. Manufacturing/yield/reliability/service model | Partial; service/failure-domain model, full-module IBM reliability packet and yield-claim reconciliation added | Packaging, attach, laser and serviceability benchmarks plus PAP-042's full-module reflow/JEDEC stress record identify the variables, process-learning boundary and correlated-failure boundary. NVIDIA's CMP-051 process claim is explicitly denominator-bounded. | Production yield waterfall, cycle time, Cpk, field return, warranty and repair-cost data. |
| 6. Total cost per delivered bit comparison | Framework strengthened; service boundary explicit; not numerically complete | A transparent 102.4T power scenario plus formal delivered-bit/TCO and service/failure-domain gates now exist. | Matched capex, module/engine cost, cooling, spares, repair, utilisation, availability and yield inputs. See [TCO gate](../08-model/tco-per-delivered-bit-gate.md). |
| 7. Value-chain profit-pool map | Partial | Platform, engine, laser, packaging and foundry control points are mapped; the six-company register separates confirmed role, route/candidate and open layers. | Attributable content, supplier share, ASP, product margin and cannibalisation. |
| 8. Operational-leadership scorecard | Framework plus second-group comparator layer | Leadership layers and evidence multipliers are defined; core and second-group dossier conclusions are separated by role. | Comparable customer, production, yield, reliability and ecosystem data to populate scores. |
| 9. Investment-attractiveness scorecard | Not eligible | Revenue-scale materiality screen, company input gates and a dated market-denominator snapshot now exist. | CPO earnings bridge, reconciled shares/ADR ratios, auditable consensus data and downside sensitivity. |
| 10. Revenue/gross-profit/earnings/valuation bridge | Partial framework only | Mathematical bridge and revenue-scale thresholds. | All product-specific economics and current valuation/consensus inputs. |
| 11. Consensus/variant-perception tracker | Management-expectation register plus market-denominator snapshot; consensus not complete | Dated management, company and partner expectations plus a 7 August 2026 feed snapshot are recorded in the [expectations tracker](../08-model/expectations-and-variant-perception-tracker.md). | Dated sell-side consensus, reconciled price/valuation/share count, probability-weighted conversion and downside sensitivity. |
| 12. Falsification dashboard/thesis-change log | Partial | Hypothesis register, claim ledger and dated company target tests exist. | Regular observed-versus-expected milestone record and probability revisions. |

## Evidence-quality constraint

No decision output should be upgraded by substituting company announcements for customer-side proof. The current source set has vendor product claims, demonstrations, standards contributions, academic simulations and some filings. It does not yet contain the linked evidence required for a valid company profit forecast: system volume, content, share, realised product margin, yield/warranty, cannibalisation and attributable capital expenditure.[CLM-084]

## Architecture status snapshot

| Architecture/domain | Current evidence-adjusted position | Governing reference |
|---|---|---|
| Advanced retimed pluggables, 102.4T Ethernet | Technically plausible; commercial economics unproven. | [102.4T comparison](../02-architecture/102.4t-cpo-vs-advanced-pluggables.md) |
| LPO, 100G/lane | Stronger system evidence than later lanes; no verified broad production/adoption denominator. | [Linear-drive benchmark](../02-architecture/linear-drive-boundary-benchmark.md) |
| LPO, 200G/lane | Conditional modeled/design feasibility, not a matched qualified production system. | [Linear-drive benchmark](../02-architecture/linear-drive-boundary-benchmark.md) |
| LPO, 400G/lane | Measured components below a modeled end-to-end rate; conventional LPO not established. | [Linear-drive benchmark](../02-architecture/linear-drive-boundary-benchmark.md) |
| NPO/OBO | Plausible serviceable/interoperable bridge; product/standard/adoption proof absent. | [NPO boundary](../02-architecture/npo-interoperability-boundary.md) |
| Switch-side CPO | Strongest 200G commercial-maturity signal, but commercial-proof threshold is not met publicly. NVIDIA's product boundary is now specific (`SN6800` / `SN6810`); no customer-side record connects either SKU to accepted units or repeat shipment. | [Commercial-proof dossiers](../07-companies/commercial-proof-dossiers/README.md) |
| Accelerator optical I/O | Credible public candidates and Marvell management targets; no qualified-volume proof. | [Marvell/Celestial dossier](../07-companies/marvell-celestial-accelerator-optical-io-dossier.md) |

## Company conclusion status

| Company/group | What can be said now | What must remain open |
|---|---|---|
| Broadcom | Merchant switch-CPO product-definition leader in current evidence. | CPO units, customer deployment, CPO revenue/margin and engine profit capture. |
| NVIDIA | Integrated platform/customer-route leader in current evidence; `SN6800` / `SN6810` specify the switch-CPO configurations. | Customer accepted CPO SKU/units, repeat deployment, engine supplier/content, CPO economics and earnings materiality. |
| Coherent | Broadest disclosed external component/manufacturing stack. | Production CPO customer, final-engine yield and margin. |
| Lumentum | Clearest external-light commercial-route signal: an earlier CPO order plus a later initial ELS-module order statement. | Customer/product allocation, quantity, conversion, margin and retention of profit. |
| Marvell / Celestial | Clearest public-company accelerator optical-I/O revenue aspiration and transaction stake. | Product qualification, shipped revenue, margin, customer and earnout probability. |
| Celestica | Credible system-design/manufacturing route with an unnamed hyperscaler CPO program and planned 2027 ramp. | Customer/SKU, units, optical scope, yield, CPO revenue, margin, capex and warranty allocation. |

No company is an evidence-supported overall **profit-pool leader** or **best public-equity opportunity** today.

## Prioritized next evidence work

1. **Customer proof:** customer-side CPO/NPO/optical-I/O deployment, exact SKU, topology, units/ports, repeat order and service history. POET/Lumilens adds a conditional purchase-order and 2027-ramp comparator, and Lumentum now reports an initial ELS-module order, but neither supplies an end-customer CPO numerator.
2. **Engine manufacturing:** final yield waterfall, fibre attach/test throughput, reliability qualification, rework and warranty allocation. POET adds installed capacity and an 800G qualification/design-in claim, but no lot yield or output distribution.
3. **Matched architecture economics:** common 200G and later 400G lane system boundary spanning CPO, NPO, LPO, retimed optics and copper/AEC.
4. **Supplier economics:** content map, ASP, supplier share, price-down, customer concentration, margin, capex and cannibalisation.
5. **Accelerator optical-I/O comparables:** the Ayar Labs, Lightmatter, Marvell/Celestial, Intel, NVIDIA and TSMC comparator layer is now documented; continue with customer/product qualification and economics.
6. **Investment overlay:** reconcile the dated market snapshot, then retain auditable consensus estimates only after the product economics are sufficiently bounded.

## Completion gate

The study may state a final, dated investment conclusion only when each final-answer field has a direct linked evidence basis:

```text
Architecture and domain -> comparable technical + commercial gate evidence
Commercial-proof and meaningful-adoption year/probability -> customer/volume denominator + calibrated scenario
Technical and volume leader -> comparable performance + qualification/units
Profit-pool leader -> content + share + realised economics + return/cost bridge
Best equity -> profit bridge + dated consensus/valuation + downside/catalyst analysis
```

Until then the correct conclusion is: **not yet investable on CPO alone; continue evidence acquisition against the listed gates.**

## References

- [CPO Research Question and Decision Scope](research-question.md).
- [Architecture trigger matrix](../02-architecture/architecture-trigger-matrix.md) and [common system-boundary scorecard](../02-architecture/system-boundary-comparison-scorecard.md).
- [Source-gap audit](../01-sources/source-gap-audit-2026-08-06.md).
- [CPO adoption timeline](../08-model/adoption-timeline.md).
- [CPO customer-proof register](../08-model/customer-proof-register.md).
- [Critical-path milestone tracker](../08-model/critical-path-milestone-tracker.md).
- [Total-cost-per-delivered-bit gate](../08-model/tco-per-delivered-bit-gate.md).
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md).
- [Six-company content-attribution register](../07-companies/six-company-content-attribution-register.md).
- [CPO earnings-materiality screen](../08-model/cpo-earnings-materiality-screen.md).
- [Claim ledger](../01-sources/claim-ledger.csv), especially CLM-074, CLM-082, CLM-084 and CLM-093 through CLM-096.
