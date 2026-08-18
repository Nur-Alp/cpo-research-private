# ESP-001 — CoreWeave SN6600-LD negative control

**Review date:** 2026-08-12  
**Source bundle:** `CMP-021`, `CMP-022`, `CMP-046`–`CMP-048`; `CLM-220`–`CLM-223`, `CLM-370`–`CLM-384`  
**Domain:** NVIDIA Spectrum-X / Vera Rubin Ethernet

## Boundary and customer record

| Field | Finding |
|---|---|
| Named operator | CoreWeave |
| Product stated by customer | `SN6600-LD`, 102.4T, 64 × 1.6T configuration |
| Architecture | Pluggable RHS-transceiver configuration, not switch-side CPO (`CLM-380`–`CLM-383`) |
| Customer context | Production-oriented/early-adopter context; separate CPO-adopter language is not SKU-allocated |
| Accepted units/ports | 64 ports are a product configuration, not a disclosed accepted fleet denominator |
| Repeat shipment/expansion | Not disclosed |
| Supplier/economics | Not disclosed |

## Disposition

**Evidence grade:** B for named pluggable platform deployment; D for target
Spectrum-X Ethernet CPO proof. **Commercial-proof gate:** open. **Disposition:**
false-positive control and architecture-boundary evidence.

This packet must not be used to claim that CoreWeave accepted `SN6810-LD` or
`SN6800-LD`. It demonstrates why a named customer, a CPO-adopter statement and
an exact product image cannot be combined unless the same source joins the
customer to the exact CPO SKU.
