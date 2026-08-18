# Fibre-attach and serviceability evidence pack

**Status:** Private public-source diligence pack; no commercial conclusion  
**As of:** 2026-08-13  
**Scope:** Scale-out CPO optical-engine fibre interface, detachable FAU / connector, external-laser service boundary, assembly and final test

## Decision answer

**Inference, medium confidence:** detachable FAUs/connectors and ELSFPs can *plausibly* reduce the cost of a late failure or field intervention by moving a fibre-interface or light-source boundary outside the non-replaceable PIC/package/ASIC stack. Public evidence does **not** show that they materially reduce final-engine scrap or field-replacement burden in a deployed CPO fleet.

```text
Replaceable external laser ≠ replaceable FAU ≠ replaceable optical engine
≠ replaceable package or switch ASIC.
```

At dense CPO fibre counts, the leading manufacturability candidates are:

1. **Pre-assembled, detachable or socketed FAU with passive/kinematic final mating.** It can move fibre preparation and some optical verification before final integration. Its open risks are mating durability, contamination, loss distribution, alignment retention and connector handling.
2. **Permanent edge/vertical attach with process-controlled passive or active alignment.** It avoids a removable interface but makes first-pass attach, rework and late test escape decisive. Its open risks are automated yield, cycle time and service scope.
3. **External-laser front-panel module (ELSFP) feeding fixed optical engines.** It has the clearest formal replacement and qualification boundary, but replaces the laser—not necessarily the FAU, engine, package or ASIC.

No public source provides the matched production record needed to rank these methods by cost per accepted, serviceable engine.

## Four questions answered

### Can detachable FAUs/connectors materially reduce late-stage scrap and field-replacement burden?

**Mechanism: yes; demonstrated fleet economics: no.**

- A detachable FAU can be assembled and potentially verified before expensive final PIC/EIC/ASIC integration (`CMP-050`; `PRI-001`; `PRI-002`). That can reduce *exposure* to late-stage scrap **if** the removable boundary retains alignment and is economically requalified after mating.
- OIF ELSFP 2.0 is stronger: it specifies a field-replaceable external laser form factor and explicit mechanical/environmental requirements (`STD-011`). This directly establishes an intended replaceable-light-source boundary.
- Neither route discloses production attach yield, rework recovery, fleet returns, mean time to repair, spare ratio, warranty owner or total replacement cost. An external laser service boundary does not repair a PIC/package/FAU defect; a detachable FAU does not repair a failed ASIC.

**Decision rule:** call a detachable boundary economically meaningful only if the same product reports (a) attach/mating yield, (b) qualification after re-insertion, (c) returned-unit disposition and (d) avoided replacement scope or warranty cost. No current supplier clears all four.

### What attachment/coupling methods are realistically manufacturable at dense CPO fibre counts?

| Architecture | Physical attachment approach | Public evidence | Manufacturability read | Essential qualification gap |
|---|---|---|---|---|
| Permanent edge / fibre-array attach | Fibre array bonded/aligned to edge couplers; passive or active alignment | imec development interfaces show geometry/alignment-sensitive yield (`PAP-043`); Intel identifies fibre alignment as a throughput issue (`PAP-003`) | Realistic and technically established, but dense-count economics hinge on automation and recovery | First-pass yield, alignment Cpk, void/contamination Pareto, rework and cycle time |
| Vertical / expanded-beam detachable FAU | Pre-built fibre array mates vertically through micro-optics, pins/sockets or fiducials | Lightmatter vendor design (`CMP-050`); detachable FAU patents (`PRI-001`, `PRI-002`) | Credible serviceable route; potentially reduces final integration exposure | Mating/reinsertion distribution, environmental durability, contamination tolerance and field MTTR |
| Socketed / separately tested engine | Optical engine is tested before final ASIC/system assembly; socket carries electrical/optical boundary | Intel CPO proof-of-concept (`PAP-003`) | Credible known-good-engine concept; socket and thermal interfaces become their own yield/service gates | Socket loss, reliability, package co-planarity, automated handling and final-system yield |
| External laser, fixed engine | Front-panel ELSFP supplies CW light to fixed OEs | OIF implementation agreement (`STD-011`); management boundary (`STD-006`) | Most formal service boundary now; removes laser from hottest co-package region | Engine-side fibre loss, laser/engine failure attribution, installed service data and warranty economics |
| Permanent vertical coupler / passive optical interposer | Lithographic vertical coupling, with passive placement objective | MIT simulation proposal (`PAP-052`) | Attractive only if tolerance translates to a repeatable package line | Fabricated line yield, thermal/reflow reliability, final test and cost |

