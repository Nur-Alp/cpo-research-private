# Primary-research interview question bank

**Status:** Ready for evidence collection; no interviews recorded  
**Scope:** 200G/lane and later 400G/lane scale-out optical engines, CPO/LPO/NPO comparison  
**As of:** 2026-08-10

## Purpose and discipline

Public sources do not disclose the customer SKU, final-engine yield, supplier transfer price, field failure rate or service economics needed to clear the investment gates. This question bank is designed to collect comparable primary evidence from packaging/test suppliers, PIC and laser vendors, platform owners, operators and industry experts.

Do not request confidential customer names, exact contract prices or export-controlled design details. Ask for ranges, architecture boundaries, dated product generations and anonymised evidence. Record the respondent's role, whether the answer is direct observation or opinion, and any commercial-interest conflict.

## Respondent metadata

```text
interview_id
date
respondent_role
organisation_type
product_generation / lane rate
deployment_domain
direct_observation_or_opinion
conflict_or_incentive
permission_to_quote (yes/no/anonymised only)
source_file_or_notes
```

## A. Platform owner / switch or XPU architect

1. Which exact product SKU and revision uses CPO, LPO, NPO or another optical boundary?
2. What is the lane rate, engine count, port count, reach, FEC and temperature class?
3. What was the qualification date, and how many systems or ports have been accepted by customers?
4. What share of production systems uses the optical architecture versus retimed pluggables, LPO, NPO or copper?
5. What is the measured inlet power at the same bandwidth and traffic load for each alternative?
6. Which failure domains are field-replaceable: laser/ELSFP, fibre, connector, PIC/engine, package, switch ASIC or full chassis?
7. What are the observed link-flap, optical-power drift, thermal excursion and replacement rates?
8. How are spares, MTTR, warranty reserve and customer downtime cost allocated between the platform owner and suppliers?
9. Which PIC, laser, package, fibre-attach, test and system-assembly suppliers are qualified, and where is second sourcing available?
10. What product-level gross-margin or price-down pressure has the optical architecture created relative to the displaced alternative?

**Minimum evidence request:** anonymised SKU, accepted unit/port range, qualification date, repeat-order indicator, field-return range and responsibility map.

## B. PIC, optical-engine or module supplier

1. Define the commercial unit: PIC, optical engine, socketed engine, ELSFP, transceiver, or complete switch subassembly.
2. Which functions are included—PIC, driver/TIA, laser, fibre attach, connector, package, control, test and rework?
3. What are the good-die, attach, package, test and final-acceptance yields at the relevant lane rate?
4. What is the first-pass yield versus final yield after rework, and what are the dominant defect Pareto categories?
5. What are automated alignment/attach and test cycle times, and what fraction is operator-dependent?
6. What optical-loss distribution is accepted at incoming, after assembly, after reflow and after environmental stress?
7. What are the operating temperature, lifetime, accelerated-aging and optical-feedback limits?
8. What percentage of qualified output is single-sourced, dual-sourced or capacity-constrained?
9. How does the supplier share of content change between CPO, NPO, LPO and retimed products?
10. What are the realised ASP range, price-down schedule, gross-margin range and warranty allocation by generation?
11. What capex and depreciation burden is attributable to the product, and what utilization is required for target margin?

**Minimum evidence request:** anonymised yield waterfall, cycle-time range, loss distribution, qualification report summary, capacity and margin range.

## C. OSAT, fibre-attach, packaging or test supplier

1. At which insertion points is optical/electrical testing performed: wafer, die, subassembly, engine, module and final system?
2. Which tests are screening tests, acceptance tests or reliability qualification tests?
3. What are test time, coverage, escape rate, false-fail rate and rework recovery by insertion point?
4. What fibre-count, pitch, alignment-tolerance and connector design most affects first-pass yield?
5. What equipment and metrology are bottlenecks for 200G/lane and 400G/lane engines?
6. What are the validated Cpk or equivalent process-capability ranges for attach, voids, bond alignment and thermal interface?
7. How do detachable/socketed designs change assembly yield, test sequencing, spare inventory and field repair?
8. What lot size, panel size and automation level is required before unit economics become attractive?
9. Who owns scrap, rework, warranty and qualification failures under typical contracts?
10. What second source or process-transfer path exists if a line is constrained?

**Minimum evidence request:** anonymised process-capability ranges, test-time distribution, rework/escape data, equipment utilization and contract-risk boundary.

