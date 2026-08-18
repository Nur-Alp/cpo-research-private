# PIC technology decision scorecard — scale-out optical engines

**Status:** Private evidence scorecard; not a supplier ranking  
**As of:** 2026-08-11  
**Decision boundary:** 200G/lane Ethernet-scale-out optical engines, with 400G/lane as a future stress test

The [PIC-engine viability promotion gate](pic-engine-viability-promotion-gate-2026-08-13.md)
is the shared handoff to manufacturing, service and economics. It requires a
route to clear those boundaries before any performance result can become a
company, supplier-share or profit-pool conclusion.

Use the [PIC-to-engine investment gates](pic-to-engine-investment-gates-2026-08-12.md)
to separate device demonstrations from a qualified, serviceable and
economically attributable engine.

The companion [PIC investment-boundary audit](pic-investment-boundary-audit-2026-08-12.md)
records the evidence-maturity ladder and the fields still required before any
route can support a company or profit-pool ranking.

## Route-control matrix

This is a decision-control table, not a weighted technology ranking. It records what each route can support at the stated boundary and what remains necessary before it can become a company or profit-pool thesis.

| Route | Relevant boundary | Strongest evidence class | Primary unresolved risk | Permitted conclusion now | Commercial gate still required |
|---|---|---|---|---|---|
| Silicon photonics + external laser | 200G/lane switch-CPO process route | Product/process and interface evidence | Delivered laser power, fibre attach, final-engine yield, service and supplier allocation | Leading switch-CPO process route for diligence, not a material winner | Exact customer SKU, qualified engine lot, supplier share, ASP, margin and warranty |
| InP | 200G-class integrated transmitter and 400G/lane advanced-pluggable countercase | Measured PIC/transmission demonstrations | Complete module power, packaging, yield, qualification and modular service economics | Serious optical-device countercase; no universal CPO conclusion | Matched system comparison, production yield, customer qualification and product economics |
| Thin-film lithium niobate | 225GBd/400G-class advanced-pluggable countercase | Measured transmission paper | Chassis power, fibre/package boundary, yield, qualification and service | High-rate modular countercase that can narrow CPO’s addressable market | Same-topology CPO comparison and qualified module economics |
| Heterogeneous / 2.5D integration | 400G aggregate to 1.6T-class packaging/process route | Measured research engines and package/process evidence | Thermal path, attach/test yield, rework, final good-engine cost and ownership | Potential process-control point, not proven supplier value capture | Named product allocation, final-engine yield waterfall, ASP/share and margin |

**Hard rule:** no route receives a company ranking, revenue attribution or profit-pool score from lane rate, PIC loss, pJ/bit, capacity or a demonstration alone. The relevant decision unit is a qualified, serviceable good engine at a defined system boundary.

## How to read this scorecard

This is an **evidence scorecard**, not a numerical technology score. A route receives `Demonstrated`, `Partial`, `Open`, or `Countercase` only for the stated boundary. No route receives a commercial or profit-pool pass without a qualified-engine denominator, yield/rework data, service evidence, customer volume and attributable economics.

| Evidence label | Meaning |
|---|---|
| Demonstrated | Retained source reports a relevant measured component, engine, packaging or transmission result. |
| Partial | A relevant result exists but misses a necessary engine, environmental, multi-channel, qualification or system boundary. |
| Open | No retained evidence supports a decision-grade conclusion at this boundary. |
| Countercase | A credible architecture can reduce the need for the route; it is not necessarily a direct replacement. |

## Technology scorecard

### Compact cross-route decision matrix

The labels below are evidence states, not rankings: `Strongest retained`
means the current source set is most developed at the stated boundary; it does
not mean the route has the best commercial outcome. `Partial` means a relevant
measurement or process record exists but a decision-critical boundary is
missing; `Open` means no product-matched evidence is retained.

