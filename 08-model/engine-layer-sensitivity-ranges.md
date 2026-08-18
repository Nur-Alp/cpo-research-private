# Private layer-level CPO economics sensitivity

**Status:** Private scenario scaffold; not an observed market estimate or company forecast  
**Owner:** Nur Alpys  
**As of:** 2026-08-12  
**Scope:** One qualified 6.4-Tb/s-class optical-engine boundary (32 × 200G lanes), with a separate external-light and service boundary

Use the [profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md) as the single control ledger for layer boundaries, status labels and overlap prevention.

## Why this layer exists

The existing profit bridge correctly leaves company inputs blocked, but a
single “content per engine” number can hide where economics actually accrue.
This table decomposes the eligible bill of material into four layers:

1. PIC/optical-engine design and assembly;
2. external laser / ELSFP source;
3. fibre attach, connector, interposer and package; and
4. optical/electrical test, burn-in and qualification.

The ranges below are deliberately wide **Nur Alpys assumptions**. They are not
analyst estimates, supplier quotes, observed ASPs, or evidence for NVIDIA,
Broadcom, Coherent, Lumentum, TSMC, Marvell or any other company. They exist to
show sensitivity and to define the evidence required before a number can enter
the investment model.

## Illustrative eligible-content ranges per qualified engine

| Layer | Bear | Base | Bull | Unit boundary | What the range is testing | Evidence still required |
|---|---:|---:|---:|---|---|---|
| PIC / optical-engine design and assembly | $250 | $500 | $900 | Revenue retained by one qualified engine supplier | Whether the supplier sells a PIC, an assembled engine, or a higher-value integrated optical subassembly | Exact product BOM, transfer price, qualified share, final-engine yield and product margin |
| External laser / ELSFP source | $100 | $250 | $500 | Separate source/module content; exclude PIC and package value | Whether light-source value is centralised, shared across engines, or embedded in the engine | Exact laser count, source boundary, customer/SKU allocation, realised price, lifetime and warranty |
| Fibre attach / connector / interposer / package | $75 | $200 | $350 | Physical attach and package value only; no PIC or laser double count | Whether attach and package control creates scarce, qualified content or remains contract-manufacturing pass-through | Named OSAT/attach role, cycle time, first-pass yield, rework, loss distribution and margin |
| Test / burn-in / qualification | $25 | $75 | $150 | Test and qualification service/content per accepted engine | Whether test insertion and late-defect discovery support pricing power or merely add cost | Test seconds, coverage, escape rate, installed utilisation, burn-in burden and warranty allocation |
| **Total eligible layers** | **$450** | **$1,025** | **$1,900** | Sum of the four non-overlapping boundaries | Sensitivity to the location of value capture | Product-matched price/share/margin evidence for every layer |

The total is an arithmetic sum of non-overlapping hypothetical boundaries. It is
not an engine ASP and must not be multiplied by a company’s system volume.
Where a supplier sells a complete engine, the four rows must be consolidated
to avoid counting the same PIC, laser, package or test value twice.

## Qualified-share and good-engine sensitivity

The following normalized case shows how the same eligible content can produce
very different attributable revenue and gross profit. The denominator is a
**hypothetical 10,000 relevant systems/year**, with **16 engines/system** only
to make the arithmetic visible. It is not a NVIDIA, Broadcom or market-volume
claim.

| Variable | Bear | Base | Bull | Classification |
|---|---:|---:|---:|---|
| Relevant systems/year | 10,000 | 10,000 | 10,000 | Nur Alpys denominator assumption |
| CPO adoption | 5% | 25% | 50% | Scenario assumption; not market share |
| Engines/system | 16 | 16 | 16 | Broadcom TH6 architecture reference only; not transferable to NVIDIA |
| Total eligible layers/engine | $450 | $1,025 | $1,900 | Sum above; not an observed ASP |
| Qualified supplier share | 25% | 50% | 75% | Scenario assumption; no qualification record |
| Good-engine yield | 70% | 85% | 95% | Scenario assumption; not production yield |
| Product gross margin before support | 15% | 35% | 50% | Scenario assumption; never consolidated margin |
| Warranty/support burden per good engine | $40 | $20 | $10 | Scenario assumption; no field-return data |
| Cannibalised legacy gross profit per good engine | $30 | $15 | $5 | Scenario assumption; no transition disclosure |

### Calculation

```text
attempted engines
  = systems × adoption × engines/system

good engines
  = attempted engines × good-engine yield

attributable layer revenue
  = good engines × eligible layers/engine × qualified supplier share

gross profit after burden
  = attributable layer revenue × product gross margin
    − attributable supplied engines × (warranty/support + cannibalised legacy GP)
```

| Output | Bear | Base | Bull |
|---|---:|---:|---:|
| Attempted engines | 8,000 | 40,000 | 80,000 |
| Good engines | 5,600 | 34,000 | 76,000 |
| Attributable supplied engines (`good × qualified share`) | 1,400 | 17,000 | 57,000 |
| Attributable layer revenue | $0.63M | $17.43M | $108.30M |
| Gross profit after support/cannibalisation | **−$0.0035M** | **$5.504M** | **$53.295M** |

These outputs are deliberately not assigned to a company. They demonstrate
that the main profit-pool variables are not merely adoption: eligible-layer
content, qualified share, good-engine yield, product margin and the burden of
service/cannibalisation all interact. The burden is charged to attributable
supplied engines, matching the controlling supplier bridge. If the research
question is instead total ecosystem economics, charge the burden to all good
engines and label that output separately; do not mix the two denominators. The
bull case is not a forecast; it is a stress point that requires every gate to
clear.

## What this model may and may not do

**Permitted:**

- compare which missing input has the greatest effect on attributable profit;
- test whether a component-only supplier can be economically material without
  owning a complete engine;
- separate external-light economics from PIC/engine economics;
- design primary-research questions and evidence requests.

**Prohibited:**

- assigning a range to a named company without product-linked evidence;
- treating a public company’s consolidated margin as layer margin;
- multiplying by NVIDIA/Broadcom announced architecture counts to infer revenue;
- using these ranges as consensus, market size, adoption or valuation forecasts;
- publishing the layer values as factual claims.

## Evidence replacement order

Replace assumptions only in this order:

1. exact SKU and customer/system denominator;
2. engine count and service boundary;
3. product-linked BOM and qualified supplier share;
4. realised transfer price or ASP;
5. stage yields, rework and test/burn-in cost;
6. warranty, replacement and cannibalisation burden;
7. product gross margin and attributable capex/R&D.

Until those records exist, the only defensible conclusion remains **no proven
CPO profit-pool leader**. See [optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md), [profit-pool scenario bridge](profit-pool-scenario-bridge.md), and [manufacturing cost per qualified good engine](manufacturing-cost-per-good-engine-gate.md).
