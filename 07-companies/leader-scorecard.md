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

## Provisional leadership view as of 2026-08-06

This is a triage result, not the completed weighted scorecard. Scores remain unpopulated because several decisive dimensions lack comparable evidence.

| Leadership layer | Provisional leader or set | Evidence-adjusted interpretation |
|---|---|---|
| Switch-side CPO platform control | NVIDIA | Strongest full-stack system route and named early ecosystem adopters; CPO-specific customer volume remains unverified. See [platform dossier](broadcom-nvidia-switch-cpo-platform-dossier.md). |
| Merchant switch CPO product definition | Broadcom | Most specific disclosed 102.4T CPO architecture; its own release says both “now shipping” and early-access sampling, so broad CPO volume remains unproven. See [platform dossier](broadcom-nvidia-switch-cpo-platform-dossier.md). |
| External-laser commercial visibility | Lumentum | Clearest disclosed CPO order value and delivery window; the NVIDIA agreement adds a multibillion-dollar purchase commitment, capacity rights and a planned 6-inch InP fab ramp, but customer, margin, product allocation and conversion remain undisclosed |
| Photonic component breadth and manufacturing | Coherent | Broad SiPh, InP, VCSEL, detector, passive, fibre-attach, module, and test stack; the NVIDIA agreement adds a multibillion-dollar purchase commitment, capacity rights and $2B investment, but product allocation, conversion and margin remain undisclosed |
| Accelerator optical-I/O public-company option | Marvell | Celestial AI plus custom XPU, switching, DSP, and NVIDIA relationship create the strongest public-company strategic bundle; production proof remains weak |
| Advanced photonics manufacturing platform | TSMC | Central foundry and advanced-packaging control point with COUPE; CPO-specific economics and customer qualification are undisclosed |
| Private optical-I/O technology | No leader established | Ayar Labs and Lightmatter have differentiated working silicon and packaging approaches but no comparable independent production evidence |
| Best public-equity opportunity | No decision | Consensus, valuation, earnings materiality, and downside work have not been completed |

### Why NVIDIA does not automatically win every category

NVIDIA controls the accelerator platform, network architecture, software, and an important customer route, but it relies on a broad photonics and manufacturing ecosystem. Supplier partners may capture scarce-component value, while NVIDIA's CPO earnings may be immaterial relative to its accelerator economics.

### Why Broadcom does not automatically win every category

Broadcom's third-generation CPO and merchant-switch position are strong technical and product-maturity signals. Public evidence still does not establish named production deployments, comparable field reliability, final-package yield, or incremental CPO gross profit.

## Evidence-matched dossiers

The cross-company evidence boundary is summarized in the [company evidence-gap matrix](company-evidence-gap-matrix.md). It is a diligence control, not a substitute for a weighted score.

- [Broadcom and NVIDIA: Switch-Side CPO Platform Dossier](broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Coherent and Lumentum: External Optical-Engine Supplier Dossier](coherent-lumentum-external-optical-engine-dossier.md)
- [Optical-Engine Profit-Pool Input Gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [CPO Earnings-Materiality Screen](../08-model/cpo-earnings-materiality-screen.md)
- [Marvell / Celestial AI: Accelerator Optical-I/O Dossier](marvell-celestial-accelerator-optical-io-dossier.md)

### Why Lumentum and Coherent matter

External lasers and InP manufacturing may become a scarce, architecture-agnostic profit pool across switch CPO and accelerator optical I/O. Both Lumentum and Coherent now have direct NVIDIA capacity/customer-route commitments, so the differentiator is no longer simply “who has a hyperscaler relationship.” Lumentum has the clearest external-laser order and planned 6-inch InP capacity milestone; Coherent has the broader publicly disclosed multi-technology engine stack. Neither disclosure identifies product allocation, qualified output, supplier share, ASP, cancellation protection or realised gross profit.

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
