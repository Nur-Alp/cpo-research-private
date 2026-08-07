# Scale-Out Optical-Engine Benchmark

**Status:** Initial evidence build; not a company ranking

**Decision domain:** AI data-centre scale-out optical links

**Generation:** 200G per lane and 1.6T engines, with a later 400G-per-lane extension

**Last updated:** 2026-08-07

## Decision question

Which optical-engine architecture can meet the required link performance at the lowest total qualified cost, and which supplier can retain durable gross profit after yield loss, packaging, test, warranty, customer concentration and capital intensity?

The benchmark separates a measured device result from a qualified engine and a commercial product. A blank or `Unknown` cell is an evidence gap, not a zero. The supporting paper-by-paper classification is in the [academic evidence matrix](academic-evidence-matrix.md).

The investment bridge for the PIC routes is in [PIC-design profit implications](pic-design-profit-implications.md). It keeps isolated device performance separate from cost-per-qualified-good-engine and supplier profit capture.

## Comparison rules

1. Compare the same direction, lane count, modulation, reach, temperature, BER/FEC and power boundary.
2. Record whether a result is measured, simulated, projected or review synthesis.
3. Do not treat aggregate optical output as full multi-channel link validation.
4. Do not award manufacturability without final-package yield, test coverage, cycle time, rework and scrap evidence.
5. Do not award commercial maturity without qualification, repeat production and customer evidence.

For external-light architectures, the OIF ELSFP 2.0 agreement adds a standards-level service and qualification boundary: the module must be designed around a chosen 0–70°C, −5–85°C or −40–85°C case class, a 10-year field-life requirement, defined durability cycles and EIA-364-1000-based mechanical/environmental/electrical testing. Those requirements make replaceable laser serviceability more concrete, but they intentionally leave application-specific optical power, noise and wavelength requirements open; ELSFP compliance therefore cannot substitute for a complete delivered-power or 200G/400G link result.[CLM-287][CLM-288][CLM-289][CLM-290]

## Technical benchmark

