# Analyst-estimate register

**Status:** Restricted-input register; public-source external-estimate snapshots ingested, but no licensed sell-side report retained  
**Owner:** Nur Alpys  
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC  
**Public-use rule:** Derived ranges and conclusions only; raw reports and named-estimate detail remain private unless licence terms clearly allow publication.

Use the [estimates-to-variant reconciliation](analyst-variant/estimates-to-variant-reconciliation-2026-08-12.md)
as the release-control summary for fiscal, currency, share, product-boundary
and public-use checks.

The [analyst-baseline reconciliation audit](analyst-variant/analyst-baseline-reconciliation-audit-2026-08-12.md)
records the current intake result: no complete licensed sell-side estimate row
is yet available, and `ANL-002` remains a provisional scale check only.

The [analyst-layer completion audit](analyst-variant/analyst-layer-completion-audit-2026-08-12.md)
is the current field-level release control for fiscal, currency, accounting,
staleness and CPO-overlay eligibility.

## Controlled fields

Every estimate row must include all fields below. Do not add a number to a scenario model until its source row is complete.

| Field | Required content |
|---|---|
| Estimate ID | `EST-###`, unique and immutable |
| Source ID | Linked `ANL-###` record in the restricted library |
| Firm / analyst | Private identifier; never publish by default |
| Report date / as-of date | Publication date and market-data/estimate cutoff date |
| Company / ticker | One of NVDA, AVGO, COHR, LITE, MRVL or TSM |
| Fiscal period | Exact company fiscal year/quarter, plus calendar-year mapping where relevant |
| Metric | Revenue, gross margin, operating margin, EPS, capex, diluted shares, valuation multiple, CPO revenue, CPO content, adoption or other named driver |
| Value / range / unit | Numerical value or low/base/high range; USD millions, USD/share, percentage, units, engines, systems or multiple |
| Accounting basis | GAAP, non-GAAP, adjusted, reported, estimated or forecast |
| Report location | Page, table, chart and row/column label |
| Evidence classification | External estimate, management target, public fact or Nur Alpys assumption |
| Public-use status | `private-only`, `derived-range-permitted`, or `publicly-citable` |
| Notes / caveat | Definition, exclusions, product boundary and reason an estimate may not be comparable |

## Intake queue

| Source ID | Firm | Company | Report/as-of date | Restriction | Ingestion status | Notes |
|---|---|---|---|---|---|---|
| `ANL-001` | Public commercial-report excerpts | CPO market | 2025–2026 publications; retrieved 2026-08-10 | Public links, paid full reports not retained | Ingested | Wide and non-comparable top-down forecasts; scenario context only. See `01-sources/analyst-estimates/ANL-001-cpo-market-forecast-comparison-2026-08-10.md`. |
| `ANL-002` | MarketScreener public consensus pages | NVDA, AVGO, COHR, LITE, MRVL, TSM | Retrieved 2026-08-10 | Public data; provider methodology not fully audited | Ingested provisionally | Consolidated scale checks only; no CPO allocation or exact EPS sensitivity permitted. See `01-sources/analyst-estimates/ANL-002-public-consensus-baselines-2026-08-10.md`. |
| `ANL-003` onward | Pending user-provided licensed report | Pending | Pending | Private-only by default | Awaiting source | Use only if lawfully accessible; preserve the original report and report-location fields. |

## Baseline-metric completion matrix

