# Restricted analyst-estimate library

Place lawfully accessed sell-side reports, model excerpts and estimate spreadsheets in this folder. The folder is ignored by Git except for this guide: source files must remain private and must never be copied to the public Quarto website.

Two controlled public-source intake records are retained alongside this guide:

- `ANL-001-cpo-market-forecast-comparison-2026-08-10.md` — public excerpts from commercial CPO market reports, retained as a dispersion check only.
- `ANL-002-public-consensus-baselines-2026-08-10.md` — public consolidated-company consensus snapshot for scale checks, not a CPO forecast.

## Intake rule

For each source, add one `ANL-###` record to [the analyst-estimate register](../../08-model/analyst-estimate-register.md) before using any number in a model. Record the firm, report date, as-of date, access restriction, exact page/table, metric definition, fiscal period, units, accounting basis and public-use status.

## Permitted internal use

- Consensus range construction and variance analysis.
- Bear/base/bull scenario inputs, clearly marked as external estimate or Nur Alpys assumption.
- Private company cards, model audit and quarterly forecast-versus-outcome review.

## Prohibited public use

- Uploading a report, screenshot, table or model page.
- Publishing a named analyst’s exact number unless licence terms clearly permit it.
- Treating an analyst estimate as a customer shipment, product yield, ASP, margin or other observed fact.

## Naming convention

`ANL-###-firm-company-asof-YYYY-MM-DD.ext`

Example: `ANL-001-exampleresearch-cohr-2026-08-10.pdf`.
