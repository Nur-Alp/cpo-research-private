# NWS-003 — Practical Optical Communication Systems

- Publisher: Irrational Analysis
- Publication date: 2025-11-07
- Canonical source: <https://irrationalanalysis.substack.com/p/practical-optical-communication-systems>
- Local retention: publisher hyperlink retained; no PDF snapshot was necessary because this is a secondary, continuously available newsletter source.
- Review date: 2026-08-07
- Evidence class: secondary technical explainer / diligence-question generator

## Why it is retained

This post is a practical orientation document for the scale-out optical-engine workstream. It organizes the engineering problem around tuning, filter periodicity, modulator/driver/TIA co-design, reliability, electronics integration, photonic design kits, simulation, and test equipment. Those topics map directly to the project’s optical-engine benchmark and yield waterfall.

## Evidence that can be used

The article is useful for identifying what must be measured before treating a PIC or optical engine as qualification-ready:

1. Photonic tuning and thermal crosstalk should be treated as yield and control-loop questions, not merely as a device-performance question.
2. Driver and TIA boundaries affect power, noise, packaging, and interoperability; they must be included in any engine-level comparison.
3. GR-468 and long-duration optical reliability qualification are explicit diligence gates for a production optical product.
4. The electronics-integration choice (flip-chip PIC/EIC, monolithic integration, or hybrid bonding) creates cost, cycle-time, yield, and thermal trade-offs that belong in the profit-pool model.

These are architecture prompts and evidence requirements, not independently measured results from this newsletter.

## Claims deliberately not accepted as facts

The post contains author forecasts and opinions about 2026 NVIDIA/Broadcom CPO shipment quantities, company leadership, 200G-per-lane VCSEL viability, InP wafer yield, TSMC COUPE economics, and supplier capacity. None is entered as verified product, customer, yield, margin, or market-share evidence without a retained primary source. The article also cites standards and a Microsoft MOSAIC paper; those are tracked separately in the repository and should be evaluated from the original documents.

## Research actions created

- Add tuning-loop stability, thermal crosstalk, driver/TIA partition, GR-468 status, and EDA/test coverage as explicit rows in company and engine diligence.
- Recover primary reliability and production evidence before scoring any 2026 CPO shipment or margin claim.
- Keep modulation technology comparisons tied to matched lane rate, reach, BER/FEC, temperature, package, and service boundaries.

