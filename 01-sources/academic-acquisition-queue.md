# Academic acquisition queue

**Owner:** Nur Alpys  
**As of:** 2026-08-12  
**Purpose:** Identify only the academic evidence that can change the CPO optical-engine/PIC investment thesis. This is a diligence queue, not a list of papers to collect indiscriminately.

## Do we need more papers?

Yes, but the current library is already sufficient for the technical framing. More papers are needed mainly to close five decision-critical gaps: matched 200G/400G system comparisons, final-engine yield and rework, reliability/serviceability, laser architecture economics, and accelerator-side optical-I/O benchmarking. Academic papers can establish physical limits and measured demonstrations; they will not substitute for customer qualification, supplier contracts, field-failure data, or public-company financial disclosure.

## Priority queue

### Commercial-proof source requiring university access — 2026-08-12

| Priority | Evidence needed | Target paper/source | Why it matters | Current status |
|---|---|---|---|---|
| Completed | Historical Meta/Broadcom CPO test configuration: switch generation, population, stress condition, elapsed time, comparators and service boundary | Siamak Amiralizadeh *et al.*, “Co-Packaged Optics Technology Evaluation for Hyperscale Data Center Fabric Switches,” ECOC 2025, pp. 1–4, DOI [10.1109/ECOC66593.2025.11263202](https://doi.org/10.1109/ECOC66593.2025.11263202) | It defines the historical TH5/Bailly system-test boundary and prevents it being overstated as TH6 deployment or field reliability. | Full four-page PDF retained as `PAP-055` and claims `CLM-574`–`CLM-577` added. It establishes a bounded >1m port-device-hour laboratory/system test, not customer procurement, accepted units, repeat shipments, field returns or TH6 economics. |

### Newly identified high-value targets — 2026-08-10

| Priority | Evidence needed | Target paper/source | Why it matters | Current status |
|---|---|---|---|---|
| Completed | 224G/lane FOWLP engine process and test boundary | Jia Qi Wu et al., “Cost-effective, high-performance heterogeneous integration for 6.4T and beyond 224Gbps/lane co-packaged-optical engines for AI/ML and data center,” SPIE 13905 (2026), DOI [10.1117/12.3085221](https://doi.org/10.1117/12.3085221) | Directly updates the FOWLP countercase with 2026 1.6T package measurements and a 6.4T/224G-lane design claim | Full eight-page PDF retained as `PAP-056`; claims `CLM-578`–`CLM-581` distinguish measured 1.6T package/interconnect evidence from modeled 6.4T/12.8T scale-up. |
| Completed | Measured 400G/lane LPO/NPO/CPO boundary | Jianying Zhou et al., “400G/lane for Linear-drive Optics Applications,” OFC 2026 Th1C.3, DOI [10.1364/OFC.2026.Th1C.3](https://doi.org/10.1364/OFC.2026.Th1C.3) | A direct 400G/lane LPO/NPO/CPO comparator materially constrains the electrical reach case | Full three-page PDF retained as `PAP-011`; measured 160/180-GBd results and modeled 212.5-GBd boundary are integrated. The 400G/lane link itself remains modeled, not measured. |

| Priority | Evidence needed | Target paper/source | Why it matters | Current status |
|---|---|---|---|---|
| Completed | 400G/lane measured driver/modulator boundary | Tran et al., “180 GBaud PAM4 Driver-Modulator Engine for IM/DD Transmissions in the O-Band,” OFC 2026 W3E.6, DOI 10.1364/OFC.2026.W3E.6 | Tests whether the driver/modulator/engine chain is approaching the later 400G/lane requirement | Full three-page PDF retained as `PAP-051`; claims `CLM-461`–`CLM-463` and `CLM-582`–`CLM-584` add measured BER, thermal condition and partial-power boundary. It is still not a fibre-attached or reach-qualified engine. |
| P0 | Matched CPO/LPO/NPO system comparison | New conference or journal measurement with the same host ASIC, lane rate, reach, FEC, temperature and power boundary | Prevents vendor power claims from being compared across incompatible denominators | Not found; highest-value search |
| Inaccessible for now | Production packaging and final-engine yield | O’Brien, “Photonic and Electronic Co-Packaging Technologies—From Research to Pilot Manufacturing,” OFC 2025 W4A.1, DOI [10.1364/OFC.2025.W4A.1](https://doi.org/10.1364/OFC.2025.W4A.1) | Links packaging route selection to pilot-line throughput, test and yield | The user could not obtain the full record through university access. Retain `PAP-032` as abstract-only and treat the full paper/presentation as generally inaccessible for now. It cannot clear the final-engine yield, throughput, qualification or economics gate. |
| P0 | Detachable fibre/known-good optical module economics | Psaila et al., “Detachable Optical Chiplet Connector for Co-Packaged Photonics,” JLT 41 (2023), 6315–6323 | Directly tests rework, serviceability and yield-compounding counterarguments to permanent fibre attach | Full 9-page PDF retained; claims `CLM-495`–`CLM-499`; still lacks production-lot economics |
| P0 | High-volume FOWLP engine | Li et al., “1.6 Tbps FOWLP-Based Silicon Photonic Engine for Co-Packaged Optics,” JLT 43 (2025), 1979–1986 | Provides a cost/yield countercase to TSV/TGV and helps identify the packaging control point | Full 3-page PDF retained; claims `CLM-500`–`CLM-503`; still lacks HVM yield and cost |
| P1 | Thermal drift and control burden | Chung, “Predictive Software Scheduling as an Early-Warning Hint Layer for Optical Engine Thermal Drift in Heterogeneous SoIC Packaging,” arXiv:2605.18612 | Quantifies whether thermal control can be managed in an integrated package | Full PDF retained as `PAP-050`; low-confidence, unreviewed preprint; seek independent/peer-reviewed corroboration |
| P1 | TSV/TGV route and high-density interposer trade-offs | Gao et al., “Heterogeneous Integration Technology Drives the Evolution of Co-Packaged Optics,” Micromachines 16 (2025), 1037 | Synthesizes route, thermal, reliability and maintainability trade-offs | Full PDF retained as `PAP-049`; review synthesis, not production data |
| Completed | External versus integrated laser link budget and reliability | Buscaino et al., “External vs. Integrated Light Sources for Intra-Data Center Co-Packaged Optical Interfaces,” JLT 39 (2021), 1984–1996 | Directly informs the laser architecture that may retain pricing power and serviceability | Full 13-page `PAP-002` PDF retained and reviewed; it remains a 2021 model, not current production evidence. |
| P1 | Polymer waveguide and detachable connector reliability | Suda et al., “High-Power Stability and Reliability of Polymer Optical Waveguide for Co-Packaged Optics,” JLT 43 (2025), 4903–4912 | Tests whether polymer waveguides can meet lifetime and thermal requirements | Full 10-page PDF retained; claims `CLM-509`–`CLM-513`; six-hour test remains short of qualification |
| P1 | Glass interposer thermal/electrical boundary | Gupta et al., “Thermal and Electrical Study of Glass Interposers in Co-Packaged Electronic-Photonic Systems,” IEEE TCPMT 15 (2025), 1625–1635 | Separates glass-interposer benefits from generic CPO claims | Existing `PAP-031` author-hosted PDF |
| P1 | Accelerator optical-I/O versus copper | Peer-reviewed Ayar Labs, Lightmatter, Celestial AI/Marvell or TSMC COUPE measurements with package, thermal and link denominators | Determines whether the highest-value profit pool sits beside the switch rather than in switch CPO | Major gap; search IEEE/JLT/OFC and university repositories |
| Completed | 400G/lane pluggable/PIC counterweight | Ogiso et al., “Uncooled O-band InP MZ Modulator PIC for 3.2 Tb/s (400 Gb/s/lane) Pluggable Transceiver,” OFC 2025 Th4D.1 | Tests whether a TEC-less InP PIC can defer CPO at the 400G/lane boundary | Full three-page PDF retained as `PAP-053`; remaining request is matched module power, yield, qualification and economics |
| P1 | 225-GBaud advanced-pluggable system boundary | St-Arnault et al., “Net 3.2 Tbps 225 Gbaud PAM4 O-Band IM/DD 2 km Transmission Using FR8 and DR8 with a CMOS 3 nm SerDes and TFLN Modulators,” arXiv:2503.24147 | Provides a measured 3.36-Tb/s/2-km counterexample that tests whether CPO is necessary at 400G-class lanes | Full 8-page PDF retained as `PAP-054`; still lacks production yield, chassis power, qualification and economics |
| P1 | TGV package loss and active-chip integration | Ge et al., “High-speed wafer-level TGV interposer for 2.5D CPO,” *Optics Communications* 579 (2025), 131517 | Tests whether a technically fast TGV interposer survives the EML/fibre coupling and assembly boundary | Full 7-page PDF now retained as `PAP-046`; coupling-loss and complete-engine qualification remain open |
| P2 | Fibre attach process capability | Peer-reviewed edge-coupler/fibre-attach studies reporting loss distribution, cycle time, Cpk, rework and thermal cycling | Converts attach from a qualitative risk into a manufacturing cost/yield input | Current papers establish mechanisms but not factory Cpk; targeted search needed |
| P2 | Field reliability and service | Long-duration, accelerated-life or field-return studies for CPO optical engines | Needed for warranty, MTTR and serviceability economics | No adequate public study located |

## Acquisition rules

1. Download and retain a local PDF whenever the full text is legally available through open access or university access.
2. If only an abstract or publisher page is available, retain an evidence note with the canonical DOI/URL and label the evidence boundary explicitly.
3. Do not treat a review article as new production evidence; use it to locate primary measurements.
4. Every retained item must be added to `source-log.csv`, mapped in `academic-evidence-matrix.md`, and linked to claims in `claim-ledger.csv`.
5. Stop expanding the academic queue once each P0 gap has either a measured source or an explicit “not publicly available” finding. At that point, primary interviews, filings and customer evidence have higher marginal value than more papers.