| Candidate | Source and evidence class | Intended use | PIC and integration | Laser architecture | Electrical and modulation boundary | Reported optical/link result | Temperature | Full-engine power | Evidence maturity |
|---|---|---|---|---|---|---|---:|---:|---|
| Nokia monolithic InP transmitter | `PAP-025`; measured conference result | 1.6T LPO O-band transmitter | Monolithic InP PIC: 4 DFBs, 8 MZMs, 8 SOAs and 8 power-monitor taps; separate SiGe driver | Four integrated DFBs, each feeding two channels; per-channel SOA for boost, control and shuttering | Representative channel: 106.25 GBd PAM4, direct linear drive; RF Vpi below 1.5 V; 15-tap FFE at both Tx and Rx | Representative channel: about 3 dB TDECQ, 0.97 RLM, 3.5 dB outer ER and 3-5 dBm fibre-coupled output. Packaged all-channel output: 2.8-3.0 dBm; complete eight-channel RF results pending | 60 C | Unknown | Component/partial-engine demonstration |
| CMOS-integrated silicon-photonics design space | `PAP-024`; peer-reviewed review synthesis | Pluggable, LPO, CPO and optical I/O | Hybrid, heterogeneous, monolithic, 2D, 2.5D and 3D options; no single compared product | External, bonded III-V/silicon, monolithic and comb-source options | Review spans IMDD and coherent links across non-matched nodes and lane rates | Not a product result. Review identifies submodule performance and integration mechanisms but cannot supply a matched engine score | Varies | Not comparable | Architecture and diligence reference |
| Modeled laser-forwarded coherent transmitter | `PAP-012`; peer-reviewed model/projection | O-band short-reach CPO; spectral-efficiency countercase | Assumes monolithic electronic-photonic OTRX with MZM IQ transmitter and coherent receiver | External laser split between Tx and forwarded local oscillator | 56 GSym/s PAM4 electrical I/Q inputs produce 224 Gb/s QAM-16; modeled one-tap FFE/DFE in host SerDes | Projected Tx driver plus laser energy: 2.27 pJ/bit unequalised, 1.63 with Tx FFE, 1.35 with DFE; no fabricated 224 Gb/s link | Modeled, unspecified | Not reported; host SerDes, Rx, tuning and control excluded | Architecture model |
| Lightmatter monolithic microring Tx+Rx | `PAP-021`; measured conference result | High-density 3D CPO beneath an XPU or switch | Inductorless Tx driver/MRM and Ge-PD/MRR AFE monolithically integrated in GF 45SPCLO; 0.006 mm2 total active area | Off-chip laser; integrated heaters and automatic ring locking | Single-wavelength NRZ: 56 Gb/s open eye without equalisation; 64 Gb/s only with three-tap software Rx FFE | On-chip Tx-to-Rx path; at 56 Gb/s, 84.4 mW excluding laser and 1.51 pJ/bit; no fibre reach or multi-wavelength result | Unspecified | Partial boundary only | Single-channel circuit demonstration |
| Ayar TeraPHY known-good connectorized chiplet | `PAP-013`; company-authored measured/simulated conference result | Accelerator/compute optical I/O chiplet packaging | GF Fotonix chiplet with V-groove passive fibre attach, fibre bundle and MOLA lens connector; electrical/optical test before final MCP assembly | Not evaluated in this paper | Connector has 12 fibres and is described as scalable to 24; current lens array uses active alignment | Simulated 0.2 dB-penalty tolerances: 6 um translation, +/-0.2 degrees tilt and +/-600 um separation; early samples show less than 0.1 dB repeatability standard deviation over ten mating cycles; no data-link result | Unspecified | Not reported | Early connector/process proof of concept |
| Microsoft MOSAIC microLED wide-and-slow link | `PAP-009`; measured prototype plus system simulation | Rack-scale optical-link countercase, not a like-for-like 200G/lane PIC | 100 microLED and CMOS-sensor channels on prototype; multicore imaging fibre and custom TIR micro-optics; envisioned vertical bonding for production | Directly modulated microLEDs; no laser or high-speed DSP | 2 Gb/s/channel prototype; 800 Gb/s target uses roughly 460 channels including redundancy | Measured 2 Gb/s over 20 m and 1.6 Gb/s over 30 m; 800 Gb/s pluggable 2 Gb/s/channel over 50 m is simulated; modeled 3.1–5.3 W per end | Prototype 20–30 m; production reach modeled to 50 m | 3.1–5.3 W per end modeled; host-interface boundary differs from CPO rows | Architectural countercase; no qualified engine or production data |
| POET CMOS optical-interposer engine | `PAP-014`; measured component and small assembled-engine demonstration | 100/200G datacom engine; 400G extension stated | CMOS-based optical interposer with multilayer waveguides, TSV/electrical traces, integrated heat sink and visually assisted passive flip-chip assembly | Four directly modulated lasers in the 6 mm × 9 mm engine; exact laser device boundary not reported | 100G eye and 100/200G receiver sensitivity meeting stated 10 km LR4 requirements; 400G not measured | Waveguide <0.3 dB/cm; 0.25 dB facet coupling; 0.5 dB vertical mirror; ~1 dB passive laser coupling | Not fully specified | Not reported | Component/engine demonstration; wafer-scale HVM and economics unproven |
| Intel OCI chiplet | `CMP-035`; official prototype demonstration and platform history | Accelerator optical I/O; future CPO/on-board implementations | Integrated silicon-photonics PIC with on-chip DWDM lasers/SOAs and an electrical IC; co-packaged with Intel CPU in demonstration | Integrated on-chip lasers; no external laser required in the described OCI implementation | 64 × 32 Gb/s channels per direction; 4 Tb/s bidirectional; standard SMF up to 100 m | Company-reported 5 pJ/bit demonstration comparison; no matched complete-link result in retained source | Demonstration boundary; not a qualification temperature sweep | Not reported as complete engine | Prototype/select-customer evaluation; prior PIC volume is pluggable-only |
| Ranovus ODIN EPIC | `CMP-036`; official manufacturing-route announcement | CPO/NPO optical engine; 800G and 6.4T implementations stated | Monolithic EPIC integrates lasers, modulators, photodetectors, drivers, TIAs and control loops | Integrated optical functions; exact wavelength/power boundary not disclosed | Aggregate product configurations stated; no retained lane-level measurement | No measured loss, BER/TDECQ, energy or complete-engine power in source | Not reported | Not reported | Planned Jabil high-volume route; shipped volume and qualification unknown |
| Cisco 51.2T linear-pluggable comparator | `CMP-037`; official system demonstration | Scale-out switch comparator against CPO | Cisco system platform; optical-engine/PIC supplier boundary undisclosed | Linear pluggable optics; CPO supply-chain strategy described separately | 64 × 800G pluggable ports in 51.2T demonstration | Company-reported 30% system-power reduction versus traditional retimed optics; not a CPO result | Not reported | Not reported as a matched CPO/LPO engine | Demonstration and stated qualification process; production CPO evidence unknown |
| Acacia 200G/lane engine family | `CMP-038`; official product announcement | 1.6T/800G client optics; LPO and retimed-optics routes | Silicon-photonic engine family paired with 3 nm Kibo PAM4 DSP; internal packaging boundary undisclosed | Silicon-photonic PIC; laser architecture not specified in announcement | 200G/lane target; 1.6T and 800G configurations stated | No retained lane-level BER/TDECQ/power result; prior >1M volume claim is for 100G/lane engines | Not reported | Not reported | Product/roadmap announcement with prior-volume baseline; 200G/lane qualification unknown |

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

