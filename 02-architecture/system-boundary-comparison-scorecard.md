# Retimed pluggable, LPO, NPO and CPO — common system-boundary scorecard

**Status:** Evidence-gated comparison; not an adoption forecast or cost ranking  
**Scope:** Ethernet scale-out at 100G, 200G and prospective 400G per lane  
**As of:** 2026-08-11

The [substitution and falsification matrix](substitution-and-falsification-matrix-2026-08-12.md)
consolidates the conditions under which an alternative architecture would
invalidate or strengthen the current CPO timing view.

The [12 August common-boundary evidence audit](common-boundary-evidence-audit-2026-08-12.md)
is the current release-control readout for missing matched system inputs.

The [substitution common-boundary audit](substitution-common-boundary-audit-2026-08-12.md)
checks that all four routes are evaluated as accepted, serviceable delivered
ports rather than incomparable PIC, module or switch-level records.

The [architecture comparison evidence packet](../09-primary-research/architecture-comparison-evidence-packet-2026-08-13.md)
sets the required identity sheet and electrical, manufacturing, service and
commercial modules before any future source can be promoted into an
architecture-winner or TCO conclusion.

## Release-control matrix

The table below is the current decision gate, not a score or forecast. A route can be technically plausible while remaining **open** on the system field that determines adoption or profit.

| Required field | Retimed pluggable | LPO / RTLR | NPO / OBO | Switch-side CPO | Current conclusion |
|---|---|---|---|---|---|
| Same ASIC, ports and lane rate | **Open/partial** | **Open/partial** | **Open** | **Open/partial** | No four-way same-SKU pair |
| End-to-end electrical margin and BER/FEC | **Partial** | **Conditional/modelled** | **Open** | **Partial** | No common 200G record; no 400G system record |
| Inlet power including cooling/conversion | **Open** | **Scenario/modelled** | **Open** | **Partial examples** | Power sensitivity only |
| Thermal/ambient qualification | **Partial** | **Partial** | **Open** | **Partial package/liquid design** | No matched thermal qualification |
| Final good-unit yield, rework and test | **Open** | **Open** | **Open** | **Process mechanisms only** | All production-yield inputs blocked |
| Service workflow, MTTR, spares and warranty | **Modular boundary known** | **Modular boundary plausible** | **Open** | **Laser boundary known; engine open** | No restored-port cost comparison |
| Supplier share and complete cost stack | **Open** | **Open** | **Open** | **Open** | No profit-pool inference |

**Decision rule:** the current record supports a conditional coexistence thesis, not a universal architecture winner. The modeled CPO power advantage must remain labelled as scenario evidence until the same product, reach, BER/FEC, cooling, service and economic boundaries are measured together.

## Decision rule

An architecture is only preferable if it meets the **same** lane rate, port count, reach, error target, temperature, cooling boundary and service policy as the alternative. A component pJ/bit figure, a best-channel loss result or a vendor power claim cannot substitute for this system boundary.

The current evidence does not support a universal winner. It supports a conditional engineering choice and a strict diligence checklist.

## Four-way comparison

