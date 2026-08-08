# Customer scale and CPO repeatability gate

**Owner:** Nur Alpys
**Status:** Analytical control; not a CPO shipment estimate
**As of:** 2026-08-08

## Why this gate exists

Large AI-cloud expansion can make a CPO claim sound commercially important even when the public record contains no CPO unit denominator. The research therefore separates:

1. **Operator scale:** data centers, power, backlog, GPU clusters and contract expansion.
2. **Platform deployment:** a named switch or photonics platform is deployed.
3. **CPO attribution:** the deployed SKU is explicitly identified as CPO and its optical boundary is known.
4. **Repeatability:** units, dates and repeat shipments or expansions are disclosed.
5. **Profit-pool attribution:** engine/PIC/laser/attach responsibility, price, yield, warranty and margin are known.

Only levels 3–5 can support the optical-engine profit-pool model. Levels 1–2 are necessary context but cannot supply the CPO numerator.

## Current evidence ladder

| Level | Current evidence | What can be inferred | What remains unavailable |
|---|---|---|---|
| Operator scale | CoreWeave reports $66.8B backlog, 43 active data centers, >850 MW active power and >3.1 GW contracted power in its March 2026 presentation [CLM-376–CLM-377]. | CoreWeave is a sufficiently large operator for a repeat-deployment claim to become economically meaningful. | CPO-specific share of the buildout, switch count and optical-engine units. |
| Platform deployment | CoreWeave describes SN6600-LD deployment and early Photonics CPO adoption [CLM-220–CLM-223; CLM-320; CLM-370]. | A named customer-side deployment and operating boundary exist. | Whether every described SN6600 unit is CPO, exact revision, units and repeat shipments. |
| CPO attribution | NVIDIA states Spectrum-X Ethernet Photonics is a 200G-SerDes CPO switch in production [CLM-346]. Lambda describes Quantum-X Photonics in a 10,000+ GPU production-scale cluster [CLM-224]. | CPO has first-party production and customer-side scale-up evidence in separate domains. | A reconciled SKU-to-engine BOM, supplier allocation and customer CPO unit count. |
| Repeatability | No retained source currently discloses a dated CPO unit count plus an expansion, renewal or repeat shipment. | Repeatability is an explicit open diligence item, not a hidden assumption. | Numerator, denominator, field population, failure distribution and replacement flow. |
| Profit-pool attribution | NVIDIA lists ecosystem partners; POET, Coherent and Lumentum disclose manufacturing or component routes [CLM-229; CLM-360–CLM-369]. | Candidate supply routes can be mapped. | Qualified share, engine ASP, yield/rework, warranty burden and realised gross margin. |

## Required evidence before calling a deployment repeatable

The minimum record must contain the exact product/revision, a qualification or acceptance date, a unit/port/system count over a defined period, and a repeat shipment, expansion or renewal. The record must also identify the network position and whether the CPO claim covers the same physical boundary as the count. A customer statement that merely names a platform or a cloud provider's total power capacity fails this gate.

## Consequence for the investment case

CoreWeave's scale increases the value of finding a real CPO numerator; it does not create one. Until that numerator is disclosed, the defensible conclusion is that NVIDIA has the strongest named switch-side route, while the optical-engine profit pool remains unallocated among NVIDIA, Coherent, Lumentum, foundry, OSAT and system partners.

## Linked controls

- [Customer proof register](customer-proof-register.md)
- [CPO earnings-materiality screen](cpo-earnings-materiality-screen.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
