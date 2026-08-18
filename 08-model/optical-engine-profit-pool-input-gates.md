# Optical-Engine Profit-Pool Input Gates

**Owner:** Nur Alpys  
**Status:** Evidence gate; not a forecast or investment conclusion  
**Scope:** 200G/lane and later 400G/lane scale-out optical engines and PICs  
**Last updated:** 2026-08-12

## Purpose

This document converts the six-company evidence set into a disciplined economic model. It records what may be modelled now, what is only an operating hypothesis, and what must remain blank until an attributable primary source exists.

It covers only the incremental economics of a scale-out optical engine or its directly supplied components. It does not estimate the value of an entire AI system, switch ASIC, GPU, data-centre network, or company.

The [private layer-level economics sensitivity](engine-layer-sensitivity-ranges.md)
decomposes hypothetical PIC/engine, external-laser, packaging/attach and
test/burn-in ranges. It is a sensitivity harness, not a source of company
inputs; all economic gates below remain in force.

The [profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md)
is the controlling ledger when a complete-engine price and component-layer
sensitivities appear in parallel. They are alternative boundaries and must not
be added together.

Before any company event enters this framework, classify it with the
[commercial event → economic eligibility matrix](commercial-event-to-economic-eligibility-matrix.md).
Orders, awards, capacity commitments, management targets, acquisition earnouts
and consolidated financial results can be material diligence signals while
remaining ineligible as attributable CPO revenue or profit inputs.

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

**Control:** Supplier content cannot be counted simultaneously at the PIC, engine, module and platform layers. Assign every dollar of content to one economic boundary only, and record any transfer price or pass-through separately.

## Required input register

| Input | Definition and unit | Needed for | Permitted evidence | Current status |
|---|---|---|---|---|
| Relevant systems | Annual count of a defined switch/system configuration | Revenue denominator | Customer, manufacturer or traceable market data | Blocked |
| CPO adoption rate | Share of those systems using the defined CPO architecture in a stated year | Revenue denominator | Customer production evidence or an explicitly probability-weighted scenario | Blocked |
| Engines per system | Number and capacity of optical engines in the exact system | Content conversion | Product architecture or teardown | Partially disclosed for Broadcom TH6-Davisson (16) and NVIDIA Spectrum-X SN6810 (32); not a dollar-content or volume input [CLM-076; CLM-514; CLM-515] |
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

## Economic-input eligibility matrix

This matrix is the model's hard boundary between evidence and sensitivity. A
**reported fact** can describe a product or process, but it is not automatically
an economic input. A **scenario-only** item may be varied to test sensitivity,
but cannot support a company base case. **Blocked** means that the model must
leave the cell blank until a matched primary record exists.

| Economic layer | Reported fact currently available | Scenario-only use permitted | Blocked until matched evidence |
|---|---|---|---|
| Optical engine / PIC | NVIDIA discloses 32 engines in the SN6810 reference architecture; Broadcom discloses 16 TH6 engines; TSMC discloses COUPE process/engineering results | Vary engines/system only within the exact SKU; stress supplier share and content as hypothetical ranges | Supplier ASP, complete-engine ownership, qualified share, final-engine yield, rework and product margin |
| External laser / ELSFP | NVIDIA describes ELS modules and TFC validation; Broadcom defines field-replaceable ELSFP; Lumentum discloses UHP/ELSFP products and order signals | Test a laser-only content boundary separately from a complete engine; vary service and replacement cost | Exact customer SKU allocation, laser count supplied, realised price, qualification, lifetime, warranty and margin |
| Fibre attach / connector | NVIDIA describes late fibre attachment and detachable connectors; Broadcom/Corning describe TH6 faceplate-to-chip collaboration | Stress attach-loss, rework and service assumptions only as labelled engineering sensitivities | Qualified attach supplier, cycle time, first-pass yield, loss distribution, replacement cost and supplier share |
| Package / assembly | NVIDIA names SPIL package/assembly/test and Foxconn system assembly; Broadcom discloses substrate-level packaging architecture | Separate OSAT value from platform value in a bounded waterfall | Package/test ASP, capacity allocation, final yield, test escape, warranty and realised margin |
| Test / qualification | NVIDIA says systems are validated before shipment; retained academic/process sources describe test vehicles and engineering yields | Use test-time or escape-rate ranges only for a sensitivity table marked “not observed” | Customer acceptance criteria, lot-level yield, test seconds, escape rate, field returns and cost per good engine |
| Customer/system denominator | Vendor production, sampling, orderability and partner statements exist; no exact accepted-unit numerator for target switch-CPO SKUs | Probability-weight adoption scenarios may be shown separately from consensus/base case | Named customer, exact SKU, accepted units/ports, repeat shipment and denominator year |
| Profit capture | Platform ownership, process routes and component breadth are observable | Rank diligence priority qualitatively, without assigning profit leadership | Supplier share, transfer price, price-down, cannibalisation, warranty, R&D, capex and product gross margin |

