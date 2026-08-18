# CPO critical-path milestone tracker

**Owner:** Nur Alpys  
**Status:** Evidence-calibrated tracker; not a forecast  
**As of:** 2026-08-12

## How to read this tracker

An observed milestone records what a retained source says happened. A planned milestone records a company target or roadmap. A required next milestone is a diligence condition, not a forecast. Statuses are deliberately separate from adoption probabilities.

## Observed and disclosed milestones

| ID | Architecture / domain | Company or customer | Milestone | Date | State | Evidence | Gate affected | Interpretation |
|---|---|---|---|---|---|---|---|---|
| MS-001 | Switch CPO, 100G/lane | Broadcom / Micas / Delta | TH5-Bailly described as a volume-production CPO baseline, with partner production milestones | 2025-05-15 | Observed company/partner claim | `PRI-028`; `CLM-199`–`CLM-200` | Commercial; manufacturing | Establishes a historical 100G/lane baseline; does not transfer to 200G/lane TH6 economics |
| MS-002 | Switch CPO, 200G/lane | Broadcom | TH6-Davisson defined as 102.4T, sixteen 6.4T engines, 200G/link, field-replaceable ELSFP | 2025-10-08 | Observed product announcement | `CMP-018`; `CLM-076` | Product; architecture | Strong product-definition milestone; customer units and final-engine yield remain open |
| MS-003 | Switch CPO, 200G/lane | Broadcom | TH6 release simultaneously says “now shipping” and sampling to early-access customers | 2025-10-08 | Observed disclosure conflict | `CMP-018`; `CLM-077` | Commercial proof | Conservative state is early-access sampling until customer-side repeat volume is shown |
| MS-003A | Switch family production versus CPO denominator | Broadcom | March 2026 release says Tomahawk 6 family is shipping in production volume, but does not isolate CPO configuration, units or optical-engine content | 2026-03-12 | Observed company claim with unresolved product mix | `CMP-031`; `CLM-284` | Commercial; content attribution | Upgrade switch-family maturity only; do not treat it as CPO-specific volume or profit proof |
| MS-004 | Switch CPO, 200G/lane | CoreWeave / NVIDIA | CoreWeave identifies early Photonics CPO adoption, but the associated named SN6600-LD deployment is not proven to be the CPO SKU | 2026 | Observed customer claim plus SKU reconciliation | `CMP-021`; `CMP-048`; `CLM-220`–`CLM-221`; `CLM-380`–`CLM-383` | Commercial; customer proof; attribution | CPO-adopter statement retained; named switch-side CPO unit numerator remains open |
| MS-005 | Switch-side Ethernet, pluggable 200G/lane boundary | CoreWeave / NVIDIA | CoreWeave corroborates 64 × 1.6T ports, 200G SerDes, 2U liquid-cooled SN6600-LD in Vera Rubin infrastructure; NVIDIA classifies SN6600-LD as pluggable RHS | 2026 | Observed customer claim plus hardware manual | `CMP-022`; `CMP-048`; `CLM-222`–`CLM-223`; `CLM-380` | Product; service; architecture | Strong pluggable-platform deployment evidence, not CPO evidence |
| MS-005A | Switch-side Ethernet, pluggable 200G/lane / operations | CoreWeave / NVIDIA | CoreWeave describes first-provider Vera Rubin NVL72 validation and a 100% liquid-cooled 102.4T Spectrum-X SN6600 scale-out fabric with 128 ports up to 800G, plus rack-level service controls; CMP-048 classifies SN6600-LD as pluggable RHS | 2026-06-17 | Observed customer/operator claim plus hardware manual | `CMP-046`; `CMP-048`; `CLM-370`–`CLM-372`; `CLM-380`–`CLM-382` | Customer proof; service; configuration | Strongens customer-operated pluggable deployment evidence; does not clear CPO attribution or units |
| MS-006 | Inter-rack scale-up CPO | Lambda / NVIDIA | Lambda says a production-scale GB300 NVL72 cluster with 10,000+ GPUs uses Quantum-X Photonics CPO | 2026 | Observed customer technology claim | `CMP-023`; `CLM-224`–`CLM-225` | Commercial; domain separation | Production-scale evidence for Quantum-X inter-rack/scale-up domain, not switch-side Spectrum-X |
| MS-007 | Switch and inter-rack CPO roadmap | Lambda / NVIDIA | Lambda says future clusters are preparing to integrate Quantum-X and Spectrum-X Photonics | 2025-11-21 | Observed roadmap/preparation claim | `CMP-024`; `CLM-226`–`CLM-227` | Product; commercial | Spectrum-X remains roadmap/preparation evidence in this customer record |
| MS-008 | Switch CPO, 200G/lane | NVIDIA | NVIDIA platform page says Spectrum-X reaches full production and names first adopters and technology partners | 2026 | Observed vendor platform claim | `CMP-025`; `CLM-228`–`CLM-229` | Commercial; supplier route | Ecosystem milestone; not a unit, BOM or yield disclosure |
| MS-009 | Packaging / engine manufacturing | TSMC | COUPE-on-substrate CPO production milestone begins in 2026; engineering-sample 3D stacking yield exceeds 99% | 2026 target | Planned/company milestone | `PRI-029`–`PRI-031`; `CLM-213`–`CLM-216` | Manufacturing | Process checkpoint; not final-engine output or customer acceptance |
| MS-010 | Scale-out/scale-up CPO/NPO engines | Coherent | Investor deck labels CPO/NPO engines as a new-revenue item in H2 2026 and estimates a $15B+ CPO SAM by 2030 | H2 2026 / 2030 estimate | Planned/market estimate | `PRS-003`; `CLM-250`–`CLM-251` | Commercial; market sizing | Management timing and SAM framing; not observed shipment, qualification, unit volume or revenue |
| MS-011 | Switch CPO, 200G/lane | Celestica / unnamed hyperscaler | Celestica reports an awarded design-and-manufacturing program for a CPO Ethernet switch using 1.6T switch silicon, co-packaged optical interconnects and liquid cooling; production ramp expected in 2027 | 2026 disclosure / 2027 planned ramp | Planned/company program claim | `CMP-028`; `CLM-255`–`CLM-256` | Customer route; commercial; manufacturing | Stronger than a generic partner quote, but still lacks SKU, units, qualification, optical BOM, supplier share and realized revenue |
| MS-013 | Switch CPO, 200G/lane | NVIDIA / CoreWeave / Lambda / OCI | NVIDIA states Spectrum-X Ethernet Photonics is a CPO-based switch with 200Gb/s SerDes and is now in production, naming first ecosystem partners/adopters | 2026-05-31 | Observed first-party production claim | `PRI-033`; `CLM-346`–`CLM-347` | Commercial; customer route | Advances timing evidence but does not provide units, repeat shipments, supplier allocation or matched performance economics |
| MS-014 | CPO technology breadth, 200G/400G | Coherent | Coherent announces 6.4T (32×200G) socketed SiPh/ELS, VCSEL CPO and 400G/lane InP modulator demonstrations | 2026-03-17 | Observed demonstration claim | `PRI-034`; `CLM-348` | Product; technology breadth | Confirms multiple routes; does not establish qualification or commercial conversion |
| MS-015 | Optical-engine component route, 200G/lane | Lumentum / NVIDIA | Lumentum describes live NVIDIA 1.6T modules using UHP laser or 200G EMLs and a path toward CPO industrialization | 2026-04-30 | Observed demonstration/roadmap claim | `PRI-035`; `CLM-349` | Product; supplier content | Maps component content in live modules, but not CPO units, engine ownership or margin |
| MS-016 | Optical engine, 400-Gbps on-board/pluggable boundary | Kang et al. | TGV-interposer optical-engine paper reports 51.8 GHz S21 bandwidth, TDECQ <1.6 dB and real-time 4 × 106 Gbps KP4-FEC operation; localized laser soldering is proposed for replacement | 2025-03-03 | Observed academic measurement; abstract-only record | `PAP-044`; `CLM-424`–`CLM-427` | 400G technical; serviceability | Strengthens the measured engine comparator and replacement design boundary, but is not a 400G/lane CPO production milestone |
| MS-017 | Manufacturing test infrastructure | Teradyne / ficonTEC | Production-oriented double-sided wafer-probe test cell announced for hybrid-bonded PIC/EIC silicon-photonics wafers | 2025-03-31 | Observed equipment-availability claim | `CMP-052`; `CLM-432`–`CLM-434` | Test; manufacturing | Establishes an equipment route for scalable electro-optical wafer test; customer installation, throughput, yield impact and economics remain open |
| MS-012 | RTLR/LPO, 112G-class electrical boundary | OIF multi-vendor implementation agreement | OIF-EEI-112G-RTLR defines interoperable retimed-transmitter/linear-receiver modules with hot plug, 200 mm host-trace capability, 11.9 dB host-loss allocation and explicit BER/FEC compliance points | 2025-10-01 | Observed standards publication | `STD-012`; `CLM-297`–`CLM-300` | Electrical; interoperability; serviceability | Establishes a concrete alternative boundary for the 200G-class comparison; does not establish shipment, power, yield, field reliability or cost |
| MS-018 | 1.6T switching route, architecture unspecified | Celestica / major hyperscaler | Celestica reports an earlier major hyperscaler 1.6T switching program with revenue expected to ramp in 2026; the disclosure does not call it CPO | 2024 disclosure / 2026 planned ramp | Historical planned program claim | `CMP-030`; `CLM-258` | Customer route; chronology | Useful predecessor/context, but must not be merged with the later CPO-specific program or counted as CPO revenue |
| MS-019 | Generic CPO optical-switch manufacturing ramp | Foxconn / unnamed cloud and AI customers | Foxconn forecasts Q3 2026 mass-production shipments and says full-year shipments may reach tens of thousands; CPO/1.6T products are being prepared with unnamed major customers | Q3 2026 planned / forecast | Company management outlook | `CMP-060`; `CLM-526`–`CLM-527` | Commercial timing; manufacturing | Pending verification against actual results. No exact product maker/SKU/customer/accepted units or supplier economics; do not assign to NVIDIA Spectrum-X or Broadcom TH6. |

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
| MS-P01 | POET Optical Interposer | Installed Malaysian optical-engine line capacity, 800G qualification/design-in claim and conditional EOI purchase-order framework reconciled to shipped units and output | Tests whether wafer-level integration converts into a qualified optical-engine supply route | Open; `CMP-042`–`CMP-044`; `CLM-360`–`CLM-366` |
| MS-P02 | POET/Lumilens EOI | Late-2026 engineering sample and 2027 production targets checked against named hyperscaler SKU, qualification and repeat orders | Converts conditional commercial intent into an observable adoption milestone | Open |

## Change-log rule

The [quarterly evidence-change register](../09-primary-research/quarterly-evidence-change-register-2026-08-12.md)
is the controlling record for state transitions and unchanged conclusions.

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
