# CMP-049 — Teradyne: Silicon Photonics Raises New Test Challenges

**Canonical source:** <https://www.teradyne.com/2025/02/24/sipho-raise-new-test-challenges/>  
**Publisher:** Teradyne  
**Publication date:** 2025-02-24  
**Local files:** [HTML snapshot](CMP-049-teradyne-silicon-photonics-test-challenges.html) · [readable PDF snapshot](CMP-049-teradyne-silicon-photonics-test-challenges.pdf)

## Why retained

This is a supplier-side manufacturing and test source, not independent customer evidence. It is useful because it identifies the test insertions and throughput constraints that must be priced into a CPO engine: wafer test, optical-engine test, package/CPO test and system-level test.

## Evidence extracted

- Teradyne defines the CPO engine as silicon photonics plus discrete components and an optical-fibre connector, with several engines assembled around the switch or GPU ASIC.
- It states that the datacom opportunity is roughly two orders of magnitude larger than the historical silicon-photonics manufacturing base, creating a scale-up requirement for wafer and optical-engine yield.
- It identifies three manufacturing requirements: higher wafer/engine yields, proof of heterogeneous packaging with OSATs/contract manufacturers, and high-volume test methods.
- It describes CPO testing as requiring active thermal management, large-package handling, optical alignment, high-speed digital and RF testing, and simultaneous electrical/optical measurement.
- It explicitly says test insertions from wafer through final package must be optimized for coverage, test time and cost; current alignment-heavy processes can become a throughput bottleneck.

## What this changes

The source supports a **test-capacity and test-cycle gate** in the cost-per-good-engine model. A technically successful PIC does not automatically translate into an economical engine if defects are discovered only after expensive package assembly or if alignment-heavy test time limits throughput.

## Limitations

- Teradyne is a test-equipment supplier describing industry requirements and its own positioning.
- No customer production lot, measured factory yield, Cpk, test seconds per engine, ASP, margin, qualification pass rate or field-return data is disclosed.
- “Two orders of magnitude” is a qualitative market-scale comparison, not a CPO unit forecast.

**Use:** manufacturing/test bottleneck evidence; do not use as a company-specific yield or revenue input. See `CLM-393`–`CLM-396`.

