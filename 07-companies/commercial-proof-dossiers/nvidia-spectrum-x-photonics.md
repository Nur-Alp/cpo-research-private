# NVIDIA Spectrum-X Ethernet Photonics — commercial-proof dossier

**Status:** Private evidence synthesis; no publication or investment-call clearance  
**As of:** 2026-08-12  
**Decision:** Has NVIDIA demonstrated repeat, customer-confirmed switch-side CPO deployment?

## Current answer

**No — not on the public record retained here.** NVIDIA has a strong first-party production and manufacturing narrative for Spectrum-X Ethernet Photonics. The platform configuration is now specific (`SN6800` / `SN6810`; hardware-manual ordering-family labels `SN6800-LD` / `SN6810-LD`), but no retained source connects either CPO SKU to a named customer, accepted units/ports, delivery period and repeat-shipment record at the same boundary. The appropriate label is **defined CPO product plus first-party production/manufacturing-route evidence; commercial numerator open**.

## What is established

| Evidence | What it establishes | What it cannot establish |
|---|---|---|
| `PRI-033` / `CLM-346` | NVIDIA describes Spectrum-X Ethernet Photonics as a 200Gb/s-SerDes CPO switch “now in production” and names CoreWeave, Lambda and OCI as first ecosystem partners/adopters. | Customer-specific CPO SKU, accepted units, repeat volume, supplier share or CPO margin. |
| `CMP-053` / `CLM-435`–`CLM-436` | NVIDIA states the system is in full production; identifies TSMC (silicon photonics), SPIL (package/assembly/test), TFC (laser-module packaging/validation) and Foxconn (system assembly); says systems are validated before shipment. | The named companies’ allocation, engine ownership, contract economics, final yield, customer acceptance or field results. |
| `CMP-083` / `CLM-556`–`CLM-557` | NVIDIA specifies additional platform-level process roles: TSMC COUPE EIC/PIC integration; SPIL CPO multi-chip-module bumping/sort/assembly/test; shared Lumentum/Sumitomo/Coherent ELS assembly/alignment/test; and named fibre/connector/system-integration ecosystem partners. | Exact SN6800/SN6810 allocation, supplier share, laser-die or complete-module ownership, customer, units, qualification, price, yield, warranty or margin. |
| `CMP-054` / `CLM-514`–`CLM-515` | NVIDIA identifies `SN6800` (409.6T quad-ASIC) and `SN6810` (102.4T) liquid-cooled Spectrum-X Ethernet Photonics CPO system configurations; the 102.4T package contains 32 × 3.2T optical engines. | Which SKU each named adopter accepted, units/ports, repeat shipments, supplier allocation or economics. |
| `CMP-057` / `CLM-519` | Dell independently lists PowerSwitch `SN6800-LD` and `SN6810-LD` CPO products with MMC-12 interfaces, separately from the OSFP224 pluggable `SN6600-LD`. | Booked orders, Dell/customer acceptance, units/ports, repeat shipment, CPO content allocation, service data or economics. |
| `CMP-058` / `CLM-520` | Dell lists both CPO SKU families with three-year limited warranty and next-business-day onsite service. | Engine/package repair method, achieved MTTR, field failure, spare policy, warranty cost, customer fleet or supplier economics. |
| `CMP-048` / `CLM-564` | NVIDIA's current hardware manual sets nitrogen-pressure and liquid-flood deployment controls for SN6810-LD/SN6800-LD cooling systems. | Customer acceptance, field-failure/return rate, engine repair method, achieved MTTR, warranty cost, fleet size or supplier economics. |
| `NWS-013` / `CLM-521` | Focus Taiwan reports an NVIDIA networking-SVP statement that the Spectrum-X CPO switch had begun shipping to select partners at GTC Taipei. | The exact `SN6800`/`SN6810` configuration, recipient/customer, evaluation versus accepted deployment, units/ports, repeat delivery or economics. |
| `CMP-071` / `CLM-540` | Supermicro says it is integrating NVIDIA photonics switches into Vera Rubin NVL72/NVL8 rack-scale solutions through a pre-validated building-block framework. | Exact Ethernet CPO SKU, customer acceptance, accepted units/ports, repeat shipment, field service or economics; the statement groups Spectrum-X and Quantum-X. |
| `CMP-081` / `CLM-550` | Supermicro separately identifies `SN6800` and `SN6810` as CPO configurations while identifying `SN6600` as pluggable. | Customer acceptance, systems/ports, repeat delivery, field service, supplier allocation or economics. This is an architecture boundary, not a deployment numerator. |
| `CMP-072` / `CLM-541` | Dell describes Rubin AI Factory integration using SN6000 CPO options, illustrates SN6800-LD and positions the rack-scale systems as validated infrastructure. | Exact-SKU customer acceptance, accepted units/ports, repeat shipment, field service or economics; the team.blue quotation is not CPO proof. |
| `CMP-073` / `CLM-542` | NVIDIA's current silicon-photonics page lists CoreWeave, Lambda, Meta, Microsoft and OCI as first Spectrum-X Photonics adopters and states second-half-2026 availability. | Adopter-to-`SN6800`/`SN6810-LD` mapping, acceptance date, accepted units/ports, repeat shipment, field service or economics. |
| `CMP-077` / `CLM-546` | Lambda says it is preparing GB300 NVL72 and Vera Rubin NVL144 clusters to integrate both Quantum-X InfiniBand Photonics and Spectrum-X Photonics Ethernet. | Delivered Spectrum-X Ethernet SKU, accepted units/ports, repeat shipment, field service or economics; the exact Q3450-LD record is InfiniBand. |
| `CMP-078` / `CLM-547` | CoreWeave reports an 8,192-GPU benchmark using the Spectrum-X Ethernet platform. | Whether the benchmark used CPO or pluggable switches, exact SKU, accepted switch units/ports, repeat shipment or economics. |
| `CMP-051` / `CLM-406`–`CLM-410` | NVIDIA describes 512 200G-capable lanes, known-good-engine screening, final-stage fibre attachment and detachable fibre connectors. | End-to-end or final-engine “100% yield”; NVIDIA does not define the denominator, sample, rework, qualification or field-return rate. |
| `CMP-021`, `CMP-046`–`CMP-048` / `CLM-380`–`CLM-384` | CoreWeave separately reports early Photonics CPO adoption and a named SN6600-LD deployment. NVIDIA’s manual classifies the deployed SN6600-LD as a pluggable RHS-transceiver switch. | A linkage between CoreWeave’s CPO-adopter statement and the SN6600-LD; this deployment must not be counted as CPO volume. |
| `CMP-011` / `CLM-081` | Meta confirms Spectrum-X platform adoption. | Spectrum-X Photonics/CPO isolation, units, timing or economics. |

