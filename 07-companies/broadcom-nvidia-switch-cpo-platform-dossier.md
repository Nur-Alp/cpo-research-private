# Broadcom and NVIDIA: Switch-Side CPO Platform Dossier

**Owner:** Nur Alpys
**Status:** Evidence-matched first-pass dossier; not an investment recommendation
**Scope:** Switch-side CPO platforms, not external component-supplier profitability
**As of:** 2026-08-07

## Decision question

Which company has the stronger public case for switch-side CPO platform control and commercial proof—and what does that imply for the external optical-engine profit pool?

## Current answer

**INFERENCE:** Broadcom has the stronger disclosed merchant-switch CPO product definition. Its TH6-Davisson materials specify a 102.4T switch, sixteen 6.4T optical engines, 200G-per-link operation and field-replaceable ELSFP laser modules. Broadcom also reports a historical 100G/lane TH5-Bailly volume-production baseline with Micas and Delta partner systems. The TH6 announcement names HPE, Celestica, Micas and Nexthop as collaborators or solution partners, but these quotations do not disclose a completed customer deployment or unit count. The TH6 announcement nevertheless describes the 200G device as sampling to early-access customers, despite saying it is “now shipping.”[CMP-018][PRI-028][CLM-199][CLM-200][CLM-246][CLM-247][CLM-248][CLM-249]

**INFERENCE:** NVIDIA has the stronger disclosed full-system route to CPO adoption. Its May 2026 announcement and official silicon-photonics platform page identify Spectrum-X Ethernet Photonics as a 200Gb/s-SerDes CPO platform and list multiple first adopters and technology partners. Two CoreWeave deployment pages independently identify the 102.4T Spectrum-X SN6600-LD in Vera Rubin infrastructure and describe CoreWeave as an early Photonics CPO adopter, providing customer-side corroboration of a named deployment.[CMP-019][CMP-025][CLM-220][CLM-221][CLM-222][CLM-223][CLM-228][CLM-229] This still does not disclose fleet size, repeat deployments, optical-engine suppliers, qualification, or field-reliability statistics.

Neither company’s public evidence establishes CPO-specific economics, final optical-engine yield, repair cost, or optical-engine supplier share. Broadcom therefore leads provisionally in **merchant CPO product definition**; NVIDIA leads provisionally in **integrated platform/customer route**; neither conclusion identifies who captures the external optical-engine profit pool.

## Comparable role map

| Dimension | Broadcom | NVIDIA | Research implication |
|---|---|---|---|
| CPO role | Merchant Ethernet switch ASIC, 200G SerDes, CPO engine/package integration and ELSFP interface | CPO switch platform, AI networking fabric, system software and AI-factory customer route | Platform control and external-engine supply are separate layers |
| Defined product boundary | **COMPANY CLAIM:** TH6-Davisson: 102.4T, 16 x 6.4T DR engines, 200G/link, ELSFP, stated IEEE 802.3 interoperability | **COMPANY CLAIM:** Spectrum-X Ethernet Photonics CPO switch with 200Gb/s SerDes; NVIDIA's later technical blog describes 32 engines, 16 Tx/16 Rx lanes per engine and 512 x 200G lanes for a reference package | NVIDIA now provides a more detailed reference-engine denominator, but neither company discloses engine supplier, cost, yield or margin; do not assume CoreWeave's SN6600-LD uses every reference detail |
| Stated commercial status | 100G/lane TH5-Bailly has partner-reported volume production; 200G/lane TH6 release says “now shipping” and “currently sampling ... to early access customers” | May 2026 release says CPO switches “now in production”; availability says Rubin production shipments start in fall | Treat 100G production and 200G status as separate states; neither 200G claim is customer-confirmed broad volume |
| Customer evidence | HPE, Celestica, Micas and Nexthop are named as collaborators or solution-route partners, but no completed TH6 customer deployment, unit count or repeat order is disclosed; TH5 partner production remains a separate 100G/lane baseline | Two CoreWeave pages corroborate a named 102.4T SN6600-LD/Vera Rubin deployment; Lambda/OCI remain named NVIDIA ecosystem partners; Meta confirms Spectrum-X platform use, not photonics/CPO use | NVIDIA has stronger customer-side deployment evidence; neither side discloses a complete unit denominator, repeat volume, supplier BOM or field population |
| Serviceability | Field-replaceable ELSFP modules; engine replacement procedure not disclosed | NVIDIA describes an eight-laser field-replaceable ELS module; engine/package replacement procedure remains undisclosed | ELS limits the laser failure domain only; it does not prove engine or package serviceability |
| Architecture alternatives | Broadcom also markets 200G retimers/AECs, 400G optical DSP and VCSEL NPO | Spectrum-X contains CPO alongside conventional networking products and broader platform options | Both have incentives to serve multiple interconnect architectures; neither is a pure CPO exposure |

