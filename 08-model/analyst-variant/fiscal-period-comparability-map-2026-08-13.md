# Fiscal-period comparability map — six-company CPO research

**Status:** Private baseline control; not an estimate, valuation model or CPO forecast  
**As of:** 2026-08-13  
**Purpose:** Prevent a company fiscal label from being silently treated as an equivalent calendar period in the analyst/variant layer.

## Hard rule

A fiscal-year label is a reporting convention, not a common economic period.
This map is a comparability aid only: it does not translate consolidated company
results into CPO revenue, margin, growth or valuation. Any exact calendar-year
comparison still requires the underlying reported period, accounting basis,
currency and share treatment to be retained beside the number.

## Reporting-calendar map

| Company | Reporting convention used in this workspace | Latest retained result | Calendar-period interpretation | Permitted current use | Prohibited shortcut |
|---|---|---|---|---|---|
| NVIDIA | Fiscal year ends in late January; `FY2027` begins in calendar 2026 | Q1 FY2027, quarter ended 26 Apr 2026 (`FIL-005`) | Primarily calendar Q2 2026 operating period | Company-specific scale anchor with its original fiscal label | Treating FY2027 growth as calendar-2027 growth or comparing it directly with calendar FY2026 results |
| Broadcom | Fiscal year ends in early November | Q2 FY2026, quarter ended 3 May 2026 (`FIL-004`) | Primarily calendar Q2 2026 operating period | Company-specific scale anchor with its original fiscal label | Treating Q2 FY2026 as the same elapsed period as a June-quarter company without the exact dates |
| Coherent | Fiscal year ends in June | Q4 FY2026, quarter ended 30 Jun 2026 (`FIL-015`; `CLM-561`) | Calendar Q2 2026 close; full fiscal year broadly spans Jul 2025–Jun 2026 | Latest consolidated materiality denominator | Aligning FY2026 directly to calendar 2026 or using its gross margin as CPO margin |
| Lumentum | Fiscal year ends in June | Q4/FY2026, quarter and year ended 27 Jun 2026 (`FIL-014`) | Calendar Q2 2026 close; full fiscal year broadly spans Jun/Jul 2025–Jun 2026 | Latest consolidated materiality denominator and dated order-context record | Comparing FY2026 consensus growth directly to December- or January-year peers without mapping |
| Marvell | Fiscal year ends in late January/early February; `FY2027` begins in calendar 2026 | Q1 FY2027, released 27 May 2026 (`FIL-006`; `CLM-096`) | Primarily calendar Q2 2026 result window | Company-specific scale and post-acquisition materiality anchor | Treating FY2027 targets as calendar-2027 CPO revenue or comparing acquisition-period results to a full year |
| TSMC | Calendar fiscal year ends in December; Taiwan listing is the reported-company reference | Q2 2026 (`FIL-010`) | Calendar Q2 2026 | Calendar-year company scale only, at its reported currency/listing boundary | Combining TSMC Taiwan-listing data with ADR valuation or USD peers without a dated FX/ADR/share bridge |

## Comparability tests before any cross-company statement

1. **Period test:** state both the fiscal label and the actual quarter/year end.
2. **Basis test:** do not blend GAAP, non-GAAP, adjusted EBITDA, EBIT or management guidance.
3. **Currency/listing test:** keep TSMC in its reported Taiwan-listing/currency context until a dated FX and ADR-ratio record exists.
4. **Share test:** do not calculate EPS sensitivity without a period-matched diluted-share count and tax-rate basis.
5. **Boundary test:** a consolidated result remains a materiality denominator; it never supplies a CPO product numerator or margin.

## Current output

The six company anchors may be discussed as individually dated scale context.
They are **not yet a harmonised consensus or valuation dataset**. Therefore the
analyst/variant layer remains limited to relative, evidence-gated stances; all
CPO EPS and valuation sensitivities remain **not eligible**.

Related controls: [public financial baseline reconciliation](../public-financial-baseline-reconciliation.md), [analyst baseline reconciliation audit](analyst-baseline-reconciliation-audit-2026-08-12.md), [analyst-estimate register](../analyst-estimate-register.md), and [scenario specification](scenario-model-specification.md).
