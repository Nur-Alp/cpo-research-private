# Six-company CPO content-attribution register

**Status:** Private evidence control; not a revenue model or supplier-ranking table  
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, TSMC and Marvell  
**As of:** 2026-08-12

## Reading rule

Each row refers to the **physical/economic layer**, not merely the company most associated with a platform. The permitted status labels are:

- **Confirmed role:** the retained record identifies the company’s role at the stated layer.
- **Route / candidate:** a partnership, technology route, demonstration or capacity relation exists, but no named SKU/content allocation is shown.
- **Open:** no retained record attributes that layer at the relevant CPO product boundary.
- **Outside switch-CPO boundary:** important optical-I/O work, but not evidence of a 200G/lane switch-CPO role.

“Confirmed role” never means confirmed revenue, supplier share, ASP, final-engine yield or margin unless those fields are separately disclosed.

## Cross-company layer control matrix

This matrix is a comparability control. **Exact/product** means a role is tied to the relevant announced product boundary; **route** means a technology, partnership or capacity signal exists without product allocation; **open** means no retained attribution; **outside** means the company’s relevant work is not evidence of switch-side 200G/lane CPO. No cell below is a revenue, share or margin estimate.

| Company / boundary | ASIC / SerDes | PIC / engine | EIC / driver / TIA | Laser / ELSFP | Fibre attach / connector | Package / assembly | Test / qualification | Economic attribution |
|---|---|---|---|---|---|---|---|---|
| NVIDIA Spectrum-X Ethernet Photonics | **Exact/product** | **Route**: TSMC SiPh fabrication / COUPE EIC-PIC integration (`CMP-083`) | **Open** | **Confirmed shared process role**: Lumentum, Sumitomo and Coherent provide ELS assembly/alignment/test; TFC laser-module packaging/validation. No allocation or laser-die ownership (`CMP-053`; `CMP-083`) | **Route/confirmed ecosystem role**: final attach process plus SENKO detachable PIC connector role (`CMP-068`); shared fibre/connector ecosystem names in `CMP-083`; complete attach ownership open | **Route**: SPIL package/assembly | **Route**: SPIL/test and pre-shipment validation | **Open**: no share, ASP, yield/rework, warranty or margin |
| Broadcom TH6-Davisson / `BCM78919` | **Exact/product** | **Exact architecture; route**: TSMC COUPE technology | **Open** | **Exact interface; supplier open**: field-replaceable ELSFP | **Route**: Corning faceplate-to-chip collaboration; historical Micas qualification dashboard is prior-generation precedent only (`CMP-070`); TH6 attach owner open | **Open** | **Open** | **Open**: no supplier allocation, ASP, yield/rework, warranty or margin |
| Coherent component/engine routes | **Outside product allocation** | **Route/candidate**: SiPh, InP, VCSEL and engine demonstrations | **Open** | **Route/candidate**: high-power InP/external-light; NVIDIA multiyear purchase/capacity agreement is broad and product-unallocated (`CMP-069`) | **Open** | **Open** | **Open** | **Open**: no named production SKU/share/margin |
| Lumentum external-light route | **Outside product allocation** | **Open** | **Open** | **Route/confirmed ecosystem role**: UHP laser and ELSFP; Lumentum identifies a role in NVIDIA Spectrum-X and Quantum-X development (`CMP-067`) | **Route boundary**: replaceable light; fibre/engine attach open | **Open** | **Open** | **Open**: order/ecosystem signal lacks product allocation, customer, share, ASP and margin |
| TSMC COUPE process route | **Outside product ownership** | **Exact process route**: COUPE SiPh/EIC integration | **Exact process route**: EIC/PIC integration | **Open** | **Open** | **Route/process**: 3D stacking/package integration | **Route/process**: engineering-sample yield, not final-engine qualification | **Open**: no complete-engine scope, ASP or CPO margin |
| Marvell / Celestial Photonic Fabric | **Outside switch-CPO boundary** | **Route/candidate outside switch-CPO**: accelerator optical-I/O chiplet | **Route/candidate outside switch-CPO** | **Open** | **Open** | **Open** | **Open** | **Open**: no named XPU/customer production economics |

**Interpretation:** NVIDIA and Broadcom are the only rows with exact switch-product boundaries. Coherent, Lumentum and TSMC can be important component/process beneficiaries without being proven suppliers to a named switch SKU; Marvell remains a separate accelerator optical-I/O thesis. The economic column stays open for all six companies.

## NVIDIA Spectrum-X Ethernet Photonics

