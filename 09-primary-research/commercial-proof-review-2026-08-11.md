# Switch-CPO commercial-proof review — 12 August 2026

**Status:** Private evidence review; no publication decision implied  
**Question:** Has switch-side CPO progressed to a customer-confirmed, repeat commercial deployment with an attributable supplier/economic chain?

## Review result

**No switch-side platform clears the commercial-proof gate.** The new primary-source review reinforces the timing route for NVIDIA Spectrum-X Ethernet Photonics and the product boundary for Broadcom TH6-Davisson, but it does not add the required same-boundary evidence of an accepted customer CPO SKU, units/ports and repeat shipments.

This is a meaningful *no-change* result. It prevents three common errors:

1. Counting NVIDIA's named adopters as confirmed CPO unit customers;
2. Counting production-volume shipment of the broader Tomahawk 6 family as TH6-Davisson CPO volume; and
3. Treating a hyperscaler CPO programme award with a planned 2027 ramp as realised CPO revenue or supplier profit.

## Gate definition

The commercial gate passes only when one evidence bundle identifies all four at the **same switch-CPO boundary**:

| Requirement | Why it matters |
|---|---|
| Exact CPO SKU/configuration | Separates CPO from Spectrum-X/Tomahawk-family, pluggable, LPO and NPO alternatives. |
| Customer acceptance/qualification date | Separates vendor availability from an operator decision. |
| Units, ports or systems over a stated period | Creates a volume denominator. |
| Repeat order, expansion or renewal | Separates a one-off sample/engineering system from repeatable deployment. |

The separate economic gate additionally needs a content boundary, supplier share, realised price, final-engine yield/rework, service/warranty allocation and margin. No company reaches that gate.

## Primary-source check

| Source and retained record | What it adds | What it does **not** add | Gate result |
|---|---|---|---|
| NVIDIA silicon-photonics product page — `CMP-025` | Spectrum-X Ethernet Photonics is described as full production; CoreWeave, Lambda, Meta, Microsoft and OCI are named first adopters. | Customer-specific CPO SKU, accepted CPO units/ports, repeat shipment, supplier share or economics. The partner list is not a bill of materials. | Timing/route only. |
| NVIDIA technical SKU architecture — `CMP-054`, `CMP-048`, `CLM-381`, `CLM-514`–`CLM-515` | Names the CPO system configurations: `SN6800` (409.6T) and `SN6810` (102.4T); the hardware manual uses the corresponding `SN6800-LD`/`SN6810-LD` CPO ordering-family labels; identifies 32 × 3.2T engines in the 102.4T package. | Which configuration any adopter accepts, units, delivery date, repeat shipment or economic allocation. The naming cross-reference is not a customer-shipment link. | SKU definition only. |
| NVIDIA production-ramp article — `CMP-053`, `CLM-435`–`CLM-437` | Names physical responsibility layers: TSMC (silicon photonics), SPIL (package/assembly/test), TFC (laser module) and Foxconn (system assembly). | Which party supplies a complete engine; any allocation of content, yield, price, margin or warranty. | Responsibility map only. |
| Focus Taiwan / CNA — `NWS-013`, `CLM-521` | Independently reports an attributed NVIDIA networking-SVP statement that Spectrum-X CPO began shipping to select partners at GTC Taipei. | Exact CPO SKU, partner/customer names, evaluation versus acceptance, units/ports, repeat shipments or economics. | Shipment-status corroboration only. |
| Foxconn Q1 2026 outlook — `CMP-060`, `CLM-526`–`CLM-527` | Foxconn forecasts Q3 2026 CPO-switch mass-production shipments and says full-year shipments may reach tens of thousands; it also describes preparation with unnamed cloud/AI customers and broad integration capabilities. | An actual shipment, named product maker/SKU/customer, accepted units/ports, repeat shipment, final-engine responsibility or economics. | Manufacturer outlook only; verify against Q3 results. |
| Dell OEM product catalogue and SN6000 datasheet — `CMP-057`, `CLM-519` | Dell independently lists PowerSwitch `SN6810-LD`/`SN6800-LD` CPO products with MMC-12 interfaces and keeps the OSFP224 `SN6600-LD` pluggable configuration separate. The 12 August live listing continues to label CPO SKUs **New** / **Contact Sales** while the pluggable SKU is **Shop Now**. | A booked order, named operator, acceptance, units, repeat shipment, product economics or supplier BOM. Different catalogue call-to-action labels do not identify supply availability, demand or shipment volume. | OEM/channel and SKU-boundary evidence only. |
| Dell networking warranty page — `CMP-058`, `CLM-520` | Dell supplies a system-level warranty/replacement policy for the two CPO SKU families. | Engine/package repair method, achieved MTTR, field-service performance, cost or a customer deployment. | Service-policy evidence only. |
| Broadcom TH6-Davisson release — `CMP-018`, `CLM-076`–`CLM-078`, `CLM-246`–`CLM-249` | Defines the 102.4T, 16-engine, 200G/link CPO switch and ELSFP service boundary; identifies partner routes. | A named completed customer deployment, accepted TH6 CPO units, repeat order, supplier BOM or economics. Its availability text still says early-access sampling. | Product/early-access only. |
| Broadcom CPO product catalogue — `CMP-062`, `CLM-530` | The live catalogue classifies BCM78919 as **Limited Release**, corroborating a conservative current commercial label. | A customer, customer acceptance, unit/port denominator, repeat order, general availability, supplier allocation or economics. | Lifecycle check only; no CPO numerator. |
| Broadcom Tomahawk 6 production-volume release | Establishes production-volume language for the **Tomahawk 6 family**. | The release does not state what part of family volume is TH6-Davisson CPO. Family volume must not be relabelled as CPO volume. | No CPO numerator. |
| Celestica Q1 2026 results — `CMP-028`, `CLM-255`–`CLM-256` | Officially reports an awarded CPO Ethernet-switch design/manufacturing programme for an unnamed hyperscaler using 1.6T silicon, CPO interconnects and liquid cooling; expected ramp in 2027. | Customer, SKU, qualification completion, units, repeat order, realised revenue, supplier content or margin. | Planned programme only. |
| CoreWeave production/benchmark records — previously retained boundary notes `CMP-021`, `CMP-046`–`CMP-048` | Confirm that a large Spectrum-X/Ethernet platform can be present in a production/benchmark fabric. | An exact Spectrum-X Ethernet Photonics CPO configuration. The retained SN6600-LD hardware boundary is pluggable, not CPO. | Negative architecture control. |
| Lambda customer records — `CMP-023`, `CMP-024`, `CMP-040` | Customer-side production-scale evidence exists for **Quantum-X InfiniBand Photonics**; Spectrum-X Ethernet is described as preparation/roadmap. | Spectrum-X Ethernet Photonics accepted units or repeat switch-side deployment. | Separate-domain evidence only. |

