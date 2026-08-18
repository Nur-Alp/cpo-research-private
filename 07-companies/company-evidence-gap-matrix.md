# Company evidence-gap matrix

**Status:** Cross-dossier diligence control; not a numeric ranking  
**As of:** 2026-08-12

The [six-company commercial-proof queue](six-company-commercial-proof-queue-2026-08-12.md) prioritizes the next evidence request for each company and defines the gate needed before numeric modelling.

This matrix prevents a company claim in one value-chain layer from being counted as proof in another. “Observed” means the retained record directly supports the stated boundary; “claimed” means the company states it; “missing” means the input is not publicly evidenced in the reviewed packet.

| Required scorecard field | Broadcom | NVIDIA | Coherent | Lumentum | TSMC | Celestica | Fabrinet |
|---|---|---|---|---|---|
| Defined product / architecture | Claimed 102.4T TH6-Davisson, 16 × 6.4T engines, 200G links | Claimed Spectrum-X Ethernet Photonics CPO, 200G SerDes | Claimed 6.4T socketed SiPh CPO, VCSEL CPO and 400G InP modulation; Tower/Coherent report a 420 Gb/s PAM4 silicon-MZM demonstration in a stated production-ready SiPho process | Observed product boundary for UHP/ELSFP; claimed CPO order and demonstrations | Claimed COUPE-on-substrate CPO, 200G MRM and 3D photonic/electrical stacking | Claimed design/manufacturing program for an unnamed hyperscaler CPO switch; separate DS6000 platform is 64 × 1.6TbE and supports optical or copper | General advanced optical packaging and outsourced manufacturing flow; no named CPO SKU |
| Customer / qualification evidence | A named **historical Meta lab-evaluation setting** exists for CPO reliability, but named production TH6 customer, accepted units and repeat shipments remain missing; current BCM78919 catalogue status is **Limited Release** | CoreWeave separately claims early Photonics CPO adoption, but its named 102.4T SN6600-LD deployment is classified as pluggable RHS by CMP-048; CMP-053 repeats CoreWeave/Lambda/OCI as first adopters and says systems are validated before shipment, but exact CPO SKU, fleet size, repeat deployments and qualification remain missing | NVIDIA purchase/capacity agreement claimed; product allocation, qualification and repeat CPO volume missing | An early ELS-module order and demand for UHP CPO lasers are disclosed in FY2026 Q4 results, but customer, exact product/platform, quantity, acceptance and repeat-volume evidence remain missing | “Several customers” 200G result claimed; names, SKU, qualification and repeat units missing | Awarded unnamed hyperscaler program; 2027 ramp planned, but units, qualification and repeat orders missing | General 3–6 month qualification process; no CPO customer, SKU or line-certification evidence |
| Measured complete-engine performance | Missing matched chassis/engine result | Missing matched chassis/engine result | 420 Gb/s PAM4 open eye at modulator level; complete-engine and system boundary missing | Missing independent complete-engine result | Missing complete-engine result; >99% is stacking yield on engineering samples only | Missing; no engine-level measurement or CPO-specific test result disclosed | Missing CPO engine result |
| PIC / laser ownership | Broadcom platform claim; supplier split missing | Platform route; supplier split missing | Broad SiPh, InP, VCSEL and packaging stack claimed | Strongest retained evidence in high-power InP/ELSFP layer | COUPE integrates photonic and electrical-control chips; laser, fibre attach and final package ownership missing | No attributable PIC/laser ownership; program supplier map missing | No attributable PIC/laser ownership; likely contract-manufacturing layer only |
| Fibre attach / package yield | Missing | Missing | Missing final-engine yield and attach cycle time | Missing final-engine yield and attach cycle time | Missing; engineering-sample stacking yield does not clear attach or final-engine gates | Missing system/engine yield, attach cycle time, rework and test escape data | Capability claimed; CPO-specific yield, attach cycle time, rework and test escape missing |
| Reliability / serviceability | Historical TH5/100G-lane Meta lab result reports 1M cumulative 400G-equivalent flap-free CPO port device-hours; ELSFP replaceability is claimed. Test protocol, population, field return and TH6 service record remain missing. | Dell lists three-year limited warranty and next-business-day onsite service for CPO SKU families, but engine repair workflow, achieved MTTR and field-failure data remain missing | Socketed demonstration; field repair and warranty missing | ELSFP source serviceability claimed; engine/package service missing | CPO production milestone claimed; field reliability, repair and warranty model missing | Liquid-cooled CPO program claimed; service model, field failure and warranty allocation missing | Reliability lab and qualification process disclosed generally; CPO field/service data missing |
| Capacity / capex | CPO-specific capacity allocation missing | CMP-053 names TSMC, SPIL, TFC and Foxconn across the production chain, but CPO-specific capacity allocation, qualified output and attributable capex remain missing | NVIDIA $2B investment and multibillion purchase/capacity commitment claimed; six-inch InP/CPO allocation and qualified output missing | NVIDIA $2B investment and multibillion purchase/capacity commitment claimed; Greensboro 6-inch InP ramp planned mid-2028; qualified output and CPO allocation missing | COUPE-on-substrate production beginning in 2026 claimed; actual output, line allocation and attributable capex missing | 2027 program ramp expected; CPO-specific capex, line capacity and working-capital requirement missing | FY2025 capex $130.7M and Thailand expansion disclosed; CPO-specific allocation missing |
| Supplier share / content per system | Missing | Missing | Missing | Missing | Missing; process control is not the same as complete-engine revenue share | Missing; system manufacturing content and optical-engine pass-through are unknown | Missing; filing does not identify CPO content or pass-through |
| CPO-specific ASP / gross margin | Missing | Missing | Missing | Missing | Missing | Missing; Celestica-wide HPS margins cannot be applied to the program | Missing; 12.1% company gross margin cannot be applied to CPO |
| Cannibalisation / support cost | Missing | Missing | Missing | Missing | Missing | Missing; platform mix and warranty/service cost are undisclosed | Missing; customer concentration and short commitments increase risk but do not quantify CPO support cost |
| Evidence-adjusted current read | Merchant CPO product-definition lead; Limited Release prevents a volume inference | Full-system/customer-route lead; named OEM SKU and warranty policy do not supply a customer CPO shipment numerator | Component breadth plus newly strengthened NVIDIA capacity/customer-route evidence | External-laser commercial-visibility: disclosed early ELS order and UHP-laser demand, but no attributable CPO revenue or profit signal | Process/stacking control-point lead; no proven profit leadership | Manufacturing-route candidate with planned 2027 hyperscaler CPO ramp; no proven optical-engine or profit leadership | Manufacturing-route candidate with broad optical packaging capability; no CPO attribution or profit leadership |

