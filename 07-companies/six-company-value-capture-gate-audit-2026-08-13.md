# Six-company value-capture gate audit — 13 August 2026

**Status:** Private decision control; not a ranking, forecast, or publication clearance  
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC  
**Purpose:** Reconcile each company’s public product role with the evidence required to claim CPO value capture.

## Why this audit exists

A company can be strategically exposed to CPO without owning the economic
layer that matters. This control keeps platform ownership, process capability,
supplier capacity, product availability and realised CPO economics separate.
It is intentionally stricter than a technology scorecard: no row becomes an
earnings or valuation input until customer scale, product-matched content and
economic evidence meet at the same boundary.

## Cross-company gate table

| Company | What the retained record proves | Most specific product boundary | What is only a route or option | Decisive missing commercial/economic evidence | Present stance |
|---|---|---|---|---|---|
| NVIDIA | Platform/product owner; `SN6800-LD` and `SN6810-LD` CPO configurations; disclosed manufacturing responsibility map | Spectrum-X Ethernet Photonics switch CPO | TSMC/SPIL/TFC/Foxconn roles; Lumentum, Coherent and SENKO ecosystem/capacity signals | Named exact-SKU customer acceptance; accepted systems/ports; repeat delivery; exact content allocation; supplier and platform economics | Positive strategic exposure / medium confidence |
| Broadcom | Merchant CPO product owner; `BCM78919`/TH6-Davisson architecture; 16 optical engines and ELSFP interface | 102.4T, 200G/lane TH6-Davisson CPO | Partner demonstrations, Limited Release status, TH6-family production language, Corning/TSMC route | Named customer acceptance; units/ports; repeat deployment; exact engine/EIC/laser/package/test allocation; margin and warranty boundary | Positive enabling exposure / medium confidence |
| Coherent | Broad optical component/engine technology and InP manufacturing capability; nonexclusive NVIDIA capacity/purchase agreement | Component/engine family, not a customer-CPO SKU | Capacity, six-inch InP production and agreement scope | Named customer/SKU allocation; qualified shipped engine output; share; transfer price; yield/rework; product margin | Constructive component exposure / medium confidence |
| Lumentum | External-light/ELSFP and UHP-laser route; CPO and initial ELS-module order signals | External-light/module layer, not a complete engine | Order value, NVIDIA agreement and capacity signal | Customer/product/quantity conversion; module share and price; qualified output; warranty burden; product margin | Constructive/watch external-laser exposure / medium confidence |
| Marvell | Celestial Photonic Fabric scale-up optical-I/O route; acquisition completed; management revenue targets stated; Q1 FY27 filing says post-acquisition revenue/earnings were not material | Accelerator optical-I/O chiplet, distinct from switch-side CPO | Existing customer traction and target run-rate language | Named XPU/customer; qualified production units; revenue recognition; yield/cost and segment margin | Strategic watch / low-to-medium confidence |
| TSMC | COUPE SiPh/EIC process and 2026 production milestone; 200G demonstration; engineering-sample stacking yield | Process/integration route, not a complete-engine contract | COUPE-on-substrate production language and Broadcom COUPE-engine reference | Customer SKU; qualified output; exact wafer/package/engine boundary; price/share; attributable foundry/package margin and capex | Manufacturing-control watch / medium confidence |

## Evidence classification matrix

| Evidence class | NVIDIA | Broadcom | Coherent | Lumentum | Marvell | TSMC |
|---|---|---|---|---|---|---|
| Exact relevant product definition | **Yes** | **Yes** | Component family only | Component/module family only | **Yes, but scale-up rather than switch CPO** | Process product only |
| Named customer at exact product boundary | No | No | No | No | No | No |
| Accepted unit/port/output denominator | No | No | No | No | No | No |
| Repeat shipment / qualified production evidence | No | No | No | No | No | No |
| Product-matched physical content / share | Platform route only | Platform route only | No | No | No | Process route only |
| Product-matched ASP / price | No | No | No | No | No | No |
| Yield / rework / warranty data | Process/service policy only | Historical/adjacent controls only | No | No | No | Engineering-sample sub-boundary only |
| Product gross margin / capex burden | No | No | No | No | No | No |

**Audit result:** no company has the full evidence bundle to support a numeric
CPO revenue, margin, EPS, valuation, profit-pool or leader conclusion.

## One record that would change each case

| Company | Highest-value next record | Why it changes the decision |
|---|---|---|
| NVIDIA | Customer/OEM record naming `SN6800-LD` or `SN6810-LD`, accepted system/port count, date and a second delivery | Converts platform/production language into an exact CPO commercial numerator |
| Broadcom | Customer/integrator record naming `BCM78919`/TH6-Davisson, accepted count/date and repeat order | Tests whether limited-release/sampling has crossed into merchant CPO deployment |
| Coherent | Product-linked customer or supplier disclosure identifying Coherent’s exact optical layer, qualified output, price and margin boundary | Separates component breadth from sellable and profitable CPO content |
| Lumentum | Order-conversion disclosure specifying customer, module/product, quantity, delivery, price/content and margin boundary | Determines whether order value represents external light, broader optical content, or capacity only |
| Marvell | Named XPU/customer qualification with production units and reported Photonic Fabric revenue/margin | Converts scale-up optical-I/O optionality into a measurable business |
| TSMC | Customer SKU and qualified COUPE output with package scope, price/capacity allocation and margin boundary | Separates enabling-process importance from complete-engine economic ownership |

## Controls against common overclaims

1. Do not transfer NVIDIA or Broadcom platform volumes into supplier revenue.
2. Do not transfer Coherent or Lumentum capacity agreements into CPO share or margin.
3. Do not transfer TSMC engineering-sample stacking yield into final-engine yield.
4. Do not transfer Marvell management targets into observed production revenue.
5. Do not use a company-wide gross margin for a component, engine, package or test layer.
6. Do not use an unnamed CPO program or test-equipment order as a named product/customer deployment.

## Source and control anchors

- [Core six-company variant cards](variant-cards/core-company-variant-cards.md)
- [Six-company commercial-proof queue](six-company-commercial-proof-queue-2026-08-12.md)
- [CPO content-attribution map](../08-model/cpo-content-attribution-map.md)
- [Profit-pool input reconciliation](../08-model/profit-pool-input-reconciliation-2026-08-12.md)
- [Commercial-proof acquisition plan](../09-primary-research/commercial-proof-evidence-acquisition-plan-2026-08-13.md)
- [Final decision-readiness matrix](../00-scope/final-decision-readiness-matrix.md)

The referenced claim IDs and source IDs in the linked controls remain the
system of record; this audit intentionally introduces no new factual claim.
