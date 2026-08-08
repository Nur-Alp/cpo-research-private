# CPO content-attribution map

**Owner:** Nur Alpys  
**Status:** Evidence-gated control map; not a revenue forecast  
**Scope:** 102.4T switch-side CPO and 200G-per-lane optical-engine layers  
**As of:** 2026-08-08

## Purpose

This map separates the physical content in a CPO system from the company that publicly claims the platform. It is the control document for preventing a Broadcom or NVIDIA switch announcement from being counted as Coherent, Lumentum or TSMC optical-engine revenue without a supplier and pricing record.

The map is deliberately asymmetric: a disclosed architecture can establish that a layer exists, while the supplier, transfer price, qualified share and margin remain unknown.

## Product boundary

The reference system is Broadcom's disclosed 102.4T TH6-Davisson architecture: sixteen 6.4T optical engines and 200G-per-link operation.[CLM-076] The reference engine is therefore a system-content boundary, not a claim that every supplier provides sixteen complete engines or that the platform is in broad production.

```text
switch ASIC / SerDes
        ↓
EIC + PIC / optical engine
        ↓
laser or ELSFP + fibre distribution
        ↓
fibre attach / connector / package / thermal path
        ↓
test, qualification, service and warranty
```

## Attribution matrix

| Layer | What is established | Company or route implicated | What cannot be attributed yet | Evidence gate |
|---|---|---|---|---|
| Switch ASIC and SerDes | Broadcom specifies the TH6-Davisson switch and 200G electrical links; NVIDIA's 2026 release states Spectrum-X Ethernet Photonics is a 200Gb/s-SerDes CPO switch now in production.[CLM-076; CLM-346] | Broadcom or NVIDIA platform owner | CPO-specific ASP, margin, optical-engine transfer price and displaced retimer/plug revenue | Platform SKU, units and customer confirmation |
| EIC / PIC integration | Broadcom names TSMC COUPE technology-based optical engines; TSMC describes COUPE as EIC/PIC integration and reports a customer-linked 200G result.[CLM-210; CLM-213; CLM-218] | TSMC process route; Broadcom platform integration | Whether TSMC supplies wafers, bonded dies, a complete engine or only a process; Broadcom's internal content and margin | Supplier responsibility map and qualified package boundary |
| Optical engine count | Broadcom discloses sixteen 6.4T optical engines in TH6-Davisson; NVIDIA separately describes 3 COUPE engines per Quantum-X subassembly and 32 engines in a Spectrum-X package.[CLM-076; CLM-233; CLM-235] | Broadcom and NVIDIA platform architectures; TSMC COUPE route | Dollar content per engine, number of PICs/lasers per engine, good-engine output and supplier share; the counts are not interchangeable across platforms | Product BOM or teardown tied to a named SKU |
| Laser / external light | Broadcom identifies field-replaceable ELSFP modules; Lumentum and Coherent disclose UHP/high-power InP and ELS/ELSFP routes.[CLM-071; CLM-068; CLM-083] | Broadcom system boundary; Lumentum/Coherent candidate suppliers | Which supplier is qualified, laser count, split ratio, delivered power after distribution, ASP and replacement/warranty allocation | Named SKU, qualification record and fibre-power tree |
| Strategic supplier route | NVIDIA has executed $2B investments and multiyear purchase/capacity agreements with both Coherent and Lumentum, and its platform page lists a wider technology-partner ecosystem.[CLM-197; CLM-198; CLM-229] | Coherent, Lumentum, TSMC, Corning, Fabrinet, Foxconn, Senko, SPIL, Sumitomo and Browave are candidate ecosystem participants. Fabrinet's filings add a full outsourced optical-packaging, DCI/HPC, NPI and fixed-price/yield-risk boundary.[CLM-265–CLM-272] | The agreements and partner list are nonexclusive/product-unallocated: they do not establish who supplies the CoreWeave SN6600-LD, Lambda Quantum-X cluster, Broadcom TH6 or any specified CPO engine. Fabrinet's DCI/HPC revenue is not CPO revenue. | Product allocation, named SKU, qualified share, shipment, yield waterfall, warranty terms and price records |
| Fibre distribution and attach | IBM, Corning, Furukawa and Ayar papers demonstrate process mechanisms or connector prototypes; NVIDIA describes detachable connectors and wafer-level micro-lenses intended for automated assembly.[CLM-019; CLM-101; CLM-102; CLM-103; CLM-236; CLM-238] | Packaging/OSAT/connector supply chain is unresolved | Attach yield, cycle time, rework, loss distribution, ownership and price | Final-engine lot data and contract/content map |
| Thermal and mechanical package | TSMC reports >99% engineering-sample 3D-stacking yield; packaging papers model or measure sub-boundaries, not a qualified TH6 engine.[CLM-216; CLM-101] | TSMC plus package/assembly partners; exact split unknown | Final package yield, thermal margin, service procedure, field-return rate and depreciation | Qualification dossier and production yield waterfall |
| Test and acceptance | Academic work supplies candidate metrology and known-good-die flows; no public CPO supplier reports production acceptance distributions.[CLM-019; CLM-020] | Supplier, OSAT and platform owner responsibility unknown | Test time, escape rate, acceptance yield, rework cost and warranty reserves | Manufacturing/test records |
| System design, assembly and manufacturing | Celestica reports an awarded design-and-manufacturing program for an unnamed hyperscaler CPO Ethernet switch, using 1.6T silicon, co-packaged optical interconnects and liquid cooling, with a planned 2027 ramp.[CLM-255; CLM-256] | Celestica as a possible system-integration/ODM route; Broadcom as a named TH6 partner route | Whether Celestica performs CPO package integration, optical attach, test, burn-in, final acceptance or field service; retained system ASP and margin | Product-level program BOM, scope, units, yield, ASP and contract terms |
| Platform service and warranty | Broadcom's ELSFP is replaceable; NVIDIA describes an eight-laser ELS module as field-replaceable and gives reference counts for Spectrum-X, but engine/package replacement and warranty terms remain undisclosed.[CLM-077; CLM-081; CLM-237] | Platform owner and field-service channel | MTTR, spares, failure-domain allocation, contract liability and cannibalised service revenue | Field procedure, warranty terms and return data |

