# When CPO wins: common-boundary decision test

**Status:** Private architecture conclusion; not an adoption forecast  
**As of:** 2026-08-14

## Bottom line

**CPO wins only when the electrical/power benefit of moving optics beside the ASIC exceeds the qualified-cost and service burden of deeper integration.** It has not won merely because a component consumes fewer pJ/bit.

## Same-boundary comparison

| Test | Retimed pluggable | LPO | NPO / OBO | CPO | CPO must demonstrate |
|---|---|---|---|---|---|
| Electrical margin at required lane rate/reach/FEC | Strongest recovery margin; longer electrical path | Conditional at 200G; no matched 400G system proof | Plausibly short path; no qualified product record | Shortest ASIC-to-engine path | A material margin/power improvement at the same ports, reach and error target. |
| Power including laser, DSP/retiming and cooling | Highest retimer/module power likely, but matched total unavailable | May remove retimer power; topology-specific | Potentially lower electrical loss; complete loads unknown | Component/interface savings plausible; complete boundary still incomplete | Lower **inlet** power after ELS, driver/TIA, control, cooling and conversion. |
| Thermal / qualification | Distributed module heat; mature module boundary | Module thermal/diagnostic dependence | Near-package interaction unqualified | Highest local integration/cooling burden | Comparable ambient and qualification pass, not a laboratory component test. |
| Yield / test / rework | Mature flow but no matched 200G/400G yield comparison | Final-module yield unproven | No production record | Process mechanisms and tooling exist; final-engine waterfall absent | Final good-unit yield and cost that offset integration risk. |
| Service / replacement burden | Replace module | Retains modular swap | Potential smaller replaceable boundary, unproven | ELS may be replaceable; engine/package/ASIC boundary remains larger | Lower cost per restored port, including MTTR, spares and downtime. |

## Conditions that would make CPO the preferred architecture

All of the following must hold at a named system boundary:

1. Retimed and LPO options fail the required electrical-loss / power-density boundary, while NPO cannot qualify or service the same deployment.
2. CPO shows lower all-in inlet power at the same ASIC, port count, lane rate, reach, FEC, temperature and cooling boundary.
3. Fibre attach and package assembly reach a measured final-engine yield/rework outcome that does not erase the power advantage.
4. Test, burn-in and qualification show acceptable late-defect and escape rates.
5. The external-light / connector / engine failure domains yield an equal or lower cost per restored port than the modular alternative.
6. Supplier economics do not transfer the savings entirely to the platform owner, OSAT or customer.

## Current conclusion

At 200G/lane, CPO has the strongest disclosed product and production-route signals, but no matched four-way system result. At 400G/lane, `PAP-051` strengthens the driver/modulator feasibility case while `PAP-053` and `PAP-054` show credible advanced-pluggable counterexamples. CPO therefore remains a **conditional system-integration thesis**, not an inevitable lane-rate outcome.

Use the full [common-boundary scorecard](system-boundary-comparison-scorecard.md) for source-level detail.
