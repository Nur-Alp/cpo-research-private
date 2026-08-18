# Package-and-test qualification evidence pack

**Status:** Private public-source diligence pack; no production-cost conclusion  
**As of:** 2026-08-13  
**Decision question:** After fibre attach is controlled, does package/test/qualification become the binding constraint for a qualified CPO optical engine?

## Decision answer

**Inference, medium confidence:** package/test/qualification is at least a
co-equal candidate constraint after fibre attach—not yet a proven replacement
for it. The public record makes the *tooling and intended flow* unusually
concrete: wafer probing, die/engine test, package/module test, wafer-level
burn-in and environmental qualification all exist as distinct insertion points.
It does not disclose the same-engine post-attach yield waterfall needed to
identify which stage creates the greatest realised loss.

The important distinction is:

```text
Production-ready test tool or OSAT process claim
≠ installed line ≠ tested-unit denominator ≠ final-pass yield
≠ rework recovery ≠ accepted-engine cost ≠ supplier value capture.
```

The current evidence therefore shifts the conclusion from “fibre attach is
probably the bottleneck” to **“fibre attach, package geometry and late test are
coupled candidates; the binding stage is unproven.”**

## Test-flow map: wafer → engine → package → module → burn-in

| Stage | Purpose | Direct public evidence | What a pass means | Missing production measure |
|---|---|---|---|---|
| Wafer / known-good PIC-EIC | Screen dies before irreversible assembly | Teradyne/ficonTEC double-sided wafer test (`CMP-052`); ASE wafer probing (`CMP-087`); Advantest (`CMP-086`) | Die meets the stated wafer-test boundary | Coverage, seconds, false pass/fail, wafer yield and cost |
| Die / optical-engine | Test assembled die-level engine or receptacle interface | ficonTEC DLT-D1 (`CMP-088`); Teradyne insertion map (`CMP-084`) | Tested subassembly clears an engine-level test boundary | Attach/test yield, retest/rework and loss distribution |
| Package / thermal assembly | Verify optical/electrical function after EIC/PIC integration, attach, reflow and lid/ball steps | IBM full-module OTV (`PAP-035`); Intel prototype (`PAP-036`); ASE process map (`CMP-087`, `CMP-089`) | A specific package/test vehicle survives its stated flow | Production Cpk, lot distribution, package yield, cycle time and cost |
| CPO module / switch-level final test | Validate completed module or switch-engine integration | Teradyne Photon 100 (`CMP-084`); Advantest final-test connector handling (`CMP-086`) | Final test was designed / can be automated | Actual coverage, escape rate, system integration loss and final accepted-unit denominator |
| Burn-in / qualification | Screen infant mortality; prove stress/reliability boundary | Aehr production WLBI signals (`CMP-056`, `CMP-080`, `FIL-016`); IBM JEDEC (`PAP-035`); Lumentum component life (`CMP-082`) | A stated component or test vehicle passed the stated stress/screen | Product-specific pass/fail, duration, field FIT, warranty reserve and shipped population |

**Control:** a pass at any earlier stage does not clear the next stage. The
only model-eligible denominator remains:

```text
starts → screened dies → attached engines → packaged engines → final-test pass
→ rework disposition → accepted/shipped units → field returns
```

## Actual production tooling/capacity versus measured yield/cost

| Record | What the public record establishes | What it does not establish | Correct decision use |
|---|---|---|---|
| Teradyne + ficonTEC (`CMP-052`, `CMP-084`) | Production-oriented double-sided PIC/EIC wafer-test capability and distinct wafer/engine/package/module insertions | Customer installation, test time, coverage, escape rate, output or CPO economics | Confirms test-flow complexity and a possible test control point |
| ficonTEC DLT-D1 (`CMP-088`) | Die-level optical-engine capability with automated fibre coupling, JEDEC handling and parallel test heads | Installed OSAT use, yield gain, test cost or accepted output | Confirms a commercial bridge between wafer and package test |
| Advantest (`CMP-086`) | Automated optical access and final-test connector handling are recognised HVM problems | Standard connector, installed line, outcome or economics | Confirms late-stage connector handling as a separate gate |
| Aehr (`CMP-056`, `CMP-080`, `FIL-016`) | Follow-on multi-wafer SiPh burn-in capacity and unnamed customer ramp signals | CPO allocation, wafer starts, utilisation, pass/fail, cost or engine output | Capacity-direction proxy only |
| ASE (`CMP-087`, `CMP-089`) | OSAT CPO process map, known-good SiPh test, package integration, warpage/coplanarity controls | Production yield, rework, field reliability, customer or supplier economics | Confirms package geometry and testability are relevant post-attach controls |
| IBM / Intel (`PAP-035`, `PAP-036`) | Full-module qualification workflow and prototype package failure mechanisms | HVM yield/cost, output, customer acceptance or field data | Strongest mechanism evidence; not a production ranking |
| TSMC / SPIL (`CMP-083`) | TSMC COUPE EIC/PIC integration and SPIL bumping/sort/assembly/test roles in NVIDIA family ecosystem | Exact-SKU process flow, yield, capacity allocation and financial attribution | Supplier responsibility map only |

## Late-defect cost map

The table ranks *economic exposure*, not observed dollar cost. Earlier failure
detection may save more costly irreversible integration; it can also add test
time/capex. None of the cost/recovery fields below is publicly quantified for a
named CPO production engine.