| Technology family | Modulator / receiver performance | Laser strategy | Fibre coupling / service | Thermal sensitivity | Testability | Yield path | Manufacturability | Decision implication |
|---|---|---|---|---|---|---|---|---|
| **Silicon photonics** | **Strongest retained** for the current 200G/lane switch-CPO architecture; full matched engine/link distributions remain partial | External InP/ELS is the clearest current route; source, fan-out loss and lifetime remain partial | Detachable-light and late fibre-attach routes are documented; service economics and attach yield remain partial | **Partial**; package, laser and fibre thermal paths are not fully reconciled | **Partial**; known-good screening, wafer/interface and final-stage test routes exist | **Open** for final accepted-engine yield; development/interface yields are not transferable | **Partial**; strongest disclosed switch-CPO process route, but no HVM Cpk/cost record | Near-term switch-CPO process-control case, not a proven material winner |
| **InP** | **Partial to strong** component evidence, including monolithic 200G-class and TEC-less 400G/lane countercases; complete module boundary varies | Integrated DFB/MZM/SOA or external high-power DFB; lifetime and full power remain partial | **Open to partial** depending on monolithic versus pluggable route; service boundary is not established | **Partial** at device/test boundary; complete engine thermal/life data open | **Open** for known-good production module path | **Open** for compound-semiconductor final-engine yield, rework and qualification | Credible device route, but compound yield and assembly economics are unresolved | Serious modular countercase; CPO cannot win by lane rate alone |
| **Thin-film lithium niobate** | **Partial** 225GBd/400G-class transmission evidence; no matched switch-engine result | External laser remains outside the core device result; total source/control power open | **Open** for product-level coupling, connector and service boundary | **Partial** laboratory temperature evidence; no module qualification/life distribution | **Open** for production known-good module testing | **Open** for wafer-to-qualified-module yield and rework | Potential high-rate modular route; manufacturing and packaging economics unproven | Could narrow CPO’s addressable market at 400G/lane |
| **Heterogeneous integration** | **Partial** aggregate/engine demonstrations across SiPh, interposer and chiplet routes; no single matched product | **Open / route-dependent**; external, integrated and chiplet sources coexist | **Partial** pre-final-assembly/test-before-final and detachable-chiplet concepts; field replacement economics open | **Open to partial**; thermal path is a primary integration risk | **Partial** wafer/interposer/known-good-die mechanisms exist | **Open** for complete package-to-good-engine waterfall, Cpk and rework | Potential control point for integration and test; no attributable commercial margin | Investable only if it lowers cost per qualified good engine at a named product boundary |

**Interpretation:** silicon photonics currently has the strongest *switch-CPO
process relevance*, InP has the strongest *modular device counterevidence*,
TFLN has the strongest *high-rate emerging modular option*, and heterogeneous
integration is the most important *manufacturing-control question*. None of
those statements establishes a customer, yield, ASP, supplier share or profit
leader.

