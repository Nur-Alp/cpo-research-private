# Coherent versus Lumentum: matched optical-engine and profit bridge

**Status:** Evidence-gated comparison; no forecast values populated  
**Owner:** Nur Alpys  
**Scope:** 200G/lane scale-out optical engines and directly supplied external-light-source layers  
**As of:** 2026-08-07

## Decision question

Which supplier can retain the larger sustainable profit pool after the optical product is reduced to a common boundary, qualified, manufactured, serviced and sold to a platform owner?

The current evidence does **not** support a direct Coherent-versus-Lumentum engine ranking. Coherent publicly demonstrates a broader set of CPO engine architectures; Lumentum publicly specifies an external laser source and has a clearer disclosed order/capacity signal. A complete Coherent engine and a Lumentum ELSFP are different economic units.

## Common boundary before comparison

The first comparable unit should be a bidirectional 6.4-Tb/s optical engine (32 × 200G), or a clearly defined fraction of that engine, with the following included or explicitly excluded:

| Boundary item | Coherent socketed CPO demonstration | Lumentum ELSFP / laser layer | Comparable status |
|---|---|---|---|
| SiPh PIC / modulator | Company says 6.4T socketed SiPh CPO; internal PIC BOM not disclosed [CMP-015] | Not supplied in the ELSFP product boundary [CMP-016] | Not comparable |
| Driver / TIA / control | Not disclosed | Not disclosed | Open |
| Laser source | Coherent says its ELS module uses its high-power InP CW lasers [CMP-015] | UHP InP laser in a centralized serviceable ELSFP; up to 350 mW at 50°C and 235 mW at 70°C, >20% PCE [CMP-016] | Partially comparable |
| Fibre distribution / splitters | Not disclosed | Multiple engines can share one ELSFP, but splitter/fibre loss and channel allocation are not disclosed [CMP-016; CLM-071] | Open |
| Fibre attach / connector | Socketed demonstration; method and yield not disclosed [CMP-015] | ELSFP product does not include the CPO engine attach boundary [CMP-016] | Not comparable |
| Package / thermal path | Socketed CPO claimed; package thermal data not disclosed [CMP-015] | Laser/module package only; engine thermal path excluded [CMP-016] | Not comparable |
| Final test / qualification | No final-engine lot or customer qualification disclosed | No ELSFP lifetime distribution or customer qualification disclosed | Open |
| Service / warranty | Socketed engine replacement procedure and warranty split unknown | Laser source is positioned as serviceable; engine, fibre and PIC failure remain outside the ELSFP boundary [CLM-071] | Partially comparable |
| Commercial unit | 6.4T CPO demonstration, not a priced production engine | ELSFP product and multi-hundred-million-dollar CPO order, but product allocation unknown [CMP-010] | Not comparable |

**Rule:** Do not divide Lumentum's disclosed order by 32 lanes or assign it to Coherent's 6.4T engine. The order may include lasers, modules, ELSFPs, other optics, or multiple product generations.

## Evidence-matched supplier read

| Dimension | Coherent | Lumentum | Current interpretation |
|---|---|---|---|
| Technical breadth | SiPh CPO, ELS/high-power InP, VCSEL CPO, InP-on-silicon 400G modulation and packaging demonstrations [CMP-015; PRS-003] | UHP/SHP lasers, ELSFP, 200G EMLs, DWDM external-light demonstrations [CMP-016; CMP-017] | Coherent has broader disclosed engine options; Lumentum has a sharper light-source boundary |
| Customer route | Executed $2B NVIDIA private placement plus access to five additional Coherent product families related to CPO; multibillion purchase/capacity commitment remains product-unallocated [PRI-026; CLM-197] | Executed $2B NVIDIA private placement plus multibillion purchase/capacity rights for advanced laser components [PRI-027; CLM-198] | Both now have executed primary NVIDIA route evidence; neither filing allocates product quantities or volume |
| Manufacturing signal | Six-inch InP volume-production claim and expansion; CPO allocation and qualified yield missing [PRS-003] | Greensboro 6-inch InP facility planned to ramp mid-2028; hundreds of millions of dollars planned; qualified output missing [PRI-025; CLM-196] | Coherent has earlier disclosed capacity; Lumentum has a dated future fab milestone |
| Commercial signal | Very-high-volume multi-year CPO order claim plus a $15B+ CPO SAM-by-2030 estimate and H2 2026 CPO/NPO new-revenue label; customer, product and terms undisclosed [PRS-003; CLM-250; CLM-251] | Multi-hundred-million-dollar CPO order for first-half 2027 delivery; product and customer undisclosed [CMP-010; CLM-083] | Lumentum has the clearer disclosed order magnitude/timing; Coherent has a broader market/roadmap framing; neither has product-level conversion |
| Potential content capture | Could span PIC, laser, package, fibre attach and test if Coherent supplies the complete engine | Most clearly captures laser/ELSFP content; complete-engine share is not shown | Coherent has higher potential content but more unproven process boundaries |
| Main economic risk | Broad stack may require more capex, yield closure and warranty ownership | Customer or platform owner may retain engine/package value while Lumentum remains a component supplier | Do not infer margin leadership from breadth or order size |