## Evidence-quality reading

- **NVIDIA:** strongest disclosed switch-CPO production and manufacturing route. The correct current statement is *company-reported production with named early adopters; switch-CPO customer numerator open*.
- **Broadcom:** clearest merchant 200G/lane switch-CPO definition. The correct current statement is *defined TH6 product with early-access / Limited Release status; volume numerator open*.
- **Celestica:** strongest new external manufacturing-program signal. The correct current statement is *unnamed-customer 2027 programme; no shipped/financial denominator*.
- **Foxconn:** material manufacturer timing signal. The correct current statement is *Q3 2026/tens-of-thousands management outlook; not an observed shipment and not allocable to NVIDIA or Broadcom.*

No record establishes a public CPO profit-pool leader. The research should preserve a neutral/watch conclusion until the commercial and economic gates both pass.

## Priority follow-up requests

1. Customer-authored confirmation of a named **Spectrum-X Ethernet Photonics** or **TH6-Davisson** deployment with configuration, acceptance date and port/system count.
2. A repeat order, expansion, fleet-wide roll-out or warranty/service disclosure tied to the same SKU.
3. A product-boundary supplier map allocating PIC/engine, EIC, external laser, fibre attach, package, connector and test.
4. A qualified-engine yield waterfall with rework and burn-in/test boundary.
5. Contract or filing evidence for content, supplier share, price-down/cancellation terms and margin/capex allocation.
6. Foxconn FY26 Q2 results scheduled for 12 August 2026, then Q3 2026 results or customer/product records that verify, revise or withdraw the stated production and volume outlook. The [event checklist](foxconn-q2-cpo-verification-checklist-2026-08-12.md) prevents generic networking commentary from being counted as a CPO shipment.

## Source-access note

The Celestica results page and PDF endpoint returned HTTP 403 to this automated environment on 11 August 2026. Its canonical original URL and evidence boundary remain in the retained `CMP-028` source card; it should be refreshed through a normal browser session when available. No blocked page is treated as a locally retained primary document.

## Linked controls

- [Commercial-proof dossier index](../07-companies/commercial-proof-dossiers/README.md)
- [NVIDIA dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md)
- [Broadcom dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md)
- [Customer-proof register](../08-model/customer-proof-register.md)
- [Content-attribution map](../08-model/cpo-content-attribution-map.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
