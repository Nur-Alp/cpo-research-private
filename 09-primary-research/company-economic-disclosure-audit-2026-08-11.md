# Company economic-disclosure audit — 11 August 2026

**Status:** Private primary-disclosure review; not a valuation model  
**Question:** Which public disclosures permit a CPO revenue, gross-profit, EPS, or valuation input for the six-company universe?

## Conclusion

**None.** The latest retained primary financial anchors establish consolidated-company scale and, in a few cases, a CPO product/order route. They do not disclose a CPO-specific revenue line, product margin, customer/system denominator, qualified content share, final-engine yield/rework, warranty cost, attributable capex, or earnings contribution.

This is a disclosure result—not evidence that CPO economics are zero or immaterial. It means the CPO overlay remains **not eligible** for a company forecast.

The accompanying [commercial event → economic eligibility matrix](../08-model/commercial-event-to-economic-eligibility-matrix.md)
now distinguishes orders, awards, capacity rights, earnouts, management targets
and consolidated financial results from product-matched realised economics.
This prevents a future event from being promoted merely because its headline
contains an order value, a revenue target or a margin figure.

## Company-by-company disclosure boundary

| Company | Latest retained primary financial anchor | CPO-specific signal actually disclosed | What the source does not disclose | Permitted model use |
|---|---|---|---|---|
| NVIDIA | Q1 FY2027: $81.615bn revenue, $75.178bn Data Center revenue, 74.9% GAAP gross margin (`FIL-005`, `CLM-088`) | Spectrum-X Ethernet Photonics production/product route is disclosed in separate product materials | CPO revenue, gross margin, systems/ports, customer mix, engine content, supplier share, yield, warranty, capex or earnings contribution | Company-scale denominator only |
| Broadcom | Q2 FY2026: $22.187bn revenue, $10.8bn company-defined AI semiconductor revenue, $10.262bn free cash flow (`FIL-004`, `CLM-087`) | TH6-Davisson product and early-access route are disclosed separately | Switch-CPO revenue, units, optical-engine contribution, product gross margin, customer, yield/rework, warranty or capex allocation | Company-scale denominator only; AI semiconductor is not CPO |
| Coherent | Q4/FY2026: $2.05bn revenue; 38.5% GAAP and 40.2% non-GAAP gross margin. The result supersedes the retained Q3 consolidated denominator for the current-period screen. | The official release refers to broad AI-datacenter optical demand and capacity expansion, but does not isolate CPO, a customer, or a supplied layer. | CPO product/customer allocation, engine revenue, product gross margin, qualified output/yield, warranty or CPO capacity utilisation | Company-scale denominator only; do not substitute company margin for a CPO layer. |
| Lumentum | Q4 FY2026: $1.0063bn revenue and 47.4% GAAP gross margin; FY2026: $3.0140bn revenue and 41.7% GAAP gross margin (`FIL-014`, `CLM-531`) | Earlier multi-hundred-million-dollar CPO order for H1 2027 delivery plus an initial ELS-module order / ultra-high-power CPO-laser demand statement (`CLM-083`, `CLM-531`). Direct review of the latest retained Q3 FY2026 10-Q found no CPO/ELSFP order-conversion disclosure (`CLM-559`). | Customer, product, units, order size, revenue-recognition timing, laser share, gross margin, capacity utilisation, cancellation terms, yield, warranty or capex allocation | External-light/order-conversion milestones only; consolidated results are not CPO or ELS margins |
| Marvell | Q1 FY2027: $2.418bn revenue; 52.1% GAAP and 58.9% non-GAAP gross margin (`FIL-006`, `CLM-096`) | Celestial/Photonic Fabric management timing targets | Photonic Fabric/CPO revenue, customer, production units, margin, yield, capex or warranty | Company-scale denominator only; management target is not revenue |
| TSMC | Q2 2026: US$40.20bn revenue; 67.7% gross margin; 60.3% operating margin (`FIL-010`, `CLM-278`) | COUPE process/200G/production-milestone disclosures are separate | COUPE/CPO wafer, package or engine revenue/output; final-engine yield; customer allocation; ASP; margin; capex allocation | Company-scale/process-capacity context only |

## Controls for the private scenario model

The following inputs must remain empty, or be explicitly labelled a private assumption/external estimate, until a product-matched source resolves them:

```text
systems × CPO adoption × engines/system × supplier content × qualified share
× product gross margin − yield/rework/warranty − cannibalisation − incremental R&D/capex
```

The sources above cannot be used to fill **any** of `supplier content`, `qualified share`, `product gross margin`, `yield/rework/warranty`, or CPO-attributable capital costs. They also cannot convert a platform/product announcement into a CPO revenue numerator.

## Decision-changing future disclosures

This audit should be updated only if a company filing, earnings call, customer statement, contract/award, or primary manufacturing record changes a field below:

1. CPO-specific booked/shipped revenue and exact product/customer boundary;
2. CPO-specific gross margin, price, content/share or revenue-recognition disclosure;
3. final-engine output/yield, rework, test, field-return or warranty/reserve data;
4. attributable CPO capacity/capex and utilisation; or
5. reconciled diluted shares, tax, current consensus and valuation inputs sufficient for a derived EPS sensitivity.

Until then, a “no CPO economic disclosure” result is a valid research output and prevents false precision.

## 13 August current-period refresh

The purpose of this refresh is to distinguish a **new company result** from a
new CPO-economic fact. Coherent released Q4/FY2026 results on 12 August 2026:
$2.05bn quarterly revenue, 38.5% GAAP gross margin and 40.2% non-GAAP gross
margin. The release describes broad optical-connectivity demand and capacity
expansion but does not name a CPO product, customer, revenue line, supplied
layer, output, price, yield or warranty boundary. It therefore refreshes only
the consolidated materiality denominator and does **not** reopen the CPO
economic-input gate.

The remaining near-term disclosure calendar is also a control, not a forecast:

| Company | Next known primary checkpoint | Required evidence before any gate changes |
|---|---|---|
| Marvell | Q2 FY2027 results, 27 August 2026 | Named Photonic Fabric/XPU customer or product revenue plus an output/economic boundary; consolidated data-center growth alone is insufficient. |
| Broadcom | Next FY2026 earnings release, not yet posted on the official quarterly-results archive at review | Exact `BCM78919` customer/units or CPO-specific financial attribution; Tomahawk-family or AI-semiconductor totals are insufficient. |
| Lumentum | FY2026 Q4 release reviewed; no later financial release was present in the official archive at review | Conversion of the CPO/ELS order into named product/customer/quantity and revenue/margin boundary. |
| NVIDIA / TSMC | Next reported period | A matching product/customer/volume and CPO/COUPE economic disclosure—not consolidated earnings or advanced-node/packaging totals. |

**Source retained for the refresh:** Coherent, [Q4 and FY2026 results](https://www.coherent.com/news/press-releases/fourth-quarter-and-fiscal-year-2026-results), published 12 August 2026; reviewed 13 August 2026. It is used solely for the consolidated-denominator update above.

## Linked records

- [Public financial-baseline reconciliation](../08-model/public-financial-baseline-reconciliation.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [Analyst scenario specification](../08-model/analyst-variant/scenario-model-specification.md)
- [Current decision memo](../00-scope/current-decision-memo-2026-08-11.md)
