# Scale-Out Optical-Engine Benchmark

**Status:** Initial evidence build; not a company ranking

**Decision domain:** AI data-centre scale-out optical links

**Generation:** 200G per lane and 1.6T engines, with a later 400G-per-lane extension

**Last updated:** 2026-08-07

## Decision question

Which optical-engine architecture can meet the required link performance at the lowest total qualified cost, and which supplier can retain durable gross profit after yield loss, packaging, test, warranty, customer concentration and capital intensity?

The benchmark separates a measured device result from a qualified engine and a commercial product. A blank or `Unknown` cell is an evidence gap, not a zero.

## Comparison rules

1. Compare the same direction, lane count, modulation, reach, temperature, BER/FEC and power boundary.
2. Record whether a result is measured, simulated, projected or review synthesis.
3. Do not treat aggregate optical output as full multi-channel link validation.
4. Do not award manufacturability without final-package yield, test coverage, cycle time, rework and scrap evidence.
5. Do not award commercial maturity without qualification, repeat production and customer evidence.

## Technical benchmark

| Candidate | Source and evidence class | Intended use | PIC and integration | Laser architecture | Electrical and modulation boundary | Reported optical/link result | Temperature | Full-engine power | Evidence maturity |
|---|---|---|---|---|---|---|---:|---:|---|
| Nokia monolithic InP transmitter | `PAP-025`; measured conference result | 1.6T LPO O-band transmitter | Monolithic InP PIC: 4 DFBs, 8 MZMs, 8 SOAs and 8 power-monitor taps; separate SiGe driver | Four integrated DFBs, each feeding two channels; per-channel SOA for boost, control and shuttering | Representative channel: 106.25 GBd PAM4, direct linear drive; RF Vpi below 1.5 V; 15-tap FFE at both Tx and Rx | Representative channel: about 3 dB TDECQ, 0.97 RLM, 3.5 dB outer ER and 3-5 dBm fibre-coupled output. Packaged all-channel output: 2.8-3.0 dBm; complete eight-channel RF results pending | 60 C | Unknown | Component/partial-engine demonstration |
| CMOS-integrated silicon-photonics design space | `PAP-024`; peer-reviewed review synthesis | Pluggable, LPO, CPO and optical I/O | Hybrid, heterogeneous, monolithic, 2D, 2.5D and 3D options; no single compared product | External, bonded III-V/silicon, monolithic and comb-source options | Review spans IMDD and coherent links across non-matched nodes and lane rates | Not a product result. Review identifies submodule performance and integration mechanisms but cannot supply a matched engine score | Varies | Not comparable | Architecture and diligence reference |
| Modeled laser-forwarded coherent transmitter | `PAP-012`; peer-reviewed model/projection | O-band short-reach CPO; spectral-efficiency countercase | Assumes monolithic electronic-photonic OTRX with MZM IQ transmitter and coherent receiver | External laser split between Tx and forwarded local oscillator | 56 GSym/s PAM4 electrical I/Q inputs produce 224 Gb/s QAM-16; modeled one-tap FFE/DFE in host SerDes | Projected Tx driver plus laser energy: 2.27 pJ/bit unequalised, 1.63 with Tx FFE, 1.35 with DFE; no fabricated 224 Gb/s link | Modeled, unspecified | Not reported; host SerDes, Rx, tuning and control excluded | Architecture model |
| Lightmatter monolithic microring Tx+Rx | `PAP-021`; measured conference result | High-density 3D CPO beneath an XPU or switch | Inductorless Tx driver/MRM and Ge-PD/MRR AFE monolithically integrated in GF 45SPCLO; 0.006 mm2 total active area | Off-chip laser; integrated heaters and automatic ring locking | Single-wavelength NRZ: 56 Gb/s open eye without equalisation; 64 Gb/s only with three-tap software Rx FFE | On-chip Tx-to-Rx path; at 56 Gb/s, 84.4 mW excluding laser and 1.51 pJ/bit; no fibre reach or multi-wavelength result | Unspecified | Partial boundary only | Single-channel circuit demonstration |
| Ayar TeraPHY known-good connectorized chiplet | `PAP-013`; company-authored measured/simulated conference result | Accelerator/compute optical I/O chiplet packaging | GF Fotonix chiplet with V-groove passive fibre attach, fibre bundle and MOLA lens connector; electrical/optical test before final MCP assembly | Not evaluated in this paper | Connector has 12 fibres and is described as scalable to 24; current lens array uses active alignment | Simulated 0.2 dB-penalty tolerances: 6 um translation, +/-0.2 degrees tilt and +/-600 um separation; early samples show less than 0.1 dB repeatability standard deviation over ten mating cycles; no data-link result | Unspecified | Not reported | Early connector/process proof of concept |