| PIC / engine route | 200G/lane performance | Laser / power boundary | Packaging / known-good-engine path | Manufacturing and qualification | Commercial / profit-pool evidence | Current investment read-through |
|---|---|---|---|---|---|---|
| **Monolithic InP transmitter** | **Partial.** Nokia’s representative channel reaches 106.25GBd PAM4 at 60°C; full eight-channel RF distribution and full link are absent (`PAP-025`, `CLM-021`–`CLM-024`). | **Partial.** DFB, MZM, SOA and monitor are integrated, but total engine input power and lifetime are absent. | **Partial.** Fewer optical interfaces are plausible, but the electronics/package boundary remains separate. | **Open.** No final-engine yield, qualification, rework or field-return record. | **Open.** No qualified supplier content, ASP, margin or customer volume. | Technically credible dense-transmitter route; investment value depends on compound-semiconductor yield and engine qualification, not integration depth alone. |
| **TEC-less InP advanced-pluggable PIC** | **Countercase.** An eight-channel InP MZ PIC reports net 400Gb/s/lane transmission over 500m from 20–80°C; it is a different architecture from the monolithic Nokia transmitter and must not be merged with it (`PAP-053`, `CLM-483`–`CLM-486`). | **Partial.** The test uses a high-power DFB and a receiver-side PDFA/TIA-less boundary; complete module input power, laser lifetime and receiver implementation are not disclosed. | **Open.** The paper is a PIC/transmission demonstration, not a package/connector or known-good-engine record. | **Open.** No module yield, qualification, rework, service or field-return evidence. | **Open.** No customer, content, ASP or margin evidence. | Important 400G/lane modular countercase: CPO must beat it on matched power, density, service and qualified cost—not lane rate alone. |
| **Silicon photonics + external laser** | **Partial.** Supports current CPO/engine architecture routes, but retained evidence is not a matched 200G/lane qualified-engine comparison (`PAP-024`, `CMP-051`). | **Partial.** High-power external-laser results exist, but power, splitter/coupling loss, lifetime and full-engine controls are not reconciled (`PAP-019`, `PAP-022`, `CLM-033`–`CLM-039`). | **Partial.** NVIDIA describes known-good-engine screening/final fibre attachment; detachable-light interfaces define a service boundary, not engine replacement (`CMP-051`, `STD-014`, `CLM-406`–`CLM-410`). | **Partial.** Interface/yield and test infrastructure evidence exists, but no HVM final-engine yield or cost is public (`PAP-043`, `CMP-049`, `CMP-052`). | **Open.** Ecosystem roles do not establish PIC, laser or engine allocation. | Most relevant current switch-CPO manufacturing route; its possible edge is process integration across laser, PIC, attach, test and service—not SiPh alone. |
| **Heterogeneous/2.5D SiPh engine** | **Partial.** 400G aggregate and 1.6T-class packaging demonstrations exist, but they do not establish a complete 200G/lane CPO system (`PAP-029`, `PAP-039`, `PAP-045`). | **Open.** Laser architecture and full electrical/thermal power are incomplete across retained records. | **Partial.** Known-good-die, FOWLP, TGV and detachable-chiplet routes show possible pre-final-assembly test and service boundaries (`PAP-028`, `PAP-029`, `PAP-044`). | **Partial.** Wafer/interposer process evidence exists; production Cpk, rework and final yield do not. | **Open.** No durable economic allocation among PIC, EIC, interposer, OSAT and platform owner. | Strong potential control point if it lowers qualified-good-engine cost; today it is a packaging/process diligence case, not a revenue case. |
| **3D CMOS microring / optical-I/O chiplet** | **Partial.** Lightmatter reports a compact 56Gb/s single-wavelength circuit, not a 200G/lane engine (`PAP-021`, `CLM-028`–`CLM-030`). | **Open.** Reported Tx/Rx energy excludes laser; thermal tuning/control and fibre-reach boundary remain incomplete. | **Partial.** Ayar’s connectorized, test-before-final-assembly flow is a credible process direction (`PAP-013`, `CLM-031`–`CLM-032`). | **Open.** No production yield, hybrid-bonding qualification or field-life data. | **Open.** Accelerator optical-I/O is a separate value pool; no scale revenue/profit proof. | High-upside density route for accelerator optical I/O; do not extrapolate its device density into switch-CPO commercial leadership. |
| **TFLN advanced-pluggable transmitter** | **Countercase.** 225GBd/420.5Gb/s net-PAM4 transmission demonstrates that advanced pluggables can preserve a modular alternative (`PAP-054`, `CLM-471`–`CLM-475`). | **Partial.** Laboratory laser temperature sweep is reported, but full module/chassis power and lifetime are not. | **Open.** No CPO package or fibre-attach production boundary. | **Open.** No module yield, qualification or customer data. | **Open.** No commercial content/margin evidence. | Important 400G/lane countercase: it can postpone or narrow CPO’s addressable market if system qualification and economics close. |

## Evidence-status matrix for the investment decision

This is the compact decision layer for the detailed tables below. A route is
not “better” because it has more `Partial` cells: the missing cells are often
the ones that determine whether a technically attractive PIC becomes a
qualified engine and a profitable supplier position.

