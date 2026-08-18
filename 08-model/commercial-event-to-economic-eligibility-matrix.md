# Commercial event → economic eligibility matrix

**Owner:** Nur Alpys  
**Status:** Private modelling control; not a revenue forecast or investment conclusion  
**As of:** 2026-08-13  
**Applies to:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC; switch-side CPO, scale-out engines/PICs, external light and accelerator optical I/O

## Decision rule

Public disclosures often sound economically meaningful long before they are
eligible as an economic model input. This matrix classifies the event itself
rather than the issuer's headline. It prevents five recurrent errors:

1. calling an order, award or capacity right recognised revenue;
2. using a consolidated margin as a CPO product margin;
3. treating a revenue target or earnout as an observed customer shipment;
4. treating a customer qualification as a supplier-content allocation; and
5. multiplying a product count by an unobserved price, share or yield and
   presenting the result as an estimate.

An event can improve the probability-weighted **timing watchlist** without
becoming an input to attributable revenue, gross profit, EPS or valuation.

## Event classification

| Event type | Current CPO example | What it legitimately establishes | What it may enter now | What it cannot enter | Minimum next record |
|---|---|---|---|---|---|
| Product catalogue / sample availability | Broadcom lists `BCM78919` as Limited Release; its launch release says early-access sampling (`CLM-077`, `CLM-530`) | Exact product boundary and lifecycle state | Commercial-timing watchlist; product denominator definition | Customer revenue, units, repeatability, ASP, margin or supplier share | Customer record with exact SKU, date and accepted count |
| Product/family production language | NVIDIA describes Spectrum-X Photonics as in/full production; Broadcom says the TH6 *family* is in production volume (`CLM-346`, `CLM-435`, `CLM-544`) | Vendor manufacturing/lifecycle claim at its stated family/product boundary | Production-readiness watchlist; source of follow-up questions | Exact customer CPO numerator, shipment scale, product margin or economics | Product-matched customer acceptance plus period/denominator |
| Customer/platform adoption statement | NVIDIA lists Spectrum-X Photonics adopters; CoreWeave identifies Spectrum-X platform use but no exact CPO SKU (`CLM-542`, `CLM-547`) | Customer relationship or platform use | Customer follow-up queue and architecture-boundary control | CPO deployment volume, system count, repeat shipments or CPO supplier economics | Customer names exact CPO SKU/configuration and accepted systems/ports |
| OEM integration / orderability | Dell and Supermicro list CPO models; Supermicro distinguishes `SN6800`/`SN6810` CPO from pluggable `SN6600` (`CLM-519`, `CLM-540`, `CLM-550`) | OEM route and exact architecture boundary | Product-boundary / false-positive control | Customer purchase, shipment, CPO revenue, service or margin | OEM/customer purchase or acceptance record with count/date |
| Partner demo or collaboration | Broadcom partner demos and Corning TH6 connectivity collaboration (`CLM-529`, `CLM-543`) | Engineering/integration route | Supplier-map route classification | Qualified share, supplied content, output, ASP, yield or warranty ownership | Supplier statement naming exact product, scope, qualification and commercial boundary |
| Award, booking or purchase commitment | Celestica's unnamed 2027 CPO program; Coherent/NVIDIA strategic commitment; Lumentum CPO/ELS order signals (`CLM-545`, `CLM-538`, `CLM-083`, `CLM-531`) | Commercial intent, capacity or conversion milestone at its disclosed scope | Dated order-conversion / capacity checkpoint; qualitative demand signal | Recognised revenue, systems, complete-engine content, margin, cancellation protection or supplier share unless explicitly disclosed | Named product/customer, amount or quantity, timing, revenue-recognition and product economics |
| Capacity or test-equipment expansion | Aehr follow-on SiPh burn-in order; TSMC COUPE production target (`CLM-549`, `CLM-213`–`CLM-216`) | Manufacturing capability or capacity-intent signal | Manufacturing diligence and capacity-ramp watchlist | Good-die output, final-engine yield, CPO demand, product cost or supplier margin | Qualified output/lot data: input, pass/fail, rework, output, customer and cost boundary |
| Acquisition consideration / revenue earnout | Marvell's Celestial acquisition and contingent revenue milestones (`CLM-093`, `CLM-095`) | Financial stake, management hurdle and prospective dilution mechanism | Transaction-risk and future milestone tracker | Current Photonic Fabric revenue, customer units, margin, yield, return on acquisition or EPS | Reported product revenue + customer/units + margin; then reconcile earnout separately |
| Consolidated filing or earnings result | Lumentum FY2026 results, Marvell Q1 FY2027, TSMC Q2 2026 (`CLM-531`, `CLM-096`, `CLM-278`) | Company-scale denominator, consolidated margin/cash-flow/capex context | Materiality screen and financial baseline | CPO/ELS/COUPE revenue, product margin, capex or warranty allocation | Product/segment disclosure sharing the same CPO boundary as the commercial record |
| Exact customer acceptance / repeat shipment | Not retained for target NVIDIA or Broadcom CPO SKUs | Customer-confirmed commercial numerator when the SKU, architecture, count and date align | System denominator and adoption/repeatability assessment | Supplier economics without a content/share boundary | Supplier/product record with exact content, share, price and cost boundary |
| Product-matched realised financial disclosure | Not retained for any priority company | Recognised CPO revenue, product price/margin and potentially capex/warranty boundary | Attributable revenue / gross-profit bridge, subject to all other gates | Broad valuation conclusion if yield, warranty, cannibalisation, shares or taxes are still missing | Complete matched economic bundle below |

