# CPO disclosure-lag model

**Status:** Private reporting-timing framework; not a deployment forecast  
**As of:** 2026-08-13

## Purpose and constraint

Technology firms commonly disclose architecture, samples, product availability,
partners and capacity before customer denominators or product economics. This
model tracks that sequence to distinguish a normal disclosure gap from a stall.
It does **not** infer that an undisclosed deployment exists, or forecast when a
company will disclose a number.

## Disclosure ladder

| Stage | Minimum public observation | Current examples | What remains open |
|---|---|---|---|
| 1. Technical route | Device, architecture, standard or demo | CPO, LPO/RTLR, NPO/OBO, InP/TFLN records | Product/customer/commercial status |
| 2. Product / samples | Product label, samples, Limited Release, early access or orderability | BCM78919 Limited Release; CPO SKU catalogues | Accepted customer numerator |
| 3. Partner / customer mention | Partner, adopter or customer mentions product family/domain | Spectrum-X adopters; partner ecosystems | Exact SKU, acceptance and units |
| 4. Production claim | Company says in production/shipping/ramping | NVIDIA CPO route; TH6-family production context; Celestica planned ramp | Product-matched accepted units/repeatability |
| 5. Commercial proof | Exact customer, SKU, accepted denominator and repeat delivery | No current 200G switch-CPO case clears | Field/service and economics |
| 6. Financial disclosure | Product content/price/revenue/margin/capex or other attributable economics | No current CPO product case clears | Sustainable margin and competitive durability |

## Lag interpretation

| Observation | Permitted reading | Not permitted |
|---|---|---|
| Long gap between stages 2–4 | A disclosure gap to monitor; may reflect early commercialisation or sensitivity | Assumption of hidden volume or failure |
| Customer family/platform mention without SKU | Partial ecosystem/context evidence | Customer acceptance of a specific CPO configuration |
| Factory/test expansion before stage 5 | Capacity-readiness proxy | Shipment, yield or margin |
| Stage 5 without stage 6 | Commercial proof may be developing while economics remain unknown | Supplier profit-pool ranking |

## Calibration register

For each company/product, record dates rather than estimated lags:

| Product / route | Stage 1 date | Stage 2 date | Stage 3 date | Stage 4 date | Stage 5 date | Stage 6 date | Current interpretation |
|---|---|---|---|---|---|---|---|
| NVIDIA Spectrum-X Ethernet CPO | Retained route record | SKU/product record | Named adopters, family boundary | Production claim | Open | Open | Commercial proof/economics not public |
| Broadcom TH6-Davisson | Retained architecture record | Limited Release/early access | Partner route | Family versus exact-product language separated | Open | Open | Product route clear; customer/economics open |
| Lumentum ELS/CPO | Product/order route | ELSFP/laser route | Not product-matched customer | Order delivery window | Open | Open | Supplier conversion signal, attribution open |
| TSMC COUPE | Process/demonstration | Process production milestone | Several-customer process statement | Process milestone | Open | Open | Process route, not complete-engine commercial proof |
| Marvell Photonic Fabric | Product/transaction route | Product roadmap | Customer context not product-matched | Management targets | Open | Open | Separate scale-up route, conversion open |

## Decision use

The model changes research *cadence*, not the conclusion. If a route remains at
stages 2–4, continue exact-SKU/customer and economics searches. Promote only
on a stage-5 or stage-6 record meeting the same-boundary gate. Record each
unchanged review in the quarterly evidence register; silence is neither
confirmation nor falsification.

Related controls: [public evidence extraction pack](../09-primary-research/public-evidence-extraction-pack.md), [commercial-proof dossiers](../07-companies/commercial-proof-dossiers/README.md), and [quarterly evidence register](../09-primary-research/quarterly-evidence-change-register-2026-08-12.md).
