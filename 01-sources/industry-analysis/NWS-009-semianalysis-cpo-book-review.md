# NWS-009 — SemiAnalysis CPO Book: Scaling with Light

- Publisher: SemiAnalysis
- Publication date: 2026-01-01 (page date)
- Canonical source: <https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling>
- Local retention: canonical hyperlink retained; no PDF snapshot was created because this is a paid secondary industry analysis and the underlying primary sources are the evidence of record.
- Review date: 2026-08-07
- Evidence class: secondary industry analysis / TCO and supply-chain hypothesis source

## Why it is retained

This is a broad industry map covering scale-out and scale-up CPO, DSP/LPO/NPO/CPO comparisons, TSMC COUPE, fibre attach, couplers, modulators, products, and the NVIDIA supply chain. It is especially valuable for the current thesis because it makes the economic boundary explicit: optical-engine and external-laser cost, supplier margin stacking, serviceability, reliability, and customer bargaining power can determine adoption even when component power is attractive.

## Evidence that can be used

The analysis supports these bounded working hypotheses:

1. First-wave scale-out CPO may have limited adoption if TCO, serviceability, reliability, and vendor bargaining power do not compensate for the deployment change.
2. Scale-up CPO has a stronger strategic case because copper reach and bandwidth scaling constrain the size of the accelerator “world,” while optical engines can enable larger domains.
3. CPO power and TCO must be modeled at the complete system boundary. Optical-engine/ELS savings can be diluted by supplier margins, fibre/FAU/shuffle components, cooling, service, and the switch vendor’s margin stack.
4. External-light-source architecture improves serviceability but introduces connector/fibre/coupling loss and high laser/TEC power; integrated-laser and ELS routes require a matched reliability and cost comparison.
5. MRM, MZM, EAM, grating-coupler, and edge-coupler comparisons must include full PIC/EIC area, thermal control, coupling loss, WDM, yield, and qualification—not isolated device metrics.

## Quantitative claims retained as estimates only

The article gives illustrative scenarios such as roughly 4–5 W per 800G for an optical engine plus ELS versus roughly 16–17 W for a DSP transceiver, and a modeled CPO network-cost advantage that can shrink after margin stacking. These are secondary estimates with assumptions and are not merged into the repository’s measured or scenario power model without a matched boundary. The article also cites Meta/Broadcom reliability results; those remain bounded by NWS-002 and require the original primary presentation and test definition.

## Claims deliberately not accepted as facts

The article’s Celestial revenue forecast, supplier commitments, named NVIDIA supply-chain assignments, exact product costs, adoption timing, and company rankings are secondary or company-derived claims. They are not treated as customer deployment, production yield, ASP, margin, or market-share evidence.

## Research actions created

- Add supplier margin stacking, FAU/shuffle-box cost, bargaining power, service cost, and blast radius to the CPO TCO model.
- Keep scale-out and scale-up adoption probabilities separate.
- Reconcile every power/TCO percentage to reach, port count, host interface, ELS, cooling, margin, and service boundaries.
- Recover primary evidence for named NVIDIA suppliers and Meta/Broadcom reliability data before scoring them.