| Decision dimension | Retimed pluggable | LPO | NPO / OBO | Switch-side CPO | Evidence-adjusted reading |
|---|---|---|---|---|---|
| **Electrical path and margin** | Retimer can restore margin through a longer host-to-module channel; OIF RTLR retains a defined hot-plug module boundary and allocates a host-loss budget (`STD-012`, `CLM-297`–`CLM-300`). | At 100G, a 51.2T system result exists; at 200G, retained work is model-dependent with non-comparable 22–31 dB assumptions (`PAP-007`, `PAP-008`, `PAP-010`). | Intended to shorten the host-to-optics electrical path. OIF explicitly distinguishes die-to-near-package NPO from die-to-on-package CPO, but supplies no qualified product interface or measured 400G system (`STD-015`, `CLM-563`). | Direct ASIC-to-engine integration structurally shortens the electrical path; product definitions are public but matched margin data are not (`CMP-055`, `CLM-516`–`CLM-517`; `CMP-054`, `CLM-514`–`CLM-515`). | Electrical reach can move optics inward; it does not alone determine system economics. |
| **Power and cooling boundary** | NVIDIA's 102.4T pluggable SN6600-LD manual specification lists 3.3 kW with FRO and 3.2 kW with TRO; it is a vendor configuration, not a matched measurement (`CLM-552`). | LPO can remove some retiming; Oracle claims 4–7 W per module in its own topology, without a matched CPO control (`CLM-324`–`CLM-325`). | Potentially reduces electrical-path power, but complete module/ASIC/cooling data are open. | NVIDIA lists 1.96 kW typical for its 102.4T CPO SN6810-LD, but the manual omits a common load, ambient, external-light and cooling boundary (`CLM-552`). A Supermicro/AMD/Micas TH5-Bailly 16-link test reports 465.87W CPO versus 754.85W pluggable, but its boundary cannot generalise to TH6/NVIDIA/200G (`CLM-523`–`CLM-524`). | Same-family specifications are useful cross-checks, not a matched power/TCO proof; a common ASIC/port/reach/FEC/cooling measurement remains open. |
| **Thermal load and package boundary** | Heat is distributed across replaceable modules; faceplate thermal density can constrain a system but no matched limit is retained. | Reduces module DSP load but still depends on host/channel/optics thermal design. | Moves a module closer to the host package; local thermal interaction and qualification remain open. | Concentrates optics next to the switch ASIC and relies on package/liquid-cooling design; final-package thermal qualification and field distribution are undisclosed. | Thermal load must include ASIC, optics, laser/ELS, package, cooling and ambient conditions—not just module watts. |
| **Serviceability and replacement burden** | Clear field-replaceable transceiver boundary and established multi-vendor service model. | Retains a faceplate module boundary, subject to linear-link diagnostics and qualification. | Proposed value is a replaceable short-channel optical module, but interface ratification, field procedure and MTTR are open (`CLM-091`). | Broadcom’s ELSFP and NVIDIA’s external-laser routes make the light source replaceable; they do not prove replacement of a failed co-packaged engine (`CLM-071`, `CLM-077`, `CLM-237`). | Replaceable laser is not equivalent to replaceable optical engine, package or ASIC. |
| **Qualification, yield and rework** | Mature module flow is an advantage, but no retained 200G/400G matched yield/field data rank it against CPO. | 100G measured operation does not establish 200G final-module yield or qualification. | No retained final-engine yield, qualification lot or field record. | Process/test mechanisms and screening claims exist, but no final-engine lot yield, rework, acceptance or field-return distribution exists (`CMP-051`, `CMP-052`, `CMP-056`). | No architecture clears a common 200G/400G final-engine manufacturing-cost comparison. |
| **Interoperability and supplier options** | Strongest established module ecosystem. | Can retain module/service boundary; interoperability still depends on host/channel compliance. | The intended advantage is a distinct near-package boundary. OIF identifies electrical, mechanical, management and multi-vendor-test requirements, but not a ratified/qualified NPO product record (`STD-015`, `CLM-563`). | Link interoperability does not establish multi-sourced engine/PIC/laser/package content; platform supplier maps remain incomplete. | Do not treat a framework, OIF/IEEE contribution or vendor partner list as qualified second-source evidence. |
| **Total replacement burden** | Module swap, spares and outage scope are comparatively clear; actual downtime/warranty cost is not matched here. | Similar modular swap boundary, subject to linear-link diagnostics and qualification. | Could isolate a smaller replaceable unit, but connector, module inventory, thermal and fault-domain costs are unmeasured. | External-laser replacement may reduce one failure domain; failed engine/package/ASIC replacement, spare strategy and warranty allocation are open. | A lower component-energy claim does not establish lower cost per restored port. |
| **Evidence state at 200G / 400G** | Credible baseline; retimed route remains live. | 200G conditional, 400G conventional-LPO unproven in the retained system evidence. | Technically plausible deferral route; qualification/open-interface proof absent. | Strongest disclosed product/production signals; named customer CPO units, repeat shipments and economics remain open. | Current decision is a coexistence framework, not a winner declaration. |

## Matched-boundary evidence register

