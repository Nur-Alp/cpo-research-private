# Commercial-proof evidence acquisition plan — 13 August 2026

**Status:** Private operating plan; no publication or investment-call clearance  
**Decision owner:** Nur Alpys  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6800-LD` / `SN6810-LD` and Broadcom `BCM78919` / TH6-Davisson

## Decision objective

Move the thesis from a vendor product/production narrative to an evidenced commercial and economic conclusion. A result is usable only when it resolves a defined gate at the same product boundary. A product-family announcement, partner demonstration, capacity investment, or generic CPO article does not clear a gate by itself.

## Evidence ladder and acquisition targets

| Priority | Required proof | Minimum record needed | Best public record holder | Current boundary | Decision effect if found |
|---|---|---|---|---|---|
| 1 | Customer acceptance | Named operator, exact CPO SKU/configuration, dated acceptance or qualification | Customer/operator, OEM, procurement filing, or case study | Both targets open | Clears the first commercial-proof field only |
| 2 | Scale denominator | Accepted systems, ports, racks or switch count and time period | Customer/operator, OEM, earnings call, shipment/capacity filing | Both targets open | Makes deployment measurable; does not prove repeatability |
| 3 | Repeatability | Second order, expansion, renewal, or subsequent installation for the same SKU | Customer/operator, OEM, integrator or supplier filing | Both targets open | Enables meaningful-adoption assessment |
| 4 | Field/service result | Field-period, installed-base denominator, return/replacement or service procedure | Customer/operator, OEM support case, reliability disclosure | Both targets open | Tests serviceability rather than lab readiness |
| 5 | Product-matched content | Exact-SKU PIC/engine, EIC, laser, attach, package, connector and test responsibility | Platform owner, named supplier, OSAT, integrator | Routes partly mapped; allocations open | Narrows candidate value capture |
| 6 | Realised economics | Qualified share, price/ASP, yield/rework, warranty, capex and product margin | Supplier filing, contract, customer/supplier disclosure | Both targets open | Required for a profit-pool leader or earnings bridge |

## Exact-SKU work queue

| Target | Lead to test | Mandatory discriminator | Accept if | Reject / retain as negative control if |
|---|---|---|---|---|
| NVIDIA `SN6800-LD` / `SN6810-LD` | CoreWeave, Lambda, Meta, Microsoft, OCI adoption statements | The record must name the Ethernet CPO SKU or matching `SN6800`/`SN6810` configuration | Customer-authored/OEM-authored record joins SKU, CPO interface and acceptance/date | It says Spectrum-X broadly, groups Quantum-X and Spectrum-X, or names `SN6600-LD`; see `ESP-001` and `ESP-002` |
| NVIDIA `SN6800-LD` / `SN6810-LD` | Dell and Supermicro validated-rack material | End customer and accepted CPO configuration must be named | A customer-side or OEM order/acceptance record includes count/time period | It merely illustrates hardware, offers CPO as an option, or describes a validated design |
| NVIDIA `SN6800-LD` / `SN6810-LD` | TSMC, SPIL, TFC, Foxconn, Lumentum, Coherent and SENKO disclosures | Exact SKU plus physical responsibility and commercial boundary | Exact system content/share, output, qualification lot, or economics is disclosed | It is ecosystem, capacity, generic process or family-level supply evidence |
| Broadcom `BCM78919` / TH6-Davisson | HPE, Celestica, Micas, Nexthop, Alpha, DNI and Corning routes | `BCM78919`/TH6-Davisson must be named, not Tomahawk 6 family alone | Customer acceptance plus configuration and count/date are disclosed | It is a demo, limited-release listing, family-volume claim, or partnership; see `ESP-003` |
| Broadcom `BCM78919` / TH6-Davisson | Celestica hyperscaler CPO program | Customer, ASIC/SKU and optical configuration must be reconciled | The program identifies BCM78919/TH6, acceptance status and a denominator | It remains unnamed, planned for 2027, or only says 1.6T silicon/CPO |
| Broadcom `BCM78919` / TH6-Davisson | Optical-engine, ELSFP, Corning/package and test disclosures | Product-matched qualified role and output/economic boundary | Supplier identifies share or priced/shipped content linked to the exact product | It states collaboration, interface compatibility, historical TH5 evidence or capacity only |

## Search cadence and stop rule

- **Event-driven:** review company earnings releases, 10-Q/10-K filings, OCP/OFC materials, operator product blogs and OEM product/case-study releases when published.
- **Quarterly control:** rerun the exact-SKU search, source-date audit and the commercial-proof readiness validator before editing the thesis.
- **Stop rule:** do not add generic CPO commentary once it fails to resolve any field in the evidence ladder. Record only a concise negative disposition if it is a plausible false positive.

## Intake protocol for a potential result

1. Save the original readable source and its canonical URL under `01-sources/`.
2. Create an evidence note stating the exact quoted boundary, source date and what the item does *not* establish.
3. Add a source-log row and claim-ledger row only if it changes a decision, closes a gate, or is a recurring false-positive control.
4. Complete the [exact-SKU evidence-packet template](exact-sku-evidence-packet-template.md).
5. Update the customer-proof register, exact-SKU dossier and supplier-map audit together; do not update only a narrative.
6. Run `python3 scripts/audit-commercial-proof-readiness.py`. A green integrity check is not permission to publish: `release_ready` must be true and the evidence must satisfy the substantive gate.

## Current decision state

The next thesis-changing record is a **customer or OEM statement with an exact NVIDIA or Broadcom CPO SKU, dated accepted systems/ports and repeat delivery**. The next profit-pool-changing record is a **product-matched supplier disclosure joining physical content to share, realised price, yield/rework, warranty and margin**. Neither has been retained as of this plan.

Related controls: [commercial-proof dossiers](../07-companies/commercial-proof-dossiers/README.md), [customer-proof register](../08-model/customer-proof-register.md), [supplier-map completeness audit](../08-model/supplier-map-completeness-audit-2026-08-12.md), [profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md), and [13 August exact-SKU refresh](exact-sku-commercial-proof-refresh-2026-08-13.md).
