# Exact-SKU commercial-proof files

**Status:** Private release-control register; no shipment, revenue or investment conclusion  
**As of:** 13 August 2026  
**Purpose:** Maintain the smallest possible evidence record for each decisive
switch-CPO product. A field remains **Open** until a public record meets the
evidence standard in the final column. “Open” means searched and not cleared;
it does not mean no non-public activity exists.

## Evidence standard

```text
product identity → named customer → dated acceptance → accepted denominator
→ repeat event → product-linked supplier allocation → qualified-engine / service
→ attributable economics
```

An item from a different product, a platform family, a partner list, a sample,
an OEM catalogue, or a generic CPO programme cannot fill a field to its right.

## NVIDIA `SN6810` / `SN6810-LD`

| Required field | Current evidence-adjusted entry | Status | Minimum clearing record |
|---|---|---|---|
| Product configuration | 102.4T Spectrum-X Ethernet Photonics CPO; NVIDIA/Dell documentation maps `SN6810` to `SN6810-LD` ordering-family material. `CMP-054`, `CMP-057`, `CMP-081` | **Cleared** | — |
| Customer | NVIDIA lists Photonics adopters, but none is joined to this SKU. `PRI-033`, `CMP-073` | **Open** | Customer/OEM statement naming `SN6810` or `SN6810-LD` and CPO. |
| Acceptance date | No public acceptance/qualification record. | **Open** | Dated customer acceptance, qualification or procurement record. |
| Accepted units / ports | No public denominator. | **Open** | Accepted systems/ports/units plus period. |
| Repeat shipment | No second dated delivery or expansion. | **Open** | Repeat order, expansion, renewal or fleet follow-on for this SKU. |
| PIC/EIC/ELS/FAU/package/test allocation | NVIDIA gives platform process roles, including TSMC, SPIL, TFC and system integrators; no `SN6810` BOM/share is public. `CMP-053`, `CMP-083` | **Route only** | Supplier statement or BOM naming layer, `SN6810`, qualified role and share/scope. |
| Qualified-engine/service result | Screening, final fibre attachment and system validation are described; no lot yield, RMA, MTTR or warranty-cost result is public. `CMP-051`, `CMP-053`, `CMP-058` | **Process only** | Lot waterfall and/or fleet service record tied to this SKU. |
| Economics | No product price, supplier content, yield/rework, warranty or margin disclosure. | **Open** | Same-boundary price/share/yield/warranty/margin evidence. |

## NVIDIA `SN6800` / `SN6800-LD`

| Required field | Current evidence-adjusted entry | Status | Minimum clearing record |
|---|---|---|---|
| Product configuration | 409.6T quad-ASIC Spectrum-X Ethernet Photonics CPO; `SN6800-LD` is a CPO ordering-family configuration. `CMP-054`, `CMP-057`, `CMP-081` | **Cleared** | — |
| Customer | NVIDIA lists Spectrum-X Photonics adopters; no source maps one to `SN6800`/`SN6800-LD`. `PRI-033`, `CMP-073` | **Open** | Customer/OEM acceptance record naming this SKU and CPO. |
| Acceptance date | No public acceptance/qualification record. | **Open** | Dated customer acceptance, qualification or procurement record. |
| Accepted units / ports | No public system/port numerator. | **Open** | Accepted systems/ports/units plus period. |
| Repeat shipment | No public second dated delivery or expansion. | **Open** | Repeat order, expansion, renewal or fleet follow-on for this SKU. |
| PIC/EIC/ELS/FAU/package/test allocation | NVIDIA platform role map is relevant but not a `SN6800` allocation. `CMP-053`, `CMP-083` | **Route only** | Product-linked supplier scope, qualification and share. |
| Qualified-engine/service result | CPO manufacturing controls and Dell support policy are documented, not observed fleet outcome. `CMP-051`, `CMP-053`, `CMP-058` | **Process/policy only** | Lot yield/rework plus field RMA/MTTR/warranty record. |
| Economics | No product-linked economics disclosed. | **Open** | Same-boundary price/share/yield/warranty/margin evidence. |

## Broadcom `BCM78919` / TH6-Davisson

| Required field | Current evidence-adjusted entry | Status | Minimum clearing record |
|---|---|---|---|
| Product configuration | 102.4T, 16 × 6.4T engines, 200G/lane, field-replaceable ELSFP. `CMP-018`, `CMP-055` | **Cleared** | — |
| Customer | HPE, Celestica, Micas and Nexthop are collaborators/routes, not named accepting end customers. `CMP-018`, `CMP-074` | **Open** | Customer or integrator acceptance record naming `BCM78919`/TH6-Davisson CPO. |
| Acceptance date | Launch language says early-access sampling; catalogue is Limited Release. `CMP-018`, `CMP-062` | **Open** | Dated customer qualification/acceptance, not sampling. |
| Accepted units / ports | No public denominator. | **Open** | Accepted systems/ports/units plus period. |
| Repeat shipment | No public repeat shipment/expansion. | **Open** | Second delivery, expansion, renewal or sustained production evidence. |
| PIC/EIC/ELS/FAU/package/test allocation | Broadcom defines ASIC/engine/ELSFP architecture; Corning states TH6 connectivity collaboration. No complete allocation is public. `CMP-055`, `CMP-085` | **Partial route** | Exact product supplier scope, qualification and share for every layer. |
| Qualified-engine/service result | Prior TH5 qualification/reliability records are not transferable to TH6. `CMP-063`, `CMP-064`, `CMP-070` | **Open** | TH6 lot yield, qualification, RMA/MTTR and warranty record. |
| Economics | No product-linked price/content/yield/warranty/margin record. | **Open** | Same-boundary realised economics. |

## Mandatory negative controls

| Candidate record | Why it cannot clear a target-SKU gate |
|---|---|
| CoreWeave `SN6600-LD` | The hardware manual classifies it as a pluggable RHS-transceiver switch, not Spectrum-X Ethernet CPO. `CMP-021`, `CMP-046`–`CMP-048` |
| Lambda Q3450-LD | Quantum-X InfiniBand CPO, not Spectrum-X Ethernet. `CMP-040` |
| Tomahawk 6 family volume language | Family-level switch production cannot be attributed to `BCM78919` CPO. `CMP-075` |
| Celestica DS6000 | TH6 silicon with OSFP224 pluggable interfaces; no `BCM78919` CPO selection shown. `CMP-029`, `CLM-558` |

## Update protocol

Every potential positive must be captured in an [exact-SKU evidence packet](../09-primary-research/exact-sku-evidence-packet-template.md), then reconciled against the [customer-proof register](customer-proof-register.md), [supplier-attribution audit](supplier-attribution-audit-2026-08-12.md), and the two full commercial-proof dossiers. A product can advance only one field at a time unless a source genuinely joins several fields.
