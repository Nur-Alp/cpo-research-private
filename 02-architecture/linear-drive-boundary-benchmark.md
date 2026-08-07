# Linear-Drive Optics Boundary Benchmark

**Owner:** Nur Alpys
**Status:** Reviewed academic evidence; not a deployment forecast
**As of:** 2026-08-07

## Decision question

At 100G, 200G and 400G per lane, when does linear-drive optics keep a pluggable architecture technically credible, and when does the electrical path instead favour near-packaged optics (NPO) or CPO?

## Executive result

**FACT:** 100G-per-lane LPO has direct system evidence: Meta reported a 51.2T switch experiment across two preliminary LPO designs, with chip-to-module losses as high as 15 dB at 26 GHz, most tested port/module combinations reaching a 1e-9 BER floor, and one design degrading as high as 1e-7.[PAP-007]

**INFERENCE:** 200G-per-lane LPO is technically conditional, not yet commercially proven by the reviewed papers. Meta's 200G analysis required roughly 22 dB channel loss for receiver sensitivity and less than 23 dB for its stated transmitter-quality limits; its planned 30 dB cabled switch path required a transmitter retimer. Hisense and Semtech respectively model 31 dB and 26 dB paths, but with materially different transmitter, equalisation, return-loss, FEC and model assumptions.[PAP-007][PAP-008][PAP-010] These are not interchangeable loss limits or a resolved reliability ranking.

**FACT:** The reviewed 400G/lane paper directly measures component behaviour at 160 and 180 GBd PAM4, not a 212.5 GBd end-to-end 400G/lane link. Its 212.5 GBd result is a model in which TDECQ below 3.5 dB and BER floor below 1e-6 hold only up to 12 dB back-to-back loss at 106 GHz; the 15 dB case fails those targets.[PAP-011]

The current evidence therefore supports a boundary view: LPO can defer CPO in a validated low-loss 100G and potentially 200G channel, while 400G/lane currently pulls the electrical boundary inward toward NPO/CPO. It does not establish adoption dates, full-system power, production yield, serviceability or which architecture will be more profitable.

## Standards anchor: useful, but not a 400G/lane answer

The OIF CEI-224G framework places the relevant topology boundary in physical terms: typically under 50 mm from die to an optical engine in an MCM/CPO package, under 150 mm for a nearby OE, and potentially over 200 mm of host trace plus a connector for a faceplate module. It also explicitly lists linear chip-to-OE interfaces as a possible path for CPO, NPO and VSR, and marks the historical 224G insertion-loss and pre-FEC BER entries as **TBD**.[STD-007][CLM-201][CLM-202][CLM-203]

IEEE P802.3dj provides a standards-level 200G/lane anchor: the task force recorded a die-to-die insertion-loss objective of ≤40 dB at 53.125 GHz for the listed 200G/lane copper/backplane PHYs. That value has different endpoints and test context from the 106 GHz, 212.5-GBd model in `PAP-011`, so it cannot be used as a 400G/lane LPO limit.[STD-008][CLM-204]

The practical conclusion is narrower than “the standard forces CPO”: standards work confirms that the electrical boundary is being formalized around 200G/lane, while the reviewed public material does not yet provide an adopted 400G/lane channel budget. The 400G gate therefore remains an end-to-end measurement question, not a settled standards number.[CLM-205]

The newer IEEE 400GPL objectives make the boundary more concrete without changing that conclusion. They include optional single-lane 400G attachment-unit interfaces for both chip-to-module and chip-to-chip use, plus objectives for 500 m single-mode fibre and 1 m twin-axial copper. Because the AUI is optional and the document supplies no insertion-loss, FEC or measured-link result, it preserves implementation optionality rather than selecting LPO, NPO or CPO.[STD-009][CLM-206][CLM-207][CLM-208][CLM-209]

An IEEE 400GPL contribution from China Mobile adds a useful mechanism-level constraint: at 400G/lane, its PAM4 example is approximately 212.5 GBaud with a 106.25 GHz Nyquist frequency, and it notes that removing a retimer requires rate/modulation alignment and changes where FEC functions can be hosted.[STD-010][CLM-259][CLM-260][CLM-261] This strengthens the reason to test NPO/CPO at a shortened electrical boundary, but it is not a measured link or an adopted standard. The contribution's 2027–2029 deployment language remains a diligence lead only.[CLM-262]

