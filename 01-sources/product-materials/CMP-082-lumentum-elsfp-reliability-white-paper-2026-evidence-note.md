# CMP-082 — Lumentum ELSFP reliability white paper (2026)

**Canonical source:** https://www.lumentum.com/sites/default/files/2026-06/elsfpreliability-wp-cl-ae.pdf  
**Publisher:** Lumentum Operations LLC  
**Document date:** March 2026 (document code `30179750 000 0326`)  
**Reviewed:** 13 August 2026  
**Retained file:** `CMP-082-lumentum-elsfp-reliability-white-paper-2026.pdf` (four pages)

## What the document directly reports

- Lumentum says its CPO-targeted UHP laser accelerated-life programme used
  thousands of production devices from multiple fabrication runs, automated
  production lines and standard burn-in procedures.
- It reports more than **100 million accelerated device-hours** under elevated
  temperature/current stress, with **zero reported catastrophic failures**.
- The document translates its accelerated-test calculation to 9 FIT at 60%
  confidence and 23 FIT at 90% confidence, and says Lumentum rates UHP lasers
  at **20 FIT for 400 mW operation**.
- It describes process transfer from Lumentum's Raman-pump manufacturing,
  including die bonding, thermal management, burn-in and quality-control
  methods. It also states a Raman-pump heritage record of nearly half a million
  deployed pumps and over 20 billion device-hours; this is an adjacent product
  heritage statement, not an observation of CPO-laser field performance.

## Allowed use

This is a **company-reported component-level qualification and manufacturing
signal** for Lumentum's external-light route. It makes the external-laser
reliability case more concrete than a product data-sheet claim and establishes
a diligence boundary for accelerated-device hours, confidence level, power and
the distinction between device and module reliability.

## Explicit non-uses

Do **not** use this source as evidence of:

- CPO switch deployment, customer acceptance, port count, repeat shipment or
  named platform allocation;
- a finished ELSFP module's reliability, because the document gives no module
  configuration, laser count, optical splitter/distribution, connector or
  module field-return population;
- a complete optical-engine, fibre-attach, package or switch reliability result;
- realised lifetime, field FIT, warranty cost, MTTR, unit volume, ASP, gross
  margin, supplier share or CPO profit-pool leadership;
- the paper's cited market forecasts, power/TCO comparisons, claimed CPO
  deployments or broad resiliency claims. Those have separate sources and
  boundaries and were not independently validated here.

## Model treatment

`R_laser` can be described qualitatively as a stronger **component-level
qualification signal** for Lumentum. It remains blocked as a monetary warranty
input: no matching module/system field population, service-cost distribution,
or supplier-specific price/margin record is supplied. `Y_laser`, ELSFP module
yield, engine yield, warranty reserve and gross margin remain unpopulated.

Claims recorded: `CLM-553`–`CLM-555`.