| Layer | Status | Retained evidence and boundary | Still open |
|---|---|---|---|
| Switch ASIC / SerDes | Confirmed role | NVIDIA defines the SN6800/SN6810 200G-SerDes CPO configurations; Dell independently carries the matching `-LD` CPO configurations as PowerSwitch products (`CLM-514`–`CLM-515`, `CLM-519`). | Customer SKU/units; platform ASP/margin. |
| PIC / optical-engine fabrication | Confirmed process role | NVIDIA names TSMC for silicon-photonics fabrication and separately describes TSMC COUPE EIC/PIC integration (`CLM-435`; `CLM-556`). | Wafer versus die/engine scope; yield, share, price and margin. |
| EIC / driver / TIA | Open | NVIDIA describes the integrated optical architecture but allocates no EIC/driver/TIA supplier. | Design owner, fabrication/package boundary, share and economics. |
| Laser / external light | Confirmed shared process and module-validation roles | NVIDIA names TFC for laser-die-module packaging and validation (`CLM-435`). NVIDIA separately identifies Lumentum, Sumitomo and Coherent as shared providers of ELS assembly, optical alignment and test with the silicon-photonics engine (`CLM-556`); Lumentum also identifies its high-power laser ecosystem role (`CMP-067`, `CLM-536`). | Laser-die source, ELS topology, quantity, redundancy, qualified share, work allocation and economics. |
| Fibre attach | Route only | NVIDIA describes final-stage fibre attachment/screening (`CLM-406`–`CLM-410`). | Attach owner, automation rate, first-pass yield, rework and cost. |
| Package | Confirmed process role | NVIDIA names SPIL for chip-scale package assembly; its technical record specifies wafer bumping, wafer sort, assembly and testing for the CPO multi-chip module (`CLM-435`; `CLM-556`). | Exact scope, final-package yield, thermal qualification and warranty allocation. |
| Connector / service boundary | Partially scoped; ecosystem supplier identified | NVIDIA describes detachable connectors/external-light service concepts; SENKO identifies detachable PIC connectors for Spectrum-X and Quantum-X (`CMP-068`, `CLM-537`); Dell lists NBD system-level repair/replacement coverage for both CPO SKU families (`CLM-237`, `CLM-520`). | Whether SENKO is allocated to the exact customer SKU, mating-life, complete attach ownership, engine replacement process, achieved MTTR and warranty cost. |
| Test | Confirmed process role | NVIDIA names SPIL for assembly/test and says systems are validated before shipment; the technical record separately assigns ELS alignment/test to a shared Lumentum/Sumitomo/Coherent group (`CLM-435`–`CLM-436`; `CLM-556`). | Coverage, test time, escape rate, final acceptance, allocation and field returns. |

## Broadcom TH6-Davisson / BCM78919

| Layer | Status | Retained evidence and boundary | Still open |
|---|---|---|---|
| Switch ASIC / SerDes | Confirmed role | Broadcom specifies BCM78919 and integrated 3nm Condor SerDes (`CLM-516`). | CPO-specific price, margin and customer-unit denominator. |
| PIC / optical-engine | Confirmed architecture; route-only supplier attribution | Broadcom specifies integrated engines and publicly names the TSMC COUPE technology route (`CLM-076`, `CLM-210`). | PIC/EIC ownership, complete-engine supplier, qualified share and transfer price. |
| EIC / driver / TIA | Open | SerDes are disclosed, but the product records do not allocate EIC/driver/TIA content. | Owner, package interface and economics. |
| Laser / external light | Confirmed service interface; supplier open | TH6 includes field-replaceable ELSFP modules (`CLM-076`–`CLM-077`). No retained supplier record allocates a laser/ELSFP to TH6. | Qualified laser/ELSFP supplier, laser count/split ratio, ASP, reliability and warranty. |
| Fibre attach / faceplate connectivity | Route-specific collaboration | Broadcom's TH6 release quotes Corning on complete faceplate-to-chip optical assemblies for TH6-Davisson systems; 512 duplex fibres and direct engine drive are separately disclosed (`CLM-517`, `CLM-529`). | Exact attach/assembly scope, qualified share, cycle time, loss/yield/rework, cost and warranty. |
| Package | Open | CPO integration is disclosed; package/OSAT allocation is not. | Assembly scope, thermal qualification, final-engine/package yield and capex. |
| Connector / service boundary | Partially scoped | ELSFP defines an external-light replacement boundary. | Engine/package connector, field workflow, spares, MTTR and warranty. |
| Test | Open | No public test owner, coverage, acceptance or failure data. | Wafer/engine/package/system test flow and economics. |

## Coherent

