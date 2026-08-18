# 102.4T power-to-cost sensitivity

**Status:** Illustrative operating-cost sensitivity; not a TCO forecast  
**Scope:** Central 102.4T switch-side scenario, CPO versus LPO and fully retimed optics  
**As of:** 2026-08-09

## Purpose

The central power model reports approximately 601.0 W for CPO, 667.8 W for LPO and 2,003.5 W for fully retimed optics at the stated facility boundary. This note converts those differences into annual electricity cost so the TCO model can test whether power savings are large enough to offset package, yield, service and capex differences.

These are arithmetic sensitivities. They do not include demand charges, cooling-system nonlinearities, rack constraints, utilisation variation or measured chassis power.

## Assumptions

- Operating hours: 8,760 per year
- Utilisation / average load factor: 80%
- Electricity prices tested: $0.08, $0.12 and $0.20 per kWh
- Facility-power boundary: same as the central 102.4T scenario

## Annual energy cost

| Architecture | Average facility power | Annual energy at 80% load | Cost at $0.08/kWh | Cost at $0.12/kWh | Cost at $0.20/kWh |
|---|---:|---:|---:|---:|---:|
| CPO | 601.0 W | 4,212 kWh | $337 | $505 | $842 |
| LPO | 667.8 W | 4,680 kWh | $374 | $562 | $936 |
| Fully retimed | 2,003.5 W | 14,041 kWh | $1,123 | $1,685 | $2,808 |

## Savings versus CPO

| Comparator | Power delta versus CPO | Annual energy saving at 80% load | Saving at $0.08/kWh | Saving at $0.12/kWh | Saving at $0.20/kWh | Five-year saving at $0.12/kWh |
|---|---:|---:|---:|---:|---:|---:|
| LPO | 66.8 W | 468 kWh | $37 | $56 | $94 | $281 |
| Fully retimed | 1,402.5 W | 9,829 kWh | $786 | $1,179 | $1,966 | $5,897 |

## Interpretation

1. In the central scenario, CPO's modeled energy advantage over LPO is only about **$56 per switch-year at $0.12/kWh**, or approximately **$281 over five years**, before cooling interactions.
2. The modeled CPO advantage over fully retimed optics is much larger—approximately **$1,179 per switch-year** at the same price and load—but still must be compared with complete hardware, service, yield and capex differences.
3. A modest CPO package premium, additional spare inventory, one replacement event or a small yield penalty could erase the modeled CPO-versus-LPO energy benefit.
4. Electricity economics can materially favour CPO against fully retimed optics while failing to distinguish CPO from LPO. This is consistent with the broader thesis that power alone does not select the winning architecture.

## Sensitivity formula

```text
annual energy cost
= facility power (kW) × 8,760 hours × utilisation × electricity price
```

Cooling savings are not automatically equal to electrical savings. Use a measured facility PUE or a documented rack/facility cooling response before adding cooling credits.

## Evidence boundary

The power values are analyst scenario outputs from the [102.4T switch-side power model](102.4t-switch-side-power-model.md), not measured chassis results. The electricity prices, utilisation and five-year horizon are illustrative assumptions. This sensitivity cannot replace product ASP, final yield, repair/service, capex or matched BER/FEC qualification evidence in the [TCO-per-delivered-bit gate](tco-per-delivered-bit-gate.md).

## Linked controls

- [102.4T switch-side power model](102.4t-switch-side-power-model.md)
- [TCO per delivered bit](tco-per-delivered-bit-gate.md)
- [Profit-pool scenario bridge](profit-pool-scenario-bridge.md)