## Comparison rules

Do not compare a headline loss number without matching all of the following:

1. Measured result versus simulation or estimate.
2. Gross lane rate, FEC, pre-FEC target and BER measurement boundary.
3. Back-to-back loss frequency and the exact endpoints included in that channel.
4. Equalisation, retiming and DSP placement in the host and module.
5. Modulator technology, bandwidth, drive swing, laser and receiver assumptions.
6. Return-loss, crosstalk, reach, temperature and multi-vendor/interoperability conditions.
7. Power boundary: module-only, host plus module, or a complete system.

## Evidence ladder

| Paper | Architecture and evidence class | Directly established | Important limitation |
|---|---|---|---|
| `PAP-007` | Meta; 100G measured in a 51.2T switch; 200G simulation | 100G LPO could operate across up to 15 dB at 26 GHz, with most combinations at a 1e-9 BER floor and one at up to 1e-7 | The 200G result is not a measured switch link; its 22/23 dB boundary is model-specific |
| `PAP-008` | Hisense; 200G VPI simulation | TFLN-plus-CTLE model reaches 31 dB at 56 GHz with stated 2.1 dB TDECQ and model-limited BER below 1e-6 | No measured link; SiP result remains poorer and internally inconsistent between text and conclusion |
| `PAP-010` | Semtech; 200G design synthesis and simulation | Model reaches 26 dB die-to-die under stated host equalisation and better-than-10 dB return loss | Less-than-10 W 1.6T LPO is an internal simulation/estimate; no matched 200G production-system proof |
| `PAP-011` | Ligent; 400G component measurement and simulation | 160/180 GBd component results measured; 212.5 GBd model needs no more than 12 dB B2B loss | No measured 212.5 GBd or end-to-end 400G/lane link |

## 200G/lane: reconciling the loss numbers

| Source | Stated loss result | Conditions that prevent direct ranking | Appropriate use |
|---|---:|---|---|
| Meta `PAP-007` | About 22 dB for receiver sensitivity; less than 23 dB for transmitter metrics; planned cabled path about 30 dB | 113 GBd PAM4, concatenated KP4/Hamming FEC, 500 m CWDM4 model; 30 dB includes cable-routed switch path | Conservative architecture trigger: a conventional long electrical path may need retiming or move optics inward |
| Hisense `PAP-008` | 31 dB at 56 GHz in its TFLN model | 112 GBd PAM4; 90 GHz TFLN MZM; 84 GHz/15 dB-peaked transmitter; enhanced CTLE and specific host receiver model | Technology countercase: aggressive TFLN/equalisation may enlarge the linear-drive envelope, pending measurement |
| Semtech `PAP-010` | 26 dB die-to-die model | 106.25 GBd PAM4; -10 dB return loss; stated 60-70 GHz blocks and host FFE/DFE | Design-method reference, not a field or multi-vendor qualification result |

The 22/23, 26 and 31 dB figures answer different questions under different channels. They must not be averaged, used as a universal LPO reach rule, or interpreted as proof that one vendor's 200G architecture is commercially superior.

## 400G/lane: measured boundary versus projection

| Result | Status | Key outcome | Architecture implication |
|---|---|---|---|
| 160 GBd PAM4 with KP4 FEC | Measured | 3.7 dB TDECQ with 15-tap FFE | Useful component evidence, below a 400G/lane gross-rate requirement |
| 180 GBd PAM4 with KP4 plus Hamming FEC | Measured | 1.9 dB TDECQ at 180 GBd with 23-tap FFE plus one DFE; degradation above 180 GBd attributed to AWG RF loss | Electrical/package bandwidth remains a practical limiting mechanism |
| 212.5 GBd PAM4/KP4 | Simulated | At 106 GHz, up to 12 dB B2B loss meets the paper's TDECQ and BER-floor targets; 15 dB does not | Supports a shortened NPO/CPO electrical path; it does not demonstrate conventional 400G LPO |

## Architecture triggers to test