## New 400G/PIC and full-module evidence

| Candidate | Source and evidence class | Intended use | PIC and integration | Laser architecture | Electrical and modulation boundary | Reported optical/link result | Temperature | Full-engine power | Evidence maturity |
|---|---|---|---|---|---|---|---:|---:|---|
| C2PO microring coherent transmitter | `PAP-038`; link-level model plus low-rate fabricated proof of concept | Beyond-PAM4 200/400G-per-wavelength optical I/O | GF45SPCLO microring/RAMZI transmitter concept with thermal tuning; fabricated chip wire-bonded on PCB | Laser-forwarded coherent architecture; total laser power modeled | Offset-QAM-16, 200/400 Gb/s per fibre per wavelength; target pre-FEC BER 10^-6 | Modeled 6.71 dBm at 200 Gb/s and 9.65 dBm at 400 Gb/s; fabricated proof only 25 Gb/s offset-QAM-4 | Thermal simulation; no production package | Unknown; total optical power is not complete engine input power | Architecture model plus low-rate prototype |
| SiON/Si 2.5D optical interposer | `PAP-039`; measured research transceiver | 400G aggregate optical I/O | SiON passive interposer with flip-chip EML and PD chiplets, CWDM/AWG routing | Four InP EMLs; flip-chip active sources | 4 × 106.25 Gb/s PAM4; 400 Gb/s CWDM aggregate | 50°C maximum TDECQ 1.81 dB, dynamic ER 4.9 dB; OMA sensitivity about −7.25 dBm at BER 2.4×10^-4; near 10^-7 at 0 dBm without FEC | 50°C transmitter result | Unknown | Measured research transceiver; not 200G/lane |
| GRIN/evanescent passive coupler | `PAP-040`; 3D FDTD simulation | Chip-to-chip and fibre-to-chip CPO packaging | GRIN lens/coupler plus evanescent interface; intended for passive assembly | Not evaluated | Not a data-link result | Simulated <0.27 dB coupling at 11 µm gap; 1 dB vertical tolerance ~2.38 µm and lateral ±2.24 µm; >360 nm bandwidth | Process assumptions only | Not applicable | Packaging simulation |
| IBM single-mode polymer-waveguide module | `PAP-041`; official abstract/full-module process record | Full-module CPO packaging | Two substrate configurations, optics-last assembly and single-mode polymer-waveguide interface | Not disclosed | Not disclosed | Abstract reports <1.2–2.0 dB insertion loss and thermal-stress resilience; no lane-rate result | Thermomechanical testing stated; conditions not disclosed | Unknown | Full-module abstract; quantitative qualification incomplete |

