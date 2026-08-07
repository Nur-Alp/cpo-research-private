# Academic evidence matrix for scale-out optical engines

**Owner:** Nur Alpys  
**Status:** Evidence synthesis; not a production forecast  
**Last updated:** 2026-08-07

## How to read this matrix

This matrix is a screening layer between the retained papers and the company/economic models. “Measured” means the paper reports a completed test vehicle or experiment. “Modelled” means the result depends on a simulation, assumed channel, or extrapolation. “Target” means an engineering objective or research direction. A paper can contain more than one evidence class; the table records the class that governs the cited investment use.

The claim IDs point to the detailed wording and limitations in [`claim-ledger.csv`](../01-sources/claim-ledger.csv). No row clears a production-yield, customer-qualification, field-reliability, ASP, or margin gate by itself.

## Matrix

| Engine / PIC question | Retained evidence | Evidence class | What it supports | What it does not support |
|---|---|---|---|---|
| Is CPO a system-level packaging problem rather than only an optical-device problem? | Mahajan’s socketable-engine concept and thermal/assembly discussion; Tan’s status review [PAP-003, PAP-001; `CLM-099`–`CLM-104`] | Prototype / review | Keeps socketability, test, fibre attach, thermal path, service and throughput in the same boundary as PIC performance. | Current production volume, final good-engine yield, or supplier economics. |
| Does moving optics inward have a network benefit? | Higher-radix and simulation studies evaluate locality, radix and network-level effects [PAP-020, PAP-006; `CLM-129`–`CLM-133`, `CLM-089`–`CLM-090`] | Modelled / simulation | Defines workload and topology variables that must enter a CPO-versus-LPO TCO comparison. | A universal adoption requirement or customer willingness to pay. |
| Is 100G/lane LPO a credible countercase? | Meta reports a 100G/lane linear-drive system demonstration with measured link margin [PAP-007; `CLM-056`–`CLM-058`] | Measured system + modelled 200G extension | Establishes a real pluggable counterexample at 100G/lane and a loss-budget method. | 200G/400G production LPO, or proof that CPO is required for every 102.4T system. |
| What is known at 200G/lane? | 200G LPO papers report loss/sensitivity boundaries under stated channel and receiver assumptions [PAP-007, PAP-008, PAP-010; `CLM-057`–`CLM-064`] | Modelled / limited test data | Defines the electrical reach and retimer assumptions for a matched 200G boundary. | A multi-vendor qualified end-to-end 200G LPO system or cost conclusion. |
| What is known at 400G/lane? | 400G linear-drive work reports component or assumed-link results and identifies open channel-loss constraints [PAP-011; `CLM-065`–`CLM-066`] | Modelled / component evidence | Makes 400G a future qualification gate rather than a current base-case deployment assumption. | A complete 400G LPO/NPO/CPO product or production date. |
| Which PIC/electronics co-design choices matter? | Electronic-photonic co-design and microring 3D-CPO studies cover driver, modulator, thermal tuning and layout co-optimization [PAP-012, PAP-021, PAP-023; `CLM-025`–`CLM-030`, `CLM-134`–`CLM-137`] | Demonstration / design methodology | Identifies PIC-driver-TIA co-design, thermal control and layout as yield and energy variables. | Comparable product-level pJ/bit, field lifetime, or gross margin. |
| Can higher-order coherent PICs extend the 200G/lane boundary? | C2PO models offset-QAM-16 microring links at 200/400 Gb/s per fibre per wavelength and fabricates only a 25 Gb/s GF45 proof of concept [PAP-038; `CLM-326`–`CLM-328`] | Link-level model + low-rate prototype | Provides a serious 400G-per-wavelength architectural countercase and makes thermal tuning/packaging explicit. | A measured 200G/400G packaged engine, complete power, fibre reach, yield, qualification or cost. |
| Is a 2.5D optical interposer a credible 400G PIC route? | Hou et al. demonstrate four 106.25 Gb/s PAM4 channels on a SiON/Si interposer with flip-chip EMLs and photodetectors [PAP-039; `CLM-329`–`CLM-331`] | Measured research transceiver | Adds an experimentally measured interposer route with channel-level TDECQ, receiver sensitivity and coupling boundaries. | 200G/lane operation, complete-engine power, simultaneous-channel margin, production yield, qualification or commercial economics. |
| Can heterogeneous integration scale? | CMOS-based optical-interposer and silicon-photonics/CMOS review work covers hybrid bonding, heterogeneous integration, wafer-level test and yield learning [PAP-014, PAP-024; `CLM-019`–`CLM-024`, `CLM-120`–`CLM-128`] | Review / research platform | Frames foundry, wafer-level test, integration route and yield as potential control points. | Qualified merchant supply, customer allocation, or attributable foundry profit. |
| Which light-source architecture is plausible? | External-light-source, high-power CW, SOA-DFB, monolithic InP and single-mode VCSEL papers compare source placement and device paths [PAP-002, PAP-019, PAP-022, PAP-025, PAP-027; `CLM-033`–`CLM-043`, `CLM-105`–`CLM-108`] | Demonstrations / research results | Establishes the architecture set for the laser benchmark: external ELS, integrated InP, SOA-DFB and VCSEL. | A winner on lifetime, service cost, yield, or supplier pricing power. |
| Can one external laser feed multiple optical channels? | Polymer-splitter and waveguide work reports high-power transmission, low PDL/DGD/PER and short-duration stability [PAP-026, PAP-030; `CLM-037`–`CLM-039`, `CLM-242`–`CLM-243`] | Measured lab vehicle | Supports testing external-light distribution as a serious serviceability and laser-count option. | Qualification lifetime, complete-engine loss distribution, field replacement cost, or production yield. |
| Can optics be attached and serviced at scale? | Fibre-array attach, thermomechanical assembly, evanescent coupling and detachable/reflow connectors report process and loss results [PAP-015–PAP-018, PAP-028; `CLM-044`–`CLM-055`, `CLM-239`–`CLM-240`] | Measured test vehicles | Supplies attach-loss, connector-loss, reflow and mechanical-risk variables for the yield/service model. | Automated high-volume cycle time, Cpk, final good-engine yield, warranty or MTTR. |
| Can passive optical assembly reduce alignment cost? | Weninger et al. simulate a GRIN/evanescent coupler with sub-0.27 dB coupling and micrometre-scale 1 dB alignment tolerances [PAP-040; `CLM-332`] | Simulation | Identifies a potential passive-assembly path that could reduce active-alignment cost and cycle time. | Fabricated coupler, measured loss distribution, automated yield, reflow and environmental qualification. |
| Is polymer-waveguide packaging entering full-module reliability work? | IBM's IEDM record describes single-mode polymer-waveguide CPO modules, optics-last assembly and thermomechanical testing [PAP-041; `CLM-333`] | Full-module abstract / process record | Extends the IBM evidence from ECTC workflow to a second substrate and polymer-waveguide module boundary. | Quantitative pass/fail, production yield, 200G/lane link result, field reliability, ASP or margin. |
| What connects laboratory packaging to pilot manufacturing? | O'Brien's OFC 2025 abstract frames glass interposers, BGA-style photonic-electronic packages, micro-optics and packaging equipment as part of the research-to-pilot transition [PAP-032; `CLM-253`–`CLM-254`] | Abstract-level process framing | Adds equipment and design-for-manufacturability questions to the manufacturing diligence queue. | Any quantitative pilot output, yield, throughput, qualification, customer SKU, cost or margin. |
| Does glass/interposer packaging improve the electrical/thermal boundary? | Glass-substrate switch test vehicles and glass-interposer thermal/electrical studies report propagation, connector, thermal and insertion-loss results [PAP-004, PAP-031; `CLM-109`–`CLM-111`, `CLM-244`–`CLM-245`] | Test vehicle + simulation | Adds glass/interposer as a packaging option and supplies bounded thermal/RF sensitivity inputs. | A complete 102.4T product, optical yield, cost advantage, or customer qualification. |
| Can optical I/O move beyond switch-side CPO? | Beyond-CPO, connectorized chiplet, FOWLP engine and accelerator/network studies cover optical chiplets and scale-up paths [PAP-005, PAP-013, PAP-029, PAP-006; `CLM-112`–`CLM-115`, `CLM-031`–`CLM-032`, `CLM-241`] | Demonstration / modelled | Keeps accelerator optical I/O and NPO as separate domains with different ownership and economics. | A switch-side CPO leadership conclusion or production revenue forecast. |
| What is the strongest academic conclusion for the profit thesis? | Across the packet, the recurring bottlenecks are attach/alignment, thermal path, testing, yield, reliability and service—not the existence of a working PIC [all PAPs above] | Cross-paper inference | Focuses diligence on cost-per-good-engine, qualification and serviceability, where sustainable profit capture is most likely decided. | Any claim that the best lab device guarantees the highest-margin supplier. |