| Lane generation | Current technical read | Provisional architecture implication | Evidence still required |
|---|---|---|---|
| 100G | LPO system operation measured, with non-uniform BER-floor outcome across preliminary designs | LPO is credible where channel and interoperability are validated | Field reliability, module power, service rate and multi-vendor qualification |
| 200G | Multiple models indicate possible operation, but their loss envelopes are unmatched; Meta's long channel needs a Tx retimer | LPO may coexist with retimed pluggables and NPO/CPO by electrical topology | Matched multi-vendor 102.4T system, full channel and return-loss data, power, temperature and error statistics |
| 400G | Component evidence is below the modeled gross rate; modeled 212.5 GBd margin collapses above 12 dB B2B loss; IEEE 400GPL discussion places PAM4 Nyquist near 106.25 GHz and highlights rate/FEC alignment without a retimer | NPO/CPO is the stronger current technical direction; traditional LPO remains unproven | Measured 212.5 GBd/400G link, fibre reach, thermal, BER distribution, yield and serviceability |

OIF-EEI-112G-RTLR-01.0 supplies a standards-level comparator that should be kept separate from unretimed LPO: it combines a retimed transmitter with a linear receiver, supports 53.125 GSym/s PAM4 and 200G/400G/800G host IDs, and allocates 11.9 dB of the recommended 16 dB ball-to-ball budget to host PCB/cable losses while preserving hot plug and module interoperability.[CLM-297][CLM-298][CLM-299][CLM-300] This does not establish a power or cost win, but it prevents the CPO thesis from treating every 200G/lane electrical reach problem as a binary CPO-versus-pluggable choice.

OIF's OFC 2026 showcase further indicates that the ecosystem is advancing CEI-224G/448G, RTLR, unretimed linear optics, co-packaging, CMIS and ELSFP in parallel. This is evidence of interoperability activity, not evidence that one path has won on production cost or field reliability.[CLM-301][CLM-302][CLM-303]

## Investment implication

LPO is a real countercase to any thesis that power alone forces switch CPO. The relevant bottleneck moves with the electrical channel: packaging, host-SerDes, connector and module placement determine whether linear pluggables can retain sufficient margin. This makes 200G/lane a coexistence problem rather than a binary CPO-versus-pluggable decision.

At 400G/lane, the present evidence shifts the diligence focus to short electrical interconnect, high-bandwidth drivers/modulators, packaging and test. That could favour NPO/CPO engine suppliers, but no reviewed paper yet shows their production economics or proves that the additional integration creates superior investor returns.

## Sources

- `PAP-007`: Elaine S. Chou et al., [*100G and 200G per Lane Linear Drive Optics for Data Center Applications*](../01-sources/papers/PAP-007-chou-linear-drive-optics-100g-200g-2024.pdf), OFC 2024 paper W4H.3, DOI 10.1364/OFC.2024.W4H.3.
- `PAP-008`: Jianying Zhou, Lei Xin and Jin Hong, [*Performance Limitations and Optimizations of Linear Driver Optics for 200G/Lane and beyond*](../01-sources/papers/PAP-008-zhou-linear-driver-optics-200g-2025.pdf), OFC 2025 paper M2H.1, DOI 10.1364/OFC.2025.M2H.1.
- `PAP-010`: E. M. Kimber and E. Frlan, [*200G LPO: Design Challenges and Latest Test Data*](../01-sources/papers/PAP-010-kimber-frlan-200g-lpo-2026.pdf), OFC 2026 paper M2B.1, DOI 10.1364/OFC.2026.M2B.1.
- `PAP-011`: Jianying Zhou et al., [*400G/lane for Linear-drive Optics Applications*](../01-sources/papers/PAP-011-zhou-400g-linear-drive-optics-2026.pdf), OFC 2026 paper Th1C.3, DOI 10.1364/OFC.2026.Th1C.3.
- `STD-007`: OIF, [*Next Generation CEI-224G Framework*](../01-sources/standards/STD-007-oif-cei-224g-framework.pdf), OIF-FD-CEI-224G-01.0, 7 February 2022.
- `STD-008`: IEEE P802.3dj, [*Key Motions*](../01-sources/standards/STD-008-ieee-p8023dj-key-motions-2024.pdf), compilation through 16 May 2024.
- `STD-009`: IEEE 802.3 400GPL Study Group, [*400GPL SG Objectives*](../01-sources/standards/STD-009-ieee-400gpl-objectives-2026.pdf), approved 10 June 2026; project status updated July/August 2026.
- `STD-010`: China Mobile, [*Consideration on NPO and CPO at 400G/Lane*](../01-sources/standards/STD-010-ieee-400gpl-npo-cpo-consideration-2026.md), IEEE 802.3 400GPL public contribution, May 2026.
