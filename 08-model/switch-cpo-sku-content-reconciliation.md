# Switch-CPO SKU content reconciliation

**Status:** Private attribution control; not a bill of materials, revenue model or supplier ranking  
**As of:** 2026-08-12  
**Purpose:** Keep the two decisive switch-CPO product boundaries separate while mapping what public sources actually identify.

See the [exact-SKU attribution completeness matrix](exact-sku-attribution-completeness-2026-08-12.md)
for the promotion rule from route evidence to product-matched supplier attribution.

## Controlled product boundaries

| Platform | Exact CPO product boundary | Commercial state permitted by retained evidence |
|---|---|---|
| NVIDIA | Spectrum-X Ethernet Photonics `SN6810` (102.4T) and `SN6800` (409.6T); Dell uses matching `SN6810-LD`/`SN6800-LD` ordering-family labels | First-party production/manufacturing-route language plus limited/select-partner shipping corroboration; no named accepted customer CPO numerator (`CLM-514`–`CLM-515`, `CLM-519`, `CLM-521`) |
| Broadcom | Tomahawk 6–Davisson `BCM78919`, 102.4T | Defined product and early-access / **Limited Release** status; “now shipping” language does not override the explicit sampling/lifecycle boundary without customer evidence (`CLM-076`–`CLM-077`, `CLM-530`) |

`SN6600-LD` is not a shorthand for NVIDIA CPO: the retained hardware documentation identifies it as a pluggable RHS-transceiver system. Nor can a general Tomahawk 6 production-volume statement be assigned to TH6-Davisson CPO. These are negative controls, not semantic details.

## Content-layer map

| Layer | NVIDIA Spectrum-X `SN6810` / `SN6800` | Broadcom TH6-Davisson `BCM78919` | Evidence status and boundary |
|---|---|---|---|
| Switch ASIC / SerDes | NVIDIA Spectrum-6 switch-CPO platform; 200G-SerDes product configurations disclosed | Broadcom BCM78919 with 64 Condor 3nm SerDes cores; 200G/lane | **Confirmed platform/product owner.** No CPO ASP or margin (`CLM-514`–`CLM-516`). |
| Engine count | `SN6810` has 32 × 3.2T SiPh engines | 16 × 6.4T Davisson DR engines | **Confirmed architecture denominators.** Not interchangeable and not dollar content (`CLM-076`, `CLM-515`). |
| PIC / optical-engine process | TSMC named for silicon-photonics fabrication; NVIDIA/TSMC COUPE process collaboration disclosed | TSMC COUPE technology-based engine route named by Broadcom | **Confirmed process route, not complete-engine supplier.** Wafer/die/package scope, allocation and margin remain open (`CLM-232`, `CLM-435`, `CLM-210`). |
| EIC / driver / TIA | No supplier allocation in retained product/manufacturing sources | SerDes architecture disclosed, but no EIC/driver/TIA supplier allocation | **Open for both.** Do not infer from COUPE naming or ASIC ownership. |
| External laser / light | TFC named for laser-die-module packaging and validation; Lumentum separately confirms a laser role in NVIDIA Spectrum-X/Quantum-X; source/die supplier and ELS commercial content undisclosed | Field-replaceable ELSFP interface; qualified laser/ELSFP supplier undisclosed | **NVIDIA: confirmed module-validation plus Lumentum ecosystem role; Broadcom: confirmed service interface.** Neither proves laser content/share/ASP (`CLM-435`, `CLM-536`, `CLM-076`–`CLM-077`). |
| Fibre attach / faceplate / connector | NVIDIA describes screening/fibre attachment; SENKO confirms detachable photonic connectors for Spectrum-X/Quantum-X, but does not allocate the complete attach process | Corning identifies collaboration on complete faceplate-to-chip optical assemblies for TH6-Davisson systems and separately demonstrates a Broadcom-silicon/Nexthop CPO tray using Corning FAUs/optical management | **NVIDIA: process/service architecture plus connector ecosystem role. Broadcom: SKU-specific collaboration plus an adjacent physical tray demonstration.** Neither gives attachment scope, yield, loss, price or warranty allocation (`CLM-406`–`CLM-410`, `CLM-537`, `CLM-529`, `CLM-565`). |
| Package / assembly / test | SPIL named for chip-scale package assembly and test; system validation before shipment stated | Advanced substrate-level multi-chip packaging stated; no OSAT/package/test owner disclosed | **NVIDIA: confirmed process role. Broadcom: architecture only.** Final yield/test coverage/rework/warranty are open (`CLM-435`–`CLM-436`, `CLM-210`). |
| System integration | Foxconn named by NVIDIA for system assembly | HPE/Celestica/Micas/Nexthop are partner-route signals; no confirmed system-assembly allocation for TH6 | **NVIDIA: confirmed system-assembly role. Broadcom: partner route.** Neither proves revenue/margin/capacity allocation (`CLM-435`, `CLM-246`–`CLM-249`). |
| Customer / unit / repeat deployment | Select-partner shipping corroborated; exact recipient, units, acceptance and repeat shipments open | Early-access samples; customer, units, acceptance and repeat shipments open | **Commercial-proof gate remains open for both.** (`CLM-521`, `CLM-077`). |
| Yield, rework, field service, warranty | Screening/validation language and OEM policy are not final-engine yield/field records | TH5 qualification context and ELSFP service boundary are not TH6 field/warranty data | **Open for both.** No cost-per-qualified-good-engine input is eligible. |
| Supplier share, ASP, gross margin | Not disclosed | Not disclosed | **Open for both.** No profit-pool ranking or EPS sensitivity is eligible. |

