# Sources

This directory contains the research source index, reading sequence, and any legitimately retained source material or original notes.

## Canonical index

`source-log.csv` is the canonical source database. Each row records one item and distinguishes bibliographic metadata from unverified claims, limitations, relevance, and review status.

`claim-ledger.csv` is the canonical assertion database. Add only thesis-relevant claims and label each as fact, company claim, estimate, inference, opinion, or unknown. Every material adoption, timing, leadership, or financial conclusion should be traceable to this ledger.

`../03-components/optical-engine-benchmark.md` is the working matched-boundary comparison for scale-out optical engines. It distinguishes measured device results from full-engine validation, qualification and commercial production.

`source-gap-audit-2026-08-06.md` is the current evidence-coverage and company-leadership audit. It separates provisional category leaders from the evidence still needed to name a durable overall winner, and contains the university-download queue.

`source-viewing-guide.md` is the reading index for publisher pages retained as HTML. It links each readable local PDF snapshot and its canonical publisher URL. Cite the publisher URL; use the PDF snapshot for local reading.

The new workflow fields are:

- `priority`: orientation, priority one, priority two, or supplementary
- `sequence`: order within that priority group
- `review_mode`: listen, watch carefully, read, or read carefully
- `review_status`: queued, in progress, reviewed, or archived

Do not mark confidence until the material has been reviewed. Important claims should be checked against standards, filings, official documentation, papers, or other primary evidence.

## Source types

- `papers/`: peer-reviewed papers and conference proceedings
- `standards/`: standards documents and implementation agreements
- `filings/`: company filings and official financial disclosures
- `product-materials/`: official product documentation and vendor presentations
- `conference-presentations/`: conference decks and market-analysis presentations
- `videos/`: original notes from video or audio material
- `newsletters/`: original notes from newsletters, industry analysis, and conference recaps

Store links and metadata in the source log. Do not copy full copyrighted articles, transcripts, or videos into the repository unless storage and sharing rights are clear.

## Recommended sequence

### Orientation

