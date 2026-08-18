# CPO falsification dashboard and thesis-change log

**Status:** Active; 12 August external-light and historical TH5 reliability-boundary updates recorded; no substantive thesis change  
**Owner:** Nur Alpys  
**As of:** 2026-08-12

## Purpose

This dashboard turns the provisional thesis into observable tests. A new announcement changes the thesis only when it crosses the stated evidence boundary. Supportive evidence and disconfirming evidence are logged together; absence of disclosure is not treated as proof either way.

## Baseline thesis

The complete scale-out optical-engine platform—PIC, driver/TIA, laser interface, fibre attach, package, test/control and serviceability—has a better chance of retaining durable external profit than an isolated PIC or laser component. Switch-side 200G/lane CPO currently has the strongest commercial-timing signal, but no company is yet proven to own the largest sustainable optical-engine profit pool.

## Falsification tests

| ID | Thesis proposition | Evidence that would support it | Falsifying or confidence-reducing trigger | Current state | Next record needed |
|---|---|---|---|---|---|
| F-01 | 200G/lane switch CPO reaches commercial proof before 200G LPO | Customer-accepted CPO SKU, repeat production, and matched qualification/TCO evidence before equivalent LPO proof | Two independent customers deploy qualified 200G LPO at lower qualified cost before CPO repeat production | NVIDIA `SN6800`/`SN6810` and Broadcom `BCM78919` product boundaries are now specific; Broadcom remains early-access / Limited Release and neither has a cleared customer numerator (`CLM-514`–`CLM-515`; `CLM-530`) | Named CPO and LPO customer SKUs, units, qualification and TCO |
| F-02 | CPO power advantage survives the full cost stack | Matched inlet-power, cooling, service and cost-per-delivered-bit result remains positive | Package, yield, spare or service cost erases the modeled CPO-versus-LPO power benefit | Central model shows only ~66.8 W CPO advantage over LPO; TCO incomplete | Same-boundary chassis power plus ASP, yield, service and capex |
| F-03 | Fibre attach is a controllable manufacturing gate | Production Cpk, first-pass yield, cycle time, rework and escape data improve with known-good-die/test insertion | Final attach yield remains low or rework/warranty consumes the margin | PAP-015, PAP-043 and CMP-052 establish mechanisms/equipment, not factory output | Supplier lot data at 200G/400G engine boundary |
| F-04 | External InP/ELS remains a valuable supplier layer | Qualified ELSFP/laser share, repeat orders and delivered-power economics support attractive margin | Lasers become interchangeable, multisourced and price-competed with no service premium | Lumentum has the strongest external-light conversion signal: an earlier CPO order plus an initial ELS-module order statement; Sumitomo provides a credible technical countercase. Neither order disclosure identifies product allocation or economics. | Product allocation, ASP, second source, lifetime and warranty terms |
| F-05 | Complete-engine integration captures more value than an isolated PIC | One supplier retains PIC, laser interface, package, test and service content at repeat margin | Platform owner internalises those layers or contract manufacturing captures them at commodity pricing | Provisional thesis only; supplier responsibility map is incomplete | BOM, contracts, transfer prices and margin by layer |
| F-06 | Socketable/detachable serviceability can offset package complexity | Measured MTTR, spare policy, field failures and lower downtime offset connector/socket cost | Connector failures, inventory or blast radius exceed pluggable replacement savings | Connector and socket evidence is laboratory/process-level | Field service and warranty data at same system boundary |
| F-07 | TSMC/OSAT process control is a control point, not automatic profit ownership | Named qualified output, package responsibility, capacity allocation and transfer economics | Platform owner or OSAT captures value while foundry receives commodity process pricing | TSMC, SPIL and related roles are mapped, but economics open | Customer-linked SKU, qualified output and contract economics |
| F-08 | 400G/lane CPO is a credible next-generation extension | Complete 400G/lane engine meets BER/TDECQ, thermal, yield and qualification gates | 400G path slips while LPO/NPO or copper alternatives qualify first | PAP-044 measures an engine boundary; no complete production route | Full 400G/lane link, qualification lot and cost |
| F-09 | CPO adoption is earnings-material for an optical supplier before a platform owner | Attributable CPO revenue exceeds a materiality threshold for Coherent/Lumentum/Celestica | CPO remains too small, low-margin or internalised to affect supplier earnings | Earnings screen shows smaller suppliers have lower thresholds; revenue unallocated | CPO revenue/content/margin line or contract bridge |
| F-10 | The thesis can support an investable public-equity conclusion | Evidence clears product, manufacturing, commercial, financial and expectations gates | No company has attributable earnings, valuation gap or downside protection after diligence | No investment decision currently justified | Product economics plus dated consensus/valuation inputs |