| Layer | Status | Retained evidence and boundary | Still open |
|---|---|---|---|
| PIC / optical engine | Route / candidate | Coherent demonstrates SiPh CPO and related optical-engine routes (`CLM-068`). Its NVIDIA purchase/capacity agreement is a strategic route signal, not a CPO SKU allocation (`CMP-069`, `CLM-538`). | Named production SKU, customer allocation, engine share, ASP, final yield and margin. |
| EIC / driver / TIA | Open | No retained product allocation. | Supplier/content, integration route and economics. |
| Laser / external light | Route / candidate | Coherent demonstrates external-light/high-power InP routes (`CLM-068`); its NVIDIA agreement provides broad capacity/purchase visibility but does not identify CPO product content (`CMP-069`, `CLM-538`). | Product allocation, delivered-power tree, qualified share, lifetime and margin. |
| Fibre attach / package / connector / test | Open | Demonstration and technology breadth do not expose a production responsibility map. | Owner, yield, rework, qualification, service and warranty. |
| Switch ASIC / SerDes | Outside supplier boundary | Coherent is assessed as a candidate component/engine supplier, not a switch-ASIC owner. | Any customer-specific content relationship. |

## Lumentum

| Layer | Status | Retained evidence and boundary | Still open |
|---|---|---|---|
| Laser / ELSFP | Confirmed product and ecosystem boundary | Lumentum specifies UHP/ELSFP and external-light routes (`CLM-071`–`CLM-072`) and identifies its high-power lasers as part of the NVIDIA Spectrum-X and Quantum-X photonics ecosystem (`CMP-067`, `CLM-536`). | Named CPO SKU/customer, exact laser allocation, quantity, ASP, qualified share, lifetime and margin. |
| PIC / engine / EIC | Open | ELSFP/light-source product is not a complete-engine allocation. | PIC/engine/EIC ownership, package/test share and economics. |
| Fibre attach / connector | Partially scoped | ELSFP makes the light source serviceable. | Fibre-distribution/attach responsibility, engine connector, loss, rework and service cost. |
| Package / test | Open | No final-engine package/test boundary is allocated. | Qualification, yield, warranty and cost. |
| Switch ASIC / SerDes | Outside supplier boundary | Lumentum is assessed as a laser/component candidate, not a switch-ASIC owner. | Any product-specific system share. |

## TSMC

| Layer | Status | Retained evidence and boundary | Still open |
|---|---|---|---|
| PIC / EIC integration | Confirmed process/control route | TSMC describes COUPE EIC/PIC integration and reports a customer-linked 200G result; Broadcom names COUPE-based engine technology (`CLM-210`, `CLM-213`–`CLM-216`). | Wafer/die/package/complete-engine economic boundary, yield at final-engine level, customer SKU, price and margin. |
| Package / 3D integration | Confirmed engineering route | TSMC reports >99% engineering-sample 3D-stacking yield (`CLM-216`). | Production accepted yield, rework, test escape, service ownership and financial allocation. |
| Laser / fibre attach / connector / test | Open | The retained records do not allocate these layers to TSMC in a CPO system. | Supplier map, final qualification and economics. |
| Switch ASIC / SerDes | Route only | TSMC is an enabling foundry/packaging control point; it is not established as a merchant-switch product owner. | Any CPO-specific output/value capture. |

## Marvell / Celestial AI

| Layer | Status | Retained evidence and boundary | Still open |
|---|---|---|---|
| Optical-I/O PIC/EIC chiplet | Route / candidate outside switch-CPO | Celestial’s Photonic Fabric is a 16Tb/s accelerator optical-I/O chiplet (`CLM-094`). | Named XPU/customer, production units, optical-engine content, margin and yield. |
| Switch ASIC / SerDes | Outside switch-CPO boundary | The retained product thesis is accelerator scale-up optical I/O, not a named 200G/lane switch-CPO system. | A relevant switch-CPO SKU or customer allocation. |
| Laser / attach / package / connector / test | Open | No retained product-level responsibility map matches an announced switch-CPO system. | Component ownership, qualification, service and economics. |

## Cross-company conclusion

The record supports **process and platform role mapping**, not a complete supplier bill of materials:

- NVIDIA has the most specific disclosed physical responsibility chain, but no supplier share or economic allocation.
- Broadcom has the clearest merchant-switch/SerDes/product boundary, but its PIC/EIC/laser/package/test attribution remains incomplete.
- Coherent and Lumentum have credible candidate component routes, not customer-linked engine-content proof.
- TSMC has a credible PIC/EIC integration control point, not demonstrated complete-engine profit ownership.
- Marvell is an accelerator-optical-I/O watch case, not comparable switch-CPO proof.

No company should be assigned CPO revenue, product gross margin or a profit-pool leadership score until the same SKU has a customer denominator, content/share map, qualified output and realised economics.

## Linked controls

- [CPO content-attribution map](../08-model/cpo-content-attribution-map.md)
- [Commercial-proof dossiers](commercial-proof-dossiers/README.md)
- [Core-company variant cards](variant-cards/core-company-variant-cards.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
