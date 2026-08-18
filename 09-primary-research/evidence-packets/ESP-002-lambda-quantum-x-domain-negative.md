# ESP-002 — Lambda Quantum-X domain-control packet

**Review date:** 2026-08-12  
**Source bundle:** `CMP-023`, `CMP-024`, `CMP-040`; `CLM-224`–`CLM-227`, `CLM-321`–`CLM-323`  
**Domain:** NVIDIA Quantum-X InfiniBand, not Spectrum-X Ethernet

## Boundary and customer record

| Field | Finding |
|---|---|
| Named operator | Lambda |
| Exact product | Quantum-X Photonics `Q3450-LD` |
| Architecture | CPO-based InfiniBand; distinct from Spectrum-X Ethernet `SN6800`/`SN6810` |
| Observed configuration | 115.2T, 144 × 800G, 18 ELS; early-access/engineering-sample context |
| Production context | Lambda describes a production-scale GB300 cluster using Quantum-X, but does not provide a switch/unit denominator |
| Spectrum-X evidence | Future preparation/roadmap only; no exact Ethernet CPO shipment |
| Repeat shipment/field population | Not disclosed |
| Supplier/economics | Not disclosed |

## Disposition

**Evidence grade:** B for a named operator’s Quantum-X operational record; D for
the target Spectrum-X Ethernet gate. **Commercial-proof gate:** open.
**Disposition:** strong adjacent-domain evidence and false-positive control.

The record proves that customer-side CPO evidence can exist at scale-up
InfiniBand while remaining inadmissible for the switch-side Ethernet numerator.
Do not transfer its system count, ELS count, power comparison or service
observations into the `SN6800`/`SN6810-LD` case.
