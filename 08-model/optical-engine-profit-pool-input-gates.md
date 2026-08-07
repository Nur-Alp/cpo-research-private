# Optical-Engine Profit-Pool Input Gates

**Owner:** Nur Alpys  
**Status:** Evidence gate; not a forecast or investment conclusion  
**Scope:** 200G/lane and later 400G/lane scale-out optical engines and PICs  
**Last updated:** 2026-08-07

## Purpose

This document converts the four initial company dossiers into a disciplined economic model. It records what may be modelled now, what is only an operating hypothesis, and what must remain blank until an attributable primary source exists.

It covers only the incremental economics of a scale-out optical engine or its directly supplied components. It does not estimate the value of an entire AI system, switch ASIC, GPU, data-centre network, or company.

## The two financial bridges

Do not subtract capital expenditure from gross profit. Gross profit and cash return answer different questions.

```text
Incremental revenue
= relevant systems
x CPO adoption rate
x engines per system
x supplier content per engine
x realised supplier share

Incremental gross profit
= incremental revenue
x realised gross margin
- cannibalised legacy gross profit
- incremental yield, rework, warranty and support cost

Incremental operating profit
= incremental gross profit
- incremental R&D, qualification and operating expense

Incremental free-cash-flow bridge
= incremental operating cash generation
- attributable capacity, packaging and test capital expenditure
```

The first two lines are model identities, not currently populated predictions. “Engines per system” and “supplier content per engine” must be defined at a shared product boundary before multiplication. Otherwise the same laser, PIC, package, or switch value can be counted twice.

## Required input register

| Input | Definition and unit | Needed for | Permitted evidence | Current status |
|---|---|---|---|---|
| Relevant systems | Annual count of a defined switch/system configuration | Revenue denominator | Customer, manufacturer or traceable market data | Blocked |
| CPO adoption rate | Share of those systems using the defined CPO architecture in a stated year | Revenue denominator | Customer production evidence or an explicitly probability-weighted scenario | Blocked |
| Engines per system | Number and capacity of optical engines in the exact system | Content conversion | Product architecture or teardown | Partially disclosed for Broadcom only [CLM-076] |
| Supplier content per engine | Revenue retained by the company per engine, in dollars | Revenue | Contract, product price, management disclosure or defensible supply-chain primary research | Blocked |
| Realised supplier share | Share of eligible engine content supplied by the company | Revenue | Named qualification, repeat orders and second-source evidence | Blocked |
| Realised gross margin | Product-level gross margin after manufacturing mix | Gross profit | Segment/product disclosure or primary research | Blocked |
| Yield and rework | Final good-engine yield, rework rate and cost per good engine | Gross profit | Manufacturing data, qualified process evidence or primary research | Blocked |
| Warranty and support | Failure, replacement and field-support cost per engine | Gross profit | Field-return/warranty records and service contract terms | Blocked |
| Cannibalised gross profit | Lost gross profit from displaced lasers, DSPs, retimed optics, switch products or other legacy content | Gross profit | Product transition / financial disclosure plus explicitly bounded assumptions | Blocked |
| Incremental R&D and qualification | Annual directly attributable operating expense | Operating profit | Filing disclosure, management evidence or rigorously sourced primary research | Blocked |
| Attributable capital expenditure | Cash investment required for incremental InP, SiPh, attach, packaging, test and reliability capacity | Free cash flow / return | Project-level disclosure or primary research | Blocked |
| Customer concentration and cancellation protection | Revenue dependence, order firmness and cancellation terms | Risk adjustment | Filing, contract or direct management/customer evidence | Partially disclosed at total-company boundary for Lumentum [CLM-073] |

## Company-by-company economic boundary

| Company | What current evidence establishes | What cannot yet be modelled | Principal economic gate |
|---|---|---|---|
| Broadcom | TH6-Davisson is defined as a 102.4T switch with sixteen 6.4T DR optical engines, 200G links and ELSFP modules [CLM-076]. | Optical-engine dollar content, what portion Broadcom retains, engine supplier share, CPO gross margin, field/service cost and unit volume. Product status is conservatively early-access sampling because the same release also says “now shipping” [CLM-077]. | Establish customer-confirmed production units and a full content map, including retimer/DSP/AEC and pluggable revenue displaced by CPO. |
| NVIDIA | NVIDIA claims Spectrum-X Ethernet Photonics CPO switches with 200G SerDes are in production and names early ecosystem adopters [CLM-079]. Meta independently confirms Spectrum-X adoption, not CPO deployment [CLM-081]. | CPO system count, customer CPO units, optical-engine supplier/content, CPO cost, pricing, margin, warranty and earnings materiality. | Identify the exact CPO SKU/customer configuration and determine whether NVIDIA captures engine content or merely platform rent. |
| Coherent | Coherent demonstrates multiple CPO component paths and says its first six-inch InP line is in volume production with planned expansion [CLM-068; CLM-069]. Consolidated Q3 FY26 margin is disclosed but is not a CPO margin [CLM-070]. | CPO customer, product content, engine ASP, final-engine yield, fibre-attach/test cost, CPO margin, CPO capacity allocation and order conversion. | Obtain a customer/product-boundary revenue bridge and final-engine manufacturing metrics; wafer capacity alone is not usable revenue. |
| Lumentum | Lumentum provides a serviceable ELSFP/UHP-laser product boundary [CLM-071], a multi-channel external-light-source demonstration [CLM-072], and a disclosed incremental multi-hundred-million-dollar CPO order for first-half 2027 delivery [CLM-083]. Consolidated margin and total-company concentration are disclosed [CLM-073]. | Customer, exact product, quantity, revenue-recognition profile, laser/engine content, CPO margin, yield, warranty, capacity allocation and cancellation protection. | Confirm whether the order is firm and what product/content it includes. Do not equate order value with external-laser revenue or gross profit. |

