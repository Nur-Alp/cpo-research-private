# CPO customer-proof register

**Owner:** Nur Alpys  
**Status:** Evidence register; not a shipment forecast  
**Scope:** Customer and partner evidence for 200G/lane switch-side and inter-rack CPO  
**As of:** 2026-08-07

## Purpose

Vendor production language and partner quotations are not interchangeable with customer-confirmed shipments. This register records exactly what each public record proves and which fields remain missing before it can supply a commercial-proof numerator.

## Evidence register

| Record | Domain and product boundary | What the source establishes | What it does not establish | Gate status |
|---|---|---|---|---|
| CoreWeave, `CMP-021`, `CLM-220`–`CLM-221` | Switch-side Ethernet; NVIDIA Photonics CPO and 102.4T SN6600-LD | CoreWeave calls itself an early NVIDIA Photonics CPO adopter and describes a 102.4T SN6600-LD with 64 × 1.6T ports and 200G SerDes | Fleet size, exact optical BOM, engine/ELS count, qualification date, repeat shipments, field returns and supplier share | **Partially clears named deployment** |
| CoreWeave, `CMP-022`, `CLM-222`–`CLM-223` | Switch-side Ethernet; Vera Rubin infrastructure; 2U liquid-cooled SN6600-LD | Corroborates the 102.4T, 64 × 1.6T-port, 200G-SerDes customer configuration and adds the 2U/liquid-cooled boundary | Does not prove Broadcom TH6, NVIDIA 32-engine reference configuration, unit count, repeat order or economics | **Corroboration only** |
| Lambda, `CMP-023`, `CLM-224`–`CLM-225` | Inter-rack/scale-up InfiniBand; Quantum-X Photonics | Lambda says a production-scale GB300 NVL72 supercluster with 10,000+ GPUs uses Quantum-X Photonics CPO in production | Switch count, optical-engine count, ELS count, customer ownership, deployment units, repeat volume, ASP or margin | **Production-scale domain evidence; no CPO numerator** |
| Lambda, `CMP-024`, `CLM-226`–`CLM-227` | Future scale-up and scale-out roadmap; Quantum-X plus Spectrum-X | Lambda says future clusters are being prepared with both Quantum-X and Spectrum-X Photonics | Spectrum-X production shipment, exact SKU, qualification, units or date | **Roadmap/preparation only for Spectrum-X** |
| Meta–NVIDIA, `CMP-011`, `CLM-081` | NVIDIA Spectrum-X Ethernet platform | Meta confirms adoption of Spectrum-X across its infrastructure footprint | Spectrum-X Photonics/CPO isolation, switch count, optical-engine content, deployment date, field data or economics | **Platform adoption; not CPO proof** |
| NVIDIA platform page, `CMP-025`, `CLM-228`–`CLM-229` | Spectrum-X and Quantum-X product/ecosystem route | NVIDIA says Spectrum-X reaches full production, names first adopters, and lists technology partners | Customer acceptance, units, exact partner-to-layer mapping, BOM, ASP, yield or margin | **Vendor ecosystem evidence** |
| Broadcom, `CMP-018`, `CLM-076`–`CLM-078` | Merchant switch-side Ethernet; TH6-Davisson BCM78919 | Broadcom defines a 102.4T, sixteen-engine, 200G/link CPO product and reports both “now shipping” and early-access sampling language | Named customer deployment, accepted SKU, units, repeat shipments, qualification, supplier content, yield or margin | **Early-access/product-definition evidence** |
| Broadcom partners, `CMP-018`, `CLM-246`–`CLM-249` | TH6 solution and integrator route | HPE, Celestica, Micas and Nexthop are quoted as collaborators or solution-route partners; Micas separately references extensive TH5 testing | None of the quotations identifies a completed TH6 customer deployment, units, date, repeat order or field population | **Partner-route evidence only** |
| Celestica Q1 2026, `CMP-028`, `CLM-255`–`CLM-256` | Switch-side Ethernet CPO; unnamed hyperscaler program | Celestica reports an awarded design-and-manufacturing program for a CPO Ethernet switch using 1.6T switch silicon, co-packaged optical interconnects and liquid cooling; production ramp is expected in 2027 | Customer identity, SKU, units, qualification completion, repeat order, optical BOM, supplier share, ASP, margin and field history | **Customer-program evidence; planned ramp, not shipped volume** |
| Celestica DS6000, `CMP-029`, `CLM-257` | TH6 1.6TbE platform; 102.4T; optical or copper interconnects | Celestica says the platform is available for order to initial customers and has 64 × 1.6TbE ports; it explicitly supports both copper and optical interconnects | CPO-specific configuration, customer identity, units, qualification, repeat order, optical-engine content or economics | **Orderable platform; architecture ambiguity remains** |

## Minimum fields for a cleared commercial-proof record

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

- **Strongest named switch-side deployment:** CoreWeave's 102.4T SN6600-LD/Vera Rubin record, while the exact CPO BOM and unit count remain open.
- **Strongest inter-rack scale-up production-scale record:** Lambda's Quantum-X Photonics statement for a 10,000+ GPU GB300 cluster; it is not switch-side Spectrum-X evidence.
- **Strongest merchant product definition:** Broadcom TH6-Davisson; its current public record remains conservative early-access sampling because “now shipping” and sampling language coexist.
- **Strongest partner-route map:** Broadcom's HPE/Celestica/Micas/Nexthop quotations and NVIDIA's broader partner/adopter list; neither clears customer shipment gates.
- **Strongest new named-program evidence:** Celestica's unnamed hyperscaler CPO-switch design/manufacturing award with an expected 2027 production ramp. It advances the route-to-production gate but still supplies no units or realized economics.

These are different leadership dimensions. No record currently clears a repeat-volume or optical-engine profit-pool gate.

## Linked controls

- [CPO evidence-gate register](evidence-gate-register.md)
- [Broadcom and NVIDIA switch-CPO dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [NVIDIA CPO reference-content bridge](nvidia-cpo-reference-content-bridge.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
