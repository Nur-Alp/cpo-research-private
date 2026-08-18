# Switch-CPO commercial-proof decision memo

**Status:** Private working memo; not cleared for publication or investment use  
**As of:** 2026-08-12  
**Question:** Has either announced 200G/lane switch-CPO route crossed into a named, accepted and repeatable customer deployment with an attributable supplier/economic chain?

## Decision in one page

**Current answer: no public record clears the full commercial-proof gate for either NVIDIA Spectrum-X Ethernet Photonics or Broadcom TH6-Davisson.** NVIDIA has the stronger integrated production/manufacturing narrative; Broadcom has the clearest merchant-switch CPO product definition. Neither has a reconciled same-SKU customer numerator or profit-pool evidence.

| Gate | NVIDIA Spectrum-X Ethernet Photonics | Broadcom TH6-Davisson |
|---|---|---|
| Exact CPO SKU | **Cleared:** `SN6810` / `SN6800`; matching `SN6810-LD` / `SN6800-LD` ordering-family labels | **Cleared:** `BCM78919`, 102.4T TH6-Davisson |
| Exact customer tied to exact CPO SKU | **Open:** named adopters are not tied to an accepted exact Ethernet CPO SKU; CoreWeave’s named `SN6600-LD` record is pluggable | **Open:** early-access customers/partners and HPE/Celestica/Micas/Nexthop routes are not an accepted TH6 customer record |
| Acceptance / qualification date | **Open** | **Open** |
| Units / ports / systems | **Open** | **Open** |
| Repeat shipment / expansion | **Open** | **Open** |
| Field service / reliability | **Partial procedure only:** Dell policy and NVIDIA liquid-cooling handling instructions are not observed fleet data | **Open:** historical TH5 results and ELSFP design are not TH6 field data |
| Supplier-content chain | **Partial route map:** TSMC, SPIL, TFC and Foxconn roles disclosed; EIC, exact engine allocation and shares open | **Partial route map:** Broadcom engine/SerDes boundary, TSMC COUPE route and Corning connectivity collaboration; package, test, supplier share open |
| Economics | **Blocked:** ASP, yield/rework, warranty, product margin and CPO allocation undisclosed | **Blocked:** ASP, yield/rework, warranty, product margin and CPO allocation undisclosed |
| Current decision | Positive strategic timing exposure, not proven volume or profit leadership | Positive enabling exposure, not proven volume or profit leadership |

## What would change the decision

Upgrade either route only when one evidence bundle identifies the exact CPO SKU, named customer/operator, acceptance or qualification date, dated accepted units/ports/systems, and a repeat shipment/expansion. Upgrade a supplier or profit-pool view only after the same product boundary also identifies PIC/engine, EIC, laser, fibre attach, package, connector and test responsibility together with supplier share, ASP, qualified yield/rework, warranty and realised margin.

Downgrade the 2026–27 timing view if customer deployments remain evaluation-only, if the product boundary proves to be pluggable/LPO/NPO rather than CPO, if service or yield forces modular replacement, or if alternatives meet the same system requirement at lower qualified cost.

## Two-page commercial-proof cards

The cards below are the release-control version of the full dossiers. “Open”
means the field was searched and not cleared by a product-matched public
record; it does not mean zero.

### NVIDIA Spectrum-X Ethernet Photonics

| Required answer | Current evidence-adjusted answer | Evidence grade |
|---|---|---|
| **SKU** | `SN6810` (102.4T) and `SN6800` (409.6T), with `SN6810-LD`/`SN6800-LD` as corresponding CPO ordering-family labels; Dell lists both as MMC-12 CPO products. | **High — product boundary** |
| **Named customer** | NVIDIA names CoreWeave, Lambda, Meta, Microsoft and OCI as Spectrum-X Photonics adopters, and Lambda says it is preparing Spectrum-X Ethernet integration. No source maps an adopter to an exact Ethernet CPO SKU. | **High — adopter; exact SKU open** |
| **Accepted units / ports** | No public exact-SKU accepted-unit, port, system or dated installed-base denominator. CoreWeave's 8,192-GPU Spectrum-X benchmark is platform-level and architecture-ambiguous; its named SN6600-LD deployment is pluggable. | **Open** |
| **Repeat shipment** | No second dated delivery, expansion, renewal or repeat fleet record for `SN6800`/`SN6810-LD`. | **Open** |
| **Supplier content** | TSMC (silicon photonics), SPIL (package/assembly/test), TFC (laser-module packaging/validation) and Foxconn (system assembly) are disclosed route roles; Lumentum/SENKO/Coherent provide broader family-level signals. Exact SKU share and EIC/engine allocation remain open. | **Medium — route, not BOM** |
| **Disconfirming evidence** | An exact customer record showing the benchmark/deployment used pluggable optics, or evidence that `SN6800`/`SN6810-LD` remains evaluation-only, would weaken the timing call. A qualified production lot with repeat delivery would upgrade it. | **Falsification condition defined** |

