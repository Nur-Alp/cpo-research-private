# Commercial-proof retrieval addendum — 12 August 2026

**Status:** Private retrieval log; no public release or investment upgrade
**Question:** Did the latest first-party and exact-label search clear any missing NVIDIA or Broadcom switch-CPO commercial-proof gate?

## Protocol

Searches were run against exact product labels and customer/deployment terms:

- NVIDIA: `SN6810`, `SN6800`, `SN6810-LD`, `SN6800-LD`, “Spectrum-X Ethernet Photonics”, customer, deployment, units, ports and repeat shipment.
- Broadcom: `BCM78919`, `TH6-Davisson`, “Tomahawk 6 CPO”, customer, deployment, units, ports and repeat shipment.

First-party product and newsroom pages were reviewed before secondary results.
A result counted as commercial proof only if it tied the exact CPO SKU to a
named customer/operator and a dated accepted denominator, with a repeat or
expansion record. Product availability, adopter lists, platform benchmarks,
sampling, partner demonstrations and family-level production language were
retained as context but excluded from the numerator.

## Results

| Route | New/current first-party signal | What it proves | What remains unproven | Gate result |
|---|---|---|---|---|
| NVIDIA Spectrum-X Ethernet Photonics | NVIDIA's current silicon-photonics page describes CPO integrated on the switch ASIC, lists CoreWeave, Lambda, Meta, Microsoft and OCI as first adopters, and presents the Ethernet product as available in the second half of 2026. The current Ethernet-switch table identifies `SN6810-LD` and `SN6800-LD` as MMC-12 CPO systems. | Exact product boundary, vendor availability language and named-adopter ecosystem. | No adopter-to-`SN6810-LD`/`SN6800-LD` mapping; no accepted units/ports/system denominator; no repeat delivery; no field-service record; no supplier ASP/share/yield/margin. | **No change: exact SKU cleared; all commercial and economic gates open.** |
| Broadcom TH6-Davisson | Broadcom's official catalogue identifies `BCM78919` as a 102.4-Tb/s CPO switch; the investor release describes sampling to early-access customers and partners. | Exact product boundary and early-access lifecycle status. | No named accepting customer; no accepted units/ports or qualification lot; no repeat delivery; no TH6-specific service history; no supplier allocation or economics. | **No change: exact SKU cleared; customer, scale, repeat and economics open.** |
| NVIDIA customer/operator results | Search results continue to return platform-level Spectrum-X material, including CoreWeave's benchmark and Lambda's separate Quantum-X `Q3450-LD` CPO record. | Platform-scale or different-domain CPO context. | Neither record proves an accepted Spectrum-X Ethernet `SN6810`/`SN6800` deployment. | **Controlled negative; do not transfer evidence across SKU/fabric.** |
| Broadcom partner results | Search results continue to return partner/demo and family-level Tomahawk 6 material. | Route and ecosystem context. | No accepted `BCM78919`/TH6-Davisson customer denominator or repeat shipment. | **Controlled negative; no CPO numerator.** |

## Decision impact

The search does not justify upgrading the 2026–27 timing view from an
evidence-gated inference to a verified volume forecast. It does, however,
increase confidence that the product labels and lifecycle distinctions are
correctly bounded:

```text
NVIDIA: exact CPO product + named adopters + vendor availability
Broadcom: exact CPO product + early-access sampling / Limited Release
Both: exact customer acceptance + units/ports + repeat shipment = open
```

The absence of a public record is not evidence that no deployment exists. It is
evidence only that the current public record cannot support the missing gate.
The next retrieval target remains a customer/OEM acceptance record with the
exact SKU and denominator, followed by supplier-content and service economics.

## External primary-source rerun — 12 August 2026

