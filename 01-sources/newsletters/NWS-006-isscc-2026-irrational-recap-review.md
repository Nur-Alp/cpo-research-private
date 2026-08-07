# NWS-006 — ISSCC 2026 Irrational Recap

- Publisher: Irrational Analysis
- Publication date: 2026-02-19
- Canonical source: <https://irrationalanalysis.substack.com/p/isscc-2026-irrational-recap>
- Local retention: publisher hyperlink retained; no PDF snapshot was created because the recap is secondary and the ISSCC presentation/paper is the required evidence of record.
- Review date: 2026-08-07
- Evidence class: secondary conference recap / technical diligence source

## Why it is retained

This recap is directly relevant to the active PIC and optical-I/O workstream. It discusses NVIDIA's clock-forward optical die-to-die link using TSMC COUPE and ring modulators, and Celestial/Marvell's accelerator-side optical-I/O presentation. It also identifies measurement-boundary issues that matter for comparing optical engines: all-lane activity, PVT coverage, PRBS length, TDECQ function, temperature, WDM penalty, coupling loss, and laser noise.

## Evidence that can be used

The recap supports a diligence checklist rather than a product ranking:

1. Clock-forward optical D2D must be assessed for PVT, chromatic-dispersion, clock-distribution, lane-to-lane variation, and yield redundancy.
2. Ring-PIC demonstrations require resonance/periodicity, extinction ratio, thermal tuning, coupling-loss, and test-pattern disclosure.
3. Accelerator optical-I/O demonstrations require all-lane activity, temperature, equalizer/TDECQ definition, WDM penalty, and link-reach boundaries.
4. Laser linewidth and RIN are relevant to ring-modulator margin, but the recap's supplier-leadership conclusion is not accepted without matched primary measurements.

Existing primary anchors include PAP-005 (interposer/optical-I/O architecture), PAP-021 (Lightmatter microring prototype), CMP-020 (Marvell/Celestial company claim), and Lumentum's retained UHP/ELSFP materials. The recap does not replace those sources.

## Claims deliberately not accepted as facts

The article's forecasts about NVIDIA commercial timing, its statement that Lumentum is the only viable high-power supplier, its Celestial TDECQ/energy interpretation, and its MediaTek/IEEE commentary are secondary or opinionated. They are not entered as production, qualification, customer, or market-share evidence.

## Research actions created

- Recover the original ISSCC NVIDIA and Celestial/Marvell presentation material and record exact test boundaries.
- Add all-lane, PVT, PRBS, TDECQ function, temperature, WDM penalty, reach, and coupling-loss fields to the optical-I/O benchmark.
- Keep accelerator-side optical I/O separate from switch-side CPO in the adoption timeline and profit-pool model.

