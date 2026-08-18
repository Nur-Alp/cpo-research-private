# Matched architecture-comparison acquisition specification

**Status:** Private evidence-collection control; not a forecast or product recommendation  
**As of:** 12 August 2026  
**Decision:** Under what conditions does CPO beat retimed pluggables, LPO/RTLR or NPO on a qualified cost-per-delivered-bit and cost-per-restored-port basis?

## Why this record is required

The current technical record supports a conditional view: CPO can reduce electrical path length and can have a large modeled power advantage versus fully retimed optics, while the modeled CPO-versus-LPO difference is small enough to be erased by incomplete laser, yield, service or package-cost boundaries. **A component pJ/bit figure** or an unmatched vendor chassis claim does not resolve that choice.

The minimum useful evidence is therefore one **same-boundary** comparison. It may come from an operator, OEM, platform owner, standards interoperability event, qualified manufacturing record or a reproducible academic/system demonstration. A source may establish only part of the table below; it must not be presented as a full architecture winner until all required fields align.

## Configuration identity — all fields required

| Field | Required recording rule | Why it prevents a false comparison |
|---|---|---|
| Product / architecture | Exact SKU/configuration for each of retimed, LPO/RTLR, NPO and CPO; state whether a case is unavailable | Prevents a product-family or alternative-generation transfer. |
| ASIC and SerDes | Same switch ASIC/stepping, SerDes mode and firmware where possible | Separates optical architecture from ASIC-power and software changes. |
| Switch configuration | Same port count, aggregate bandwidth, lanes per port and optical attach rate | A partially populated CPO system cannot be compared with a fully populated pluggable system. |
| Link boundary | Same reach, fibre/cable type, electrical loss, return loss, connector count and endpoint definition | Avoids attributing a shorter/easier channel to architecture superiority. |
| Operating condition | Same traffic/workload, utilisation, temperature/ambient and run duration | Prevents an idle or cool-system result from being treated as production power/reliability. |
| Error / quality | Same pre-FEC BER target, FEC mode, post-FEC criterion and link-flap/failure definition | A power result is not useful if one configuration is less qualified. |

## Measured system and commercial fields

| Required field | Unit / definition | Minimum acceptable evidence | Explicit non-qualifier |
|---|---|---|---|
| Inlet power | W at stated workload, including defined conversion/cooling boundary | Instrumented system/chassis measurement for every compared architecture | Module-only watts, pJ/bit, or an unbounded vendor percentage. |
| Cooling / thermal | Inlet/ASIC/package/faceplate temperatures; fan/pump or liquid-cooling contribution | Same ambient and cooling set point with stated measurement locations | A module thermal specification or a package simulation alone. |
| Electrical performance | Channel loss/return loss, BER/FEC and run duration | Same lane rate and end points, with error and flap distribution | A best-channel eye or a different FEC/temperature condition. |
| Yield / rework | Final accepted module/engine or system numerator and denominator; rework disposition | Lot or qualification record tied to configuration | Wafer, subassembly or engineering-sample yield only. |
| Service boundary | Failure unit, repair procedure, spare scope, MTTR and warranty owner | Operator/OEM service or qualification record | “ELSFP is replaceable” without the engine/package failure workflow. |
| Cost stack | Module/engine, laser, attach, package, install, qualification, repair/spares and capital-recovery boundary | Contract, product price, attributable cost record, or explicitly separated private primary research | Consolidated company margin or a presumed supplier ASP. |
| Supplier structure | PIC/engine, EIC, laser, attach, package, connector and test responsibility plus qualified share | Product-linked BOM, qualification or contract | Ecosystem/partner list or trade-show collaboration. |

## Decision outputs permitted by evidence completeness

| Completeness state | Permitted conclusion | Prohibited conclusion |
|---|---|---|
| Electrical fields only | A route meets or misses a stated electrical/BER boundary | Lower system power, lower TCO, better reliability or a profit winner. |
| Electrical plus inlet-power/thermal fields | A route has lower measured power at that stated system boundary | Universal power advantage, deployment leadership or better total cost. |
| Adds yield and service fields | A route has a bounded qualified-cost / restoration-risk comparison | Supplier margin or company investment conclusion without content and price. |
| Adds full cost and supplier structure | A product-specific TCO comparison may be modelled and linked to supplier economics | A broad architecture/company ranking beyond the stated SKU, customer and time period. |

## Minimum decision-changing tests

### 200G/lane Ethernet scale-out

1. Same 102.4T-class switch ASIC, port count and 1.6T port configuration.
2. At least retimed and CPO measured at the same reach/FEC/ambient/workload; add LPO/RTLR and NPO where technically available.
3. Inlet system power, optical-interface power, cooling contribution, BER/FEC and link-flap statistics captured over a stated duration.
4. A service/repair statement that distinguishes module, laser, engine, package and ASIC failure domains.

This can determine whether the large CPO-versus-retimed modeled delta survives a real system boundary and whether the smaller CPO-versus-LPO/RTLR delta is material.

### 400G/lane Ethernet scale-out

1. A measured 212.5-GBd/400G end-to-end link—not a component result or model—with stated loss/return-loss, reach, BER/FEC and temperature.
2. A short-reach NPO/CPO boundary and an available pluggable/linear alternative tested at comparable endpoints.
3. Package/engine thermal, yield, test/rework and replaceability record before translating the electrical result into a deployment or profit claim.

## Intake protocol

1. Retain the complete readable original source or its permitted PDF, plus a Markdown evidence note with URL, publication date and access date.
2. Extract each field above verbatim into a configuration record; label absent fields **open**, never zero.
3. Add a source-log row and claim-ledger entries only when the source changes a decision gate.
4. Reconcile the result against the [common scorecard](../02-architecture/system-boundary-comparison-scorecard.md), [linear-drive benchmark](../02-architecture/linear-drive-boundary-benchmark.md), [NPO boundary](../02-architecture/npo-interoperability-boundary.md) and [TCO gate](../08-model/tco-per-delivered-bit-gate.md).
5. Run `python3 scripts/validate-private-research.py` before changing any conclusion. No publish, commit or push without Nur Alpys’s explicit instruction.

## Current status

No retained public source clears this specification. The most useful existing evidence is: 100G LPO system operation; conditional/modelled 200G LPO boundaries; a bounded TH5 CPO-versus-pluggable power comparison; and component/model-level 400G-lane evidence. They establish the decision map, not a qualified architecture winner.
