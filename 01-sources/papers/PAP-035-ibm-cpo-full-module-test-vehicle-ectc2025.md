# PAP-035 — IBM CPO full-module test vehicle and reliability pre-conditioning

- **Authors:** John U. Knickerbocker et al.
- **Publisher:** IBM Research / IEEE ECTC 2025
- **Canonical record:** https://research.ibm.com/publications/co-packaged-optics-cpo-technology-full-module-test-vehicle-demonstrations
- **DOI:** https://doi.org/10.1109/ECTC51687.2025.00052
- **Publication:** 2025-05-27
- **Evidence class:** Full eight-page conference paper; research test vehicle, not production qualification
- **Local PDF:** [PAP-035 full paper](PAP-035-ibm-cpo-full-module-test-vehicle-ectc2025.pdf)

## Evidence extracted

IBM reports full CPO modules with polymer-waveguide fibre interfaces and compares two assembly orders: PIC-to-polymer-waveguide first and PIC-to-polymer-waveguide last. The team characterized optical link performance before and after reflow, reporting flip-chip and BGA reflow compatibility. Full-module hardware underwent reliability pre-conditioning and JEDEC stress testing including deep thermal cycling, low-temperature storage, high-temperature storage, and high-temperature/high-humidity exposure followed by characterization. The link-loss evaluation used twelve channels per PIC with a 50 µm PIC-to-polymer interface pitch; sub-25 µm pitch was supported by modeling and prototype hardware.

The full paper reports −40°C to +125°C deep thermal cycling up to 1,000 cycles, 85°C/85% RH testing up to 1,000 hours, −40°C storage up to 500 hours and 110°C/125°C high-temperature storage up to 1,000 hours. It states that multiple PIC/module samples were built, including three-PIC-per-module samples, and that material, contamination-control, tolerance and process changes improved insertion-loss distributions, yield and thermal stability. The final reported PIC-to-single-mode-fibre insertion-loss range is below 1.5–3.0 dB after improvement, versus more than 3.2–5.1 dB in early full-module hardware. These are research test-vehicle results, not HVM yield statistics.

## Evidence boundary

The paper establishes a full-module reliability-test vehicle and a concrete qualification workflow, not a production qualification result. It does not provide a complete lot-level yield waterfall, accepted-unit denominator, automated cycle time, lifetime model, field-return distribution, customer SKU, ASP or margin. Its insertion-loss plots and reliability results should not be converted into commercial engine yield without the sample-level data.