### Model-use rule

## Conditional value-capture tests by layer

The model uses **conditions**, not assumed winners. A layer is economically
eligible only if all of its stated conditions are evidenced at the same product
boundary; otherwise it stays a labelled sensitivity or blank input.

| Layer | Conditions required for durable value capture | Evidence that would fail the case | Current eligibility |
|---|---|---|---|
| PIC / optical engine | Product-linked design/qualified share; repeat qualified output; final-engine yield/rework; differentiated performance or switching cost; price and margin after packaging/test | Multi-source commodity engine, weak yield, platform-owner capture, or no product allocation | **Blocked** |
| External laser / ELSFP | Exact product/module allocation; delivered-power and reliability record; service/replacement boundary; capacity utilisation; price, warranty and margin | Integrated-light substitution, unallocated order, field failures, low utilisation or price-down | **Blocked** |
| Fibre attach / connector / FAU | Qualified interface role; low-loss/yield distribution; rework/service advantage; supplier share and ASP | Standardised/multisourced interface, attach yield loss, no repair advantage or unallocated role | **Blocked** |
| OSAT / assembly | Product-linked package scope; test insertion/control; qualified good-engine output; rework/warranty boundary; return on dedicated capex | Pass-through assembly economics, low utilisation, late defect/warranty burden or no CPO allocation | **Blocked** |
| Test / qualification | Required test-control point; validated coverage/escape value; throughput and cost per accepted engine; switching/qualification friction | Multiple qualified tools, low switching cost, unproven coverage or no product-level economics | **Blocked** |

**Promotion rule:** a layer may become a scenario input only after a named
product/customer or qualified-output record identifies the physical boundary,
and the economics are separately sourced. A company can be technically vital
without satisfying either condition.

The model may use the reported architecture denominators to define the shape
of a waterfall, and may use scenario-only values to show how sensitive the
answer would be. It may not multiply those denominators by an invented ASP,
share, yield or margin and call the result a company forecast. This is why the
current conclusion remains **no proven CPO profit-pool leader**, even though
the technical responsibility map is increasingly specific.

### Capacity-disclosure control

Tower's $1.3bn 2027 silicon-photonics contract disclosure and $290m
capacity-reservation prepayments are a useful comparison case: they show that
capacity can be commercially contracted, but span pluggable, NPO and CPO
applications.[CLM-534] The figures therefore cannot populate any CPO
denominator, content, margin or return input. The minimum evidence standard is
**capacity commitment + exact CPO product allocation + supplier economic layer**,
not capacity commitment alone.

## Company-by-company economic boundary

