# Public financial-baseline reconciliation

**Status:** Private control record — reported-company baseline only; not a CPO forecast  
**As of:** 2026-08-12
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC

## Purpose

This record creates the denominator required before an analyst-expectations or CPO-sensitivity layer can be credible. It reconciles the latest retained **reported** company financial anchor with the fiscal label, accounting basis and product boundary used in the CPO model.

It is deliberately distinct from:

- the restricted [analyst-estimate register](analyst-estimate-register.md), which records external expectations;
- the [CPO earnings and valuation bridge](earnings-valuation-bridge-template.md), whose CPO overlay remains **not eligible**; and
- a valuation model or price target.

No row below assigns a dollar, margin, unit, share or cash-flow amount to CPO.

## Reconciliation rules

1. A fiscal label is retained exactly as reported. Do not compare fiscal years across companies as calendar years without an explicit period mapping.
2. Revenue, gross margin, cash flow, capex and share counts remain on their reported accounting basis. GAAP and non-GAAP values are never blended.
3. A company or segment metric is a **materiality denominator**, not a CPO numerator or a CPO product-margin proxy.
4. Use the most recent retained filing/result for a baseline. A newer source can replace it only with its source ID, report date and boundary recorded here.
5. An EPS or valuation sensitivity cannot be calculated until compatible tax rate, diluted shares, scenario output and accounting basis are present. This record does not clear that gate.
6. TSMC is recorded in its reported currencies and Taiwan listing context. Any ADR, FX or share-ratio analysis requires a dated reconciliation row before use.

## Latest reported anchors

| Company | Latest retained reported period | Source | Reported baseline | Fiscal / unit control | CPO boundary |
|---|---|---|---|---|---|
| NVIDIA | Q1 FY2027, quarter ended 26 Apr 2026 | `FIL-005`; `CLM-088` | Revenue $81.615bn; Data Center $75.178bn; GAAP gross margin 74.9% | USD; company fiscal label retained | Data Center and networking do not disclose CPO revenue, margin, systems, supplier share or capex. |
| Broadcom | Q2 FY2026, quarter ended 3 May 2026 | `FIL-004`; `CLM-087` | Revenue $22.187bn; company-defined AI semiconductor revenue $10.8bn; free cash flow $10.262bn; adjusted EBITDA $15.244bn; capex $231m | USD; company fiscal label retained; adjusted EBITDA is not GAAP operating income | AI semiconductor is broader than CPO. No switch-CPO revenue, units, engine content or CPO margin is reported. |
| Coherent | Q3 FY2026, quarter ended 28 Mar 2026 | `FIL-002` | Revenue $1.806bn; GAAP gross margin 37.7%; non-GAAP gross margin 39.6% | USD; GAAP and non-GAAP kept separate | Consolidated result; no CPO engine revenue, yield, ASP, customer qualification or CPO margin. |
| Lumentum | Q4 and FY2026, quarter and fiscal year ended 27 Jun 2026 | `FIL-014` | Q4 revenue $1.0063bn; Q4 GAAP gross margin 47.4%; Q4 non-GAAP gross margin 50.4%; FY2026 revenue $3.0140bn; FY2026 GAAP gross margin 41.7%; FY2026 non-GAAP gross margin 46.0% | USD; quarter and full-year measures remain separate; GAAP and non-GAAP values are not blended | Consolidated results remain broader than CPO/ELS; the initial ELS-module-order statement has no disclosed CPO allocation, product margin, revenue-recognition or unit boundary. |
| Marvell | Q1 FY2027, released 27 May 2026 | `FIL-006`; `CLM-096` | Revenue $2.418bn; GAAP gross margin 52.1%; non-GAAP gross margin 58.9%; operating cash flow $638.8m | USD; GAAP and non-GAAP kept separate; results include Celestial and XConn from acquisition dates | No separate Photonic Fabric/CPO revenue, margin, customer, units, bookings or yield. Management commentary is not an allocation. |
| TSMC | Q2 2026 results | `FIL-010` | Revenue US$40.20bn; gross margin 67.7%; operating margin 60.3%; net profit margin 55.6% | TSMC-reported result; retain reported currency and Taiwan-listing context until a dated ADR/FX bridge is added | No COUPE, advanced-packaging or CPO revenue, output, yield, margin, capex or customer allocation is reported. |

## Baseline-to-scenario eligibility

| Required field | Reported company baseline | External-expectation baseline | CPO overlay | Status |
|---|---|---|---|---|
| Revenue | Six anchors above | Provisional `ANL-002` coverage | No attributable CPO revenue | **Blocked** |
| Gross margin | Reported company margin where disclosed | Pending compatible consensus field | No CPO product margin | **Blocked** |
| Operating margin / operating profit | Partial company disclosure only | Provisional for some companies | No CPO incremental opex/R&D | **Blocked** |
| Capex | Partial company disclosure only | Provisional for Coherent only | No CPO-attributed capex | **Blocked** |
| Diluted shares | Marvell Q2 FY27 guidance is retained; all-company compatible baseline not reconciled | Pending | No CPO EPS bridge | **Blocked** |
| Tax and valuation multiple | Not reconciled | Pending / restricted | No CPO valuation sensitivity | **Blocked** |

The word **blocked** means “do not calculate”, not zero. A CPO model may use an explicit scenario assumption only after it is labelled as such and traceable in the analyst-scenario specification.

## Fiscal-period comparability control

The six company reporting periods are now mapped in the
[fiscal-period comparability map](analyst-variant/fiscal-period-comparability-map-2026-08-13.md).
It permits individually dated company-scale context, but it does **not** create
a harmonised cross-company consensus dataset: NVIDIA and Marvell use
January/early-February fiscal conventions, Broadcom uses November, Coherent and
Lumentum use June, and TSMC uses a December calendar year. TSMC ADR/FX/share
treatment remains separately blocked.

## Analyst-layer handoff

`ANL-002` is retained as a provisional, public-consensus scale check. It must be refreshed by 2026-11-08 or excluded from a current consensus range. A licensed analyst report, if added, must first reconcile to the relevant reported baseline above by fiscal period, currency, GAAP/non-GAAP basis and share treatment.

Before an analyst expectation can support a company card, the card must contain:

1. one reported financial anchor from this record;
2. one dated expectation record;
3. one explicitly labelled CPO scenario input or an explicit **not eligible** result; and
4. a falsification event that can be observed publicly.

## Explicit prohibitions

- Do not multiply CPO revenue by NVIDIA, Broadcom, Coherent, Lumentum, Marvell or TSMC consolidated gross margin and call the result CPO gross profit.
- Do not attribute company AI, networking, Components, Systems, Data Center or advanced-technology growth to CPO without a disclosed product boundary.
- Do not compare TSMC's Taiwan listing to its ADR, or compare companies on calendar-year growth, without dated conversion and fiscal-period controls.
- Do not infer customer demand, accepted units, repeat shipments, yield or warranty economics from the reported baselines.

## Audit checklist

- [x] Six companies have a retained primary reported anchor.
- [x] Every baseline row names the source ID and fiscal/report period.
- [x] GAAP/non-GAAP distinctions are visible where both are disclosed.
- [x] Every row preserves the CPO attribution boundary.
- [x] Fiscal labels and the current reported-period calendar windows are mapped; a period-matched comparison is still required for each future cross-company calculation.
- [ ] Exact diluted-share, effective-tax-rate and valuation-multiple baselines reconciled.
- [ ] Any CPO earnings or valuation sensitivity eligible.
