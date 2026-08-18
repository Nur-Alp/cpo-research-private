# Evidence-integrity audit — 2026-08-10

## Checks performed

The local source and claim ledgers were parsed after the latest research batch.

| Check | Result |
|---|---:|
| Source-log rows | 169 |
| Unique source IDs | 169 |
| Claim-ledger rows | 513 |
| Unique claim IDs | 513 |
| Claim rows with missing cited source IDs | 0 |
| CSV rows with schema-width or semantic-field errors | 0 |
| Markdown claim references with missing claim IDs | 0 |
| Missing relative Markdown links | 0 |
| `git diff --check` excluding retained raw HTML | Pass |

## PDF corpus check

The retained `01-sources/**/*.pdf` corpus was opened with `pypdf` and sampled for page extraction:

| Check | Result |
|---|---:|
| PDF files opened | 83 |
| Total pages opened | 1,250 |
| PDFs with zero pages or extraction errors | 0 |
| Largest retained filing | 146 pages (`FIL-013` CoreWeave FY2025 10-K) |

The claim ledger now has 513 rows. “Open” is the workflow status for all claim rows; it does not mean that every claim is unverified. Confidence and evidence boundaries govern how each claim may be used.

Some PDFs emit non-fatal parser warnings about malformed pointing objects while still opening and yielding pages/text. Those files should receive visual inspection before being used for figure-level or table-level claims.

## Scope and limitation

This is a referential-integrity and ledger-schema audit, not a truth audit. It verifies that IDs cited in the ledgers and Markdown, required CSV fields, allowed confidence/status values, local paths cited across the source index and Markdown links resolve. It does not independently validate the factual accuracy of every claim, the quality of a source, customer production volume, final-engine yield, ASP, margin or investment conclusion. Those remain governed by the evidence gates and claim-level limitations.

## Reproducibility

The audit can be repeated with the dependency-free script:

```bash
python3 scripts/audit_evidence.py
python3 scripts/audit_pdfs.py
git diff --check -- ':!01-sources/**/*.html'
```

Any new source or claim batch should rerun both checks before a future intentional commit.
