# CPO Laser-Architecture Benchmark

**Status:** Initial evidence build; not a supplier ranking

**Decision domain:** Light sources for AI data-centre scale-out optical engines

**Target generations:** 200G per lane and later 400G per lane, 2026-2032

**Last updated:** 2026-08-09

## Decision question

Which laser architecture provides the lowest qualified cost per delivered optical watt after fibre coupling, distribution loss, redundancy, cooling, control, serviceability, lifetime, yield and warranty - and which supplier can retain an attractive share of that value?

The source with the highest laboratory output or efficiency does not automatically win. The relevant unit is usable optical power at the engine input over life, not power at an unmatched chip facet.

The quantitative boundary conversion is maintained in the [laser delivered-power waterfall](../08-model/laser-delivered-power-waterfall.md). It applies prototype fan-out loss only as a labelled sensitivity and does not combine unrelated supplier products into a production claim.

## Comparison rules

1. Keep chip-on-submount, packaged ex-fibre and optical-engine-input power separate.
2. Compare power-conversion efficiency only across the same electrical, thermal, coupling and control boundary.
3. Separate directly modulated sources from continuous-wave sources feeding silicon-photonic modulators.
4. Include splitter, connector, waveguide and redundancy loss in delivered-power economics.
5. Do not infer reliability, yield or commercial readiness from one-device performance.
6. Keep O-band InP sources and 850 nm VCSEL links separate unless reach, fibre, modulation and receiver boundaries are matched.

## Evidence-matched comparison

| Candidate | Source and evidence class | Source architecture | Wavelength | Reported output boundary | Efficiency boundary | Temperature boundary | Link or signal evidence | Integration and serviceability | Evidence maturity |
|---|---|---|---:|---|---|---|---|---|---|
| Lumentum conventional high-power DFB | `PAP-019`; measured two-page conference paper | 4 mm InGaAsP/InP DFB in 14-pin butterfly module, lensed PM fibre | 1310 nm | Maximum ex-fibre output: 720 mW at 25 C, 640 mW at 40 C and 580 mW at 50 C laser temperature; 86% coupling. Chip-on-submount maximum: 880 mW at 25 C | At least 10% module PCE at 400 mW across reported test conditions | Laser: 25-50 C; case: 50 and 70 C | CW source only; module SMSR above 45 dB and RINc below -156 dBc over 200-500 mW at 40 and 50 C laser temperature | External and potentially replaceable; distribution, redundancy and ELSFP implementation not tested | Packaged single-device prototype |
| Sumitomo SOA-integrated DFB | `PAP-022`; measured one-page vendor symposium paper | DFB seed plus widened integrated SOA with independent output control; p-side down on AlN | 1.3 um | More than 500 mW at 45 C and more than 300 mW at 70 C; output is not stated as fibre-coupled | Reported 25% PCE at 45 C over 200-440 mW; calculation boundary not detailed | 45-70 C device measurements | CW source only; SMSR above 50 dB and linewidth below 200 kHz | External-source candidate; no package, connector or service process shown | Device/submount result with sparse methods |
| Furukawa eight-channel ELS plus AIST polymer fan-out | `PAP-026`; measured two-page conference paper | Eight fibre-coupled ELS channels feeding polymer 1x4 Y-branch splitter on glass-epoxy substrate | CWDM4 | More than +20 dBm per ELS channel before splitter; splitter plot shows approximately 10.5-15 dB total insertion loss | Not reported; an external BDFA compensates splitter loss | Not reported | One ELS wavelength directly supports four sequential 112 Gb/s PAM4 measurements below 3.4 dB TDECQ; 1.6 and 3.2 Tb/s are extrapolated | External source and substrate distribution may improve serviceability, but adds optical interfaces and fan-out loss | Distribution proof of concept |
| Nokia monolithic InP transmitter PIC | `PAP-025`; measured conference paper | Four DFBs, eight MZMs, eight SOAs and eight monitor taps on one InP PIC | O-band | Representative modulated channel about 3-5 dBm ex-fibre; packaged eight-channel output 2.8-3.0 dBm per channel | Full transmitter and laser power not reported | 60 C | Representative 106.25 GBd PAM4 channel; about 3 dB TDECQ with 15-tap Tx and Rx FFE | Removes an external source-distribution boundary but places laser failure and heat inside the transmitter assembly | Component/partial-engine demonstration |
| Zn-diffusion single-mode VCSEL | `PAP-027`; measured peer-reviewed journal paper | Directly modulated 850 nm single-junction VCSEL with ring-shaped Zn-diffusion aperture | 850 nm | Five-micrometre variant: 6.7 mW; seven-micrometre variant: 16 mW near-single-mode output | Not reported | Not reported | Five-micrometre variant: 27 GHz, 56 Gb/s eye under -6 dB feedback, 46 Gb/s over 500 m MMF and 48 Gb/s over 200 m nominal SMF; no direct BER count | Potential dense direct-source array path; this paper tests one device, not an array or package | Single-device laboratory demonstration |

