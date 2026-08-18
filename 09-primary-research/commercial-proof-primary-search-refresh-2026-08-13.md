# Commercial-proof primary-search refresh — 13 August 2026

**Status:** Private no-change retrieval audit; not publication clearance  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6810-LD` / `SN6800-LD` and Broadcom TH6-Davisson `BCM78919`

## Search question

Can a primary customer, OEM, integrator or filing source establish an exact switch-CPO SKU, named buyer, accepted-unit/port denominator, repeat shipment, or attributable supplier economics?

## New and rechecked primary records

| Record | What it establishes | Why it does not clear the commercial gate |
|---|---|---|
| NVIDIA SN6000 hardware documentation | The live manual gives `SN6810-LD` / `SN6800-LD` CPO installation, liquid-cooling and maintenance procedures. | It is a vendor hardware manual: no buyer, order, accepted system, port denominator, repeat delivery, field-return result or supplier economics. |
| Dell PowerSwitch SN6000 integration | Dell independently describes CPO options in the SN6000 route and illustrates `SN6800-LD`; support policy covers the CPO SKU families. | OEM availability/support policy are not customer acceptance, installed-base or observed MTTR/warranty-cost data. |
| NVIDIA current silicon-photonics page | NVIDIA names CoreWeave, Lambda, Meta, Microsoft and OCI as first Photonics adopters and states second-half-2026 availability. | No adopter-to-`SN6810-LD` / `SN6800-LD` mapping, acceptance date, unit/port count, repeat shipment, service population or economics. |
| TACC / NVIDIA supercomputing record | TACC, Lambda and CoreWeave are publicly tied to **Quantum-X InfiniBand** Photonics integration; TACC’s Horizon record identifies Quantum-2 InfiniBand. | Different product/domain: it cannot create an Ethernet Spectrum-X CPO denominator. |
| Broadcom `BCM78919` product page | The live page identifies 102.4T, 512 × 200G all-optical I/O and 64 Condor SerDes cores; lifecycle remains **Limited Release** with no distributor inventory. | No customer name, accepted quantity, repeat delivery, field-service population, supplier share, ASP or margin. |
| Broadcom TH6 release | The announcement says the device is sampling to early-access customers/partners. | It does not identify customers, accepted/qualified samples, quantity, repeat business, final configuration or economics. |
| Celestica Q1 FY2026 filing/release | Celestica reports a 1.6T CPO Ethernet-switch design/manufacturing award for an unnamed hyperscaler, with expected 2027 production ramp. | No buyer or ASIC/CPO SKU. It cannot be assigned to `BCM78919`, NVIDIA, Broadcom or any component supplier, and is not accepted units. |

## Invalid joins deliberately excluded

1. Named NVIDIA adopter is not exact Ethernet-CPO acceptance.
2. TACC’s named CPO record is not Spectrum-X Ethernet.
3. Celestica’s CPO award is not TH6-Davisson.
4. Limited Release and sampling are not accepted production volume.

## Gate result — unchanged

| Required gate | NVIDIA `SN6810-LD` / `SN6800-LD` | Broadcom `BCM78919` |
|---|---:|---:|
| Exact CPO SKU | **Pass** | **Pass** |
| Named buyer linked to exact SKU | Open | Open |
| Dated acceptance or qualification | Open | Open |
| Accepted system/port denominator | Open | Open |
| Repeat shipment or expansion | Open | Open |
| Exact supplier/content allocation | Open | Open |
| Yield, warranty, ASP or gross margin | Open | Open |

## Decision impact

This rerun strengthens the false-positive controls, not the deployment case. The public record supports a 2026–2027 switch-CPO verification window and specific NVIDIA/Broadcom product routes, but not demonstrated volume deployment or a proven CPO profit-pool leader.

**Sources already retained:** `CMP-018`, `CMP-021`, `CMP-028`, `CMP-029`, `CMP-048`, `CMP-057`, `CMP-058`, `CMP-062`, `CMP-073`, `CMP-076`, `CMP-077`, `CMP-079`, `CMP-081`, `CLM-220`, `CLM-255`–`CLM-257`, `CLM-519`–`CLM-520`, `CLM-530`, `CLM-542`, `CLM-545`–`CLM-550`.
