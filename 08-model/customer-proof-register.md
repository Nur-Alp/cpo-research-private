# CPO customer-proof register

**Owner:** Nur Alpys  
**Status:** Evidence register; not a shipment forecast  
**Scope:** Customer and partner evidence for 200G/lane switch-side and inter-rack CPO  
**As of:** 2026-08-12

## Purpose

Vendor production language and partner quotations are not interchangeable with customer-confirmed shipments. This register records exactly what each public record proves and which fields remain missing before it can supply a commercial-proof numerator.

## Evidence register

| Record | Domain and product boundary | What the source establishes | What it does not establish | Gate status |
|---|---|---|---|---|
| CoreWeave, `CMP-021`, `CLM-220`–`CLM-221`, `CLM-382`–`CLM-383` | Operator adoption statement plus 102.4T SN6600-LD deployment | CoreWeave separately says it is an early NVIDIA Photonics CPO adopter and describes a 102.4T SN6600-LD with 64 × 1.6T ports; the claims are not tied to one SKU | NVIDIA's full manual classifies SN6600-LD as a pluggable RHS-transceiver switch; no customer CPO SKU, units, repeat shipments, field data or supplier share | **CPO attribution withdrawn; separate claims retained** |
| CoreWeave, `CMP-022`, `CLM-222`–`CLM-223`, `CLM-380` | Switch-side Ethernet; Vera Rubin infrastructure; 2U liquid-cooled SN6600-LD | Corroborates the 102.4T, 64 × 1.6T-port, 200G-SerDes customer configuration and adds the 2U/liquid-cooled boundary | CMP-048 identifies this SKU as pluggable RHS, not CPO; no CPO unit count, repeat order or economics | **Pluggable-platform deployment only** |
| Lambda, `CMP-023`, `CLM-224`–`CLM-225` | Inter-rack/scale-up InfiniBand; Quantum-X Photonics | Lambda says a production-scale GB300 NVL72 supercluster with 10,000+ GPUs uses Quantum-X Photonics CPO in production | Switch count, optical-engine count, ELS count, customer ownership, deployment units, repeat volume, ASP or margin | **Production-scale domain evidence; no CPO numerator** |
| Lambda, `CMP-024`, `CLM-226`–`CLM-227` | Future scale-up and scale-out roadmap; Quantum-X plus Spectrum-X | Lambda says future clusters are being prepared with both Quantum-X and Spectrum-X Photonics | Spectrum-X production shipment, exact SKU, qualification, units or date | **Roadmap/preparation only for Spectrum-X** |
| Lambda operator adoption, `CMP-077`, `CLM-546` | Customer/operator adoption planning; Quantum-X InfiniBand and Spectrum-X Ethernet | Lambda says GB300 NVL72 and Vera Rubin NVL144 cluster plans will integrate both photonics families | Delivered Spectrum-X Ethernet `SN6800`/`SN6810-LD`, accepted units/ports, repeat shipment, field service or economics; the exact Q3450-LD record is InfiniBand | **Customer adoption lead; exact-SKU numerator open** |
| CoreWeave benchmark, `CMP-078`, `CLM-547` | Customer/operator Spectrum-X Ethernet platform benchmark; 8,192 GPUs | CoreWeave reports a large Spectrum-X platform deployment/benchmark | CPO versus pluggable architecture, exact SKU, accepted switch units/ports, repeat shipment or economics | **Platform-scale negative control; CPO numerator open** |
| Meta–NVIDIA, `CMP-011`, `CLM-081` | NVIDIA Spectrum-X Ethernet platform | Meta confirms adoption of Spectrum-X across its infrastructure footprint | Spectrum-X Photonics/CPO isolation, switch count, optical-engine content, deployment date, field data or economics | **Platform adoption; not CPO proof** |
| NVIDIA platform page, `CMP-025`, `CLM-228`–`CLM-229` | Spectrum-X and Quantum-X product/ecosystem route | NVIDIA says Spectrum-X reaches full production, names first adopters, and lists technology partners | Customer acceptance, units, exact partner-to-layer mapping, BOM, ASP, yield or margin | **Vendor ecosystem evidence** |
| NVIDIA Vera Rubin release, `PRI-033`, `CLM-346`–`CLM-347` | Switch-side Ethernet; Spectrum-X Ethernet Photonics, 200Gb/s SerDes | NVIDIA states the CPO switch is now in production and names CoreWeave, Lambda and OCI among first ecosystem partners/adopters | Units, repeat shipments, exact SKU configuration, supplier allocation, qualification, matched power protocol, ASP and margin | **First-party production claim; numerator open** |
| NVIDIA production-ramp article, `CMP-053`, `CLM-435`–`CLM-436` | Switch-side Ethernet; Spectrum-X Ethernet Photonics; full-stack manufacturing route | NVIDIA identifies TSMC, SPIL, TFC and Foxconn roles, says systems are validated before customer shipment and repeats the CoreWeave/Lambda/OCI first-adopter list | Exact customer SKU, accepted units, repeat shipments, final-engine yield, supplier share, field data or economics | **Manufacturing/timing corroboration; customer numerator open** |
| Dell PowerSwitch catalogue, `CMP-057`, `CLM-519` | Switch-side Ethernet; `SN6810-LD`/`SN6800-LD` CPO versus `SN6600-LD` pluggable | Dell lists the two NVIDIA CPO configurations as PowerSwitch products with MMC-12 interfaces and Contact Sales availability, separately from the OSFP224 pluggable system | Booked order, customer identity, acceptance, units/ports, repeat deployment, supplier content, field results or economics | **OEM/channel product route; customer numerator open** |
| Dell networking warranty coverage, `CMP-058`, `CLM-520` | OEM service-policy boundary for `SN6810-LD`/`SN6800-LD` CPO systems | Dell lists limited three-year warranty and NBD onsite repair/replacement service for both CPO SKU families | Engine-level repair, achieved MTTR, field outcomes, spare policy, warranty cost, customer fleet or economics | **System-level service policy; no customer numerator** |
| Dell/NVIDIA Rubin AI Factory integration, `CMP-072`, `CLM-541` | OEM/platform integration; Rubin AI Factory, SN6000 CPO options and illustrated `SN6800-LD` | Dell describes validated rack-scale integration of Rubin compute, SN6000 networking, CPO options and liquid cooling | Exact-SKU customer acceptance, units/ports, acceptance date, repeat shipment, field service, supplier allocation, yield, ASP or margin; the team.blue quotation is not CPO evidence | **OEM integration lead / false-positive control; customer numerator open** |
| XenoSpectrum/TrendForce triangulation, `NWS-011`, `CLM-411`–`CLM-415` | Switch-side Ethernet; NVIDIA Spectrum-X and Broadcom Bailly volume-ramp interpretation | Secondary reporting says limited partner shipments may have begun by July 2026, but cannot determine evaluation versus commercial deployment and reports that volumes/yield/general availability are undisclosed | No primary customer confirmation, exact SKU, units, repeat shipment, qualification or field history; underlying TrendForce records are not retained | **Secondary triangulation only; numerator remains open** |
| TrendForce press-center record, `NWS-012`, `CLM-416`–`CLM-420` | Switch-side Ethernet; NVIDIA Spectrum-X and Broadcom Bailly production/ramp signal | TrendForce reports select-partner Spectrum-X shipments, limited Bailly shipments, optical-engine/SiPh/advanced-packaging bottlenecks and a 2027–2028 ramp view | No named customer, SKU, unit count, repeat order, qualification lot, final-engine yield or financial allocation; research-house claims are not independently audited | **Secondary triangulation only; numerator remains open** |
| Focus Taiwan / CNA, `NWS-013`, `CLM-521` | Switch-side Ethernet; NVIDIA Spectrum-X CPO shipment-status statement | Reports NVIDIA networking SVP Gilad Shainer saying Spectrum-X CPO had begun shipping to select partners at GTC Taipei | Recipients, SKU, evaluation versus accepted deployment, units/ports, repeat delivery, field data, supplier content and economics | **Independent shipment-status corroboration; numerator remains open** |
| Foxconn Q1 2026 outlook, `CMP-060`, `CLM-526`–`CLM-527` | Generic CPO optical-switch manufacturing route; product maker/configuration unspecified | Foxconn forecasts Q3 2026 mass-production shipments and says full-year shipments may reach tens of thousands; it describes preparation with unnamed cloud/AI customers | Actual Q3 shipments, product maker/SKU, named customer, acceptance, units/ports, repeat delivery, field data, supplier allocation and economics | **Manufacturer outlook; no customer numerator and no NVIDIA/Broadcom attribution** |
| Broadcom, `CMP-018`, `CLM-076`–`CLM-078` | Merchant switch-side Ethernet; TH6-Davisson BCM78919 | Broadcom defines a 102.4T, sixteen-engine, 200G/link CPO product and reports both “now shipping” and early-access sampling language | Named customer deployment, accepted SKU, units, repeat shipments, qualification, supplier content, yield or margin | **Early-access/product-definition evidence** |
| Broadcom CPO product catalogue, `CMP-062`, `CLM-530` | Merchant switch-side Ethernet; TH6-Davisson BCM78919 | Broadcom currently labels BCM78919 as **Limited Release** | Customer identity, acceptance, units, repeat shipment, general availability, supplier content, yield or economics | **Limited-release lifecycle corroboration; numerator remains open** |
| Broadcom partners, `CMP-018`, `CLM-246`–`CLM-249` | TH6 solution and integrator route | HPE, Celestica, Micas and Nexthop are quoted as collaborators or solution-route partners; Micas separately references extensive TH5 testing | None of the quotations identifies a completed TH6 customer deployment, units, date, repeat order or field population | **Partner-route evidence only** |
| Supermicro / AMD / Micas validated design, `CMP-059`, `CLM-522`–`CLM-525` | Historical 100G/lane TH5-Bailly CPO test configuration | Names M2-W6940-128X1-FR4, TH5-Bailly, CPO engines/RLMs and a one-switch/two-server/16-link evaluation | A customer procurement/acceptance, installed units, repeat shipment, independent field reliability, TH6 configuration or supplier economics | **Specified partner validation; no customer numerator** |
| Supermicro Rubin photonics integration, `CMP-071`, `CLM-540` | OEM/platform integration; Spectrum-X and Quantum-X photonics switches in Vera Rubin NVL72/NVL8 | Supermicro describes pre-validated rack-scale building blocks combining NVIDIA photonics switches, compute and liquid cooling | Exact `SN6800`/`SN6810-LD` acceptance, units/ports, shipment date, repeat deployment, field service, supplier allocation, yield, ASP or margin; Ethernet and InfiniBand are grouped | **OEM integration lead; customer numerator open** |
| Broadcom OCP partner/demo announcement, `CMP-074`, `CLM-543` | TH6-Davisson/ Tomahawk 6 partner-showcase boundary | Broadcom names Alpha Networks, Celestica, DNI Emerging Technologies and Micas as conference demo partners, including a Micas TH6-Davisson CPO demo | No purchased/accepted `BCM78919`, end customer, qualification date, accepted units/ports, repeat shipment, field service, supplier allocation or economics | **Demo/partner route; customer numerator open** |
| Celestica Q1 2026, `CMP-028`, `CLM-255`–`CLM-256` | Switch-side Ethernet CPO; unnamed hyperscaler program | Celestica reports an awarded design-and-manufacturing program for a CPO Ethernet switch using 1.6T switch silicon, co-packaged optical interconnects and liquid cooling; production ramp is expected in 2027 | Customer identity, SKU, units, qualification completion, repeat order, optical BOM, supplier share, ASP, margin and field history | **Customer-program evidence; planned ramp, not shipped volume** |
| Celestica DS6000, `CMP-029`, `CLM-257` | TH6 1.6TbE platform; 102.4T; optical or copper interconnects | Celestica says the platform is available for order to initial customers and has 64 × 1.6TbE ports; it explicitly supports both copper and optical interconnects | CPO-specific configuration, customer identity, units, qualification, repeat order, optical-engine content or economics | **Orderable platform; architecture ambiguity remains** |
| CoreWeave, `CMP-039`, `CLM-320`, `CLM-383` | Customer/operator co-design and separate Photonics CPO adoption statement | CoreWeave describes production-oriented validation and early Photonics CPO adoption, while separately confirming early SN6600-LD deployment | CMP-048 prevents treating the SN6600-LD record as CPO; CPO-specific SKU, units, repeat shipments, qualification and economics remain open | **Operator adoption context; no CPO numerator** |
| CoreWeave/NVIDIA, `CMP-046`–`CMP-048`, `CLM-370`–`CLM-384` | Vera Rubin operations; SN6600-LD pluggable switch; NVIDIA family CPO SKU boundary | CoreWeave describes first-provider validation and a 100% liquid-cooled SN6600 deployment; NVIDIA documents that SN6600-LD is pluggable while SN6810-LD/SN6800-LD are CPO families | Customer CPO SKU, unit count, repeat deployment, supplier content and field data remain open | **SKU boundary resolved; CPO attribution withdrawn** |
| Lambda, `CMP-040`, `CLM-321`–`CLM-323` | NVIDIA Quantum-X InfiniBand Photonics Q3450-LD; early-access engineering sample | Concrete 115.2T/144×800G/18-ELS hardware and rack/serviceability observations; customer-reported power comparison | Repeat production, field population, qualification, yield, MTTR, ASP and margin | **Early-access operational evidence** |
| Oracle, `CMP-041`, `CLM-324`–`CLM-325` | Acceleron scale-out; LPO/LRO at 400G/800G | Operator explicitly chooses multiplanar LPO/LRO with modular replacement and claims 4–7 W/module savings | Matched CPO comparison, link qualification, field reliability and product economics | **Active LPO countercase** |

