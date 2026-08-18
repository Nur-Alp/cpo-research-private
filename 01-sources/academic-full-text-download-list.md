# Academic full-text download list

**Owner:** Nur Alpys  
**Created:** 2026-08-10  
**Purpose:** Sources whose complete paper is not currently retained locally. Download the publisher PDF through university access, then place it in `01-sources/papers/` and tell me the filename so I can verify its contents and update the evidence ledger.

These are deliberately **not** papers that are already available in full locally. The existing abstract/evidence notes remain in the repository so the current claims are still traceable, but the claims must not be expanded beyond the stated abstract boundary until the full paper is reviewed.

The former 2026 SPIE 224G/lane FOWLP target is now fully retained as `PAP-056`; the 2026 Tran 180-GBaud target is fully retained as `PAP-051`; and the historical Meta/Broadcom test paper is fully retained as `PAP-055`. Their evidence notes separate measurements from modeled or commercial claims.

## Download status — 2026-08-10

Priority 1 is now complete: full PDFs for `PAP-028`, `PAP-029` and `PAP-044` were retrieved from Downloads, checked against their title pages and page structure, and integrated into the source notes and claim ledger. `PAP-032` remains inaccessible; the publisher page provides an abstract and presentation/video access path rather than a downloadable full paper.

`PAP-032` remains inaccessible (abstract/presentation record only). The user was unable to obtain the O’Brien full text through university access, so it is now classified as generally inaccessible for the present research cycle rather than an unresolved download action.

### Download status — 2026-08-10 update

`PAP-030` is now downloaded and verified as a complete 10-page PDF. It reports eight polymer-waveguide samples, PDL <0.5 dB, DGD <0.2 ps, PER >20 dB across CWDM4 wavelengths, +20 dBm input, six-hour stability without measurable degradation, and a 4.4 °C measured temperature rise. These results remain component-level and short-duration; they do not clear qualification or HVM economics gates. `PAP-048` remains intentionally untouched.

## Generally inaccessible evidence

Some remaining requests are not realistically obtainable from public downloads alone. Customer-accepted CPO SKU/unit counts, final-engine yield waterfalls, supplier transfer prices, warranty reserves, field-return distributions and realised CPO margins are generally private or only available through company filings, customer disclosures, supplier interviews or university/library access. The project will continue using bounded priors and explicit “not publicly disclosed” labels for these fields rather than treating them as silently missing or estimating them as facts.

## Priority 1 — highest value for the active 200G/400G optical-engine thesis

### PAP-051 — 180-GBaud PAM4 driver–modulator engine — completed

