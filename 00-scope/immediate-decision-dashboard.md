# Immediate CPO decision dashboard

**Status:** Private decision control; not a forecast, price target or publication clearance  
**As of:** 2026-08-13  
**Purpose:** Put the six company cases, PIC bottleneck and architecture countercases on one decision page.

## What can be decided now

The current evidence supports relative *strategic exposure* views, not a CPO revenue, EPS, margin, market-share or profit-pool ranking. The common reason is not a lack of technical claims: it is the absence of a product-matched chain from accepted customer volume through supplier content, qualified manufacturing and realised economics.

| Company | Exposure and exact boundary | Evidence grade | Current stance | Single highest-value catalyst | Falsification / downgrade | Missing decision data |
|---|---|---|---|---|---|---|
| NVIDIA | `SN6810-LD` / `SN6800-LD` Spectrum-X Ethernet switch CPO | Product/manufacturing route: medium | Positive strategic exposure | Named customer tied to exact CPO SKU, accepted units and repeat delivery | Production never connects to exact-SKU customer proof; service/yield favours modular alternatives | Customer, accepted systems/ports, repetition, supplier shares, service, economics |
| Broadcom | `BCM78919` / TH6-Davisson merchant switch CPO | Product architecture: medium | Positive enabling exposure | Named TH6 CPO customer, accepted count/date and repeat order | Limited Release/sampling does not convert; alternatives win at lower qualified cost | Customer, units, repeat deployment, content allocation, margin/warranty |
| Coherent | SiPh, InP, VCSEL and packaging component/engine routes | Component route: medium | Constructive component exposure | Named product allocation with qualified engine output and margin boundary | Product milestones slip or content is dual-sourced at weak margin | Exact layer, shipped output, share, price, yield/rework and product margin |
| Lumentum | External-light / ELSFP / UHP-laser layer | Product/order route: medium | Constructive watch | Customer/product/quantity conversion of CPO/ELS orders plus realised margin | Delivery slips, capacity burden is unattractive, or integrated light displaces external laser | Customer, SKU, quantity, content share, realised price, warranty and margin |
| Marvell | Celestial Photonic Fabric accelerator optical-I/O chiplet; separate from switch CPO | Technology/target route: low–medium | Strategic watch | Named XPU customer, production units and reported revenue/margin | FY28/29 targets slip or alternate optical-I/O qualifies first | Product customer, units, revenue recognition, yield/cost and margin |
| TSMC | COUPE SiPh/EIC integration and advanced packaging process | Process route: medium | Manufacturing-control watch | Named COUPE SKU, qualified output and attributable economics | Production milestone fails to become qualified customer volume; alternative integration route wins | Complete-engine scope, output, allocation, pricing, capex and margin |

**Readout:** NVIDIA and Broadcom have the clearest switch-CPO product boundaries. Coherent and Lumentum are the most relevant optical-component routes. TSMC is a process-control watch. Marvell is an important but separate accelerator optical-I/O case. No row clears an attributable CPO economics gate.

## Exact-SKU commercial-conversion control

The two switch-CPO routes must clear the same chain before their strategic
position becomes commercial or financial evidence:

```text
SKU → named customer → accepted units / ports → repeat shipments
→ supplier content → qualified-engine evidence → economics
```

| Platform | Current cleared fields | Open fields | Current decision label |
|---|---|---|---|
| NVIDIA Spectrum-X Ethernet Photonics `SN6810` / `SN6800` | Exact CPO product; manufacturing and ecosystem **routes** | Customer-to-SKU mapping; acceptance date; units/ports; repeat shipment; exact BOM/share; yield/service and economics | Strategically promising; commercially early |
| Broadcom TH6-Davisson `BCM78919` | Exact CPO product; early-access lifecycle; partner **routes** | Named end customer; acceptance date; units/ports; repeat shipment; PIC/EIC/ELS/FAU/OSAT/test allocation; TH6 qualified output and economics | Strategically promising; commercially early |

**Hard control:** product-family production, a CPO programme with no disclosed
SKU, an ecosystem/partner announcement, or a pluggable TH6/Spectrum-X route is
not an accepted CPO shipment. Current conclusion: **no proven CPO profit-pool
leader**. See the [NVIDIA/Broadcom commercial-conversion dossier](../09-primary-research/nvidia-broadcom-commercial-conversion-dossier-2026-08-13.md).

## The investable PIC question

The question is not “which PIC has the best laboratory specification?” It is: **which route can lower the cost per qualified, serviceable optical engine at the required lane rate while retaining a defensible content and margin boundary?**

| Route | Current strategic role | Bottleneck that determines investability | Current state | What would promote it |
|---|---|---|---|---|
| SiPh + external laser | Leading disclosed switch-CPO process route | Delivered laser power, fibre attach, final-engine yield and replaceable-service boundary | Partial process proof; economics open | Product-matched yield waterfall, engine allocation, service data and gross margin |
| Monolithic / TEC-less InP | Dense transmitter and modular 400G/lane countercase | Compound yield, packaging, full power/lifetime and module qualification | Strong device evidence; commercial proof open | Qualified output, complete power/thermal test and customer economics |
| TFLN pluggable | High-rate modular countercase | Packaging/manufacturing/qualification rather than baud rate | Transmission proof; economics open | Same-system 400G comparison with power, service and qualified cost |
| Heterogeneous / 2.5D integration | Potential integration/test control point | Known-good die, attach/test/rework and final good-engine cost | Process mechanisms; final yield open | Lot-level cost-per-good-engine data and named product content/margin |

## Architecture decision rule

| Architecture | Current role | What would make it win the same-system test |
|---|---|---|
| Retimed pluggable | Modularity and service benchmark | CPO must show enough power/density benefit to offset replacement and qualification burden |
| LPO / RTLR | Live electrical/power countercase while retaining a module boundary | Same-ASIC 200G/400G field data with power, BER/FEC, service and total-cost boundaries |
| NPO / OBO | Plausible CPO-deferral route | Qualified replaceable near-package boundary with clear interoperability and repair economics |
| Switch CPO | Strongest disclosed 200G product/timing signal | Final yield, serviceability and total restored-port cost must beat alternatives at same boundary |

## Operating conclusion

Maintain the present conclusion until one product-matched evidence bundle clears both a commercial gate (customer, accepted numerator, repetition) and an economic gate (content, yield/rework, warranty and margin). The absence of those disclosures is consistent with early commercialisation and commercially sensitive terms; it is not evidence of no activity or technological failure.

## Controlling detail

- [Six-company variant cards](../07-companies/variant-cards/core-company-variant-cards.md)
- [PIC technology scorecard](../03-components/pic-technology-decision-scorecard.md)
- [Manufacturing cost-per-good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md)
- [Common architecture boundary scorecard](../02-architecture/system-boundary-comparison-scorecard.md)
- [Profit-pool input reconciliation](../08-model/profit-pool-input-reconciliation-2026-08-12.md)
