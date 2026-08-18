# Manufacturing gate: cost per qualified good optical engine

**Owner:** Nur Alpys  
**Status:** Evidence-gated model scaffold; no supplier ranking yet  
**Scope:** Scale-out optical engines/PICs, 200G/lane and later 400G/lane  
**Last updated:** 2026-08-08

The [manufacturing-to-model handoff](../09-primary-research/manufacturing-production-handoff-2026-08-12.md)
defines which retained process records can and cannot populate this waterfall.

## Decision question

Which architecture can deliver a *qualified, serviceable good engine* at the lowest recurring cost—not merely the lowest measured PIC loss or device energy?

The relevant unit is a tested engine that can be accepted into a platform after assembly, reflow, optical test, burn-in/qualification and any required rework. A die, PIC, laser or connector result is an input to this calculation, not the unit itself.

## Cost-per-good-engine waterfall

The model should be populated only when the evidence boundary is explicit:

```text
materials + wafer/PIC + laser + driver/TIA
+ fibre attach / connector / interposer
+ package, thermal hardware and assembly
+ optical/electrical test + burn-in
+ rework + scrap + yield loss
+ qualification amortisation + warranty/service reserve
----------------------------------------------------------------
realised cost per qualified good engine
```

For a process with sequential yields, the first-pass cost is approximately:

```text
cost per good engine = fully loaded process cost / (Y_PIC × Y_laser × Y_attach × Y_package × Y_test)
```

The fibre-count sub-calculation is documented separately in [Fibre-count and first-pass-yield sensitivity](fibre-count-yield-sensitivity.md). It is intentionally not added to the complete-engine yield until the connection count and process boundary are matched to a real product.

Use [CPO yield-claim reconciliation](yield-claim-reconciliation.md) to normalize company claims, prototype measurements and illustrative calculations before entering any yield variable.

This is a bookkeeping identity, not a forecast. The current public evidence does not provide the required production yields or loaded costs, so no numerical ranking should be assigned.

## Interface-yield sensitivity (illustrative only)

PAP-043 reports development-run optical-interface yields of 57%, 68% and 75.5% for three edge-vertical-coupler lengths. The table below shows the arithmetic effect if those percentages were inserted **only as an interface-yield factor** while all other yields and the loaded process cost are held constant. It is not a supplier forecast and must not be read as final-engine yield.

Illustrative assumptions: fully loaded process cost = **$1,000 per attempted engine**; `Y_PIC = 90%`; `Y_laser = 95%`; `Y_package = 98%`; `Y_test = 99%`; interface factor = PAP-043 development-run value.

```text
cost per accepted engine = $1,000 / (0.90 × 0.95 × 0.98 × 0.99 × Y_interface)
```

| Interface factor used | Implied combined yield under these assumptions | Illustrative cost per accepted engine |
|---:|---:|---:|
| 57.0% (PAP-043, 0.5 mm) | 47.2% | $2,115 |
| 68.0% (PAP-043, 1.0 mm) | 56.3% | $1,773 |
| 75.5% (PAP-043, 1.5 mm) | 62.6% | $1,597 |

The roughly $518 spread between the low and high interface cases is a mechanical consequence of the formula, not an observed cost advantage. It excludes connection-count compounding, scrap recovery, rework labour, qualification amortisation, warranty, service inventory and any correlation between interface failure and the other yield terms. Replace each assumption with lot-level data before using this model for company ranking (`PAP-043`, `CLM-421`–`CLM-423`).

## Evidence-to-input map

