# Manufacturing evidence → cost-per-qualified-engine gate

**Status:** Private scenario framework; no production cost, yield or margin forecast  
**As of:** 2026-08-14  
**Decision question:** Which bottleneck is most likely to determine cost per qualified, serviceable optical engine?

## Verdict

**Inference, medium confidence:** fibre attach/package geometry is the leading *physical-yield* risk; final test and qualification are the leading *late-defect-cost* risks. The available evidence does not establish which one dominates production cost. A supplier cannot be ranked on profit capture until both routes are measured at the same product boundary.

## What the new papers change

| Source | What it adds | What it does not add |
|---|---|---|
| `PAP-055` Meta/Broadcom historical Bailly evaluation | 15 CPO systems / 120 optical engines / 240 pluggable laser sources, plus >1m 400G-port device-hours without UCWs in stressed self-loopback. It supports the proposition that a system-test reliability programme can be run at scale. | Production yield, repair cost, field-return distribution, TH6 equivalence, supplier economics (`CLM-574`–`CLM-577`). |
| `PAP-056` Wu FOWLP engine | Measured 1.6T package/electrical/coupling evidence; nine packages with four optical I/Os each; below-2-dB/facet post-FOWLP coupling and no open daisy chains in tested structures. | Factory first-pass yield, rework recovery, test seconds, qualification population, cost or margin (`CLM-578`–`CLM-581`). |
| `PAP-051` Tran driver/modulator | Measured 180-GBaud driver/modulator feasibility, BER threshold, 40°C TEC-controlled test and explicit partial-power boundary. | Fibre-attach/package/test flow, full engine power, yield, qualification and service burden (`CLM-461`–`CLM-463`, `CLM-582`–`CLM-584`). |

## Range model — deliberately bounded, not false precision

The public record supports only two numerical engineering ranges, neither a final-engine yield or cost forecast:

| Variable | Usable evidence range | Legitimate use | Prohibited use |
|---|---|---|---|
| Development optical-interface yield | 57.0%–75.5% across PAP-043's specific development-run interfaces | Stress-test the arithmetic sensitivity of an interface step. | Apply as a production engine yield, supplier yield or company margin. |
| PAP-056 post-FOWLP coupling | Below 2 dB per facet in the stated small development sample | Establish a loss/cleanliness threshold for a candidate route. | Convert loss into attach yield, rework recovery or cost. |
| Rework recovery | **Not publicly parameterised**; mechanically bounded between no recovered failures and all recoverable failures | Keep `recovered_s` explicit in scenario algebra. | Assume recovery simply because an interface is detachable. |
| Test and burn-in burden | **Not publicly parameterised**; public sources establish multi-stage test capability, not seconds/coverage/cost | Keep test and burn-in as separate late-value-at-risk terms. | Fold test into an aggregate “yield” or treat equipment availability as production throughput. |
| Service burden | **Not publicly parameterised**; external light may be replaceable, while engine/package failure can have a larger blast radius | Keep replacement material, labour, logistics, downtime and spares distinct. | Treat ELSFP or a warranty policy as a measured CPO service advantage. |

For stage `s`, the only permitted arithmetic is:

```text
accepted_s = first-pass_s + recovered_s
stage yield_s = accepted_s / attempts_s

cost per accepted engine =
  (materials + attach + package + test + burn-in + rework
   + qualification + warranty/service + capital)
  / accepted engines
```

## Three scenario families

| Scenario family | Dominant condition | What must be observed before adopting it | Implication for value capture |
|---|---|---|---|
| **Attach-dominant** | Coupling/alignment defects or fibre-count compounding create the largest unrecovered loss. | Attempts, attach first-pass, rework recovery, loss distribution and cycle time by product. | FAU/connector/alignment/assembly process can capture value if scarce and qualified. |
| **Package/test-dominant** | Attach is stable, but warpage/reflow/thermal damage or late electrical/optical test failures destroy more accumulated value. | Starts-to-pass by package stage; defect Pareto; test seconds/coverage; retest, rework and escape data. | OSAT/test process control becomes the likely cost and qualification control point. |
| **Qualification/service-dominant** | Factory pass is stable, but burn-in, environmental screening or field replacement drives economics. | Stress population/pass-fail, field returns, MTTR, spare ratio, warranty and downtime cost. | Replaceable-boundary architecture and qualified service owner can matter more than component pJ/bit. |

## Current decision

The most defensible answer is **not “fibre attach” alone**. Attach and package geometry are the strongest unresolved early yield candidates; test/qualification are the strongest late-cost candidates. The bottleneck should be promoted only when a product-matched loss waterfall shows the highest unrecovered loss or cost at that stage.

This is why a lower component-energy number cannot win the investment case. CPO wins economically only if it retains its electrical/power benefit **after** interface yield, package/test escapes, qualification and the service replacement boundary are included.

## Linked records

- [Qualified-engine loss and late-defect model](qualified-engine-loss-and-late-defect-model-2026-08-13.md)
- [Cost-per-qualified-engine waterfall](manufacturing-cost-per-good-engine-gate.md)
- [Service and failure-domain model](service-and-failure-domain-cost-model.md)
- [Packaging/reliability benchmark](../03-components/packaging-reliability-benchmark.md)
