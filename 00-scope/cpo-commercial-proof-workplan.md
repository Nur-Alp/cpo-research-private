# CPO commercial-proof workplan

**Status:** Active private research plan  
**As of:** 2026-08-12  
**Publication status:** Not approved. No public report update, commit or push is implied by this plan.

## Decision objective

Turn the current technical thesis into a falsifiable investment decision:

> Which CPO architecture can clear a credible deployment and profit-capture chain, on what timing, and which public company can plausibly retain the economics?

The current answer remains: **switch-side 200G/lane CPO has the strongest product-route signal, but no retained public record proves named-customer accepted units, repeat shipment, supplier economics or a CPO profit-pool leader.**

## Work sequence

| Priority | Deliverable | Decision it can change | Completion evidence | Current state |
|---|---|---|---|---|
| P0 | NVIDIA commercial-proof dossier | Does Spectrum-X Ethernet Photonics have a real CPO deployment? | Exact SKU + named customer + accepted units/ports + repeat shipment + service/reliability boundary | Dossier built; product/SKU and Dell route documented; customer, units and repeat-shipment gates open. |
| P0 | Broadcom commercial-proof dossier | Does TH6-Davisson/BCM78919 have a real CPO deployment? | Exact SKU + named customer + accepted units/ports + repeat shipment + supplier/content boundary | Dossier built; product/lifecycle record documents early-access / Limited Release status; customer, units and repeat-shipment gates open. |
| P0 | System-level alternative comparison | Is CPO superior after system economics, not component power alone? | Common boundary for retimed pluggable, LPO, NPO and CPO across power, reach, thermal, service, qualification and replacement | Built; real matched TCO and field-service data remain open. |
| P0 | Supplier-content map | Who supplies each value-chain layer and where can economics accrue? | Confirmed versus candidate versus open role for ASIC/SerDes, PIC, EIC, laser, fibre, package, connector and test | Built for six companies; contract/qualified-share evidence is open. |
| P0 | Profit-pool scenario gate | Can any company be assigned a credible CPO earnings sensitivity? | Customer denominator, CPO numerator, content/ASP, share, product margin, yield/rework, warranty and cannibalisation evidence | Framework built; no company is eligible for a numeric CPO forecast. |
| P1 | PIC technology scorecard | Which scale-out optical-engine route is technically and economically advantaged? | Comparable modulator/receiver, laser, coupling, thermal, test, yield and manufacturing evidence | Built; production-route proof is incomplete. |
| P1 | Manufacturing reality dossier | Is an engine manufacturable and serviceable at reliable cost? | Known-good-die, fibre attach, final-engine test, burn-in, rework, qualification, field failure and warranty evidence | Mechanisms mapped; production yield/rework/warranty data open. |
| P1 | Six company update cards | Which company has the best evidence-gated relative exposure? | Standard product boundary, customer evidence, supplier role, value capture, catalyst, falsification and confidence | Built; update only when a decision-relevant source changes a gate. |
| P1 | Expectations-versus-variant layer | Is the market expectation different from an evidence-gated view? | Reconciled fiscal period, accounting basis, external expectation record and explicit variant/falsification | Reported baseline complete; `ANL-002` is provisional; restricted-intake template and automated publication-boundary check added; no CPO EPS bridge eligible. |

## P0 evidence queue

### NVIDIA Spectrum-X Ethernet Photonics

1. Seek an end-customer, OEM, distributor, colocation or procurement record that names `SN6800`/`SN6810` or their controlled Dell `SN6800-LD`/`SN6810-LD` equivalents **and** explicitly identifies CPO.
2. Require an accepted-unit, port, system or capacity denominator. A product page, demo, “production” label or broader Spectrum-X deployment cannot substitute.
3. Find a second dated shipment, expansion order or acceptance record before calling the route repeatable.
4. Map product content only when the supplier role is named in a product, filing, contract, qualification or credible manufacturing disclosure.
5. Record field service, spare, repair and failure boundary separately. Dell’s warranty route establishes a system warranty path, not engine repair economics.

