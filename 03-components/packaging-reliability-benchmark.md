# CPO Packaging, Fibre-Attach and Serviceability Benchmark

**Owner:** Nur Alpys

**Status:** First evidence block; not a supplier ranking

**Deployment boundary:** Scale-out optical engines and adjacent CPO packaging

**Last updated:** 2026-08-07

## Decision question

Which optical-engine packaging flow can achieve the lowest qualified cost after optical loss, assembly yield, test time, rework, thermal-mechanical stress, field reliability and serviceability are included?

The reviewed papers establish useful process mechanisms and laboratory measurements. They do not disclose final-engine yield, field failure rates, automated line throughput, warranty cost or customer qualification. No supplier receives a manufacturing-readiness or reliability-leadership score from this evidence block alone.

## Comparison rules

1. Separate measured optical loss from modeled tolerance and process-control predictions.
2. State whether loss covers one interface, two interfaces, waveguide propagation, bends or the complete fibre-to-PIC path.
3. Record sample count, channel count, mating cycles, thermal exposure and environmental conditions.
4. Do not treat short mating repeatability as lifetime reliability.
5. Do not treat a single reflow profile as JEDEC, Telcordia or customer qualification.
6. Do not call a process high-volume-ready without yield distribution, statistical process capability, cycle time, rework and production-volume evidence.

## Evidence-matched comparison

| Approach | Evidence and boundary | Measured result | What it may solve | What remains unproven |
|---|---|---|---|---|
| Intel socketable 1.6T photonic-engine concept | `PAP-003`; Intel-led 25.6T conceptual switch with 16 separately assembled/tested engines and a March-2020 proof-of-concept; socket-test boundary is component-level | The high-speed LGA socket met the paper's `<=0.5 dB` insertion-loss target through 28 GHz; contact resistance was measured across three samples and approached 37 mOhm/pin at 30 lbf. The paper does not report total system yield | Separates engine test from final-switch assembly; avoids BGA reflow of engines and creates a potential engine-replacement boundary | Current production status, final-engine and system yield, mating/environmental lifetime, field replacement procedure/time, engine inventory cost, socket cost, customer qualification and 102.4T/204.8T scalability |
| IBM passive fibre-array attach process control | `PAP-015`; 30 GlobalFoundries 45SPCLO mock-ups, 16-fibre 250 um-pitch FAUs, silicon V-grooves, 1270-1330 nm; loopbacks retained as the insertion-loss reference | An OBR model using four extracted factors reported correlation 0.98, average error 0.4 dB and error standard deviation 0.5 dB on 1,178 observations; the same data were reinjected for evaluation. GLP was estimated at 10 seconds setup plus 2 minutes measurement per 16-channel site, versus 1 minute setup plus 3-10 minutes measurement for OBR or standard IL | Loopback-free process monitoring, reduced test-structure die area, fast detection of poor fibre seating and diagnosis of process drift | Held-out or external model validation, false-pass/false-fail rate, production Cpk, transfer across couplers and lines, final attach yield, rework, cost and actual HVM volume |
| Large 51.2T CPO assembly simulation | `PAP-016`; finite-element model of a 200 x 200 mm substrate with one ASIC package, 16 socketed 3.2T optical engines, reflow cooling from 180 C to 25 C and 400 N bolt pretension | Modeled socket-area warpage was 0.035 and 0.041 mm against a 0.05 mm target; corner-BGA stress was about 38 MPa after cooling and 41 MPa after compression versus an approximately 75 MPa SAC305 yield-strength reference; socket corner forces were 0.21-0.23 N in compression against a 0.1 N target | Exposes coupled warpage, solder-stress and socket-force trade-offs before building a large package | Physical validation, initial substrate warpage, repeated reflow, thermal or power cycling, creep/fatigue lifetime, optical alignment after assembly, production tolerances and field reliability |
| Corning IOX glass interconnect, evanescent coupling and detachable MT connector | `PAP-017`; different sub-experiments with a 16-channel glass fan-out, six flip-chip SiN devices and a detachable physical-contact connector | The 250-to-50 um fan-out averaged 0.86 +/- 0.13 dB fibre-to-fibre, including two estimated 0.3 dB edge couplings. The best evanescent-path result was 0.38 dB at 1337 nm but excluded FAU-to-glass edge coupling. A separate detachable connector interface reported 0.8 dB including connector and mode mismatch | Dense pitch conversion, separable fibre cable, and a glass transfer path between fibre and PIC | A combined end-to-end assembly, connector-cycle distribution, reflow, environmental qualification, contamination sensitivity, automated assembly, yield, rework and cost |
| Furukawa collimated-beam magnetic detachable connector | `PAP-018`; 12 channels at 250 um pitch and 1310 nm; two FA-to-FA connector pairs for mating repeatability; a separate one-sample PLC assembly for reflow | Both FA-to-FA pairs remained at or below 0.4 dB with variation within +/- 0.05 dB over ten mating cycles. One PLC sample underwent a 260 C peak for 60 seconds; total loss before reflow was below 1 dB, average before/after change was below 0.14 dB, and five-cycle variation was within +/- 0.05 dB. A four-connector glass mock-up demonstrated 1.2 channels/mm | Removes fibre handling during substrate reflow, enables detachable service access and relaxes lateral tolerance through a 60 um collimated beam | CPO-substrate or powered-engine test, multiple reflows, sample distribution, long-cycle wear, shock/vibration, humidity, dust, magnetic ageing, qualification, passive alignment yield, cost and volume |
| Ayar known-good connectorized optical-I/O chiplet | `PAP-013`; early MOLA and fibre-attached TeraPHY process concept | Ten mating cycles showed less than 0.1 dB repeatability standard deviation; reported alignment tolerances were simulations, not measured production distributions | Electrical and optical test before combining the fibre-attached chiplet with expensive compute dies | Sample count, fibre-attach yield, automated cycle time, environmental and lifetime qualification, rework economics and production volume |

