# CPO evidence-gate register

**Owner:** Nur Alpys  
**Status:** Active diligence queue; not a forecast  
**As of:** 2026-08-07

This register translates the unresolved fields in the company dossiers into auditable research tasks. A gate is “cleared” only when the record identifies the product boundary, architecture, date, unit and source quality. A company announcement can establish a claim, but cannot by itself clear an independent production, yield, margin or field-reliability gate.

## Priority queue

| Priority | Gate / missing input | Companies or architecture | Why it changes the thesis | Evidence that would clear it | Current anchor |
|---|---|---|---|---|---|
| P0 | Customer-confirmed production SKU, units, ports and deployment date | Broadcom TH6-Davisson; NVIDIA Spectrum-X Photonics | Converts vendor “shipping/production” language into a commercial-proof numerator | Customer filing, named deployment statement, or repeat shipment record identifying CPO configuration | `CLM-077`, `CLM-079`, `CLM-081`; [switch dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md) |
| P0 | Complete engine bill of materials and supplier responsibility map | Broadcom, NVIDIA, Coherent, Lumentum | Determines who captures optical-engine content and prevents double counting platform and component rent | Product teardown, contract disclosure, supplier statement with engine/PIC/laser/package ownership | `CLM-076`, `CLM-068`, `CLM-071`; [profit-pool gates](optical-engine-profit-pool-input-gates.md) |
| P0 | Final-engine yield waterfall, attach cycle time, rework and scrap | All complete-engine suppliers | Converts technical feasibility into realised gross margin and capacity | Manufacturing paper with lots and Cpk, customer qualification dossier, or primary factory evidence | `CLM-019`, `CLM-020`, `CLM-101`; [packaging benchmark](../03-components/packaging-reliability-benchmark.md) |
| P0 | Product ASP, realised CPO margin and price-down schedule | Coherent, Lumentum, Broadcom, NVIDIA | Determines whether the opportunity is profitable rather than merely revenue-generating | Product-level filing, contract, earnings disclosure or defensible primary supply-chain research | `CLM-070`, `CLM-073`, `CLM-083`; [supplier dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md) |
| P0 | Field reliability, engine replacement and warranty allocation | CPO platforms, ELSFP and optical engines | Tests serviceability, failure-domain claims and support-cost leakage | Field-return/MTBF data, qualification report, warranty reserve or service procedure | `CLM-071`, `CLM-081`, `CLM-192`; [external-light boundary](../03-components/external-light-serviceability-boundary.md) |
| P1 | Matched 200G/lane electrical boundary versus LPO/NPO/CPO | Scale-out Ethernet | Determines whether CPO is technically needed at the target topology | Multi-vendor measured link with reach, loss, return loss, FEC, BER, temperature and power | `CLM-057`, `CLM-059`, `CLM-063`; [linear-drive benchmark](../02-architecture/linear-drive-boundary-benchmark.md) |
| P1 | Measured 400G/lane end-to-end link | 400G LPO versus NPO/CPO | Establishes whether the 400G electrical boundary actually forces optics inward | Measured 212.5-GBd/400G lane link, not component-only or modeled data; public standards material currently supplies context rather than an adopted 400G/lane channel budget | `CLM-065`, `CLM-066`, `CLM-067`, `CLM-201`–`CLM-205`; [linear-drive benchmark](../02-architecture/linear-drive-boundary-benchmark.md) |
| P1 | Delivered optical power after splitters, connectors and fibre attach | External laser / ELSFP architectures | Tests whether high-power laser headlines survive the complete distribution path | Multi-channel loss distribution over temperature and life without lab-only amplification | `CLM-106`, `CLM-108`; [laser benchmark](../03-components/laser-architecture-benchmark.md) |
| P1 | Laser lifetime, redundancy and replaceability at the engine boundary | Lumentum, Coherent, external-light CPO | Determines warranty inventory and whether ELSFP serviceability has economic value | Accelerated-life qualification, field failure distribution, spare policy and MTTR | `CLM-107`, `CLM-114`; [external-light boundary](../03-components/external-light-serviceability-boundary.md) |
| P1 | CPO-specific capacity allocation and incremental capex | Coherent, Lumentum, Broadcom, NVIDIA | Separates general corporate capacity from usable CPO supply and return on capital | Project-level capex, line allocation, qualified capacity and ramp schedule | `CLM-069`, `CLM-073`; [profit-pool gates](optical-engine-profit-pool-input-gates.md) |
| P1 | Second-source status, cancellation protection and price-down terms | All suppliers | Tests durable pricing power and customer bargaining risk | Contract terms, dual-qualified supplier list, backlog conversion and price schedule | `CLM-083`; supplier dossiers |
| P2 | MOSAIC simultaneous 800G hardware and production packaging | Wide-and-slow countercase | Determines whether a non-laser architecture can cap long-run CPO pricing power | Aggregate hardware demo, microLED/CMOS yield, fibre termination, reliability and customer evidence | `CLM-116`–`CLM-119`; [MOSAIC countercase](../02-architecture/mosaic-microled-countercase.md) |
| P2 | Accelerator optical-I/O customer qualification and revenue conversion | Marvell/Celestial, Ayar, Lightmatter | Separates strategic option value from scale-up production economics | Named XPU/customer, shipped units, product margin and reported revenue | `CLM-085`, `CLM-094`–`CLM-096`; [Marvell dossier](../07-companies/marvell-celestial-accelerator-optical-io-dossier.md) |
| P2 | Interposer-level optical I/O process and thermal yield | NVIDIA/interposer and future 3D routes | Tests whether post-CPO integration changes the supplier control point by 2028–2032 | Production 2.5D/3D package, thermal cycling, alignment yield and cost | `CLM-112`–`CLM-115`; [interposer boundary](../02-architecture/interposer-optical-io-boundary.md) |

## Scoring rule after gates clear

Do not assign a 0–5 operational score because a field is plausible. Record the gate as **cleared**, **partially cleared**, or **open**, attach the source and claim IDs, then score only the evidence-supported dimension. A company may lead technically while remaining unscorable on profit-pool capture.

The minimum evidence bundle for a numeric company scenario is:

1. A defined system and annual unit denominator.
2. A customer-confirmed production numerator or explicitly labelled probability-weighted scenario.
3. Engine content, supplier share, ASP and product-level margin.
4. Yield, warranty, cannibalisation and incremental R&D assumptions.
5. Attributable capacity capex and second-source/cancellation terms.

Until that bundle exists, the correct output is a ranked diligence queue and a qualitative maturity view, not a fabricated earnings forecast.

## Linked controls

- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Company evidence-gap matrix](../07-companies/company-evidence-gap-matrix.md)
- [CPO adoption timeline](adoption-timeline.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
