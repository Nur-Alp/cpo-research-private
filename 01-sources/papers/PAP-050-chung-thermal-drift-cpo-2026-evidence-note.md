# PAP-050 — Chung, thermal drift and CPO scheduling

## Citation

Chi Fei Chung, “Predictive Software Scheduling as an Early-Warning Hint Layer for Optical Engine Thermal Drift in Heterogeneous SoIC Packaging,” arXiv:2605.18612 (23 May 2026). [arXiv record](https://arxiv.org/abs/2605.18612) · [Local PDF](PAP-050-chung-thermal-drift-cpo-2026.pdf).

## What was reviewed

The complete 8-page arXiv preprint was retrieved and read on 2026-08-10. It is not peer-reviewed and reports author-generated software/thermal experiments; it should be treated as a low-confidence research lead, not as TSMC or COUPE product evidence.

## Bounded evidence

- The paper proposes a software scheduling layer intended to provide early-warning thermal hints to photonic bias control in a hypothetical heterogeneous SoIC/COUPE context.
- It reports author-generated validation over 90,000 inference steps, including a claimed load correlation of R² = 0.9911, wavelength drift below 0.36 nm, Rth = 0.45 °C/W and an 80-ms thermal time constant (abstract and pp. 1–3).
- The work makes thermal drift and workload transients explicit as a potential accelerator-side optical-I/O control problem.

## Evidence boundary and credibility controls

The preprint does not identify a TSMC customer package, disclose a fabricated COUPE test vehicle, provide independent replication, report BER/TDECQ under a complete link, or establish production yield, reliability, service, ASP or margin. Its numerical results are author-reported and should not be used as COUPE specifications. Claims are recorded as `CLM-458`–`CLM-460`.

## Research use

Use PAP-050 only to formulate a thermal-control diligence question: can workload-aware control reduce wavelength drift without adding unacceptable latency, power, firmware complexity or failure modes? Seek peer-reviewed package measurements and vendor/customer qualification before using any number in the model.