**Dense-count warning:** OIF’s connection-count calculation is illustrative, not a factory measurement, but it shows why per-connection yield and recovery cannot be ignored: 1,088 connections at an assumed 99.865% first-pass rate compound to about 23.0%, versus about 67.8% for 288 (`STD-014`). A method is not “manufacturable” merely because its single-channel loss is low.

### Which company controls each boundary?

Roles below are public ecosystem / architecture statements, not exact-SKU BOM, sole-source, qualified-share or financial allocations.

| Boundary | Confirmed / bounded public role | Candidate or adjacent route | What is unproven |
|---|---|---|---|
| PIC/EIC integration | TSMC: COUPE EIC/PIC integration in NVIDIA ecosystem (`CMP-083`) | Broadcom internal CPO optical-engine route (`CMP-055`); Lightmatter / Intel architectures | Exact SN6800/SN6810 or BCM78919 PIC/EIC supplier allocation and yield |
| Fibre/connector/FAU | SENKO: NVIDIA photonics connector ecosystem (`CMP-068`); Corning: FAU / optical-management switch-tray demo (`CMP-085`) | Lightmatter vClick; Teramount detachable connector architecture | Qualified share, exact product allocation, mating-life and economics |
| Alignment / laser-assembly / test | Lumentum, Sumitomo and Coherent: ELS assembly, alignment and test in NVIDIA ecosystem (`CMP-083`) | ficonTEC / Teradyne test-cell route (`CMP-052`) | Which company owns the final fibre attach and test escape boundary for each SKU |
| OSAT / final module assembly | SPIL: CPO multi-chip-module bumping, sort, assembly and test (`CMP-083`) | Foxconn/Fabrinet system assembly and chassis integration (`CMP-083`); ASE with Lightmatter (`CMP-050`) | Exact engine/package flow, yield/rework, quality ownership and supplier margin |
| Wafer / engine / module test | Teradyne/FiconTEC production-oriented test cell (`CMP-052`); Teradyne Photon 100 test stages (`CMP-084`); Advantest test-cell capability (`CMP-086`) | Aehr wafer-level burn-in (`CMP-056`, `CMP-080`) | Customer installed base, throughput, coverage, cost, output and profit capture |
| Field-replaceable laser | OIF ELSFP interoperability boundary (`STD-011`); Lumentum reliability evidence (`CMP-082`) | Broadcom historical pluggable-laser qualification (`CMP-070`) | Exact customer implementation, actual replacement process, warranty allocation and economics |

### What would show that the constraint moved from fibre attach to package/test instead?

| Evidence that would *de-risk fibre attach* | Evidence that would elevate package/test as the binding constraint |
|---|---|
| Product-matched attach attempts, first-pass yield and recovery published across dense fibre count | Starts-to-package-pass waterfall showing failures after successful attach |
| Loss distribution before/after mating/re-insertion plus contamination and thermal-cycle pass rates | Optical/electrical test seconds, coverage, false-pass/false-fail, escapes and retest/rework cost |
| Automated cycle time and Cpk by FAU/connector geometry | Package warpage/reflow/thermal failure Pareto and qualification population |
| Field connector mating life, MTTR and returned-FAU disposition | Burn-in duration, pass/fail distribution, post-burn-in field return and warranty reserve |
| Demonstration that attach loss/yield does not dominate accepted-engine cost | Customer-installed test utilisation / capex and a cost per accepted die or engine |

