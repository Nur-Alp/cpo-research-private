# OEM/operator exact-SKU search audit — 12 August 2026

**Status:** Private retrieval control; no publication or investment upgrade
**Question:** Did an OEM or operator publish a dated acceptance, installed-unit denominator, or repeat deployment for the exact NVIDIA Spectrum-X Ethernet CPO SKUs or Broadcom TH6-Davisson BCM78919?

## Search protocol

The search used exact labels and deployment verbs across official and OEM/operator pages:

- NVIDIA: `SN6800-LD`, `SN6810-LD`, `SN6800`, `SN6810`, `Spectrum-X Ethernet Photonics`, deployed, installed, customer, accepted, shipment, repeat.
- Broadcom: `BCM78919`, `TH6-Davisson`, Tomahawk 6 CPO, deployed, installed, customer, accepted, shipment, repeat.

Product catalogues and hardware manuals were checked separately from customer/operator-authored deployment pages. A result could clear the customer gate only if it named the exact CPO configuration and provided a dated acceptance or shipment denominator. A product's nominal port count is not an installed-unit denominator.

## Findings

| Record | Exact product boundary | Evidence found | Gate treatment |
|---|---|---|---|
| NVIDIA SN6800-LD / SN6810-LD catalogue and manual | **Yes:** SN6800-LD and SN6810-LD are identified as MMC-12 CPO systems; the manual gives 2,048 and 512 200GbE breakout ports respectively | Product specifications, cooling and interface data; no operator name, order, acceptance date, installed systems or repeat shipment | Product-boundary corroboration only; **no customer numerator** |
| NVIDIA CoreWeave | **No target match:** current operator post identifies SN6600-LD for Vera Rubin NVL72 | SN6600-LD is a separate pluggable/OSFP-family boundary; no SN6800-LD/SN6810-LD acceptance | Controlled negative; do not transfer to target CPO SKUs |
| NVIDIA Spectrum-X platform benchmarks | **No target match:** customer/operator benchmark uses the Spectrum-X platform without naming SN6800-LD/SN6810-LD or CPO configuration | Platform scale and performance context only | Controlled negative; platform deployment is not CPO volume |
| NVIDIA first-adopter list | **No target match:** CoreWeave, Lambda, Meta, Microsoft and OCI named as first adopters, but no adopter-to-SKU mapping | Ecosystem/adoption signal; no accepted systems/ports or repeat delivery | Follow-up lead; exact-SKU gate remains open |
| Broadcom BCM78919 catalogue/product brief | **Yes:** BCM78919 is a 102.4T CPO switch with 512 × 200G capability | Product definition; lifecycle is Limited Release and distributor inventory is listed as none | Exact-SKU product pass; no customer acceptance or shipment denominator |
| Broadcom TH6-Davisson announcement | **Yes:** BCM78919/TH6-Davisson is named; release says now shipping and sampling to early-access customers/partners | Partner quotes from HPE, Celestica, Corning, Micas and Nexthop; no named accepting customer or unit count | Early-access/partner context; no customer-scale gate |
| Broadcom Tomahawk 6 family production statement | **No target match:** family-level production language covers multiple SerDes and interconnect options | Broad family timing signal | Cannot be used as BCM78919 CPO numerator |
| Celestica DS6000 / CPO award | **No target match:** 102.4T platform and unnamed hyperscaler CPO program do not identify BCM78919 | Ready-to-order/expected-2027-ramp context, configuration ambiguous | Route lead only; no exact-SKU customer proof |

## Result

No new exact-SKU customer acceptance, accepted-unit/port denominator, repeat shipment, or field-service record was found. The absence of a public record does not prove that deployments do not exist; it limits what the public evidence can support.

The current commercial numerator therefore remains:

```text
NVIDIA SN6800-LD/SN6810-LD: 0 publicly verified accepted systems
Broadcom BCM78919:           0 publicly verified accepted systems
```

The zeroes above mean **not disclosed / not verified**, not “zero deployed.” They must not be used as market-share estimates.

## Next evidence request

The highest-value follow-up is a customer or OEM document that states one of the following in the same record: exact SKU, qualification/acceptance date, systems or ports accepted, and a second shipment/expansion. For supplier economics, the required follow-on is a product-linked BOM or supplier filing that identifies PIC/engine, ELS, attach/package/test allocation and a realised price or margin boundary.

Related controls: [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md), [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md), [commercial-proof retrieval addendum](commercial-proof-retrieval-addendum-2026-08-12.md), and [customer-proof register](../08-model/customer-proof-register.md).