The table below is the release-control view of the comparison. “Partial” means
that a source supports a technical mechanism or one boundary, not that the
architecture wins the complete system test. “Open” means the field is required
for a decision but is not presently supported by a matched public record.

| Required decision field | Retimed pluggable | LPO / RTLR | NPO / OBO | Switch-side CPO | Current decision status |
|---|---|---|---|---|---|
| Exact same-ASIC product pair | Partial | Open/partial | Open | Partial | No four-way product pair retained |
| 200G/lane end-to-end electrical margin | Partial | Conditional/modelled | Open | Partial | No common BER/FEC/reach test |
| 400G/lane end-to-end electrical margin | Open | Open | Open | Component/model evidence only | No architecture call permitted |
| Inlet power including cooling/conversion | Open | Scenario/modelled | Open | Partial bounded system examples | Power sensitivity only |
| Thermal and ambient boundary | Partial | Partial | Open | Partial liquid/package design | No matched thermal qualification |
| Final good-unit yield and rework | Open | Open | Open | Process/test mechanisms only | All yield inputs blocked |
| Service workflow, MTTR and spares | Modular boundary known; cost open | Modular boundary plausible; cost open | Interface/service record open | Laser boundary known; engine/package cost open | No restored-port cost comparison |
| Qualification and field reliability | Mature ecosystem context; matched 200G/400G record open | 100G/conditional records; higher-rate record open | Open | Historical/prototype/process records; target-SKU field record open | No field-adjusted winner |
| Supplier share and complete cost stack | Open | Open | Open | Open | No profit-pool inference |

### Interpretation rule

The current evidence supports a **conditional coexistence thesis**: CPO has a
strongest-case rationale where electrical reach and power density dominate;
retimed pluggables retain the strongest modularity benchmark; LPO/RTLR may
capture part of the electrical-margin benefit; and NPO remains a plausible
intermediate boundary. None has a complete matched record that clears the
electrical, power, manufacturing, service and economic fields together. The
report must therefore label any architecture preference as an inference with
an explicit falsification condition, not as a universal technology forecast.

## RTLR is a separate hybrid comparator

RTLR (retimed transmitter / linear receiver) is not synonymous with LPO and should not be collapsed into either the fully retimed-pluggable or unretimed-LPO column. OIF RTLR preserves a hot-plug module/interoperability boundary while adding a retiming function at the transmit side. It therefore widens the possible electrical-loss envelope without proving a system power, cost, field-reliability or 200G-per-lane commercial result (`STD-012`, `CLM-297`–`CLM-300`).

| RTLR decision dimension | What current evidence supports | What remains open | Consequence for the CPO thesis |
|---|---|---|---|
| Electrical path | A defined retimed-transmitter / linear-receiver architecture with a recommended 16 dB ball-to-ball budget, including 11.9 dB host PCB/cable allocation. | 200G/400G-lane end-to-end margin, exact host topology, return-loss, BER/FEC and temperature distribution. | Prevents treating an electrical-reach challenge as a binary fully-retimed-versus-CPO choice. |
| Power / cooling | Removing the receive-side retimer can be a bounded power-saving mechanism. | Complete module/host/laser/cooling power at a matched 200G/400G system boundary. | A claimed CPO power advantage must be compared with RTLR where that topology is viable. |
| Serviceability | Hot plug and module interoperability remain explicit design goals. | Field replacement time, diagnostics, qualification, spares, failure rate and warranty cost. | RTLR retains a modular repair boundary that CPO must overcome economically. |
| Economics / adoption | It is a defined standards-level option. | Customer qualification, units, repeat shipment, module ASP, margin and total cost per delivered bit. | It is a live architectural countercase, not evidence that RTLR is the winning product. |

## Minimum matched comparison before an architecture call

The comparison should include all fields below at the same configuration:

1. Exact ASIC, port count, lane rate, reach, fibre/cable type and electrical loss/return-loss boundary.
2. Pre-FEC BER, FEC mode, link flap/error distribution and temperature/ambient conditions.
3. Inlet power plus power conversion, fans/pumps/liquid cooling and allocated thermal load.
4. Module/engine, laser, fibre/connector, package, rack-installation, spares and replacement labour cost.
5. Final-engine/module yield, attach/test cycle time, rework, qualification sample/pass rate and field-return rate.
6. Repair workflow, mean time to restore, outage/failure-domain scope, warranty allocation and spare inventory.
7. Supplier qualification/share, price-down, second-source and cancellation terms.