## Current baseline and change rule

The current commercial-proof priors are maintained in [commercial-proof probability priors](commercial-proof-probability-priors.md). These are analyst ranges, not observations. Change a range only when a record changes one of the following fields:

1. Exact product/SKU and architecture boundary.
2. Customer acceptance or qualification date.
3. Units, ports, repeat shipment or expansion.
4. Final-engine yield, test/rework, field failure or service cost.
5. Supplier content, realised price, margin, capex or cannibalisation.

Do not change a probability because a company repeats an unchanged roadmap claim or because a secondary article repeats an unretained source.

## Thesis-change log

| Date | Event / source | Claim IDs | What changed | Probability or ranking change | Why |
|---|---|---|---|---|---|
| 2026-08-09 | Dashboard created | — | Baseline recorded; no substantive thesis change | None | Existing evidence remains supportive of timing and process mechanisms but insufficient for profit leadership |
| 2026-08-11 | NVIDIA Spectrum-X SKU reconciliation and Broadcom CPO catalogue lifecycle check | `CLM-514`–`CLM-515`; `CLM-530` | NVIDIA CPO configurations are controlled as `SN6800` / `SN6810`; Broadcom `BCM78919` is confirmed Limited Release rather than assumed general-volume availability | None | Product/lifecycle precision improved, but no source supplies a named customer, accepted units/ports, repeat delivery, supplier allocation or economics at the same SKU boundary. |
| 2026-08-12 | Lumentum FY2026 Q4 results | `CLM-531` | Added a company statement that an initial ELS-module order exists, alongside increasing demand for ultra-high-power CPO lasers. | None | The statement is a route-conversion signal only: it gives no customer, product/SKU, platform, quantity, delivery date, revenue, supplier share, product margin, yield or warranty allocation. It cannot alter switch-CPO commercial proof or a profit-pool ranking. |
| 2026-08-12 | Broadcom TH6-Davisson briefing | `CLM-532` | Recovered a first-party source for the previously secondary-reported no-link-flap observation; detailed slides identify it as a historical TH5-Bailly, 100G/lane result. | None | The PDF lacks a customer, population, conditions, port denominator, field-return, warranty or TH6 boundary. It sharpens a historical reliability control but cannot prove TH6 deployment, 200G/lane reliability or profit capture. |
| 2026-08-12 | Broadcom CPO reliability release | `CLM-533` | Identified Meta as the high-temperature lab-characterisation setting for the historical 1M cumulative 400G-equivalent flap-free CPO port-device-hours result. | None | Named lab context is stronger than an unnamed slide claim, but it supplies no TH6 SKU, accepted units, installed base, test population/duration, field returns, supplier economics or profit-pool evidence. |

## Current decision state

- **Commercial timing:** switch-side 200G/lane CPO has the strongest public production signal, but commercial proof is not independently cleared.
- **Technical leader:** no single leader established across PIC, laser, package, test and service.
- **Manufacturing control point:** TSMC/SPIL/TFC/Foxconn and Teradyne/ficonTEC roles are visible; supplier economics are not.
- **Profit-pool leader:** no leader established.
- **Investment conclusion:** no decision until product-specific revenue, margin, yield, service, capex and valuation evidence are linked.

## Linked controls

- [Scale-out optical-engine profit-pool thesis](../00-scope/scale-out-optical-engine-profit-pool-thesis.md)
- [Commercial-proof probability priors](commercial-proof-probability-priors.md)
- [Decision-output completion audit](decision-output-completion-audit.md)
- [Evidence-gate register](evidence-gate-register.md)
- [Critical-path milestone tracker](critical-path-milestone-tracker.md)
