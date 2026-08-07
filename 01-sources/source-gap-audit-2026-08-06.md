# CPO Source-Gap Audit

**Owner:** Nur Alpys

**As of:** 2026-08-07 (refreshed after the PAP-028–PAP-032 review)

**Decision question:** Which architecture becomes commercially meaningful first, and which company captures the largest sustainable incremental profit pool?

## Executive conclusion

The current library is adequate for explaining why CPO may be needed and for framing a 102.4T switch comparison. The academic packet is now classified in the [academic evidence matrix](../03-components/academic-evidence-matrix.md), which explicitly separates measured demonstrations, modeled results and research targets. The library is still not adequate for declaring one company the durable technology or investment leader.

The full required-output status is now maintained in [CPO Decision-Output Completion Audit](../00-scope/decision-output-completion-audit.md). The immediate research priority remains evidence that converts architecture and company claims into measurable customer, manufacturing and economic outcomes.

The largest imbalance is that the research contains architecture reviews, standards, demonstrations, and company claims, but very little independent evidence on:

- customer qualification and named production deployments
- matched system power and link reliability
- final-package yield, optical attach yield, rework, test time, and scrap cost
- field failure rates, repair procedures, mean time to repair, and warranty allocation
- supplier content, pricing, gross margin, and cannibalisation
- accelerator-side optical I/O versus copper, active electrical cable, NPO, and alternative optical architectures
- what adoption and earnings are already reflected in public-company valuations

The correct interim answer is therefore layered rather than universal:

| Leadership question | Provisional answer | Evidence confidence | What prevents a final call |
|---|---|---:|---|
| Switch-side CPO platform and customer control | NVIDIA | Medium | Named adoption is for Spectrum-X and Vera Rubin platforms; CPO-specific deployed volume and matched performance remain unverified |
| Merchant switch CPO product maturity | Broadcom | Medium | Third-generation and production-volume claims are company supplied; named customer deployments, units, yield, and field data are absent |
| External-laser commercial visibility | Lumentum | Medium | Multi-hundred-million-dollar CPO order is disclosed, but customer, product content, margin, and cancellation protection are undisclosed |
| Broadest photonic component and manufacturing stack | Coherent | Medium | Strong breadth, 6-inch InP capacity, NVIDIA partnership, and a high-volume order are disclosed; customer and CPO revenue boundaries are not |
| Accelerator-side optical-I/O option among public companies | Marvell | Low to medium | Celestial AI, custom XPU, switching, and optical DSP assets are strategically coherent; production, customer, yield, and revenue evidence remain limited |
| Foundry and packaging control point | TSMC | Medium | COUPE and customer ecosystem are important, but product-level yield, pricing, and CPO-specific economics are not disclosed |
| Private optical-I/O technology candidates | Ayar Labs and Lightmatter | Low | Working silicon and sampling are visible; independent qualification, high-volume yield, field reliability, and customer revenue are not |
| Best public-equity opportunity | No decision | Low | No expectations, valuation, CPO earnings bridge, or downside model is populated |

No company currently earns the label “best technology overall.” Switch CPO, accelerator optical I/O, lasers, optical engines, packaging, and system platforms are different contests.

## Current evidence coverage

| Evidence block | Current coverage | Assessment |
|---|---|---|
| CPO architecture and packaging reviews | Mahajan; Tan; Lee; Buscaino | Good conceptual base |
| Switch-side 102.4T CPO | Broadcom and NVIDIA product material; architecture papers | Moderate, mostly company supplied |
| LPO and advanced pluggables | OIF requirements plus reviewed PAP-007, PAP-008, PAP-010 and PAP-011 academic papers | Moderate on electrical mechanisms; weak on matched production-system proof |
| NPO | IEEE 400GPL contribution and review material | Early standards framing only |
| External lasers | OIF management document; Lumentum, Coherent, NVIDIA claims | Moderate on architecture, weak on lifetime and field statistics |
| Optical packaging and manufacturability | Mahajan; IBM attach metrology; Cao assembly model; Corning and Furukawa detachable connectors | Moderate on mechanisms and laboratory results; weak on actual yield, cost and volume |
| Reliability and serviceability | Assembly simulation plus short connector-cycle and single-reflow screens | Weak on qualification, lifetime and field data |
| Network-level value | Maniotis and Kuchta simulation | Useful mechanism, no deployment validation |
| Customer adoption | Meta Spectrum-X partnership; vendor early-access and production claims | Weak for CPO-specific deployed units |
| Accelerator optical I/O | Marvell/Celestial, Ayar Labs, Lightmatter announcements | Major gap |
| Supplier economics | Lumentum order; Coherent order/capacity; Marvell acquisition filing | Early anchors only |
| Consensus, valuation, and earnings sensitivity | None | Critical gap |