## Measurement-boundary reconciliation

| Result | Included | Excluded or uncertain | Correct use |
|---|---|---|---|
| IBM OBR prediction error | Reflection-derived factors compared with loopback IL across 1,178 observations | Independent test set, cross-lot validation and economic yield impact | Process-monitoring feasibility, not production-yield proof |
| Corning 0.86 +/- 0.13 dB | Two fibre edge couplings, glass propagation and fan-out bend loss | Evanescent PIC coupling and detachable connector | Fan-out subassembly result |
| Corning 0.38 dB minimum | Glass propagation/bends plus IOX-to-SiN evanescent coupling for one device/wavelength | FAU-to-IOX edge coupling; full detachable connector | Best partial-path result, not total fibre-to-PIC loss |
| Corning 0.8 dB connector | Detachable physical-contact connector plus fibre/IOX mode mismatch | PIC coupling and full glass path | Separate connector-interface result |
| Furukawa <=0.4 dB | One FA-to-FA detachable connector interface at 1310 nm | PIC, glass-PIC coupling, engine and full link | Short-cycle connector result |
| Furukawa reflow result | Two connector interfaces plus PLC waveguide; one 260 C/60-second exposure | Actual CPO glass substrate, populated package, repeated reflow and qualification sequence | Reflow-feasibility screen, not reliability qualification |

## Manufacturing and economic read-through

### What the evidence supports

- A socketable engine may move electrical/optical test and some assembly risk ahead of final switch integration. It does not eliminate fibre-attach scrap risk or prove a field-service model; the socket itself introduces an electrical, mechanical and inventory boundary.
- Fibre attach is not only an optical-loss problem. It creates die-area, metrology, test-time, false-pass and combined-yield consequences.
- Detachable connectors create a plausible serviceability and known-good-subassembly path by allowing fibres to be absent during reflow or final package assembly.
- Large CPO packages create coupled mechanical trade-offs. Reducing warpage with a larger stiffener can increase C4 stress, and a flatter substrate can retain more BGA stress.
- The complete economic boundary must include attach yield, test coverage, rework, connector loss, line throughput and qualification—not simply the lowest demonstrated coupling loss.

### What the evidence does not support