| Input | What the retained evidence can establish | What is still missing before a model input is investable |
|---|---|---|
| Optical loss and margin | IBM full-module OTV: typically 1.5–2.0 dB assembled channel, some <1.2 dB; 0–0.25 dB change over 0–3 reflows (`PAP-042`). Corning/Furukawa provide partial fan-out and detachable-connector boundaries (`PAP-017`, `PAP-018`). | Full lane/channel distribution at operating temperature, BER/TDECQ margin, contamination sensitivity, repair threshold and correlation between loss and electrical yield. |
| Fibre attach | IBM OBR/GLP work reports 1,178 observations, 0.98 correlation and a 10-second setup plus 2-minute measurement estimate (`PAP-015`). | Held-out validation, Cpk, false-pass/false-fail rates, automated cycle time, attach first-pass yield, rework fraction and scrap cost. |
| Fibre-count compounding | OIF's 51.2T switch-card examples show 1,088 versus 288 fibre connections; at an assumed 99.865% per-connection first-pass yield, calculated board fibre-assembly yield is about 23.0% versus 67.8% (`STD-014`, `CLM-397`–`CLM-400`). | Measured per-connection distributions, actual package architecture, rework recovery and complete-engine yield. |
| Mechanical/reflow | Cao's 51.2T model exposes warpage, BGA stress and socket-force trade-offs (`PAP-016`); IBM reports process changes were needed before later OTV stress passes (`PAP-042`). | Measured lot distributions, repeated reflow, thermal cycling/humidity/shock results, pass/fail counts and line-level process capability. |
| Connector/service boundary | Furukawa reports ≤0.4 dB over ten mating cycles and one PLC reflow screen; Corning reports a separate 0.8 dB connector result (`PAP-017`, `PAP-018`). | Long-cycle wear, dust/shock/vibration/humidity qualification, field replacement time, connector inventory and service-return economics. |
| PIC/laser assembly | PAP-025 is a close 200G/lane transmitter boundary; PAP-019 and PAP-022 establish credible external-laser routes; PAP-021 and PAP-012 are device/model boundaries. | Matched engine BOM, laser coupling loss, thermal control, complete wall-plug power, multi-channel yield and supplier pricing. |
| FOWLP engine process | Full PAP-045 reports an eight-channel 1.6-Tb/s-class FOWLP engine, protected optical edge couplers, wafer-level testing and direct-drive PAM4 TDECQ around 2.08–2.32 dB. | Good-engine denominator, mould/edge-coupler defect rate, attach/test cycle time, rework, thermal qualification, loaded cost and supplier ASP/margin. |
| Active-chip/interposer packaging | PAP-046 measures a 110-GHz TGV/RDL interposer and reports a single EML output falling from 4.9 dBm pre-package to −0.07 dBm post-package; PAP-036 reports severe prototype substrate/thermal exposure losses. | Lot-level optical-loss distribution, process capability, accepted-unit denominator, rework recovery, qualification and cost impact of coupling/thermal defects. |
| 400G/lane PIC countercase | PAP-053 reports TEC-less 400G/lane InP MZ PIC transmission over 500 m from 20–80°C, with low adjacent-channel crosstalk. | Complete module power, fibre attach, driver/PIC integration, production yield, reliability, customer qualification and economics before treating it as a qualified pluggable engine. |
| Test and known-good boundary | Socketable or detachable concepts can move some testing before final system assembly (`PAP-003`, `PAP-013`, `PAP-018`). | Actual test coverage, test time, fixtures, retest/rework rules, burn-in duration, failure Pareto and whether failed engines are economically replaceable. |
| Test insertion and throughput | Teradyne identifies wafer, optical-engine, package/CPO and system-level test as separate insertion points, with optical alignment, thermal control and high-speed RF/digital handling requirements (`CMP-049`, `CLM-393`–`CLM-396`). | Measured seconds per insertion, coverage, escape rate, equipment utilization, capital cost and late-discovery/rework economics. |
| Production wafer-test infrastructure | Teradyne/ficonTEC announce a high-volume double-sided wafer-probe test cell for hybrid-bonded PIC/EIC wafers, combining ATE, optical alignment, probing and wafer handling (`CMP-052`, `CLM-432`–`CLM-434`). | Customer-installed throughput, test time, Cpk, escape rate, yield delta, utilization, ASP and service economics. |
| Wafer-level burn-in capacity signal | Aehr reports follow-on automated wafer-level burn-in-system orders and later says its unnamed lead SiPh customer is ramping, while a second unnamed networking customer forecasts more systems (`CMP-056`, `CMP-080`, `FIL-016`, `CLM-518`, `CLM-549`, `CLM-562`). | Customer/product identity, CPO allocation, wafer starts, seconds per wafer, burn-in screen, coverage, Cpk, test yield, installed utilisation and cost per good die. |
| Detachable known-good-engine route | Lightmatter vClick reports a detachable FAU, below-1.5 dB insertion/re-insertion loss, passive assembly and known-good optical-engine verification before final ASIC/XPU integration (`CMP-050`, `CLM-401`–`CLM-405`). | Independent yield improvement, mating life, environmental qualification, automated cycle time, service cost and customer production evidence. |
| NVIDIA screening/attachment claim | NVIDIA describes final-stage fibre attachment and pre-attachment screening, and calls the resulting known-good-component process “100% yield” (`CMP-051`, `CLM-406`–`CLM-410`). | Denominator/stage definition, complete-engine yield waterfall, escape/rework, package yield, qualification and customer lot evidence. |
| Qualification and warranty | IBM's OTV record shows a credible JEDEC workflow and process-learning loop (`PAP-042`). | Customer qualification lot size, FIT/field-return data, warranty reserve, replacement logistics and platform-level downtime cost. |

## Manufacturing gates

An architecture should not receive a cost or profit-pool leadership score until it clears all of these gates:

1. **Boundary gate:** the reported result covers a complete engine or a clearly separable subassembly.
2. **Yield gate:** first-pass and final accepted yield are reported by process step or bounded by a defensible range.
3. **Loss gate:** optical loss distribution is measured at temperature and after relevant reflow/handling, not only as a best channel.
4. **Test gate:** cycle time, coverage and rework disposition are known.
5. **Reliability gate:** qualification conditions, sample counts and pass/fail outcomes are disclosed.
6. **Service gate:** replacement path, connector/socket boundary and failure-domain ownership are explicit.
7. **Economic gate:** BOM/content, loaded manufacturing cost, ASP, gross margin and warranty/capex burden are either disclosed or modeled as ranges with sensitivity.

