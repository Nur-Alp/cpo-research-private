# Broadcom TH6-Davisson — commercial-proof dossier

**Status:** Private evidence synthesis; no publication or investment-call clearance  
**As of:** 2026-08-12  
**Decision:** Has Broadcom demonstrated repeat, customer-confirmed switch-side 200G/lane CPO deployment?

## Current answer

**No — not on the public record retained here.** Broadcom supplies the clearest merchant-switch 200G/lane CPO product definition, but its TH6-Davisson release uses both “now shipping” and early-access sampling language. No retained primary record identifies a completed customer TH6 CPO deployment, accepted units, repeat order or CPO-specific economics. The appropriate label is **defined product with early-access sampling; broad commercial numerator open**.

## What is established

| Evidence | What it establishes | What it cannot establish |
|---|---|---|
| `CMP-018` / `CLM-076` | TH6-Davisson is specified as a 102.4Tb/s CPO switch with sixteen 6.4T DR optical engines, 200Gb/s links and field-replaceable ELSFP laser modules. | Customer deployment, engine supplier share, qualified yield, ASP, margin, or service economics. |
| `CMP-055` / `CLM-516`–`CLM-517` | BCM78919 is defined as 64 3nm Condor SerDes cores, 512 × 200G PAM4 all-optical I/O and 512 duplex 1310nm single-mode fibres directly driven through integrated optical engines. | Supplier allocation across EIC, PIC, laser, fibre attach, connector, package and test; customer units or economics. |
| `CMP-018` / `CLM-077` | The same release says “now shipping” and that BCM78919 is “currently sampling” to early-access customers and partners. | Broad production volume; the conservative status is early-access sampling until a customer/unit record appears. |
| `CMP-062` / `CLM-530` | Broadcom’s current CPO product catalogue classifies BCM78919 as **Limited Release**. | A customer deployment, accepted units, repeat shipment, general availability, supplier content or economics. |
| `CMP-063` / `CLM-532` | Broadcom's briefing recovers a first-party, historical TH5-Bailly statement of no link flaps in its first 1M CPO device hours. | TH6 200G/lane reliability, a customer field population, service economics, acceptance, units or repeat delivery. |
| `CMP-064` / `CLM-533` | Broadcom identifies Meta as the high-temperature lab-characterisation setting for its historical 1M cumulative 400G-equivalent flap-free CPO port-device-hours statement. | Meta procurement or production volume, TH6 SKU, test population/duration, field returns, warranty economics or TH6 deployment. |
| `PRI-032`, `PRI-028` / `CLM-199`–`CLM-200` | Broadcom and partners describe a historical 100G/lane TH5-Bailly volume-production baseline, including Micas/Delta/Foxconn production milestones. | 200G/lane TH6 status, units, yield, or field reliability; 100G evidence cannot be rolled forward automatically. |
| Current Micas historical refresh / `PRI-028` | Micas' official page says its 51.2T TH5-Bailly CPO system entered volume production and that orders were being accepted. | TH6/`BCM78919` customer acceptance, units, repeat shipments, final-engine yield, ASP, margin or service data. |
| `CMP-059` / `CLM-522`–`CLM-525` | A Supermicro/AMD/Micas validated design identifies a specific TH5-Bailly 51.2T/128×400G CPO system and reports a bounded one-switch/two-server power comparison. | TH6-Davisson status, a named customer deployment, multi-switch performance, independent field reliability, units, supplier economics or 200G/lane maturity. |
| `CMP-018` / `CLM-246`–`CLM-249` | HPE, Celestica, Micas and Nexthop are named collaborators or solution-route partners. | A completed TH6 customer deployment, purchase order, units or repeat shipment. |
| `CMP-028` / `CLM-255`–`CLM-256` | Celestica reports an unnamed hyperscaler CPO-switch program using 1.6T silicon, co-packaged optics and liquid cooling, with production ramp expected in 2027. | Customer name, SKU, qualification completion, units, supplier map, revenue, or proof it is TH6-Davisson. |
| `CMP-029` / `CLM-257`, `CLM-558` | Celestica’s customer-orderable DS6000 102.4T platform uses Broadcom TH6 silicon but exposes 64 × 1.6TbE OSFP224 ports and supports copper/optical interconnects. | `BCM78919` / TH6-Davisson CPO selection or shipment; OSFP224 availability is a pluggable-interface route, not CPO proof. |
| `CMP-070` | Micas presents a Broadcom-sourced historical CPO qualification dashboard marking the pluggable laser source, PIC and optical connector as qualified. | TH6/`BCM78919` qualification, customer acceptance, lot size, supplier share, yield, warranty or economics. |
| `CMP-074` / `CLM-543` | Broadcom's OCP announcement names Alpha Networks, Celestica, DNI Emerging Technologies and Micas as Tomahawk 6/TH6 demonstration partners, including a Micas TH6-Davisson CPO demo. | Purchased or accepted `BCM78919`, end customer, qualification date, accepted units/ports, repeat shipment, field service or economics. |
| `CMP-075` / `CLM-544` | Broadcom states that the Tomahawk 6 **family** is shipping in production volume and moved from initial samples to production deployment, with 100G and 200G SerDes options. | Exact TH6-Davisson/BCM78919 CPO configuration, customer, accepted units/ports, repeat shipment, supplier content or economics. |
| `CMP-076` / `CLM-545` | Celestica discloses an award for a CPO switch program with an unnamed hyperscaler and expects production ramp in 2027. | Named customer, exact SKU or Broadcom mapping, accepted units, repeat shipment, supplier content, yield or margin. |
| `CMP-009` | Broadcom's OFC 2026 material describes the 102.4T Tomahawk 6 as shipping in production volume and presents TH6-Davisson CPO alongside the broader Ethernet portfolio. | Whether the production-volume statement is specifically the `BCM78919` CPO configuration, plus customer identity, accepted units/ports, repeat shipment, field service or economics. |