### Adjacent operator proof — useful, but not transferable to Spectrum-X Ethernet

`CMP-040` is a customer/operator-authored record of an NVIDIA **Quantum-X
InfiniBand Photonics Q3450-LD** early-access installation at Lambda. It identifies
the exact switch, a 4U/115.2 Tb/s configuration, 144 x 800G InfiniBand ports,
18 removable external-light modules, liquid cooling, busbar power and the
installation/service work required around the CPO boundary. This is stronger
operational evidence than a vendor product page and should inform the
serviceability and deployment-workflow analysis.

It does **not** clear the Spectrum-X Ethernet commercial-proof gate. Q3450-LD
is a different product family, fabric protocol, port configuration and customer
deployment boundary from `SN6800`/`SN6810`. Lambda's article also describes an
early look/engineering-sample context and does not disclose accepted fleet
units, repeat shipments, field returns or economics. The correct transfer is:

| What may transfer | What may not transfer |
|---|---|
| Evidence that NVIDIA can put a CPO switch into a customer rack; external-light/service and liquid-cooling diligence questions; installation workflow | Spectrum-X Ethernet customer acceptance; `SN6800`/`SN6810` units or ports; repeat shipments; Ethernet supplier allocation; Ethernet CPO margin or profit-pool leadership |

This adjacent record upgrades the **NVIDIA CPO operating-readiness** context,
not the **Spectrum-X Ethernet exact-SKU commercial numerator**.

