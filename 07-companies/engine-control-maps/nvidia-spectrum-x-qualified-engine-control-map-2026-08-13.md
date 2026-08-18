# NVIDIA Spectrum-X qualified-engine control map

**Scope:** SN6800/SN6810 family route; not a bill of materials or allocation  
**As of:** 2026-08-13

| Layer | Public role classification | Named public controller / role | Economic boundary | Required proof of defensible value capture |
|---|---|---|---|---|
| ASIC / SerDes | Confirmed | NVIDIA platform/product owner | Platform price may include system value; CPO content unallocated | Product margin or supplier-content allocation |
| PIC / EIC integration | Confirmed process role | TSMC COUPE integration | Process/foundry fee boundary unknown | SKU-linked output, price and margin |
| Laser / ELS | Confirmed shared role | Lumentum, Sumitomo, Coherent; TFC module validation | Shared route, no laser-die/module share | Allocated product, quantity, ASP, yield/warranty |
| Fibre interface | Confirmed ecosystem / attach owner open | SENKO connector ecosystem; NVIDIA final attach process | Connector and attach are separate charge points but allocation open | Exact SKU supply, qualified share, mating/service economics |
| Assembly / OSAT | Confirmed family role | SPIL bump/sort/assembly/test | Final-package scope and price unknown | Product flow, accepted yield, rework and OSAT economics |
| Test / burn-in | Family process role / tooling open | SPIL test; Teradyne/ficonTEC/Advantest/Aehr are capability routes | No tested-unit denominator or test supplier allocation | Test time/coverage/escape, accepted output, cost |
| System integration | Confirmed family role | Foxconn / Fabrinet | Chassis/system economics distinct from engine | SKU contract, content/revenue/margin |
| Service | Partial | Dell warranty; ELS and connector service boundaries | Warranty owner and replacement unit unknown | Field return/MTTR/spares/warranty allocation |

## Economic readout

NVIDIA controls the platform; TSMC/SPIL and the named ecosystem control important manufacturing routes. Public evidence does not show which party captures engine/PIC/laser/attach/test gross profit. The likely constrained qualified-engine step is fibre-interface plus package/test, but no supplier can be promoted on that inference.

**Upgrade requirement:** one SN6800/SN6810 product record joining accepted units, supplier allocation, stage yield/service and commercial terms.

**Anchors:** `CMP-053`, `CMP-054`, `CMP-058`, `CMP-067`, `CMP-068`, `CMP-083`, `CMP-090`; `CLM-515`, `CLM-556`, `CLM-557`.