## Priority-zero evidence still missing

These sources or data would most change the architecture and company ranking.

### 0. Economic input gate: completed first-pass company dossiers, still no valid forecast inputs

The Broadcom/NVIDIA and Coherent/Lumentum dossiers now establish the correct product and evidence boundaries. They also confirm that a numerical CPO revenue, gross-profit or free-cash-flow forecast is not supportable from the current public set: the linked inputs for system volume, attributable content, supplier share, realised product margin, yield/warranty, cannibalisation and capacity capital expenditure are absent or non-comparable.[CLM-073][CLM-074][CLM-077][CLM-079][CLM-083][CLM-084]

The governing model framework is [Optical-Engine Profit-Pool Input Gates](../08-model/optical-engine-profit-pool-input-gates.md). The next evidence order is: customer-side deployment/SKU confirmation; content map and supplier attribution; final-engine yield/service data; contract economics; then CPO-specific financial disclosure. Do not populate adoption probabilities or company valuation sensitivities before the architecture, product, manufacturing, commercial and financial gates are explicitly assessed.

### 1. Matched CPO versus LPO versus NPO system evidence

Required boundary:

```text
same host ASIC and lane rate
same aggregate bandwidth and optical attach rate
same reach, fibre plant, BER, FEC, and workload
ASIC SerDes + optics + lasers + control + conversion + cooling
measured inlet power and thermal conditions
link-flap and error statistics
```

No reviewed source meets this boundary. Until one does, vendor power multiples must remain company claims.

### 2. LPO: completed paper review, unresolved system proof

PAP-007, PAP-008, PAP-010 and PAP-011 have been reviewed on a matched evidence boundary:

1. Elaine Chou et al., *100G and 200G per Lane Linear Drive Optics for Data Center Applications*, OFC 2024, W4H.3, DOI 10.1364/OFC.2024.W4H.3 — 100G switch measurements, 200G simulation.
2. Jianying Zhou et al., *Performance Limitations and Optimizations of Linear Driver Optics for 200G/Lane and beyond*, OFC 2025, M2H.1, DOI 10.1364/OFC.2025.M2H.1 — 200G VPI model.
3. E. M. Kimber and E. Frlan, *200G LPO: Design Challenges and Latest Test Data*, OFC 2026, M2B.1, DOI 10.1364/OFC.2026.M2B.1 — 200G design and simulation synthesis.
4. Jianying Zhou et al., *400G/lane for Linear-drive Optics Applications*, OFC 2026, Th1C.3, DOI 10.1364/OFC.2026.Th1C.3 — 160/180 GBd component measurement and 212.5 GBd model.

They establish a conditional technical boundary, not how long advanced pluggables can defer NPO/CPO commercially. Still required: matched 200G multi-vendor systems at stated loss/return-loss/FEC/reach/temperature boundaries, 212.5 GBd measured links, module and chassis power, field reliability, qualification, service and cost data.

### 3. Packaging yield, rework, and reliability evidence

PAP-015 through PAP-018 are now reviewed and establish attach-metrology, mechanical-model and detachable-connector mechanisms. They do not supply production yield or qualification. Obtain the following additional evidence through university access where needed:

