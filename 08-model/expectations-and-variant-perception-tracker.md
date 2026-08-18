# CPO expectations and variant-perception tracker

**Owner:** Nur Alpys  
**Status:** Three-layer expectation register; management records populated, restricted analyst-consensus layer awaiting source ingestion
**As of:** 2026-08-09

## Purpose

The investment question requires a dated comparison between what companies/markets appear to expect and what the evidence supports. This tracker now separates observed facts, external expectations and Nur Alpys' variant view. The currently populated records remain management, company or partner expectations. Restricted analyst-consensus inputs will be added only through `ANL-###` / `EST-###` records in [the analyst-estimate register](analyst-estimate-register.md); they must not be confused with facts, fair values or achieved revenue.

## Three-layer rule

| Layer | What belongs here | Current status | Public treatment |
|---|---|---|---|
| Observed facts | Customer, production, qualification, shipment and filing records | Maintained in the claim ledger and company dossiers | Cite original public source |
| External expectations | Management targets, consultant forecasts and restricted analyst estimates | Management records populated; analyst layer awaiting reports | Publish only derived ranges where permitted |
| Nur Alpys variant | Chosen bear/base/bull range, rationale, catalyst and falsification | Framework created; no numeric analyst-driven variant yet | Publish the derived conclusion and methodology, not proprietary source detail |

## Retained expectation records

| ID | Company / source | Expectation or milestone | Date / horizon | Evidence class | What is observable | What remains unverified | Variant-perception use |
|---|---|---|---|---|---|---|---|
| EXP-001 | Coherent, `PRS-003`, `CLM-250` | CPO SAM estimated at more than $15B by calendar 2030 | 2030 | Company presentation using LightCounting and internal estimates | A dated management market-size framing | SAM definition, adoption rate, ASP, supplier share, realised revenue and margin | Potential market-size anchor; not a company revenue forecast |
| EXP-002 | Coherent, `PRS-003`, `CLM-251` | CPO/NPO engines shown as a new-revenue item labelled H2 2026 | H2 2026 | Company roadmap/presentation | A dated management milestone | SKU, customer, qualification, units, shipment and revenue recognition | Test whether the milestone becomes an observed shipment or slips |
| EXP-003 | Lumentum, `CMP-010`, `CLM-083` | Incremental multi-hundred-million-dollar CPO order deliverable in the first half of calendar 2027 | H1 2027 | Official financial-results disclosure | Order magnitude and delivery window | Customer, product, unit count, cancellation terms, conversion, margin and field deployment | Highest-value near-term supplier conversion checkpoint |
| EXP-004 | Broadcom, `CMP-018`, `CLM-211` | Fourth-generation CPO roadmap targeting 400G per channel | Undated | Company roadmap | Direction of lane-rate roadmap | Launch date, measured link, qualification, customer and production volume | Tests whether 400G shifts the profit pool toward deeper integration |
| EXP-005 | NVIDIA, `CMP-025`, `CLM-228`–`CLM-229` | Spectrum-X Ethernet Photonics reaches full production and has named first adopters/technology partners | 2026 | Company platform claim | Platform/adopter/partner list | Customer units, exact SKU, repeat volume, supplier allocation, yield and margin | Tests whether ecosystem language converts into CPO deployment and supplier content |
| EXP-006 | Marvell/Celestial, `CMP-020`, `CLM-095` | Meaningful revenue in H2 FY28; $500M annualized Q4 FY28; $1B annualized Q4 FY29 | FY28–FY29 | Management forecast and earnout case | Dated, falsifiable revenue targets | Production customer, units, ASP, margin, probability and achieved revenue | Strongest public-company accelerator optical-I/O expectation record |
| EXP-007 | TSMC, `PRI-029`–`PRI-031`, `CLM-214`–`CLM-216` | COUPE-on-substrate CPO production milestone beginning in 2026 | 2026 | Company technology milestone | Process/stacking target and engineering-sample yield | Named SKU, shipped units, final-engine yield, package responsibility, ASP and margin | Tests process-control conversion rather than market adoption alone |
| EXP-008 | Celestica, `CMP-028`, `CLM-255`–`CLM-256` | Design-and-manufacturing program for an unnamed hyperscaler CPO Ethernet switch; production ramp expected in 2027 | 2027 | Company program disclosure | Awarded program, 1.6T switch silicon, co-packaged optics and liquid cooling | Customer identity, SKU, units, qualification, repeat orders, optical BOM, supplier share, ASP and margin | Newest route-to-production checkpoint for switch-side CPO; planned ramp is not shipped volume |
| EXP-009 | Celestica, `CMP-030`, `CLM-258` | Earlier major hyperscaler 1.6T switching program; revenue expected to begin ramping in 2026 | 2026 | Historical company program disclosure | A prior 1.6T switching route and dated revenue expectation | Whether it is the later CPO program, actual revenue conversion, architecture, units and margin | Chronology control; prevents broader 1.6T switching expectations from being counted as CPO revenue |
| EXP-010 | NVIDIA, `CMP-053`, `CLM-435`–`CLM-437` | Spectrum-X Ethernet Photonics described as in full production, with TSMC, SPIL, TFC and Foxconn assigned fabrication, packaging/test, laser validation and system-assembly roles | June 2026 | Company production-ramp and supply-chain disclosure | A more specific production-responsibility map and pre-shipment validation statement | Customer-accepted SKU, units, repeat shipments, final-engine yield, supplier share, ASP, margin and warranty allocation | Tests whether the named full-stack route converts into repeat CPO deployments and attributable supplier economics |