- No paper supplies final-package or final-engine yield.
- No paper reports Cpk, automated line volume, scrap cost or field return rate.
- No connector receives a reliability qualification from ten mating cycles or one reflow exposure.
- No result establishes that specialist packaging suppliers retain pricing power rather than competing as capital-intensive manufacturing vendors.
- No reviewed experiment compares the same connector and attach flow across competing PIC platforms on a matched cost and reliability boundary.

## Investment implication

Packaging remains a credible control point but not yet a demonstrated standalone profit pool. The strongest potential differentiation is likely to come from a supplier that owns the coupled process window across PIC edge design, fibre attach, connector, assembly, in-line metrology, final test and rework. A low-loss connector record without qualified process yield is unlikely to guarantee durable margin.

For Coherent, Lumentum, Broadcom and other candidates, the company diligence should request evidence at the following boundary:

```text
qualified engines shipped
x fibre-attach first-pass yield
x final-package yield
x customer acceptance yield
x realised price
- rework, scrap, warranty and capital cost
```

## Evidence gates for company scoring

1. Fibre-attach loss distribution by lot, temperature and wavelength, not a best channel.
2. First-pass yield, rework yield, process Cpk and escape rate.
3. Automated alignment and test cycle time per engine.
4. Complete path loss from laser or fibre input through the PIC boundary.
5. Reflow count and profile, thermal cycling, humidity, shock, vibration and contamination testing.
6. Mating-cycle distribution and connector wear after environmental exposure.
7. Failure isolation, field replacement unit and mean time to repair.
8. Named customer qualification, shipped volume and field-return statistics.
9. Attributable packaging/test capital and depreciation per good engine.
10. Warranty allocation and liability across PIC, laser, connector, OSAT and platform owner.

## Current conclusion

> The reviewed evidence supports packaging, fibre attach and serviceability as adoption-critical engineering constraints. It does not yet identify a qualified manufacturing leader or prove a packaging profit pool. IBM provides the strongest process-metrology evidence, Corning and Furukawa provide useful detachable-interface prototypes, and Cao et al. expose large-package mechanical trade-offs; all remain short of matched production yield, qualification and field economics.

## Sources

- `PAP-003`: Ravi Mahajan et al., [*Co-Packaged Photonics for High Performance Computing: Status, Challenges and Opportunities*](../01-sources/papers/PAP-003-mahajan-co-packaged-photonics-hpc-2022.pdf), *Journal of Lightwave Technology* 40(2), 2022, DOI `10.1109/JLT.2021.3104725`. Intel-led 25.6T proof-of-concept and assembly/test framework; not a current production or yield disclosure.
- `PAP-013`: Chong Zhang et al., [*Connectorized Optical I/O Chiplet with V-groove for AI and High Performance Computing*](../01-sources/papers/PAP-013-zhang-connectorized-optical-io-chiplet-2025.pdf), OFC 2025 paper Th3H.2.
- `PAP-015`: Paul Gond-Charton et al., [*Fiber array attach for co-packaged optics: high volume production process control and performance*](../01-sources/papers/PAP-015-gond-charton-fiber-array-attach-cpo-2024.pdf), ECTC 2024, DOI `10.1109/ECTC51529.2024.00185`.
- `PAP-016`: Rui Cao et al., [*Thermomechanical and Compression Analyses for Large-Scale Co-Packaged Optics (CPO) Assembly*](../01-sources/papers/PAP-016-cao-thermomechanical-cpo-assembly-2024.pdf), *IEEE Transactions on Components, Packaging and Manufacturing Technology* 14(11), 2024, DOI `10.1109/TCPMT.2024.3488003`.
- `PAP-017`: Lars Brusberg et al., [*High-density Evanescent Chip Coupling with Detachable Fiber Connector for Co-packaged Optics*](../01-sources/papers/PAP-017-brusberg-evanescent-detachable-connector-2025.pdf), OFC 2025 paper Th3H.1.
- `PAP-018`: Kengo Watanabe et al., [*Ultra-compact Reflow-compatible Detachable Optical Connector for Co-Packaged Optics*](../01-sources/papers/PAP-018-watanabe-reflow-detachable-connector-2025.pdf), OFC 2025 paper M4J.2, DOI `10.1364/OFC.2025.M4J.2`.