## Minimum fields for a cleared commercial-proof record

## Completed negative-control packets

The following packets are retained so future evidence is tested against the
same boundary rather than re-opening known false positives:

- [ESP-001 — CoreWeave `SN6600-LD` pluggable negative](../09-primary-research/evidence-packets/ESP-001-coreweave-sn6600-pluggable-negative.md)
- [ESP-002 — Lambda Quantum-X domain control](../09-primary-research/evidence-packets/ESP-002-lambda-quantum-x-domain-negative.md)
- [ESP-003 — Broadcom OCP TH6 demo negative](../09-primary-research/evidence-packets/ESP-003-broadcom-ocp-demo-negative.md)

## Operator-scale context (not a CPO numerator)

CoreWeave's March 2026 investor presentation reports $66.8B of backlog, 43 active data centers, more than 850 MW of active power and more than 3.1 GW of contracted power; its FY2025 10-K describes the broader Quantum-X800, Quantum-2, Spectrum-X and liquid-cooling infrastructure context.[CLM-376–CLM-378] These records establish that CoreWeave is a large, repeat-capable operator, but they do **not** identify CPO switch units, optical-engine content, qualification, repeat CPO shipments or CPO economics. They therefore belong in the denominator/context layer, not in the customer-confirmed CPO numerator. See [customer scale and repeatability gate](customer-scale-repeatability-gate.md).

