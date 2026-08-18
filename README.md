# CPO Research Private

Investment-grade research on co-packaged optics, with the active workstream focused on scale-out optical engines and PICs.

## Central question

Which CPO architecture reaches meaningful commercial deployment first, in which application and year, and which company captures the largest sustainable incremental profit pool?

The near-term decision question is narrower:

> Which company can manufacture the lowest-total-cost, qualification-ready 200G/lane and later 400G/lane scale-out optical engine while retaining sustainable gross profit after platform owners, customers and manufacturing partners take their shares?

## Scope

The study keeps these architectures separate:

- Retimed and advanced pluggable optics
- LPO
- NPO/OBO
- Switch-side CPO
- Accelerator optical I/O
- AEC, retimers and improved copper

Deployment domains include Ethernet scale-out, accelerator scale-up, inter-rack links and possible memory/disaggregated-compute links. The forecast horizon is 2026–2032.

## Current evidence-adjusted view

- Switch-side 200G/lane CPO has the strongest public commercial-timing signal.
- Broadcom has the clearest merchant-switch CPO product definition.
- NVIDIA has the strongest integrated platform and customer-route evidence.
- Coherent has the broadest disclosed optical-engine/component stack.
- Lumentum has the clearest external-laser/ELSFP commercial signal.
- TSMC, SPIL, TFC, Foxconn and Teradyne/ficonTEC are visible process or equipment control points, but supplier profit ownership is unproven.
- No company is yet proven to capture the largest sustainable optical-engine profit pool.

## Start here

1. [Research question and decision outputs](00-scope/research-question.md)
2. [Current decision memo](00-scope/current-decision-memo-2026-08-11.md)
3. [Scale-out optical-engine profit-pool thesis](00-scope/scale-out-optical-engine-profit-pool-thesis.md)
4. [Optical-engine benchmark](03-components/optical-engine-benchmark.md)
5. [Company leadership scorecard](07-companies/leader-scorecard.md)
6. [Adoption timeline](08-model/adoption-timeline.md)
7. [Commercial-proof probability priors](08-model/commercial-proof-probability-priors.md)
8. [Profit-pool scenario bridge](08-model/profit-pool-scenario-bridge.md)
9. [TCO per delivered bit](08-model/tco-per-delivered-bit-gate.md)
10. [Falsification dashboard](08-model/falsification-dashboard.md)
11. [Primary-research interview question bank](09-primary-research/interview-question-bank.md)
12. [Public-data boundary register](08-model/public-data-boundary-register.md)
13. [Final conclusion](00-scope/final-conclusion-2026-08-10.md)
14. [Commercial-proof closeout](07-companies/commercial-proof-dossiers/commercial-proof-closeout-2026-08-14.md)
15. [Supplier-content map](07-companies/supplier-content-map-2026-08-14.md)
16. [Manufacturing-economics gate](08-model/manufacturing-economics-decision-gate-2026-08-14.md)
17. [CPO conditional-win test](02-architecture/cpo-conditional-win-test-2026-08-14.md)
18. [Six company conclusions](07-companies/six-company-investable-conclusions-2026-08-14.md)

## Evidence standard

Every material claim should be traceable to:

- a retained local PDF/HTML or a canonical direct link;
- a source ID in [`01-sources/source-log.csv`](01-sources/source-log.csv);
- a claim ID in [`01-sources/claim-ledger.csv`](01-sources/claim-ledger.csv);
- an explicit evidence boundary and limitation.

Company announcements establish what a company claims. They do not independently establish customer units, final-engine yield, qualification, field reliability, ASP, margin or supplier profit.

Run `python3 scripts/audit_evidence.py` after adding a source or claim batch. The latest referential-integrity results are recorded in [evidence-integrity-audit-2026-08-10.md](01-sources/evidence-integrity-audit-2026-08-10.md). Check the retained PDF corpus with `python3 scripts/audit_pdfs.py`.

The current ledger contains 218 retained sources and 584 claim records. The retained PDF corpus is separately audited rather than inferred from filenames; run `python3 scripts/audit_pdfs.py` after adding a PDF batch.

## Repository map

| Directory | Purpose |
|---|---|
| `00-scope` | Research question, thesis and decision outputs |
| `01-sources` | Retained papers, standards, filings, product sources and ledgers |
| `02-architecture` | CPO/LPO/NPO/copper architecture comparisons |
| `03-components` | PIC, laser, packaging and optical-engine benchmarks |
| `07-companies` | Company dossiers and leadership scorecards |
| `08-model` | Adoption, yield, TCO, service and profit-pool models |
| `09-primary-research` | Interview questions and future primary evidence |

## Current decision status

The project is **not yet investment-decision-ready**. The highest-priority open inputs are customer-confirmed CPO SKU/units, complete engine BOM and supplier share, final-engine yield, qualification and field-service data, matched CPO/LPO/NPO TCO, ASP/margin, capex and valuation expectations. The [public-data boundary register](08-model/public-data-boundary-register.md) distinguishes fields that are generally private from gaps that can still be closed with public evidence.