## What is not yet in the tracker

The following are required before an investment-attractiveness score is eligible:

1. Dated sell-side consensus revenue, margin and earnings estimates for each public company.
2. As-of-date share price, diluted share count, market capitalisation and valuation multiple.
3. A defined CPO revenue/content bridge for each company.
4. Probability-weighted conversion of each management target into bear/base/bull cases.
5. Explicit downside if the milestone slips, is captured by another supplier, or converts at low margin.

Management SAM and revenue targets must never be substituted for consensus. A company can beat its own roadmap and still miss market expectations, or miss its own roadmap while the stock already discounts the miss.

## Variant-perception template

For every future expectation update, record:

```text
expectation_id
company
architecture/domain
source_date and as-of date
management or consensus value
unit and time horizon
what the market likely assumes
evidence-supported alternative
observable catalyst
falsification condition
valuation/earnings variable affected
source_id and claim_id
```

## Current evidence-adjusted interpretation

- The clearest near-term supplier conversion expectation is Lumentum's H1 2027 CPO order.
- The clearest market-size framing is Coherent's $15B+ CPO SAM estimate for 2030, but it is not attributable revenue.
- The clearest accelerator optical-I/O revenue aspiration is Marvell's FY28/FY29 Photonic Fabric case, but it remains an earnout-linked management forecast.
- Broadcom, NVIDIA and TSMC provide important product/process milestones, but their CPO-specific earnings expectations are not separately disclosed.
- Celestica adds a concrete 2027 planned production-ramp checkpoint for an unnamed hyperscaler CPO switch, but the disclosure is still insufficient for a volume or earnings estimate.

No variant-perception conclusion is currently investable because the public expectation records are not yet matched to restricted consensus, valuation, product economics or observed conversion. The company-card framework is now in [core-company variant cards](../07-companies/variant-cards/core-company-variant-cards.md).

## Market-denominator update

The [7 August 2026 market snapshot](market-snapshot-2026-08-07.md) now records feed-level prices, market-cap outputs and P/E fields for COHR, LITE, AVGO, NVDA, MRVL, CLS and TSM. This is a dated denominator only. The feed requires independent share-count/ADR reconciliation, and no sell-side consensus or CPO-specific earnings estimate has been added. The snapshot therefore does not change the “investment conclusion not eligible” status.

## Linked controls

- [CPO earnings-materiality screen](cpo-earnings-materiality-screen.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Total-cost-per-delivered-bit gate](tco-per-delivered-bit-gate.md)
- [Critical-path milestone tracker](critical-path-milestone-tracker.md)
- [CPO decision-output completion audit](../00-scope/decision-output-completion-audit.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