## Yield waterfall: what is actually known

For either supplier, good shipped engines require:

```text
Y_total = Y_die × Y_attach × Y_package × Y_test × Y_accept
N_good = N_starts × Y_total + recovered_rework_units
```

| Yield input | Coherent | Lumentum | Evidence status |
|---|---|---|---|
| PIC / laser good-die yield | No CPO-specific lot data | No CPO-specific lot data | Open for both |
| Fibre-attach first-pass yield | No final-engine data | No engine attach boundary in ELSFP disclosure | Open for both |
| Package assembly yield | No final-engine distribution | No complete-engine package data | Open for both |
| Optical/electrical test yield | No customer-qualified distribution | No customer-qualified ELSFP distribution | Open for both |
| Customer acceptance yield | No named CPO production customer | NVIDIA customer route claimed, acceptance not disclosed | Open for both |
| Rework recovery and scrap | Not disclosed | Not disclosed | Open for both |

The academic packet provides process mechanisms and measurement methods, but no supplier-specific final-engine yield. PAP-015's 1,178-observation fibre-attach experiment is not a Coherent or Lumentum production lot and cannot be inserted into either waterfall.

## Profit bridge

For a common engine boundary:

```text
Revenue_supplier
= systems × adoption × engines_per_system × supplier_content_per_engine × qualified_share

Gross_profit_supplier
= Revenue_supplier × realised_product_margin
  − yield_and_rework_cost
  − warranty_and_support_cost
  − cannibalised_legacy_gross_profit

Cash_return_supplier
= Gross_profit_supplier − incremental_R&D − qualification_cost − attributable_capacity_capex
```

The current evidence status is:

| Input | Coherent | Lumentum | Why it remains blank |
|---|---|---|---|
| Systems and adoption | Blocked | Blocked | No customer-confirmed CPO production denominator |
| Engines per system | Partial only for Broadcom architecture, not supplier attribution [CLM-076] | Blocked | Lumentum ELSFP sharing topology is not a complete-engine count |
| Supplier content / ASP | Blocked | Blocked | Neither agreement discloses product pricing or content |
| Qualified supplier share | Blocked | Blocked | Nonexclusive agreements and second-source status are not enough |
| Realised product margin | Blocked | Blocked | Consolidated gross margins are not product margins [CLM-070; CLM-073] |
| Yield/rework/warranty | Blocked | Blocked | No lot, field-return or repair data |
| Incremental capex | Partial company-level signal | Partial company-level signal: Lumentum reported $284.5M of consolidated nine-month capex versus $177.1M prior year, but did not allocate it to CPO [CLM-219] | Executed NVIDIA investments, total-company capex and Lumentum's fab plan are not CPO-attributable capacity or margin [CLM-194–CLM-198; CLM-219] |

## What would change the ranking

1. A customer or platform-owner record identifies a Coherent or Lumentum CPO SKU, unit count and repeat production.
2. A supplier or customer qualification record maps PIC, laser, ELSFP, fibre attach, package, driver/TIA and test ownership.
3. A lot-level yield waterfall reports die yield, attach yield, package yield, test escape, rework and qualified acceptance.
4. A contract or product disclosure supplies ASP, price-down schedule, second-source status, warranty allocation and realised margin.
5. Facility disclosures connect capex and qualified capacity to the relevant product family rather than to general AI optics.

The latest Lumentum filing adds a useful negative constraint: consolidated capex rose to $284.5M for the nine months ended March 28, 2026 from $177.1M in the prior-year period, but the filing does not identify what portion supports CPO, lasers, Greensboro or other products [CLM-219]. This is evidence that capital intensity must remain in the diligence queue; it is not an allowable CPO free-cash-flow input.

Until those records exist, the evidence-adjusted conclusion remains:

### Financial evidence added in the current batch

Coherent's Q3 FY2026 revenue and gross margin establish a $1.806B / 37.7% GAAP company denominator, while Lumentum's Q3 filing establishes $808.4M revenue and 44.2% GAAP gross margin. Lumentum's utilization/mix disclosures, component-versus-system increase, cloud-transceiver growth, optical-circuit-switch shipments, customer concentration and $284.5M nine-month capex sharpen the operating context. None is allocated to a CPO engine, so consolidated margins and capex remain blocked inputs rather than model values.[CLM-335][CLM-336][CLM-337][CLM-338][CLM-339][CLM-340]

> Coherent is the broader potential complete-engine content owner; Lumentum is the clearer external-laser/ELSFP and near-term commercial-conversion candidate. Neither is yet proven to capture the largest sustainable CPO profit pool.

## Linked controls

- [Optical-engine yield waterfall template](engine-yield-waterfall-template.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Coherent and Lumentum supplier dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md)
- [Packaging, fibre-attach and serviceability benchmark](../03-components/packaging-reliability-benchmark.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
