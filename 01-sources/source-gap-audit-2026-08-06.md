# CPO Source-Gap Audit

**Owner:** Nur Alpys

**As of:** 2026-08-06

**Decision question:** Which architecture becomes commercially meaningful first, and which company captures the largest sustainable incremental profit pool?

## Executive conclusion

The current library is adequate for explaining why CPO may be needed and for framing a 102.4T switch comparison. It is not yet adequate for declaring one company the durable technology or investment leader.

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
| LPO and advanced pluggables | OIF requirements; vendor demonstrations; OFC abstracts | Weak because the most decision-relevant OFC papers are not available in full |
| NPO | IEEE 400GPL contribution and review material | Early standards framing only |
| External lasers | OIF management document; Lumentum, Coherent, NVIDIA claims | Moderate on architecture, weak on lifetime and field statistics |
| Optical packaging and manufacturability | Mahajan; glass substrate; Coherent capacity deck | Moderate on approaches, weak on actual yield and cost |
| Reliability and serviceability | Review papers and vendor design descriptions | Weak on qualification and field data |
| Network-level value | Maniotis and Kuchta simulation | Useful mechanism, no deployment validation |
| Customer adoption | Meta Spectrum-X partnership; vendor early-access and production claims | Weak for CPO-specific deployed units |
| Accelerator optical I/O | Marvell/Celestial, Ayar Labs, Lightmatter announcements | Major gap |
| Supplier economics | Lumentum order; Coherent order/capacity; Marvell acquisition filing | Early anchors only |
| Consensus, valuation, and earnings sensitivity | None | Critical gap |

## Priority-zero evidence still missing

These sources or data would most change the architecture and company ranking.

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

### 2. Complete LPO papers

Download through university access:

1. Elaine Chou et al., *100G and 200G per Lane Linear Drive Optics for Data Center Applications*, OFC 2024, W4H.3, DOI 10.1364/OFC.2024.W4H.3.
2. Jianying Zhou et al., *Performance Limitations and Optimizations of Linear Driver Optics for 200G/Lane and beyond*, OFC 2025, M2H.1, DOI 10.1364/OFC.2025.M2H.1.
3. E. M. Kimber and E. Frlan, *200G LPO: Design Challenges and Latest Test Data*, OFC 2026, M2B.1, DOI 10.1364/OFC.2026.M2B.1.
4. Jianying Zhou et al., *400G/lane for Linear-drive Optics Applications*, OFC 2026, Th1C.3, DOI 10.1364/OFC.2026.Th1C.3.

These papers determine how long advanced pluggables can defer NPO or CPO.

### 3. Packaging yield, rework, and reliability

Download through university access where needed:

1. Nicholas Psaila et al., *Detachable Optical Chiplet Connector for Co-Packaged Photonics*, JLT 41, 6315-6323 (2023). This directly addresses yield compounding, known-good optical modules, rework, and detachable fibres.
2. Xin Li et al., *1.6 Tbps FOWLP-Based Silicon Photonic Engine for Co-Packaged Optics*, JLT 43, 1979-1986 (2025). This tests a volume-manufacturable fan-out packaging route.
3. Satoshi Suda et al., *High-Power Stability and Reliability of Polymer Optical Waveguide for Co-Packaged Optics*, JLT 43, 4903-4912 (2025), DOI 10.1364/JLT.43.004903.
4. *Thermal and Electrical Study of Glass Interposers in Co-Packaged Electronic-Photonic Systems*, IEEE TCPMT 15, 1625-1635 (2025), DOI 10.1109/TCPMT.2025.3533388.
5. Peter O'Brien, *Photonic and Electronic Co-Packaging Technologies - From Research to Pilot Manufacturing*, OFC 2025, W4A.1, DOI 10.1364/OFC.2025.W4A.1. Obtain the presentation video if the proceedings contain only an abstract.

Even these papers are unlikely to disclose production package yield. Primary research with packaging engineers, OSATs, fibre-attach suppliers, and system manufacturers will still be necessary.

### 4. CPO-specific customer proof

Required evidence for NVIDIA and Broadcom:

- named customer and exact switch or optical-engine SKU
- qualification completion date
- systems or ports deployed, not merely sampled
- repeat order or production schedule
- workload and network position
- measured power and link availability
- replacement procedure and field failure rate

Meta confirms adoption of NVIDIA Spectrum-X across its infrastructure, but the reviewed customer statement does not isolate Spectrum-X Photonics or quantify CPO deployment. NVIDIA and Broadcom production statements therefore need customer-side confirmation.

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
| Fabrinet | NVIDIA photonics ecosystem membership and high-volume optical manufacturing capability | CPO-specific programme, content, customer, revenue, margins, capital intensity, and warranty exposure |
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

The next filings set should include Broadcom, NVIDIA, Marvell, Lumentum, Coherent, TSMC, and Fabrinet. Use SEC or company filings rather than third-party financial summaries.

## Recommended research order

1. Obtain the four LPO papers and five packaging/reliability papers above.
2. Build one matched evidence table for NVIDIA Spectrum-X Photonics and Broadcom TH6-Davisson.
3. Build external-laser dossiers for Lumentum and Coherent, anchored to order, capacity, qualification, and margin evidence.
4. Build accelerator optical-I/O dossiers for Marvell/Celestial AI, Ayar Labs, Lightmatter, TSMC, and NVIDIA.
5. Conduct primary research with system operators, OSATs, fibre-attach suppliers, and field-service engineers.
6. Only then populate operational and investment scores and the 2026-2032 adoption probabilities.

## Public sources added in this audit

- IEEE 400GPL, *How NPO May Fit in IEEE 400GPL*.
- OIF, *Management of External Light Sources and Co-Packaged Optical Engines*.
- Microsoft Research, *MOSAIC: Breaking the Optics versus Copper Trade-off with a Wide-and-Slow Architecture and MicroLEDs*.
- Coherent, *Technology Innovation Briefing*, OFC 2026.
- NVIDIA, *NVIDIA Kicks Off the Next Generation of AI With Rubin*.

The TSMC 2025 symposium paper, OCP short-reach photonics white paper, Broadcom OFC 2026 release, and the two open-access JLT PDFs were readable online but rejected automated file download. They remain URL-indexed or in the university-download queue.
