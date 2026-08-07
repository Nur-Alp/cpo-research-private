# Scale-Out Optical Engine and PIC Profit-Pool Thesis

**Owner:** Nur Alpys  
**Status:** Provisional thesis, not an investment conclusion  
**Deployment domain:** AI data-centre scale-out Ethernet switching  
**Technology horizon:** 102.4T and 204.8T switch generations, 2026 to 2032  
**Last updated:** 2026-08-07

## Thesis in one sentence

> Within scale-out photonics, the most defensible external-supplier profit pool is likely to accrue to companies that can repeatedly manufacture a complete optical-engine platform - PIC, driver and TIA co-design, laser interface, fibre attach, package, test and control - at superior yield, reliability and cost, rather than to the company with the best isolated PIC result.

This is a probability-weighted thesis, not a guarantee. Technical leadership produces durable profit only if it creates pricing power, qualified market share, repeat volume and acceptable returns after yield loss, warranty cost, research spending and capital expenditure.

## Two different profit pools

### 1. Total system-level economic rent

The largest absolute economic rent may remain with switch and platform owners such as Broadcom and NVIDIA. They control important system interfaces, switch silicon, SerDes, software, qualification and the customer purchasing decision. Broadcom presents an integrated CPO platform spanning switching, silicon photonics and advanced packaging, while NVIDIA states that Spectrum-X Ethernet Photonics CPO switches are in production.[S1][S2]

That does not automatically make either company the best CPO investment. Their incremental CPO profit is not publicly separated from much larger semiconductor or accelerated-computing businesses.

### 2. Concentrated external-photonics profit

Among external photonics suppliers, the potentially attractive position is a vertically integrated optical-engine platform. Coherent publicly demonstrates silicon-photonics, VCSEL and InP-on-silicon CPO approaches, including a 6.4T socketed silicon-photonics engine, and describes capabilities across lasers, detectors, fibre attach and packaging.[S3][S4]

Lumentum must also remain in the core optical-engine/PIC universe. Its public evidence is strongest in high-power InP lasers, serviceable ELSFP architecture and heterogeneous optical-engine integration. It has also disclosed an incremental multi-hundred-million-dollar CPO order for delivery in the first half of 2027, although the customer, product boundary, margin and cancellation terms are undisclosed.[S5][S6][S7]

## Why the complete engine matters more than the isolated PIC

An optical engine becomes economically valuable only when all of the following work together:

1. The PIC meets bandwidth, insertion-loss, modulation and thermal requirements.
2. Driver and TIA electronics meet the required lane rate and electrical-loss budget.
3. The laser architecture supplies adequate power with acceptable lifetime and efficiency.
4. Fibre attach and connectors achieve repeatable alignment and loss at scale.
5. The package can be assembled, tested and reworked with acceptable yield.
6. The engine passes customer qualification and operates within a supportable failure domain.
7. Manufacturing cost falls faster than customer pricing.

Academic work identifies packaging, thermal management, test, socketability and high-volume manufacturability as central CPO constraints, while 102.4T link modelling shows that laser placement, temperature, architecture and fibre count materially affect the system design.[S8][S9]

## Provisional profit-pool ranking

| Position | Provisional profit potential | Reason | Principal risk |
|---|---:|---|---|
| Switch ASIC plus optical-engine platform | Highest absolute rent | Controls architecture, interfaces, qualification and system pricing | CPO-specific earnings may be immaterial or undisclosed |
| Complete optical engine plus PIC and package | High external-supplier potential | High content, difficult co-design and direct control of engine yield and performance | Standardisation, multisourcing and customer bargaining power |
| High-power InP laser plus ELSFP | Potentially high bottleneck value | Difficult reliability and thermal requirements; useful across multiple SiPh engines | Lower content per system, dual sourcing and possible integration alternatives |
| Fibre attach and specialist packaging | Necessary but uncertain rent | Directly controls loss, assembly yield and manufacturability | Capital intensity and contract-manufacturing price pressure |
| Foundry fabrication | Durable enabling role | High process barriers and broad customer access | Incremental CPO economics may be small relative to the foundry base |
| Individual passive components | Lower expected rent | Necessary content with possible volume scale | Greater commoditisation and substitution risk |

## Laser thesis after the first device comparison

The first matched review weakens, but does not reject, the high-power external-laser profit-pool thesis. The detailed comparison is in [CPO Laser-Architecture Benchmark](../03-components/laser-architecture-benchmark.md).

