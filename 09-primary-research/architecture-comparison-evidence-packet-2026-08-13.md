# Architecture comparison evidence packet

**Status:** Private intake control; not an architecture recommendation or TCO result  
**As of:** 2026-08-13  
**Scope:** Retimed pluggable, LPO/RTLR, NPO/OBO and switch-side CPO at 200G and prospective 400G per lane

## Purpose

The existing evidence supports a conditional coexistence view. This packet
sets a higher admission bar for future reports that claim one architecture
beats another. It is deliberately organised around a **qualified, serviceable
delivered port**, not a component, module or switch-chip claim.

## Mandatory identity sheet

The following must be completed before a comparison is read as more than a
mechanism-level result:

| Field | Record exactly | Reject if missing or mismatched |
|---|---|---|
| Architecture | Retimed, LPO, RTLR, NPO/OBO or CPO; exact implementation | A route label without retimer/DSP, optics and service-boundary placement |
| Exact product | ASIC/stepping, optics/engine or module revision, firmware | Product family or different-generation comparison |
| Capacity | Active ports, lane rate, aggregate bandwidth and lanes per port | A partially populated system compared with a full one |
| Link | Reach, fibre/cable, connector count, channel loss/return loss and endpoint definition | Best-channel result or a different channel |
| Operating point | Workload, utilisation, duration, ambient, cooling mode and set points | Idle, different ambient, or unstated cooling boundary |
| Quality target | Pre/post-FEC BER, FEC, flap/error definition and availability objective | A power result without an equivalent error objective |

## Four evidence modules

All modules must use the same identity sheet. A source can clear one module
without clearing the full comparison.

| Module | Required fields | What it can establish | What it cannot establish alone |
|---|---|---|---|
| E — electrical and thermal | Channel/return loss, BER/FEC, error distribution, inlet/package/faceplate temperatures, cooling boundary | Link feasibility and a bounded power/thermal comparison | Yield, lifecycle cost, serviceability or supplier economics |
| M — manufacturing and qualification | Input and accepted-unit denominator, test coverage/time, yield, rework/scrap, stress/sample/pass rates | Cost-risk and quality comparison at the stated unit | Field reliability, price/margin or operating TCO |
| S — service and reliability | Failure unit, service procedure, MTTR, spare ratio, warranty owner/reserve, exposure and returns | Cost per restored port and failure-domain comparison | Purchase price, supplier margin or broad deployment share |
| C — commercial and cost | Product price/content, installation, energy/cooling, supplier structure/share, capex, price-down and cancellation terms | A product-specific total-cost and value-capture comparison | A universal architecture winner outside the stated product/time boundary |

## Promotion rules

| Completed modules | Maximum permitted conclusion |
|---|---|
| E only | “The stated implementation meets/misses a link and power/thermal boundary.” |
| E + M | “The stated implementation has a bounded qualification/manufacturing comparison.” |
| E + M + S | “The stated implementation has a qualified cost-per-restored-port comparison.” |
| E + M + S + C | “A product-specific TCO comparison is eligible, subject to source and calculation audit.” |

No row authorises a general adoption-share, company-margin or investment call.

## Current evidence disposition

| Architecture | E | M | S | C | Controlled conclusion |
|---|---|---|---|---|---|
| Retimed pluggable | Partial modular/electrical baseline | Open at matched 200G/400G | Modular failure boundary known; cost/field record open | Open | Serviceability benchmark, not matched higher-rate winner |
| LPO / RTLR | 100G measured; higher-rate conditional/modelled | Open | Modular boundary plausible; diagnostics/field cost open | Open | Live electrical-margin countercase |
| NPO / OBO | Mechanism/short-channel rationale | Open | Replaceability/interface record open | Open | CPO-deferral hypothesis |
| Switch-side CPO | Defined 200G products and bounded power examples | Process mechanisms, not final yield | Light-source boundary exists; engine/package service open | Open | Strongest disclosed timing signal, not proven lifecycle winner |

## Immediate decision-changing records

1. **200G:** Same 102.4T-class ASIC and port count, retimed versus CPO at
   equal reach/FEC/ambient/workload, with inlet power and cooling included.
2. **200G service:** Field or qualification record that distinguishes module,
   laser, engine, package and ASIC failures, plus MTTR/spares/warranty.
3. **400G:** Measured 212.5-GBd end-to-end link for a modular and short-path
   alternative, with the same quality and temperature boundary.
4. **Economics:** Matched final yield/rework and product-price/supplier-share
   record. Without it, a power delta remains a sensitivity—not TCO.

## Explicit rejection controls

Do not accept any of the following as a full architecture result:

- pJ/bit, module watts or an unspecified vendor percentage;
- a CPO product announcement or “production” statement;
- optical-engine, modulator or SerDes-only result;
- a lab link using different FEC, reach, temperature, lane rate or ASIC;
- a replaceable ELSFP/laser interface without the package/engine repair path;
- a consolidated margin, generic capacity expansion, or partner list; or
- claimed power savings without cooling, service and qualification boundaries.

Related controls: [matched architecture-comparison specification](matched-architecture-comparison-acquisition-spec.md), [common system-boundary scorecard](../02-architecture/system-boundary-comparison-scorecard.md), [substitution matrix](../02-architecture/substitution-and-falsification-matrix-2026-08-12.md), and [TCO per delivered-bit gate](../08-model/tco-per-delivered-bit-gate.md).
