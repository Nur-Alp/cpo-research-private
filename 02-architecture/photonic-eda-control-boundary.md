# Photonic EDA control boundary

**Status:** Adjacent control-point hypothesis; not an optical-engine ranking  
**Source:** `PAP-023`, Patel et al., Synopsys, 2022

## What the paper establishes

PAP-023 explains why increasing PIC complexity makes a simple electrical-equivalent model increasingly awkward: a multiwavelength, multimode optical signal can require up to nine electrical ports/signals per wavelength, increasing pin count, probing and verification burden. It proposes domain-specific electrical and photonic simulators with automatic partitioning, shared sampling and schematic-driven layout/back-annotation.

Its worked TW-MZM example is a design-specific co-simulation. For the studied PIC and Q-factor target, a path-length mismatch up to 21 mm is acceptable at 10 Gb/s, but only 8 mm at 25 Gb/s. This demonstrates the coupling between RF layout and photonic performance; it is not a universal package tolerance for 200G/400G lanes.

## Investment relevance

EDA and PDK interoperability may become a control point because electronic, photonic, packaging and thermal choices increasingly need to be closed together before tapeout. However, the paper provides no design-cycle benchmark, customer adoption, recurring software revenue, PDK market share, yield improvement or margin data. Synopsys should therefore remain an adjacent tooling candidate—not a current scale-out optical-engine leader—until those commercial links are evidenced.

## Diligence gates

1. Independent customer evidence of OptoCompiler/PDK adoption in production PIC programs.
2. Measured reduction in tapeout iterations, verification escapes or design time.
3. Foundry PDK interoperability and portability across process nodes.
4. Software/PDK pricing, recurring revenue and renewal economics.
5. Demonstrated correlation between co-design flow and final package yield or link performance.

## Sources

- `PAP-023`: [retained PDF](../01-sources/papers/PAP-023-patel-electronic-photonic-codesign-flow-2022.pdf), DOI [10.1109/MWP54208.2022.9997638](https://doi.org/10.1109/MWP54208.2022.9997638).
- Claim ledger: `CLM-134` through `CLM-137`.