| Route | Target-boundary performance | Full power / thermal boundary | Packaging and known-good path | Production yield / qualification | Customer and economic evidence | Permitted conclusion now |
|---|---|---|---|---|---|---|
| Monolithic InP | Partial 200G-class transmitter evidence | Partial component boundary | Partial integration concept | Open | Open | Feasible transmitter countercase; no engine or profit conclusion |
| TEC-less InP pluggable | Partial/strong 400G-class transmission evidence | Partial | Open | Open | Open | Serious modular countercase; requires matched system test |
| SiPh + external laser | Partial architecture/process evidence | Partial, with laser boundary incomplete | Partial screening/attach/service route | Partial process evidence; final yield open | Open | Leading switch-CPO process route for diligence, not a proven supplier winner |
| Heterogeneous / 2.5D SiPh | Partial aggregate/engine demonstrations | Open | Partial wafer/interposer/test routes | Partial development evidence; production yield open | Open | Potential packaging control point; value capture blocked |
| 3D CMOS microring / optical-I/O | Partial below target lane or separate accelerator boundary | Open | Partial connectorized/test-before-final route | Open | Open | Separate accelerator optical-I/O option; not switch-CPO proof |
| TFLN advanced pluggable | Partial 225-GBaud/400G-class transmission | Partial | Open | Open | Open | High-rate modular countercase; CPO adoption cannot be inferred from lane rate |

### PIC thesis boundary

The current evidence supports a **process-control thesis**, not a material
winner thesis. At 200G/lane, SiPh with external light is the most relevant
switch-CPO route because it is connected to disclosed product architectures and
manufacturing flows. That does not establish that SiPh, TSMC, Coherent,
Lumentum, NVIDIA or any other participant captures the profit pool. At
400G/lane, integrated InP and TFLN advanced pluggables are credible
countercases, so CPO must win a matched electrical, thermal, service,
qualification and cost test rather than rely on PIC bandwidth.

## Promotion test: laboratory result to investable engine route

No technology receives a commercial rank by adding performance points. It must
pass the following chain in order; a later pass cannot repair an earlier open
boundary.

| Promotion rung | Evidence required | Current route status | Investment consequence |
|---|---|---|---|
| Device performance | Measured modulator/receiver/link result at stated lane/thermal boundary | Relevant partial evidence across SiPh, InP, TFLN and heterogeneous routes | Technical feasibility only |
| Complete engine boundary | Laser, EIC, PIC, coupling, package, power and thermal scope defined | Partial for SiPh external-light route; open/partial elsewhere | Identifies what must be costed and qualified |
| Known-good/manufacturing path | Test before final assembly where possible; attach/package/test/rework flow defined | Partial mechanisms across SiPh/heterogeneous routes | Potential integration control, not a yield result |
| Qualified good-engine output | Lot denominator, accepted yield, rework and reliability qualification | Open for every route | Required before cost-per-good-engine preference |
| Serviceable system boundary | Replacement scope, MTTR, spares and warranty known | Open for every route; detachable light is partial only | Required before CPO versus modular economic claim |
| Attributable economics | Content, price, margin and capital burden at named supplier/customer boundary | Open for every route | Required before supplier/profit-pool conclusion |

**Investment read-through:** the likely durable bottleneck is not necessarily
the PIC material. It may be the party that can repeatedly qualify the
laser/PIC/package/fibre/test stack at an acceptable cost and service boundary.
That proposition remains an inference until the final three rungs are evidenced.

## Comparable technology evidence — the fields that matter

This matrix is deliberately **not a weighted score**. A `Partial` result in one column cannot compensate for an `Open` result in another: for example, a strong modulator result cannot establish a fibre-attach yield, and an external-laser demonstration cannot establish a qualified receiver or service cost. The common target is a complete 200G/lane scale-out engine, including laser/control power and the physical service boundary.

