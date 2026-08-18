# Optical-engine profit-pool scenario bridge

**Status:** Auditable scenario template; illustrative sensitivities are not a forecast  
**Scope:** Scale-out switch CPO optical engines, 200G/lane and later 400G/lane  
**As of:** 2026-08-12

## Purpose

This bridge converts a defined system denominator into supplier revenue, gross profit and cash-return scenarios without treating a platform announcement as supplier revenue. It is deliberately separate from the [commercial-proof probability priors](commercial-proof-probability-priors.md): probability of proof is not adoption rate.

For a layer-by-layer sensitivity of PIC/engine, external laser, packaging/attach
and test/burn-in content, see the [private layer-level economics sensitivity](engine-layer-sensitivity-ranges.md). That companion is an assumption harness only; it does not populate this bridge with company inputs.

Apply the [profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md)
before changing any bridge variable. It defines the shared denominator and
prevents component layers from being counted again inside a complete-engine
content value.

## Formula

```text
Supplier revenue
= relevant systems
× architecture adoption rate
× engines per system
× supplier content per engine
× qualified supplier share

Supplier gross profit
= supplier revenue × realised product gross margin
− yield/rework cost
− warranty/support cost
− cannibalised legacy gross profit

Supplier operating profit
= supplier gross profit
− incremental R&D and qualification expense

Supplier cash return
= supplier operating profit
− attributable capacity, packaging and test capex
```

Every multiplier needs the same product boundary, year and domain. A 16-engine Broadcom TH6 architecture cannot be multiplied by a 32-engine NVIDIA reference architecture, and a Lumentum ELSFP cannot be treated as a complete Coherent optical engine.[CLM-076; CLM-235–CLM-237]

## Input ledger

| Variable | Unit | Evidence currently allowed in a base case | Current state |
|---|---|---|---|
| `S` relevant systems | systems/year | Customer or manufacturer denominator for a defined SKU/domain | Open |
| `A` adoption rate | % of `S` | Customer numerator and defined denominator, or separately labelled probability-weighted scenario | Open; no adoption share cleared |
| `E` engines/system | engines/system | Exact product architecture or teardown | 16 for Broadcom TH6 only; 32 for NVIDIA reference architecture; do not transfer between SKUs |
| `P` supplier content/engine | $/engine | Contract, realised product price or management disclosure | Open |
| `Q` qualified supplier share | % | Named qualification, repeat orders and second-source evidence | Open |
| `M` realised product gross margin | % | Product-level or directly comparable segment disclosure | Open |
| `Y` yield/rework cost | $/engine | Final-engine yield waterfall and rework data | Open; process examples are not production output |
| `W` warranty/support cost | $/engine | Field-return, replacement and service records | Open |
| `K` cannibalised legacy gross profit | $/engine | Product transition and displaced-content evidence | Open |
| `R` incremental R&D/qualification | $/year | Attributable company disclosure or primary research | Open |
| `C` attributable capex | $/year | Product-linked capacity/test/packaging investment | Open |

## Illustrative sensitivity (not a forecast)

The table below is an arithmetic stress test only. It uses **10,000 relevant systems/year**, **16 engines/system**, **$500 supplier content/engine**, **50% qualified supplier share**, **35% realised product margin**, **$25 yield/rework**, **$15 warranty/support** and **$10 cannibalised legacy gross profit** per supplied engine. None of these assumptions is an observed company input.

| Adoption rate | Supplier revenue | Gross profit before R&D/capex |
|---:|---:|---:|
| 1% | $0.4M | $0.1M |
| 5% | $2.0M | $0.5M |
| 10% | $4.0M | $1.0M |
| 25% | $10.0M | $2.5M |
| 50% | $20.0M | $5.0M |
| 100% | $40.0M | $10.0M |

Calculation: `10,000 × adoption × 16 × $500 × 50%` for revenue; gross profit is `revenue × 35% − supplied engines × ($25 + $15 + $10)`. Replace every illustrative input before using the bridge for a company or valuation decision.

## Bear / base / bull range block (scenario-only)

The following ranges are deliberately **Nur Alpys sensitivities**, not analyst estimates and not observations about any company. They are included to expose which unknowns drive the result. The example holds a defined 10,000 relevant-system denominator and 16 engines/system solely to make the arithmetic comparable; it does not assert that either NVIDIA or Broadcom has that annual volume or engine count.

| Input | Bear | Base | Bull | Status / boundary |
|---|---:|---:|---:|---|
| Defined systems/year (`S`) | 10,000 | 10,000 | 10,000 | Illustrative denominator; not a customer observation |
| CPO adoption (`A`) | 5% | 25% | 50% | Scenario only; no market share claim |
| Engines/system (`E`) | 16 | 16 | 16 | Broadcom TH6 architecture reference only; do not transfer to NVIDIA |
| Supplier content/engine (`P`) | $250 | $500 | $900 | Hypothetical eligible-layer content; not ASP |
| Qualified supplier share (`Q`) | 25% | 50% | 75% | Hypothetical; no qualification record |
| Product gross margin (`M`) | 15% | 35% | 50% | Hypothetical product margin; never consolidated margin |
| Yield/rework cost/engine (`Y`) | $50 | $25 | $10 | Hypothetical cost per supplied engine |
| Warranty/support cost/engine (`W`) | $30 | $15 | $8 | Hypothetical service burden |
| Cannibalised legacy GP/engine (`K`) | $25 | $10 | $5 | Hypothetical displaced-content burden |

