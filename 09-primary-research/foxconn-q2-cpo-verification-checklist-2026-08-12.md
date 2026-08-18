# Foxconn FY26 Q2 CPO verification checklist — 12 August 2026

**Status:** Private pre-release diligence control. Do not publish, commit or push from this document.  
**Event:** Foxconn FY26 Q2 investor conference, scheduled for 12 August 2026.  
**Decision use:** Test—not assume—the May 2026 outlook that CPO optical-switch mass-production shipments would begin in Q3 and might reach tens of thousands of units in FY26 (`CMP-060`; `CLM-526`–`CLM-527`).

## The question

Did Foxconn disclose an *observed* CPO switch shipment or a materially more specific customer/product/manufacturing record? If so, can it be tied to NVIDIA `SN6810`/`SN6800` (or Dell `SN6810-LD`/`SN6800-LD`), Broadcom `BCM78919`/TH6-Davisson, or neither?

The default state is unchanged unless a new primary source provides the missing fields. A Q2 financial result that discusses cloud/networking growth, AI servers, optical capability or CPO investment without product/customer/denominator evidence is not commercial proof.

## Retrieval and retention procedure

1. Retain the official Q2 results release, investor deck and call transcript, preferably as publisher PDFs. If a publisher page is the only record, retain the original page plus a readable Markdown evidence note with the canonical URL, publication date and access date.
2. Search the full retained material for: `CPO`, `co-packaged`, `optical switch`, `1.6T`, `Spectrum`, `SN6810`, `SN6800`, `Tomahawk`, `Davisson`, `BCM78919`, `customer`, `mass production`, `shipment`, `unit`, `thousand`, `yield`, `laser`, `ELSFP`, `COUPE`, `MMC`, `fibre/fiber`, `warranty`, `repair` and `qualification`.
3. Preserve the complete surrounding answer for any hit: speaker, question, date, whether it is historical/observed versus future/planned, unit and time period.
4. Add a source-log row and claim-ledger item only if the material changes a decision gate. Do not create a claim for generic corporate performance.
5. Re-run `python3 scripts/validate-private-research.py` before any downstream interpretation.

## Required fields and evidence classes

| Field | Evidence that qualifies | Evidence that does **not** qualify |
|---|---|---|
| Product | Exact SKU or unambiguous maker/configuration boundary: `SN6810`/`SN6800`, `SN6810-LD`/`SN6800-LD`, or `BCM78919`/TH6-Davisson | “CPO,” “optical switch,” “Spectrum-X,” “Tomahawk,” “1.6T,” or an exhibition reference alone |
| Customer | Named operator/OEM/customer and a direct statement that it accepted/deployed the named CPO product | “Major cloud/AI customers,” partner list, demonstration or source qualification |
| Scale | Observed delivered units, ports, systems, capacity or contract value with period/date | Addressable market, future target, design capacity, production-line capacity or a non-CPO consolidated revenue number |
| Repeatability | Second dated shipment, expansion, reorder, acceptance stage or sustained production record | A one-time sample, launch, validation, roadmap, orderable SKU or a vendor phrase such as “shipping” without a denominator |
| Supplier role | Exact product-linked role for a named layer: ASIC/SerDes, PIC/engine, EIC, laser, fibre attach, package, connector or test | Ecosystem membership, MOU, general manufacturing capability or a role from a different CPO system |
| Economics | Attributable content/ASP/share plus product-margin, yield/rework, warranty and service boundary | Consolidated gross margin, segment growth, capex or a supplier’s technology role |

## Decision matrix

