# CPO missing-input value-of-information register

**Status:** Private model-control tool; no EPS, valuation or target-price output  
**As of:** 2026-08-13  
**Purpose:** Rank missing inputs by how much they can change the current decision, rather than filling them with false precision.

## Decision rule

An input has high value of information when it can invalidate a current view, unblock several later inputs, and match a defined product boundary. A number is not useful merely because it is precise: a consolidated margin, generic market forecast or adjacent product must not enter the model.

| Priority | Missing input | Why it has decision value | Status now | Minimum acceptable evidence | What it unlocks | What it does **not** unlock alone |
|---:|---|---|---|---|---|---|
| 1 | Exact CPO SKU, named customer, accepted systems/ports and date | Establishes that the product—not a platform or pluggable option—crossed a commercial boundary | Unavailable | Customer/OEM/procurement record with exact configuration and denominator | Commercial numerator; timing view | Repeatability, supplier economics or margin |
| 2 | Repeat order, expansion or second customer | Separates evaluation/sample/one-off delivery from commercial proof | Unavailable | Dated second delivery/expansion/renewal at same SKU boundary | Commercial-proof gate | Product economics |
| 3 | Product-matched supplier content/share | Identifies who may receive revenue at each PIC/engine, laser, attach, package and test layer | Unavailable | BOM, qualified supplier statement or contract at exact product boundary | Supplier attribution and non-overlap model | ASP, margin or yield |
| 4 | Final accepted-engine yield waterfall and rework | Determines whether architecture value survives fibre attach, package and late test | Unavailable | Lot denominator from die/attach/package/test through accepted output, with rework disposition | Cost-per-good-engine range | Field warranty or supplier margin |
| 5 | Field failure, repair scope, MTTR and warranty allocation | Tests whether external-light replacement solves the actual system failure domain | Unavailable | Population, time period, failure/return data and service workflow | Cost-per-restored-port and service-risk range | Manufacturing yield or price |
| 6 | Product price/ASP, price-down and cancellation terms | Converts content into attributable revenue rather than a notional BOM | Unavailable | Product/customer contract, filing or disclosed transfer price | Revenue range | Product gross margin |
| 7 | Product gross margin and incremental capex/R&D | Determines whether revenue produces retained economics | Unavailable | Product/segment margin with cost boundary plus project-linked capex/R&D | Gross/operating-profit sensitivity | Market share or valuation |
| 8 | Matched CPO/LPO/NPO/retimed system data | Tests whether CPO is necessary rather than merely possible | Partial | Same ASIC, ports, lane rate, reach, BER/FEC, cooling, service and cost boundary | Architecture preference | Supplier-specific profit capture |

## Collection sequence

```text
exact customer/SKU numerator → repeatability → supplier allocation
→ accepted-engine yield/rework → service/warranty → price → margin/capex
```

Do not reverse this sequence. A supplier-margin estimate cannot repair a missing product denominator, and a production announcement cannot establish a repeat shipment or profit pool.

## Model output discipline

The current scenario bridge may show labelled *assumption ranges*, but its only actionable output is the next data request above. No company receives numeric revenue, EPS, valuation or leadership output until the relevant priority inputs are evidenced at the same boundary.

## Links

- [Profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md)
- [Cost per good engine gate](manufacturing-cost-per-good-engine-gate.md)
- [Quarterly evidence register](../09-primary-research/quarterly-evidence-change-register-2026-08-12.md)
- [Immediate decision dashboard](../00-scope/immediate-decision-dashboard.md)