- **Why download:** Directly tests the 180-GBaud-to-400G/lane component boundary and driver/MZM co-design.
- **Citation:** Son Tran et al., “180 GBaud PAM4 Driver-Modulator Engine for IM/DD Transmissions in the O-Band,” OFC 2026, W3E.6.
- **DOI:** [10.1364/OFC.2026.W3E.6](https://doi.org/10.1364/OFC.2026.W3E.6)
- **Publisher record:** [Optica abstract](https://opg.optica.org/abstract.cfm?uri=OFC-2026-W3E.6)
- **Direct PDF button:** [Optica PDF endpoint](https://opg.optica.org/viewmedia.cfm?seq=0&uri=OFC-2026-W3E.6) (requires institutional/session access)
- **Current local status:** Full three-page PDF retained: [`PAP-051` evidence note](papers/PAP-051-tran-180gbaud-driver-modulator-engine-2026-evidence-note.md).
- **What remains open:** Fibre attach, reach, complete package/system power, yield, qualification, customer and economics.

### PAP-044 — TGV-interposer 400-Gbps optical engine

- **Why download:** Adds a measured 400-Gbps engine and a localized laser-replacement/serviceability boundary.
- **Citation:** Eun Kyu Kang et al., “Through-Glass-Via Interposer for High-Speed Electrical Interfacing in a 400 Gbps Optical Engine,” *Journal of Lightwave Technology* 43, 5390–5399 (2025).
- **DOI:** [10.1109/JLT.2025.3546984](https://doi.org/10.1109/JLT.2025.3546984)
- **Publisher record:** [Optica abstract](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-43-11-5390)
- **Direct PDF button:** [Optica PDF endpoint](https://opg.optica.org/jlt/viewmedia.cfm?seq=0&uri=jlt-43-11-5390) (requires institutional/session access)
- **Accessible mirror:** [ETRI/KSP record](https://ksp.etri.re.kr/ksp/article/read?id=70515)
- **Current local status:** Clearly labelled abstract snapshot and evidence note: [`PAP-044` note](papers/PAP-044-kang-tgv-400g-optical-engine-evidence-note.md)
- **Full paper would close:** Complete power and optical-reach boundary, sample count, BER/TDECQ/FEC details, replacement process, thermal/reliability results, yield and package economics.

### PAP-029 — 1.6-Tb/s FOWLP silicon-photonic engine

- **Why download:** Primary FOWLP engine paper; important countercase to TGV and conventional CPO packaging.
- **Citation:** Xin Li et al., “1.6 Tbps (224 Gbps/lambda) Silicon Photonic Engine Fabricated with Advanced Electronic-Photonic FOWLP for Co-Packaged Optics and Linear Drive Applications,” OFC 2024, Tu3A.2.
- **DOI:** [10.1364/OFC.2024.Tu3A.2](https://doi.org/10.1364/OFC.2024.Tu3A.2)
- **Publisher record:** [Optica abstract](https://opg.optica.org/abstract.cfm?uri=ofc-2024-Tu3A.2)
- **Current local status:** Full 3-page PDF downloaded and reviewed: [`PAP-029` evidence note](papers/PAP-029-li-fowlp-silicon-photonic-engine-2024-evidence-note.md).
- **Full paper would close:** Fabrication flow, optical/electrical test boundary, wafer/package yield, direct-drive performance, thermal/reflow behavior, cycle time and evidence behind the volume-manufacturing claim.

### PAP-028 — detachable optical chiplet connector

- **Why download:** Relevant to known-good optical-engine testing, detachable serviceability and fibre-attach economics.
- **Citation:** “Detachable Optical Chiplet Connector for Co-Packaged Photonics,” *Journal of Lightwave Technology* 41(19), 6315 (2023).
- **DOI:** [10.1109/JLT.2023.3285149](https://doi.org/10.1109/JLT.2023.3285149)
- **Publisher record:** [Optica abstract](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-41-19-6315)
- **Direct PDF button:** [Optica PDF endpoint](https://opg.optica.org/jlt/viewmedia.cfm?seq=0&uri=jlt-41-19-6315) (requires institutional/session access)
- **Current local status:** Full 9-page PDF downloaded and reviewed: [`PAP-028` evidence note](papers/PAP-028-psaila-detachable-optical-chiplet-connector-2023-evidence-note.md).
- **Full paper would close:** Connector geometry, alignment tolerances, mating/replacement cycles, loss distribution, environmental testing, assembly time and service economics.

## Priority 2 — packaging, reliability and manufacturing evidence

### PAP-048 — high-density TSV/TGV CPO interposers

- **Why download:** Compares TSV and TGV interposer bandwidth and proposed 112-GBaud optical-engine architectures.
- **Citation:** Chang Ge et al., “High-density co-packaged optics based on TSV and TGV interposers for advanced optical interconnection,” *Advanced Photonics Nexus* 5(3), 036019 (2026).
- **DOI:** [10.1117/1.APN.5.3.036019](https://doi.org/10.1117/1.APN.5.3.036019)
- **Publisher record:** [SPIE full record](https://www.spiedigitallibrary.org/journals/advanced-photonics-nexus/volume-5/issue-03/036019/High-density-co-packaged-optics-based-on-TSV-and-TGV-interposers/10.1117/1.APN.5.3.036019.full)
- **Current local status:** Abstract/evidence note only: [`PAP-048` note](papers/PAP-048-ge-tsv-tgv-high-density-cpo-2026-evidence-note.md)
- **Full paper would close:** Fabrication details, complete eye/BER/TDECQ boundary, optical coupling, thermal behavior, process capability, yield and 112-GBaud engine integration evidence.

### PAP-030 — polymer-waveguide stability and reliability

- **Why download:** Directly informs polymer-waveguide lifetime, thermal stability and packaging reliability.
- **Citation:** Satoshi Suda et al., “High-Power Stability and Reliability of Polymer Optical Waveguide for Co-Packaged Optics,” *Journal of Lightwave Technology* 43(10), 4903 (2025).
- **DOI:** [10.1109/JLT.2025.3543339](https://doi.org/10.1109/JLT.2025.3543339)
- **Publisher record:** [Optica abstract](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-43-10-4903)
- **Direct PDF button:** [Optica PDF endpoint](https://opg.optica.org/jlt/viewmedia.cfm?seq=0&uri=jlt-43-10-4903) (open-access article; publisher bot protection may still intervene)
- **Current local status:** Full 10-page PDF downloaded and reviewed: [`PAP-030` evidence note](papers/PAP-030-suda-polymer-waveguide-reliability-2025-evidence-note.md).
- **Full paper would close:** Optical-power stress conditions, duration, temperature/humidity, degradation distributions, sample counts, failure criteria and whether the result supports CPO qualification.

### PAP-041 — IBM single-mode polymer-waveguide CPO module

- **Why download:** Full-module process and thermomechanical reliability evidence for an optics-last/serviceable packaging route.
- **Citation:** Akihiro Horibe et al., “Co-packaged optics module with single-mode polymer waveguide,” IEDM 2025.
- **Publisher record:** [IBM Research publication page](https://research.ibm.com/publications/co-packaged-optics-module-with-single-mode-polymer-waveguide)
- **Current local status:** Official abstract/evidence note only: [`PAP-041` note](papers/PAP-041-ibm-single-mode-polymer-waveguide-iedm2025.md)
- **Full paper would close:** Sample counts, channel-loss distributions, stress duration and pass/fail statistics, substrate/assembly details, yield and qualification evidence.

## Priority 3 — broader architecture and pilot-manufacturing context

### PAP-032 — photonic/electronic co-packaging from research to pilot manufacturing — inaccessible for now

- **Why download:** Useful pilot-manufacturing and scale-up context for moving photonic packages from laboratory demonstrations toward production.
- **Citation:** Peter O’Brien and Das Kumar, “Photonic and Electronic Co-Packaging Technologies — From Research to Pilot Manufacturing,” OFC 2025, W4A.1.
- **DOI:** [10.1364/OFC.2025.W4A.1](https://doi.org/10.1364/OFC.2025.W4A.1)
- **Publisher record:** [Optica abstract](https://opg.optica.org/abstract.cfm?uri=OFC-2025-W4A.1)
- **Current local status:** Abstract retained; Optica explicitly marks the full-text article unavailable and points to a presentation/video. A ResearchGate record and OFC 2025 archive/session guide corroborate the citation, but neither provides the technical presentation. University access did not yield the full paper. Treat it as generally inaccessible for the current cycle; no evidence upgrade is justified.
- **Full presentation would close:** Pilot-line process steps, equipment, panel/wafer flow, design rules, throughput, process-control metrics and manufacturing readiness claims.

## Download and handoff procedure

1. Open the DOI or publisher record while signed in through the university library/VPN.
2. Download the **publisher PDF**, not a browser print or abstract-page snapshot.
3. Preserve the original filename temporarily in Downloads.
4. Send or move the PDF into `01-sources/papers/` without renaming it first if possible.
5. I will inspect the title page, authors, page count, figures, tables and measured boundaries, then create/update the evidence note and claim ledger.

Do not treat an abstract, search-result PDF, browser print, presentation screenshot or filename as equivalent to the full paper. If the university cannot retrieve a source, retain the DOI/URL and access limitation rather than upgrading the evidence class.