| Detection point | Failure examples | Value already integrated at failure | Likely disposition | Late-defect exposure | What would make it measurable |
|---|---|---|---|---|---|
| Wafer test | PIC/EIC electrical or optical defect | Wafer processing only | Bin, exclude or retest die | Lowest | Die count, coverage, false pass/fail, test seconds and cost |
| Die / pre-package engine | Coupler/FAU alignment or optical loss | PIC/EIC, perhaps local optical subassembly | Re-align, rework or scrap subassembly | Low-to-medium | Attach attempts, recovery, loss distribution and cycle time |
| Post-attach / package | Warpage, delamination, thermal damage, reflow loss, package electrical defect | Optical engine plus package/interposer and possibly expensive ASIC-adjacent assembly | Process-specific repair if possible; otherwise scrap package/engine | **High** | Starts-to-package-pass, defect Pareto, rework rate and post-rework reliability |
| Module / switch final test | System integration, connector handling, lane-level optical/electrical failure | Completed engine/package and system integration | Retest, rework, module/switch replacement | **Very high** | Test coverage/escapes, repair scope, accepted unit denominator and disposition |
| Burn-in / environmental qualification | Infant mortality, thermal/mechanical failures, latent optical/electrical defects | Completed product after significant manufacturing value | Rework, reserve, replacement or scrap | **Very high** | Screen duration, pass/fail distribution, failure Pareto and warranty allocation |
| Field return | Laser, FAU/connector, engine, package or ASIC failure | Installed system plus service inventory and downtime exposure | Replace the smallest qualified unit—or larger system boundary | Potentially highest | Fleet exposure, MTTR, spares, return disposition and service cost |

### What the retained technical record actually says about late loss

- Intel’s prototype observed approximately 50% substrate loss in a thermal
  pre-screen and approximately 90% cumulative loss after a subsequent thermal
  compression/attach route before process optimisation (`PAP-036`). This is a
  process-specific prototype warning that post-attach package loss can dominate
  **in that flow**, not a general CPO yield.
- IBM’s test vehicles required iterative material/process changes before later
  reflow and JEDEC stress results met the stated boundary (`PAP-035`). It
  confirms a late qualification learning loop, not a cost or field-FIT result.
- ASE identifies warpage and coplanarity control as necessary to meet FAU
  coupling requirements (`CMP-089`), binding package geometry to the fibre
  interface rather than treating it as a separate problem.

## Control-point and value-capture map

| Step | Publicly named controllers / roles | Capability or production evidence | Value-capture verdict |
|---|---|---|---|
| PIC/EIC wafer integration | TSMC / COUPE (`CMP-083`) | Family-level integration role | No SKU allocation, volume, yield, ASP or margin |
| Wafer optical test | Teradyne, ficonTEC, Advantest, ASE (`CMP-052`, `CMP-086`–`CMP-088`) | Tooling/capability; some production-oriented claims | **No CPO revenue or profit capture proven** |
| EIC/PIC assembly and package | SPIL (`CMP-083`); ASE (`CMP-087`, `CMP-089`) | Family role / OSAT process capability | No product attribution, yield/rework or gross margin |
| Die/engine test | ficonTEC, Teradyne, Advantest | Equipment capability | No installed-line utilisation or financial evidence |
| Burn-in | Aehr (`CMP-056`, `CMP-080`, `FIL-016`) | Follow-on SiPh equipment orders, unnamed customers | Equipment demand signal; no CPO-specific revenue/margin attribution |
| Module/system assembly & final test | SPIL, Foxconn, Fabrinet in NVIDIA map (`CMP-083`) | Family-level process roles | No exact flow, service cost or economics |
| Qualification / service | OEM warranty boundary (`CMP-058`); ELS component programme (`CMP-082`) | Policy/component-level evidence | No engine/system warranty or supplier profit proof |

## How to determine whether package/test has overtaken fibre attach

| Required evidence | Interpretation |
|---|---|
| Dense fibre attach yield/recovery is high and stable across a named product/lot | Fibre attach may no longer be the first-pass limiter |
| Package starts-to-final-test-pass identifies warpage/reflow/thermal/electrical loss after accepted attach | Package has a credible claim to the binding loss stage |
| Final test shows high escape/retest/rework burden despite package pass | Test coverage/handling becomes the binding cost or quality constraint |
| Burn-in / qualification creates the largest disposition or warranty burden | Reliability/qualification becomes the economic bottleneck |
| Matched cost per accepted engine shows a later stage dominates after recovery | Required to make any profit-pool conclusion |

No retained public record clears these tests. Therefore the current research
conclusion remains **not enough evidence to rank fibre attach against
package/test/qualification by realised cost or value capture.**

## Ranked primary-evidence gaps

1. Named engine/lot test flow with stage denominators and failure disposition.
2. OSAT post-attach package yield, warpage/reflow failure Pareto and rework
   route tied to optical/electrical acceptance.
3. Final test coverage, seconds, escape rate and repair scope.
4. Burn-in conditions, pass/fail distribution and post-burn-in field returns.
5. Supplier-specific economic allocation: equipment/assembly/test ASP, gross
   margin, consumables, warranty and capital burden.

## Bottom line

The practical evidence says the bottleneck does **not** cleanly move from fibre
attach to package/test. Advanced packaging changes fibre coupling through
warpage, coplanarity and thermal exposure; test and burn-in decide whether the
resulting defect is found before or after expensive integration. The most
defensible current thesis is a **coupled late-defect-cost problem**, with broad
tooling availability but no public production waterfall to establish the
binding stage or the value-capture winner.

## Related controls

- [Fibre-attach and serviceability evidence pack](fibre-attach-serviceability-evidence-pack-2026-08-13.md)
- [Public manufacturing-readiness dossier](public-manufacturing-readiness-dossier-2026-08-13.md)
- [Manufacturing-to-model handoff](manufacturing-production-handoff-2026-08-12.md)
- [Manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md)