## What can be concluded now

- Broadcom and NVIDIA can be compared on platform control and disclosed product status, but not on CPO profit.
- Coherent and Lumentum can be compared on component breadth, external-light-source evidence and commercial visibility. Lumentum's FY2026 Q4 initial ELS-module order is a commercial-route signal, not a product/customer/quantity or CPO-margin disclosure (FIL-014 / CLM-531).
- TSMC can now be compared on COUPE process/stacking control and dated production milestones, but not on complete-engine content, final yield or profit capture.
- No company passes the five conditions for a base-case profit forecast in `08-model/optical-engine-profit-pool-input-gates.md`.

## Second-group extension

| Company / route | What is now evidenced | What remains blocked |
|---|---|---|
| Intel OCI/PIC | Live-data OCI chiplet prototype co-packaged with a CPU; Intel also claims more than 8 million PICs and 32 million integrated lasers shipped in pluggable products (`CMP-035`, `CLM-304`–`CLM-305`). | OCI/CPO production units, complete-engine yield, attach/test cycle time, qualification, field reliability, ASP and margin. |
| Ranovus / Jabil ODIN | Monolithic EPIC architecture and a planned Jabil high-volume manufacturing route for CPO/NPO optical engines (`CMP-036`, `CLM-306`). | Shipped volume, customer SKU, qualified yield, process ownership, content share, ASP, margin and service data. |
| Cisco / Acacia | Cisco reports system-level LPO/CPO qualification and supply-chain approach; Acacia separately announced 200G/lane silicon-photonic engines and reported prior volume of more than one million 100G/lane engines (`CMP-037`–`CMP-038`, `CLM-307`–`CLM-311`). | 200G/lane production and qualification, PIC/laser/package ownership, fibre-attach loss and yield, CPO attribution, ASP and margin. |

## Highest-value missing records

1. Customer-confirmed SKU, production date, unit count and repeat order.
2. Bill of materials and supplier responsibility map per switch, engine and ELSFP.
3. Die-to-engine yield waterfall, attach/test cycle time, rework and field-return rate.
4. Product ASP, realised gross margin, warranty reserve and price-down schedule.
5. Attributable capacity capital, second-source status and cancellation protection.
6. TSMC COUPE production conversion: named SKU, shipped units, qualified line, final-engine yield and package responsibility.

## Sources

- [Second-group optical-engine comparator dossier](second-group-optical-engine-comparators-dossier.md)
- [Accelerator optical-I/O and NPO comparator dossier](accelerator-optical-io-comparator-dossier.md)

- [Broadcom and NVIDIA switch-CPO dossier](broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum external optical-engine dossier](coherent-lumentum-external-optical-engine-dossier.md)
- [Marvell / Celestial accelerator optical-I/O dossier](marvell-celestial-accelerator-optical-io-dossier.md)
- [Celestica CPO manufacturing-route dossier](celestica-cpo-manufacturing-route-dossier.md)
- [Fabrinet manufacturing-route dossier](fabrinet-manufacturing-route-dossier.md)
- [Leadership scorecard](leader-scorecard.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