## Integration trade-offs from the review literature

### PAP-024 cross-platform evidence boundary

The 2026 *Nature Reviews Electrical Engineering* synthesis is useful for mapping the integration stack, but it is not a matched optical-engine benchmark. It identifies the principal coupling and packaging gates: conventional grating couplers are roughly −2.2 dB with 30–40 nm bandwidth, advanced edge/grating demonstrations can be below 1 dB, and record devices may require non-standard foundry steps. Those figures are component results, so the benchmark must still obtain a multi-fibre loss distribution, attach cycle time, rework rate and final-package yield.

The review also gives a mechanism for why integration depth matters. It associates 2D wire-bond paths with roughly 0.5–1.0 nH/mm parasitics and typical energy above 5 pJ/bit, while 3D stacking shortens the path but introduces thermal density and fine alignment constraints. Its cited 15–30 pJ/bit pluggable and approximately 40% LPO reduction are orientation only; they are not substitutes for the matched 102.4T scenario model. See `CLM-120` through `CLM-123`.

Investment consequence: the scarce capability may be the process-control stack that jointly closes coupling loss, electrical parasitics, thermal path, wafer/package test and yield—not simply the PIC material or laser architecture with the best isolated headline number.

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

The additional packaging records `PAP-028`–`PAP-031` reinforce why the rows above cannot be scored on PIC bandwidth alone: detachable known-good-module testing, FOWLP engine construction, external-light polymer distribution and glass-interposer thermal/RF behavior each improve a different part of the engine flow. Their reported losses, short-duration stability and test-vehicle temperatures remain non-comparable to a qualified 200G/lane or 400G/lane engine, so they are constraints and design options rather than ranking inputs. See `CLM-239`–`CLM-245` and the [packaging benchmark](packaging-reliability-benchmark.md).

The electrical-channel countercase is recorded in [Linear-Drive Optics Boundary Benchmark](../02-architecture/linear-drive-boundary-benchmark.md). It matters here because an excellent PIC does not create an automatic CPO profit pool if a customer can retain LPO margin at its required topology and service boundary.

The first supplier comparison is in [Coherent and Lumentum External Optical-Engine Supplier Dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md). It keeps demonstrated component breadth and ELSFP serviceability separate from unknown complete-engine yield, qualification and CPO-specific profitability.

## Sources

