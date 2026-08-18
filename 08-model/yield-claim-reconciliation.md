# CPO yield-claim reconciliation

**Status:** Evidence boundary control; not a supplier ranking  
**Scope:** Optical engine and CPO assembly yield  
**Last updated:** 2026-08-12

## Why this file exists

The research now contains several yield-related numbers and phrases that refer to different stages. They must not be placed in one waterfall without a denominator and process boundary.

| Source/result | What is actually reported | Denominator or stage | Valid use | What it cannot prove |
|---|---|---|---|---|
| OIF panel (`STD-014`, `CLM-397`–`CLM-400`) | 23.0% and 67.8% board fibre-assembly yield | Calculated from assumed 99.865% independent per-fibre first-pass yield across 1,088 or 288 connections | Architecture/yield sensitivity; shows connection-count compounding | Measured HVM yield, package yield, rework, test escape or supplier performance |
| imec polymer flip-chip (`PAP-034`, `CLM-312`–`CLM-314`) | Two acceptable functional samples out of 16 in three batches | Small prototype process sample | Reproducibility/warpage risk signal | Production yield or complete-engine economics |
| imec edge-vertical coupler (`PAP-043`, `CLM-421`–`CLM-423`) | 75.5%, 68% and 57% optical-interface yield for three coupler lengths | Development-run interface structures | Coupler geometry, voids and lateral alignment affect interface yield | Final-engine/board yield, lot denominator, Cpk, rework, qualification or cost |
| IBM full-module OTV (`PAP-042`, `CLM-391`) | Typical 1.5–2.0 dB assembled channel loss, reflow and JEDEC stress workflow after process/material changes | Full test vehicle; public abstract/paper omits HVM lot distribution | Process/reliability learning and qualification workflow | Final-engine yield, field FIT, warranty or customer acceptance |
| IBM full-module assembly (`PAP-035`, `CLM-479`–`CLM-482`) | Two assembly sequences include inspection and test; the authors state that pre-tested known-good die/components are important for high yield | Research test vehicles; no reported screen or accepted-unit denominator | A known-good/test insertion point and reflow/qualification boundary | Good-die yield, final-test yield, screen escape, rework recovery or HVM output |
| Intel PIPES/CHIPS package (`PAP-036`, `CLM-491`–`CLM-494`) | ~50% thermal pre-screen substrate loss and ~90% cumulative loss in the reported prototype route; later lower-thermal-exposure route reports no delamination | Prototype process route; unreported matched lot population | Failure-mode and thermal-process-window diligence | Generic package yield, final-engine yield, Cpk, rework recovery or cost per good package |
| NVIDIA Spectrum-X blog (`CMP-051`, `CLM-406`–`CLM-410`) | “Guaranteed 100% yield” after screening known-good optical components before switch-silicon integration | Company wording does not define the insertion point, denominator, escapes or final acceptance | Process hypothesis: pre-screening can prevent known-bad components from entering expensive package integration | 100% complete-package yield, 100% shipped-engine yield or field reliability |
| Lightmatter vClick (`CMP-050`, `CLM-401`–`CLM-405`) | Detachable FAU, passive assembly, known-good-engine verification and <1.5 dB insertion/re-insertion loss | Product/process announcement; no lot distribution | Known-good and serviceability route | Production yield, lifetime, ASP, customer volume or margin |
| Broadcom TH6-Davisson briefing (`CMP-063`, `CLM-532`) | No link flaps in the first 1M CPO device hours | First-party historical TH5-Bailly performance-slide claim; no population, stress or customer-field denominator | Historical reliability diligence boundary and a reason to request the underlying evaluation method | TH6 200G/lane reliability, final-engine yield, field returns, warranty or economic performance |
| Broadcom / Meta release (`CMP-064`, `CLM-533`) | 1M cumulative 400G-equivalent CPO port device-hours of flap-free operation at Meta | Named high-temperature lab-characterisation setting; no disclosed population, duration, SKU or customer production denominator | Strengthens the historical TH5 reliability-control context | Meta CPO production units, TH6 reliability, final-engine yield, field returns, warranty or supplier economics |
| Lumentum UHP / ELSFP reliability paper (`CMP-082`, `CLM-553`–`CLM-555`) | >100m accelerated device-hours, zero reported catastrophic failures; stated 20-FIT rating at 400mW | Supplier-reported UHP laser-device programme; module and system boundary undisclosed | Component-level laser qualification signal and a request for raw lot/stress/field data | UHP/ELSFP production yield, module/engine yield, field FIT, warranty reserve, CPO customer qualification or supplier economics |
| Teradyne Photon 100 (`CMP-084`, `CLM-560`) | Wafer, optical-engine/package and CPO-module test insertions; production-level hybrid-bonded PIC/EIC wafer-test capability | Test-equipment product boundary; no installed line or outcome denominator | Require three test insertions in production diligence | Test coverage, seconds, throughput, false rejects/escapes, engine final-test yield, rework and cost per good engine |

## Required normalization

Every future yield number must include:

1. **Unit:** die, PIC, laser, fibre connection, optical engine, package, board or customer-accepted system.
2. **Stage:** first pass, after rework, final test, qualification or field survival.
3. **Denominator:** starts, attempts, tested units, submitted units or shipped units.
4. **Sample and lot:** sample count, number of lots, line/site and date.
5. **Conditions:** temperature, reflow, environmental stress, mating cycles and test coverage.
6. **Failure disposition:** scrap, rework recovery, downgrade, escape or warranty return.

## Model rule

Do not substitute any of the rows above for `Y_die`, `Y_attach`, `Y_pkg`, `Y_test` or `Y_accept` in the [engine yield waterfall](engine-yield-waterfall-template.md) unless the source supplies the matching unit and stage. NVIDIA's 100% statement is particularly important to reconcile because it may describe a screening insertion rather than the final-engine denominator.

## Next evidence request

For NVIDIA, Lightmatter, Broadcom, Coherent and Lumentum, seek a process or qualification record that reports:

```text
units started → optical components screened → engines assembled
→ final-test pass → rework recovery → customer-accepted/shipped engines
```

with stage-level counts and test time. Until such a record exists, preserve the yield claims as evidence-quality-bounded process signals and keep the profit-pool model unpopulated.

See also the [manufacturing proof matrix](manufacturing-proof-matrix.md), which separates full-paper process demonstrations from the missing production/economic chain.
