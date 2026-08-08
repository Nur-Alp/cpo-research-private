# Service and failure-domain cost model

**Status:** Evidence-gated model; no field-rate assumptions populated  
**As of:** 2026-08-08  
**Scope:** Switch-side CPO, NPO, ELSFP and advanced-pluggable service economics

## Decision question

Does moving the laser or optical engine inward reduce total outage and service cost enough to offset larger package blast radius, fibre/connector faults, spares, controls and repair complexity?

## Failure domains

| Domain | Replaceable boundary | What the evidence establishes | Cost input still missing |
|---|---|---|---|
| Faceplate pluggable | Module can be removed without opening the package | Mature serviceability/interchangeability is an architectural advantage; exact field rates are not in the reviewed packet | Module failure rate, MTTR, spare ratio, labour and service contract |
| ELSFP / external light | Blind-mate external-light module | OIF defines thermal classes, 10-year field-life requirement and durability tests; ELS does not repair PIC/package/fibre faults [CLM-287–CLM-290] | Qualified laser lifetime distribution, optical-loss drift, ELS-to-OE fault isolation, MTTR, warranty and spare policy |
| Socketable optical engine | Engine may be tested/replaced before or after switch assembly | Intel and academic records support a test/rework mechanism; no production engine-service population is disclosed [PAP-003; PAP-013] | Socket/engine replacement cycle, inventory, mating lifetime, package yield, field rate and warranty |
| Fixed CPO package | ASIC, PIC/package and fibre attach are integrated | Short electrical path and density are plausible; a failed package can create a larger service blast radius | Package failure rate, full-switch replacement cost, downtime, spares and platform warranty allocation |
| NPO/OBO module | Short electrical module intended to remain replaceable | Standards proposal identifies an exposed interoperability/service boundary as a potential CPO-deferral benefit; no ratified deployment evidence [CLM-091–CLM-092] | Measured 400G service procedure, qualification, multi-vendor availability, MTTR and module ASP |
| Passive fibre/connector path | Depends on connector and chassis access | External-light management explicitly leaves delivery-fibre faults outside ELS detection; detachable connector prototypes show feasibility, not field reliability [CLM-097; CLM-098] | Fault-isolation coverage, contamination/wear rate, loss drift, replacement labour and warranty owner |

## Cost identity

For architecture `a`, over a defined fleet and service period:

```text
expected service cost_a
= failure events_a × (replacement material_a
                     + service labour_a
                     + logistics_a
                     + downtime cost_a)
  + spare inventory carrying cost_a
  + qualification / monitoring / control cost_a
```

For a multi-domain CPO system, split failure events by component rather than applying one engine failure rate:

```text
failure events
= laser/ELS + fibre/connector + PIC/engine
  + package/ASIC + control/map + cooling
```

The model must preserve correlated failures. A package or cooling failure can disable many optical channels simultaneously; independent module failure assumptions cannot be used for that case.

## What can be compared now

| Question | Current evidence-supported answer |
|---|---|
| Is ELSFP a real service boundary? | Yes, as a standards-defined external-light interface with explicit durability and environmental requirements; not proof of complete-engine service economics. |
| Does ELSFP make CPO fully replaceable? | No. The PIC/package, fibre path, connector, control map and host package remain separate failure domains. |
| Do pluggables retain serviceability value? | Yes as an architectural feature, but its monetary value requires field failure, MTTR, spares and downtime data. |
| Can socketable/NPO routes reduce blast radius? | Potentially; current records are demonstrations/proposals without production service populations. |
| Can service economics decide CPO vs LPO? | Yes in principle, but no public record supplies the matched rates and costs needed to calculate it. |

## Required evidence before TCO calculation

1. Failure-rate distributions by laser, fibre/connector, engine/package, control and cooling domain.
2. Replacement unit, labour, logistics and downtime cost for each boundary.
3. MTTR, spare ratio, safe replacement procedure and warranty allocation.
4. Environmental/lifetime qualification tied to the exact deployed SKU.
5. Correlated-failure and availability model for multi-channel CPO packages.
6. Customer service records or field-return data for CPO, ELSFP, NPO and pluggable alternatives.

## Current conclusion

Serviceability is a plausible CPO/NPO differentiator but not an established economic advantage. PAP-042 strengthens the engineering reliability boundary with full-module reflow and JEDEC stress evidence, while also showing that early process versions failed before later process/material changes; it supplies no fleet failure or repair-cost distribution. ELSFP improves the replaceability of the light source, while leaving optical-engine, fibre, package and control failures unresolved. Until failure and cost distributions are disclosed, service cost must remain an explicit blocked input in the [TCO-per-delivered-bit gate](tco-per-delivered-bit-gate.md), not a qualitative claim converted into a margin adjustment.

## References

- [External-light serviceability boundary](../03-components/external-light-serviceability-boundary.md).
- [Packaging, fibre-attach and serviceability benchmark](../03-components/packaging-reliability-benchmark.md).
- [NPO interoperability boundary](../02-architecture/npo-interoperability-boundary.md).
- [Optical-engine yield waterfall](engine-yield-waterfall-template.md).
- OIF ELSFP 2.0, `STD-011`; OIF ELS/OE management, `STD-006`; claim ledger `CLM-091`, `CLM-097`–`CLM-098`, `CLM-287`–`CLM-290`.
