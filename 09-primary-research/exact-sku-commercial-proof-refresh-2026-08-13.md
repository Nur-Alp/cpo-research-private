# Exact-SKU commercial-proof refresh — 13 August 2026

**Status:** Private retrieval audit; no publication or release clearance  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6800-LD`/`SN6810-LD` and Broadcom `BCM78919` / TH6-Davisson

## Current public records rechecked

| Record | What it confirms | What remains unproven |
|---|---|---|
| NVIDIA silicon-photonics page | CoreWeave, Lambda, Meta, Microsoft and OCI are described as first adopters; Spectrum-X Ethernet Photonics is described as reaching full production; product availability is stated for the second half of 2026 | No adopter-to-`SN6800-LD`/`SN6810-LD` mapping, acceptance date, accepted units/ports, repeat shipment, field record or economics |
| NVIDIA Ethernet switch table | `SN6810-LD` is listed as 128 × MMC-12 CPO and `SN6800-LD` as 512 × MMC-12 CPO; `SN6600-LD` remains separately listed with OSFP pluggable connectivity | Product catalogue and “available” language are not customer shipment or installed-base evidence |
| NVIDIA SN6000 liquid-cooling deployment section | The manual defines nitrogen-pressure and liquid-flood checks before CPO-system power-on | Installation controls do not identify a customer, accepted unit, engine repair, field-return rate, MTTR, warranty cost or repeat delivery |
| Supermicro Vera Rubin release | `SN6800` is identified as 409.6 Tb/s CPO and `SN6810` as 102.4 Tb/s CPO, while `SN6600` is expressly described as pluggable | OEM architecture confirmation does not name an end customer, CPO order, acceptance, unit denominator, repeat shipment or economics |
| Broadcom TH6 release | `BCM78919`/TH6-Davisson is specified at 102.4T, 16 × 6.4T engines, 200G/link, with field-replaceable ELSFP; release says “now shipping” and separately says sampling to early-access customers/partners | No named customer, exact accepted systems/ports, repeat shipment, field-service result, supplier allocation or economics |
| Broadcom supporting quotes | HPE, Celestica, Corning, Micas, Nexthop and TSMC describe collaboration or platform support | Collaboration and partner quotations do not establish procurement, acceptance, units, repeatability or supplier share |

## Gate result

| Gate | NVIDIA | Broadcom |
|---|---:|---:|
| Exact CPO product | **Pass** | **Pass** |
| Named customer tied to exact CPO SKU | **Open** | **Open** |
| Dated acceptance/qualification | **Open** | **Open** |
| Accepted unit/port/system denominator | **Open** | **Open** |
| Repeat shipment/expansion | **Open** | **Open** |
| Product-matched supplier allocation | **Open** | **Open** |
| Yield, ASP, warranty, margin | **Open** | **Open** |

## Interpretation

The NVIDIA page is important because it now presents a coherent product,
partner and production narrative. The simultaneous second-half-2026
availability statement means the page still cannot be read as evidence that a
named operator has accepted `SN6800-LD` or `SN6810-LD` systems. This is a
product-readiness and timing signal, not a customer-volume denominator.

Broadcom's release is similarly strong on product definition and architecture,
but the phrase “now shipping” remains bounded by the explicit early-access
sampling statement and the live **Limited Release** catalogue status. It is not
safe to convert either phrase into general production volume or repeat shipment.

## Search conclusion

No new public record found in this refresh ties either exact SKU to a named
customer's accepted systems and a repeat delivery. The Supermicro record adds
an independent architecture boundary only: it reinforces that an `SN6600`
deployment cannot be counted as `SN6800`/`SN6810` CPO volume. No supplier-level record
joins PIC/engine, EIC, laser, fibre attach, package, connector or test content
to a realised price, share, yield, warranty or margin boundary.

### Named-adopter customer-site sweep

On 13 August 2026, the customer-side public domains for CoreWeave, Lambda,
Oracle and Meta were searched specifically for `SN6810-LD`, `SN6800-LD`,
`BCM78919`, `TH6-Davisson` and `Spectrum-X Ethernet Photonics`. No result
returned a customer-authored exact-SKU acceptance, system/port denominator or
repeat-shipment record. This is a dated retrieval disposition, **not evidence
that no such deployment exists**: customer sites may use different terminology,
restrict procurement information or publish outside their main web domains.
It leaves every commercial gate in the table above open and creates no new
claim-ledger row.

The 2026–2027 thesis therefore remains a **verification window**, not a
demonstrated volume-adoption call. The private dossiers remain the controlling
commercial-proof records, and publication remains locked.

Related controls: [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md), [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md), [supplier-map completeness audit](../08-model/supplier-map-completeness-audit-2026-08-12.md), and [final decision-readiness matrix](../00-scope/final-decision-readiness-matrix.md).

The current customer/OEM/integrator rerun is recorded in [commercial-proof primary-search refresh — 13 August 2026](commercial-proof-primary-search-refresh-2026-08-13.md). It reconfirms that TACC's named CPO work is Quantum-X InfiniBand rather than Spectrum-X Ethernet, and that Celestica's CPO award has no disclosed ASIC/SKU link. Neither clears an exact switch-CPO commercial gate.
