# Analyst-layer completion audit — 12 August 2026

**Status:** Private control document; no CPO EPS, valuation or target-price output
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC

## Audit verdict

The analyst layer is structurally ready for lawful intake but not populated
enough for a current consensus range or a company-specific CPO sensitivity.
`ANL-001` is a definition-dispersed market-forecast comparison and `ANL-002`
is a provisional consolidated scale snapshot. Neither supplies a product-
matched CPO numerator or economics. No restricted sell-side report has yet
cleared the intake schema in the private library.

## Field-by-field result

| Control | Current state | Required before use |
|---|---|---|
| Source and access identity | `ANL-001` and `ANL-002` documented; no licensed sell-side row | `ANL-###` source ID, access restriction and retention status |
| Report/as-of date | Present for current snapshots | Exact report date and market-data cutoff for each estimate row |
| Fiscal period | Company labels partly recorded; cross-company mapping incomplete | Exact fiscal year/quarter plus calendar mapping |
| Currency and units | USD and TWD contexts visible; TSMC ADR/FX unresolved | Currency, unit, ADR ratio, split adjustment and FX date |
| Accounting basis | Reported baselines distinguish GAAP/non-GAAP where available; consensus rows are incomplete | Metric-level GAAP/non-GAAP/adjusted basis |
| Revenue and margin | Consolidated scale context only | Reconciled revenue, gross margin and operating margin rows |
| EPS, shares and tax | Incomplete for all six companies | Diluted shares, effective tax and EPS basis |
| Valuation multiple | Not reconciled | Dated price, enterprise/equity convention and multiple basis |
| Staleness | `ANL-002` remains within 90 days at this cut-off | Refresh by 2026-11-08 or exclude from current range |
| CPO overlay | No exact product/customer/content/share/economics | Exact commercial gates plus product-level inputs |

## Company readiness

| Company | External expectation use now | CPO overlay | Blocking issue |
|---|---|---|---|
| NVIDIA | Consolidated scale context | Not eligible | Exact CPO customer denominator and fiscal/share/multiple reconciliation |
| Broadcom | Consolidated scale context | Not eligible | TH6 customer acceptance, content/share and accounting reconciliation |
| Coherent | Consolidated scale and capacity context | Not eligible | Product allocation, order conversion and product margin |
| Lumentum | Consolidated scale plus order-expectation context | Not eligible | Order-to-product/customer/quantity bridge and margin |
| Marvell | Consolidated scale plus management target context | Not eligible | Photonic Fabric customer production and acquisition/share treatment |
| TSMC | TWD scale context | Not eligible | ADR/FX/share reconciliation and COUPE output/economics |

## Hard controls

- A market-size forecast cannot create a systems denominator.
- Consolidated revenue, EBIT or gross margin cannot create CPO ASP, share,
  yield, warranty or product margin.
- Management targets and analyst estimates remain separate evidence classes.
- A stale estimate is historical context, not a current consensus input.
- A restricted number may enter a private scenario only after all metadata are
  complete; public output may contain only a permitted derived range.
- No CPO EPS or valuation sensitivity is eligible until exact-product
  commercial and economic gates clear independently.

## Intake completion checklist

For the next licensed report or model excerpt, complete one `EST-###` row with:

1. source ID, firm/private identifier and access restriction;
2. report/as-of date and exact fiscal period;
3. metric, value/range, unit, currency and accounting basis;
4. page/table/row location;
5. reported-baseline reconciliation, FX/ADR/split treatment;
6. product/contractual boundary and public-use status;
7. scenario linkage, catalyst and falsification condition; and
8. prior-quarter comparison and reviewer/date.

If any field is missing, mark the row **pending** and keep the CPO overlay
**not eligible**.

Related controls: [analyst estimate register](../analyst-estimate-register.md), [baseline reconciliation](../public-financial-baseline-reconciliation.md), [estimates-to-variant reconciliation](estimates-to-variant-reconciliation-2026-08-12.md), [quarterly refresh checklist](quarterly-refresh-checklist.md), and [public release manifest](../../00-scope/public-release-manifest-2026-08-12.md).
