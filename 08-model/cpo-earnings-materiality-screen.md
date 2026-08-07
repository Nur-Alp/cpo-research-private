# CPO Earnings-Materiality Screen

**Owner:** Nur Alpys
**Status:** Revenue-scale screen; not a CPO revenue forecast, valuation or recommendation
**Last updated:** 2026-08-07

## Purpose

This screen answers a narrow but essential investment question:

> How large would identifiable CPO revenue have to become before it can plausibly matter to each company’s reported quarterly scale?

It does **not** estimate CPO revenue, gross margin, operating profit, cash flow, stock value or an investment return. No company currently discloses the CPO-specific inputs needed for those conclusions.[CLM-084]

## Baseline financial scale

Use the most recent reviewed quarterly disclosure for each company. These figures are denominators only. They must not be treated as CPO business results or applied as a CPO margin proxy.

| Company | Reporting period | Reported revenue | Other relevant disclosed metric | CPO disclosure boundary | Evidence |
|---|---|---:|---|---|---|
| Broadcom | Q2 FY26, ended 2026-05-03 | $22.187B | $10.8B AI-semiconductor revenue; $10.262B free cash flow | No CPO revenue, content, margin or capex line | [CLM-087] |
| NVIDIA | Q1 FY27, ended 2026-04-26 | $81.615B | $75.178B Data Center revenue; 74.9% GAAP gross margin | No CPO revenue, content, margin or capex line | [CLM-088] |
| Coherent | Q3 FY26 | $1.806B | 37.7% GAAP gross margin | No CPO revenue/content/margin line | [CLM-070] |
| Lumentum | Q3 FY26 | $808.4M | 44.2% GAAP gross margin; total-company customer concentration disclosed | No CPO revenue/content/margin line | [CLM-073] |
| Marvell | Q1 FY27 | $2.418B | 52.1% GAAP gross margin; Celestial results included from acquisition date | No Photonic Fabric/Celestial revenue/content/margin line | [CLM-096] |
| Celestica | Q1 2026, ended 2026-03-31 | $4.047B | Approximately $1.7B HPS revenue; 6.7% GAAP operating margin | CPO hyperscaler program disclosed, but no CPO revenue/content/margin line | [CLM-263]–[CLM-264] |
| TSMC | Q2 2026, ended 2026-06-30 | $40.20B | 67.7% gross margin; 77% of wafer revenue from 7nm-and-more-advanced technologies | No COUPE/CPO revenue, content, margin or capex line | [CLM-278]–[CLM-281] |

The periods are not synchronized. This is acceptable for a first **scale** screen but not for valuation, growth comparisons or margin ranking.

### Newly retained primary-financial packet

The four local filing records now preserve the full SEC HTML and an evidence note: [Coherent FIL-002](../01-sources/filings/FIL-002-coherent-q3-fy2026-evidence-note.md), [Lumentum FIL-003](../01-sources/filings/FIL-003-lumentum-q3-fy2026-evidence-note.md), [Broadcom FIL-004](../01-sources/filings/FIL-004-broadcom-q2-fy2026-evidence-note.md), and [NVIDIA FIL-005](../01-sources/filings/FIL-005-nvidia-q1-fy2027-evidence-note.md). These records improve denominator, utilization, mix, capex and concentration context; none reports CPO-specific ASP, margin, content, units or yield.[CLM-335][CLM-344]

## Quarterly revenue thresholds

The table calculates a purely arithmetic threshold:

```text
Illustrative CPO revenue threshold
= reported quarterly revenue x materiality percentage
```