### Current lifecycle refresh (12 August 2026)

Broadcom's live `BCM78919` catalogue still classifies the device as **Limited Release** and shows no distributor inventory. This is a useful lifecycle control, but it cannot distinguish a small early-access shipment from no shipment and does not identify a customer, accepted units/ports, repeat delivery or supplier economics. The release remains conservatively classified as early access until those fields are disclosed.

Broadcom's March 2026 production-volume statement upgrades the **Tomahawk 6
family** timing record, but it explicitly covers a family with multiple SerDes
and interconnect options. It cannot be used as a `BCM78919` CPO numerator. The
Celestica award is a separate, useful 2027 CPO-ramp lead; its unnamed
hyperscaler and undisclosed configuration prevent attribution to TH6-Davisson.

The OFC 2026 material is directionally consistent with that interpretation: it
places the “shipping in production volume” language next to the 102.4T
Tomahawk 6 portfolio and lists TH6-Davisson CPO as a related solution, but it
does not supply the missing configuration, customer, or unit denominator.
Treat it as corroborating lifecycle language, not independent TH6 CPO volume.

Broadcom's announcement also describes TH6 as building on a foundation of “field shipments.” That phrase is not a TH6 customer denominator: the same release separately says BCM78919 is sampling to early-access customers and partners, while the retained field/qualification records refer to earlier CPO generations. Historical CPO field experience can inform the technology route, but it cannot be rolled forward into TH6 accepted units, repeat shipment or TH6 margin.

## Product boundary

The item under review is **TH6-Davisson BCM78919**, not the Tomahawk 6 family generally, a 100G/lane TH5-Bailly program, or a generic 102.4T Celestica platform. Celestica's DS6000 is a particularly important control: it uses TH6 silicon but its disclosed 64 × 1.6TbE **OSFP224** interface is a pluggable form-factor route. The relevant commercial denominator is customer-accepted TH6 CPO systems/ports—not all Tomahawk, 1.6T, optical or copper shipments.

## Supplier-content map — evidence-adjusted

