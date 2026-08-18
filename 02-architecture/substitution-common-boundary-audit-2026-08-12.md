# Substitution common-boundary audit — 12 August 2026

**Status:** Private architecture-control document; no adoption or winner claim
**Purpose:** Check that retimed pluggables, LPO/RTLR, NPO/OBO and switch-side CPO are compared on the same delivered-port decision boundary.

## Audit verdict

The existing comparison is directionally symmetric and correctly concludes
conditional coexistence. It is not yet a matched architecture experiment:
there is no single ASIC, port count, lane rate, reach, BER/FEC, cooling,
qualification, service and economic record covering all four routes. The
current 200G CPO timing view is therefore an evidence-gated inference, not a
technology inevitability or market-share forecast.

## Controlled delivered-port boundary

The unit of comparison is **one accepted and serviceable delivered port over a
defined operating period**, not one PIC, module or switch chip. Every route
must be evaluated with the following fields held constant:

| Boundary field | Required control | Why it matters |
|---|---|---|
| ASIC and port count | Same ASIC generation, radix and active ports | Prevents a larger or newer switch from masquerading as an architecture advantage |
| Lane rate and reach | Same gross lane rate, fibre/cable type and distance | Prevents 100G or short-reach results from clearing a 200G/400G gate |
| Electrical channel | Same endpoints, insertion/return loss, crosstalk, equalisation and retiming placement | Determines whether LPO/RTLR can actually replace inward integration |
| Error target | Same pre-FEC BER, FEC mode, link-flap/error distribution and uptime target | Connects lab eye/TDECQ results to usable service performance |
| Power boundary | ASIC-side, module/engine, laser, DSP/retimer, conversion and cooling included | Avoids comparing module-only watts with a complete switch or rack |
| Thermal boundary | Same ambient/case temperature, liquid/air cooling and thermal allocation | CPO concentration can move cost from optics into package/cooling |
| Qualification | Same sample size, stress tests, accepted-lot criteria and environmental life | A demonstration cannot substitute for a qualified production population |
| Service | Same failure domains, MTTR, spares, labour, warranty and restored-port target | Replaceable laser is not equivalent to replaceable module or engine |
| Economics | Same BOM scope, ASP/transfer price, supplier share, yield/rework and price-down | Technical indispensability does not establish profit capture |

## Route-by-route symmetry check

| Route | Strongest retained evidence | Boundary still missing | Permitted use |
|---|---|---|---|
| Retimed pluggable | Mature modular/interoperability and service boundary; standards-level host-loss controls | Matched 200G/400G power, qualification, field cost and same-ASIC comparison | Serviceability benchmark and live countercase |
| LPO / RTLR | 100G measured LPO and 200G/400G models/standards; RTLR preserves hot-plug boundary | Target-rate end-to-end BER/FEC, power/cooling, yield, diagnostics and repeat production | Conditional electrical-margin countercase |
| NPO / OBO | Plausible short-channel and intermediate service boundary | Ratified/qualified interface, complete module, field service and cost per restored port | CPO-deferral hypothesis |
| Switch-side CPO | Strongest disclosed 200G product/timing signal; ELSFP/detachable-light process concepts | Exact customer acceptance, final-engine yield, engine/package repair, matched TCO and economics | Timing lead hypothesis, not universal winner |

No route has a complete row. The asymmetry is therefore in evidence maturity,
not in a justified score: CPO has stronger product announcements, while
pluggables have stronger service/interoperability history. Neither fact alone
answers lifecycle economics.

## Falsification tests

The current CPO timing inference should be downgraded if any of these are
demonstrated at the same delivered-port boundary:

1. Retimed, LPO/RTLR or NPO reaches the target rate and error objective with
   lower total cost per accepted/restored port.
2. CPO final-engine yield, rework, warranty or chassis-level repair creates a
   higher lifecycle burden than a field-replaceable alternative.
3. A customer accepts the CPO product only for evaluation while an alternative
   enters repeat production at the same topology.
4. CPO power savings disappear after cooling, conversion, laser service and
   failure-domain costs are included.
5. The supposed CPO advantage depends on a different ASIC, port count, reach,
   FEC or temperature boundary than the alternative.

## Evidence acquisition priority

The highest-value missing record is a same-ASIC 200G comparison containing:

- full channel and return-loss map;
- pre-FEC BER/FEC and error distribution;
- inlet power including conversion and cooling;
- final module/engine yield and rework;
- field replacement workflow, MTTR, spares and warranty; and
- product-linked price, supplier share and margin boundary.

Until that record exists, preserve the conclusion as:

> Switch-side 200G/lane CPO has the strongest disclosed timing signal, while
> retimed pluggables, LPO/RTLR and NPO remain live conditional alternatives.

This is an inference with explicit falsification conditions, not a forecast of
adoption or profit-pool leadership.

Related controls: [common-boundary scorecard](system-boundary-comparison-scorecard.md), [alternatives evidence audit](common-boundary-evidence-audit-2026-08-12.md), [substitution matrix](substitution-and-falsification-matrix-2026-08-12.md), and [TCO gate](../08-model/tco-per-delivered-bit-gate.md).

The operative intake checklist is the [architecture comparison evidence packet](../09-primary-research/architecture-comparison-evidence-packet-2026-08-13.md). It separates electrical/thermal, manufacturing, service and commercial evidence so a strong component or power result cannot be promoted into an unqualified lifecycle conclusion.