### Interpretation control

Do not multiply CoreWeave's data-center, power, backlog or GPU-scale figures by an assumed CPO penetration rate. A valid CPO numerator still requires an exact product/revision, a dated unit or port count and repeat deployment evidence at the same physical boundary.

At least one customer-side record must identify:

1. Exact product SKU and CPO/NPO/optical-engine configuration.
2. Customer acceptance or qualification completion date.
3. Units, ports or systems deployed, with a defined time period.
4. Repeat shipment, expansion or renewal evidence.
5. Network position and workload/topology boundary.
6. Measured power, link availability or service history at the same product boundary.
7. Optical-engine, laser, PIC, attach and package responsibility—or an explicit statement that these remain undisclosed.

Without fields 1–4, the record cannot produce the numerator in:

```text
commercial-proof rate = customer-confirmed CPO systems / defined target systems
```

Fields 5–7 are needed to connect adoption to the optical-engine profit pool rather than merely to platform revenue.

## Current evidence-adjusted ranking

- **Strongest named switch-side deployment:** CoreWeave's SN6600-LD record is now confirmed as a pluggable RHS-transceiver deployment, not CPO. CoreWeave's separate Photonics CPO-adopter statement remains unallocated to a SKU, so the named switch-side CPO unit numerator is open.
- **Strongest inter-rack scale-up production-scale record:** Lambda's Quantum-X Photonics statement for a 10,000+ GPU GB300 cluster; it is not switch-side Spectrum-X evidence.
- **Strongest merchant product definition:** Broadcom TH6-Davisson; its current public record remains conservative early-access / **Limited Release** because “now shipping,” sampling and current catalogue lifecycle language do not supply an accepted-unit denominator.
- **Strongest partner-route map:** Broadcom's HPE/Celestica/Micas/Nexthop quotations and NVIDIA's broader partner/adopter list; neither clears customer shipment gates.
- **Strongest new named-program evidence:** Celestica's unnamed hyperscaler CPO-switch design/manufacturing award with an expected 2027 production ramp. It advances the route-to-production gate but still supplies no units or realized economics.
- **Strongest new timing evidence:** NVIDIA's May 2026 release states that Spectrum-X Ethernet Photonics is now in production. This upgrades the first-party timing record but does not replace the missing customer-side unit numerator or repeat-shipment evidence.

These are different leadership dimensions. No record currently clears a repeat-volume or optical-engine profit-pool gate.

## Linked controls

- [CPO evidence-gate register](evidence-gate-register.md)
- [Broadcom and NVIDIA switch-CPO dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [NVIDIA CPO reference-content bridge](nvidia-cpo-reference-content-bridge.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
