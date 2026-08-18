# Switch-side CPO commercial-proof closeout

**Status:** Private decision readout; no publication, revenue forecast or investment recommendation  
**As of:** 2026-08-14  
**Question:** Is switch-side CPO real deployment, or still product/platform/qualification evidence?

## Required proof bundle

A deployment is counted only when the same evidence bundle supplies: exact CPO SKU, named customer, acceptance/qualification date, a units/ports/systems denominator, and repeat shipment/expansion. A product page, partner, availability date, sample, platform deployment or historical lab test cannot replace a missing field.

## NVIDIA Spectrum-X Ethernet Photonics — one-page readout

| Field | Evidence-adjusted answer | Evidence boundary |
|---|---|---|
| **Exact CPO SKU / architecture** | **Defined.** `SN6810` is 102.4T and `SN6800` is 409.6T, both liquid-cooled Spectrum-X Ethernet Photonics CPO systems; `SN6810-LD` / `SN6800-LD` are controlled ordering-family labels. NVIDIA describes 200G-SerDes CPO, 32 × 3.2T engines in the 102.4T package, detachable fibre connectors and external-light architecture. | Product definition is strong; it does not identify a buyer, an installed configuration or economics (`CLM-514`–`CLM-515`, `CLM-519`, `CLM-406`–`CLM-410`). |
| **Named-customer evidence** | **Platform/adopter evidence only.** NVIDIA names CoreWeave, Lambda, Meta, Microsoft and OCI as Spectrum-X Photonics adopters; Dell and Supermicro describe CPO-capable product/integration routes. | No retained customer source maps an adopter to `SN6810`/`SN6800` or a matching `-LD` SKU. CoreWeave's named `SN6600-LD` deployment is explicitly pluggable, not CPO (`CLM-380`–`CLM-384`, `CLM-542`). |
| **Production status** | **First-party production route is real.** NVIDIA says the system is in full production and maps TSMC, SPIL, TFC and Foxconn roles; a contemporaneous independent report says CPO shipping began to select partners. | Production/partner shipping is not accepted customer deployment or general availability at a defined scale (`CLM-435`–`CLM-437`, `CLM-521`). |
| **Units / repeat shipments** | **Not publicly disclosed.** | No accepted units, ports, systems, acceptance date, repeat delivery, renewal or expansion at an exact Ethernet CPO SKU boundary. |
| **Service / reliability** | **Partial architecture evidence only.** Dell warranty and onsite-service terms exist; external light and connectors are replaceable boundaries. | No observed field-return rate, engine repair workflow, MTTR, spare policy or warranty cost. |

**Verdict — platform/production evidence, not publicly proven commercial deployment.** NVIDIA has the strongest disclosed integrated system and manufacturing route. It has **not** cleared the exact-SKU customer/scale/repeat gate. Upgrade only with a customer record tying `SN6810`/`SN6800` to accepted units and a subsequent repeat/expansion; downgrade the timing thesis if availability continues without that record or customers use pluggable/LPO/NPO alternatives for service or qualification.

## Broadcom TH6-Davisson / BCM78919 — one-page readout

| Field | Evidence-adjusted answer | Evidence boundary |
|---|---|---|
| **Exact CPO SKU / architecture** | **Defined.** `BCM78919` / TH6-Davisson is a 102.4T merchant CPO switch with 64 3nm Condor SerDes cores, 512 × 200G PAM4 all-optical I/O, sixteen 6.4T DR optical engines, 512 duplex fibres and field-replaceable ELSFP light modules. | Architecture/product definition does not allocate PIC, EIC, laser, package, test or economic ownership (`CLM-076`–`CLM-077`, `CLM-516`–`CLM-517`). |
| **Named-customer evidence** | **Partner-route evidence only.** HPE, Celestica, Micas, Nexthop and Corning evidence solution/ecosystem routes. | No named operator/OEM has confirmed accepting TH6 CPO units; an unnamed 2027 hyperscaler programme does not identify TH6 or a customer numerator (`CLM-246`–`CLM-249`, `CLM-255`–`CLM-257`). |
| **Production status** | **Conservative label: early-access / limited release.** The original announcement contains “now shipping” and sampling language; Broadcom's current catalogue labels BCM78919 “Limited Release.” | Neither phrase supplies a customer, accepted units, repeat shipments or broad volume (`CLM-077`, `CLM-530`). |
| **Units / repeat shipments** | **Not publicly disclosed.** | No exact-customer acceptance, port/system denominator, repeat order or expansion record. |
| **Historical validation** | **Meaningful but non-transferable.** PAP-055 reports a TH5/Bailly 51.2T system test with >1m 400G-port device-hours and no UCWs; Meta is the test setting. | This is historical TH5/100G-lane system-test evidence, not TH6/200G customer deployment, yield, field reliability or profit evidence (`CLM-574`–`CLM-577`). |

**Verdict — defined merchant CPO product with early-access/limited-release evidence, not publicly proven commercial deployment.** Broadcom has the clearest disclosed 200G-lane merchant switch CPO product. It has **not** cleared named customer, accepted scale, repeat or CPO-economics gates. Upgrade only with a named TH6 customer plus accepted units and repeat delivery; downgrade if limited release does not convert or alternatives meet the same system requirement at lower qualified cost.

## Cross-SKU conclusion

Neither vendor has public evidence that meets the complete deployment bundle. The correct current statement is: **switch-side CPO is technically and product-route real, with credible production/qualification signals; broad, customer-confirmed repeat deployment remains unproven on the public record.**

## Linked evidence

- Detailed [NVIDIA dossier](nvidia-spectrum-x-photonics.md) and [Broadcom dossier](broadcom-th6-davisson.md).
- [Supplier-content closeout](../supplier-content-map-2026-08-14.md).
- [Exact-SKU search audit](../../09-primary-research/sku-customer-search-audit-2026-08-11.md).
- [Claim ledger](../../01-sources/claim-ledger.csv), especially `CLM-435`–`CLM-437`, `CLM-514`–`CLM-521`, `CLM-530`–`CLM-533`, and `CLM-574`–`CLM-577`.
