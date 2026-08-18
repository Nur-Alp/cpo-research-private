# Public-release manifest — 12 August 2026

**Status:** Private control document. **No publication, commit or push is authorized.**  
**Owner:** Nur Alpys  
**Purpose:** Define the evidence boundary for any future public Quarto release. The private workspace is the evidence system of record; this manifest is a release gate, not a publication itself.

## Permitted public evidence classes

Only the following may enter the public report after a separate release approval:

- Original explanations, diagrams, tables and calculations created for the report.
- Derived ranges or scenarios whose inputs are identified as facts, estimates or Nur Alpys assumptions.
- Publicly available factual claims with a canonical original URL and a source ID.
- Clearly labelled **Fact**, **Inference**, **Forecast** and **Open question** statements.
- Public company filings, official product documentation, standards, academic papers and other sources whose public-use status is recorded.
- Figure captions containing source IDs, canonical links, as-of dates, calculation boundaries and a reproducibility note.

## Prohibited public evidence classes

The following must remain private, even when they inform a derived conclusion:

- Raw or converted source PDFs, HTML archives, screenshots and downloaded copyrighted material.
- Restricted analyst reports, model pages, spreadsheets, exact proprietary estimates and analyst-only commentary.
- Interview notes, private correspondence, confidential contracts, customer disclosures or unpublished model workings.
- Private filesystem paths, repository structure that exposes restricted materials, and credentials or access details.
- Unverified customer/SKU joins, implied shipment volumes, inferred supplier assignments or roadmap language presented as observed fact.
- Supplier ASP, share, yield, rework, warranty, margin or capacity figures unless their public-use status and product boundary are explicit.
- Consolidated company financials silently relabelled as CPO product economics.
- CPO-specific revenue, EPS, valuation or market-share estimates that cannot be reproduced from public inputs.

## Required claim-level release record

Every material public claim, number and figure must have the following fields in the release ledger before publication:

| Field | Requirement |
|---|---|
| Claim/exhibit ID | Stable ID linked to `claim-ledger.csv` or the figure register |
| Source ID and canonical URL | Direct public source; local path alone is insufficient |
| Claim type | Fact, company claim, estimate, inference, forecast or open question |
| Evidence grade | Confidence and boundary stated in plain language |
| Chapter/exhibit | Exact public destination |
| Public-use status | Cleared, derived-only, or blocked |
| Private dependency | Explicitly states whether restricted material informed the result |
| Falsification condition | What new evidence would change or withdraw the claim |

## Mandatory pre-release checks

Before any public render or deployment, all of these must pass:

1. No private paths, raw archives, analyst files, interview notes or restricted source material appear in rendered HTML, PDF, assets or metadata.
2. Every material factual assertion has a public citation; every inference and forecast is labelled and has a falsification condition.
3. Every figure has source metadata, an as-of date, a calculation boundary and a short recreation method.
4. All bibliography keys resolve, internal links and local assets resolve, and external source links are checked or manually marked inaccessible.
5. The public report contains no exact-SKU customer, units, repeat-shipment, supplier-economics or CPO-earnings conclusion unless the corresponding commercial gate is cleared.
6. Quarto HTML and PDF renders complete successfully and pass visual inspection for navigation, tables, figures and page boundaries.
7. The commercial-proof validator remains false unless the exact evidence gates are genuinely cleared; a framework or vendor announcement cannot change this automatically.
8. A dated release manifest is reviewed and explicitly approved before publication, commit or push.

## Current release decision

**Blocked / build-only.** The current evidence supports the conditional conclusion that switch-side 200G/lane CPO has the strongest disclosed timing signal, but it does not establish an exact-SKU deployed-volume leader, repeatable production denominator, final-engine/service-cost advantage or CPO profit-pool leader.

The decisive open fields remain:

- exact customer tied to the exact NVIDIA or Broadcom CPO SKU;
- accepted units, ports or systems and date;
- repeat shipment or expansion;
- field-service, reliability and warranty record;
- product-linked supplier content, ASP, qualified yield, rework and margin;
- matched CPO-versus-LPO/NPO/retimed system economics.

No public release is authorized while these gates remain open. This manifest does not replace the [objective completion audit](objective-completion-audit-2026-08-12.md), [final decision-readiness matrix](final-decision-readiness-matrix.md), or [commercial-proof audit](../09-primary-research/commercial-proof-readiness-audit-2026-08-11.md); it binds them to a concrete publication control.
