# CPO critical-path milestone tracker

**Owner:** Nur Alpys  
**Status:** Evidence-calibrated tracker; not a forecast  
**As of:** 2026-08-07

## How to read this tracker

An observed milestone records what a retained source says happened. A planned milestone records a company target or roadmap. A required next milestone is a diligence condition, not a forecast. Statuses are deliberately separate from adoption probabilities.

## Observed and disclosed milestones

| ID | Architecture / domain | Company or customer | Milestone | Date | State | Evidence | Gate affected | Interpretation |
|---|---|---|---|---|---|---|---|---|
| MS-001 | Switch CPO, 100G/lane | Broadcom / Micas / Delta | TH5-Bailly described as a volume-production CPO baseline, with partner production milestones | 2025-05-15 | Observed company/partner claim | `PRI-028`; `CLM-199`–`CLM-200` | Commercial; manufacturing | Establishes a historical 100G/lane baseline; does not transfer to 200G/lane TH6 economics |
| MS-002 | Switch CPO, 200G/lane | Broadcom | TH6-Davisson defined as 102.4T, sixteen 6.4T engines, 200G/link, field-replaceable ELSFP | 2025-10-08 | Observed product announcement | `CMP-018`; `CLM-076` | Product; architecture | Strong product-definition milestone; customer units and final-engine yield remain open |
| MS-003 | Switch CPO, 200G/lane | Broadcom | TH6 release simultaneously says “now shipping” and sampling to early-access customers | 2025-10-08 | Observed disclosure conflict | `CMP-018`; `CLM-077` | Commercial proof | Conservative state is early-access sampling until customer-side repeat volume is shown |
| MS-004 | Switch CPO, 200G/lane | CoreWeave / NVIDIA | CoreWeave identifies early Photonics CPO adoption and a 102.4T SN6600-LD boundary | 2026 | Observed customer claim | `CMP-021`; `CLM-220`–`CLM-221` | Commercial; customer proof | Strongest named switch-side deployment record, but no unit denominator or BOM |
| MS-005 | Switch CPO, 200G/lane | CoreWeave / NVIDIA | CoreWeave corroborates 64 × 1.6T ports, 200G SerDes, 2U liquid-cooled SN6600-LD in Vera Rubin infrastructure | 2026 | Observed customer claim | `CMP-022`; `CLM-222`–`CLM-223` | Product; service | Adds system boundary; does not identify engine supplier or repeat volume |
| MS-006 | Inter-rack scale-up CPO | Lambda / NVIDIA | Lambda says a production-scale GB300 NVL72 cluster with 10,000+ GPUs uses Quantum-X Photonics CPO | 2026 | Observed customer technology claim | `CMP-023`; `CLM-224`–`CLM-225` | Commercial; domain separation | Production-scale evidence for Quantum-X inter-rack/scale-up domain, not switch-side Spectrum-X |
| MS-007 | Switch and inter-rack CPO roadmap | Lambda / NVIDIA | Lambda says future clusters are preparing to integrate Quantum-X and Spectrum-X Photonics | 2025-11-21 | Observed roadmap/preparation claim | `CMP-024`; `CLM-226`–`CLM-227` | Product; commercial | Spectrum-X remains roadmap/preparation evidence in this customer record |
| MS-008 | Switch CPO, 200G/lane | NVIDIA | NVIDIA platform page says Spectrum-X reaches full production and names first adopters and technology partners | 2026 | Observed vendor platform claim | `CMP-025`; `CLM-228`–`CLM-229` | Commercial; supplier route | Ecosystem milestone; not a unit, BOM or yield disclosure |
| MS-009 | Packaging / engine manufacturing | TSMC | COUPE-on-substrate CPO production milestone begins in 2026; engineering-sample 3D stacking yield exceeds 99% | 2026 target | Planned/company milestone | `PRI-029`–`PRI-031`; `CLM-213`–`CLM-216` | Manufacturing | Process checkpoint; not final-engine output or customer acceptance |
| MS-010 | Scale-out/scale-up CPO/NPO engines | Coherent | Investor deck labels CPO/NPO engines as a new-revenue item in H2 2026 and estimates a $15B+ CPO SAM by 2030 | H2 2026 / 2030 estimate | Planned/market estimate | `PRS-003`; `CLM-250`–`CLM-251` | Commercial; market sizing | Management timing and SAM framing; not observed shipment, qualification, unit volume or revenue |
| MS-011 | Switch CPO, 200G/lane | Celestica / unnamed hyperscaler | Celestica reports an awarded design-and-manufacturing program for a CPO Ethernet switch using 1.6T switch silicon, co-packaged optical interconnects and liquid cooling; production ramp expected in 2027 | 2026 disclosure / 2027 planned ramp | Planned/company program claim | `CMP-028`; `CLM-255`–`CLM-256` | Customer route; commercial; manufacturing | Stronger than a generic partner quote, but still lacks SKU, units, qualification, optical BOM, supplier share and realized revenue |

## Required next milestones

| ID | Architecture / domain | Required observation | Why it changes the decision | Current status |
|---|---|---|---|---|
| MS-N01 | Switch CPO, 200G/lane | Customer confirms exact TH6-Davisson or Spectrum-X Photonics SKU, accepted units/ports and deployment date | Converts a named product into a commercial-proof numerator | Open; customer-proof register |
| MS-N02 | Switch CPO, 200G/lane | Repeat order, expansion or sustained production record from one major customer or two independent customers | Clears the defined commercial-proof threshold | Open |
| MS-N03 | Optical engine | Product BOM identifies PIC/EIC/COUPE, laser/ELS, fibre attach, package and test responsibility | Prevents double counting and identifies profit-pool capture | Open |
| MS-N04 | Optical engine | Lot-level die-to-good-engine yield, attach cycle time, rework and test escape data | Determines whether technical feasibility becomes qualified cost | Open |
| MS-N05 | Optical engine | Qualification and field-service record: temperature/life, failure rate, replacement procedure and warranty allocation | Tests serviceability and support-cost leakage | Open |
| MS-N06 | LPO/CPO boundary | Matched 200G/lane and later 400G/lane system measurement at defined loss, reach, FEC, temperature and power | Determines whether CPO is technically necessary rather than merely marketed | Open |
| MS-N07 | Supplier economics | ASP, qualified share, second-source status, price-down and cancellation terms | Converts architecture content into supplier gross profit | Open |
| MS-N08 | TSMC COUPE route | 2026 milestone reconciled to named customer SKU, shipped units, final-engine yield and package responsibility | Separates process readiness from attributable revenue | Open |

## Change-log rule

Every future update should preserve:

```text
milestone_id
state_before -> state_after
observed_date or planned_date
source_id and claim_id
evidence boundary
what remains unproven
```

Do not convert a vendor roadmap date into an observed date. Do not convert a partner quotation into customer shipment. Do not convert an engineering-sample yield into final-engine yield.

## Linked controls

- [CPO adoption timeline](adoption-timeline.md)
- [CPO customer-proof register](customer-proof-register.md)
- [CPO evidence-gate register](evidence-gate-register.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
