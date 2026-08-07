# Company evidence-gap matrix

**Status:** Cross-dossier diligence control; not a numeric ranking  
**As of:** 2026-08-07

This matrix prevents a company claim in one value-chain layer from being counted as proof in another. “Observed” means the retained record directly supports the stated boundary; “claimed” means the company states it; “missing” means the input is not publicly evidenced in the reviewed packet.

| Required scorecard field | Broadcom | NVIDIA | Coherent | Lumentum | TSMC | Celestica |
|---|---|---|---|---|---|
| Defined product / architecture | Claimed 102.4T TH6-Davisson, 16 × 6.4T engines, 200G links | Claimed Spectrum-X Ethernet Photonics CPO, 200G SerDes | Claimed 6.4T socketed SiPh CPO, VCSEL CPO and 400G InP modulation | Observed product boundary for UHP/ELSFP; claimed CPO order and demonstrations | Claimed COUPE-on-substrate CPO, 200G MRM and 3D photonic/electrical stacking | Claimed design/manufacturing program for an unnamed hyperscaler CPO switch; separate DS6000 platform is 64 × 1.6TbE and supports optical or copper |
| Customer / qualification evidence | Missing named production CPO customer and repeat units | Two CoreWeave pages claim early Photonics CPO adoption and deployment of the 102.4T SN6600-LD; fleet size, repeat deployments and qualification remain missing | NVIDIA purchase/capacity agreement claimed; product allocation, qualification and repeat CPO volume missing | NVIDIA purchase/capacity agreement claimed; product allocation, qualification and repeat CPO volume missing | “Several customers” 200G result claimed; names, SKU, qualification and repeat units missing | Awarded unnamed hyperscaler program; 2027 ramp planned, but units, qualification and repeat orders missing |
| Measured complete-engine performance | Missing matched chassis/engine result | Missing matched chassis/engine result | Missing independent complete-engine result | Missing independent complete-engine result | Missing complete-engine result; >99% is stacking yield on engineering samples only | Missing; no engine-level measurement or CPO-specific test result disclosed |
| PIC / laser ownership | Broadcom platform claim; supplier split missing | Platform route; supplier split missing | Broad SiPh, InP, VCSEL and packaging stack claimed | Strongest retained evidence in high-power InP/ELSFP layer | COUPE integrates photonic and electrical-control chips; laser, fibre attach and final package ownership missing | No attributable PIC/laser ownership; program supplier map missing |
| Fibre attach / package yield | Missing | Missing | Missing final-engine yield and attach cycle time | Missing final-engine yield and attach cycle time | Missing; engineering-sample stacking yield does not clear attach or final-engine gates | Missing system/engine yield, attach cycle time, rework and test escape data |
| Reliability / serviceability | ELSFP replaceability claimed; engine service missing | Service and warranty model missing | Socketed demonstration; field repair and warranty missing | ELSFP source serviceability claimed; engine/package service missing | CPO production milestone claimed; field reliability, repair and warranty model missing | Liquid-cooled CPO program claimed; service model, field failure and warranty allocation missing |
| Capacity / capex | CPO-specific capacity allocation missing | CPO-specific capacity allocation missing | NVIDIA $2B investment and multibillion purchase/capacity commitment claimed; six-inch InP/CPO allocation and qualified output missing | NVIDIA $2B investment and multibillion purchase/capacity commitment claimed; Greensboro 6-inch InP ramp planned mid-2028; qualified output and CPO allocation missing | COUPE-on-substrate production beginning in 2026 claimed; actual output, line allocation and attributable capex missing | 2027 program ramp expected; CPO-specific capex, line capacity and working-capital requirement missing |
| Supplier share / content per system | Missing | Missing | Missing | Missing | Missing; process control is not the same as complete-engine revenue share | Missing; system manufacturing content and optical-engine pass-through are unknown |
| CPO-specific ASP / gross margin | Missing | Missing | Missing | Missing | Missing | Missing; Celestica-wide HPS margins cannot be applied to the program |
| Cannibalisation / support cost | Missing | Missing | Missing | Missing | Missing | Missing; platform mix and warranty/service cost are undisclosed |
| Evidence-adjusted current read | Merchant CPO product-definition lead | Full-system/customer-route lead | Component breadth plus newly strengthened NVIDIA capacity/customer-route evidence | External-laser commercial-visibility plus newly strengthened NVIDIA capacity/customer-route evidence | Process/stacking control-point lead; no proven profit leadership | Manufacturing-route candidate with planned 2027 hyperscaler CPO ramp; no proven optical-engine or profit leadership |

## What can be concluded now

- Broadcom and NVIDIA can be compared on platform control and disclosed product status, but not on CPO profit.
- Coherent and Lumentum can be compared on component breadth, external-light-source evidence and commercial visibility, but not on complete-engine margin or yield.
- TSMC can now be compared on COUPE process/stacking control and dated production milestones, but not on complete-engine content, final yield or profit capture.
- No company passes the five conditions for a base-case profit forecast in `08-model/optical-engine-profit-pool-input-gates.md`.

## Highest-value missing records

1. Customer-confirmed SKU, production date, unit count and repeat order.
2. Bill of materials and supplier responsibility map per switch, engine and ELSFP.
3. Die-to-engine yield waterfall, attach/test cycle time, rework and field-return rate.
4. Product ASP, realised gross margin, warranty reserve and price-down schedule.
5. Attributable capacity capital, second-source status and cancellation protection.
6. TSMC COUPE production conversion: named SKU, shipped units, qualified line, final-engine yield and package responsibility.

## Sources

- [Broadcom and NVIDIA switch-CPO dossier](broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum external optical-engine dossier](coherent-lumentum-external-optical-engine-dossier.md)
- [Marvell / Celestial accelerator optical-I/O dossier](marvell-celestial-accelerator-optical-io-dossier.md)
- [Celestica CPO manufacturing-route dossier](celestica-cpo-manufacturing-route-dossier.md)
- [Leadership scorecard](leader-scorecard.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
