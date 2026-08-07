# CPO Company Leadership Scorecard

**Status:** Framework with provisional evidence-adjusted leadership view
**Last updated:** 2026-08-07

## Purpose

Leadership must be assessed separately by architecture, deployment domain, value-chain layer, and economic outcome. Do not produce one company ranking until those dimensions are specified.

## Required ranking views

1. Technical leader
2. Qualification leader
3. Volume leader
4. Platform leader
5. Profit-pool leader
6. Best public-equity opportunity, if any

## Operational-leadership score

Score each dimension from 0 to 5 using cited evidence.

| Dimension | Weight | Question |
|---|---:|---|
| Customer and qualification evidence | 20% | Are independent customers qualified and placing repeat production orders? |
| Manufacturing readiness | 20% | Are yield, fibre attach, test, capacity, and rework ready for scale? |
| Verified product performance | 15% | Does the product meet the defined system requirements under a clear boundary? |
| Platform and architecture control | 15% | Does the company control interfaces, system design, or the purchasing decision? |
| Reliability and serviceability | 10% | Is there evidence for lifetime, failure isolation, repair, and warranty economics? |
| Ecosystem and supply resilience | 10% | Are critical suppliers, capacity, and alternatives qualified? |
| Standards and interoperability | 10% | Can the implementation support the level of interoperability customers require? |

Apply an evidence-quality multiplier:

| Evidence quality | Multiplier |
|---|---:|
| Independent production and customer evidence | 1.00 |
| Multiple primary sources with partial customer evidence | 0.85 |
| Company documentation only | 0.65 |
| Announcement or demonstration only | 0.40 |
| Unverified secondary commentary | 0.20 |

## Investment-attractiveness score

Keep this separate from operational leadership.

| Dimension | Weight | Question |
|---|---:|---|
| Probability-weighted incremental gross profit | 30% | How much sustainable gross profit is created after cannibalisation and execution costs? |
| Earnings materiality | 20% | Is the opportunity material relative to the existing company? |
| Expectations and valuation gap | 20% | How different is the research view from evidenced market expectations? |
| Catalysts and timing | 15% | Which observable events could close the gap, and when? |
| Downside and execution risk | 15% | What happens if adoption is late, narrow, lower margin, or won by another supplier? |

## Company row template

| Field | Entry |
|---|---|
| Company | |
| Architecture | |
| Deployment domain | |
| Value-chain layer | |
| Product and status | |
| Evidence IDs | |
| Customer evidence | |
| Manufacturing evidence | |
| Main differentiation | |
| Critical dependency | |
| Potential cannibalisation | |
| Incremental content per system | |
| Gross-margin implication | |
| Research and capital requirements | |
| Warranty and inventory exposure | |
| Consensus expectation | |
| Variant view | |
| Next catalyst | |
| Falsification condition | |
| Operational score | |
| Evidence multiplier | |
| Adjusted operational score | |
| Investment-attractiveness score | |

## Initial company universe

Begin with the existing company set, but do not assume every company belongs in every architecture or layer. Add a company only when its role can be mapped to a product, interface, customer route, and potential economic content.

## Provisional leadership view as of 2026-08-07

This is a triage result, not the completed weighted scorecard. Scores remain unpopulated because several decisive dimensions lack comparable evidence.