## Product and maturity evidence

### Broadcom

1. **COMPANY CLAIM:** TH6-Davisson is described as Broadcom’s third-generation CPO Ethernet switch. The company specifies 102.4 Tb/s switching capacity, sixteen 6.4T Davisson DR engines, 200 Gb/s per link and field-replaceable ELSFP lasers.[CMP-018]
2. **COMPANY CLAIM:** The same release asserts a 70% optical-interconnect power reduction and more than 3.5x lower power than traditional pluggables, plus improved link-flap behaviour based on a TH5-Bailly study. These are not a controlled TH6-versus-pluggable system comparison at matched reach, workload, thermal and power boundaries.[CMP-018]
3. **FACT about disclosure wording:** The release’s lead says TH6-Davisson is “now shipping,” whereas its availability section says the BCM78919 device is “currently sampling” to early-access customers and partners. The conservative maturity label is therefore **early-access sampling disclosed; broad CPO volume not independently established**.[CMP-018]
4. **COMPANY CLAIM:** Broadcom’s OFC 2026 statement describes the wider Tomahawk 6 switch as shipping in production volume, while separately listing TH6-Davisson CPO in the portfolio. This does not prove that the CPO variant itself is in production volume.[CMP-009]
5. **COMPANY/PARTNER CLAIM:** Broadcom’s May 2025 release describes TH5-Bailly as the first volume-production 100G/lane CPO solution and records Micas and Delta production milestones, plus Foxconn production release of CPO sockets and laser-source cages/connectors. This is a 100G/lane baseline and does not establish 200G/lane TH6 volume.[PRI-028][CLM-199][CLM-200]
6. **PARTNER-ROUTE CLAIM:** The TH6 release quotes HPE, Celestica, Micas and Nexthop on collaboration, testing and solution positioning. These statements improve the route-to-market map but do not clear the customer-production gate because they omit accepted SKU, units, date, repeat orders and field history.[CMP-018][CLM-246][CLM-247][CLM-248][CLM-249]

### NVIDIA

1. **COMPANY CLAIM:** NVIDIA’s May 2026 announcement says Spectrum-X Ethernet Photonics is a CPO-based switch with 200Gb/s SerDes “now in production.” It claims 5x better power efficiency, 5x longer AI uptime and 1.3x faster time to deployment relative to networks using traditional transceivers.[CMP-019]
2. **COMPANY CLAIM:** The same source names CoreWeave, Lambda and Oracle Cloud Infrastructure as first ecosystem partners/adopters, while stating that Vera Rubin production shipments are set to begin in the fall. It does not state how many CPO switches these parties have received, qualified or deployed.[CMP-019]
3. **FACT:** Meta’s February 2026 announcement confirms adoption of the NVIDIA Spectrum-X Ethernet networking platform across its infrastructure footprint. It does not isolate Ethernet Photonics, CPO switches, system count, deployment date or economics.[CMP-011]
4. **COMPANY CLAIM:** NVIDIA’s January Rubin press kit also described Spectrum-X Ethernet Photonics as CPO-based and said its systems offer power-efficiency and uptime improvements. The later May source is the stronger current production-status disclosure, while both retain company-claim status.[CMP-008][CMP-019]

## Economic-control map

The layer-by-layer attribution control is maintained in the [CPO content-attribution map](../08-model/cpo-content-attribution-map.md). It should be read before converting the sixteen-engine TH6 architecture into any supplier revenue or margin assumption.

| Economic question | Broadcom | NVIDIA | What remains unknown |
|---|---|---|---|
| Platform and purchasing control | Merchant switch architecture, SerDes and CPO platform | Full AI-factory hardware, networking and software route | Actual system buyer decision rights and supplier-selection process |
| CPO content per system | At least a switch ASIC plus integrated optical engines by architecture; dollar content undisclosed | System/platform CPO content and supplier split undisclosed | Engine count, content, ASP and retained gross profit |
| External supplier dependence | Release explicitly names TSMC COUPE technology-based optical engines, plus an ELSFP boundary and ecosystem partners; it does not establish who supplies the complete qualified engine | Public materials do not identify CPO optical-engine or laser supplier content | Supplier responsibility, qualification, dual sourcing and pricing power |
| Cannibalisation | CPO can displace some optics, retimer and cable content even as Broadcom sells multiple alternatives | CPO may improve networking attach/content but is likely immaterial beside accelerator economics until units are known | Net incremental gross profit after displaced products and support cost |
| Service/warranty exposure | ELSFP is replaceable; engine/package repair and warranty allocation undisclosed | CPO service and warranty model undisclosed | Field returns, spares, MTTR, service labour and warranty reserves |