1. **Listen:** [From Fiber to AI: A Laser Giant's Rebirth](https://www.youtube.com/watch?v=6GlyVh4BaCc). Можно слушать как подкаст в дороге.
2. **Watch carefully:** [The AI Bandwidth Wall & Co-Packaged Optics](https://www.youtube.com/watch?v=G5r2OyCN5_s).
3. **Watch carefully:** [Why next-gen AI scale-up needs CPO](https://www.youtube.com/watch?v=-HppUFVl-Ak).
4. **Workflow task:** Install the Substack application if it is useful for maintaining the reading queue.

### Priority one

Read these in order because the sequence helps show how the industry discussion developed:

1. [Optical Illusions](https://irrationalanalysis.substack.com/p/optical-illusions-fn-cien-sitm-lite)
2. [OCP Global Summit 2025: Irrational Recap](https://irrationalanalysis.substack.com/p/ocp-global-summit-2025-irrational)
3. [Practical Optical Communication Systems](https://irrationalanalysis.substack.com/p/practical-optical-communication-systems)
4. [OFC 2026 Irrational Recap](https://irrationalanalysis.substack.com/p/ofc-2026-irrational-recap)

These are the highest-priority posts in the supplied list. Work through difficult technical sections with textbooks, standards, primary papers, or careful AI-assisted explanation rather than accepting every claim at face value.

### Priority two

1. [2/26 Earnings Roundup: LITE, COHR, SITM, QCOM, ARM](https://irrationalanalysis.substack.com/p/226-earnings-roundup-lite-cohr-sitm)
2. [ISSCC 2026 Irrational Recap](https://irrationalanalysis.substack.com/p/isscc-2026-irrational-recap)
3. [Citrini 3/12/2026 Optics Basket Comments](https://irrationalanalysis.substack.com/p/citrini-3122026-optics-basket-comments)
4. [5/8/26 Earnings Roundup](https://irrationalanalysis.substack.com/p/5826-earnings-roundup-on-fn-lite)

### Supplementary SemiAnalysis material

1. [Co Packaged Optics: Scaling with Light for the Next Wave of Interconnect](https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling)
2. [GTC 2026: The Inference Kingdom Expands](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands)

Use these for CPO architecture, AI networking, NVIDIA platform context, and further diligence questions. Verify commercial status, roadmaps, performance claims, and investment conclusions using primary sources.

### Conference presentations

1. `PRS-001`: Yole Group, *Status of High-End Performance Packaging (2.5D & 3D) and Co-packaged Optics*, presented by Vishal Saroha at the SEMI 3D & Systems Summit, 2025.

Use conference decks for orientation, market framing, and diligence questions. Treat market forecasts and third-party estimates cautiously, record their definitions, and reconcile them against physical unit assumptions where possible.

### Academic core

Read the locally retained papers in this order:

1. `PAP-003`: Ravi Mahajan et al., *Co-Packaged Photonics For High Performance Computing: Status, Challenges And Opportunities* (2022). Use its switch case study to establish the packaging, socketability, thermal, test, yield, and high-volume manufacturing framework.
2. `PAP-001`: Min Tan et al., *Co-packaged optics (CPO): status, challenges, and solutions* (2023). Use it to map CPO and NPO architectures, integration approaches, thermal constraints, packaging, and standardisation.
3. `PAP-002`: Brandon Buscaino et al., *External vs. Integrated Light Sources for Intra-Data Center Co-Packaged Optical Interfaces* (2021). Extract the 102.4T architecture assumptions, laser-placement trade-offs, temperature effects, reliability assumptions, fibre count, and optical link budgets.

### Broader investment case

Read these after the academic core:

1. `PAP-006`: Pavlos Maniotis and Daniel M. Kuchta, *Exploring the benefits of using co-packaged optics in data center and AI supercomputer networks* (2024). Test whether CPO can create system value through higher radix, fewer switches, network locality, and throughput rather than through optical-module power alone.
2. `PAP-005`: Benjamin G. Lee et al., *Beyond CPO: A Motivation and Approach for Bringing Optics Onto the Silicon Interposer* (2023). Map the possible migration from package-adjacent optics to interposer-level optical I/O and the resulting changes in suppliers, packaging, and thermal design.
3. `PAP-004`: Lucas Yeary et al., *Co-packaged Optics on Glass Substrates for 102.4 Tb/s Data Center Switches* (2023). Evaluate glass substrates as a manufacturable and potentially lower-cost integration path, separating proposed architecture from demonstrated performance.

### Linear-drive comparators

- `PAP-007`: Elaine Chou et al., *100G and 200G per Lane Linear Drive Optics for Data Center Applications*, OFC 2024, paper W4H.3.
- `PAP-008`: Jianying Zhou et al., *Performance Limitations and Optimizations of Linear Driver Optics for 200G/Lane and beyond*, OFC 2025, paper M2H.1.
- `PAP-010`: E. M. Kimber and E. Frlan, *200G LPO: Design Challenges and Latest Test Data*, OFC 2026.
- `PAP-011`: Jianying Zhou et al., *400G/lane for Linear-drive Optics Applications*, OFC 2026. This is a one-page digest, so weight it below full papers.

All four local files were checked against their contents rather than filenames. They are queued for analytical review; acquisition does not mean their claims have been accepted.

### Focused PIC, packaging, and profit-pool expansion

The verified `PAP-012` through `PAP-027` packet covers electronic-photonic co-optimisation, optical-I/O chiplets, interposers, fibre attach, thermomechanical reliability, detachable connectors, external lasers, switch-radix economics, microring and InP PICs, VCSELs, design tools, and CMOS/silicon-photonics integration. Prioritise:

1. `PAP-024` for the current device and integration map.
2. `PAP-012`, `PAP-021`, `PAP-025`, and `PAP-013` for scale-out optical-engine and PIC design.
3. `PAP-015`, `PAP-016`, `PAP-017`, and `PAP-018` for manufacturing, fibre attach, serviceability, and reliability.
4. `PAP-019`, `PAP-022`, `PAP-026`, and `PAP-027` for external versus integrated laser technology and the supplier thesis.
5. `PAP-014` and `PAP-023` for potential platform and tooling control points.
6. `PAP-020` for the system-level value mechanism behind higher-radix CPO switches.

The three previously incomplete downloads have now been replaced by verified full papers. See `papers/acquisition-issues.md` for the audit trail.

### Current leadership-diligence packet

Read these after the focused architecture sprint:

1. `CMP-008`: NVIDIA Rubin platform press kit — integrated switch-platform and production-roadmap evidence.
2. `CMP-009`: Broadcom OFC 2026 material — merchant CPO maturity and 400G-per-lane roadmap; official two-page PDF retained locally.
3. `CMP-010`: Lumentum fiscal Q2 2026 results — near-term CPO order and delivery signal.
4. `PRS-003`: Coherent OFC 2026 investor deck — InP capacity, component breadth and customer-order claims.
5. `FIL-001`: Marvell May 2026 10-Q — transaction facts and execution risk for the Celestial AI optical-I/O strategy.
6. `CMP-011`: Meta–NVIDIA partnership — customer-side Spectrum-X evidence that does not isolate CPO volume.
7. `CMP-012` and `CMP-013`: Ayar Labs and Lightmatter — private accelerator optical-I/O and NPO candidates; roadmap evidence only.
8. `CMP-014`: TSMC COUPE — manufacturing-platform roadmap rather than a directly comparable end product; the local retrieval note points to the official page and attached PDF, which currently block automated download.

See `company-leadership-source-manifest.md` for the complete mapping between these conclusions, local files, retained formats, and canonical publisher URLs.

Use `STD-005` to test whether NPO remains technically viable at 400G per lane, `STD-006` for the external-laser management baseline, and `PAP-009` as an architectural countercase to the assumption that CPO is the only future optical fabric.

## Review method

For each source:

1. Update `review_status`.
2. Extract the main claim without changing its meaning.
3. Record important numbers with their comparison baseline and units.
4. Separate author assumptions from sourced facts.
5. Record limitations and possible conflicts of interest.
6. Add claims that matter to the thesis to `claim-ledger.csv`.
7. Identify the primary evidence needed to confirm or contradict the source.