| Leadership layer | Provisional leader or set | Evidence-adjusted interpretation |
|---|---|---|
| Switch-side CPO platform control | NVIDIA | Strongest full-stack system route and named early ecosystem adopters; CPO-specific customer volume remains unverified. See [platform dossier](broadcom-nvidia-switch-cpo-platform-dossier.md). |
| Merchant switch CPO product definition | Broadcom | Most specific disclosed 102.4T CPO architecture. Broadcom now separately says the Tomahawk 6 family is shipping in production volume, but the CPO configuration, units and optical-engine content remain unisolated; the earlier TH6 CPO release also contains early-access wording. Celestica's unnamed hyperscaler CPO-switch program with a planned 2027 ramp strengthens the route-to-production evidence but does not identify units or a CPO-specific TH6 SKU. See [platform dossier](broadcom-nvidia-switch-cpo-platform-dossier.md) and `CMP-031`. |
| External-laser commercial visibility | Lumentum | Clearest disclosed CPO order value and delivery window. The NVIDIA agreement and Greensboro announcement add a customer-linked 6-inch InP capacity route with a mid-2028 ramp, but customer, margin, product allocation, qualified output and order conversion remain undisclosed (`CMP-033`). |
| Photonic component breadth and manufacturing | Coherent | Broad SiPh, InP, VCSEL, detector, passive, fibre-attach, module, and test stack; the NVIDIA agreement adds a multibillion-dollar purchase commitment, capacity rights and $2B investment, but product allocation, conversion and margin remain undisclosed |
| Accelerator optical-I/O public-company option | Marvell | Celestial AI plus custom XPU, switching, DSP, and NVIDIA relationship create the strongest public-company strategic bundle; production proof remains weak |
| Advanced photonics manufacturing platform | TSMC | Central foundry and advanced-packaging control point with COUPE; CPO-specific economics and customer qualification are undisclosed |
| CPO system design/manufacturing route | Celestica | Awarded unnamed hyperscaler CPO-switch design/manufacturing program with planned 2027 ramp; exact system, optical scope, units, yield and margin remain undisclosed. See [Celestica dossier](celestica-cpo-manufacturing-route-dossier.md). |
| Advanced optical packaging / outsourced manufacturing route | Fabrinet | FY2025 filing documents end-to-end optical packaging, NPI-to-Thailand transfer and qualification infrastructure, but no named CPO programme, content allocation, yield or margin. See [Fabrinet dossier](fabrinet-manufacturing-route-dossier.md). |
| Accelerator optical-I/O PIC route | Intel | OCI chiplet prototype co-packaged with a CPU plus prior high-volume PIC/laser shipments in pluggable transceivers; OCI production, qualification and economics remain unproven (`CMP-035`, `CLM-304`–`CLM-305`). |
| Alternative monolithic optical-engine route | Ranovus / Jabil | ODIN EPIC integrates the major analog optical-engine functions and has a planned Jabil high-volume manufacturing route; no shipped volume, yield, customer or margin evidence (`CMP-036`, `CLM-306`). |
| System-level LPO/CPO comparator | Cisco | Cisco reports a 51.2T/64×800G linear-pluggable demonstration, multi-source CPO supply-chain strategy and module/platform qualification process; no controlled CPO comparison or production CPO evidence (`CMP-037`, `CLM-307`–`CLM-308`). |
| Private optical-I/O technology | No leader established | Ayar Labs and Lightmatter have differentiated working silicon and packaging approaches but no comparable independent production evidence |
| Best public-equity opportunity | No decision | Consensus, valuation, earnings materiality, and downside work have not been completed |

## Control-point view for the scale-out optical-engine profit pool

The current evidence supports a layered control map rather than a single “winner.” TSMC’s COUPE evidence is now stronger than a generic foundry roadmap: it reports 200G transmission with several customers in 2025, greater than 99% 3D-stacking yield on engineering samples, and a COUPE-on-substrate CPO production milestone beginning in 2026. Those facts make TSMC the clearest public **process/stacking control point**, but they still do not establish complete-engine ASP, supplier share or final-engine yield.[CLM-210][CLM-213][CLM-214][CLM-215][CLM-216]

| Control point | Current evidence-adjusted leader | What the evidence actually supports | Missing gate before profit leadership |
|---|---|---|---|
| Switch platform and purchasing decision | Broadcom / NVIDIA, domain-dependent | Broadcom has the most explicit 102.4T merchant CPO definition; NVIDIA has the strongest integrated platform/customer route | Customer-confirmed CPO units, platform margin and supplier-content map |
| COUPE/3D photonics stacking and package process | TSMC | Customer-linked 200G result, engineering-sample stacking yield and dated CPO-on-substrate production milestone | Actual 2026 output, final-engine yield, package responsibility, ASP and margin |
| Complete external optical-engine breadth | Coherent | Public demonstrations span SiPh, InP, VCSEL, lasers, attach and packaging | Qualified production engine, yield, content ownership and realised margin |
| External laser / ELSFP layer | Lumentum | Clearest disclosed ELSFP boundary, high-power laser evidence and near-term CPO order signal | Order conversion, laser share of the engine, qualified output, warranty and price protection |
| Qualified high-volume 200G/lane engine | No leader established | Public records now show multiple routes and milestones, but no matched customer-qualified final-engine lot | End-to-end qualification, repeat shipments and field/service economics |
| Sustainable incremental profit pool | No leader established | Technical and process control are visible, but supplier content, ASP, margin, cannibalisation and capex remain blocked | Full five-input economic bundle in the profit-pool gates |