**Current card conclusion:** NVIDIA has the strongest first-party production,
manufacturing-route and named-adopter signal. The appropriate stance is
**positive strategic timing exposure, commercial numerator open**—not proven
Ethernet CPO volume leadership or profit-pool leadership.

### Broadcom TH6-Davisson

| Required answer | Current evidence-adjusted answer | Evidence grade |
|---|---|---|
| **SKU** | `BCM78919` / TH6-Davisson: 102.4T, 16 × 6.4T Davisson optical engines, 200G/link, field-replaceable ELSFP modules. Broadcom's live catalogue still says **Limited Release**. | **High — product boundary** |
| **Named customer** | Broadcom names HPE, Celestica, Micas and Nexthop as collaborators/route partners; its OCP material names demonstrations, not an accepting end customer. Celestica separately discloses an unnamed hyperscaler CPO award. | **Medium — route; exact customer open** |
| **Accepted units / ports** | No public `BCM78919` customer acceptance, units, ports, systems, qualification lot or dated installed-base denominator. | **Open** |
| **Repeat shipment** | No second dated delivery, expansion, renewal or repeat TH6 CPO fleet record. Family-level Tomahawk 6 production-volume language is not a CPO-specific numerator. | **Open** |
| **Supplier content** | Broadcom owns the switch/SerDes and specifies the engine boundary; Corning discloses TH6 faceplate-to-chip collaboration; TSMC and historical Micas routes inform the ecosystem. Complete PIC/EIC/laser/attach/package/test allocation and share remain open. | **Medium — partial route** |
| **Disconfirming evidence** | Continued Limited Release/early access without a named CPO customer, or a TH6 deployment that uses copper/pluggable optics, would weaken the 200G CPO timing call. An exact `BCM78919` acceptance and repeat shipment would upgrade it. | **Falsification condition defined** |

**Current card conclusion:** Broadcom has the clearest merchant-switch CPO
architecture and prior-generation process learning, but the current public
record does not prove TH6 CPO volume, repeatability, service economics or a
profit-pool leader. The appropriate stance is **positive enabling exposure,
commercial numerator open**.

### Gate interpretation

The two cards deliberately separate product maturity from commercial proof:

```text
exact SKU → named customer → accepted denominator → repeat delivery
→ service/qualification → attributable supplier economics
```

Neither route currently clears the chain. The report may publish a timing
view only as an evidence-gated inference, not as a verified market-share or
profit forecast.

## Evidence boundary

The [six-company commercial-proof queue](../six-company-commercial-proof-queue-2026-08-12.md) extends these switch-platform cards into a standardized next-evidence queue for Coherent, Lumentum, Marvell and TSMC. It does not relax the exact-SKU customer or economic gates.

- Full [NVIDIA dossier](nvidia-spectrum-x-photonics.md)
- Full [Broadcom dossier](broadcom-th6-davisson.md)
- [Exact-SKU customer search audit](../../09-primary-research/sku-customer-search-audit-2026-08-11.md)
- [Exact-SKU evidence-gate matrix](../../08-model/evidence-gate-register.md)
- [SKU content reconciliation](../../08-model/switch-cpo-sku-content-reconciliation.md)
- [Supplier-attribution audit](../../08-model/supplier-attribution-audit-2026-08-12.md)

This memo intentionally does not convert vendor production language, OEM orderability, “Limited Release,” sampling, historical CPO field shipments, partner quotations, or a different CPO domain into customer volume. It contains no CPO revenue, EPS, valuation or target-price estimate.