## Same-SKU attribution matrix

The matrix below applies the strictest rule in this research: a role may be
called **exact-SKU confirmed** only when the retained record names both the
company role and the specific product boundary. A company can therefore have a
confirmed *platform* or *process* role while remaining unconfirmed as the
supplier of sellable content for the SKU.

| Physical layer | NVIDIA `SN6810` / `SN6800` | Broadcom `BCM78919` / TH6-Davisson | Permitted model treatment |
|---|---|---|---|
| Switch ASIC / SerDes | **Exact product owner** — `CMP-054`, `CLM-514`–`CLM-515` | **Exact product owner** — `CMP-055`, `CLM-516` | Platform boundary only; no transfer price, customer units or margin. |
| PIC / optical-engine fabrication | **Platform process role** — NVIDIA names TSMC in `CMP-053`, `CLM-435`; no source says TSMC supplies the complete sellable engine for either SKU | **Technology route** — Broadcom names TSMC COUPE-based engines in `CLM-210`; no source says TSMC supplies the complete sellable engine | Route/process control point; no engine ASP, share, yield or profit. |
| EIC / driver / TIA | **Unallocated** — no retained source names a supplier at this boundary | **Unallocated** — SerDes architecture is disclosed, but EIC/driver/TIA content is not | Leave blank; do not infer from ASIC or COUPE ownership. |
| Laser / external light | **Exact platform process role** — TFC laser-die packaging/validation in `CMP-053`, `CLM-435`; Lumentum confirms a NVIDIA Spectrum-X laser role in `CMP-067`/`CLM-536`; laser-die source and commercial allocation open | **Exact product service boundary, supplier open** — field-replaceable ELSFP in `CMP-018`, `CLM-076`–`CLM-077` | Service/interface evidence only; no laser share, ASP, yield or warranty cost. |
| Fibre attach / connector | **Exact platform process description; supplier ecosystem role** — late attach/screening in `CMP-051`, `CLM-406`–`CLM-410`; SENKO confirms detachable connector supply in `CMP-068`/`CLM-537` | **SKU-specific collaboration, not BOM** — Corning faceplate-to-chip collaboration in `CLM-529`; 512-fibre boundary in `CMP-055`, `CLM-517` | Process/collaboration signal; no qualified share, loss distribution, rework or price. |
| Package / assembly | **Platform process role** — SPIL package/assembly/test and Foxconn system assembly in `CMP-053`, `CLM-435`–`CLM-436` | **Unallocated** — packaging architecture is disclosed, but no package/OSAT owner is named | Responsibility map only; no final-engine yield or supplier economics. |
| Test / qualification | **Platform validation claim** — pre-shipment validation in `CMP-053`, `CLM-436`; test scope and escapes open | **Unallocated** — no retained TH6 test owner, coverage, lot or acceptance record | Do not populate test cost, yield, warranty or field-return inputs. |

### Attribution conclusion

The only exact-SKU supplier role that is presently unambiguous is the
platform/ASIC owner. NVIDIA's named manufacturing chain is more detailed, but
it is still a first-party responsibility map rather than a customer-linked
bill of materials. Broadcom's TH6-specific Corning collaboration is more
product-specific than a generic ecosystem list, but its supplied boundary and
commercial allocation remain undefined. Neither company has a public
same-SKU map that reaches supplier share, qualified good-engine output,
realised ASP, warranty cost and gross margin. Those fields remain blocked in
the economic model.

## What can and cannot move across platforms

### Permitted comparison

- Both systems are defined 200G/lane switch-CPO routes with named TSMC-related photonics process evidence.
- Both use a serviceability strategy that keeps at least one optical/light or connector boundary outside the irreparable ASIC package.
- Both retain unfilled customer, final-engine yield and economics gates.

### Prohibited transfers

- Do not use NVIDIA’s 32-engine reference denominator for Broadcom’s 16-engine TH6, or vice versa.
- Do not use NVIDIA’s named TSMC/SPIL/TFC/Foxconn responsibility map as Broadcom’s supplier bill of materials.
- Do not use Corning’s TH6 connectivity collaboration as proof of an NVIDIA fibre supplier role.
- Do not use a broader Spectrum-X deployment, `SN6600-LD` deployment, Tomahawk-family production volume, or a partner quotation as a customer-accepted CPO unit numerator.
- Do not use either platform’s architecture or claimed power improvement as supplier profit, product gross margin or an all-in total-cost result.

## Decision implication

The public record now supports a **platform/process map**, not a fully attributable CPO value chain. NVIDIA currently has the more disclosed physical manufacturing-role map; Broadcom has the more explicit merchant product and a TH6-specific Corning connectivity collaboration. Neither system has a named customer accepted-unit record, an allocated engine BOM, final-engine yield/rework, field-service/warranty or economic record. Therefore neither can be declared the deployed-volume or profit-pool leader.

## Linked controls

- [Supplier-attribution audit](supplier-attribution-audit-2026-08-12.md)
- [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md)
- [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md)
- [Customer-proof register](customer-proof-register.md)
- [SKU-bound customer search audit](../09-primary-research/sku-customer-search-audit-2026-08-11.md)
- [SKU-bound supplier-attribution search audit](../09-primary-research/sku-supplier-attribution-search-audit-2026-08-12.md)
- [CPO content-attribution map](cpo-content-attribution-map.md)
- [Optical-engine profit-pool gates](optical-engine-profit-pool-input-gates.md)
