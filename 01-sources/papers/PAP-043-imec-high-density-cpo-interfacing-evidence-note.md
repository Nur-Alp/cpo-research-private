# PAP-035 — imec, “Interfacing silicon photonics for high-density co-packaged optics”

**Canonical source:** <https://www.imec-int.com/en/articles/interfacing-silicon-photonics-high-density-co-packaged-optics>  
**Original publication context:** Chip Scale Review, Nov./Dec. 2024 (the imec page reproduces the article)  
**Local preservation:** [HTML snapshot](PAP-043-imec-high-density-cpo-interfacing.html) · [readable PDF snapshot](PAP-043-imec-high-density-cpo-interfacing.pdf)

## Evidence extracted

- The article frames optical interfacing as a high-density CPO assembly-yield and scalability problem, not only a coupling-loss problem.
- In an initial development run, the reported overall optical yield for the 1.5-mm edge-vertical-coupler design was **75.5%**, compared with **68%** for 1.0 mm and **57%** for 0.5 mm.
- The article attributes non-functional devices to die loss during collective die-to-wafer assembly, edge voids and lateral (y-axis) misalignment. The 0.5-mm design was especially sensitive to lateral misalignment above about 1 µm; the 1.5-mm design tolerated up to about 1.5 µm in the shown data.
- The reported SiN-to-fibre interface is approximately **−1.5 dB/fibre** for the cited hybrid edge-coupler approach, while the longer coupler improves alignment tolerance in the reported development structure.

## Boundary and limitations

These are laboratory/development-run measurements for an optical interface, not a complete optical engine, package, board or production line. The article does not provide a production denominator, lot statistics, Cpk, automated cycle time, rework recovery, thermal-cycle/lifetime qualification, customer SKU, ASP or margin. The 75.5% figure must therefore be stored as **interface-development yield**, not final-engine or board yield.

## Research use

Use this source to calibrate the fibre-interface and alignment-yield gate in [packaging-reliability-benchmark.md](../../03-components/packaging-reliability-benchmark.md), [fibre-count-yield-sensitivity.md](../../08-model/fibre-count-yield-sensitivity.md) and [yield-claim-reconciliation.md](../../08-model/yield-claim-reconciliation.md). It supports the view that coupler geometry and alignment tolerance can materially change yield, but it does not rank imec or any commercial supplier.