An additional exact-label rerun was performed against the current official
pages after the private dossier refresh. NVIDIA's live Ethernet-switch table
still exposes `SN6810-LD` and `SN6800-LD` as CPO families, while the Spectrum-X
and silicon-photonics pages continue to use named-adopter language without
mapping an adopter to either ordering label. Broadcom's `BCM78919` page still
shows **Limited Release** and no distributor inventory; Broadcom's launch
announcement still says the device is sampling to early-access customers and
partners. These are consistent with the controlled baseline and do not add a
customer acceptance, units/ports denominator or repeat-shipment event.

This rerun therefore creates **no new source-log or claim-ledger row** and no
gate transition. It is retained here to make the search reproducible and to
prevent later readers from mistaking a repeated product-page result for new
commercial proof.

The same review reconfirmed two **product-specific partner signals** in the
Broadcom release: HPE describes continued collaboration on TH6-Davisson for
future AI-native solutions, and Corning describes complete faceplate-to-chip
optical assemblies for TH6-Davisson systems. These narrow the supplier and
integrator diligence path, but neither statement names an end customer,
qualification/acceptance date, accepted systems or ports, repeat shipment,
commercial share, ASP, yield, warranty or margin. They remain route-level
evidence (`CLM-246`, `CLM-529`), not customer-scale proof.

## Same-day official-page rerun — 12 August 2026

The current official pages were checked again against the exact-label gate:

- NVIDIA's technical blog identifies the **SN6810** single-ASIC and
  **SN6800** quad-ASIC Spectrum-X Ethernet Photonics systems, with 200G lane
  configurations and 102.4T/409.6T system bandwidth. This strengthens the
  product-boundary and architecture record, but the page still does not tie a
  named operator to either ordering-family label (`SN6810-LD`/`SN6800-LD`) or
  provide accepted systems, ports, repeat deliveries, service outcomes or
  economics. See the canonical [NVIDIA technical blog](https://developer.nvidia.com/blog/scaling-power-efficient-ai-factories-with-nvidia-spectrum-x-ethernet-photonics/)
  and the [NVIDIA Ethernet-switch catalogue](https://www.nvidia.com/en-us/networking/ethernet-switching/).
- Broadcom's current **BCM78919** page still identifies the 102.4T/200G CPO
  device and reports **Limited Release** with no distributor inventory. The
  official launch release continues to use both “now shipping” and
  “sampling ... to early access customers and partners”; neither page names a
  completed TH6 customer deployment or a unit/port denominator. See the
  [BCM78919 catalogue](https://www.broadcom.com/products/fiber-optic-modules-components/co-packaged-optics/switches/bcm78919)
  and [launch release](https://www.broadcom.com/company/news/product-releases/63626).

This rerun adds no new customer, qualification, repeat-shipment, service or
supplier-economics gate. It is retained as a negative-control record so that
stronger product and lifecycle language is not later mistaken for a commercial
numerator.

## Canonical pages reviewed

- [NVIDIA Silicon Photonics](https://www.nvidia.com/en-us/networking/products/silicon-photonics/)
- [NVIDIA Ethernet Switching](https://www.nvidia.com/en-us/networking/ethernet-switching/)
- [NVIDIA SN6000 hardware manual](https://docs.nvidia.com/networking/display/sn6000hw)
- [Broadcom BCM78919 catalogue](https://www.broadcom.com/products/fiber-optic-modules-components/co-packaged-optics/switches/bcm78919)
- [Broadcom TH6-Davisson announcement](https://investors.broadcom.com/node/63626/pdf)

Related records: [SKU-customer search audit](sku-customer-search-audit-2026-08-11.md), [commercial-proof decision memo](../07-companies/commercial-proof-dossiers/commercial-proof-decision-memo.md), and [customer-proof register](../08-model/customer-proof-register.md).

The later [OEM/operator exact-SKU search audit](oem-operator-exact-sku-search-audit-2026-08-12.md)
extends this control to customer-authored and OEM records. It found the
SN6600-LD pluggable deployment and current product catalogues, but no exact
SN6800-LD/SN6810-LD or BCM78919 accepted-unit denominator or repeat-shipment
record.