| Route | Modulator / transmitter evidence | Receiver / link evidence | Laser strategy | Fibre coupling / service boundary | Thermal boundary | Testability / known-good path | Final-engine yield / manufacturability | Decision use today |
|---|---|---|---|---|---|---|---|---|
| **Monolithic InP** | **Partial.** Eight integrated MZMs, SOAs and monitors; representative 106.25GBd PAM4 result (`PAP-025`). | **Open.** No complete eight-channel RF/BER/reach distribution. | **Partial.** Integrated DFBs reduce an external-light interface but do not disclose lifetime or total engine power. | **Open.** Fibre attach, replacement and field boundary are undisclosed. | **Partial.** Representative operation at 60°C; no full thermal distribution/life. | **Partial.** Integrated function set is clear; production test flow is not. | **Open.** No lot yield, rework, qualification or cost. | Feasibility counterweight to SiPh; not a cost or supplier-leadership conclusion. |
| **TEC-less InP pluggable** | **Partial.** Eight-channel 400Gb/s/lane / 500m result (`PAP-053`). | **Partial.** BER is reported across stated temperature/channel conditions, but the test uses a TIA-less/PDFA receiver boundary and does not disclose a complete module link. | **Partial.** A high-power DFB and thermo-optic adjustment are present; complete power and lifetime are absent. | **Open.** Fibre attach, module service and customer replacement boundary are undisclosed. | **Partial.** 20–80°C transmission is measured; it is not a product qualification or life distribution. | **Open.** No known-good-module or production test flow is reported. | **Open.** No yield, rework, qualification or cost. | Strong 400G-lane countercase; compare on a matched system boundary before assuming optics must move inward. |
| **SiPh + external laser** | **Partial.** Current CPO routes and external-light records establish an architecture, not a matched 200G/lane engine (`CMP-051`, `PAP-019`, `PAP-022`). | **Open.** No retained common-boundary 200G/lane receiver/link result. | **Partial.** External light creates a separable laser service boundary; delivered loss, lifetime and total power remain incomplete. | **Partial.** Detachable-light and final-fibre-attach routes are disclosed, but engine replacement economics are not (`CMP-051`, `STD-014`). | **Open.** No product-matched engine thermal/lifetime record. | **Partial.** Screening and wafer/interface test routes are identified. | **Open.** Development interface yield is not final-engine yield (`PAP-043`). | Primary switch-CPO diligence route; investigate integration control, not a generic “SiPh winner.” |
| **Heterogeneous / 2.5D SiPh** | **Partial.** 400G aggregate and 1.6T-class engine demonstrations (`PAP-039`, `PAP-045`). | **Partial.** Some measured aggregate link/TDECQ records; not a matched 200G/lane CPO system. | **Open.** Source and full power-tree allocation vary by record. | **Partial.** Glass/interposer/FOWLP records demonstrate potential pre-final-assembly and detachable boundaries (`PAP-028`, `PAP-044`). | **Open.** No comparable full-engine thermal/lifetime data. | **Partial.** Known-good-die and wafer/interposer test mechanisms exist. | **Open.** No final yield waterfall, Cpk, rework or cost. | Process-control option; only earns a value-capture case if it lowers qualified-good-engine cost. |
| **3D CMOS microring / optical-I/O** | **Partial.** Compact monolithic Tx/Rx circuit at 56Gb/s, not 200G/lane (`PAP-021`). | **Open.** No multi-wavelength fibre-reach result at the decision boundary. | **Open.** Off-chip laser and tuning/control burden remain outside reported circuit power. | **Partial.** Connectorized/test-before-final-assembly flow is a credible direction (`PAP-013`). | **Open.** Heater, laser and package thermal qualification are incomplete. | **Partial.** Pre-final-assembly optical/electrical test is demonstrated conceptually. | **Open.** No hybrid-bonding yield or field-life denominator. | Separate accelerator-optical-I/O option; do not use as switch-CPO proof. |
| **TFLN advanced pluggable** | **Partial.** 225GBd transmission demonstration establishes a high-rate modular countercase (`PAP-054`). | **Partial.** 2km transmission is demonstrated; module/chassis boundary is incomplete. | **Partial.** Laser-temperature sweep is reported, not module lifetime/power. | **Open.** No CPO fibre-attach or service boundary. | **Partial.** Laser sweep is not complete module thermal qualification. | **Open.** No retained known-good-module test path. | **Open.** No manufacturing yield, qualification or cost. | Architecture substitution test at 400G/lane, not a direct CPO PIC winner. |

### Comparability controls