| Company | Revenue | Gross margin | Operating margin | EPS | Capex | Diluted shares | Valuation multiple | Fiscal-year mapping | Status |
|---|---|---|---|---|---|---|---|---|---|
| NVIDIA | Reported anchor; external estimate pending | Reported anchor only | Pending | Pending | Pending | Pending | Pending | Retain company fiscal label | Consolidated scale only; see public baseline reconciliation |
| Broadcom | Reported anchor; provisional external estimate | Pending | Provisional external estimate | Pending | Reported capex; no forecast baseline | Pending | Pending | Retain company fiscal label | AI semiconductor is not CPO; see public baseline reconciliation |
| Coherent | Reported anchor; provisional external estimate | Reported anchor only | Provisional external estimate | Pending | Provisional external estimate | Pending | Pending | Retain company fiscal label | Consolidated scale only; see public baseline reconciliation |
| Lumentum | Reported anchor; provisional external estimate | Reported anchor only | Provisional external estimate | Pending | Reported capex; no forecast baseline | Pending | Pending | Retain company fiscal label | Consolidated scale only; see public baseline reconciliation |
| Marvell | Reported anchor; provisional external estimate | Reported anchor only | Provisional external estimate | Reported non-GAAP EPS only; no consensus bridge | Pending | Q2 guidance only; not reconciled | Pending | Retain company fiscal label | Photonic Fabric allocation remains absent; see public baseline reconciliation |
| TSMC | Reported anchor; provisional external estimate (TWD) | Reported anchor only | Provisional external estimate (TWD) | Pending | Pending | Pending | Provisional; ADR reconciliation pending | Retain company fiscal label | ADR/currency reconciliation still required |

## Readiness matrix for a CPO investment sensitivity

This is the release-control view. A company can have a usable consolidated denominator while its CPO overlay remains **not eligible**. “Pending” is not a zero and does not imply that the missing value can be inferred from company scale.

| Company | Consolidated baseline | Fiscal/currency/share reconciliation | Exact CPO product boundary | Customer volume and repeatability | Supplier content/share | Product margin/yield/warranty | EPS/valuation sensitivity |
|---|---|---|---|---|---|---|---|
| NVIDIA | Partial reported/public-consensus scale | Pending | Partial: `SN6810`/`SN6800` defined | Open | Open | Open | **Not eligible** |
| Broadcom | Partial reported/public-consensus scale | Pending | Partial: `BCM78919` defined | Open | Open | Open | **Not eligible** |
| Coherent | Partial reported/public-consensus scale | Pending | Route-level CPO/engine families | Open | Open | Open | **Not eligible** |
| Lumentum | Partial reported/public-consensus scale | Pending | Route-level ELSFP/UHP laser boundary | Open | Open | Open | **Not eligible** |
| Marvell | Partial reported/public-consensus scale | Pending | Accelerator optical-I/O boundary, not switch-CPO | Open | Open | Open | **Not eligible** |
| TSMC | Partial reported/public-consensus scale, TWD | ADR/currency/share treatment pending | COUPE process route, not complete-engine SKU | Open | Open | Open | **Not eligible** |

### Overlay release rule

An analyst estimate may enter a private CPO scenario only when its fiscal period, accounting basis, unit, product boundary, source ID, as-of date and public-use status are complete **and** the commercial/economic gates for the relevant company are separately addressed. Until then, use analyst material to document expectations or sensitivity ranges—not to fill customer units, supplier share, ASP, product margin, yield, warranty or CPO EPS.

## Reconciliation rules

1. Preserve individual estimates; calculate a current range only from estimates with an as-of date no more than 90 days old.
2. Keep stale estimates in the historical record. Exclude them from the current range unless a note explicitly preserves them for a historical-expectations comparison.
3. Never combine GAAP and non-GAAP metrics without an explicit reconciliation row.
4. Reconcile fiscal year, currency, share class, ADR ratio and split-adjustment before comparing companies or calculating valuation sensitivity.
5. Management guidance and analyst consensus are separate estimate classes. Do not average them.
6. A CPO-specific input must identify the product boundary. Do not infer it from consolidated company revenue or gross margin.
7. The [public financial-baseline reconciliation](public-financial-baseline-reconciliation.md) is the required reported-company denominator before any analyst row becomes a scenario input.

## Quarterly refresh controls

- Preserve the prior-quarter consensus range and published variant view.
- Add the new source rows with their original as-of dates.
- Recalculate the current range, explain material changes and compare prior estimates with reported results.
- Record whether a catalyst was achieved, delayed, withdrawn or remains unobserved.
