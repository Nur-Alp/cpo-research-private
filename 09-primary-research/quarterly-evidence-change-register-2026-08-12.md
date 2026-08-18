# Quarterly evidence-change register

**Status:** Private operating template; no publication, commit or push
**As of:** 2026-08-12
**Purpose:** Record only evidence that changes a CPO decision gate, while preserving negative results and unchanged conclusions.

## State-transition rules

An update may move a gate only when the new record matches the same company,
product/domain, date and denominator. The permitted transitions are:

```text
open → partial evidence → cleared
```

`partial evidence` is not a production or profit pass. A vendor roadmap,
platform benchmark, partner demonstration, inaccessible page, unchanged product
listing or repeated secondary article records a retrieval status, not a gate
transition.

## Required row format

| Field | Required content |
|---|---|
| Review ID | Quarter and as-of date, e.g. `QR-2026-Q3-001` |
| Gate / milestone | Exact gate affected: SKU, customer, units, repeat, supplier, yield, service, economics or alternative comparison |
| Company / architecture | NVIDIA, Broadcom, Coherent, Lumentum, Marvell, TSMC or alternative route |
| Product/domain boundary | Exact SKU, engine, lane rate, topology and service boundary |
| State before | Open, partial or cleared |
| New observation | What the source actually says, with numerator and denominator if available |
| State after | Permitted transition only; otherwise unchanged |
| Source / claim IDs | Retained source and claim references, canonical URL if needed |
| Evidence class | Fact, external expectation, process signal, customer proof, production proof or negative control |
| What remains unproven | Missing fields and boundary limitations |
| Decision impact | Timing, supplier map, economics, alternative comparison or no change |
| Reviewer / date | Reviewer and retrieval date |

## Required source locations by gate

Search the locations below before expanding the source set. A secondary source
may identify a lead, but a gate moves only on the primary customer, OEM,
supplier, filing, standard or measured technical record specified here.

| Gate | First source locations | Minimum source content | If not found |
|---|---|---|---|
| Exact SKU/customer/units/repeat | Customer/operator engineering blogs; OEM case studies; procurement/qualification announcements; platform-owner releases | Exact SKU, customer, date and numerator; a second event for repeatability | Record search disposition; retain gate as open |
| Supplier content/share | Product BOMs; supplier product releases; qualified-vendor records; OSAT/process announcements tied to SKU | Named layer and product relationship, preferably allocation/share | Keep route level only; no revenue attribution |
| Yield/rework/test | Manufacturing conference papers; supplier process presentations; test-equipment customer case studies; qualification disclosures | Starts-to-accepted denominator, test/rework flow and sample boundary | Preserve as mechanism/capability, not yield |
| Service/warranty | OEM manuals; customer operations records; RMA/field-reliability or qualification reports | Population, time period, failure/replacement scope and warranty/MTTR boundary | Treat replaceable laser or policy as partial only |
| ASP/margin/capex | Company filings; earnings releases; disclosed contracts; lawful restricted analyst input | Product allocation, price/content, margin and capital boundary | Do not use consolidated margin or market forecast |
| CPO alternatives | Same-ASIC system papers; customer qualification reports; standards test events | Lane rate, reach, BER/FEC, power/cooling, service and total-cost boundary | Maintain coexistence framework |

## Required decision-impact order

Before a review adds a source, test it against the
[missing-input value-of-information register](../08-model/missing-input-value-of-information.md).
Prioritise exact SKU/customer numerator, repeatability, supplier allocation,
accepted-engine yield/rework, service/warranty, price and margin—in that order.
Do not add generic CPO coverage merely to increase source count.

## Current quarter register

| Review ID | Gate / boundary | State before | New observation | State after | Decision impact |
|---|---|---|---|---|---|
| QR-2026-Q3-001 | NVIDIA exact Ethernet CPO customer proof: `SN6810-LD`/`SN6800-LD` | Open | CoreWeave identifies deployed `SN6600-LD` and separately describes Photonics CPO adoption; the source does not connect the two or identify the target CPO SKU (`CMP-079`, `CLM-548`) | **Unchanged: open** | Negative control; platform/SKU conflation explicitly rejected |
| QR-2026-Q3-002 | NVIDIA product boundary | Partial | Current NVIDIA product materials identify `SN6810-LD` and `SN6800-LD` as MMC-12 CPO systems and state production/availability language | **Unchanged: partial** | Product boundary confirmed; no customer numerator |
| QR-2026-Q3-003 | Broadcom exact TH6 customer proof: `BCM78919` | Open | Current Broadcom catalogue/release retains Limited Release and early-access sampling language without customer units or repeat event | **Unchanged: open** | Lifecycle context only; no commercial upgrade |
| QR-2026-Q3-004 | Supplier economics | Open | Layer reconciliation confirms all PIC/engine, laser, package/attach and test dollar ranges remain labelled assumptions; no product-linked ASP/share/yield/margin record added | **Unchanged: open** | No profit-pool leader; no company CPO sensitivity |
| QR-2026-Q3-005 | Manufacturing proof | Open | Research vehicles, supplier capabilities and product/process claims were consolidated; no exact-SKU production lot with starts-to-accepted denominator was found | **Unchanged: open** | Yield, warranty and cost remain blocked |
| QR-2026-Q3-006 | Architecture substitution | Partial / coexistence | Common-boundary matrix now defines falsification conditions for retimed pluggables, LPO/RTLR, NPO/OBO and CPO; no matched 200G/400G system comparison cleared | **Unchanged: partial** | CPO remains conditional, not universal winner |
| QR-2026-Q3-007 | Lumentum CPO/ELS order conversion and economic attribution | Open | Direct 13 August review of the latest retained Q3 FY2026 10-Q found no CPO, ELSFP, external-laser-source or optical-engine order-conversion disclosure. Consolidated financials therefore remain non-allocable (`FIL-003`, `CLM-559`). | **Unchanged: open** | No conversion from disclosed order signal to revenue, margin, capacity or profit-pool input |

## Sign-off checklist

- [x] As-of date recorded.
- [x] Exact SKU/domain boundaries checked before any state change.
- [x] Negative retrievals retained where they prevent false positives.
- [x] Facts separated from expectations, assumptions and variant conclusions.
- [x] No stale or inaccessible source treated as a milestone outcome.
- [x] Commercial, manufacturing, supplier and alternative gates reconciled.
- [x] Validators run after the refresh.
- [x] Public release, commit and push remain disabled unless explicitly requested.

## Next review requests

1. Exact NVIDIA or Broadcom customer/OEM acceptance record with SKU, date,
   units/ports and repeat shipment.
2. Product-matched BOM and supplier qualification/share record.
3. Final-engine lot yield, attach/test cycle time, rework, field service and
   warranty data.
4. Same-ASIC/port-count 200G or 400G comparison against LPO/RTLR/NPO.

Related controls: [critical-path milestone tracker](../08-model/critical-path-milestone-tracker.md), [decision-changing evidence queue](decision-changing-evidence-acquisition-queue.md), [estimates-to-variant reconciliation](../08-model/analyst-variant/estimates-to-variant-reconciliation-2026-08-12.md), and [commercial-proof retrieval addendum](commercial-proof-retrieval-addendum-2026-08-12.md).

The [quarterly gate-ownership audit](quarterly-gate-ownership-audit-2026-08-12.md)
adds accountable workstreams, review cadence and stop rules for every open or
partial gate.
