# Optical-engine yield waterfall template

**Status:** Empty evidence-gated model; no forecast values populated  
**Scope:** A defined 200G/lane or 400G/lane scale-out optical engine  
**As of:** 2026-08-09

This template is deliberately blank. It specifies the calculation needed to convert manufacturing evidence into cost per shipped engine; it does not substitute assumptions for missing company data.

## Required unit boundary

Before entering a value, define:

- engine capacity and lane rate;
- direction (transmit, receive or bidirectional);
- PIC, driver/TIA, laser/ELSFP, fibre attach, connector and package included;
- whether the denominator is dies started, engines assembled, engines tested or customer-accepted engines;
- currency, period and whether costs are variable, fixed or attributable capital depreciation.

## Waterfall

| Stage | Symbol | Required input | Current evidence | Status |
|---|---|---|---|---|
| PIC/laser good-die yield | `Y_die` | Good dies ÷ dies started | No company-specific final-engine yield in reviewed packet | Open |
| Fibre-attach first-pass yield | `Y_attach` | First-pass accepted attaches ÷ attach attempts | PAP-015 gives process-monitoring evidence, not production Cpk/yield | Open |
| Package assembly yield | `Y_pkg` | Packages passing assembly ÷ package starts | No final-package lot distribution | Open |
| Optical/electrical test yield | `Y_test` | Engines passing final test ÷ engines tested | No customer-qualified final-test distribution | Open |
| Customer acceptance yield | `Y_accept` | Accepted engines ÷ submitted engines | No customer acceptance or escape-rate data | Open |
| Rework recovery | `R_rework` | Reworked failures recovered ÷ failed units | No rework cost or recovery data | Open |
| Good shipped engines | `N_ship` | `N_starts × Y_die × Y_attach × Y_pkg × Y_test × Y_accept + recovered units` | No production denominator | Blocked |

The multiplicative yield term is:

```text
Y_total = Y_die × Y_attach × Y_pkg × Y_test × Y_accept
```

If rework is counted, record the recovery path separately rather than silently increasing a first-pass yield:

```text
N_good = N_starts × Y_total + (failed units × R_rework)
cost per good engine = total attributable manufacturing cost ÷ N_good
```

## Cost bridge

| Cost item | Symbol | Required evidence | Current status |
|---|---|---|---|
| PIC/laser die cost | `C_die` | Wafer cost, die count, yield and test allocation | Open |
| Attach and alignment labour/equipment | `C_attach` | Cycle time, automation, consumables, depreciation | Open |
| Package/interposer/connector | `C_pkg` | BOM and supplier price | Open |
| Driver/TIA and control | `C_eic` | EIC BOM and test/calibration cost | Open |
| Final test and burn-in | `C_test` | Test time, equipment, escape rate and energy | Open |
| Rework and scrap | `C_rework` | Recovery cost and non-recoverable scrap | Open |
| Warranty/support allocation | `C_warranty` | Failure rate, replacement, MTTR and reserve | Open |
| Attributable capital cost | `C_capex` | Incremental capacity and depreciation/return treatment | Open |

```text
C_good = (C_die + C_attach + C_pkg + C_eic + C_test
          + C_rework + C_warranty + C_capex) / Y_total
```

This formula is a modelling identity only. It must not be populated with consolidated company gross margin or a best-case component loss number.

## Profit bridge

```text
realised gross profit per shipped engine
= realised ASP - C_good

incremental gross profit
= shipped engines × realised gross profit per engine
  - cannibalised legacy gross profit
```

The model is not eligible for a base-case company forecast until the evidence bundle in the [CPO evidence-gate register](evidence-gate-register.md) is substantially cleared.

## Evidence anchors and limits

- `PAP-003` identifies assembly, test, thermal and manufacturability categories but does not provide a production yield waterfall.
- `PAP-015` supplies a process-monitoring experiment with 1,178 observations and estimated measurement times; its model was evaluated on reused observations and does not clear production Cpk or yield.
- `PAP-004`, `PAP-013`, `PAP-017` and `PAP-018` supply interface/connector measurements, not final-engine yield or field reliability.
- `PAP-042` supplies a full-module OTV, reflow and JEDEC stress boundary, including early-failure/process-iteration evidence, but no production yield or field-return distribution.
- Company dossiers disclose platform, capacity or order signals, but no reviewed company source supplies all inputs above.

## Source controls

- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Evidence-gate register](evidence-gate-register.md)
- [Packaging, fibre-attach and serviceability benchmark](../03-components/packaging-reliability-benchmark.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
