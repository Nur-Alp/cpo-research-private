# Analyst-baseline reconciliation audit — 12 August 2026

**Status:** Private control record; no CPO EPS, valuation or target-price output
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC

## Audit result

The current analyst layer contains one public, provisional consolidated-scale
snapshot (`ANL-002`) and no licensed sell-side rows with complete estimate
metadata. It is adequate to describe **external scale expectations**, but not
to calculate a current consensus range or a CPO earnings overlay.

| Control | Current result | Consequence |
|---|---|---|
| Source identity and retrieval date | `ANL-002`, retrieved 2026-08-10 | Public source can be cited as a provisional snapshot, not a fully audited consensus set |
| Fiscal-period labels | Company fiscal labels are recorded; cross-company calendar mapping is incomplete | Do not compare growth or valuation across companies as if periods were identical |
| Currency and listing | USD rows are retained; TSMC remains TWD/Taiwan-listing context | No ADR/FX/share-ratio comparison yet |
| GAAP/non-GAAP basis | Reported baseline distinguishes bases where available; estimate snapshot is mainly sales/EBIT | No EPS bridge or blended margin calculation |
| Diluted shares and tax | Not reconciled for all six companies | CPO EPS cannot be calculated |
| Valuation multiple | Not reconciled | No valuation sensitivity or target price |
| Staleness | Snapshot is within the 90-day rule as of 2026-08-12 | Refresh by 2026-11-08 or exclude from current range |
| CPO numerator | No exact CPO revenue, units, content, share, margin, yield or warranty input | CPO overlay remains **not eligible** |

## Company status

| Company | Baseline usable for | Missing before a private EPS sensitivity | Current output |
|---|---|---|---|
| NVIDIA | Reported/public-consensus scale context | fiscal/share/tax/multiple reconciliation plus exact CPO numerator and economics | Relative stance only |
| Broadcom | Reported/public-consensus scale context | fiscal/share/tax/multiple reconciliation plus TH6 customer/content/economics | Relative stance only |
| Coherent | Reported/public-consensus scale context | GAAP/non-GAAP row reconciliation plus product allocation and economics | Relative stance only |
| Lumentum | Scale context plus disclosed order expectation | order-to-revenue/product bridge plus fiscal/share/tax/multiple and margin boundary | Relative stance only |
| Marvell | Scale context plus management Photonic Fabric targets | fiscal/acquisition/share treatment plus production customer and economics | Relative stance only |
| TSMC | TWD scale context | ADR/FX/share/fiscal mapping plus COUPE output and economics | Relative stance only |

## Hard stop

No number from `ANL-002` or any future analyst source may populate systems,
adoption, engines, supplier content, ASP, share, yield, warranty, product
margin, CPO revenue, CPO EPS or valuation unless the estimate row is complete
and the relevant exact-product commercial gates are separately cleared. The
correct value while a critical field is missing is **not eligible**, not zero.

## Next intake packet

For each new licensed report, add one complete `EST-###` row with source ID,
firm/private identifier, report/as-of date, fiscal period, unit/currency,
GAAP/non-GAAP basis, page/table location, public-use status and caveats. Then
reconcile it to the [reported baseline](../public-financial-baseline-reconciliation.md)
before using it in a scenario.

Related controls: [analyst-estimate register](../analyst-estimate-register.md),
[estimates-to-variant reconciliation](estimates-to-variant-reconciliation-2026-08-12.md),
[scenario specification](scenario-model-specification.md), [quarterly refresh
checklist](quarterly-refresh-checklist.md), and [public-release manifest](../../00-scope/public-release-manifest-2026-08-12.md).
