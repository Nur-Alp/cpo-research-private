# Estimates-to-variant reconciliation — 12 August 2026

**Status:** Private control ledger; no public target price or CPO EPS call
**Scope:** NVIDIA, Broadcom, Coherent, Lumentum, Marvell and TSMC

## Purpose

This control prevents consolidated analyst expectations from being mistaken
for CPO evidence. An external estimate can describe what the market may expect,
but it cannot create customer units, supplier share, ASP, yield, warranty or
product margin that the public record does not disclose.

## Four-layer separation

| Layer | Permitted contents | Current use |
|---|---|---|
| Observed fact | Filing, customer acceptance, exact product, shipment, qualification or reported financial result | Can support a factual claim only at its stated boundary |
| External expectation | Analyst estimate, management target or consultant forecast with source/date/unit | Documents the expectation; does not become fact |
| Nur Alpys assumption | Explicit bear/base/bull input used to test sensitivity | Scenario only; never presented as consensus or observation |
| Variant conclusion | Evidence-adjusted positive/neutral/negative view with catalyst and falsification | Relative stance only until all financial gates clear |

## Company reconciliation

| Company | Current baseline state | Fiscal/currency/share control | CPO boundary | Missing expectation-to-CPO bridge | Variant status |
|---|---|---|---|---|---|
| NVIDIA | Reported/public-consensus scale only | NVIDIA fiscal year retained; diluted shares, estimate date and valuation basis require reconciliation | `SN6810-LD`/`SN6800-LD` defined; customer acceptance open | No CPO revenue, supplier content, product margin, yield or CPO allocation | Positive strategic timing exposure; CPO EPS not eligible |
| Broadcom | Reported/public-consensus scale only | Broadcom fiscal year and AI-semiconductor baseline must remain separate from CPO; share/valuation basis pending | `BCM78919`/TH6-Davisson defined; customer acceptance open | Family production language cannot supply CPO units, content, margin or share | Positive enabling exposure; CPO EPS not eligible |
| Coherent | Reported/public-consensus scale only | Fiscal-year and non-GAAP basis require row-level reconciliation | SiPh/InP/engine routes, no allocated CPO SKU | SAM, capacity or NVIDIA agreement cannot supply CPO revenue or margin | Constructive component exposure; CPO EPS not eligible |
| Lumentum | Reported/public-consensus scale plus disclosed order expectation | Fiscal-year, order timing, share count and currency basis require reconciliation | ELSFP/UHP route; order product/customer/quantity open | Order magnitude cannot be allocated to CPO modules, supplier share or margin | Constructive/watch; CPO EPS not eligible |
| Marvell | Reported/public-consensus scale plus management Photonic Fabric targets | Fiscal-year and non-GAAP EPS basis require reconciliation; acquisition/earnout framing separate | Accelerator optical-I/O, not switch CPO | Revenue targets cannot supply production units, content, yield or margin | Strategic watch; CPO EPS not eligible |
| TSMC | Reported/public-consensus scale in TWD/ADR context | TWD/USD, ADR ratio, fiscal year, shares and valuation basis unresolved | COUPE process/integration route; complete-engine output open | Process milestones and engineering yield cannot supply CPO revenue or margin | Manufacturing-control watch; CPO EPS not eligible |

## Hard release gates

No analyst estimate may enter a company CPO bridge until every applicable
field below is present in the estimate register and the product evidence gates
are separately cleared:

1. source ID, firm/private identifier, report date and as-of date;
2. exact company fiscal period, accounting basis, currency and unit;
3. diluted share, ADR/split and valuation treatment where relevant;
4. exact CPO product/domain and denominator;
5. customer acceptance, repeatability and supplier qualification;
6. supplier content/share, realised ASP and product gross margin;
7. final-engine/module yield, rework, warranty and attributable R&D/capex;
8. public-use status and a derived-range method that does not expose restricted material.

If any gate is missing, the output is `not eligible`, not zero. Consolidated
revenue or margin may be retained as a scale denominator but cannot be relabelled
as CPO economics.

## Variant-writing template

Every company update should answer:

```text
What consensus/management appears to expect:
What is actually observed:
Where Nur Alpys differs and why:
CPO financial variable affected (or “not eligible”):
Catalyst that would upgrade the view:
Evidence that would falsify it:
Source IDs, claim IDs and as-of date:
```

## Current decision

The estimates layer is useful for framing expectations, but no company has a
publicly reconciled CPO numerator and economic chain. The current relative
stances therefore remain evidence-gated and qualitative. Do not publish exact
analyst values, company CPO EPS sensitivities or valuation impacts until the
commercial and product-economics gates clear.

Related controls: [analyst-estimate register](../analyst-estimate-register.md), [scenario model specification](scenario-model-specification.md), [quarterly refresh checklist](quarterly-refresh-checklist.md), [six-company commercial-proof queue](../../07-companies/six-company-commercial-proof-queue-2026-08-12.md), and [profit-pool input reconciliation](../profit-pool-input-reconciliation-2026-08-12.md).