## D. Laser / ELSFP supplier

1. Is the source continuous-wave, directly modulated, SOA-integrated DFB, monolithic InP or VCSEL, and what is the delivered power boundary?
2. What are electrical-to-optical efficiency, TEC/control power and output at the required temperature and aging point?
3. What splitter, connector, fibre and redundancy losses occur before the engine input?
4. How many engines share one source, and what is the failure blast radius if a source, splitter or fibre fails?
5. What are lifetime, optical-feedback tolerance, RIN, linewidth, wavelength drift and replacement-cycle data?
6. Is the source field-replaceable without opening the engine or switch, and what is observed MTTR?
7. What percentage of the customer's engine BOM is the laser/ELSFP, and what is the qualified supplier share?
8. What are ASP, price-down, warranty and cancellation-protection terms by generation?

**Minimum evidence request:** delivered-power tree, aging/reliability summary, replacement data, qualified share and anonymised economics range.

## E. Hyperscaler / system operator

1. Which exact network domain is being evaluated: front-end scale-out, back-end scale-out, scale-up, inter-rack or memory/disaggregation?
2. What problem is the architecture solving—power, electrical reach, world size, latency, uptime, density, serviceability or supply?
3. What is the unit of adoption: switch, port, rack, engine, link or cluster?
4. What qualification tests and failure thresholds must a new optical architecture pass?
5. What is the replacement boundary and acceptable MTTR for laser, engine, package, fibre and chassis failures?
6. What measured power, utilization, link availability and downtime data are available against the current alternative?
7. What price premium is acceptable for lower power or larger world size after spares and service are included?
8. What would cause the operator to choose LPO, NPO, retimed optics, AEC or copper instead of CPO?
9. Has the operator accepted repeat shipments or expanded the deployment? If not, what gate remains open?

**Minimum evidence request:** anonymised product boundary, deployment range, qualification status, measured power/availability range and adoption decision criteria.

## F. Evidence-specific follow-ups from the latest academic packet

These prompts translate the latest measured boundaries into questions for practitioners; they do not assume the papers represent production capability.

1. `PAP-030`: Can a polymer-waveguide path that survives +20 dBm for six hours be supported by accelerated-life data, PMF-array assembly data, and a defined optical-loss drift limit over the customer's field-life requirement?
2. `PAP-028`: Does detachable known-good-module screening reduce final-engine yield compounding in a production line, and what are the measured mating-cycle, rework-recovery and connector-loss distributions?
3. `PAP-029`: What are the actual wafer/package yield, test time, rework and cost-per-good-engine distributions behind 224G/lambda FOWLP claims?
4. `PAP-044`: Does localized laser-solder replacement work in a qualified service process, and what are replacement cycle time, thermal/reflow limits, post-replacement acceptance criteria and field failure rates?
5. `PAP-011`: At 400G/lane, what measured host/channel loss and FEC margin are available beyond the paper's modeled 212.5-GBd boundary, and which package/electrical insertion point is expected to move from LPO to NPO or CPO?

## Evidence coding

| Code | Meaning |
|---|---|
| `PR-OBS` | Directly observed by respondent or documented in an anonymised record |
| `PR-COMP` | Company-specific but not independently verified |
| `PR-EST` | Expert estimate or range; useful for sensitivity only |
| `PR-NEG` | Respondent says the requested value is unavailable or not tracked |
| `PR-CONF` | Confidential detail; record only the existence of the limitation |

Primary-research claims should enter the claim ledger only with the code, boundary, date, respondent role and confidence. A confidential interview can raise a research prior, but should not be presented as a public fact unless the respondent permits attribution.

## Highest-priority outreach sequence

1. Independent OSAT/test or fibre-attach process engineer: yield, test and cycle-time boundary.
2. Optical-engine or laser supplier engineer: delivered-power, reliability and qualification boundary.
3. Hyperscaler/network operator engineer: customer acceptance, service and replacement economics.
4. Platform owner or system manufacturer: SKU, supplier allocation and repeat production.
5. Industry expert or former employee: triangulation only, never sole proof of units or margin.

## Linked controls

- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [Falsification dashboard](../08-model/falsification-dashboard.md)
- [Customer-proof register](../08-model/customer-proof-register.md)
- [Source and claim ledger](../01-sources/claim-ledger.csv)