1. Nicholas Psaila et al., *Detachable Optical Chiplet Connector for Co-Packaged Photonics*, JLT 41, 6315-6323 (2023). This directly addresses yield compounding, known-good optical modules, rework, and detachable fibres.
2. Xin Li et al., *1.6 Tbps FOWLP-Based Silicon Photonic Engine for Co-Packaged Optics*, JLT 43, 1979-1986 (2025). This tests a volume-manufacturable fan-out packaging route.
3. Satoshi Suda et al., *High-Power Stability and Reliability of Polymer Optical Waveguide for Co-Packaged Optics*, JLT 43, 4903-4912 (2025), DOI 10.1364/JLT.43.004903.
4. *Thermal and Electrical Study of Glass Interposers in Co-Packaged Electronic-Photonic Systems*, IEEE TCPMT 15, 1625-1635 (2025), DOI 10.1109/TCPMT.2025.3533388.
5. Peter O'Brien, *Photonic and Electronic Co-Packaging Technologies - From Research to Pilot Manufacturing*, OFC 2025, W4A.1, DOI 10.1364/OFC.2025.W4A.1. Obtain the presentation video if the proceedings contain only an abstract.

The first four records are now retained locally as `PAP-028`–`PAP-031`: Psaila's abstract HTML, Li's abstract HTML, Suda's open-access abstract HTML, and Gupta's author-hosted PDF. O'Brien's OFC 2025 pilot-manufacturing abstract is now retained as `PAP-032`; the full presentation/video remains inaccessible. These records add useful mechanism and manufacturing questions, but do not clear production package yield. Primary research with packaging engineers, OSATs, fibre-attach suppliers, and system manufacturers will still be necessary. See the [packaging benchmark](../03-components/packaging-reliability-benchmark.md), [academic evidence matrix](../03-components/academic-evidence-matrix.md), and [source viewing guide](source-viewing-guide.md).

### 4. CPO-specific customer proof

Required evidence for NVIDIA and Broadcom:

- named customer and exact switch or optical-engine SKU
- qualification completion date
- systems or ports deployed, not merely sampled
- repeat order or production schedule
- workload and network position
- measured power and link availability
- replacement procedure and field failure rate

Meta confirms adoption of NVIDIA Spectrum-X across its infrastructure, but the reviewed customer statement does not isolate Spectrum-X Photonics or quantify CPO deployment. CoreWeave now provides the strongest customer-side named deployment record for NVIDIA's 102.4T SN6600-LD/Vera Rubin boundary. Broadcom's TH6 announcement adds HPE, Celestica, Micas and Nexthop partner-route statements, but those quotations do not provide accepted SKU, units, deployment date or repeat shipments (`CLM-246`–`CLM-249`). NVIDIA and Broadcom production statements therefore still need customer-side unit and qualification confirmation.

### 5. Accelerator-side optical-I/O evidence

The research must compare Marvell/Celestial AI, Ayar Labs, Lightmatter, TSMC COUPE, NVIDIA internal photonics, and credible copper/AEC alternatives on a shared boundary:

- shoreline bandwidth density
- energy per delivered bit including SerDes and laser
- latency
- topology and protocol
- package area and HBM interaction
- thermal coupling to the XPU
- optical-engine and package yield
- fibre escape and connector count
- serviceability
- customer qualification and production date

Current public evidence is too heterogeneous to rank their measured technology.

## Company evidence required before a durable leadership call

| Company | Strongest current evidence | Highest-priority missing evidence |
|---|---|---|
| NVIDIA | Spectrum-X and Quantum-X CPO products, production announcement, named platform adopters, TSMC/SPIL/Foxconn ecosystem | Customer-confirmed CPO units, matched performance, package yield, field failure data, pricing and supplier content |
| Broadcom | Third-generation 102.4T Davisson CPO, production-volume claim, merchant switching position | Named production customers, unit volume, independently measured power, link-flap study methodology, engine yield and repair economics |
| Lumentum | Incremental multi-hundred-million-dollar CPO order for first-half 2027 and high-power laser roadmap | Customer identity, product and quantity, firm versus cancellable backlog, gross margin, capacity and qualification milestones |
| Coherent | NVIDIA partnership, vertically integrated component stack, 6-inch InP production, high-volume multi-year CPO order | Customer identity, content per system, order timing and margin, independent device comparison, yield and qualification data |
| Marvell | Celestial AI acquisition, custom XPU and switching portfolio, NVIDIA strategic investment, NPO/CPO booking commentary | Photonic Fabric production customer, revenue milestones, measured link data, packaging partner, yield, and acquisition return bridge |
| TSMC | COUPE integration platform and central foundry/advanced-packaging position | Qualification status by customer product, yield, capacity, pricing, process ownership, and revenue materiality |
| Ayar Labs | 8 Tb/s UCIe optical chiplet and thermal/BER company testing | Independent test report, named production customer, package yield, volume capacity, economics and deployment date |
| Lightmatter | Passage roadmap, 3D integration, manufacturing partnerships, sampling and rack demonstrations | Named production customer, independent measured comparison, yield, qualification, field data, and unit economics |
| Fabrinet | NVIDIA photonics ecosystem membership, end-to-end optical packaging capability, current DCI/HPC revenue and disclosed yield/warranty risk mechanics (`FIL-007`, `FIL-008`) | CPO-specific programme, content, customer, revenue, margins, capital intensity allocation, qualified yield and warranty exposure |
| Cisco/Acacia, Intel, Ranovus | Relevant silicon-photonics assets and demonstrations | Current product status, strategic commitment, customer proof, and commercial scale |

