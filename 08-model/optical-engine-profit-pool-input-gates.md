# Optical-Engine Profit-Pool Input Gates

**Owner:** Nur Alpys  
**Status:** Evidence gate; not a forecast or investment conclusion  
**Scope:** 200G/lane and later 400G/lane scale-out optical engines and PICs  
**Last updated:** 2026-08-07

## Purpose

This document converts the four initial company dossiers into a disciplined economic model. It records what may be modelled now, what is only an operating hypothesis, and what must remain blank until an attributable primary source exists.

It covers only the incremental economics of a scale-out optical engine or its directly supplied components. It does not estimate the value of an entire AI system, switch ASIC, GPU, data-centre network, or company.

## Domain partition update

The secondary-source review confirms that one profit-pool model cannot cover every CPO use case. Keep at least three separate economic cases:

1. **Switch-side CPO / Ethernet scale-out:** primarily a transceiver-replacement and switch-platform decision; test TCO, serviceability, blast radius, supplier margin stacking and customer bargaining power.
2. **Inter-rack scale-up CPO:** primarily a world-size and reach decision; test workload benefit, rack topology, optical endpoint count, copper/AEC alternatives, service model and roadmap confidence.
3. **Accelerator optical I/O / NPO chiplets:** primarily a host-package and chiplet-interface decision; test PIC/EIC ownership, optical-I/O content, hybrid bonding, yield, protocol and customer qualification.

Do not transfer an engine ASP, adoption rate, pJ/bit result or supplier share from one domain into another without a matched product and economic boundary. [CLM-177; CLM-178; CLM-183; CLM-185]

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
| Margin-stack and bargaining-power boundary | Supplier, switch-platform, FAU/shuffle, service and customer margin layers applied to the same content | TCO / profit pool | Contract, realised pricing, channel structure or bounded primary supply-chain research | Blocked; SemiAnalysis scenario only [CLM-180] |
| Domain-specific workload benefit | Network-layer reduction or accelerator-world-size/collective-communication benefit attributable to CPO | Adoption and value capture | Customer workload benchmark, topology and system cost/power evidence | Blocked; scale-up rationale remains a hypothesis [CLM-178; CLM-187] |

## Company-by-company economic boundary

| Company | What current evidence establishes | What cannot yet be modelled | Principal economic gate |
|---|---|---|---|
| Broadcom | TH6-Davisson is defined as a 102.4T switch with sixteen 6.4T DR optical engines, 200G links and ELSFP modules; the release names TSMC COUPE technology-based engines and a future 400G-per-channel roadmap. TSMC separately reports a customer-linked 200G COUPE result, >99% engineering-sample stacking yield and a 2026 production milestone [CLM-076; CLM-210; CLM-211; CLM-213; CLM-214; CLM-215; CLM-216]. | Optical-engine dollar content, what portion Broadcom retains, whether TSMC supplies process, wafers, complete engines or packaging, engine supplier share, CPO gross margin, field/service cost and unit volume. Product status is conservatively early-access sampling because the same release also says “now shipping” [CLM-077]. | Establish customer-confirmed production units and a full content map, including TSMC/Broadcom/laser/PIC/attach/test responsibility, engine supplier share, retimer/DSP/AEC and pluggable revenue displaced by CPO. NVIDIA's detailed 32-engine Spectrum-X reference map must not be substituted for Broadcom's 16-engine TH6 map [CLM-235]. |
| NVIDIA | NVIDIA claims Spectrum-X Ethernet Photonics CPO switches with 200G SerDes are in production and names early ecosystem adopters [CLM-079]. Its technical architecture record describes 32 engines per Spectrum-X package, 16 Tx/16 Rx lanes per engine, eight-laser ELS modules and detachable connectors [CLM-235; CLM-236; CLM-237]. CoreWeave independently confirms a named 102.4T SN6600-LD deployment, while Lambda provides production-scale Quantum-X evidence in a separate domain [CLM-220–CLM-224]. Meta independently confirms Spectrum-X adoption, not CPO deployment [CLM-081]. | CPO system count, customer CPO units, optical-engine supplier/content, CPO cost, pricing, margin, warranty and earnings materiality. The NVIDIA reference architecture is not proof that every customer SKU uses the same engine/ELS count. | Identify the exact CPO SKU/customer configuration and determine whether NVIDIA captures engine content or merely platform rent; map which partner supplies PIC, ELS, fibre attach, packaging and test. |
| Coherent | Coherent demonstrates multiple CPO component paths and says its first six-inch InP line is in volume production with planned expansion; SEC filing confirms the executed $2B NVIDIA investment and access to five additional CPO-related product families [CLM-068; CLM-069; CLM-197]. Consolidated Q3 FY26 margin is disclosed but is not a CPO margin [CLM-070]. | CPO product allocation, engine ASP, final-engine yield, fibre-attach/test cost, CPO margin, CPO capacity allocation and order conversion. | Use the matched engine bridge; executed financing and product-family access are not usable revenue. |
| Lumentum | Lumentum provides a serviceable ELSFP/UHP-laser product boundary [CLM-071], a multi-channel external-light-source demonstration [CLM-072], and a disclosed incremental multi-hundred-million-dollar CPO order for first-half 2027 delivery; SEC filing confirms the executed $2B NVIDIA investment and advanced-laser capacity rights, while Greensboro 6-inch InP capacity is planned for mid-2028 [CLM-083; CLM-198; CLM-196]. Consolidated margin and total-company concentration are disclosed [CLM-073]. | Customer, exact product, quantity, revenue-recognition profile, laser/engine content, CPO margin, yield, warranty, capacity allocation and cancellation protection. | Reconcile order, capacity and fab records with the laser/engine boundary. Executed financing and planned capacity are not qualified output or gross profit. |

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
| Coherent: six-inch InP line plus NVIDIA capacity agreement | Assess capacity/customer-route evidence and identify product-allocation diligence questions [CLM-069; CLM-194]. | Convert wafer expansion, purchase commitment or $2B investment into CPO-engine shipments or CPO margin. |
| Lumentum: CPO order plus NVIDIA capacity agreement and Greensboro fab | Set first-half-2027 order-conversion and mid-2028 capacity checkpoints [CLM-083; CLM-195; CLM-196]. | Assign the order, investment, fab or capacity rights to lasers, engines, gross profit or a named customer. |
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

Use the [CPO evidence-gate register](evidence-gate-register.md) as the active prioritized queue for the blocked inputs below. The [engine yield waterfall template](engine-yield-waterfall-template.md) defines the cost-per-good-engine calculation without inventing values.

- [Scale-Out Optical Engine and PIC Profit-Pool Thesis](../00-scope/scale-out-optical-engine-profit-pool-thesis.md)
- [Broadcom and NVIDIA Switch-CPO Platform Dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum External Optical-Engine Dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md)
- [Coherent versus Lumentum matched engine and profit bridge](coherent-lumentum-matched-engine-profit-bridge.md)
- [CPO content-attribution map](cpo-content-attribution-map.md)
- [NVIDIA CPO reference-content bridge](nvidia-cpo-reference-content-bridge.md)
- [Total-cost-per-delivered-bit gate](tco-per-delivered-bit-gate.md)
- [CPO Company Leadership Scorecard](../07-companies/leader-scorecard.md)
- [Company leadership source manifest](../01-sources/company-leadership-source-manifest.md)
- [Claim ledger](../01-sources/claim-ledger.csv)

All company-specific statements in this document are bounded by the cited claim ledger entries. They do not establish independent production, company-specific margin or investment attractiveness unless the relevant gate is passed.
