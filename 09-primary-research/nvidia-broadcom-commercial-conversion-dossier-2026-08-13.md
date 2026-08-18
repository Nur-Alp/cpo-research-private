# NVIDIA and Broadcom switch-CPO commercial-conversion dossier

**Status:** Private decision evidence; no publication, investment-call or supplier-revenue clearance  
**As of:** 13 August 2026  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6810` / `SN6800` (including `-LD` ordering labels) and Broadcom TH6-Davisson `BCM78919` only.

## Decision answer

**No reviewed public primary source bridges the whole commercial chain for either product.** Both routes have a defined CPO product and meaningful product-route evidence. Neither has a public record that links an exact SKU to a named customer, dated accepted systems or ports, a repeat shipment, a product-matched supplier allocation, qualified-engine output, and attributable economics.

That result is a disclosure finding, **not** evidence of zero activity, technological failure, or zero revenue. The correct current decision is: **strategically promising, commercially early, no proven CPO profit-pool leader.**

## The required conversion chain

```text
exact CPO SKU → named customer → accepted units / ports → repeat shipments
→ supplier content → qualified-engine evidence → attributable economics
```

The fields must be joined at one product boundary. A platform announcement, a partner quotation, a family-level production statement, or a CPO programme without a disclosed SKU does not clear the chain.

## NVIDIA Spectrum-X Ethernet Photonics

| Conversion field | Public record | Status | Boundary that remains open |
|---|---|---|---|
| Exact CPO SKU | NVIDIA identifies `SN6810` (102.4T) and `SN6800` (409.6T); Dell and NVIDIA manuals use `SN6810-LD` / `SN6800-LD` CPO ordering-family labels. `SN6600-LD` is a separate pluggable route. `CMP-054`, `CMP-057`, `CMP-081`, `CMP-048` | **Pass — product boundary** | Product definition does not identify a buying or accepting customer. |
| Named customer | NVIDIA names CoreWeave, Lambda, Meta, Microsoft and OCI as Spectrum-X Photonics adopters; Lambda describes preparation for Spectrum-X Ethernet integration. `PRI-033`, `CMP-073`, `CMP-077` | **Partial — adopter/platform only** | No source maps any adopter to `SN6810` / `SN6800` or the `-LD` ordering label. |
| Accepted systems / ports / date | No product-matched customer acceptance or installed-base denominator is retained. | **Open** | Customer acceptance date; accepted systems, ports, or qualified lot. |
| Repeat shipment / expansion | No second delivery, expansion, renewal or repeat fleet record for either Ethernet CPO SKU is retained. | **Open** | A dated repeat event at the same SKU/customer boundary. |
| Supplier content | NVIDIA names TSMC for silicon photonics, SPIL for CPO MCM bumping/sort/assembly/test, TFC for laser-module packaging/validation, and Foxconn/Fabrinet for system integration; its ecosystem map includes shared ELS and fibre/connector roles. `CMP-053`, `CMP-083` | **Route evidence** | Exact SKU BOM, PIC/EIC ownership, qualified supplier shares, and commercial terms. |
| Qualified-engine evidence | NVIDIA describes known-good-engine screening, final-stage fibre attachment and validation before shipment. `CMP-051`, `CMP-053` | **Process evidence only** | Yield denominator, rework, acceptance criteria, field returns and warranty cost. |
| Economics | No SKU-matched ASP, supplier revenue share, product gross margin, warranty reserve or realised yield is disclosed. | **Open** | Product-matched price/content/yield/warranty/margin record. |

### NVIDIA false-positive controls

- CoreWeave's named `SN6600-LD` record is pluggable. It cannot be counted as `SN6810`/`SN6800` CPO volume. `CMP-021`, `CMP-046`–`CMP-048`.
- Lambda's named Q3450-LD operating record is Quantum-X InfiniBand, not Spectrum-X Ethernet. It informs deployment-workflow diligence only. `CMP-040`.
- Spectrum-X platform adoption, benchmark evidence, OEM availability and production language do not supply an exact-SKU accepted-unit numerator. `CMP-011`, `CMP-071`–`CMP-073`, `CMP-078`.

**NVIDIA conclusion:** the strongest integrated product/manufacturing narrative, but the Ethernet-CPO commercial numerator and supplier economics remain open.

## Broadcom TH6-Davisson

| Conversion field | Public record | Status | Boundary that remains open |
|---|---|---|---|
| Exact CPO SKU | Broadcom specifies `BCM78919` / TH6-Davisson at 102.4T with 16 × 6.4T optical engines, 200G links and replaceable ELSFP modules. `CMP-018`, `CMP-055` | **Pass — product boundary** | Product definition does not show a customer has accepted the configuration. |
| Named customer | Broadcom names HPE, Celestica, Micas and Nexthop as collaborators/route partners. `CMP-018`, `CMP-074` | **Route evidence only** | No named end customer tied to `BCM78919` CPO. |
| Accepted systems / ports / date | The launch says the device is sampling to early-access customers and partners; the catalogue remains Limited Release. `CMP-018`, `CMP-062` | **Early-access lifecycle signal** | Customer name, acceptance date, qualified lot and accepted system/port denominator. |
| Repeat shipment / expansion | No public repeat delivery, customer expansion or recurring order for `BCM78919` is retained. | **Open** | A dated second delivery/expansion at the CPO configuration boundary. |
| Supplier content | Broadcom owns the switch/SerDes boundary; Corning states a TH6 faceplate-to-chip collaboration. Other named partners are integration routes. `CMP-055`, `CMP-074`, `CMP-085` | **Partial route** | Complete PIC/EIC, ELS, FAU/connector, OSAT and test allocation; qualified share and ownership boundary. |
| Qualified-engine evidence | Historical TH5 qualification/reliability records provide process precedent only. `CMP-063`, `CMP-064`, `CMP-070` | **Not transferable to TH6** | TH6 test ownership, accepted-engine yield, reliability population and service result. |
| Economics | No product-specific price, supplier content, yield/rework, warranty or margin record is disclosed. | **Open** | Product-matched cost and realised margin. |

### Broadcom false-positive controls

- Broadcom's Tomahawk 6 family production-volume language is not a `BCM78919` CPO shipment denominator. `CMP-075`, `CMP-009`.
- Celestica's customer-orderable DS6000 uses Broadcom TH6 silicon but exposes OSFP224 pluggable ports; it is not a `BCM78919` CPO selection. `CMP-029`, `CLM-558`.
- Historical TH5/Micas production and qualification cannot be rolled forward to TH6 200G/lane CPO. `PRI-028`, `PRI-032`, `CMP-063`, `CMP-070`.

**Broadcom conclusion:** the clearest merchant-switch CPO definition and an early-access route, but no public TH6 CPO customer, volume, qualified-engine or economic proof.

## Supplier-allocation disposition

| Layer | NVIDIA `SN6810` / `SN6800` | Broadcom `BCM78919` | Permitted conclusion |
|---|---|---|---|
| PIC / EIC | TSMC process route disclosed; EIC and complete-engine allocation open | Broadcom architecture and TSMC route; allocation open | **Route, not BOM** |
| External laser | TFC/Lumentum/Sumitomo/Coherent roles are disclosed at platform/family scope | ELSFP interface disclosed; supplier allocation open | **Topology/route, not supplier revenue** |
| FAU / connector | NVIDIA ecosystem names fibre/connector roles; exact supplier/attach ownership open | Corning TH6 collaboration; exact assembly and qualified share open | **Collaboration/route, not allocation** |
| OSAT / assembly | SPIL CPO MCM role; Foxconn/Fabrinet system route | No exact TH6 OSAT allocation retained | **NVIDIA route; Broadcom open** |
| Test / qualification | Screening and shipment validation described; metrics open | No TH6 product-linked test owner/metrics retained | **Process evidence, not qualified output** |

No supplier can be credited with an exact-SKU content share, ASP, margin or profit-pool leadership until an exact product allocation and qualified-output/economic record are both public.

## Commercial-conversion watchlist

| Programme | What is public | What is not public | Decision use today |
|---|---|---|---|
| Lumentum 2027 CPO order | Incremental multi-hundred-million-dollar CPO order, deliverable in H1 calendar 2027. `CMP-010`, `CLM-083` | Customer, product, quantity, whether it is ELS/engine/system content, revenue recognition, margin, cancellation terms | **Commercial signal; no supplier or system allocation** |
| TSMC COUPE | 200G transmission with several customers in 2025; CPO/COUPE production target/beginning-production milestone in 2026. `PRI-029`, `CMP-090`, `CLM-213`–`CLM-215`, `CLM-572` | Customer names, product SKU, accepted output, yield, package/test scope, pricing and margin | **Process readiness; no named product conversion** |
| Celestica | Unnamed-hyperscaler CPO switch award; 2027 production ramp expected. `CMP-028`, `CMP-076` | Customer, ASIC/CPO SKU, acceptance, units, supplier allocation, revenue and margin | **2027 timing lead; not NVIDIA/Broadcom attribution** |
| Foxconn | Management target: CPO-switch mass production in Q3 2026 and annual shipments at tens of thousands. `CMP-060`, `CLM-526` | Observed shipments, customer, SKU, acceptance, repeat deliveries, yield and economics | **Forward-looking manufacturer target only** |
| Fabrinet | Broad optical packaging/test capability. `CMP-091`, `CLM-573` | Any CPO programme, SKU, output, yield, revenue/margin or allocation | **Capability diligence route only** |

## Promotion and downgrade tests

### Promotion to commercial proof

For either NVIDIA or Broadcom, require one customer/OEM/operator record that identifies: exact CPO SKU, named customer, acceptance or qualification date, accepted units/ports/systems, and a repeat shipment or expansion. For supplier economics, add product-matched physical allocation plus qualified-output/yield and price, warranty or margin evidence.

### Downgrade of the timing view

Downgrade if the expected production/availability interval passes without an exact-SKU customer/acceptance record, if a named deployment proves to use a pluggable/LPO/NPO configuration, or if service, yield, qualification or cost evidence causes a switch away from CPO.

## Linked controls

- [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md)
- [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md)
- [Commercial-proof decision memo](../07-companies/commercial-proof-dossiers/commercial-proof-decision-memo.md)
- [Exact-SKU search audit](exact-sku-commercial-proof-search-audit-2026-08-12.md)
- [Supplier-attribution audit](../08-model/supplier-attribution-audit-2026-08-12.md)

**Release control:** keep the public conclusion at “strategically promising, commercially early, no proven profit-pool leader.” Do not publish a customer-volume, supplier-revenue, margin, EPS or leader claim from the current record.
