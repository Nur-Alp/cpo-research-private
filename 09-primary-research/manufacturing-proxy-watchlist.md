# Public manufacturing-proxy watchlist

**Status:** Private directional-readiness control; proxies cannot clear commercial, yield or economics gates  
**As of:** 2026-08-13

## Interpretation rule

Equipment orders, fab expansion, test-cell announcements, OSAT partnerships and
hiring can indicate *preparation* for scale. They do not identify an exact CPO
SKU, accepted output, yield, customer, supplier allocation, price or margin.
Every proxy must therefore remain below the production-evidence ladder.

| Proxy class | Examples to monitor | What it can update | What it cannot update | Exact search terms |
|---|---|---|---|---|
| Equipment order / installation | Wafer probe, optical alignment, burn-in, active alignment, fibre attach, high-speed test | Manufacturing capability and likely process bottleneck | Customer product, output, yield or economics | `CPO` / `silicon photonics` + `order`, `installed`, `wafer test`, `burn-in`, `active alignment` |
| Factory / capacity expansion | InP/laser fab, SiPh line, OSAT/advanced packaging or fibre-assembly expansion | Capacity option and capex direction | CPO allocation, utilisation, realised revenue/margin | Company + `expansion`, `capacity`, `InP`, `silicon photonics`, `CPO`, `advanced packaging` |
| Laser / SiPh supply | External laser, ELSFP, PIC/EIC wafer, coupling/connector production | Potential supplier route and technical dependency | Qualified share, ASP, warranty or engine economics | `ELSFP`, `external laser`, `UHP`, `SiPh`, `COUPE`, `optical engine` |
| Test-system deployment | ATE, double-sided wafer probe, package test, burn-in, reliability test | Test insertion points and screening readiness | Throughput, coverage, escape, accepted-engine yield or cost | `Photon 100`, `ficonTEC`, `wafer probe`, `CPO test`, `hybrid bonded` |
| OSAT / integration partnership | Assembly/test, package, fibre attach, system integration | Route map and potential control point | Exact product allocation, share or gross margin | `CPO` + `assembly`, `OSAT`, `SPIL`, `Fabrinet`, `Foxconn`, `fibre attach` |
| Hiring | Photonics packaging, reliability, NPI, test development, manufacturing engineering | Organisational capability/capacity direction | Production start, customer, quality or revenue | Company + `CPO`, `silicon photonics`, `optical packaging`, `reliability`, `test` |

## Proxy recording format

| Date | Company / site | Proxy | Exact wording | Product/SKU linkage | Permitted inference | Prohibited inference | Follow-up gate |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD |  |  |  | Exact / family / none | Capability, capacity or route only | Shipment, yield, revenue or margin | Yield/test, supplier map or economics |

## Existing retained proxy examples

| Evidence | Proper interpretation |
|---|---|
| Aehr follow-on SiPh burn-in orders | Screening-capacity direction; no named CPO product or output denominator |
| TSMC COUPE process milestones | SiPh/EIC integration capability; no complete-engine economic allocation |
| NVIDIA/SPIL/TSMC/Foxconn route map | Family/platform manufacturing responsibility; not an exact-SKU BOM or supplier economics |
| Lumentum planned InP manufacturing expansion | Capacity route; not qualified CPO output or gross profit |

Use this watchlist with the [manufacturing cost-per-good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md) and the [public evidence extraction pack](public-evidence-extraction-pack.md).