## Evidence-adjusted model rule

A number can enter the base case only when all five conditions hold:

1. It has an explicit unit, year, architecture and product boundary.
2. Its underlying source is retained locally or, if blocked, logged with its canonical direct link and retrieval limitation.
3. It is traceable to a claim ID and source ID.
4. It does not double count another company’s content or mix company-wide and CPO-specific economics.
5. Its evidence quality supports the intended use: customer-confirmed production for a base case; otherwise use only as a labelled scenario or sensitivity.

No current company meets all five conditions for a numeric company revenue, gross-profit or free-cash-flow forecast. The current numerical use of sixteen engines is limited to Broadcom's disclosed platform architecture, not a dollar-content or unit-volume forecast [CLM-076].

## Known but non-convertible signals

These records are material for diligence, but cannot be multiplied into a profit forecast:

| Signal | Correct use | Prohibited shortcut |
|---|---|---|
| Broadcom: sixteen 6.4T engines in TH6-Davisson | Define the technical content map that needs pricing and supplier attribution [CLM-076]. | Assume Broadcom sells or retains sixteen complete external engines at a presumed ASP. |
| NVIDIA: CPO production claim and named ecosystem partners | Prioritise customer/SKU confirmation and identify supplier relationships [CLM-079]. | Treat partners as CPO switch buyers or infer CPO revenue. |
| Coherent: six-inch InP line in volume production | Assess general ability to invest and identify capacity diligence questions [CLM-069]. | Convert wafer expansion into CPO-engine shipments or CPO margin. |
| Lumentum: incremental CPO order | Set a dated commercial-conversion checkpoint for first-half 2027 [CLM-083]. | Assign the full order to lasers, engines, gross profit or a named customer. |
| Consolidated gross margins | Bound corporate financial capacity and compare later with product-level evidence [CLM-070; CLM-073]. | Apply company-wide margin to CPO content. |

## Falsification and execution gates

| Gate | Pass condition | What fails if it does not pass |
|---|---|---|
| Architecture | CPO/NPO electrical path is needed at the specified rate/topology after matched comparison with LPO, retimed optics and copper. | Adoption-rate assumption is unsupported. |
| Product | A named system has qualified the complete engine at the relevant lane rate. | Relevant-system and adoption denominators are unsupported. |
| Manufacturing | Final-engine yield, attach/test throughput, reliability and rework economics meet a defined production threshold. | Realised gross margin is unsupported. |
| Commercial | Customer-confirmed repeat volume, price/content, supply share and cancellation terms are known. | Revenue and supplier-share inputs are unsupported. |
| Financial | Cannibalisation, R&D and capacity costs are attributed rather than hidden in consolidated reporting. | Operating-profit and cash-return conclusion is unsupported. |

## Highest-priority evidence requests

1. A customer-side confirmation of a Broadcom TH6-Davisson or NVIDIA Spectrum-X Ethernet Photonics CPO deployment: SKU, ports/units, production date, topology and service history.
2. A product-boundary content map: number of engines, PICs, lasers/ELSFP modules, fibre-attach assemblies, drivers/TIAs and test ownership per system.
3. Final-engine manufacturing data: yield waterfall from die to tested engine, automated attach cycle time, rework rate, test time and field-return/warranty terms.
4. Contract economics: supplier ASP, second-source status, price-down schedule, capacity commitments and cancellation protection.
5. Company filings and investor materials that isolate CPO revenue, backlog conversion, capital expenditure and product/segment margin rather than total-company figures.

## Links to evidence

- [Scale-Out Optical Engine and PIC Profit-Pool Thesis](../00-scope/scale-out-optical-engine-profit-pool-thesis.md)
- [Broadcom and NVIDIA Switch-CPO Platform Dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum External Optical-Engine Dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md)
- [CPO Company Leadership Scorecard](../07-companies/leader-scorecard.md)
- [Company leadership source manifest](../01-sources/company-leadership-source-manifest.md)
- [Claim ledger](../01-sources/claim-ledger.csv)

All company-specific statements in this document are bounded by the cited claim ledger entries. They do not establish independent production, company-specific margin or investment attractiveness unless the relevant gate is passed.
