# Supplier-content evidence-packet register

**Status:** Private acquisition and attribution control; not a BOM, revenue model, or supplier ranking  
**As of:** 2026-08-13  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6810`/`SN6800` (and matching `-LD` labels) and Broadcom TH6-Davisson `BCM78919`

## Purpose

The public record already has a broad route map. The missing step is not a
longer ecosystem list; it is an evidence packet that assigns a **physical
responsibility and commercial boundary to the same exact SKU**. This register
turns every open layer into a concrete record request. It is the handoff for
future filings, OEM material, supplier disclosures, channel checks, permitted
expert calls, and manufacturing records.

## Admission rule

A packet is usable only if it records all of the following:

1. exact product/configuration and revision;
2. physical layer and scope of work;
3. named legal supplier or internal manufacturing entity;
4. qualification, production, shipment or service state and date;
5. count/share/output at the same boundary; and
6. price, cost, yield/rework, warranty or margin boundary if the packet is to
   populate the economics model.

A partner quote, demo, ecosystem list, generic CPO capacity statement, or
company-wide margin cannot substitute for a missing field.

## NVIDIA evidence packets

| ID | Layer | Current strongest evidence | What must be acquired | Best record holder | Promotion if acquired | Do not accept as substitute |
|---|---|---|---|---|---|---|
| N-SUP-01 | PIC / engine | NVIDIA names TSMC for SiPh fabrication (`CLM-435`) | Wafer versus die versus complete-engine scope; qualified source/share; shipped or accepted output | NVIDIA, TSMC, engine assembler or customer BOM | Product-linked PIC/engine attribution | COUPE technology demonstration or generic SiPh capacity |
| N-SUP-02 | EIC / driver / TIA | Integrated 200G architecture only; supplier unallocated | Design/fabrication/package ownership and interface boundary | NVIDIA, TSMC, engine supplier, ASIC/package documentation | First direct EIC allocation | ASIC ownership or a product block diagram alone |
| N-SUP-03 | Laser / ELS | TFC packaging/validation; Lumentum family ecosystem role (`CLM-435`, `CLM-536`) | Laser-die source, ELS topology/count, qualified share, redundancy and replacement/warranty owner | NVIDIA, TFC, laser supplier, customer service document | Product-linked external-light allocation | High-power laser capability or an unallocated NVIDIA agreement |
| N-SUP-04 | Fibre attach / connector | NVIDIA describes late attachment; SENKO names detachable connectors (`CLM-406`–`CLM-410`, `CLM-537`) | Attach supplier, automation flow, first-pass yield, rework and connector allocation | NVIDIA, SPIL, connector/attach supplier, qualification report | Product-linked attach/connector responsibility | Connector compatibility or a detachable-interface headline |
| N-SUP-05 | Package / assembly / test | NVIDIA names SPIL and pre-shipment validation (`CLM-435`–`CLM-436`) | Exact SPIL scope, lot acceptance, final-engine/package yield, test coverage/escapes and cost/warranty split | NVIDIA, SPIL, OEM or field-return record | Final-package/test attribution and possibly yield input | System warranty policy or engineering-sample yield |
| N-SUP-06 | System / customer | NVIDIA production/adopter statements; OEM CPO models defined (`CLM-542`, `CLM-550`) | Named customer, exact CPO SKU, accepted systems/ports, date and repeat delivery | Customer/operator, OEM, procurement/earnings record | Commercial numerator and repeatability gate | Spectrum-X platform use, SN6600 deployment, or a CPO option |

## Broadcom evidence packets

| ID | Layer | Current strongest evidence | What must be acquired | Best record holder | Promotion if acquired | Do not accept as substitute |
|---|---|---|---|---|---|---|
| B-SUP-01 | PIC / engine / EIC | TH6 specifies integrated engines and names COUPE technology (`CLM-076`, `CLM-210`) | Complete-engine supplier, PIC/EIC split, COUPE process scope, qualified share and output | Broadcom, TSMC, engine/OSAT supplier, customer BOM | Product-linked engine/PIC/EIC attribution | COUPE roadmap, process claim or 16-engine count |
| B-SUP-02 | Laser / ELSFP | Field-replaceable ELSFP is a defined interface (`CLM-076`–`CLM-077`) | Qualified laser/ELSFP supplier, laser count, source redundancy, price and warranty boundary | Broadcom, ELS supplier, integrator/service record | Product-linked light-source allocation | ELSFP form-factor compatibility or generic laser capability |
| B-SUP-03 | Fibre / faceplate / connector | Corning collaboration on faceplate-to-chip assemblies (`CLM-529`) | Supplied assembly scope, qualified share, attach method, loss/yield/rework, spare/warranty owner | Corning, Broadcom, integrator, qualification report | Product-linked connectivity attribution | Collaboration quote or a historical TH5 dashboard |
| B-SUP-04 | Package / OSAT / test | Advanced substrate-level packaging architecture, no owner | Package/OSAT owner, test flow, acceptance criteria, final yield, rework and warranty allocation | Broadcom, TSMC, OSAT, OEM/customer qualification record | Final package/test attribution | Architecture image or previous-generation reliability test |
| B-SUP-05 | System / customer | Sampling, Limited Release and partner/demo routes (`CLM-077`, `CLM-530`, `CLM-543`) | Named customer and exact `BCM78919` configuration, acceptance date/count and repeat delivery | Customer, HPE/Celestica/Micas/Nexthop, Broadcom filing | Commercial numerator and repeatability gate | Tomahawk-family volume statement, product catalogue, demo or “Contact Sales” |

## Economics packet: required after a physical role is confirmed

Physical responsibility alone does not establish profit capture. For each
promoted supplier layer, open a second packet with the same SKU and period:

| Field | Required evidence | Invalid proxy |
|---|---|---|
| Content / supplier share | Contract, qualified supplier list, BOM, exact allocation or disclosed mix | Ecosystem membership, capacity, or a platform-owner list |
| Revenue / ASP | Realised price, contracted price, revenue-recognition policy or attributable product/segment revenue | Award value, backlog, TAM, acquisition earnout or company revenue |
| Yield / rework / test | Input, pass/fail, rework/scrap, test coverage/time and qualified output denominator | Engineering-sample yield, equipment capacity, or vendor “validated” language |
| Warranty / service | Failure population/exposure, repair/replacement route, reserve or service contract boundary | Replaceable interface, general warranty policy or historical lab test |
| Margin / return | Product/segment margin or reconciled cost stack; attributable capex/R&D | Consolidated gross margin, free cash flow or generic capex |

## Gate result

No packet presently meets the admission rule for an external supplier at an
exact NVIDIA or Broadcom CPO SKU. The only unambiguous exact-product owners
remain NVIDIA and Broadcom at their respective switch/SerDes platform layers.
The appropriate outcome is therefore a ranked evidence-acquisition queue—not
a CPO supplier-share or profit-pool conclusion.

Related controls: [six-company content-attribution register](../07-companies/six-company-content-attribution-register.md), [switch-CPO SKU reconciliation](../08-model/switch-cpo-sku-content-reconciliation.md), [commercial-proof acquisition plan](commercial-proof-evidence-acquisition-plan-2026-08-13.md), and [commercial-event eligibility matrix](../08-model/commercial-event-to-economic-eligibility-matrix.md).
