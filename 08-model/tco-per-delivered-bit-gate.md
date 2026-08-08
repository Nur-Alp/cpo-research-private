# Total-cost-per-delivered-bit gate

**Owner:** Nur Alpys  
**Status:** Framework only; no company forecast values populated  
**Scope:** Matched 102.4T switch-side CPO, LPO, advanced/retimed pluggables and later 400G/lane alternatives  
**As of:** 2026-08-08

## Decision question

Does CPO create a lower qualified cost per useful delivered bit than the best improving alternative at the same switch bandwidth, reach, workload and service boundary?

Power savings alone cannot answer this. A CPO design may reduce electrical-interface watts while increasing package yield risk, repair blast radius, qualification cost or spare inventory. Conversely, a pluggable design may consume more power while preserving replaceability and multi-source competition.

## Common comparison boundary

Every architecture case must use the same:

- Switch bandwidth and port count
- Lane rate and modulation target
- Reach, fibre plant and receiver margin
- BER/FEC and temperature requirement
- Workload/utilisation assumption
- Measurement point for power and cooling
- Service period, availability target and spare policy
- Economic life and discount/amortisation convention

The current reference case is 102.4 Tb/s, 64 × 1.6T ports, 200G/lane and up to 500 m. The [102.4T power model](102.4t-switch-side-power-model.md) supplies scenario power only; it does not clear this TCO gate.

## Formula

For architecture `a` over an economic period `T`:

```text
qualified total cost_a
= annualised hardware and packaging cost_a
 + annual energy and cooling cost_a
 + expected failure, spare and repair cost_a
 + qualification, R&D and support cost_a
 + attributable capacity/test capital recovery_a
```

```text
useful delivered bits_a
= rated bandwidth
 × utilisation
 × service availability
 × operating time
 × reach/quality acceptance factor
```

```text
TCO per delivered bit_a
= qualified total cost_a / useful delivered bits_a
```

The reach/quality factor must not be used to hide a failed BER or FEC requirement. If an architecture cannot meet the required link margin, it is not a higher-cost case; it is outside the qualified comparison.

## Required inputs and current status

| Input | Unit | CPO | LPO / advanced pluggable | Retimed pluggable | Evidence status |
|---|---|---:|---:|---:|---|
| Optical engine/module ASP | $/1.6T port or system | Unknown | Unknown | Partial public demos only | Blocked |
| Final good-unit yield | % | Unknown | Unknown | Unknown | Blocked |
| Fibre attach / connector cost | $/port | Unknown | Module boundary varies | Included in module if applicable | Blocked |
| Laser, TEC and control power | W/port | Boundary incomplete | Boundary varies | Module demonstrations available | Partially bounded |
| Host SerDes / electrical reach power | W/port | Unknown | Unknown | Unknown | Blocked |
| Cooling and conversion overhead | W/system | Scenario only | Scenario only | Scenario only | Scenario assumption |
| Utilisation | % | Unknown | Unknown | Unknown | Must be common assumption |
| Service availability | % | Unknown | Unknown | Unknown | Field data absent |
| Failure/repair/spares cost | $/system-year | Unknown | Unknown | Unknown | Blocked |
| Qualification and support cost | $/system-year | Unknown | Unknown | Unknown | Blocked |
| Attributable capex recovery | $/system-year | Unknown | Unknown | Unknown | Blocked |
| Useful delivered bits | bits/year | Not calculated | Not calculated | Not calculated | Requires common utilisation/availability |

## What can be used now

The current 102.4T scenario provides a bounded operating-power sensitivity:

| Scenario | CPO facility power | LPO facility power | Fully retimed facility power | Evidence boundary |
|---|---:|---:|---:|---|
| Optimistic | 465.8 W | 474.3 W | 1,630.3 W | Analyst scenario using published or derived per-port inputs |
| Central | 601.0 W | 667.8 W | 2,003.5 W | Analyst scenario; not measured chassis data |
| Stress | 756.4 W | 945.5 W | 2,836.4 W | Analyst stress case |

At the central boundary, CPO's modeled advantage over LPO is only 66.8 W of facility-adjusted switch power. That difference can be economically erased by higher CPO package cost, yield loss, service inventory, warranty cost or unmodelled laser/control power. The approximately 1,402.5 W advantage over fully retimed optics is materially more robust to small boundary changes. These are model implications, not observed TCO outcomes.

## Gate rules

The comparison may enter a base-case investment model only when:

1. Each architecture meets the same BER/FEC, reach and thermal requirement.
2. Product cost includes the complete relevant optical/electrical boundary, not only the PIC or module headline.
3. Final good-unit yield and rework are defined at the same unit boundary.
4. Service, spares, repair time and failure allocation are included.
5. Power is measured or bounded at the same inlet/system boundary.
6. Capex and qualification costs are attributed consistently.
7. Utilisation and availability assumptions are stated before comparing delivered bits.

Until these conditions are met, report only the power sensitivity and keep `TCO per delivered bit = not yet calculable`.

## Decision implication

The most important unresolved commercial question is not whether CPO can save watts. It is whether the small CPO-versus-LPO power delta survives the full qualified cost stack while the much larger CPO-versus-retimed advantage remains relevant to the customer's topology. This is why the optical-engine profit-pool thesis prioritises final yield, serviceability, supplier share and price—not isolated PIC performance.

The service-cost boundary is now explicit in [Service and failure-domain cost model](service-and-failure-domain-cost-model.md). ELSFP can make the light source replaceable, but it does not establish replacement economics for the PIC/package, delivery fibre, connector, control map, cooling or correlated package failures. Those terms remain blocked in the TCO identity.

## Linked controls

- [102.4T switch-side optical power model](102.4t-switch-side-power-model.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Engine yield waterfall template](engine-yield-waterfall-template.md)
- [CPO customer-proof register](customer-proof-register.md)
- [Service and failure-domain cost model](service-and-failure-domain-cost-model.md)
- [CPO decision-output completion audit](../00-scope/decision-output-completion-audit.md)