## Evidence-adjusted readiness view

| Gate | Broadcom | NVIDIA | Why no numeric leader score yet |
|---|---|---|---|
| Defined switch-CPO product | Medium to high | Medium | Both rely primarily on company product claims; comparison boundaries differ |
| Platform/customer route | Medium | Medium to high | NVIDIA names adoption partners; customer-side CPO volumes are absent |
| Manufacturing and qualification | Low to medium | Low to medium | No final-engine yield, qualification pass-rate, capacity allocation or test/rework data |
| Reliability/serviceability | Low to medium for ELSFP only | Low | No matched field-failure, link-flap methodology, engine-repair or warranty evidence |
| CPO economic proof | Unknown | Unknown | Neither reports CPO revenue, gross margin, content, TCO or earnings materiality |

## Implication for the active optical-engine thesis

Platform leadership does not make Broadcom or NVIDIA the external optical-engine profit-pool leader. The platform owner may capture the system-level rent while TSMC, laser suppliers, PIC/engine suppliers, fibre-attach partners and assemblers split the optical content. Conversely, vertical CPO integration may reduce the addressable content available to independent suppliers. The relevant diligence item is an explicit engine bill of materials and commercial responsibility map—not a claim that a CPO announcement proves supplier profit.

Broadcom's TH6 release makes the control-point question sharper: TSMC COUPE is the named optical-engine technology route, while Broadcom owns the switch ASIC/platform and ELSFP system definition. TSMC's 2025 Annual Report adds a customer-linked 200G COUPE result and a 2026 volume-production target. Together these support a potential TSMC manufacturing/process-control position, not evidence that TSMC captures the complete engine ASP or that Broadcom outsources all optical content. Broadcom also describes a future 400G-per-channel fourth-generation roadmap, but no date or qualification result is public.[CLM-210][CLM-211][CLM-213][CLM-214]

## Falsification and next diligence

Reduce this platform-leadership view if:

1. A customer confirms that “production” refers only to samples or lab systems rather than repeat commercial deployment.
2. Broad CPO qualification is delayed by package yield, serviceability, link availability or procurement concerns.
3. LPO/NPO meets the same operating requirement at lower all-in cost or faster service.
4. An alternative switch/platform vendor shows customer-confirmed CPO units and superior field economics.

Next evidence required: deployed customer SKU and unit count, repeat deployment record, exact CPO optical-engine and laser suppliers, qualification completion, measured chassis power at a matched boundary, field failure/link-flap methodology, engine-replacement procedure, warranty allocation and CPO-specific financial contribution. The two CoreWeave records advance the customer-confirmation gate but do not clear its volume or economics conditions.[CLM-220–CLM-223]

## Sources

- `CMP-008`: NVIDIA, [Rubin platform press kit](../01-sources/product-materials/CMP-008-nvidia-rubin-cpo-production-2026.pdf), 5 January 2026.
- `CMP-009`: Broadcom, [OFC 2026 AI-infrastructure announcement](../01-sources/product-materials/CMP-009-broadcom-ofc-2026-cpo.pdf), 12 March 2026.
- `CMP-011`: Meta and NVIDIA, [long-term infrastructure partnership](../01-sources/product-materials/CMP-011-meta-nvidia-partnership-2026.html), 17 February 2026.
- `CMP-018`: Broadcom, [TH6-Davisson CPO announcement](https://www.broadcom.com/company/news/product-releases/63626), 8 October 2025. The [local HTML archive](../01-sources/product-materials/CMP-018-broadcom-th6-davisson.html) is retained as `ARC-001`; cite the canonical publisher page for external use.
- `CMP-019`: NVIDIA, [Vera Rubin ramps into full production](../01-sources/product-materials/CMP-019-nvidia-rubin-full-production-2026.pdf), 31 May 2026.
- `PRI-028`: Broadcom, [TH5-Bailly 100G/lane volume-production baseline](../01-sources/product-materials/PRI-028-broadcom-th5-volume-production.md), 15 May 2025.

Company sources establish what the companies claim and disclose; they do not independently establish CPO units, commercial economics, final-engine yield, field reliability or an investment ranking.
