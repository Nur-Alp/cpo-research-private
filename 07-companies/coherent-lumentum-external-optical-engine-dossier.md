# Coherent and Lumentum: External Optical-Engine Supplier Dossier

**Owner:** Nur Alpys
**Status:** Evidence-matched first-pass dossier; not an investment recommendation
**Scope:** Scale-out optical engines and external laser sources for switch-side CPO/NPO
**As of:** 2026-08-07

## Decision question

Which supplier has the stronger evidence that it can capture a durable external optical-engine profit pool as CPO moves from demonstrations toward 200G- and 400G-per-lane systems?

## Current answer

**INFERENCE:** Coherent has the broader demonstrated component and manufacturing stack. Its company materials describe silicon photonics, high-power InP lasers, VCSELs, advanced packaging and a 6.4T (32 x 200G) socketed CPO demonstration, while it reports volume production on a six-inch InP line and planned capacity expansion through 2027. The March 2026 NVIDIA agreement adds a multibillion-dollar purchase commitment, future capacity rights and a $2B investment, but does not identify product allocation or realised CPO revenue.[CMP-015][PRS-003][PRI-023][CLM-194]

**INFERENCE:** Lumentum has the clearer narrow product-and-commercial signal for an external laser source: a serviceable ELSFP product boundary, specified UHP/SHP laser demonstrations, and a previously disclosed incremental multi-hundred-million-dollar CPO order for delivery in the first half of calendar 2027. The March 2026 NVIDIA agreement and planned Greensboro 6-inch InP fab strengthen the capacity/customer-route case, but do not prove complete-engine content, yield or margin.[CMP-016][CMP-017][CMP-010][PRI-024][PRI-025][CLM-195][CLM-196]

Neither company has disclosed the information needed to call a sustainable CPO profit-pool leader: customer-confirmed CPO deployment, final optical-engine yield, automated fibre-attach and test cost, warranty/field-return data, CPO content per system, contract margin, or a CPO revenue line. The appropriate present status is **Coherent leads on breadth and reported capacity; Lumentum leads on external-laser commercial visibility; no overall supplier leader is established.**

## Comparable role map

| Dimension | Coherent | Lumentum | Decision relevance |
|---|---|---|---|
| Primary CPO role | Company presents complete technology choices: SiPh CPO with ELS, VCSEL CPO, and InP-on-silicon 400G modulation | High-power CW/UHP/SHP laser and ELSFP module supplier; also optical components, modules and OCS | Coherent may retain more engine content; Lumentum may sell a scarce serviceable light-source layer across multiple engines |
| Direct technical evidence | **COMPANY CLAIM:** OFC 2026 6.4T socketed SiPh CPO (32 x 200G), ELS and high-power InP laser; 400G/lane InP-modulator-array demonstration | **COMPANY CLAIM:** UHP product page lists 350 mW at 50 C, 235 mW at 70 C, above-20% PCE; OFC announcement lists SHP over 800 mW at 50 C and 16 simultaneous DWDM channels | Product numbers are not a matched complete-engine comparison and do not establish field reliability or production volume |
| Manufacturing and capacity | **COMPANY CLAIM:** six-inch InP line in volume production; expansion in Texas, Sweden and Switzerland; total InP production planned to double in 2026 and again in 2027; NVIDIA agreement adds future capacity rights | UHP product says InP platform and high manufacturing scalability; Greensboro 6-inch InP fab is planned to ramp mid-2028 with NVIDIA as a customer; NVIDIA agreement adds future laser-capacity rights | Coherent has earlier disclosed capacity; Lumentum has a dated future fab milestone; neither discloses CPO-engine yield/capacity or qualification output |
| Commercial signal | **COMPANY CLAIM:** very-high-volume multi-year CPO orders from an unnamed leading AI-data-centre customer; NVIDIA agreement adds a multibillion-dollar purchase commitment | **COMPANY CLAIM:** incremental multi-hundred-million-dollar CPO order for first-half 2027 delivery; NVIDIA agreement adds a multibillion-dollar purchase commitment | Neither disclosure identifies customer/product allocation, price, cancellation terms, margin or shipped CPO units |
| Financial scale | Q3 FY26 revenue $1.806B; GAAP gross margin 37.7%; non-GAAP gross margin 39.6% | Q3 FY26 revenue $808.4M; GAAP gross margin 44.2%; non-GAAP gross margin 47.9% | Consolidated margin cannot be assigned to CPO; Lumentum’s CPO would be more earnings-material if it converts, but the revenue/margin allocation is unknown |
| Customer concentration | Not established in the reviewed source set | Two customers represented 24% and 16% of FY26 nine-month revenue through March 28 | Lumentum’s concentration increases both demand visibility and customer-pricing/execution risk; CPO-customer identity is undisclosed |
| Serviceability | Socketed CPO is demonstrated, but CPO-engine replacement process is not disclosed | ELSFP moves lasers to a faceplate-replaceable source, but does not make a failed optical engine replaceable | OIF confirms that external light introduces host-control and fibre-distribution dependencies; it mitigates one failure domain, not PIC/fibre/package reliability. See [external-light boundary](../03-components/external-light-serviceability-boundary.md). |

