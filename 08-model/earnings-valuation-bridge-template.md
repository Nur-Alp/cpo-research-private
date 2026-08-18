# CPO earnings and valuation bridge template

**Status:** Evidence-gated template; restricted analyst-baseline layer created, no company forecast populated  
**Scope:** Broadcom, NVIDIA, Coherent, Lumentum, Marvell, Celestica and TSMC CPO/optical-engine exposure  
**As of:** 2026-08-09

## Purpose

This template connects an evidence-supported optical-engine scenario to company earnings and valuation without applying consolidated margins to CPO revenue. It is a bridge, not a target price.

## Required bridge

```text
attributable CPO revenue
= systems × adoption × engines/system × supplier content/engine × qualified share

incremental gross profit
= attributable CPO revenue × product gross margin
 − yield/rework cost
 − warranty/support cost
 − cannibalised legacy gross profit

incremental operating profit
= incremental gross profit
 − incremental R&D
 − qualification expense

incremental net income
= incremental operating profit × (1 − effective tax rate)
 − incremental interest / other attributable costs

incremental EPS
= incremental net income / diluted shares

valuation sensitivity
= incremental EPS × selected valuation multiple
```

The valuation sensitivity is the change attributable to the CPO scenario, not a claim that the whole company deserves the selected multiple.

## Scenario input table

| Input | Bear | Base | Bull | Evidence required before population |
|---|---:|---:|---:|---|
| Defined systems/year | — | — | — | Customer/manufacturer denominator for an exact SKU/domain |
| CPO adoption rate | — | — | — | Customer numerator and denominator, or labelled probability-weighted scenario |
| Engines/system | — | — | — | Exact product architecture; do not transfer TH6 and Spectrum-X counts |
| Supplier content/engine | — | — | — | Contract, product price or management disclosure |
| Qualified supplier share | — | — | — | Named qualification, repeat shipments and second-source status |
| Product gross margin | — | — | — | Product-level or directly comparable margin |
| Yield/rework cost | — | — | — | Final-engine yield waterfall and rework data |
| Warranty/support cost | — | — | — | Field returns, MTTR, spare policy and warranty allocation |
| Cannibalised legacy gross profit | — | — | — | Displaced pluggable/DSP/retimer/AEC content and price bridge |
| Incremental R&D/qualification | — | — | — | Attributable company disclosure or primary research |
| Effective tax rate | — | — | — | Company filing or scenario assumption, stated separately |
| Diluted shares | — | — | — | Latest filing, including ADR/share-class treatment |
| Valuation multiple | — | — | — | Dated market data and selected comparable methodology |

## Company boundary table

| Company | CPO/engine revenue line | Product margin | Supplier content/share | Cannibalisation | Capex/R&D | Valuation overlay status |
|---|---|---|---|---|---|---|
| Broadcom | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |
| NVIDIA | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |
| Coherent | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |
| Lumentum | Not disclosed; order signal only | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |
| Marvell | Not disclosed; management Photonic Fabric targets only | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |
| Celestica | Not disclosed; planned hyperscaler CPO program | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |
| TSMC | Not disclosed; COUPE milestone only | Not disclosed | Not disclosed | Not disclosed | Not attributable | Not eligible |

## Interpretation controls

1. A management SAM or order headline is not attributable revenue.
2. A consolidated gross margin is not a CPO product margin.
3. A capacity investment is not CPO capex unless product allocation is documented.
4. Supplier content cannot be counted simultaneously at the PIC, engine, module and platform layers.
5. A platform owner's CPO revenue may be system rent, while an optical supplier's revenue may be component content; compare only like-for-like boundaries.
6. If the CPO scenario is immaterial to consolidated earnings, that does not mean the supplier economics are unattractive; it means the equity sensitivity belongs at a different denominator.

## Required outputs once gates clear

For each company and bear/base/bull case, report:

- Revenue and year of recognition
- Gross profit and product margin
- Cannibalised gross profit
- Operating profit and incremental EPS
- Capex and cash-return effect
- Valuation sensitivity under at least two multiples
- Downside if the milestone slips, is multisourced or converts at lower margin
- Source IDs, claim IDs and evidence-quality label for every non-assumption input

Until the [optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md) clear, the correct result is **not eligible**, not zero and not a hidden assumption.

## Analyst-baseline integration

The bridge now receives restricted baseline inputs only through [the analyst-estimate register](analyst-estimate-register.md). For each company, record the latest eligible consensus revenue, margin, EPS, capex, diluted shares and valuation multiple alongside the source IDs and as-of date. Keep that baseline separate from the CPO overlay in [the analyst scenario model](analyst-variant/scenario-model-specification.md).

The permitted output before CPO-specific inputs clear is a **relative CPO sensitivity**: a labelled bear/base/bull overlay against the analyst baseline. It is not a standalone target price, and no baseline value may appear in public material unless its publication status allows it.

## Linked controls

- [Profit-pool scenario bridge](profit-pool-scenario-bridge.md)
- [CPO earnings-materiality screen](cpo-earnings-materiality-screen.md)
- [Expectations and variant-perception tracker](expectations-and-variant-perception-tracker.md)
- [Market snapshot](market-snapshot-2026-08-07.md)
- [Decision-output completion audit](decision-output-completion-audit.md)