## Current control-point reading

- **Broadcom** has the clearest disclosed switch-level content map, but not the supplier economics.
- **NVIDIA** has the clearest disclosed customer/platform route, but not the optical bill of materials.
- **TSMC** has the clearest public COUPE process/stacking control point, but not complete-engine revenue ownership.
- **Coherent** has the broadest public candidate component stack; its complete-engine share and yield remain unproven.
- **Lumentum** has the clearest external-laser/ELSFP product and order signal; its content may be narrower than a full engine.

These are control-point observations, not a profit ranking. The ranking changes only when a supplier-linked SKU, qualified output, realised price and margin are available.

## Required records to clear attribution

1. A customer or platform-owner record naming the exact CPO SKU and production units.
2. A supplier bill of materials identifying PIC, EIC, laser/ELSFP, fibre attach, package and test ownership.
3. A qualified-engine yield waterfall and field-replacement/warranty allocation.
4. A product ASP or contract price, qualified supplier share and price-down schedule.
5. A capex and capacity map that connects the line to the same product boundary.

Until these records exist, use the system architecture to define the denominator only; do not multiply sixteen engines by a presumed supplier ASP or company-wide margin.

The NVIDIA–Coherent and NVIDIA–Lumentum agreements are therefore **route evidence, not attribution evidence**. They increase the prior probability that each supplier can participate in future photonics volume, but they do not permit assigning customer deployments, CPO revenue or optical-engine profit to either supplier.[CLM-197][CLM-198]

The May 2026 NVIDIA production statement changes the commercial-timing state but not the attribution rule: a production claim and named ecosystem partners still do not identify the exact customer SKU, optical BOM, supplier share, transfer price or final-engine yield.[CLM-346][CLM-350]

## Linked controls

- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Company evidence-gap matrix](../07-companies/company-evidence-gap-matrix.md)
- [Broadcom and NVIDIA switch-CPO dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum matched profit bridge](coherent-lumentum-matched-engine-profit-bridge.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
