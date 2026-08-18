# Broadcom TH6-Davisson qualified-engine control map

**Scope:** BCM78919 / TH6-Davisson; not a bill of materials or allocation  
**As of:** 2026-08-13

| Layer | Public role classification | Named public controller / role | Economic boundary | Required proof of defensible value capture |
|---|---|---|---|---|
| ASIC / SerDes | Confirmed | Broadcom BCM78919 / Condor SerDes | Merchant-switch product control; engine economics separate | CPO product margin or content allocation |
| PIC / optical engine | Architecture confirmed; supplier route open | Broadcom integrated engines; COUPE route mentioned | PIC/EIC ownership and price open | Qualified engine supplier/share and economics |
| Laser / ELSFP | Interface confirmed; supplier open | Field-replaceable ELSFP | Laser provider, split, price, reliability open | Named ELSFP supplier/product plus service/warranty economics |
| Fibre interface | TH6 collaboration confirmed | Corning faceplate-to-chip collaboration | Scope could span fibre/FAU/optical management; exact content open | SKU allocation, attach yield, loss/rework and price |
| Assembly / OSAT | Open | No retained TH6-specific OSAT allocation | Entire package cost/yield boundary open | Named assembly flow and accepted yield |
| Test / burn-in | Open | No TH6 test owner or result | Tooling availability is not product evidence | Test flow, coverage/escape/cost and qualification data |
| System integration | Partner/demo route | Micas, Celestica, HPE, Nexthop partner ecosystem | Partner demo is not customer economics | Customer accepted units and commercial terms |
| Service | Partial | ELSFP; historical TH5 evidence only | Replaceable laser is not engine/package replacement | TH6 field procedure, MTTR, returns and warranty allocation |

## Economic readout

Broadcom has the clearest merchant-switch product boundary, but the qualified engine is a black box economically: no public PIC, laser, package, test or OSAT allocation is sufficiently SKU-linked. Historical TH5 service/reliability must not be transferred to TH6.

**Upgrade requirement:** a TH6 customer record joining accepted units with a qualified engine/ELS/attach flow and supplier economics.

**Anchors:** `CMP-055`, `CMP-063`, `CMP-070`, `CMP-074`, `CMP-085`; `CLM-516`, `CLM-517`, `CLM-529`.
