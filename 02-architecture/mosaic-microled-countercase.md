# MOSAIC microLED countercase to laser-based CPO

**Status:** Reviewed academic countercase; not a product forecast  
**Source:** `PAP-009` — Benyahya et al., ACM SIGCOMM 2025  
**Decision relevance:** Tests whether a wide-and-slow, microLED optical link could displace or complement 200G/400G-per-lane laser engines in scale-out AI fabrics.

## What the paper actually demonstrates

Microsoft reports a 100-channel prototype using directly modulated microLEDs, CMOS sensor arrays and a multicore imaging fibre. Measurements show 2 Gb/s per channel over 20 m with median BER below 2×10^-8. At 30 m, the prototype meets the cited Ethernet/InfiniBand pre-FEC threshold at 1.6 Gb/s, but 2 Gb/s is slightly above it. These are hardware results from a prototype using wire bonding, discrete drivers/TIAs and bulky optics—not a qualified module.

The proposed 800 Gb/s module would use roughly 460 channels (including redundancy) at 2 Gb/s/channel. The paper simulates 2 Gb/s over 50 m and estimates 3.1–5.3 W per end, versus 9.8–12 W for its mainstream optical baseline. Both the 800 Gb/s module and the power comparison are estimates; full-link power is twice the per-end figure and the host-interface boundary must be matched before comparing with CPO engine data.

## Why it matters to the CPO thesis

MOSAIC attacks the same scale-out constraints from a different direction: hundreds of slow channels avoid high-speed DSP/ADC/DAC/CDR, while microLED redundancy may improve reliability. The paper says the design is compatible with CPO and could benefit more from short host traces, but it does not build or qualify a CPO implementation. It therefore belongs in the countercase set, not in the current CPO leader ranking.

The manufacturing question is different from laser CPO. MOSAIC trades high-speed optical-electrical complexity for dense microLED/CMOS bonding, custom TIR micro-optics, imaging-fibre coupling and hundreds of channels. The authors explicitly identify adaptation of consumer microLED and imaging-fibre manufacturing lines, packaging, deployment, system integration and reliability at scale as remaining work. Their cost discussion is qualitative and expressly outside the paper's detailed scope.

## Investment interpretation

MOSAIC is a credible option-value threat if 800 Gb/s modules can be manufactured, serviced and qualified at the modeled power and reliability. It does not yet answer the active profit question because no ASP, BOM, yield, qualification, customer, volume or supplier-share evidence is reported. The relevant diligence gates are:

- simultaneous 800 Gb/s (then 1.6 Tb/s) hardware, not channel-count extrapolation;
- package-level BER, thermal drift, fibre/coupler loss and environmental reliability;
- microLED/CMOS die yield, wafer-scale lens/bonding throughput and imaging-fibre termination cost;
- a matched host-interface power tree against pluggable, NPO and CPO alternatives;
- customer deployment evidence and a service/warranty model.

Until those gates clear, laser-based scale-out optical engines remain the primary commercial scope, while MOSAIC is a tracked architectural countercase that could cap long-run pricing power.

## Source

- `PAP-009` — [ACM DOI](https://doi.org/10.1145/3718958.3750510); retained PDF: `01-sources/papers/PAP-009-microsoft-mosaic-microled-2025.pdf`.
- Claim ledger: `CLM-116` through `CLM-119`.
