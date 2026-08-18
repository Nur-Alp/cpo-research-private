# CPO analyst-scenario model specification

**Status:** Input framework; values remain unpopulated until restricted analyst sources are ingested.  
**As of:** 2026-08-12  
**Output:** Relative positive/neutral/negative CPO stance plus EPS and valuation sensitivity; no standalone target price.

## Model sequence

```text
reconciled consensus baseline
+ incremental CPO scenario
- legacy-content cannibalisation
- yield, rework and warranty cost
- incremental R&D / qualification
= incremental operating profit
→ incremental EPS
→ valuation sensitivity
```

## Required scenario inputs

| Driver | Unit | Source class | Bear | Base | Bull | Control |
|---|---|---|---:|---:|---:|---|
| Defined systems per year | systems | Analyst estimate / public fact | Pending | Pending | Pending | Exact deployment boundary required |
| CPO adoption rate | % | Nur Alpys scenario | Pending | Pending | Pending | Cannot exceed defined system denominator |
| Engines per system | engines | Product architecture | Pending | Pending | Pending | Do not transfer across platforms |
| Supplier content per engine | USD | Analyst estimate / public fact | Pending | Pending | Pending | One value-chain layer only |
| Qualified supplier share | % | Analyst estimate / public fact | Pending | Pending | Pending | Customer/qualification boundary required |
| Realised ASP | USD | Analyst estimate | Pending | Pending | Pending | Separate from content if pass-through exists |
| Product gross margin | % | Analyst estimate / assumption | Pending | Pending | Pending | Never use consolidated margin as fact |
| Yield/rework/warranty burden | % of revenue or USD | Assumption | Pending | Pending | Pending | Labelled sensitivity until observed data exists |
| Legacy gross-profit cannibalisation | USD | Assumption | Pending | Pending | Pending | Avoid double count with platform content |
| Incremental R&D / qualification | USD | Analyst estimate / assumption | Pending | Pending | Pending | Period-specific |
| Effective tax rate | % | Analyst baseline | Pending | Pending | Pending | Reconcile accounting basis |
| Diluted shares | shares | Analyst baseline / filing | Pending | Pending | Pending | ADR/share treatment explicit |
| Valuation multiple | x | Analyst estimate / scenario | Pending | Pending | Pending | Sensitivity only, not price target |

## Formula controls

```text
attributable CPO revenue
= systems × adoption rate × engines per system × supplier content per engine × qualified supplier share

incremental gross profit
= attributable CPO revenue × product gross margin
 − yield/rework/warranty burden
 − cannibalised legacy gross profit

incremental operating profit
= incremental gross profit − incremental R&D / qualification

incremental EPS
= incremental operating profit × (1 − effective tax rate) ÷ diluted shares

valuation sensitivity
= incremental EPS × valuation multiple
```

## Hard controls

- Scenario assumptions are not facts. Every unobserved input is labelled `external estimate` or `Nur Alpys assumption`.
- No product margin may be populated from consolidated company gross margin without an explicit sensitivity label.
- Do not count platform revenue and optical-engine content in the same revenue bridge unless the contractual boundary proves both accrue to the company.
- Every output must retain its input IDs, as-of date and scenario label.
- If a critical input is absent, show `not eligible` rather than zero.