- `PAP-024`: Yating Wan et al., [*Integrating silicon photonics with complementary metal-oxide-semiconductor technologies*](../01-sources/papers/PAP-024-wan-integrating-silicon-photonics-cmos-2026.pdf), *Nature Reviews Electrical Engineering*, volume 3, 2026, DOI `10.1038/s44287-025-00223-0`.
- `PAP-025`: S. Porto et al., [*1.6 Tb/s Monolithic InP Transmitter PIC with DFB, MZM, and SOA Arrays*](../01-sources/papers/PAP-025-porto-monolithic-inp-transmitter-pic-2026.pdf), OFC 2026 paper Th1C.4.
- `PAP-012`: Antroy Roy Chowdhury, Wahid Rahman and Vladimir Stojanovic, [*Electronic-Photonic Co-Optimization of Linear Drive Laser-Forwarded Coherent Silicon Photonic Transmitters for Co-Packaged Optical (CPO) Links*](../01-sources/papers/PAP-012-chowdhury-electronic-photonic-cooptimization-2025.pdf), *Journal of Lightwave Technology* 43(9), 2025, DOI `10.1109/JLT.2025.3532994`.
- `PAP-021`: Reza Baghdadi et al., [*Monolithically Integrated Microring Transmitter and Receiver for High-Density 3D Co-Packaged Optics*](../01-sources/papers/PAP-021-baghdadi-microring-3d-cpo-2025.pdf), OFC 2025 paper Tu3J.6.
- `PAP-013`: Chong Zhang et al., [*Connectorized Optical I/O Chiplet with V-groove for AI and High Performance Computing*](../01-sources/papers/PAP-013-zhang-connectorized-optical-io-chiplet-2025.pdf), OFC 2025 paper Th3H.2.
- `PAP-009`: Kaoutar Benyahya et al., [*MOSAIC: Breaking the Optics versus Copper Trade-off with a Wide-and-Slow Architecture and MicroLEDs*](../01-sources/papers/PAP-009-microsoft-mosaic-microled-2025.pdf), ACM SIGCOMM 2025, DOI `10.1145/3718958.3750510`. Countercase only: prototype measurements and modeled 800 Gb/s module are not a qualified 200G/400G-per-lane engine.
- `CMP-035`: [Intel OCI chiplet demonstration and silicon-photonics platform](../01-sources/product-materials/CMP-035-intel-oci-chiplet-ofc2024.md), canonical Intel sources retained. Prototype optical-I/O integration and prior pluggable PIC volume; no OCI production proof.
- `CMP-036`: [Ranovus/Jabil ODIN optical-engine manufacturing collaboration](../01-sources/product-materials/CMP-036-ranovus-jabil-odin-mass-production.md), canonical Ranovus announcement retained. Planned EPIC manufacturing route; no shipped-volume or yield proof.
- `CMP-037`: [Cisco CPO architecture and supply-chain qualification boundary](../01-sources/product-materials/CMP-037-cisco-ai-networking-cpo-supply-chain.md), canonical Cisco post retained. System comparator and qualification-process claim; no controlled CPO result.
- `CMP-038`: [Acacia 200G/lane silicon-photonic optical-engine family](../01-sources/product-materials/CMP-038-acacia-200g-lane-optical-engine-2025.md), canonical Acacia announcement retained. Direct 200G/lane product route with prior 100G/lane volume context; no 200G/lane qualification proof.
- `PAP-038`: Dan Sturm et al., [*C2PO: Coherent Co-packaged Optics using offset-QAM-16 for Beyond PAM-4 Optical I/O*](../01-sources/papers/PAP-038-sturm-c2po-coherent-cpo-qam16-2025.pdf), arXiv:2506.12160. Full PDF retained; 200/400G results are modeled and the fabricated proof is 25 Gb/s.
- `PAP-039`: Daibao Hou et al., [*2.5D co-packaged optical I/O chipsets on a SiON/Si interposer for 4 × 100G optical interconnection*](../01-sources/papers/PAP-039-hou-sion-optical-interposer-2026.pdf), arXiv:2602.08284. Full PDF retained; measured 400G aggregate research transceiver.
- `PAP-040`: Drew Weninger et al., [*Graded Index Couplers for Next Generation Chip-to-Chip and Fiber-to-Chip Photonic Packaging*](../01-sources/papers/PAP-040-weninger-grin-couplers-cpo-2025.pdf), arXiv:2503.00121. Full PDF retained; coupling and alignment results are simulations.
- `PAP-041`: Akihiro Horibe et al., [*Co-packaged optics module with single-mode polymer waveguide*](../01-sources/papers/PAP-041-ibm-single-mode-polymer-waveguide-iedm2025.md), IBM Research / IEDM 2025. Official abstract record retained; full paper requires access.