| Company | 0.5% of reported quarterly revenue | 1% | 5% | 10% | Interpretation |
|---|---:|---:|---:|---:|---|
| Broadcom | $110.9M | $221.9M | $1.109B | $2.219B | CPO must be extremely large before it is a material consolidated revenue driver. |
| NVIDIA | $408.1M | $816.2M | $4.081B | $8.162B | CPO is likely immaterial at the consolidated-company level for a long time; Data Center is a more relevant but still very large denominator. |
| Coherent | $9.0M | $18.1M | $90.3M | $180.6M | A successful CPO/engine program could become revenue-material at a much lower absolute level. |
| Lumentum | $4.0M | $8.1M | $40.4M | $80.8M | The disclosed order signal may matter sooner than it would to platform owners, but its product allocation and margin remain unknown. |
| Marvell | $12.1M | $24.2M | $120.9M | $241.8M | Management's Celestial targets, if achieved, would be revenue-material; achievement and margin are unproven. |
| Celestica | $20.2M | $40.5M | $202.4M | $404.7M | The planned CPO program could become visible at the HPS/company level only after units, revenue recognition and program margin are disclosed; thresholds are arithmetic denominators, not forecasts. |
| TSMC | $201.0M | $402.0M | $2.010B | $4.020B | COUPE/CPO would need very large attributable revenue to move consolidated TSMC results; the company-scale margin is not a CPO margin proxy. |

These calculations do not mean a threshold is reached, contracted, profitable, incremental or valuation-relevant. They simply prevent the common error of treating the same CPO revenue figure as equally material to a $0.8B quarterly company and an $81.6B quarterly company.

## No gross-profit shortcut

Do **not** multiply the revenue thresholds by the reported consolidated margins. Broadcom’s free cash flow, NVIDIA’s gross margin, Coherent’s gross margin and Lumentum’s gross margin include many products other than CPO.[CLM-070][CLM-073][CLM-087][CLM-088]

A CPO gross-profit bridge needs:

```text
CPO revenue
x CPO-specific realised gross margin
- yield/rework cost
- warranty/support cost
- cannibalised legacy gross profit
```

Then an operating/cash-return bridge needs incremental R&D, qualification cost and attributable capacity/test capital expenditure. See [Optical-Engine Profit-Pool Input Gates](optical-engine-profit-pool-input-gates.md).

## Company-specific interpretation

### Broadcom and NVIDIA

Their platform roles may capture substantial *system* value, but reported consolidated scale means that a technical CPO win can still be financially immaterial. Any equity case must isolate incremental networking/CPO revenue, displaced alternatives, CPO cost and the investor expectation already embedded in AI-networking growth.[CLM-082][CLM-087][CLM-088]

### Coherent and Lumentum

Their smaller reported revenue bases make a defined external optical-engine or external-laser program potentially more earnings-material. That is not proof that they capture the profit pool: final-engine content, customer identity, yield, price, warranty and CPO margin are all still unknown.[CLM-074][CLM-075][CLM-083]

### Marvell / Celestial AI

Marvell's current denominator is between the focused optical suppliers and platform owners. Its announced $500M and $1B annualized Photonic Fabric targets would be material if achieved, but they are management forecasts tied to an acquisition/earnout case rather than reported revenue.[CLM-095][CLM-096] See the [Marvell / Celestial accelerator optical-I/O dossier](../07-companies/marvell-celestial-accelerator-optical-io-dossier.md).

### Celestica

Celestica's Q1 2026 HPS revenue is a much smaller denominator than NVIDIA's or Broadcom's, so a successful CPO system-manufacturing program could become visible sooner. The release does not identify CPO revenue, retained content, program margin, units, capex or warranty cost, and HPS is broader than CPO.[CLM-255][CLM-263][CLM-264] The arithmetic thresholds must therefore remain a screening device, not an earnings estimate.

## Required next records before a valuation overlay

1. A CPO revenue line, product-content map or contract evidence linking CPO units to an attributable supplier.
2. CPO-specific or clearly comparable segment gross margin and the cost of yield, rework, warranty and support.
3. Cannibalisation of pluggable modules, DSP, retimers, cables or other legacy content.
4. Capacity and test capital required for incremental CPO volume.
5. Dated sell-side consensus estimates, valuation, share count and market price from an auditable source, with the as-of date preserved.

Until then, a claim that CPO is “material” to a company or already reflected in a stock price is not evidence-backed.

## References

- [Claim ledger](../01-sources/claim-ledger.csv), CLM-070, CLM-073 through CLM-075, CLM-082 through CLM-084, CLM-087, CLM-088 and CLM-263–CLM-264.
- [Company leadership source manifest](../01-sources/company-leadership-source-manifest.md), FIL-002 through FIL-005.
- [Optical-Engine Profit-Pool Input Gates](optical-engine-profit-pool-input-gates.md).