| Layer | Public responsibility signal | Confidence | Not established |
|---|---|---|---|
| Merchant switch ASIC / SerDes | Broadcom specifies 64 integrated 3nm Condor SerDes cores and associated PCS | High | CPO-specific platform price, retained gross profit or transfer pricing |
| Optical engines / PIC-EIC package route | Broadcom specifies sixteen integrated engines; each optical path is directly driven from a Condor SerDes; TSMC COUPE is a named technology route in the wider dossier | High for switch/interface architecture; low for supplier allocation | PIC/EIC ownership, complete-engine supplier, assembly boundary and retained content |
| Fibre / faceplate connectivity | Corning says it is collaborating on complete faceplate-to-chip optical assemblies for TH6-Davisson systems | Medium for a TH6-specific connectivity collaboration | Exact assembly scope, qualified share, connector/attach ownership, loss/yield, commercial allocation and warranty |
| Fibre / connector boundary | 512 duplex single-mode 1310nm fibres reach the front panel; ELSFP modules are field-replaceable | High for interface; medium for service boundary | Fibre-attach owner and yield, connector supplier, loss/rework, field procedure, spare policy, ASP or margin |
| Package / test / qualification | CPO is described as an integrated engine/ASIC product | Low | OSAT/test owner, test time, final yield, acceptance criteria or warranty allocation |
| System/integration route | HPE, Celestica, Micas, Nexthop named as collaborators | Medium for route | Customer selection, system share, qualified configuration or economic allocation |
| Sockets / cages/connectors | Foxconn production release applies to the historical TH5 baseline | Medium for historical ecosystem | TH6 qualification, supplier share or unit volume |

The presence of sixteen engines is a technical denominator, not a revenue input. Corning's TH6-specific faceplate-to-chip collaboration makes the fibre/connectivity diligence route more concrete, but no public record establishes whether Broadcom, TSMC, Corning, a dedicated optical-engine supplier, OSATs or laser suppliers retain each layer’s economics (`CLM-529`).

Micas' qualification dashboard is a useful historical control because it shows
the component classes Broadcom's earlier CPO ecosystem considered separately:
pluggable laser source, PIC and optical connector (`CMP-070`). It does not
establish that the same components, test protocol or suppliers cleared TH6
`BCM78919`; keep it as a prior-generation qualification precedent, not a TH6
customer or economics input.

## Commercial-proof gate

| Required field | Current status | Evidence needed |
|---|---|---|
| Exact CPO SKU/configuration | **Pass:** `BCM78919` / TH6-Davisson product configuration disclosed | Product definition alone does not establish a customer deployment |
| Exact customer TH6 CPO SKU/configuration | Open | Customer/operator statement or named system BOM |
| Acceptance / qualification date | Open | Customer qualification, manufacturing release or procurement record |
| Units / ports / systems | Open | Dated shipment/installed-base denominator for TH6 CPO |
| Repeat shipment / expansion | Open | Repeat order, customer expansion or sustained production evidence |
| Field service / reliability | Partially scoped by ELSFP | Field-return, engine-repair, MTTR, spare and warranty record |
| Product-linked supplier allocation / economics | Open | Named qualified supplier role plus content share, ASP, product margin, yield/rework and warranty boundary |

## Timing implication and falsification

**Current inference:** Broadcom’s architecture and **Limited Release** / early-access route make TH6-Davisson a leading merchant switch-CPO candidate for the 2026–2027 verification window, not a verified volume leader.

The recovered TH5 result is helpful only as a historical technology-route
control. It removes the need to rely on a newsletter for the quoted
one-million-device-hour observation, but its disclosed boundary is still
insufficient to prove a TH6 reliability or deployment outcome.

The named Meta test setting strengthens the historical validation context but
does not change that conclusion: a high-temperature lab-characterisation
record is not an accepted-unit or field-service numerator.

Upgrade only after a named customer confirms a TH6 CPO configuration, accepted units and repeat shipments. Downgrade if sampling does not progress to an identified production customer, if the 2027 Celestica program does not ramp as planned, or if serviceability/yield causes a switch to pluggable, LPO or NPO configurations.

## Source boundary

Primary retained sources: `CMP-018`, `CMP-055`, `CMP-062`, `CMP-063`, `CMP-064`, `CMP-070`, `CMP-074`, `CMP-075`, `CMP-076`, `PRI-032`, `PRI-028`, `CMP-028`, `CMP-029`. The exact-SKU search cycle is logged in [exact-SKU commercial-proof search audit](../../09-primary-research/exact-sku-commercial-proof-search-audit-2026-08-12.md). Claim IDs above are the system of record. This dossier makes no CPO revenue, EPS, market-share, margin or supplier-allocation forecast.

Current live product reference reviewed 12 August 2026: [Broadcom BCM78919 catalogue](https://www.broadcom.com/products/fiber-optic-modules-components/co-packaged-optics/switches/bcm78919). It is used only for the lifecycle status described above; no new customer-volume claim is created from it.