If an input is unavailable, preserve it as **open**. Do not fill it using a consolidated margin, an unbounded vendor percentage, or an adjacent product architecture.

## Manufacturing comparison — evidence and conclusion boundary

The manufacturing question is now explicitly closed at the **public-evidence
boundary**. The table does not claim costs that are not disclosed; it records
which manufacturing advantage is structurally plausible and which production
metric would be needed to verify it.

| Manufacturing / service field | Retimed pluggable | LPO / RTLR | NPO / OBO | Switch-side CPO | Current evidence-adjusted conclusion |
|---|---|---|---|---|---|
| Fibre attach | Connectorised module boundary; manufacturing distribution at 200G/400G not matched | Connectorised module boundary retained | Proposed shorter, replaceable optical boundary; qualification open | Final-stage attachment and detachable/external-light interfaces are disclosed, but first-pass loss/yield and rework are open | Attach is a real CPO process gate, not proven to be the binding cost constraint. |
| Package and test flow | Mature module ecosystem; matched higher-rate final-test data open | Module boundary retained; high-rate qualified flow open | Package/module split is proposed; product flow open | Wafer/engine/package/module test mechanisms and OSAT routes are documented; lot coverage/time/escape data open | CPO shifts test and late-defect exposure inward; no public cost-per-good-engine comparison exists. |
| Rework / replacement scope | Replace module; actual restored-port cost open | Similar module swap boundary, subject to link diagnostics | Intended smaller replaceable unit; field procedure open | ELS/laser can be replaceable, but failed engine/package/ASIC scope is not disclosed | ELSFP does not prove engine/package serviceability. |
| Qualification burden | Mature baseline, but not a 200G/400G matched pass-rate record | Requires host/channel and linear-link qualification | Interface, interoperability and repair qualification remain open | Integrated optical, package, thermal and fibre boundaries require coupled qualification; public pass rates open | No architecture has public evidence of lower qualified-system cost. |
| Restored-port cost | Service boundary is clear; field cost and warranty allocation open | Service boundary is clear; field cost open | Boundary is theoretical until qualified | Light-source boundary is clear; engine/package failure economics open | No route wins on public cost per restored port. |

**Result:** technical mechanisms establish why CPO may reduce electrical path
and faceplate power while increasing integration and late-defect stakes. They
do not establish a lower manufacturing, warranty or restored-port cost than
retimed, LPO or NPO alternatives. The [architecture evidence packet](../09-primary-research/architecture-comparison-evidence-packet-2026-08-13.md)
defines the E/M/S/C modules required to promote this conclusion.

## Current investment implication

- **Retimed pluggables** are the serviceability and interoperability benchmark, not an obsolete architecture.
- **LPO** is the principal unretimed, power-oriented countercase at validated electrical boundaries; **RTLR** is a distinct hybrid that may retain modular serviceability while recovering some electrical margin.
- **NPO** is a plausible CPO-deferral route if a short, replaceable and qualified module boundary emerges.
- **CPO** is most compelling when electrical reach, density and system power outweigh the cost of a more integrated repair and qualification boundary.

No public evidence currently shows the complete, matched cost-per-delivered-bit and cost-per-restored-port calculation required to claim that any route dominates at 200G or 400G per lane.

## Linked evidence

- [Architecture trigger matrix](architecture-trigger-matrix.md)
- [Linear-drive boundary benchmark](linear-drive-boundary-benchmark.md)
- [NPO interoperability and serviceability boundary](npo-interoperability-boundary.md)
- [102.4T CPO versus advanced pluggables](102.4t-cpo-vs-advanced-pluggables.md)
- [Total-cost-per-delivered-bit gate](../08-model/tco-per-delivered-bit-gate.md)
- [Matched architecture-comparison acquisition specification](../09-primary-research/matched-architecture-comparison-acquisition-spec.md)
- [TCO sensitivity arithmetic check](../scripts/validate-tco-sensitivity.py)
