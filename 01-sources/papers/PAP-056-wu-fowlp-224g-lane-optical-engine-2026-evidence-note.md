# PAP-056 — Wu et al., FOWLP 224G/lane optical engine

## Citation

Jia Qi Wu *et al.*, “Cost-Effective, High Performance Heterogeneous Integration for 6.4T and Beyond 224Gbps/lane Co-Packaged-Optical Engines for AI/ML & Data Center,” *Proceedings of SPIE* 13905 (2026), 139050H, DOI [10.1117/12.3085221](https://doi.org/10.1117/12.3085221).

## What was reviewed

The complete eight-page SPIE PDF was retrieved through university access, visually checked page by page, and retained locally on 2026-08-13.

## Full-paper evidence

- The authors present a fan-out wafer-level package (FOWLP) route for a 1.6-Tb/s 13 mm × 9.5 mm optical-engine package with a silicon-photonic PIC and four EICs. The paper reports a 224-Gb/s PAM4 eye after 21 receive-side FFE taps with 2.25 dB TDECQ.
- Nine packages were used for wafer-level optical checks across four vertical optical I/Os each. Except for one particle-affected coupler, the reported insertion losses were consistent; post-FOWLP fibre-to-edge optical-I/O coupling loss was below 2 dB per facet without index-matching epoxy. Daisy-chain tests found no open defects in the tested structures.
- The paper reports measured through-mould-via insertion loss of 0.18 dB and return loss of 17 dB at 28 GHz, and measured optical-engine-to-switch routing loss of 0.39 dB at 28 GHz and 0.62 dB at 56 GHz. The latter test produced a 112-Gb/s PAM4 eye with 1.62 dB TDECQ.
- The 1.6T package's warpage, solder-fatigue life and thermal behavior are simulations: 19.5 μm predicted warpage, predicted solder-joint fatigue life above 4,000 −40°C-to-125°C cycles, and simulated PIC temperature at or below 65°C under stated airflow/heatsink conditions. The 6.4T/12.8T route is likewise a modeled scale-up, not a fabricated 224G/lane full-engine demonstration.

## Evidence boundary

The authors call FOWLP lower cost than 2.5D/3D routes, but the paper does not supply a production cost model, lot-yield distribution, test seconds, rework rate, qualification population, field reliability, customer, shipment or gross-margin evidence. Treat the 1.6T package measurements as engineering evidence and the 6.4T/12.8T claims as design/simulation evidence. Claims are recorded as `CLM-578`–`CLM-581`.

## Research use

PAP-056 materially strengthens the FOWLP countercase: fibre/interface cleanliness, package routing and test structures can be measured in an advanced route. It does not show that FOWLP is the lowest-cost qualified good engine or that it captures the CPO profit pool.
