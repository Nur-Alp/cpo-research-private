# PIC-engine viability promotion gate — 13 August 2026

**Status:** Private decision control; not a technology ranking or investment conclusion  
**Decision unit:** One customer-accepted, serviceable scale-out optical engine at a defined 200G/lane or 400G/lane system boundary

## Purpose

The PIC scorecard shows which material/device routes are technically credible. This gate decides whether a route may be promoted from a laboratory or process result into a scale-out engine thesis. It makes performance necessary but never sufficient: a route must also close integration, production, service and economic boundaries.

## Promotion ladder

| Stage | Required proof | Silicon photonics + ELS | InP | TFLN | Heterogeneous integration |
|---|---|---|---|---|---|
| 1. Device feasibility | Relevant modulation/receiver/coupling result at a stated test boundary | Present | Present | Present | Present across subassemblies |
| 2. Engine performance | Multi-channel engine or module at target lane, reach, BER/FEC and temperature | Partial | Partial | Partial at advanced-pluggable boundary | Partial |
| 3. Complete integration | Laser, EIC, PIC, coupling, package, thermal path and test mapped to one product | Partial | Open | Open | Partial, ownership open |
| 4. Qualified production | Lot/revision denominators for starts, test, rework, accepted units and environmental qualification | Open | Open | Open | Open |
| 5. Serviceable deployment | Customer SKU, installed base/exposure, replacement procedure, MTTR and warranty boundary | Open | Open | Open | Open |
| 6. Economic attribution | Product-matched share, price, yield/rework, warranty, margin and capex/R&D boundary | Open | Open | Open | Open |

**Current result:** all four routes are at stages 1–3 only. None is eligible for a supplier-profit, revenue, EPS, valuation or “technology winner” claim.

## Decision gates

| Gate | Minimum comparison requirement | Why it matters |
|---|---|---|
| Performance | Same lane rate, reach, BER/FEC, active channels, temperature and optical/electrical power boundary | Prevents a best-channel or device pJ/bit result from being compared with a complete engine |
| Integration | One declared laser/EIC/PIC/coupling/package/test/service bill of materials | Prevents omitted laser, tuning, packaging or test content from disappearing economically |
| Production | Product/lot starts → screen → attach/package → final test → rework → accepted output | Makes yield, scrap and cycle-time claims auditable |
| Service | Defined replaceable unit, fault isolation, spares, MTTR, field exposure and warranty ownership | Tests cost per restored port, not only cost per assembled engine |
| Economics | Product-matched content/share, realised ASP, price-down, margin, capex and R&D | Determines whether technical indispensability creates profit |

## What would change the technology read-through

| Route | Upgrade condition | Downgrade / countercase condition |
|---|---|---|
| Silicon photonics + external light | Exact 200G-lane CPO SKU with a complete supplier/engine map, qualified output, field service and economics | A matched modular architecture supplies the same delivered-port power, reach and reliability at lower qualified/restored-port cost |
| InP | A complete engine/module clears production/qualification and customer service economics at a matched 200G or 400G boundary | Compound-device yield, thermal/lifetime or supply economics prevent qualified module scale |
| TFLN | A qualified high-rate module demonstrates full power, packaging, service and manufacturing economics at the matched boundary | Laser/control, package/attach or yield burden erodes its laboratory rate advantage |
| Heterogeneous integration | One named product shows lower final-good-engine cost, through known-good test, attach/package yield and rework, with attributable economics | Thermal/assembly yield, test cost or ownership fragmentation consumes the integration benefit |

## Relationship to CPO alternatives

At 200G/lane, silicon photonics + external light is the principal current switch-CPO process route. At 400G/lane, InP and TFLN advanced-pluggable demonstrations are countercases: they can delay or narrow CPO adoption only if they pass the same delivered-port, service and qualified-cost tests. Heterogeneous integration is not a separate optical material winner; it is an integration, known-good-test and final-engine-cost question.

This gate therefore does **not** select a universal architecture. It sets the evidence needed to distinguish a potentially attractive PIC from a customer accepted, serviceable and economically attributable engine.

Related controls: [PIC technology decision scorecard](pic-technology-decision-scorecard.md), [PIC-to-engine investment gates](pic-to-engine-investment-gates-2026-08-12.md), [manufacturing production-evidence checklist](../09-primary-research/manufacturing-production-evidence-checklist.md), [production-record intake schema](../09-primary-research/production-record-intake-schema-2026-08-13.md), and [common system-boundary scorecard](../02-architecture/system-boundary-comparison-scorecard.md).
