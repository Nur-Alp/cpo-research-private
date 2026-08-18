# Quarterly gate-ownership audit — 12 August 2026

**Status:** Private operating control; no publication or forecast
**Purpose:** Verify that each unresolved research gate has an owner, a specific evidence route, a review cadence, a permitted state transition and a downgrade rule.

## Audit result

The quarterly register and acquisition queue cover the right decision fields,
but the ownership and stop-rule layer was implicit. This audit makes the next
action operational: every gate has one accountable workstream, one minimum
acceptable record, one review cadence and one condition that prevents an
unsupported upgrade.

## Gate ownership matrix

| Gate | Accountable workstream | Next evidence route | Review cadence | Permitted transition | Stop/downgrade rule |
|---|---|---|---|---|---|
| NVIDIA exact-SKU customer acceptance | Commercial proof / NVIDIA dossier | Customer or OEM record naming SN6800-LD/SN6810-LD, dated acceptance, systems/ports and repeat event | Every quarterly cut-off; event-driven on OEM release | Open → partial only with exact SKU and date; cleared only with repeatability | Keep open if record says Spectrum-X generally, SN6600-LD, platform benchmark or availability only |
| Broadcom exact-SKU customer acceptance | Commercial proof / Broadcom dossier | Customer/integrator record naming BCM78919/TH6-Davisson, qualification date, units/ports and repeat event | Every quarterly cut-off; event-driven on HPE/Celestica/Micas/Nexthop release | Open → partial with exact configuration and date; cleared only with repeatability | Keep open for Tomahawk 6 family, sampling, Limited Release or demo language |
| Supplier content attribution | Supplier map / company cards | Product-linked BOM, qualification or supplier statement naming who does what for the exact product | Quarterly; immediately after exact-SKU acceptance | Route-level → exact-SKU role; economics remain open | Do not promote ecosystem, partnership, capacity or MOU language to allocation |
| Final-engine yield and rework | Manufacturing / engine economics | Lot waterfall: die → attach → package → test → accepted, with denominator and rework | Quarterly; event-driven on production/test disclosures | Open → partial process evidence; production only with accepted-lot denominator | Do not infer final yield from interface yield, engineering samples or equipment availability |
| Field service and warranty | Serviceability / OEM evidence | Failure population, MTTR, replacement scope, spares and warranty tied to exact SKU | Quarterly; event-driven on field case/qualification release | Open → partial with population and boundary; cleared with repeated field evidence | ELSFP replaceability alone does not clear engine/package serviceability |
| Product ASP and supplier margin | Economic model / analyst layer | Product-linked price, share, price-down and gross-margin record | Quarterly; event-driven on filing or contract disclosure | Blocked → scenario-only unless product-linked record clears | Never use consolidated company margin or SAM as product margin |
| Matched CPO/LPO/NPO/retimed comparison | Architecture / TCO | Same ASIC, ports, lane rate, reach, BER/FEC, cooling, qualification and service | Quarterly; event-driven on measured system report | Partial → matched evidence only when all boundary fields are present | A component pJ/bit, model or different lane generation cannot clear the gate |
| PIC route maturity | PIC/engine diligence | Device → subassembly → process → qualified engine → commercial attribution ladder | Quarterly; event-driven on full-paper or product release | Advance only one evidence rung at a time | Do not assign company leadership from device bandwidth or loss alone |
| Analyst baseline reconciliation | Restricted estimates | Fiscal year, currency, accounting basis, shares, revenue, margin, capex and valuation convention | Every quarterly model refresh | Pending → reconciled baseline; CPO overlay remains blocked until commercial input exists | Stale or incomplete estimates remain archived and excluded from current range |

## Review packet requirements

Every quarterly cut-off must retain:

1. as-of date and reviewer;
2. exact searches and official/OEM/customer domains checked;
3. new sources, inaccessible routes and negative controls;
4. state-before/state-after for each gate;
5. source and claim IDs for any transition;
6. what remains unproven;
7. changed, withdrawn and unchanged conclusions; and
8. validator output and confirmation that nothing was published, committed or pushed without explicit authorization.

## Current ownership status

As of 12 August 2026, all gates remain open or partial as documented in the
[quarterly evidence-change register](quarterly-evidence-change-register-2026-08-12.md)
and [evidence-gate register](../08-model/evidence-gate-register.md). No gate
has an evidence bundle sufficient for a company-specific CPO revenue, EPS,
margin or profit-pool conclusion.

## Operational stop rule

If a new source cannot satisfy the same product/domain boundary and denominator,
record it as a retrieval result or negative control and do not alter the
thesis. Repeated product pages, unchanged roadmaps, inaccessible pages and
secondary summaries are not progress toward a cleared gate.

Related controls: [quarterly change register](quarterly-evidence-change-register-2026-08-12.md), [critical-path milestone tracker](../08-model/critical-path-milestone-tracker.md), [decision-changing evidence queue](decision-changing-evidence-acquisition-queue.md), and [public release manifest](../00-scope/public-release-manifest-2026-08-12.md).
