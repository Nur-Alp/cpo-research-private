# Exact-SKU supplier-attribution completeness — 12 August 2026

**Status:** Private control matrix; not a BOM, revenue estimate or supplier ranking
**Scope:** NVIDIA Spectrum-X `SN6810-LD`/`SN6800-LD` and Broadcom `BCM78919`/TH6-Davisson

## Status definitions

- **Exact product owner:** the platform/ASIC owner is named for the product.
- **Product-linked route:** a process, collaboration or validation role is
  tied to the product, but sellable content or supplier share is not disclosed.
- **Family/route only:** the role exists at a broader platform or technology
  level and cannot be assigned to the exact SKU.
- **Open:** no product-matched attribution is retained.

None of these statuses unlocks ASP, share, yield, warranty or margin.

## Layer completeness

| Physical layer | NVIDIA exact-SKU state | Broadcom exact-SKU state | Promotion evidence required |
|---|---|---|---|
| ASIC / SerDes | **Exact product owner** — Spectrum-6 / SN6800-LD/SN6810-LD | **Exact product owner** — BCM78919 / Condor SerDes | Product-linked transfer price and platform margin |
| PIC / optical engine | **Product-linked route** — TSMC SiPh/COUPE process; complete engine supplier open | **Product-linked route** — TSMC COUPE engine technology; supplier scope open | Exact BOM or qualification record naming PIC/engine supplier and share |
| EIC / driver / TIA | **Open** | **Open** | Supplier, die/package boundary and product qualification |
| Laser / ELS | **Product-linked route** — TFC packaging/validation; broader Lumentum ecosystem role | **Product-defined interface** — replaceable ELSFP; supplier open | Exact laser/ELS supplier, count, qualification, price and warranty boundary |
| Fibre attach | **Product-linked process** — late-stage attach/screening; owner and yield open | **Product-linked collaboration** — Corning faceplate-to-chip route; attach economics open | Process owner, attempts, first-pass yield, rework and cost |
| Connector / faceplate | **Family/route only** — SENKO detachable connector role | **Product-linked collaboration** — Corning TH6 connectivity | Exact supplied assembly, mating life, service liability and share |
| Package / assembly | **Product-linked route** — SPIL package/assembly/test; Foxconn system assembly | **Open** | OSAT/package owner, scope, yield, capex and margin |
| Test / qualification | **Product-linked process** — validation before shipment; coverage and acceptance distribution open | **Open** | Test owner, seconds, coverage, escapes, lot acceptance and warranty |
| Customer / units / repeat | **Open** — adopters/platform records not exact target-SKU acceptance | **Open** — early access/partner records not accepted customer volume | Named customer, exact SKU, date, units/ports and repeat event |
| Supplier economics | **Open** | **Open** | ASP, qualified share, price-down, product margin, yield, warranty and capex |

## Decision readout

NVIDIA has the more detailed disclosed manufacturing-route map. Broadcom has
the clearer merchant-switch product boundary and a TH6-specific connectivity
collaboration. Neither reaches a product-matched supplier bill of materials,
customer denominator or realised economics. The only unambiguous exact-SKU
ownership currently established is the platform/ASIC layer.

## Promotion rule

Do not promote a route to exact-SKU supplier attribution unless one retained
record names the exact product, physical responsibility, qualification or
shipment status, and at least one product-matched economic or output boundary.
An ecosystem list, MOU, capacity reservation, partner demo or adjacent product
does not qualify.

Related controls: [supplier-attribution audit](supplier-attribution-audit-2026-08-12.md), [switch-CPO SKU reconciliation](switch-cpo-sku-content-reconciliation.md), [six-company attribution register](../07-companies/six-company-content-attribution-register.md), and [profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md).
