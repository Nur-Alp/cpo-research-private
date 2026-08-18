# Production-record intake schema — 13 August 2026

**Status:** Private evidence-control template; not a yield or economics model  
**Scope:** PICs, optical engines, external-light modules, CPO packages, fibre attach, test, burn-in and field service

## Use rule

Use this template for every claimed production, yield, qualification, shipment,
reliability, warranty or manufacturing-economics record. It is deliberately
stricter than a source note: a disclosure is not eligible for a company model
input until the relevant fields below are filled from a product-matched source.
Blank fields are evidence gaps, not zero values.

## Required metadata

| Field | Required capture |
|---|---|
| Source ID and canonical link | Retained source, publisher, date and access date |
| Product boundary | Exact SKU/revision; lane rate; engine/module/package direction; what is included/excluded |
| Physical stage | Wafer/die screen, attach, package, final test, burn-in, customer acceptance or field service |
| Manufacturing location and period | Site, line, lot/date/quarter and whether engineering, qualification, pilot or volume production |
| Counterparty | Customer, supplier, OSAT, test provider or operator; record `unnamed` explicitly if not disclosed |
| Evidence class | Customer acceptance, supplier production record, qualification report, field-service report, product claim, research vehicle or supplier capability |

## Stage record

| Item | Required value | Reject as insufficient when |
|---|---|---|
| Numerator | Passes, failures, recoveries, returns, shipments or accepted units | It says only “high yield,” “production ready,” “shipping” or “100%” |
| Denominator | Starts, attempts, tested units, installed-base exposure or submitted units | The unit, population, sampling method or time period is omitted |
| Conditions | Test limits, temperature, reflow/stress, line rate, reach, optical budget and relevant handling boundary | A best-channel/device result is presented as a full-engine result |
| Failure disposition | Scrap, rework, retest, replacement, return-to-vendor or no-fault-found; separate late escapes | Recovery is silently folded into first-pass yield |
| Time | Cycle time, burn-in duration, exposure hours, deployment period and any ageing window | A one-time demonstration has no period or usage definition |
| Cost boundary | Labour/equipment, materials, test/burn-in, rework/scrap, warranty and capex scope | Consolidated company margin or generic equipment capacity substitutes for product cost |

## Model eligibility by stage

| Model input | Minimum accepted record | Do not use |
|---|---|---|
| `Y_die`, `Y_laser`, `Y_screen` | Product/lot starts, screened count, pass/fail, escape definition and date/site | A process demonstration or test-equipment order |
| `Y_attach`, `R_rework`, `C_attach` | Attach attempts, first-pass passes, recoveries, scrap, fibre/FAU count and cycle time | Fibre count, coupling loss or alignment capability alone |
| `Y_pkg` | Package starts, thermal/reflow route, failures, accepted packages and site/lot | Prototype failure analysis without a matched production denominator |
| `Y_test`, `C_test` | Final-test count, limits, seconds, coverage, retest/escape rules and output | ATE/wafer-probe capability without installed-product throughput |
| `Y_accept` | Customer-submitted and customer-accepted units on an exact product/date boundary | Vendor “in production” language or a partner demonstration |
| `W`, MTTR, service reserve | Installed base, period/exposure, returns/failure modes, repair/replacement path and warranty ownership | Warranty policy, detachable interface or lab reliability alone |
| `P`, `Q`, `M`, `C`, `R` | Product-matched contract/filing or attributable supplier record containing price/share, product margin and capex/R&D boundary | Company-wide gross margin, capacity agreement or nonexclusive ecosystem partnership |

## Fast rejection checklist

Reject the item as a model input—and retain it only as a technical or diligence
lead—if any answer is “no”:

1. Is the exact product/revision and physical layer clear?
2. Does the record state a numerator and denominator?
3. Does it provide a date/lot/site or field-exposure period?
4. Are conditions and pass/fail/rework/escape dispositions known?
5. Is the claimed output tied to customer acceptance or a defined production stage?
6. Does the economic record align price, share, yield, warranty and margin to that same boundary?

## Current application

- NVIDIA’s known-good screening language, Broadcom’s historical lab-device-hour
  result, TSMC’s engineering-sample stacking yield, research test vehicles and
  test/burn-in equipment orders do **not** fill this schema at a production
  product boundary.
- Aehr’s `CMP-080` follow-on production burn-in order fills a manufacturing
  demand/capacity direction field but not the customer, SKU, wafer-start,
  pass/fail, throughput, output or cost fields. It remains manufacturing-scale
  evidence, not a yield or CPO-economics input.

Related controls: [manufacturing production-evidence checklist](manufacturing-production-evidence-checklist.md), [manufacturing-to-model handoff](manufacturing-production-handoff-2026-08-12.md), [manufacturing proof matrix](../08-model/manufacturing-proof-matrix.md), [yield waterfall template](../08-model/engine-yield-waterfall-template.md), and [profit-pool input reconciliation](../08-model/profit-pool-input-reconciliation-2026-08-12.md).