1. Lumentum has the strongest reviewed packaged result: its 1310 nm DFB prototype reached 580 mW ex-fibre at 50 C laser temperature, and module PCE was at least 10% at 400 mW across the reported conditions.[S11]
2. Sumitomo is a credible competing InP source. Its SOA-integrated DFB exceeded 500 mW at 45 C and reported 25% PCE over 200-440 mW, but the output is not stated as fibre-coupled and the PCE boundary is insufficiently detailed for direct comparison with Lumentum.[S12]
3. External-laser power is not the same as delivered engine-input power. An AIST polymer 1x4 splitter experiment tolerated more than +20 dBm input but showed approximately 10.5-15 dB total insertion loss and required a fibre amplifier; its 1.6 and 3.2 Tb/s figures were extrapolations rather than simultaneous aggregate links.[S13]
4. A directly modulated 850 nm VCSEL demonstrated strong single-device power, bandwidth and optical-feedback tolerance, but remained at a 56 Gb/s eye rate and lacked array, temperature, lifetime, yield and package evidence. It is a longer-term short-reach countercase, not a current matched 200G-per-lane alternative.[S14]

The provisional conclusion is therefore:

> High-power InP ELS is a technically credible candidate profit pool, but current academic evidence does not prove durable scarcity or supplier pricing power. Profit depends on packaged ex-fibre efficiency, lifetime, qualified capacity and the complete distribution path.

The laser scorecard must use cost per delivered optical watt over warranted life. Comparing unmatched chip-facet power or PCE figures would overstate technical and economic differentiation.

## Companies currently inside the core comparison

| Company | Role in this thesis | Current evidence boundary |
|---|---|---|
| Broadcom | Merchant switch ASIC, SerDes, silicon-photonics engine and package integration | Strong company-supplied platform and production claims; insufficient independent yield, unit and CPO-margin evidence |
| NVIDIA | Integrated scale-out networking platform and CPO system architecture | Production claim and named adopters; supplier content and CPO-specific economics remain unclear |
| Coherent | Complete external optical-engine/PIC candidate spanning SiPh, InP, VCSEL, lasers, attach and packaging | Broad demonstrations and capacity evidence; customer identity, production yield and CPO margin remain undisclosed |
| Lumentum | Optical-engine/PIC participant with a particularly strong InP laser and ELSFP position | Material order signal and device evidence; exact supplied content and profitability remain undisclosed |
| Intel | Historical silicon-photonics, packaging and socketable-engine reference point | Current product, customer and economic position requires a fresh evidence review |
| Cisco/Acacia and Ranovus | Additional scale-out PIC and optical-engine candidates | Require comparable product-boundary, production and customer evidence |

Meta and other hyperscalers belong in the customer-requirements and adoption evidence set. They should not receive optical-engine or PIC technology-leadership scores unless they disclose a directly controlled design and its measurable results.

## Profit conversion test

For every company, estimate:

```text
Incremental CPO gross profit
= addressable systems
x optical content per system
x qualified market share
x realised gross margin
- cannibalised legacy gross profit
- yield loss, warranty and support cost
- incremental research and qualification cost
- attributable capital expenditure
```

Technical superiority affects only some of these variables. A company can lead technically and still destroy value through poor yield, excessive capital intensity, customer concentration, price erosion or cannibalisation.

## Evidence required before increasing confidence

1. Complete optical-engine power and performance at a defined boundary.
2. Known-good-die, package and final-engine yield distributions.
3. Fibre-attach cycle time, loss distribution, automation and rework rate.
4. Laser lifetime, redundancy, replaceability and warranty allocation.
5. Named customer qualification, repeat orders and production volume.
6. Content per switch, realised selling price and incremental gross margin.
7. Customer concentration, second-source status and cancellation protection.
8. Capital required for InP, silicon photonics, packaging and test capacity.
9. Evidence that CPO wins against improving LPO, NPO and retimed pluggables on total cost per delivered bit.

## Falsification conditions

Reduce or reject this thesis if any of the following occurs:

- Optical engines become standardised and readily multisourced before suppliers establish durable differentiation.
- Hyperscalers or switch vendors internalise the highest-value PIC and engine design while external suppliers retain only low-margin manufacturing.
- Advanced pluggables or NPO meet 102.4T and 204.8T requirements without an economically material CPO advantage.
- Engine yield, fibre attach, warranty cost or capital intensity consumes the expected gross profit.
- High-power lasers become broadly interchangeable and price competition removes the apparent bottleneck rent.
- Disclosed CPO orders fail to convert into repeat revenue at attractive margins.