| Possible Q2 disclosure | Correct update | What remains unproven |
|---|---|---|
| Repeats the Q3/tens-of-thousands outlook | Keep `MS-019` as a **planned management outlook**; add no shipment claim | Actual shipment, SKU, customer, units and economics |
| Reports generic CPO shipment but no product/customer/denominator | Record an observed generic manufacturing milestone; do **not** allocate to NVIDIA or Broadcom | Product attribution, customer acceptance, scale/repeatability and profit capture |
| Names CPO product maker or SKU but no customer/units | Upgrade the product/manufacturer linkage only | Customer, accepted scale, repeatability and economics |
| Names customer plus exact CPO SKU but no units | Advance customer-deployment evidence; leave commercial scale gate open | Units/ports, repeat delivery, service and economics |
| Names SKU/customer and observed units or ports | Advance the commercial-proof numerator for that *specific* system only | Repeat shipment, supplier allocation, yield/service and profit capture |
| Names repeat shipment or expansion for the same SKU/customer | Advance repeatability for that system; still keep economics separately gated | Supplier content, share, ASP, product margin, yield/rework and warranty |
| Discloses supplier role without price/share/yield/margin | Update supplier-content map with the precise layer and status | Any profit-pool conclusion |
| Discloses attributable CPO content/share plus margin/yield/service terms | Evaluate the relevant private scenario gate; do not use consolidated margin as CPO margin | Independent corroboration and sustainability of terms |

## Anti-contamination controls

- Foxconn has a general system-integration relationship in NVIDIA’s manufacturing narrative. That does not attach a generic Foxconn CPO statement to Spectrum-X (`CMP-053`; `CLM-435`–`CLM-437`).
- Foxconn’s CPO activity does not attach to Broadcom TH6-Davisson without `BCM78919`/TH6 or an equivalent unambiguous product link.
- Keep NVIDIA’s `SN6600-LD` outside the CPO numerator: it is a pluggable RHS system, unlike `SN6810-LD` and `SN6800-LD` (`CMP-048`; `CLM-380`–`CLM-383`).
- Do not infer the number of CPO switches from a statement about AI servers, networking revenue, rack capacity, optical modules or 1.6T switching.
- Do not convert management guidance, factory capacity or a “tens of thousands” target into accepted units.

## Downstream documents to reconcile only if a gate moves

1. `01-sources/source-log.csv` and `01-sources/claim-ledger.csv`.
2. `07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md` and/or `broadcom-th6-davisson.md`.
3. `08-model/customer-proof-register.md`, `critical-path-milestone-tracker.md`, `evidence-gate-register.md` and `falsification-dashboard.md`.
4. `07-companies/six-company-content-attribution-register.md` and `08-model/switch-cpo-sku-content-reconciliation.md` only for exact layer attribution.
5. `08-model/optical-engine-profit-pool-input-gates.md` only if a disclosure changes an actual required economic input.

## Current baseline, before the event

- **NVIDIA:** exact Spectrum-X CPO products are identified, but no public customer record joins a named CPO SKU to accepted units/ports and repeat shipment.
- **Broadcom:** BCM78919/TH6-Davisson is exact CPO product evidence; the latest retained lifecycle record is Limited Release and the announcement says early-access sampling. No customer, units or repeat shipment is public.
- **Foxconn:** Q3 CPO-switch mass-production and tens-of-thousands FY26 units are management outlooks only; they are product/customer unallocated and cannot enter either platform’s commercial numerator.
- **Profit pool:** no disclosed CPO supplier share, ASP, qualified yield/rework, warranty or product gross margin supports a CPO profit-pool leader conclusion.

## Retrieval check — 12 August 2026

At the review time on 12 August, Foxconn's official [investor-conference index](https://www.honhai.com/en-us/investor-relations/investor-relations-activities/investor-conference) listed the FY26 Q2 conference for that date, but the entry contained no downloadable results deck or transcript. A subsequent check of the official [dedicated event page](https://www.honhai.com/en-us/investor-relations/investor-relations-activities/investor-conference/107) likewise found no attached files. A second official-search check after the scheduled event continued to return the event listing rather than Q2 materials. This is a retrieval observation, not evidence that results have not been released elsewhere or will not be posted later. No CPO claim, source-log entry or commercial gate has changed; repeat retrieval only after official materials are attached.

**Current retrieval state:** event page live; results deck absent; transcript absent; CPO evidence not reviewed. Do not mark this event complete in the quarterly review.

## Retrieval update — 12 August 2026 (third check)

The official quarterly-earnings and financial-reports routes were checked again after the scheduled event. Both returned a bot-challenge response rather than readable FY26 Q2 results, a deck or a transcript. This is an **access limitation**, not evidence that Foxconn did not release results, and it cannot support a CPO claim or a gate downgrade. Recheck through a normal authenticated browser session or when an official downloadable PDF/transcript appears.