### Current first-party product-page refresh (12 August 2026)

NVIDIA's current Ethernet-switch table identifies `SN6810-LD` and `SN6800-LD` as co-packaged-optics systems and states that Spectrum-X Ethernet Photonics is available in the second half of 2026. This strengthens the product-definition and vendor-timing record, but it is not a customer acceptance, shipment-denominator or repeat-delivery record. The live product page does not identify which operator has accepted either exact SKU or how many systems/ports were delivered. Keep this as **product availability evidence**, not customer-proof evidence.

Lambda's operator statement is a meaningful adoption-planning signal because it
names Spectrum-X Photonics Ethernet in future cluster integration. It still
groups Ethernet with Quantum-X InfiniBand and provides no delivered Ethernet
SKU or unit denominator. The separate Lambda Q3450-LD unboxing therefore cannot
be counted as Spectrum-X Ethernet volume.

The current evidence uses two different lifecycle statements that must remain separate: NVIDIA's GTC/production material says the full-stack system is in full production and validates systems before customer shipment, while the live product table gives second-half-2026 availability for the CPO configurations. This can be read as production readiness preceding broad availability, but it does not resolve customer acceptance, delivered units or repeatability. Treat the difference as a timing-boundary note, not as contradictory evidence or a volume estimate.

## Product boundary

The systems under review are **SN6800** (409.6T) and **SN6810** (102.4T), the disclosed Spectrum-X Ethernet Photonics switch-side 200G-SerDes CPO configurations. NVIDIA's technical architecture blog uses those base product labels; the hardware manual uses the corresponding **SN6800-LD** and **SN6810-LD** CPO ordering-family labels (`CLM-381`, `CLM-514`). Treat them as a controlled naming cross-reference, not proof that a customer deployment of one spelling is a shipment of the other without a source that ties the configuration to a purchase or acceptance.

They must remain distinct from Quantum-X Photonics/InfiniBand and from the **SN6600-LD** pluggable Ethernet deployment. A platform/adopter statement, a pluggable switch deployment, and a CPO SKU shipment are three separate evidence classes.

## Supplier-content map — evidence-adjusted

| Layer | Public responsibility signal | Confidence | Not established |
|---|---|---|---|
| Switch ASIC / SerDes / system route | NVIDIA; Dell is a confirmed OEM/channel product route for `SN6800-LD`/`SN6810-LD` | High for product route | Retained CPO gross profit, buyer economics or Dell shipment/acceptance |
| Silicon-photonics fabrication | TSMC named by NVIDIA; COUPE EIC/PIC integration is explicitly described | Medium | Wafer/engine share, ASP or margin |
| EIC / driver / TIA | NVIDIA describes the integrated 200G CPO architecture, but does not allocate the electronic interface or driver/TIA content by supplier | Low for allocation | EIC/driver/TIA supplier, package boundary, qualified share, ASP, margin and warranty ownership |
| Package, assembly and test | SPIL named by NVIDIA; the technical map says bumping, wafer sort, assembly and testing for NVIDIA's CPO multi-chip module | Medium | Exact package scope, test time, yield or warranty |
| External laser source | TFC named for laser-module packaging/validation; Lumentum, Sumitomo and Coherent are named jointly for ELS assembly, optical alignment and test | Medium for shared process role | Laser die source, ELS content allocation, ASP, redundancy or margin |
| Rack integration | Foxconn and Fabrinet are named for system-level CPO assembly/test and chassis integration; Foxconn separately forecasts generic CPO-switch mass production in Q3 2026 | Medium for role; low for SKU linkage | CPO-specific system value-add or economics; the role map does not name an exact SKU or allocation |
| OEM service/warranty route | Dell lists three-year limited warranty and NBD onsite service for SN6800-LD/SN6810-LD | Medium for policy | Engine/package repair workflow, achieved MTTR, field-return rate and warranty cost |
| Engine/PIC, fibre attach, connectors | NVIDIA describes architecture/process; technology-partner page names candidates | Low for allocation | Named qualified supplier per SKU and all content shares |

