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
| Can heterogeneous integration scale? | CMOS-based optical-interposer and silicon-photonics/CMOS review work covers hybrid bonding, heterogeneous integration, wafer-level test and yield learning [PAP-014, PAP-024; `CLM-019`–`CLM-024`, `CLM-120`–`CLM-128`] | Review / research platform | Frames foundry, wafer-level test, integration route and yield as potential control points. | Qualified merchant supply, customer allocation, or attributable foundry profit. |
| Which light-source architecture is plausible? | External-light-source, high-power CW, SOA-DFB, monolithic InP and single-mode VCSEL papers compare source placement and device paths [PAP-002, PAP-019, PAP-022, PAP-025, PAP-027; `CLM-033`–`CLM-043`, `CLM-105`–`CLM-108`] | Demonstrations / research results | Establishes the architecture set for the laser benchmark: external ELS, integrated InP, SOA-DFB and VCSEL. | A winner on lifetime, service cost, yield, or supplier pricing power. |
| Can one external laser feed multiple optical channels? | Polymer-splitter and waveguide work reports high-power transmission, low PDL/DGD/PER and short-duration stability [PAP-026, PAP-030; `CLM-037`–`CLM-039`, `CLM-242`–`CLM-243`] | Measured lab vehicle | Supports testing external-light distribution as a serious serviceability and laser-count option. | Qualification lifetime, complete-engine loss distribution, field replacement cost, or production yield. |
| Can optics be attached and serviced at scale? | Fibre-array attach, thermomechanical assembly, evanescent coupling and detachable/reflow connectors report process and loss results [PAP-015–PAP-018, PAP-028; `CLM-044`–`CLM-055`, `CLM-239`–`CLM-240`] | Measured test vehicles | Supplies attach-loss, connector-loss, reflow and mechanical-risk variables for the yield/service model. | Automated high-volume cycle time, Cpk, final good-engine yield, warranty or MTTR. |
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
- [Laser architecture benchmark](laser-architecture-benchmark.md)
- [Packaging and reliability benchmark](packaging-reliability-benchmark.md)
- [Engine yield waterfall template](../08-model/engine-yield-waterfall-template.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [CPO evidence-gate register](../08-model/evidence-gate-register.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