## Nokia measurement boundary

| Dimension | What is established | What remains unknown |
|---|---|---|
| Channel count | DC performance assessed across eight channels; integrated architecture physically contains eight Tx paths | Eight-channel RF/TDECQ/BER distributions |
| Lane performance | One representative channel operated at 106.25 GBd PAM4, corresponding to 212.5 Gb/s raw signalling | Production distribution, FEC boundary and margin across process/temperature |
| Optical output | Approximately 3-5 dBm on the representative RF channel; 2.8-3.0 dBm modulated output across eight packaged channels | Output distribution over lifetime, coupling variation and complete link budget |
| Signal quality | About 3 dB TDECQ, 0.97 RLM and 3.5 dB outer ER on the representative channel | BER/reach result for this exact linear-drive configuration and statistical repeatability |
| Control | Per-channel SOAs provide power adjustment and approximately -20 dBm shuttering | Control-loop power, failure modes, calibration time and firmware complexity |
| Packaging | PIC and SiGe chips were packaged in an OSFP LPO configuration with a commercial receiver | Fibre-attach method, connector loss, assembly time, rework and final yield |
| Thermals | Representative operation and all-channel DC testing at 60 C | Full module thermal gradients, hot spots, cooling and lifetime acceleration |
| Economics | No evidence | Die area, wafer yield, package cost, ASP, gross margin, capex and warranty |
| Commercial stage | Demonstrated | Qualification, customer, production volume and repeat orders |

## Comparator measurement boundaries

| Candidate | What is established | What remains unknown |
|---|---|---|
| Modeled coherent transmitter | A reproducible co-optimisation framework exposes interactions among driver strength, MZM bandwidth and length, external-laser split, receiver noise and host equalisation | Fabricated 224 Gb/s performance; receiver, host-SerDes, tuning and control power; matched reach; total cost; yield; reliability and qualification |
| Lightmatter microring Tx+Rx | A compact 45 nm monolithic circuit produces a 56 Gb/s NRZ open eye without equalisation; reported Tx+Rx power is 84.4 mW excluding laser | Multi-wavelength operation, fibre reach, 200G-per-lane modulation, direct 64 Gb/s BER, heater/laser power, package thermals, production yield and lifetime |
| Ayar KGCC and MOLA | A specific test-before-final-assembly flow and early connector geometry/repeatability evidence | Fibre-attach yield, alignment cycle time, number of samples, environmental/lifetime qualification, passive lens alignment, rework, cost and production volume |

## Integration trade-offs from the review literature

| Integration approach | Potential advantage | Main evidence-backed constraint | Investment relevance |
|---|---|---|---|
| Hybrid assembly | Independent optimisation and pre-screening of III-V, PIC and electronics | Alignment, coupling loss, packaging bulk and thermal management | May favour suppliers with packaging, known-good-die and fibre-attach process control |
| Heterogeneous wafer bonding | Wafer-scale alignment, density and potential cost/reliability improvement | Bonding yield, substrate removal, thermal pathway and early reliability screening | Could create process/IP advantages if yield and burn-in are controlled |
| Monolithic InP transmitter | Fewer optical interfaces and integration of laser, modulator, amplifier and monitor | Complex compound-semiconductor fabrication; full-engine yield and electronics remain separate | Nokia result proves a credible architecture, not a profit-pool winner |
| 2.5D EIC-PIC integration | Higher interconnect density with less thermal concentration than 3D | Added interposer complexity and cost | Possible packaging/platform control point |
| 3D EIC-PIC integration | Short electrical paths, high density and lower parasitics | Thermal density and sub-micrometre alignment reduce yield | Attractive performance path only if test, thermal and rework economics close |