### Product-family supplier confirmations (not complete BOMs)

Two supplier announcements narrow the NVIDIA route without clearing the
commercial numerator. Lumentum says its high-power lasers have a crucial role
in the development and deployment of **Spectrum-X Photonics** and Quantum-X
Photonic switches (`CMP-067`). SENKO says it supplies detachable photonic
connectors for both switch families (`CMP-068`). These are stronger than a
generic ecosystem list because each supplier describes its own role, but neither
announcement names `SN6800`/`SN6810`, a customer acceptance, a qualified share,
price, yield, warranty or margin.

Coherent's 2026 strategic agreement with NVIDIA adds a separate commercial
signal: a multibillion-dollar purchase commitment and future capacity rights
for advanced laser and optical-networking products (`CMP-069`). The public
scope is deliberately broader than CPO and does not permit allocation to
Spectrum-X Ethernet. It should inform the supplier-capacity watchlist, not a
CPO revenue or profit forecast.

No row above is a supplier-revenue assumption. Partnership or manufacturing-role evidence is not equivalent to an engine bill of materials or retained profit.

## Commercial-proof gate

| Required field | Current status | Evidence needed |
|---|---|---|
| Exact CPO SKU/configuration | **Pass:** `SN6800` / `SN6810` configurations disclosed | Product definition alone does not establish a customer deployment |
| Exact customer CPO SKU/configuration | Open | Customer/operator deployment record naming `SN6800`/`SN6810` or the matching `-LD` ordering-family label, with an unambiguous CPO configuration |
| Acceptance / qualification date | Open | Customer statement, qualification filing, or procurement evidence |
| Units / ports / systems | Open | Defined CPO shipment or installed-base denominator |
| Repeat shipment / expansion | Open | Second delivery, expansion, renewal, or recurring order record |
| Field service / reliability | **Partial procedure only:** OEM warranty policy and NVIDIA cooling-handling instructions exist; neither is observed field performance | MTBF/return, engine replacement procedure, achieved MTTR, spares, warranty allocation and operating history |
| Product-linked supplier allocation / economics | Open | Named qualified supplier role plus content share, ASP, product margin, yield/rework and warranty boundary |

## Timing implication and falsification

**Current inference:** NVIDIA’s production and manufacturing-route disclosures support a meaningful 2026–2027 verification window, but not a claim of broad switch-side CPO adoption.

Upgrade only when a named operator links a specific Spectrum-X Photonics CPO SKU to dated accepted units and a repeat deployment. Downgrade the timing case if production language remains unaccompanied by an identifiable customer CPO configuration and repeat shipment evidence, or if a customer reverts to a pluggable/LPO/NPO architecture for service, yield or qualification reasons.

## Source boundary

Primary retained sources: `PRI-033`, `CMP-051`, `CMP-053`, `CMP-054`, `CMP-057`, `CMP-058`, `CMP-021`, `CMP-046`–`CMP-048`, `CMP-011`, `CMP-071`, `CMP-072`, `CMP-073`, `CMP-077`–`CMP-079`, `CMP-081`, `CMP-083`. Adjacent operator CPO record: `CMP-040` (Quantum-X InfiniBand Q3450-LD; not transferable to Spectrum-X Ethernet). Independent shipment-status corroboration: `NWS-013`. Foxconn's generic manufacturing outlook is retained as `CMP-060` / `CLM-526`–`CLM-527`, but is not evidence of an NVIDIA SKU shipment. The exact-SKU search cycle is logged in [exact-SKU commercial-proof search audit](../../09-primary-research/exact-sku-commercial-proof-search-audit-2026-08-12.md). Claim IDs above are the system of record. This dossier makes no CPO revenue, EPS, market-share, margin or supplier-allocation forecast.

Current live product reference reviewed 12 August 2026: [NVIDIA Ethernet Switching](https://www.nvidia.com/en-us/networking/ethernet-switching/). It is used only for the product-table and availability boundary described above; no new customer-volume claim is created from it.
