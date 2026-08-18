# Public CPO evidence extraction pack

**Status:** Private, public-only research workflow; no publication, forecast or claim clearance  
**As of:** 2026-08-13  
**Use:** Search narrowly for records that can move a defined gate. Save only permitted, readable originals and create an evidence note before a decision changes.

## Common operating rules

1. Search the exact product label first; do not start with “CPO market.”
2. Record the source date, canonical URL, exact wording, product boundary and denominator.
3. A proxy, patent, standard, job post or equipment order can refine a diligence question. It cannot prove shipment, yield, customer acceptance, revenue or margin.
4. Use lawful public import/shipping records only where access and terms permit; treat consignee/product descriptions as leads until independently confirmed.
5. An earnings-call statement is management commentary unless it gives a product-matched numerator or economics boundary.

## Gate-by-gate search cards

| Gate | Exact terms to combine | First public locations | Accept only if | Non-qualifier |
|---|---|---|---|---|
| NVIDIA customer/units/repeat | `"SN6810-LD"`, `"SN6800-LD"`, `"Spectrum-X Ethernet Photonics"` + `deploy*`, `accepted`, `qualification`, `shipment`, `ports`, `expansion` | NVIDIA/Dell/Supermicro; CoreWeave, Lambda, Meta, Microsoft, OCI engineering sites; earnings releases/transcripts; OCP/OFC decks | Exact Ethernet CPO SKU/configuration + named operator + date + systems/ports; second event for repetition | Spectrum-X generally, Quantum-X, SN6600-LD, benchmark, product listing |
| Broadcom customer/units/repeat | `"BCM78919"`, `"TH6-Davisson"`, `"Davisson"` + same commercial terms | Broadcom; HPE, Celestica, Micas, Nexthop, Alpha/DNI; OCP/OFC decks; calls/filings | Exact CPO part/configuration + customer/integrator + dated denominator; second event for repetition | Tomahawk 6 family, 1.6T platform, demo, Limited Release, samples |
| Supplier content/share | Exact SKU + `BOM`, `qualified`, `supplier`, `optical engine`, `EIC`, `laser`, `ELSFP`, `fibre attach`, `assembly`, `test` | Platform/supplier pages; OSAT/connector/test-vendor case studies; conference decks; patents | Who does what for the exact product; share only when explicitly stated | Ecosystem lists, MoUs, compatibility and capacity statements |
| Yield/rework/test | Exact product/layer + `yield`, `first pass`, `rework`, `scrap`, `Cpk`, `test time`, `burn-in`, `escape`, `qualification` | ECTC/OFC/IEEE papers; equipment-customer case studies; OSAT presentations; quality reports | Process-step denominator through accepted output and rework disposition | Best channel, interface yield, equipment capability or engineering sample alone |
| Service/warranty | Exact SKU + `RMA`, `failure rate`, `MTTR`, `field return`, `warranty`, `spares`, `replacement` | OEM manuals/support; operator reliability posts; qualification reports; filings | Population/time period + replacement scope and service boundary | Warranty policy or replaceable laser alone |
| Price/margin/capex | Exact product/layer + `ASP`, `price`, `backlog`, `gross margin`, `warranty reserve`, `capex`, `capacity`, `utilisation` | 10-Q/10-K/20-F; earnings decks/transcripts; contract announcements; lawful analyst excerpts | Product-matched allocation and accounting period | Company/segment margin, SAM, generic AI-optics growth |
| Alternatives | `LPO`, `RTLR`, `NPO`, `OBO`, `400G/lane`, `224G`, `400G` + `BER`, `FEC`, `power`, `thermal`, `qualification`, `service` | OIF/IEEE; OFC/ECOC/ECTC papers/decks; customer/OEM qualification sources | Same ASIC/ports/lane/reach/FEC/cooling/service boundary | Component pJ/bit or different lane generation |

## Source route checklist

| Source class | What to extract | Search route |
|---|---|---|
| Filings | Customer concentration, capex, warranty/reserves, capacity, product terms and explicit CPO/ELS/SiPh keywords | SEC EDGAR / company IR / TSMC IR; use document search across CPO synonyms |
| Earnings calls | Customer/product names, conversion timing, order/backlog, utilisation, margin and cancellation language | Official transcript/presentation first; otherwise lawful transcript source; retain speaker and date |
| Conference decks | Product label, system topology, supplier role, test/qualification and production language | OCP, OFC, ECOC, ECTC, IEEE; preserve page/slide number |
| Product manuals | Exact interface, optics boundary, repair/FRU, cooling and warranty constraints | Official support/docs portals; compare configuration labels carefully |
| Patents | Intended architecture: fibre attach, external laser, package, test and service design | Google Patents, USPTO Patent Center, WIPO Patentscope; search assignee plus technical feature |
| Standards | Interface, management, interoperability and service assumptions | OIF, IEEE 802.3, OCP; use final/implementation-agreement status versus draft/contribution |
| Lawful trade records | Possible supply-chain lead and timing | Licensed/public customs databases only; independently corroborate before any claim |
| Hiring | Skills/capacity direction: test, reliability, OSAT, fibre attach | Official careers pages / archived postings; record location and job scope | 

## Intake result labels

`Gate evidence`, `partial boundary`, `proxy`, `architecture/standards context`,
`false-positive control`, and `no decision change` are the only permitted
labels. The label determines whether the result reaches the source log/claim
ledger or stays in a retrieval log.

Related controls: [commercial-proof acquisition plan](commercial-proof-evidence-acquisition-plan-2026-08-13.md), [decision-changing evidence queue](decision-changing-evidence-acquisition-queue.md), and [quarterly evidence register](quarterly-evidence-change-register-2026-08-12.md).