| Company | What current evidence establishes | What cannot yet be modelled | Principal economic gate |
|---|---|---|---|
| Broadcom | TH6-Davisson is defined as a 102.4T switch with sixteen 6.4T DR optical engines, 200G links and ELSFP modules; the release names TSMC COUPE technology-based engines and a future 400G-per-channel roadmap. TSMC separately reports a customer-linked 200G COUPE result, >99% engineering-sample stacking yield and a 2026 production milestone [CLM-076; CLM-210; CLM-211; CLM-213; CLM-214; CLM-215; CLM-216]. | Optical-engine dollar content, what portion Broadcom retains, whether TSMC supplies process, wafers, complete engines or packaging, engine supplier share, CPO gross margin, field/service cost and unit volume. Product status is conservatively early-access / **Limited Release** because the official release combines “now shipping” with sampling language and the current product catalogue supplies no customer denominator [CLM-077; CLM-530]. | Establish customer-confirmed production units and a full content map, including TSMC/Broadcom/laser/PIC/attach/test responsibility, engine supplier share, retimer/DSP/AEC and pluggable revenue displaced by CPO. NVIDIA's detailed 32-engine Spectrum-X reference map must not be substituted for Broadcom's 16-engine TH6 map [CLM-235]. |
| NVIDIA | NVIDIA's 2026 release states Spectrum-X Ethernet Photonics is a 200Gb/s-SerDes CPO switch now in production and names early ecosystem partners/adopters [CLM-346]. Its technical architecture record describes 32 engines per Spectrum-X package, 16 Tx/16 Rx lanes per engine, eight-laser ELS modules and detachable connectors [CLM-235; CLM-236; CLM-237]. CoreWeave confirms a named 102.4T SN6600-LD deployment, but CMP-048 classifies that SKU as pluggable RHS rather than CPO; Lambda provides production-scale Quantum-X evidence in a separate domain [CLM-220–CLM-224; CLM-380–CLM-384]. Meta independently confirms Spectrum-X adoption, not CPO deployment [CLM-081]. | CPO system count, customer CPO units, optical-engine supplier/content, CPO cost, pricing, margin, warranty and earnings materiality. The NVIDIA reference architecture is not proof that every customer SKU uses the same engine/ELS count. | Identify the exact CPO SKU/customer configuration and determine whether NVIDIA captures engine content or merely platform rent; map which partner supplies PIC, ELS, fibre attach, packaging and test. |
| Coherent | Coherent demonstrates multiple CPO component paths and says its first six-inch InP line is in volume production with planned expansion; SEC filing confirms the executed $2B NVIDIA investment and access to five additional CPO-related product families [CLM-068; CLM-069; CLM-197]. The 2026 strategic agreement also discloses a multibillion-dollar purchase commitment and future capacity rights across advanced optics, not a CPO-specific line [CLM-538]. Consolidated Q3 FY26 margin is disclosed but is not a CPO margin [CLM-070]. | CPO product allocation, engine ASP, final-engine yield, fibre-attach/test cost, CPO margin, CPO capacity allocation and order conversion. | Use the matched engine bridge; executed financing, purchase commitment and product-family access are not usable CPO revenue. |
| Lumentum | Lumentum provides a serviceable ELSFP/UHP-laser product boundary [CLM-071], a multi-channel external-light-source demonstration [CLM-072], an earlier incremental multi-hundred-million-dollar CPO order for first-half 2027 delivery, and a later initial ELS-module-order statement [CLM-083; CLM-531]. SEC filing confirms the executed $2B NVIDIA investment and advanced-laser capacity rights; the Greensboro announcement adds an NVIDIA-linked 6-inch InP facility with a mid-2028 ramp [CLM-198; CLM-196; CLM-286]. Consolidated results are disclosed but remain non-allocable [CLM-073; CLM-531]. | Customer, exact product, quantity, revenue-recognition profile, laser/engine content, CPO margin, yield, warranty, capacity allocation and cancellation protection. | Reconcile the order, ELS statement, capacity and fab records with a defined laser/engine boundary. Executed financing and planned capacity are not qualified output or gross profit. |
| Fabrinet | Fabrinet describes end-to-end outsourced optical packaging, integration, final assembly, testing, NPI transfer and qualification infrastructure [CLM-265; CLM-266]. Current DCI/HPC revenue and fixed-price/yield disclosures strengthen the manufacturing economics case [CLM-269; CLM-271]. FY2025 optical-communications revenue and company gross margin provide scale denominators [CLM-267]. | CPO programme, engine content, supplier share, qualified yield, ASP, CPO margin, warranty, and attributable capex. | Establish a named CPO programme and separate contract-manufacturing pass-through from value-added manufacturing profit; model yield/warranty downside explicitly; do not apply the 12.1% company margin to CPO. |
| Celestica | Celestica's Q1 2026 filing supplies HPS/CCS scale, capex, segment margin and customer-concentration denominators [CLM-273; CLM-274; CLM-275; CLM-276]. The separate results release supplies the CPO-programme award and planned 2027 ramp [CLM-255; CLM-256]. | CPO programme revenue, system/engine content, supplier share, qualified yield, ASP, CPO margin, warranty and attributable capex. | Keep the 10-Q denominators separate from the CPO release; do not apply 10.8% gross margin, 8.6% CCS margin or ~$1B capex directly to CPO. |
| TSMC | TSMC's COUPE milestones and board-level advanced-packaging appropriation establish a process/capacity control-point case [CLM-213; CLM-214; CLM-215; CLM-216; CLM-282]. Q2 earnings provide scale denominators [CLM-278; CLM-279]. | COUPE/CPO output, package responsibility, supplier share, final-engine yield, ASP, CPO margin, customer units and attributable capex. | Keep the US$44.962B appropriation and 67.7% consolidated gross margin separate from COUPE; no public allocation supports a CPO profit forecast. |

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
| Coherent: six-inch InP line plus NVIDIA capacity agreement | Assess capacity/customer-route evidence and identify product-allocation diligence questions [CLM-069; CLM-194; CLM-538]. | Convert wafer expansion, purchase commitment or $2B investment into CPO-engine shipments or CPO margin. |
| Lumentum: CPO order, initial ELS order, NVIDIA capacity agreement and Greensboro fab | Set first-half-2027 order-conversion and mid-2028 capacity checkpoints; seek a named product/customer/quantity record for the initial ELS order [CLM-083; CLM-195; CLM-196; CLM-531]. | Assign the order, investment, fab or capacity rights to lasers, engines, gross profit or a named customer. |
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
- [Optical-engine profit-pool scenario bridge](profit-pool-scenario-bridge.md)
- [CPO content-attribution map](cpo-content-attribution-map.md)
- [NVIDIA CPO reference-content bridge](nvidia-cpo-reference-content-bridge.md)
- [Total-cost-per-delivered-bit gate](tco-per-delivered-bit-gate.md)
- [CPO Company Leadership Scorecard](../07-companies/leader-scorecard.md)
- [Company leadership source manifest](../01-sources/company-leadership-source-manifest.md)
- [Claim ledger](../01-sources/claim-ledger.csv)

All company-specific statements in this document are bounded by the cited claim ledger entries. They do not establish independent production, company-specific margin or investment attractiveness unless the relevant gate is passed.
