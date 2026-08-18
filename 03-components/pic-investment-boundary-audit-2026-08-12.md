# PIC investment-boundary audit — 12 August 2026

**Status:** Private control document; no public-release approval
**Purpose:** Audit whether the PIC scorecard can support an investment conclusion without converting device or prototype evidence into a supplier or profit-pool ranking.
**Decision boundary:** A customer-accepted, serviceable 200G/lane scale-out optical engine. 400G/lane evidence is retained as an architecture countercase, not silently substituted for the 200G/lane boundary.

## Audit verdict

The scorecard is decision-useful for technology diligence, but it does **not** clear an investment ranking for any PIC route or company. The strongest current result is a process-control hypothesis: silicon photonics with external light is the most product-relevant switch-CPO route at 200G/lane. That is an architecture/process observation, not evidence that a silicon-photonics, laser, packaging or platform supplier captures the profit pool.

The scorecard also correctly preserves InP and TFLN as modular countercases at the 400G/lane boundary. Heterogeneous integration is treated as an integration and test architecture rather than a standalone material category. No route has a retained record that simultaneously proves the target lane boundary, full power, final-good-engine yield, qualification, serviceability, customer acceptance and attributable economics.

## Evidence maturity ladder

Every technology claim should be assigned the highest rung actually supported by the retained source. A lower rung must not be promoted because a related company announcement uses stronger language.

| Rung | Evidence state | What it can support | What it cannot support |
|---|---|---|---|
| 1 | Device measurement | Modulator, receiver, laser or coupling feasibility | Complete engine power, production yield or company economics |
| 2 | Subassembly/prototype engine | Multi-channel or packaging integration at a stated test boundary | Customer qualification, HVM yield, service cost or profit attribution |
| 3 | Process and test flow | Possible known-good-die, attach, screening or rework mechanism | Accepted-unit denominator, repeat shipments or supplier share |
| 4 | Qualified production engine | Product-matched performance, environmental and reliability evidence | Profit capture unless price, share, yield and cost are known |
| 5 | Commercially attributable engine | Customer acceptance, volume/repeatability and supplier economics | A durable profit-pool conclusion if pricing and competitive substitution remain open |

Current retained PIC records are mostly rungs 1–3. The exact NVIDIA and Broadcom CPO packets provide product-route evidence, but do not promote any PIC supplier to rung 4 or 5.

## Route audit

| Route | Device result | Engine/process result | Missing promotion evidence | Permitted investment use |
|---|---|---|---|---|
| Silicon photonics + external laser | Relevant 200G/lane product and process architecture; external-light and screening records | Fibre attach, interface testing and known-good-engine concepts; no final good-engine denominator | Exact-SKU PIC/laser allocation, delivered power, final yield/rework, qualification, accepted volume, realised share and margin | Primary switch-CPO diligence route; use as a process-control hypothesis only |
| InP | Monolithic 200G-class transmitter and 400G-class modular transmission evidence | Partial integration concepts; no matched serviceable engine | Complete multi-channel power/link boundary, package/attach, production yield, qualification and customer economics | Serious modular countercase; pressure-test CPO substitution and cost |
| Thin-film lithium niobate | 225GBd/400G-class transmission result | No retained production engine, package or service flow | Full module/chassis boundary, manufacturing yield, qualification and customer adoption | High-rate modular countercase; may narrow CPO’s addressable market |
| Heterogeneous / 2.5D integration | Aggregate engine and interposer demonstrations across multiple material routes | Wafer/interposer, FOWLP, TGV and test-before-final-assembly mechanisms | One matched product architecture, thermal path, final-good-engine yield, ownership, price and supplier economics | Potential integration/test control point; never score as a material winner by itself |

## Missing fields that must be closed before ranking

The current documents cover most conceptual fields. The following remain genuinely open and are the next evidence requests:

1. **Product match:** PIC, EIC, laser and package identity for the exact NVIDIA SN6800/SN6810 and Broadcom BCM78919 boundary.
2. **Power completeness:** laser source, splitter/coupling loss, receiver/TIA, tuning/control, host SerDes and chassis boundary under one protocol.
3. **Yield waterfall:** wafer-tested dies → assembled engines → final-test pass → rework → accepted/shipped units, with denominators.
4. **Service boundary:** replaceable laser versus replaceable engine, field procedure, MTTR, spare burden, warranty and failure-domain data.
5. **Economic attribution:** transfer price/ASP, qualified supplier share, price-down, rework/warranty burden, capex and product gross margin.
6. **Alternative comparison:** matched 200G/400G system evidence against retimed pluggables, LPO and NPO at the same reach, thermal and service boundary.

Until these fields are populated, any company-specific PIC call must remain `Watch/neutral`, `process-control hypothesis`, or `countercase`, with no CPO-specific EPS or margin contribution treated as observed.

## Anti-overclaim checks

- Do not compare a component pJ/bit number with complete-engine power.
- Do not treat 400G/lane laboratory transmission as proof of 200G/lane CPO adoption.
- Do not treat a broad partnership, capacity reservation or manufacturing announcement as exact-SKU supplier allocation.
- Do not infer final-engine yield from interface yield, engineering-sample stacking yield or test-vehicle reliability.
- Do not infer profit capture from technical indispensability; qualified alternatives, price-down and warranty can reverse the economics.

## Links to controlling records

- [PIC technology decision scorecard](pic-technology-decision-scorecard.md)
- [PIC-to-engine investment gates](pic-to-engine-investment-gates-2026-08-12.md)
- [Common-boundary architecture evidence audit](../02-architecture/common-boundary-evidence-audit-2026-08-12.md)
- [Manufacturing production handoff](../09-primary-research/manufacturing-production-handoff-2026-08-12.md)
- [Supplier attribution audit](../08-model/supplier-attribution-audit-2026-08-12.md)
- [Public release manifest](../00-scope/public-release-manifest-2026-08-12.md)

**Release decision:** retain as private evidence-system control. Do not publish the route table as a company ranking until the missing promotion evidence is independently retained and reconciled.