## Investment analysis still required

Technology leadership alone cannot answer the equity question. For each public company, add:

1. CPO-addressable content per system and likely supplier share
2. Unit denominator by deployment domain
3. ASP erosion and mix shift
4. Gross margin after yield loss, warranty, and incremental depreciation
5. Cannibalisation of pluggable DSPs, transceivers, or existing switches
6. Research expense and capital expenditure
7. Customer concentration and pricing power
8. Revenue recognition and backlog quality
9. Consensus revenue, margin, and valuation assumptions
10. Bear-case value if CPO is delayed or the architecture changes

The next filings set should include Broadcom, NVIDIA, Marvell, Lumentum, Coherent, TSMC, and Fabrinet. Fabrinet's FY2025 10-K and Q3 FY2026 10-Q are now retained as `FIL-007` and `FIL-008`; use them for manufacturing-route denominators and risk gates, not as CPO revenue evidence. Use SEC or company filings rather than third-party financial summaries.

## Recommended research order

1. Obtain customer-side production/SKU confirmation and a component/content map for NVIDIA Spectrum-X Photonics and Broadcom TH6-Davisson.
2. Obtain product-level yield, test, field-service and warranty evidence for the external optical-engine candidates.
3. Obtain contract/order conversion, supply share, ASP and CPO-specific margin/capex evidence for Coherent and Lumentum.
4. Obtain matched 200G LPO/NPO/CPO system evidence and seek 400G-lane measured-link results.
5. Obtain O'Brien's OFC 2025 pilot-manufacturing presentation if the proceedings or university access provide it, and seek production-yield evidence from primary sources.
6. Build accelerator optical-I/O dossiers for Marvell/Celestial AI, Ayar Labs, Lightmatter, TSMC, and NVIDIA.
7. Conduct primary research with system operators, OSATs, fibre-attach suppliers, and field-service engineers.
8. Only then populate operational and investment scores and the 2026-2032 adoption probabilities.

## Public sources added in this audit

- IEEE 400GPL, *How NPO May Fit in IEEE 400GPL*.
- OIF, *Management of External Light Sources and Co-Packaged Optical Engines*.
- Microsoft Research, *MOSAIC: Breaking the Optics versus Copper Trade-off with a Wide-and-Slow Architecture and MicroLEDs*.
- Coherent, *Technology Innovation Briefing*, OFC 2026.
- NVIDIA, *NVIDIA Kicks Off the Next Generation of AI With Rubin*.
- Fabrinet, FY2025 Form 10-K and Q3 FY2026 Form 10-Q (`FIL-007`, `FIL-008`).
- Celestica, Q1 2026 Form 10-Q (`FIL-009`), retaining HPS/CCS scale, capex and concentration boundaries separately from the CPO programme announcement.
- TSMC, Q2 2026 financial results (`FIL-010`), retaining consolidated earnings scale separately from COUPE/CPO attribution.
- TSMC, February 2026 board resolution (`FIL-011`), retaining advanced-packaging capex context separately from COUPE/CPO allocation.

The TSMC 2025 symposium paper, OCP short-reach photonics white paper, and Broadcom OFC 2026 release remain URL-indexed or retained in the product-materials folder. The PAP-028–PAP-032 packaging packet is now retained locally with its access limitations recorded; it should not be treated as production-yield evidence.