## Why the headline numbers are not directly rankable

| Tempting comparison | Why it is invalid | Required matched evidence |
|---|---|---|
| Sumitomo 25% PCE versus Lumentum at least 10% PCE | Sumitomo does not state a fibre-coupled package boundary; Lumentum includes module and fibre coupling | Same ex-fibre power, wavelength, package, case and laser temperature, control power, spectral requirement and aging state |
| Lumentum 580-720 mW versus Nokia 3-5 dBm per channel | The external source is intended to be split among engines or channels; Nokia reports modulated per-channel output after on-PIC functions | Complete delivered-power tree from electrical input through source, splitters, couplers, modulator and fibre output |
| 16 mW VCSEL versus 27 GHz VCSEL | These are different aperture variants in `PAP-027` | One device and operating point meeting both power and bandwidth requirements |
| PAP-026 at 3.2 Tb/s versus a measured 3.2 Tb/s engine | Only one ELS wavelength and four splitter outputs were exercised sequentially; higher capacities multiply the result by unused ELS channels | Simultaneous eight-wavelength transmission with receiver BER, thermal operation and aggregate power |
| More than +20 dBm ELS input versus usable engine power | Prototype fan-out loses approximately 10.5-15 dB and needs a BDFA | Qualified splitter and connector loss distribution, without laboratory amplification, over temperature and life |

## Provisional architecture assessment

### Modeled external versus integrated boundary

`PAP-002` is a peer-reviewed architecture model, not a device or product benchmark. At its stated 53.125-Gbaud O-band assumptions, cooled external lasers have higher modeled source output than integrated lasers, but external-source designs encounter the finite fibre-attachment limit earlier. The resulting WDM, coupling and multiplexing losses produce modeled external-source link budgets 1-5 dB below integrated-source architectures in the relevant cases. The same model finds integrated sources can consume less *system* electrical power despite worse individual source efficiency because they avoid input coupling and can use more sources at lower operating power.[CLM-105][CLM-106]

This is a decisive diligence rule, not a 2026 product conclusion. Source efficiency, ex-fibre output and replaceability must be reconciled with attachment count, splitter/coupler loss, wavelength count, thermal environment, backup sources, PIC yield and field repair. The model's 70 C integrated-PIC case loses 2-4 dB of link budget and requires a backup source under the authors' assumed failure criterion; that is a reliability sensitivity, not a reported fleet failure rate.[CLM-107]

### High-power external InP source

The evidence supports technical feasibility, not scarcity rent. Lumentum has the strongest reviewed packaged ex-fibre result. Sumitomo demonstrates a potentially more efficient SOA-DFB device, but on a different boundary. At least two credible architectures and suppliers therefore exist before considering other public sources.

External placement can isolate heat and make laser replacement or redundancy more practical, but it moves risk into blind-mate connectors, splitters, distribution fibre, control and loss. `PAP-026` shows that this distribution penalty can be large enough to require an amplifier in a laboratory prototype.

### Monolithic InP transmitter source

The Nokia result integrates source, modulation, amplification and monitoring and therefore challenges an external-laser-only thesis. It can remove high-power fan-out interfaces, but full-engine yield may become more correlated and laser failure may impair a larger assembly. No reviewed source supplies a matched reliability or cost comparison.

### Directly modulated VCSEL source

The reviewed VCSEL is a real technical countercase for dense short-reach links, especially if source arrays can be packaged close to compute. It is not yet a matched alternative for the active 200G-per-lane O-band scale-out question: the paper demonstrates a single 850 nm device at 56 Gb/s eye rate, not an array, qualified engine or 200G lane.