Until the same named engine has these records, the correct finding is **constraint unresolved, with fibre interface and test/package as coupled candidates**—not that either has won.

## Attachment/service architecture ranking

The ranking answers “best public evidence for a manufacturable and serviceable route,” not “lowest cost” or “best investment.”

| Rank | Route | Readiness | Why | Hard limitation |
|---:|---|---|---|---|
| 1 | ELSFP external-laser module + fixed engine | Highest standards maturity | Formal OIF mechanical, thermal, environmental, connector and 10-year-life requirements; explicit replaceable laser | Service boundary stops at laser; no system TCO or field-return evidence |
| 2 | Detachable / pre-assembled FAU | Strong design-route maturity | Multiple vendor/patent designs make interface, alignment and removable scope concrete | No disclosed production mating/yield/service economics |
| 3 | Permanent controlled fibre attach | Strongest underlying technical precedent | Direct interface/yield mechanisms and broad CPO history | Dense-fibre HVM yield, rework and service burden undisclosed |
| 4 | Socketable optical engine | Valuable system-level risk isolation concept | Separately tested engine can move defect discovery earlier | Socket/thermal/final-system qualification and economics remain open |
| 5 | Fully passive vertical interposer route | Promising, lowest evidence maturity | Simulation suggests larger alignment tolerance and low coupling loss | No production package demonstration or qualification |

## Qualification requirements that matter

OIF ELSFP 2.0 makes the following requirements tangible for the replaceable laser boundary: service-temperature classes, a 10-year field-life requirement, 100 connector/cage and 50 module durability cycles, mating/unmating forces, latch retention, environmental and connector tests (`STD-011`). These are necessary but not sufficient for system serviceability.

For a detachable FAU or engine boundary, require the same categories plus optical-loss distribution after re-insertion, thermal cycling and contamination; alignment retention and fibre-count scaling; first-pass yield/recovery/scrap disposition; reflow, warpage, shock/vibration, humidity and burn-in; late-stage test coverage/escape/retest cost; and field MTTR, spares, failure isolation and warranty ownership.

## Evidence quality and source-use rule

| Class | Sources in this pack | Permitted conclusion |
|---|---|---|
| Standards | `STD-006`, `STD-011`, `STD-014`, `STD-015` | Required intended interface/service boundary; not deployment or cost |
| Academic / technical | `PAP-003`, `PAP-043`, `PAP-052` | Mechanism and test/assembly risk; not production yield |
| Company product / ecosystem | `CMP-050`, `CMP-068`, `CMP-082`–`CMP-086` | Supplier route/capability or company claim; not allocation/economics |
| Patent disclosure | `PRI-001`, `PRI-002` | Intended architecture / service scope only |

## Ranked next records to acquire

1. Manufacturer or OSAT attachment qualification: fibre count, first-pass yield, recovery, automated cycle time and post-qualification result.
2. Service manual or RMA statement for a named CPO SKU: replaceable unit, MTTR, field connector/ELS handling and warranty owner.
3. Test supplier / customer record: installed line, product boundary, test stages, throughput/coverage and output denominator.
4. Package/OSAT record: reflow/thermal yield and defect disposition after an already-passed attach process.

## Bottom line

The evidence supports a practical engineering thesis: **designing a removable FAU or ELS boundary may reduce the replacement scope and enable earlier test, but it replaces one qualification problem with another.** The right bottleneck is the stage with the largest loss *after* the most expensive irreversible integration. Public records do not yet identify that stage for a production 200G/lane CPO engine.

This pack therefore strengthens the PIC/engine thesis by locating potential control points—fibre interface, test flow and service boundary—without falsely assigning their value pool to a company.

## Related controls

- [Public manufacturing-readiness dossier](public-manufacturing-readiness-dossier-2026-08-13.md)
- [Manufacturing evidence boundary matrix](manufacturing-evidence-boundary-matrix-2026-08-12.md)
- [Manufacturing cost per qualified good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md)
- [Patent and standards mining protocol](patent-and-standards-mining-protocol.md)