### Broadcom TH6-Davisson / BCM78919

1. Seek an early-access-to-general-availability or customer-acceptance record tied specifically to `BCM78919` or TH6-Davisson.
2. Require an explicit CPO confirmation: a Tomahawk/AI-system announcement without the CPO SKU is not evidence of CPO volume.
3. Seek a dated production order, repeat shipment or deployment expansion with a port/unit denominator.
4. Separate Broadcom silicon/platform revenue from optical-engine, laser, packaging and test supplier content.
5. Treat “now shipping” language as a product-status signal until independent accepted-unit evidence appears.

## Evidence standards

| Question | Minimum standard before the claim can move from open to evidence-supported |
|---|---|
| Customer deployment | Named customer or operator, exact CPO SKU and explicit deployment/acceptance language in a primary source. |
| Scale | Unit, port, system, capacity or spend denominator and report date. |
| Repeatability | A second shipment, expansion, repeat order or independently reported continued deployment. |
| Supplier content | Named product/contract/qualification role at one value-chain layer; partnerships alone remain candidate evidence. |
| Profit capture | Attributable content/ASP and share plus product-margin, yield/rework, warranty and cannibalisation boundary. |
| Architecture win | Matched system comparison covering power, reach, thermal, service, qualification and total replacement burden. |
| Manufacturing maturity | Final-engine test/yield, rework, burn-in/qualification and a service/failure-domain boundary. |

## Exclusions and anti-patterns

- Do not add generic CPO articles merely to increase citation count.
- Do not turn platform production language into CPO deployment proof.
- Do not use component pJ/bit as a total-cost or profit-pool result.
- Do not turn a supplier partnership into qualified content share.
- Do not multiply a CPO scenario by a consolidated company margin.
- Do not report an “unknown” as zero, or a management target as observed revenue.

## Research cadence

1. **Ingest:** retain a readable original source and source card; assign a source ID.
2. **Classify:** link it to one decision gate, state the product/system boundary and add a claim only if it changes the decision record.
3. **Reconcile:** update the relevant NVIDIA/Broadcom dossier, supplier map, company card and/or scenario gate without duplicating content.
4. **Validate:** run the full private validation suite before considering any public derivative.
5. **Release review:** only after the deployment, supplier-content and profit-capture evidence is sufficient; publication requires a separate explicit instruction.

## Next research targets

1. NVIDIA and Broadcom customer/OEM acceptance records with unit or port denominators.
2. CPO-specific bill-of-materials, supply-chain, qualification or packaging disclosures that identify PIC/engine, EIC, laser, fibre-attach, package and test roles.
3. Production manufacturing data for fibre attach, known-good-die, final-engine yield/rework, burn-in and warranty/service.
4. Matched system evidence for CPO versus advanced pluggables, LPO and NPO at 200G/lane and 400G/lane.
5. Lawfully accessible analyst material only after the source/date/fiscal basis can be reconciled to the reported [financial baseline](../08-model/public-financial-baseline-reconciliation.md).
6. Foxconn FY26 Q2 event was listed on 12 August 2026, but its official event page had no results deck or transcript at two retrieval checks. Recheck after files appear, then Q3 results and customer/product records: test the May outlook for Q3 CPO mass production and tens-of-thousands full-year units against actual disclosure using the [event checklist](../09-primary-research/foxconn-q2-cpo-verification-checklist-2026-08-12.md). Do not treat the outlook as actual volume until a dated result identifies what shipped; do not assign generic Foxconn CPO activity to NVIDIA or Broadcom without a product-level link.

## Analyst-input control state

The research can now receive a restricted analyst report without weakening the
evidence boundary. Use the [intake template](../01-sources/analyst-estimates/EST-INTAKE-TEMPLATE.md) for each usable metric, retain the source locally under an ignored `ANL-###` filename, and run `python3 scripts/validate-analyst-estimate-boundary.py` before a model update. This is an ingestion control, not permission to publish proprietary inputs or to calculate a CPO valuation before the product-economics gates clear.
