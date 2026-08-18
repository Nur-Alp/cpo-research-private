# Profit-pool arithmetic audit — 12 August 2026

**Status:** Private model-control document; no public release
**Purpose:** Verify that the layer sensitivity and supplier bridge use consistent denominators and do not double-count yield, share or service burdens.

## Reconciliation result

The prior layer-sensitivity scaffold charged warranty and cannibalisation to
all good engines while the controlling supplier bridge charged them to
qualified supplier units. That was an ambiguity in the economic boundary. It is
now corrected: supplier-level outputs charge the burden to **attributable
supplied engines = good engines × qualified supplier share**.

On 13 August 2026, a separate regression check also found that the
whole-engine bear/base/bull table had reported supplied-engine counts that were
ten times too low relative to its own `S × A × E × Q` formula. The table now
reports 2,000 / 20,000 / 60,000 supplied engines and the resulting gross profit
of −$0.135M / $2.5M / $25.62M. This is a correction to an illustrative
assumption harness, not a change to any company evidence, forecast or
investment conclusion.

## Controlled identities

```text
attempted engines = S × A × E
good engines      = attempted engines × good-engine yield
supplied engines  = good engines × Q
supplier revenue  = supplied engines × P
supplier gross profit = supplier revenue × M
                    − supplied engines × (Y + W + K)
supplier operating profit = supplier gross profit − R
supplier cash return     = supplier operating profit − C
```

`Y` must represent a cost still borne per supplied engine. If yield loss has
already been reflected in the good-engine yield, do not subtract the same scrap
cost again. If `Y` represents incremental rework/support after acceptance, its
definition must say so explicitly and retain a source or assumption status.

## Two valid but non-interchangeable views

| View | Burden denominator | Use | Current status |
|---|---|---|---|
| Supplier economics | Supplied engines (`good × Q`) | Company-level revenue, gross profit and cash bridge | Controlling view; illustrative only |
| Ecosystem economics | All good engines | Total value-chain cost or architecture TCO | Optional sensitivity; must not be called supplier profit |

The current private company bridge uses the first view. The layer-sensitivity
table now uses the first view as well. No company-specific input is populated.

## Numerical check of the corrected layer sensitivity

| Case | Good engines | Qualified share | Supplied engines | Layer revenue | Gross profit after burden |
|---|---:|---:|---:|---:|---:|
| Bear | 5,600 | 25% | 1,400 | $0.630M | −$0.0035M |
| Base | 34,000 | 50% | 17,000 | $17.425M | $5.504M |
| Bull | 76,000 | 75% | 57,000 | $108.300M | $53.295M |

These are arithmetic outputs from labelled assumptions, not observations or
forecasts. They are retained to make denominator choices auditable.

## Release control

- No value in this audit is a company input.
- No architecture engine count is a volume denominator.
- No consolidated margin is a product margin.
- No yield, warranty, ASP, share or capex value is observed until the relevant
  product-matched gate clears.
- The conclusion remains **no proven CPO profit-pool leader**.

Related controls: [profit-pool input reconciliation](profit-pool-input-reconciliation-2026-08-12.md), [scenario bridge](profit-pool-scenario-bridge.md), [layer sensitivity](engine-layer-sensitivity-ranges.md), and [optical-engine input gates](optical-engine-profit-pool-input-gates.md).

The automated control is [validate-profit-pool-sensitivity.py](../scripts/validate-profit-pool-sensitivity.py). It independently recomputes both scenario tables and asserts their anti-double-counting and assumption-boundary language.