## Current-event disposition by company

| Company | Best current commercial event | Proper status | Economic-input status | Why the distinction matters |
|---|---|---|---|---|
| NVIDIA | Defined `SN6800`/`SN6810` CPO products, first-party production route and named adopter ecosystem | Product/route evidence | **Blocked** | No adopter-to-exact-SKU acceptance, units, repeat shipment, allocation, price or product margin (`CLM-514`–`CLM-515`, `CLM-542`, `CLM-550`) |
| Broadcom | Defined `BCM78919` CPO switch, early-access sampling / Limited Release and partner route | Product/sampling evidence | **Blocked** | “Now shipping” cannot overrule the explicit sampling boundary or create an accepted customer denominator (`CLM-077`, `CLM-530`, `CLM-543`) |
| Coherent | NVIDIA strategic purchase/capacity commitment and broad CPO-capability route | Capacity/customer-route signal | **Blocked** | Agreement scope is advanced optics, not CPO product allocation, realised output, price, yield or margin (`CLM-197`, `CLM-538`) |
| Lumentum | Incremental CPO order and initial ELS-module order | Order-conversion signal | **Blocked** | Neither order identifies customer, product, quantity, revenue-recognition, content/share or margin (`CLM-083`, `CLM-531`) |
| Marvell | Completed Celestial acquisition, contingent revenue milestones and FY28/FY29 management targets | Transaction / forward-expectation signal | **Blocked** | An earnout and target establish incentives, not a production customer, recognised Photonic Fabric revenue or margin (`CLM-093`–`CLM-096`) |
| TSMC | COUPE 200G customer demonstrations and 2026 production target | Process/production-milestone signal | **Blocked** | Demonstration/engineering yield does not identify a complete-engine output, foundry/package revenue or product margin (`CLM-210`, `CLM-213`–`CLM-216`) |

## Minimum bundle for model promotion

Promote an event into the revenue bridge only when all applicable fields are
matched to one product boundary:

1. **Product:** exact SKU/configuration and domain (switch CPO, external light,
   engine/PIC, or accelerator optical I/O).
2. **Commercial denominator:** customer-accepted systems/ports/engines in a
   stated period, plus repeat shipment or a scenario probability explicitly
   labelled as an assumption.
3. **Supplier allocation:** physical content, qualified share, and whether the
   company sells the PIC, engine, laser, package, test service or platform.
4. **Revenue:** realised or contractually defined price/content and
   revenue-recognition boundary—not a total award, capacity commitment, TAM,
   earnout or annualised target.
5. **Cost:** product gross margin or its cost constituents, including yield,
   rework, test, warranty/service and cannibalisation.
6. **Return:** attributable R&D, capex, taxes and diluted shares for any EPS or
   cash-flow conclusion.

If one field is missing, the result may remain a *labelled sensitivity* but is
not a company base case. If the customer/SKU or allocation field is missing,
the revenue cell itself remains blank—not zero.

## Quarterly review protocol

For each new primary event:

1. Classify it using the table above before it enters a dossier or model.
2. Record its exact product and fiscal-period boundary.
3. Update the commercial-proof gate and supplier-map layer at the same time.
4. Promote only the inputs actually cleared; retain all others as blocked.
5. Reconcile a later financial disclosure against the original order/award;
   do not assume conversion because time has passed.

Related controls: [commercial-proof acquisition plan](../09-primary-research/commercial-proof-evidence-acquisition-plan-2026-08-13.md), [company economic-disclosure audit](../09-primary-research/company-economic-disclosure-audit-2026-08-11.md), [profit-pool input gates](optical-engine-profit-pool-input-gates.md), and [analyst scenario specification](analyst-variant/scenario-model-specification.md).
