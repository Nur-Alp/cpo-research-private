# Supplier-attribution audit — exact-SKU versus route evidence

**Status:** Private control document; not a supplier ranking or revenue model
**As of:** 2026-08-12

The [exact-SKU attribution completeness matrix](exact-sku-attribution-completeness-2026-08-12.md)
is the compact release-control view of the layer-by-layer status below.

## Classification rule

- **Confirmed exact-SKU:** the retained source names the supplier role and the
  exact CPO product boundary.
- **Confirmed route:** the source names a process, platform or family role, but
  does not prove sellable content allocation to the exact SKU.
- **Candidate:** the company has relevant capability or a broader agreement,
  but no product-matched role is disclosed.
- **Open:** no retained source supports an attribution at that layer.

No state below unlocks ASP, share, yield, warranty or margin by itself. Those
economic fields require a product-matched BOM/contract and a qualified-output
record.

## Attribution-evidence hierarchy

The vocabulary below is mandatory whenever a supplier claim is added. It stops
an accurate technical statement from being promoted into a commercial claim.

| Evidence label | Minimum source content | What it can establish | What it must not establish by itself |
|---|---|---|---|
| **Exact product owner** | Names the exact switch ASIC/SKU and its owner | Platform/product ownership and architecture boundary | Customer acceptance, unit volume, ASP, platform margin or external supplier economics |
| **Product-linked route** | Names a process, assembly, collaboration or interface role tied to the exact product | A physical responsibility or integration route worthy of diligence | Complete sellable content, qualified supplier share, shipment, yield, warranty or margin |
| **Family/technology route** | Names a platform family, ecosystem, capability, standard or adjacent product | A relevant capability and potential supplier universe | Exact-SKU allocation, production use or commercial entitlement |
| **Demonstration / candidate** | Shows a prototype, tray, test vehicle or partnership with a relevant technical boundary | A possible implementation path and an evidence request | A deployed product BOM, repeat shipment, customer acceptance or revenue |
| **Exact economic attribution** | Names the exact product/layer plus qualified output or contract boundary and price, share, cost, yield, warranty or margin | A permitted company-specific model input, subject to the other commercial gates | A complete profit-pool conclusion unless the customer, scale and repeatability gates also clear |

**Application to the current records:** NVIDIA `CMP-083` is a
**family/platform process-route** map; it does not name `SN6800` or `SN6810`.
Corning `CMP-085` is a **demonstration/candidate** record involving Broadcom
silicon and Nexthop; it does not name `BCM78919` or TH6-Davisson. Neither can
be promoted into exact-SKU supplier allocation or a model input.

## Exact-SKU audit

| Layer | NVIDIA `SN6800`/`SN6810` | Broadcom `BCM78919`/TH6-Davisson | Current state | Economic field still missing |
|---|---|---|---|---|
| ASIC / SerDes | NVIDIA Spectrum-6 product owner | Broadcom BCM78919 / Condor SerDes product owner | **Confirmed exact-SKU** | Transfer price, optical-content allocation, platform gross margin |
| PIC / optical-engine | TSMC named for silicon-photonics fabrication and COUPE EIC/PIC integration | Broadcom/TSMC COUPE route described; complete engine supplier not named | **Confirmed route** | Wafer/die/package boundary, engine supplier, qualified share, ASP, yield |
| EIC / driver / TIA | No retained supplier allocation | No retained supplier allocation | **Open** | Supplier, die boundary, package, test yield, price |
| Laser / external light | TFC laser-die packaging/validation; Lumentum, Sumitomo and Coherent shared ELS assembly/alignment/test role at NVIDIA platform boundary | ELSFP topology and replaceability specified; supplier not named | **NVIDIA confirmed route; Broadcom open/candidate** | Laser die source, module share, delivered-power loss, replacement cost, warranty |
| Fibre attach | NVIDIA describes late-stage attach/screening; SENKO connector role is family-level | Corning discloses TH6 faceplate-to-chip collaboration and a separate Broadcom-silicon/Nexthop CPO-tray demonstration with Corning FAUs and optical management | **Confirmed process/collaboration route** | Attach owner, first-pass yield, rework, connector share, ASP |
| Connector / faceplate | SENKO detachable connector role for Spectrum-X/Quantum-X family | Corning TH6-specific connectivity collaboration | **Confirmed collaboration route** | Exact supplied assembly, qualified share, loss distribution, price, service liability |
| Package / assembly | SPIL bumping/sort/assembly/test for CPO MCM; Foxconn/Fabrinet system-level assembly/test and chassis integration | No exact TH6 package/OSAT owner | **NVIDIA confirmed route; Broadcom open** | Package scope, Cpk, rework, capex, cost per good engine |
| Test / qualification | NVIDIA says systems are validated before customer shipment; SPIL role broad | No TH6 test owner or acceptance distribution | **NVIDIA process route; Broadcom open** | Test seconds, coverage, escapes, final acceptance yield, warranty reserve |
| System integration | Foxconn named by NVIDIA | HPE/Celestica/Micas/Nexthop partner routes; no final allocation | **NVIDIA confirmed route; Broadcom candidate/route** | Product units, system ASP, ODM margin, customer acceptance |
| Field service / warranty | Dell policy covers CPO SKUs, but no observed fleet data | ELSFP replaceability; no TH6 field record | **Policy/interface only** | MTTR, spares, failures, reserve, replacement boundary |

## Company-specific control reading

| Company | What can be said now | What must not be said |
|---|---|---|
| NVIDIA | Owns the disclosed Spectrum-X platform and publishes the most detailed manufacturing responsibility map, including shared ELS and system-integration process roles | That TSMC, SPIL, TFC, Foxconn, Fabrinet, Lumentum, Sumitomo, Coherent or SENKO receive a known share of SN6800/SN6810 CPO revenue or margin |
| Broadcom | Owns the BCM78919/TH6 platform and specifies the engine/ELSFP architecture; Corning has a TH6 connectivity collaboration | That Broadcom, Corning, TSMC, Micas or any laser supplier has a proven TH6 CPO BOM, volume share or profit pool |
| TSMC | Important silicon-photonics/advanced-packaging process control point | Complete sellable CPO-engine ownership or CPO revenue allocation |
| Coherent | Broad SiPh/InP/laser capability and broader NVIDIA commercial route | Exact NVIDIA/Broadcom CPO engine share, order conversion or product margin |
| Lumentum | Strongest disclosed external-laser/ELS route and NVIDIA family role | CPO system revenue, exact laser share, yield, warranty or margin |
| Marvell | Accelerator-side optical-I/O/Photonic Fabric option value | Switch-side CPO deployment or profit leadership |

## Promotion rule

An attribution may move from route to exact-SKU only when a source names:

1. the exact CPO SKU/configuration;
2. the supplier's physical layer and responsibility boundary;
3. qualification or shipment status at that boundary; and
4. a product-matched share, price, yield or cost record.

Until then, the private model may use a labelled sensitivity range but must
leave company-specific supplier economics blocked. The public report may cite
the route evidence and state the gap, but may not publish inferred supplier
revenue or margin.

## Linked controls

- [Switch-CPO SKU content reconciliation](switch-cpo-sku-content-reconciliation.md)
- [CPO content-attribution map](cpo-content-attribution-map.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md)
- [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md)