## Initial read-through for the thesis

1. `PAP-024` supports the thesis that the complete integration and manufacturing flow matters more than an isolated device record. It does not identify a company winner.
2. `PAP-025` makes integrated InP a serious countercase to an external-laser-only thesis because it combines source, modulation, amplification and monitoring on one PIC.
3. The Nokia paper does not yet show the metrics that determine sustainable profit: full-engine power, final yield, automated fibre attach, qualification, lifetime, cost or volume.
4. The correct classification is therefore **technically promising component/partial-engine demonstration**, not qualification-ready product.
5. `PAP-012` reinforces that energy is a system co-design output, not a standalone PIC metric. Its best number cannot be compared with complete-engine power because host-SerDes, receiver, tuning and control are outside the boundary.
6. `PAP-021` shows why Lightmatter is relevant to PIC design: its monolithic circuit density is exceptional. It does not yet answer the 200G-per-lane scale-out engine question.
7. `PAP-013` makes pre-assembly optical testing and fibre-attach yield explicit. The economic mechanism is plausible, but ten connector cycles and simulations do not demonstrate high-volume manufacturing.

## Adjacent evidence blocks

The laser papers are now compared separately in [CPO Laser-Architecture Benchmark](laser-architecture-benchmark.md), because source power, packaged efficiency and delivered engine-input power require a different boundary from modulated lane performance.

Fibre attach, connector, assembly and serviceability evidence from `PAP-015` through `PAP-018` is now compared separately in [CPO Packaging, Fibre-Attach and Serviceability Benchmark](packaging-reliability-benchmark.md). The next optical-engine step is to apply these PIC, laser and packaging gates to matched company dossiers for Broadcom, Coherent, Lumentum and NVIDIA.

The electrical-channel countercase is recorded in [Linear-Drive Optics Boundary Benchmark](../02-architecture/linear-drive-boundary-benchmark.md). It matters here because an excellent PIC does not create an automatic CPO profit pool if a customer can retain LPO margin at its required topology and service boundary.

The first supplier comparison is in [Coherent and Lumentum External Optical-Engine Supplier Dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md). It keeps demonstrated component breadth and ELSFP serviceability separate from unknown complete-engine yield, qualification and CPO-specific profitability.

## Sources

- `PAP-024`: Yating Wan et al., [*Integrating silicon photonics with complementary metal-oxide-semiconductor technologies*](../01-sources/papers/PAP-024-wan-integrating-silicon-photonics-cmos-2026.pdf), *Nature Reviews Electrical Engineering*, volume 3, 2026, DOI `10.1038/s44287-025-00223-0`.
- `PAP-025`: S. Porto et al., [*1.6 Tb/s Monolithic InP Transmitter PIC with DFB, MZM, and SOA Arrays*](../01-sources/papers/PAP-025-porto-monolithic-inp-transmitter-pic-2026.pdf), OFC 2026 paper Th1C.4.
- `PAP-012`: Antroy Roy Chowdhury, Wahid Rahman and Vladimir Stojanovic, [*Electronic-Photonic Co-Optimization of Linear Drive Laser-Forwarded Coherent Silicon Photonic Transmitters for Co-Packaged Optical (CPO) Links*](../01-sources/papers/PAP-012-chowdhury-electronic-photonic-cooptimization-2025.pdf), *Journal of Lightwave Technology* 43(9), 2025, DOI `10.1109/JLT.2025.3532994`.
- `PAP-021`: Reza Baghdadi et al., [*Monolithically Integrated Microring Transmitter and Receiver for High-Density 3D Co-Packaged Optics*](../01-sources/papers/PAP-021-baghdadi-microring-3d-cpo-2025.pdf), OFC 2025 paper Tu3J.6.
- `PAP-013`: Chong Zhang et al., [*Connectorized Optical I/O Chiplet with V-groove for AI and High Performance Computing*](../01-sources/papers/PAP-013-zhang-connectorized-optical-io-chiplet-2025.pdf), OFC 2025 paper Th3H.2.