| Output | Bear | Base | Bull |
|---|---:|---:|---:|
| Supplier revenue (`S × A × E × P × Q`) | $0.5M | $10.0M | $54.0M |
| Supplied engines (`S × A × E × Q`) | 2,000 | 20,000 | 60,000 |
| Gross profit after `M`, `Y`, `W`, `K` | **−$0.135M** | **$2.5M** | **$25.62M** |

Calculation control: revenue is `S × A × E × P × Q`; gross profit is `revenue × M − supplied engines × (Y + W + K)`. The negative bear result demonstrates how low share, low margin and service/yield burden can erase apparent content economics. R&D, qualification expense and capex are excluded from this gross-profit output and must be subtracted separately in the operating-profit/cash bridge.

**Interpretation boundary:** this range block does not identify a likely case, assign a company, imply a market-size forecast, or establish a CPO profit-pool leader. It is a sensitivity harness to be replaced only when the evidence-gate register clears the corresponding denominator, content/share, margin, yield, warranty and cannibalization fields.

## What the sensitivity demonstrates

1. System adoption alone does not determine the profit pool; supplier share and content per engine are equally important.
2. A supplier can have a large technical role but low profit if the platform owner or contract manufacturer captures the engine price.
3. Yield, warranty and cannibalisation can erase a seemingly attractive product margin.
4. Capex and R&D affect cash return, not the gross-profit line; they must be modelled separately.
5. A $40M annual supplier-revenue result is materially different for Lumentum or Coherent than for Broadcom or NVIDIA, so the earnings-materiality screen must remain company-specific.[CLM-070; CLM-073; CLM-087; CLM-088]

## Six-company model-entry matrix

This is a control table, not an estimate table. **Blocked** means the value
cannot enter a company base case; it is not a zero. “Partial” identifies a
technical or reported-company denominator that still cannot be multiplied into
CPO revenue or profit.

| Company | Product / technical denominator | Customer-volume denominator | Content / share | Product margin | Yield / warranty | Attributable capex / R&D | Model-entry status |
|---|---|---|---|---|---|---|---|
| NVIDIA | Partial: defined CPO SKU and disclosed architecture | Blocked | Blocked | Blocked | Blocked | Blocked | **Blocked** |
| Broadcom | Partial: BCM78919 and 16-engine architecture | Blocked | Blocked | Blocked | Blocked | Blocked | **Blocked** |
| Coherent | Partial: CPO engine demonstrations and company capacity route | Blocked | Blocked | Blocked | Blocked | Blocked | **Blocked** |
| Lumentum | Partial: ELSFP/UHP laser route and customer-unallocated order signals | Blocked | Blocked | Blocked | Blocked | Blocked | **Blocked** |
| Marvell | Partial: accelerator optical-I/O chiplet route, outside switch-CPO boundary | Blocked | Blocked | Blocked | Blocked | Blocked | **Blocked** |
| TSMC | Partial: COUPE process/integration route | Blocked | Blocked | Blocked | Blocked | Blocked | **Blocked** |

The detailed evidence and boundaries behind this table are in the
[six-company content-attribution register](../07-companies/six-company-content-attribution-register.md)
and the [profit-pool input gates](optical-engine-profit-pool-input-gates.md).
No partial technical denominator can be paired with an invented content, share,
margin, yield, warranty, or capital input.

## Evidence replacement queue

Replace the illustrative values in this order:

1. Exact customer SKU and annual systems/ports (`S`).
2. Exact engine count and architecture boundary (`E`).
3. Supplier qualification and repeat-share evidence (`Q`).
4. Realised engine or module price and supplier content (`P`).
5. Final-engine yield, rework, field-return and service cost (`Y`, `W`).
6. Displaced legacy content and price-down terms (`K`).
7. Attributable R&D, qualification spend and capacity/test capex (`R`, `C`).

Until steps 1–7 are evidenced, the bridge is a reusable calculation framework, not an investment conclusion. Current source records specifically leave these inputs open for Broadcom, NVIDIA, Coherent and Lumentum.[CLM-435–CLM-437]

**Capacity control:** a large capacity contract or customer prepayment is not
an engine-revenue input unless the disclosure allocates it to the relevant CPO
product and supplier layer. Tower's disclosed silicon-photonics contracts span
pluggable, NPO and CPO applications, illustrating why it remains outside this
bridge.[CLM-534]

## Linked controls

- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md)
- [Coherent versus Lumentum matched engine bridge](coherent-lumentum-matched-engine-profit-bridge.md)
- [CPO content-attribution map](cpo-content-attribution-map.md)
- [CPO earnings-materiality screen](cpo-earnings-materiality-screen.md)
- [Commercial-proof probability priors](commercial-proof-probability-priors.md)
