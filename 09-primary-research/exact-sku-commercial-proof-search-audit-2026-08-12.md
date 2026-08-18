# Exact-SKU commercial-proof search audit — 12 August 2026

**Status:** Private research log; no publication or release clearance  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6800-LD`/`SN6810-LD` and Broadcom `BCM78919` / TH6-Davisson  
**Search objective:** Find a named customer, accepted-unit/port denominator, repeat shipment, or product-matched supplier/economic record.

## Search routes checked

| Route | Result | Interpretation |
|---|---|---|
| NVIDIA Ethernet product/manual pages | Exact `SN6800-LD` and `SN6810-LD` CPO product definitions and port tables found | Product boundary and availability; no customer acceptance or installed-base denominator |
| NVIDIA silicon-photonics page | CoreWeave, Lambda, Meta, Microsoft and OCI named as first Spectrum-X Photonics adopters; second-half-2026 availability stated | Named-adopter/platform signal; no adopter-to-SKU mapping, accepted units or repeat shipment |
| NVIDIA technical blog | `SN6810` and `SN6800` CPO architecture and 2026 commercial-availability framing | Architecture/product route; no accepted customer numerator |
| Broadcom TH6 release/product catalogue | Exact `BCM78919`, 102.4T, 16 × 6.4T engines, 200G/link; “sampling” and **Limited Release** | Exact product and lifecycle state; no named customer, units, repeat shipment or economics |
| Broadcom OCP/partner materials | Micas, Celestica, Alpha and DNI demonstrations/partner routes | Demonstration and ecosystem evidence; not purchase or acceptance evidence |
| Celestica results and filings | Unnamed hyperscaler CPO-switch award with expected 2027 ramp | Integrator timing lead; no exact Broadcom SKU, named customer or units |
| OEM/operator searches | CoreWeave `SN6600-LD` record is pluggable/ambiguous; Lambda Spectrum-X statement is planning/adoption language; exact Lambda CPO record is Quantum-X Q3450-LD | Negative controls prevent false conversion of platform or adjacent InfiniBand evidence into Spectrum-X Ethernet CPO volume |

## Follow-up search and corroboration

The follow-up exact-label search also returned the following, none of which
clears a commercial gate:

- Broadcom's live `BCM78919` product page repeats the 102.4Tb/s, 512 × 200G
  architecture and still shows **Limited Release** with no distributor
  inventory. This corroborates lifecycle status only.
- NVIDIA's current Spectrum-6 hardware documentation repeats `SN6810-LD` and
  `SN6800-LD` as CPO ordering-family labels and reports their port
  configurations. This corroborates the product boundary only.
- Supermicro's official Vera Rubin release independently lists `SN6800` and
  `SN6810` as CPO, and `SN6600` as pluggable. It strengthens the
  CPO-versus-pluggable false-positive control but discloses no customer,
  acceptance, scale or economics (`CMP-081` / `CLM-550`).
- Third-party technical and reseller pages repeat Broadcom/NVIDIA product
  specifications. They do not identify a customer, purchase order, accepted
  units, installed ports, repeat shipment, field population, or supplier
  economics, and are therefore excluded from the evidence numerator.
- Broadcom's public release continues to use both “now shipping” language and
  early-access sampling language. Without a named customer record, the
  conservative state remains **early-access/product shipping signal**, not
  verified volume deployment.

No newly returned result tied `SN6800-LD`, `SN6810-LD`, or `BCM78919` to a
named operator's accepted system and a repeat delivery. Search results that
merely repeat a vendor specification are not treated as independent shipment
corroboration.

## Exact-SKU gate result

| Required gate | NVIDIA | Broadcom |
|---|---:|---:|
| Exact CPO SKU | **Pass** — `SN6800-LD`/`SN6810-LD` | **Pass** — `BCM78919`/TH6-Davisson |
| Named customer tied to exact SKU | **Open** | **Open** |
| Dated acceptance/qualification | **Open** | **Open** |
| Accepted units/ports/systems | **Open** | **Open** |
| Repeat shipment or expansion | **Open** | **Open** |
| Product-matched supplier allocation | **Open** | **Open** |
| Yield, ASP, warranty or margin | **Open** | **Open** |

## False-positive controls retained

- CoreWeave's `SN6600-LD` is retained as a pluggable/ambiguous negative control;
  it is not joined to NVIDIA's separate Photonics CPO-adopter statement.
- Lambda's exact `Q3450-LD` installation is Quantum-X InfiniBand, not
  Spectrum-X Ethernet; it informs operating-readiness questions only.
- Broadcom's Tomahawk 6 family production-volume statement is not assigned to
  the `BCM78919` CPO configuration.
- Broadcom OCP demos and Celestica's unnamed hyperscaler award remain routes,
  not accepted customer shipments.

## Decision impact

The search strengthens the product-definition and ecosystem/timing evidence but
does not change either commercial-proof dossier's decision. The 2026–2027
window remains a verification window, not a demonstrated volume-adoption call.
No company can be promoted to proven CPO profit-pool leader. The next decisive
record is an operator/OEM/customer disclosure tying an exact SKU to dated
accepted systems and a repeat event; the next economic record is a
product-matched supplier share or qualified-good-engine cost/yield boundary.

## Linked evidence

- [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md)
- [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md)
- [OEM/operator exact-SKU search audit](oem-operator-exact-sku-search-audit-2026-08-12.md)
- [Supplier-map completeness audit](../08-model/supplier-map-completeness-audit-2026-08-12.md)
- [Commercial-proof decision memo](../07-companies/commercial-proof-dossiers/commercial-proof-decision-memo.md)

**Outcome:** no new exact-SKU customer, scale, repeat-shipment, supplier-share,
or economics evidence found in this search cycle. Release remains gated.

The next-day refresh is recorded in [exact-SKU commercial-proof refresh — 13
August 2026](exact-sku-commercial-proof-refresh-2026-08-13.md).
