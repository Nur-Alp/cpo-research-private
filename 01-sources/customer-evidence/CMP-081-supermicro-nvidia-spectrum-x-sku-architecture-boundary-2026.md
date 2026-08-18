# CMP-081 — Supermicro NVIDIA Spectrum-X SKU / architecture boundary

**Source type:** Official OEM investor-relations release  
**Organisation:** Super Micro Computer, Inc.  
**Published:** 2026-01-05  
**Reviewed:** 2026-08-13  
**Canonical URL:** https://ir.supermicro.com/news/news-details/2026/Supermicro-Announces-Support-for-Upcoming-NVIDIA-Vera-Rubin-NVL72-HGX-Rubin-NVL8-and-Expanded-Rack-Scale-Manufacturing-Capacity-for-Liquid-Cooled-AI-Solutions/default.aspx  
**Decision use:** NVIDIA exact-SKU CPO-versus-pluggable boundary control

## Evidence retained

Supermicro's Vera Rubin platform release identifies three NVIDIA Spectrum-X
models separately:

| Model | Supermicro's stated configuration |
|---|---|
| `SN6800` | Liquid-cooled 409.6 Tb/s **CPO**, 512 × 800G ports |
| `SN6810` | Liquid-cooled 102.4 Tb/s **CPO**, 128 × 800G ports |
| `SN6600` | **Pluggable**, 102.4 Tb/s, 128 × 800G ports; air/liquid-cooled |

This is an independent OEM confirmation that the two target Spectrum-X CPO
configurations must not be conflated with the `SN6600` pluggable configuration.

## Boundary and limitation

The release is a product/platform announcement. It says Supermicro is
positioned to deploy Vera Rubin infrastructure and refers to availability of
models, but it identifies neither an end customer nor an accepted CPO system.
It supplies no order date, accepted unit/port count, repeat shipment, field
service population, supplier allocation, yield, ASP, warranty cost, or margin.

## Decision classification

**Observed:** exact model/architecture distinction at an OEM boundary.

**Open:** customer-to-`SN6800`/`SN6810` mapping, acceptance, scale, repeat
shipment, service record, and product-linked supplier economics.

**Decision treatment:** retain as a false-positive control. It makes the
CoreWeave `SN6600-LD` record less—not more—usable as evidence for the target
CPO products. It does not change the NVIDIA commercial-proof gate.

Related dossiers: [NVIDIA Spectrum-X commercial proof](../../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md), [exact-SKU refresh](../../09-primary-research/exact-sku-commercial-proof-refresh-2026-08-13.md).