## Current research priority

The primary workstream is therefore:

> Which company can manufacture the lowest-total-cost, qualification-ready 200G/lane and later 400G/lane scale-out optical engine, and how much sustainable gross profit can it retain after customers, switch-platform owners and manufacturing partners take their shares?

The first comparative deep dive should cover Broadcom, Coherent, Lumentum and NVIDIA. Intel, Cisco/Acacia and Ranovus should be added once their current scale-out products and commercial status are documented on the same evidence boundary.

## References

- **[S1]** Broadcom, [CPO platform overview](https://www.broadcom.com/info/optics/cpo), accessed 2026-08-07. Company description of its integrated silicon-photonics, switch and packaging position.
- **[S2]** NVIDIA, [Vera Rubin Ramps Into Full Production](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory), 2026-05-31. Company production claim for Spectrum-X Ethernet Photonics.
- **[S3]** Coherent, [Multiple CPO technologies demonstrated at OFC 2026](https://www.coherent.com/news/press-releases/coherent-co-packaged-optics-cpo-technologies-ofc-2026), 2026-03-17.
- **[S4]** Coherent, [Technology Innovation Briefing, OFC 2026](../01-sources/conference-presentations/PRS-003-coherent-ofc-investor-event-2026.pdf), 2026-03-17.
- **[S5]** Lumentum, [Ultra-high-power lasers for CPO](https://www.lumentum.com/en/products/data-center/cw-lasers/uhp-lasers-cpo), accessed 2026-08-07.
- **[S6]** Lumentum, [Advanced packaging and heterogeneous integration for AI](https://www.lumentum.com/en/blog/advanced-packaging-and-heterogeneous-integration-reshaping-photonic-architectures-ai), 2026-03-31.
- **[S7]** Lumentum, [Fiscal second-quarter 2026 results](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Second-Quarter-of-Fiscal-Year-2026-Financial-Results/default.aspx), 2026-02-03.
- **[S8]** Ravi Mahajan et al., [*Co-Packaged Photonics for High Performance Computing: Status, Challenges and Opportunities*](../01-sources/papers/PAP-003-mahajan-co-packaged-photonics-hpc-2022.pdf), *Journal of Lightwave Technology* 40(2), 2022, DOI 10.1109/JLT.2021.3104725.
- **[S9]** Brandon Buscaino et al., [*External vs. Integrated Light Sources for Intra-Data Center Co-Packaged Optical Interfaces*](../01-sources/papers/PAP-002-buscaino-external-vs-integrated-light-sources-2021.pdf), *Journal of Lightwave Technology* 39(7), 2021, DOI 10.1109/JLT.2020.3043653.
- **[S10]** OIF, [*Management of External Light Sources and Co-Packaged Optical Engines*](../01-sources/standards/STD-006-oif-elsfp-management.pdf). External-laser management and interoperability reference.
- **[S11]** Wenjia Zhou et al., [*High Power CW Laser for Co-Packaged Optics*](../01-sources/papers/PAP-019-zhou-high-power-cw-laser-cpo-2022.pdf), CLEO 2022 paper SS2D.3, DOI 10.1364/CLEO_SI.2022.SS2D.3.
- **[S12]** Daisuke Inoue et al., [*High Power SOA-integrated DFB Lasers for Co-packaged Optics*](../01-sources/papers/PAP-022-inoue-soa-dfb-lasers-cpo-2025.pdf), JSAP-Optica Joint Symposia 2025 abstract 8p-N203-6.
- **[S13]** Satoshi Suda et al., [*High-Capacity Transmission with Single External Laser Source and Polymer-Based Splitters for Co-Packaged Optics*](../01-sources/papers/PAP-026-suda-external-laser-polymer-splitters-2024.pdf), CLEO 2024 paper SF3F.7.
- **[S14]** Cheng-Wei Lin et al., [*Single-Mode VCSELs With Zn-Diffusion Apertures for Applications in Co-Packaged Optics Systems*](../01-sources/papers/PAP-027-lin-single-mode-vcsel-cpo-2025.pdf), *IEEE Journal of Selected Topics in Quantum Electronics* 31(2), 2025, DOI 10.1109/JSTQE.2024.3454318.

Company announcements establish what the companies claim and disclose; they do not independently prove performance, production volume, yield or sustainable profit.
