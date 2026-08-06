# Evidence and Forecasting Standard

**Status:** Active research protocol
**Last updated:** 2026-08-06

## Objective

Every important conclusion must be traceable from evidence through assumptions to a model output. Source volume is not a substitute for evidence quality or independence.

## Evidence hierarchy

1. Customer deployment evidence, standards documents, and regulatory filings
2. Peer-reviewed papers and complete conference proceedings
3. Official product specifications and qualification documentation
4. Patents and detailed technical presentations
5. Supplier and manufacturing evidence
6. Management commentary and earnings calls
7. Trade publications and specialist industry analysis
8. Consultant forecasts
9. Social media and anonymous commentary

Lower-ranked sources are useful for questions and hypotheses but should not independently support a high-impact conclusion.

## Claim labels

- `FACT`: directly supported by a cited primary source
- `COMPANY CLAIM`: stated by a company but not independently verified
- `ESTIMATE`: calculated from cited data and explicit assumptions
- `INFERENCE`: conclusion drawn from multiple facts or estimates
- `OPINION`: judgement not established by evidence
- `UNKNOWN`: important information not available or not yet verified

## Product-status verification

For each company and architecture, separately record:

- Announcement date
- Demonstration date and test boundary
- Sampling date and customer type
- Qualification start and completion
- Limited-production evidence
- Volume-production evidence
- Repeat-order evidence
- Customer deployment evidence
- Revenue materiality

Use `00-scope/terminology.md` for minimum interpretations. Do not use `shipping` without defining samples, qualification units, limited production, or repeat volume.

## Independence standard

Important conclusions should normally have:

1. A primary technical or commercial source
2. Independent corroboration from a customer, supplier, standard, filing, or measurement
3. A documented contradiction search

Multiple articles repeating one company statement count as one underlying source.

## Forecast standard

Every forecast must include:

- Unit and denominator
- Architecture and deployment domain
- Time period
- Low, base, and high cases
- Probability or confidence
- Source and reasoning
- Critical-path milestones
- Sensitivity
- Falsification condition
- Date last updated

Avoid unsupported point estimates. Record a range and the variable that drives it.

## Probability updates

Change adoption probabilities only when evidence affects a defined gate or assumption. Record:

```text
Previous probability
New probability
Evidence ID
Gate affected
Reason for magnitude of change
Date
```

Do not change a probability merely because a company repeats its roadmap.

## Consensus and variant perception

For every proposed investment conclusion, record:

- Evidenced consensus adoption timing
- Consensus revenue and margin assumptions where available
- What appears reflected in valuation
- The research view
- The exact difference
- Evidence required for the difference to close
- Catalyst and expected timing
- Downside if the variant view is wrong

If consensus cannot be evidenced, label it `UNKNOWN` rather than inventing a market view.
