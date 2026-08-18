# Common-boundary alternatives audit — 12 August 2026

**Status:** Private decision control; no architecture winner or adoption forecast
**Scope:** Retimed pluggables, LPO/RTLR, NPO/OBO and switch-side CPO

## Audit result

The alternatives scorecard is complete as a **decision framework**, but no
route has a fully matched public system record at 200G/lane or 400G/lane. The
current evidence supports conditional coexistence rather than a universal CPO
winner.

| Required comparison field | Current evidence | Status | Why it remains open |
|---|---|---|---|
| Same ASIC, port count and lane rate | Product and standards records cover different platforms and generations | Open | No four-way same-SKU pair |
| Reach, host loss and return loss | RTLR/LPO budgets and component/link demonstrations exist | Partial | No common BER/FEC/reach test across all four routes |
| Inlet power including conversion/cooling | Bounded CPO/alternative scenarios and one historical CPO comparison | Partial | Measurement boundaries, cooling and chassis conditions are not common |
| Thermal and ambient qualification | Package, module and standard temperature boundaries exist | Partial | No matched qualified system population |
| Final yield, rework and test | Research vehicles, supplier test infrastructure and process claims | Open | No product-matched lot waterfall for any route |
| Service, MTTR, spares and warranty | Pluggable/RTLR modularity and CPO ELSFP boundaries | Partial | No restored-port cost or field-return comparison |
| Supplier share and complete cost stack | Architecture/content maps | Open | No realised ASP, share, margin or price-down record |

## Evidence discipline

- Component pJ/bit, module wattage or vendor power percentages are mechanism or
  scenario inputs, not system TCO outcomes.
- A 100G LPO result does not clear a 200G/400G LPO gate; a historical TH5 CPO
  result does not clear TH6 or NVIDIA exact-SKU economics.
- ELSFP or a detachable connector proves only a replaceable boundary; it does
  not prove engine/package/ASIC repairability or lower lifecycle cost.
- A standards contribution or roadmap is not a qualified customer product.
- The CPO-versus-LPO central power difference remains a sensitivity, not a
  measured economic advantage; hardware, yield, service and qualification can
  reverse it.

## Architecture-specific readout

| Route | Current strength | Evidence needed before it can invalidate or confirm the CPO timing view |
|---|---|---|
| Retimed pluggable | Strongest modularity, interoperability and service benchmark | Matched 200G/400G system with lower qualified cost per restored port |
| LPO / RTLR | Live electrical-margin countercase retaining a modular boundary | End-to-end target-rate BER/FEC, power, yield, diagnostics and repeat production |
| NPO / OBO | Plausible intermediate integration/service boundary | Qualified short-channel product with measured margin, field service and cost |
| Switch-side CPO | Strongest disclosed 200G product/timing signal | Exact-SKU customer acceptance, repeatability, final-engine yield/service and matched TCO |

## Decision impact

The current statement remains:

> Switch-side 200G/lane CPO has the strongest disclosed timing signal, but no
> architecture has yet cleared the complete electrical, power, manufacturing,
> service and economic comparison.

On 13 August, the OIF CEI-448G framework was added as a narrow topology and
interoperability control. It distinguishes near-package NPO from on-package
CPO and lists the electrical, mechanical, management and multi-vendor-testing
work required for interoperability (`STD-015`, `CLM-563`). It does **not** add
any product qualification, service, unit or economic record. The audit still
makes the missing matched evidence explicit and keeps the report from turning
an illustrative power table into an adoption or profit conclusion.

Related controls: [common-boundary scorecard](system-boundary-comparison-scorecard.md), [substitution matrix](substitution-and-falsification-matrix-2026-08-12.md), [TCO gate](../08-model/tco-per-delivered-bit-gate.md), [matched comparison acquisition specification](../09-primary-research/matched-architecture-comparison-acquisition-spec.md), and [public-release manifest](../00-scope/public-release-manifest-2026-08-12.md).
