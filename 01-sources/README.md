# Sources

This directory contains the research source index, reading sequence, and any legitimately retained source material or original notes.

## Canonical index

`source-log.csv` is the canonical source database. Each row records one item and distinguishes bibliographic metadata from unverified claims, limitations, relevance, and review status.

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

## Review method

For each source:

1. Update `review_status`.
2. Extract the main claim without changing its meaning.
3. Record important numbers with their comparison baseline and units.
4. Separate author assumptions from sourced facts.
5. Record limitations and possible conflicts of interest.
6. Add claims that matter to the thesis to a claim ledger once that file exists.
7. Identify the primary evidence needed to confirm or contradict the source.