## Investment read-through

1. High-power InP is likely necessary content for several silicon-photonics architectures, but the current papers do not prove a single-supplier bottleneck.
2. Supplier advantage must be evaluated on packaged ex-fibre efficiency, lifetime, qualified capacity and cost - not facet power alone.
3. Optical distribution can shift value toward connectors, splitters and packaging, but high loss can also destroy system efficiency and force amplification.
4. Integrated lasers trade serviceability for fewer high-power interfaces; the economic winner depends on failure correlation, rework and final-package yield.
5. VCSELs may create a separate short-reach profit pool rather than directly displacing O-band ELS in the first scale-out CPO deployments.
6. Fibre-attachment capacity can overturn a source-level ranking. External sources add a delivery boundary; an integrated source removes it but moves heat and failure correlation into the engine.

## Evidence required to rank suppliers

| Gate | Required evidence |
|---|---|
| Efficiency | Electrical input through packaged ex-fibre output, including TEC, control, redundancy and distribution loss |
| Reliability | FIT/AFR, accelerated aging, wear-out model, temperature cycling, optical-feedback tolerance and warranty allocation |
| Manufacturing | Wafer and final-package yield, test coverage, cycle time, rework, scrap and qualified capacity |
| Architecture | Lasers per system, split ratio, connector count, delivered engine-input power and redundancy strategy |
| Commercial | Named qualifications, repeat orders, volume, ASP, gross margin, second-source status and cancellation protection |
| Economics | Cost per delivered optical watt over warranted life and incremental gross profit after yield, warranty and capex |

## Current conclusion

The high-power InP ELS thesis remains plausible but must be weakened from **scarce proven profit pool** to **technically credible candidate profit pool**. Lumentum has strong packaged-device evidence, while Sumitomo demonstrates credible competing device performance. Polymer distribution and monolithic InP results show that source power cannot be separated from fan-out loss and engine integration. VCSELs remain a longer-term, shorter-reach countercase.

No reviewed paper establishes lifetime, high-volume yield, qualified capacity, cost, customer concentration or sustainable margin. Those variables, rather than the present device records, will determine profit capture.

## Sources

- `PAP-019`: Wenjia Zhou et al., [*High Power CW Laser for Co-Packaged Optics*](../01-sources/papers/PAP-019-zhou-high-power-cw-laser-cpo-2022.pdf), CLEO 2022 paper SS2D.3, DOI `10.1364/CLEO_SI.2022.SS2D.3`.
- `PAP-022`: Daisuke Inoue et al., [*High Power SOA-integrated DFB Lasers for Co-packaged Optics*](../01-sources/papers/PAP-022-inoue-soa-dfb-lasers-cpo-2025.pdf), JSAP-Optica Joint Symposia 2025 abstract 8p-N203-6.
- `PAP-026`: Satoshi Suda et al., [*High-Capacity Transmission with Single External Laser Source and Polymer-Based Splitters for Co-Packaged Optics*](../01-sources/papers/PAP-026-suda-external-laser-polymer-splitters-2024.pdf), CLEO 2024 paper SF3F.7.
- `PAP-027`: Cheng-Wei Lin et al., [*Single-Mode VCSELs With Zn-Diffusion Apertures for Applications in Co-Packaged Optics Systems*](../01-sources/papers/PAP-027-lin-single-mode-vcsel-cpo-2025.pdf), *IEEE Journal of Selected Topics in Quantum Electronics* 31(2), 2025, DOI `10.1109/JSTQE.2024.3454318`.
- `PAP-025`: S. Porto et al., [*1.6 Tb/s Monolithic InP Transmitter PIC with DFB, MZM, and SOA Arrays*](../01-sources/papers/PAP-025-porto-monolithic-inp-transmitter-pic-2026.pdf), OFC 2026 paper Th1C.4.
- `PAP-002`: Brandon Buscaino et al., [*External vs. Integrated Light Sources for Intra-Data Center Co-Packaged Optical Interfaces*](../01-sources/papers/PAP-002-buscaino-external-vs-integrated-light-sources-2021.pdf), *Journal of Lightwave Technology* 39(7), 2021, DOI `10.1109/JLT.2020.3043653`. Model assumptions and outputs; not a current product or supplier comparison.