## Cost-per-qualified-good-engine input classification

The unit below is one *accepted optical engine* at a defined product boundary.
`Measured` means the retained source measures the named mechanism only; it does
not mean the result is production representative. `Assumption` is permitted
only in the private scenario harness. `Unavailable` cannot be filled from a
corporate margin or a generic market estimate.

| Cost / loss term | Required numerator and denominator | Current classification | Permitted use now | Not permitted |
|---|---|---|---|---|
| Known-good die screening | Dies tested, pass/fail, coverage, seconds and cost per die | **Measured mechanism; cost unavailable** | Require a pre-package screening insertion point | Infer final-engine yield or test cost from equipment availability |
| Fibre attach / coupling | Attach attempts, first-pass yield, loss distribution, rework and cycle time | **Measured mechanism; production values unavailable** | Treat attach as a cost-risk variable | Use best-channel loss as a line-yield input |
| Package / interposer assembly | Starts, yield, defects, rework, qualification and loaded cost | **Partial process evidence; cost unavailable** | Identify package boundary and failure modes | Apply process/engineering-sample yield to final engines |
| Test / burn-in / qualification | Insertions, seconds, coverage, escape/retest, duration and utilisation | **Measured capability; economics unavailable** | Require each insertion point in diligence | Translate capacity into accepted output or margin |
| Rework | Reworked units, recovery rate, added cycle time and cost | **Unavailable** | Keep as a blocked input | Assume zero or use a generic semiconductor rate |
| Final accepted-engine yield | Attempted complete engines and accepted engines after all tests | **Unavailable** | Keep denominator open | Call screening “100% final yield” |
| Field service / warranty | Population, return rate, replacement scope, MTTR, spares and cost | **Unavailable** | Separate laser from engine/package/ASIC repair | Treat detachable light as system-service proof |
| Loaded cost per good engine | All manufacturing/service cost divided by accepted engines | **Assumption range only** | Private sensitivity with every term labelled | Public cost, margin, EPS or profit-pool conclusion |

### Formula and stop rule

```text
cost per qualified good engine =
 (materials + attach + package + test/burn-in + rework + warranty allocation
  + attributable manufacturing depreciation) / accepted engines
```

Use the formula only after every numerator carries the same product boundary
and the denominator is accepted engines. Until then, the model's decision
output is **which term to learn next**, not a claimed cost advantage.

## Current interpretation

- The packaging literature supports a plausible route to low-loss, reflow-tolerant and potentially detachable subassemblies. It does **not** establish a lowest-cost production flow.
- Fibre attach and process control may dominate cost-per-good-engine even when PIC energy and coupling loss are excellent.
- Fibre count can amplify small per-connection defects into a large board-level first-pass-yield penalty. OIF's figures are an assumed-yield sensitivity, not a production result, but they justify treating fibre count as an explicit economic variable (`STD-014`, `CLM-397`–`CLM-400`).
- A socketable or detachable engine can improve known-good testing and serviceability, but the socket/connector becomes part of the qualified cost and failure boundary.
- IBM's full-module OTV evidence is currently the strongest retained public process/reliability record, while its missing HVM yield and field data prevent a production-cost ranking.
- Teradyne's test-flow description makes late defect discovery a separate economic risk: a PIC can be functional while an alignment-, thermal- or RF-test bottleneck still prevents attractive cost per accepted engine. This is a gate definition, not a measured supplier cost (`CMP-049`, `CLM-393`–`CLM-396`).
- Aehr's follow-on burn-in-system order is a useful capacity-direction signal, not a manufacturing-economics input: the customer, optical product and achieved output are undisclosed. It therefore raises the priority of wafer-level burn-in diligence without clearing any yield, deployment or profit gate (`CMP-056`, `CLM-518`).
- Lightmatter/SENKO's vClick route is a current product-level example of shifting optical-engine verification before expensive ASIC/XPU integration. It strengthens the known-good and serviceability hypothesis, but its loss, HVM and field-service claims remain vendor-reported (`CMP-050`, `CLM-401`–`CLM-405`).
- NVIDIA's “guaranteed 100% yield” language should be recorded as a screening/process claim, not a complete-engine yield input. The diligence question is which insertion-point denominator it covers and how much late package/test loss remains (`CMP-051`, `CLM-406`–`CLM-410`).
- TSMC/POET-style wafer-level integration and monolithic PIC claims remain economically interesting, but public records still lack comparable final-engine yield, cycle time and qualification evidence.

## Data requests for the next batch

Prioritise sources that can fill at least one missing numerator or denominator:

- customer or supplier qualification reports with sample counts and pass/fail distributions;
- manufacturing presentations reporting attach yield, Cpk, cycle time or rework;
- teardown/BOM evidence for 200G/lane and 400G/lane engines;
- service manuals showing field-replaceable engine/connector boundaries;
- supplier filings disclosing capacity, capex, warranty or optical-engine gross-margin commentary.

Until these are found, the correct conclusion is **manufacturing readiness is unresolved**, not that any PIC or connector is the cost leader.