## Decision use

1. Use measured rows to set engineering bounds and to populate sensitivity cases.
2. Use modelled rows only when the channel, topology, temperature and FEC assumptions are carried into the comparison.
3. Keep research targets out of the base case until a later paper or product source demonstrates the same boundary.
4. Do not convert any academic result directly into market share, ASP, margin or adoption probability.

## Linked model gates

- [Optical-engine benchmark](optical-engine-benchmark.md)
- [PIC-design profit implications](pic-design-profit-implications.md)
- [Laser architecture benchmark](laser-architecture-benchmark.md)
- [Packaging and reliability benchmark](packaging-reliability-benchmark.md)
- [Engine yield waterfall template](../08-model/engine-yield-waterfall-template.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [CPO evidence-gate register](../08-model/evidence-gate-register.md)
- [Claim ledger](../01-sources/claim-ledger.csv)

## New academic packet

- `PAP-038`: Dan Sturm et al., [*C2PO: Coherent Co-packaged Optics using offset-QAM-16 for Beyond PAM-4 Optical I/O*](../01-sources/papers/PAP-038-sturm-c2po-coherent-cpo-qam16-2025.pdf), arXiv:2506.12160. Full 9-page PDF retained; modeled 200/400 Gb/s link and 25 Gb/s fabricated proof of concept.
- `PAP-039`: Daibao Hou et al., [*2.5D co-packaged optical I/O chipsets on a SiON/Si interposer for 4 × 100G optical interconnection*](../01-sources/papers/PAP-039-hou-sion-optical-interposer-2026.pdf), arXiv:2602.08284. Full 9-page PDF retained; measured four-channel 400 Gb/s aggregate transceiver boundary.
- `PAP-040`: Drew Weninger et al., [*Graded Index Couplers for Next Generation Chip-to-Chip and Fiber-to-Chip Photonic Packaging*](../01-sources/papers/PAP-040-weninger-grin-couplers-cpo-2025.pdf), arXiv:2503.00121. Full 21-page PDF retained; simulation only.
- `PAP-041`: Akihiro Horibe et al., [*Co-packaged optics module with single-mode polymer waveguide*](../01-sources/papers/PAP-041-ibm-single-mode-polymer-waveguide-iedm2025.md), IBM Research / IEDM 2025. Official abstract record retained; full paper requires access.