## Product-boundary evidence

### Coherent

1. **COMPANY CLAIM:** Coherent’s OFC 2026 CPO demonstration includes a 6.4T socketed silicon-photonics CPO system with 32 x 200G lanes, paired with its external laser source and high-power InP CW lasers. It also showed a multimode VCSEL CPO and an InP modulator on silicon at 400G.[CMP-015]
2. **COMPANY CLAIM:** The company reports that its first six-inch InP line is in volume production, with stated total InP-output expansion in 2026 and 2027. This is meaningful capacity evidence for EMLs, CW lasers, photodiodes and PICs, but not proof of CPO-engine yield or allocation.[PRS-003]
3. **FACT:** Coherent reported Q3 FY26 revenue of $1.806B, GAAP gross margin of 37.7%, non-GAAP gross margin of 39.6%, and Q4 non-GAAP gross-margin guidance of 39-41%.[FIL-002]

### Lumentum

1. **COMPANY CLAIM:** Lumentum’s UHP product page specifies a 1311-nm laser at up to 350 mW at 50 C and 235 mW at 70 C, above 20% PCE, below 500 kHz linewidth and RIN below -147 dB/Hz. The company says it is used in ELSFP modules for serviceable SiPh CPO engines.[CMP-016]
2. **COMPANY CLAIM:** At OFC 2026, Lumentum reported an SHP laser above 1.0 W at 25 C and above 800 mW at 50 C, and a 16-channel DWDM demonstration from two ELSFP modules at approximately 24 dBm per fibre channel. This is a company demonstration, not a customer system or field-reliability result.[CMP-017]
3. **FACT:** Lumentum reported Q3 FY26 revenue of $808.4M, GAAP gross margin of 44.2% and non-GAAP gross margin of 47.9%. In its Q3 10-Q, two customers accounted for 24% and 16% of nine-month revenue through March 28, 2026.[FIL-003]
4. **COMPANY CLAIM:** Lumentum’s Q2 FY26 release disclosed an incremental multi-hundred-million-dollar CPO order to be delivered in the first half of calendar 2027. The order’s product, customer, unit, margin and cancellation conditions are not public.[CMP-010]

## Matched engine and profit bridge

The supplier disclosures are not yet apples-to-apples: Coherent's public unit is a 6.4T socketed CPO demonstration, while Lumentum's clearest unit is an ELSFP/laser layer. Use the [matched engine and profit bridge](../08-model/coherent-lumentum-matched-engine-profit-bridge.md) before assigning content, ASP or supplier share.

## Economic logic and unknowns

| Economic field | Coherent | Lumentum | Current research treatment |
|---|---|---|---|
| Content per CPO system | Unknown: vertically integrated CPO could include PIC, laser, detector, packaging and subassembly content | Unknown: ELSFP can be a higher-value light-source layer, but engine/power split is undisclosed | Do not infer content from a product demonstration or order value |
| Realised gross margin | Unknown CPO-specific margin; consolidated gross margin is not a proxy | Unknown CPO-specific margin; consolidated gross margin is not a proxy | Leave unmodeled until revenue/product mix or contract evidence is available |
| Cannibalisation | May displace some pluggable component/module demand but could also supply components to non-CPO architectures | ELS/CPO could displace laser/module content inside retimed pluggables while adding higher-power laser and module content | Model both gain and displaced legacy profit once system content is known |
| Capex and capacity | Reported six-inch InP expansion suggests substantial manufacturing commitment; CPO-specific capex undisclosed | Fab expansion and component capacity support demand; CPO-specific capex undisclosed | Use capacity as a supply-readiness gate, not as incremental CPO capital deployed |
| Warranty and inventory | Unknown CPO-engine terms, repair path and returns | ELSFP improves laser replacement access; engine/laser warranty split and inventory exposure unknown | No TCO or gross-profit conclusion until failure and service data exist |

