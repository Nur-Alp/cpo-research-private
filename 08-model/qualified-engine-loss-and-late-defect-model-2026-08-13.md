# Qualified-engine loss and late-defect model

**Status:** Private decision model; no production costs or yields populated  
**As of:** 2026-08-13  
**Unit:** One accepted, serviceable optical engine at a named product boundary

## Decision output

**Current bottleneck verdict — inference, medium confidence:** no stage is
proven dominant in a production CPO engine. Fibre attach and package geometry
are the strongest *physical-yield* candidates; final test and qualification are
the strongest *late-defect-cost* candidates. Test/burn-in has the clearest
public capacity evidence, but that does not establish its share of cost or
profit.

| Candidate | Why it could dominate | What public evidence actually proves | Current rank | What would resolve it |
|---|---|---|---|---|
| Fibre attach / connector | Dense interfaces compound small loss/alignment defects; recovery may be hard after integration | Development mechanisms and architecture routes | Highest unresolved physical-yield risk | Attempts, first-pass/recovery yield, loss distribution and cycle time by dense product |
| Package / thermal / reflow | Warpage, coplanarity and thermal stress can damage a previously viable interface after expensive integration | Prototype loss mechanisms and OSAT process controls | Co-equal physical-yield / late-loss risk | Package starts-to-pass, defect Pareto, rework and qualification population |
| Final test | Late optical/electrical failures may be discovered after package or module completion | Multi-stage tooling is commercially available | Highest observable late-cost control point | Test seconds, coverage, escapes, retest/rework and cost per accepted engine |
| Burn-in / qualification | Infant mortality or environmental failures can occur after most manufacturing value is added | Screening capacity and research stress flows | High but unranked cost-risk | Product stress profile, pass/fail, post-burn-in reliability and warranty reserve |
| Field service | Failure can require replacement of a large package/system boundary | ELSFP and warranty scopes define only partial boundaries | Potentially highest total-cost risk | Fleet exposure, return disposition, MTTR, spares and actual warranty cost |

No row supports a supplier profit-pool conclusion.

## Common loss waterfall

| Stage | Failures to record | Value at risk when detected | Reworkable? | Evidence status | Model status |
|---|---|---|---|---|---|
| Wafer / known-good die | Optical/electrical die defect, probe/contact failure | Wafer processing | Bin/retest possible | Tooling and process capability public | Yield/cost blocked |
| Fibre attach / engine | Alignment, void, contamination, coupling loss, connector mating | PIC/EIC plus local optical subassembly | Architecture-dependent; recovery unknown | Mechanisms measured, no HVM waterfall | Yield/rework blocked |
| Package / thermal assembly | Warpage, delamination, reflow/attach thermal damage, electrical interconnect defect | Engine plus package/interposer, sometimes ASIC-adjacent value | Process-specific, recovery unknown | Prototype/OSAT evidence | Yield/rework blocked |
| Final test | Optical/electrical lane failure, connector/handling failure, escape from earlier screen | Completed package/module | Retest or repair boundary unknown | Equipment capability public | Test cost/yield blocked |
| Burn-in / qualification | Infant mortality, temperature/humidity/cycling failure | Completed product and qualification time | Usually disposition-dependent | Capacity/research evidence | Acceptance/warranty blocked |
| Field service | Laser, FAU, engine, package/ASIC, cooling/control | Installed system, spare inventory and downtime | Depends on replaceable boundary | Standards/policy only | MTTR/warranty blocked |

## Loss accounting identity

For stage `s`, do not enter a yield without a product-matched denominator:

```text
loss_s = attempts_s - first-pass_s - recovered_s
stage yield_s = (first-pass_s + recovered_s) / attempts_s
```

The cost of an accepted engine is only eligible once all stages use the same
boundary:

```text
cost per accepted engine =
  (material + attach + package + test + burn-in + rework + warranty + capital)
  / accepted engines
```

## Stage-change tests

The bottleneck moves **away from fibre attach** only if a named engine shows
stable attach first-pass/recovery performance and a later stage supplies a
larger loss or cost numerator. It moves **to package** if post-attach
warpage/reflow/thermal losses dominate accepted engines. It moves **to test**
if package pass is stable but coverage, test time, escapes or retest/rework
dominate. It moves **to qualification/service** if burn-in or field returns
dominate the accepted-engine/warranty boundary.

## Evidence anchors

- Fibre attach: `PAP-043`, `STD-014`, `CMP-050`, `PRI-001`, `PRI-002`.
- Package/thermal: `PAP-035`, `PAP-036`, `CMP-087`, `CMP-089`.
- Test flow: `CMP-052`, `CMP-084`, `CMP-086`, `CMP-088`.
- Burn-in/qualification: `CMP-056`, `CMP-080`, `FIL-016`, `CMP-082`.

## Release control

This is a private decision model. It contains no public-ready cost estimate;
any public use must cite original permissible sources and preserve all missing
denominators.
