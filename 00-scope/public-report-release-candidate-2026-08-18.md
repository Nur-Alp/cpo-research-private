# Public CPO report — release-candidate update plan

**Status:** Private pre-publication control; no website update, commit, push or deployment authorized  
**As of:** 18 August 2026  
**Purpose:** Convert only permissible, decision-changing private research into a public report refresh.

## Release decision

The existing public Quarto book is internally consistent: its 35 in-text
citation keys resolve to the bibliography. It is **not current**: its evidence
cut-off is 10 August 2026 and it lacks the 13–18 August technical/system-test
updates and the closed commercial-proof synthesis.

The next public edition may publish the conclusion that the **public record
does not establish** customer-confirmed CPO scale or a profit-pool leader. It
may not publish a claimed customer deployment, supplier share, product yield,
margin, analyst estimate or CPO EPS sensitivity.

## Permissible additions

| Public report destination | Public-safe change | Required public source | Private evidence that must remain private |
|---|---|---|---|
| Executive summary | Replace broad production rhetoric with: “product and production-route evidence is stronger than exact-SKU customer/scale proof.” | NVIDIA official product/manufacturing pages; Broadcom product page/release. | Exact-SKU search logs, customer-retrieval notes and private commercial-proof files. |
| Manufacturing chapter | Add historic 51.2T CPO system-test context, measured FOWLP package evidence and measured 180-GBaud driver/modulator boundary. | DOI/canonical pages for PAP-055, PAP-056 and PAP-051. | Downloaded conference PDFs, extracted figures and all source notes. |
| Architecture chapter | State the conditional CPO-win test: lower all-in inlet power, qualified yield/rework and lower restored-port cost at the same boundary. | Existing OIF/IEEE and public company/product sources; new papers where relevant. | Private sensitivity calculations and non-public model inputs. |
| Company cases | Use six compact evidence-gated stances; name the exact NVIDIA/Broadcom product boundaries and state the missing customer/scale/economics fields. | Official NVIDIA/Broadcom/TSMC/Coherent/Lumentum/Marvell filings and pages. | Supplier-content map allocations beyond the disclosed public role. |
| Methodology / change log | Advance cut-off to 18 August; record a negative public exact-SKU refresh without claiming non-deployment. | Public canonical product pages/release links; dated methodology statement. | Search queries, inaccessible-page captures and all private audits. |

## Mandatory bibliography additions before any public edit

| Proposed key | Public source-of-record | Allowed claim boundary |
|---|---|---|
| `amiralizadeh2025cpo` | DOI: `10.1109/ECOC66593.2025.11263202` | Historical 51.2T Bailly/TH5 system-test configuration, bounded power comparison and stressed self-loopback reliability—not TH6 deployment. |
| `wu2026fowlp` | DOI: `10.1117/12.3085221` | 1.6T FOWLP package/interconnect measurement; 6.4T/12.8T remains modeled. |
| `tran2026driver` | DOI: `10.1364/OFC.2026.W3E.6` | 180-GBaud driver/modulator subassembly, measurement condition and partial-power boundary—not full engine power or qualification. |
| `broadcom2025bcm78919` | Broadcom official product brief/page | Exact merchant CPO product/lifecycle status—not a named-customer deployment. |
| `nvidia2025sipho` | NVIDIA official silicon-photonics technical post | Platform-family manufacturing roles—not an exact-SKU supplier-share allocation. |

## Publication blockers that must stay visible

1. No exact `SN6810`/`SN6800` or `BCM78919` customer-acceptance and unit record.
2. No repeat shipment or expansion at either product boundary.
3. No product-matched PIC/EIC/laser/FAU/OSAT/test content share.
4. No final-engine lot yield, rework, test seconds, qualification or service-cost waterfall.
5. No attributable ASP, product margin or CPO EPS/valuation bridge.
6. No matched retimed/LPO/NPO/CPO same-system TCO comparison.

## Pre-publication work sequence

1. Add and validate the five public bibliography entries above.
2. Edit only public-safe claims in the Quarto sources; do not copy private notes, PDFs or extracts.
3. Generate a claim-to-source manifest for each new paragraph and figure.
4. Render HTML and PDF locally; inspect desktop, mobile and print layouts.
5. Run private-path, restricted-material, broken-link and citation-resolution scans.
6. Present the rendered release candidate to Nur Alpys for approval. Only then is a commit/push/deployment decision in scope.

## Current recommendation

Build the report refresh as a **v1.1 release candidate**, not a “new bullish CPO call.” The current conclusion becomes clearer and more defensible: CPO is technically real and commercially plausible, but its public investment case is still gated by the commercial/economic chain.