### Why NVIDIA does not automatically win every category

NVIDIA controls the accelerator platform, network architecture, software, and an important customer route, but it relies on a broad photonics and manufacturing ecosystem. Its own technical architecture record now provides a detailed reference denominator—32 Spectrum-X engines, eight-laser ELS modules and detachable optical connectors—while still leaving partner allocation, final yield and product economics undisclosed [CLM-235–CLM-238]. Supplier partners may capture scarce-component value, while NVIDIA's CPO earnings may be immaterial relative to its accelerator economics.

### Why Broadcom does not automatically win every category

Broadcom's third-generation CPO and merchant-switch position are strong technical and product-maturity signals. Public evidence still does not establish named production deployments, comparable field reliability, final-package yield, or incremental CPO gross profit.

## Evidence-matched dossiers

The cross-company evidence boundary is summarized in the [company evidence-gap matrix](company-evidence-gap-matrix.md). It is a diligence control, not a substitute for a weighted score.

- [Broadcom and NVIDIA: Switch-Side CPO Platform Dossier](broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum: External Optical-Engine Supplier Dossier](coherent-lumentum-external-optical-engine-dossier.md)
- [Optical-Engine Profit-Pool Input Gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [Total-cost-per-delivered-bit gate](../08-model/tco-per-delivered-bit-gate.md)
- [CPO customer-proof register](../08-model/customer-proof-register.md)
- [Critical-path milestone tracker](../08-model/critical-path-milestone-tracker.md)
- [CPO Earnings-Materiality Screen](../08-model/cpo-earnings-materiality-screen.md)
- [Expectations and variant-perception tracker](../08-model/expectations-and-variant-perception-tracker.md)
- [NVIDIA CPO reference-content bridge](../08-model/nvidia-cpo-reference-content-bridge.md)
- [Marvell / Celestial AI: Accelerator Optical-I/O Dossier](marvell-celestial-accelerator-optical-io-dossier.md)

### Why Lumentum and Coherent matter

External lasers and InP manufacturing may become a scarce, architecture-agnostic profit pool across switch CPO and accelerator optical I/O. Both Lumentum and Coherent now have direct NVIDIA capacity/customer-route commitments, so the differentiator is no longer simply “who has a hyperscaler relationship.” Lumentum has the clearest external-laser order and planned 6-inch InP capacity milestone; Coherent has the broader publicly disclosed multi-technology engine stack. Neither disclosure identifies product allocation, qualified output, supplier share, ASP, cancellation protection or realised gross profit.

The content-attribution map now makes the critical negative explicit: NVIDIA's executed agreements with Coherent and Lumentum are nonexclusive and product-unallocated. They cannot be assigned to CoreWeave's Spectrum-X deployment, Lambda's Quantum-X deployment, Broadcom TH6, or any other named CPO system without a supplier-linked SKU and shipment record. See [CPO content-attribution map](../08-model/cpo-content-attribution-map.md) and `CLM-197`–`CLM-198`.

The input-gate framework now makes the scorecard boundary operational: no company should receive a numeric investment-attractiveness score until system volume, attributable content, supplier share, realised product margin, cannibalisation and the relevant cost/capital terms are traceably evidenced. Consolidated margin, a product demonstration, capacity expansion or an order headline is not a substitute.

The first revenue-scale screen shows why platform leadership and investable earnings sensitivity must remain separate: a given CPO revenue figure is much less material to Broadcom and NVIDIA's reported quarterly scale than to Coherent's or Lumentum's. It is a denominator test only, not evidence of CPO revenue, profit or valuation impact. See [CPO Earnings-Materiality Screen](../08-model/cpo-earnings-materiality-screen.md).

### Why Marvell is a different thesis

Marvell is not currently the best-evidenced switch-CPO product leader. Its potential leadership case is accelerator-side optical I/O and custom connectivity after acquiring Celestial AI. That thesis requires customer production, revenue milestones, and a return-on-acquisition bridge.

## Ranking rules

- Never award volume leadership based on announcements, samples, or a single demonstration.
- Never use market share without a defined product category, period, and source.
- Penalise evidence that comes only from the company being scored.
- Record both opportunity and cannibalisation.
- Show raw and evidence-adjusted scores.
- Preserve prior rankings and explain material changes.
- `No leader established` is valid when evidence is insufficient.
