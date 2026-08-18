# CMP-054 — NVIDIA Spectrum-X Ethernet Photonics switch-SKU architecture

## Retained source

- **Publisher:** NVIDIA Technical Blog
- **Title:** *Inside the NVIDIA Vera Rubin Platform: Six New Chips, One AI Supercomputer*
- **Publication date:** 2026-01-06
- **Canonical URL:** <https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/>
- **Local preservation:** [original HTML](CMP-054-nvidia-spectrum-x-sn6800-architecture.html)
- **Reviewed:** 2026-08-11

## Evidence retained

NVIDIA identifies two switch-system configurations under Spectrum-X Ethernet Photonics:

| System | Stated CPO configuration |
|---|---|
| `SN6800` | Quad-ASIC, liquid-cooled, 409.6Tb/s; 512 × 800G or 2,048 × 200G ports. |
| `SN6810` | Liquid-cooled, 102.4Tb/s; 128 × 800G or 512 × 200G ports. |

The same source describes the Spectrum-6 CPO package as 102.4Tb/s through 512 × 200G ports with 32 silicon-photonics optical engines at 3.2Tb/s each, micro-ring modulators and detachable fibre connectors.

## Evidence boundary

This resolves the **product-SKU/configuration** part of the NVIDIA commercial-proof gate. It does not identify which configuration a named customer accepted, a delivery date, installed ports/units, repeat shipments, supplier allocation, engine price, yield/rework, warranty or margin. The SKU facts must not be used to infer a customer volume or revenue denominator.

## Research use

Use as the source of record for `CLM-514`–`CLM-515` and in the NVIDIA commercial-proof dossier. Keep `SN6800`/`SN6810` distinct from the pluggable `SN6600-LD` and from Quantum-X `Q3450-LD`.
