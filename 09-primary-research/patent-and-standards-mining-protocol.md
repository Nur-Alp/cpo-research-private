# Patent and standards mining protocol

**Status:** Private architecture-diligence protocol; no patent or standard proves deployment or profit capture  
**As of:** 2026-08-13

## What this research can answer

Patents can disclose intended design choices before product details are public:
external-laser topology, fibre attach, package stack, optical test insertion,
connector/removability and failure isolation. Standards can show what must
interoperate and which service/management assumptions are being formalised.
Neither establishes customer adoption, production yield, supplier allocation or
economics.

## Patent search map

| Topic | Assignee starting points | Query terms | Extract | Boundary warning |
|---|---|---|---|---|
| Fibre attach / connector | NVIDIA, Broadcom, TSMC, Corning, SENKO, Ayar, Lightmatter, Coherent, Lumentum | `co-packaged optics fibre attach`, `detachable optical`, `optical connector`, `fibre array unit` | Attachment sequence, alignment, detachable boundary, rework/service intention | Filing may never ship; inventor/assignee is not supplier allocation |
| External laser / service | Broadcom, NVIDIA, Lumentum, Coherent, Sumitomo | `external laser source`, `ELSFP`, `laser module`, `replaceable laser` | Laser count/redundancy, power path, replacement scope, management | A replaceable laser is not a replaceable engine/package |
| PIC/EIC/package | TSMC, Broadcom, Intel, NVIDIA, IBM, Marvell, Celestial | `photonic engine`, `EIC PIC`, `hybrid bond`, `COUPE`, `co-packaged` | Die/package boundary, thermal path, test insertion and integration sequence | Patent architecture is not final product BOM or yield |
| Test / known-good die | Teradyne, Advantest, ficonTEC, Ayar, Lightmatter, IBM, Intel | `silicon photonics test`, `known good die`, `optical engine test`, `wafer burn in` | Test stages, alignment, screening before final assembly, possible rework boundary | Test method does not give test time, coverage or cost |

## Standards search map

| Body / record | Questions to extract | Decision use | Do not infer |
|---|---|---|---|
| OIF CEI / EEI / ELSFP | Electrical loss budgets, module/laser management, hot-plug and interop requirements | Whether LPO/RTLR/external-light retains a practical modular boundary | Qualified product, adoption volume or cost |
| IEEE 802.3 / 400GPL | Lane objectives, NPO/CPO considerations, PMD/interoperability scope | Whether standards path makes CPO avoidable or enables alternatives | Commercial winner or supplier margin |
| OCP | System form factor, rack/cooling/service context and implementation ecosystem | Deployment constraints and operator requirements | Customer purchase or production proof |

## Record template

| Source ID | Patent/standard identifier | Date/status | Exact technical feature | Product relevance | Service/manufacturing implication | What remains unproven |
|---|---|---|---|---|---|---|
|  |  | Application/granted; draft/final |  | Exact/family/adjacent |  | Customer, yield, share, economics |

## Promotion rule

Patent and standards findings may refine the PIC, manufacturing or alternative
scorecards. They remain **architecture context** until joined to an exact
product, measured/qualified output and a commercial boundary.
