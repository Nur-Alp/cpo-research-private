# Fibre-count and first-pass-yield sensitivity

**Owner:** Nur Alpys  
**Status:** Arithmetic sensitivity; not an observed production forecast  
**Scope:** CPO/optical-engine assembly with multiple fibre connections  
**Last updated:** 2026-08-09

## Purpose

This table translates the OIF co-packaging example into a reusable model control. It isolates one question: how quickly does board-level first-pass fibre-assembly yield fall as fibre count increases, holding every connection statistically independent and identically distributed?

The calculation is:

```text
Y_board = y_connection ^ N_connections
```

It excludes package, die, laser, electrical, test, rework and customer-acceptance yields. Therefore it is a lower-level sensitivity, not the cost-per-good-engine result.

The imec development-run measurements add a physical interface example: reported yield changed from 57% to 75.5% as the edge-vertical-coupler length increased from 0.5 mm to 1.5 mm, with lateral misalignment and voids identified as loss mechanisms (`PAP-043`, `CLM-421`–`CLM-423`). These percentages are not substituted for the board-level connection-yield assumption below.

## Calculated board fibre-assembly yield (%)

| Assumed per-connection first-pass yield | 288 connections | 512 connections | 1,024 connections | 1,088 connections |
|---:|---:|---:|---:|---:|
| 99.500% | 23.6% | 7.7% | 0.6% | 0.4% |
| 99.800% | 56.2% | 35.9% | 12.9% | 11.3% |
| 99.865% (OIF 3-sigma assumption) | 67.8% | 50.1% | 25.1% | 23.0% |
| 99.900% | 75.0% | 59.9% | 35.9% | 33.7% |
| 99.950% | 86.6% | 77.4% | 59.9% | 58.0% |

The 288- and 1,088-connection columns reproduce the OIF panel's approximately 67.8% and 23.0% examples at the 99.865% assumption (`STD-014`, `CLM-398`). The intermediate columns are new arithmetic sensitivities, not OIF measurements.

## Per-connection yield needed for a target board yield

| Connections | For 90% board yield | For 95% board yield | For 99% board yield |
|---:|---:|---:|---:|
| 288 | 99.9634% | 99.9822% | 99.9965% |
| 512 | 99.9794% | 99.9900% | 99.9980% |
| 1,024 | 99.9897% | 99.9950% | 99.9990% |
| 1,088 | 99.9903% | 99.9953% | 99.9991% |

## Interpretation for the architecture comparison

- A low-fibre architecture can have a materially higher first-pass assembly yield at the same per-connection process quality.
- Reducing fibre count is not automatically beneficial: it may trade against optical loss, splitter loss, laser redundancy, bandwidth density, serviceability or the number of external components. Those trade-offs must be modeled separately.
- A CPO design with many direct fibre connections needs either extremely high per-connection yield, substantial rework recovery, or a pre-tested/detachable subassembly boundary to avoid a severe yield penalty.
- The table does not prove that NPO, ELSFP or pluggables are economically superior. It identifies a falsifiable production gate that each architecture must clear.

## Required production evidence

Replace this sensitivity with measured values when available:

1. connection count and exact connector/fibre architecture;
2. per-connection first-pass yield distribution and process capability;
3. correlation between connection failures and board/package failures;
4. rework recovery, cycle time and scrap cost;
5. complete-engine final acceptance yield after optical/electrical test and qualification.

**Sources:** [OIF panel evidence note](../01-sources/standards/STD-014-oif-co-packaging-panel-2023-evidence-note.md); [manufacturing cost-per-good-engine gate](manufacturing-cost-per-good-engine-gate.md).