Before moving any route from a technology option to a company value-capture conclusion, require a **single product-matched record** to state: (1) lane rate/modulation/reach and BER or TDECQ; (2) total electrical plus optical power including laser, control and thermal tuning; (3) coupling-loss distribution and package/connector boundary; (4) temperature, qualification and sample denominator; (5) test coverage, first-pass yield, rework and final good-engine yield; and (6) supplier content, ASP, warranty and margin boundary. Until then, the appropriate output is an evidence gap—not a score, margin estimate or supplier ranking.

## Technology-to-company diligence mapping

The scorecard changes *what to ask* of the six covered companies; it does not allocate a role that the product evidence has not confirmed.

| Company / boundary | Relevant technology question | Evidence needed before value capture can be assessed |
|---|---|---|
| NVIDIA switch CPO | Does the disclosed SiPh/external-light integration route produce a customer-accepted `SN6810`/`SN6800` engine at a measurable service and yield boundary? | Exact customer SKU, accepted units, engine BOM, supplier allocation, final-engine yield and field-service cost. |
| Broadcom merchant switch CPO | Does the TH6-Davisson COUPE/ELSFP route convert from early-access sampling to qualified volume at an attributable engine boundary? | Customer confirmation, production units, COUPE/engine/laser/package/test ownership, qualified yield and margin stack. |
| Coherent | Which of its SiPh, InP, VCSEL or 400G/lane routes enters a named production engine, and who owns the package/test margin? | Named product allocation, qualified output, yield/rework, share and CPO-specific gross margin. |
| Lumentum | Is external light the constrained content layer after loss, service, lifetime and pricing are reconciled? | Named product/order conversion, laser content/share, delivered-power/lifetime, warranty and realised margin. |
| TSMC | Does COUPE process control extend to an attributable final-engine/package economics boundary? | Customer SKU, supplier scope, final-engine/output data, yield and CPO-specific capacity/margin allocation. |
| Marvell / accelerator optical I/O | Can optical-I/O chiplet density survive package thermal, bonding-yield and customer qualification at commercial scale? | Named XPU/customer, production volume, complete optical power and thermal data, yield and product margin. |

## What this changes in the thesis

1. **Near-term CPO selection is more likely to be won by qualified-engine process control than by a universal PIC-material winner.** The same architecture must close laser delivery, fibre coupling, package thermal path, test coverage, rework and service.
2. **External light is a potential value-control layer, not an automatic margin pool.** It can improve laser service separation while leaving engine/package failure, yield and supplier allocation unresolved.
3. **The 400G/lane boundary remains an option-value question.** TFLN and other advanced-pluggable routes demonstrate that CPO should be tested against improving modular alternatives, not compared only with older retimed modules.
4. **No company ranking follows from this table.** Assigning a supplier winner requires a product-specific engine BOM, qualified output, content share, ASP, margin, warranty and second-source evidence.

## Next evidence needed per route

| Route | Highest-value missing evidence |
|---|---|
| Monolithic InP | Multi-channel link/thermal distribution, final-engine yield, qualification and customer design win. |
| TEC-less InP pluggable | Complete module power/receiver boundary, yield, qualification and a matched system comparison against CPO. |
| SiPh + external laser | Delivered optical-power/loss distribution, laser lifetime, engine yield, ELS/service economics and supplier allocation. |
| Heterogeneous/2.5D | Final-package yield waterfall, cycle time, rework rate, test coverage and ownership of interposer/package margin. |
| 3D optical-I/O | Multi-wavelength high-rate link, hybrid-bonding yield, thermal/lifetime qualification and customer product revenue. |
| TFLN pluggables | Qualified module/chassis power, manufacturing yield and operating-cost comparison against CPO at matched reach/topology. |

## Linked records

- [Supplier-attribution audit](../08-model/supplier-attribution-audit-2026-08-12.md)
- [Scale-out optical-engine benchmark](optical-engine-benchmark.md)
- [PIC-design profit implications](pic-design-profit-implications.md)
- [Academic optical-engine benchmark](../08-model/optical-engine-academic-benchmark.md)
- [Packaging reliability benchmark](packaging-reliability-benchmark.md)
- [Linear-drive boundary benchmark](../02-architecture/linear-drive-boundary-benchmark.md)