## Evidence-adjusted readiness view

Scores are intentionally not populated. The scorecard requires a comparable 0-5 record across all four core companies, and the decisive evidence is absent for both suppliers. Qualitative status is still useful:

| Gate | Coherent | Lumentum | What would change the assessment |
|---|---|---|---|
| Product and technical breadth | Medium | Medium | Independent third-party or customer validation at a specified link/power/temperature boundary |
| Manufacturing readiness | Medium | Low to medium | Final-engine yield, fibre attach/test cycle time, capacity allocation and qualification pass-rate |
| Commercial proof | Low to medium | Low to medium | Named customer, SKU, repeat order/shipments and timing, with a defined CPO product boundary |
| Serviceability and reliability | Low | Low to medium for the laser source only | FMEA, laser and engine qualification, field-return/MTTR data and warranty allocation |
| Sustainable gross-profit capture | Unknown | Unknown | Content, ASP, GM, warranty, capex and cannibalisation disclosures |

## Falsification and next diligence

Reduce the supplier thesis if any of the following occurs:

1. A switch/platform owner internalises lasers and optical-engine design, leaving the supplier with commoditised manufacturing.
2. LPO/NPO retains enough electrical margin that CPO engine volume remains narrow.
3. CPO final-package yield, fibre attach, rework or service cost prevents attractive gross margin.
4. Multiple high-power InP and ELS suppliers qualify rapidly, removing the expected bottleneck rent.
5. Disclosed orders do not convert to repeat revenue at an identifiable attractive margin.

The next evidence to obtain is a customer-side CPO confirmation, CPO-specific company revenue/margin commentary, and physical-engine manufacturing/qualification data. Broadcom and NVIDIA must then be assessed separately as platform owners rather than treated as component suppliers.

## Sources

- `CMP-010`: Lumentum, [Fiscal second-quarter 2026 results](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Second-Quarter-of-Fiscal-Year-2026-Financial-Results/default.aspx), 3 February 2026.
- `CMP-015`: Coherent, [Multiple CPO technologies demonstrated at OFC 2026](../01-sources/product-materials/CMP-015-coherent-cpo-ofc-2026.html), 17 March 2026. Canonical publisher URL is retained in the source manifest.
- `CMP-016`: Lumentum, [UHP laser sources for CPO](../01-sources/product-materials/CMP-016-lumentum-uhp-lasers-cpo.html), accessed 7 August 2026. Canonical publisher URL is retained in the source manifest.
- `CMP-017`: Lumentum, [OFC 2026 scale-out, scale-up and scale-across technologies](../01-sources/product-materials/CMP-017-lumentum-ofc-2026-ai-optics.html), 17 March 2026. Canonical publisher URL is retained in the source manifest.
- `FIL-002`: Coherent, [Q3 FY26 Form 8-K and earnings release](https://www.sec.gov/Archives/edgar/data/820318/000119312526208972/d57080dex991.htm), 6 May 2026.
- `FIL-003`: Lumentum, [Q3 FY26 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1633978/000162828026030777/lite-20260328.htm), filed 6 May 2026.
- `PRS-003`: Coherent, [OFC 2026 investor event](../01-sources/conference-presentations/PRS-003-coherent-ofc-investor-event-2026.pdf), 17 March 2026.
- `PRI-023`: Coherent, [NVIDIA strategic optics agreement](../01-sources/product-materials/PRI-023-nvidia-coherent-strategic-partnership.md), 2 March 2026.
- `PRI-024`: Lumentum, [NVIDIA strategic optics agreement](../01-sources/product-materials/PRI-024-nvidia-lumentum-strategic-partnership.md), 2 March 2026.
- `PRI-025`: Lumentum, [Greensboro InP facility](../01-sources/product-materials/PRI-025-lumentum-greensboro-fab.md), 26 March 2026.

Company materials establish disclosed product claims and financial statements establish corporate-level financial facts; neither independently validates CPO performance, volume, yield, reliability or profitability.
