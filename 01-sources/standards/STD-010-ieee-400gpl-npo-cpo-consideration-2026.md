# STD-010 — Consideration on NPO and CPO at 400G/Lane

- **Authors:** Runlong Hu, Haojie Wang and Weiqiang Cheng (China Mobile)
- **Forum:** IEEE 802.3 400GPL Study Group, May 2026 public contribution
- **Canonical source:** [IEEE contribution PDF](https://www.ieee802.org/3/400GPL/public/2605/wang_h_400GPL_01_2605.pdf)
- **Local preservation:** This evidence note retains the canonical link; the publisher PDF was not copied into the repository.
- **Review status:** Read on 2026-08-07

## What the contribution establishes

The authors define the architectural distinction between CPO (optics on the same substrate as the ASIC) and NPO (optics near the ASIC package but not on the same substrate). They argue that eliminating a retimer/DSP shortens the electrical path and requires electrical and optical domains to align in rate and modulation format. For a 400G/lane PAM4 path, the contribution states approximately 212.5 GBaud and 106.25 GHz Nyquist frequency; it contrasts this with a PAM6 case of approximately 170 GBaud and 85 GHz Nyquist frequency.[CLM-259][CLM-260]

The contribution also identifies a FEC/control trade-off: a retimer/gearbox can host rate adaptation, FEC alignment and modulation mapping, while an NPO/CPO implementation without that retimer has to accommodate those functions elsewhere.[CLM-261]

## Evidence boundary

This is an IEEE Study Group contribution, not a ratified standard, measured end-to-end link, or product qualification. Its 400G/lane arithmetic and architecture discussion are useful for the electrical-boundary model. Its statements about industry launches, hyperscaler roadmaps, Chinese deployment timing, and power savings are not independent production evidence and are not used as adoption forecasts.[CLM-262]

The contribution's cited 200,000-GPU power figures are secondary references and are not imported into the project's power model. The project's 400G conclusion therefore remains: a short electrical path is technically attractive, but the source does not prove that NPO/CPO beats LPO on total cost, reliability, yield, serviceability or profit.

## Model use

- Use `CLM-259`–`CLM-261` as a topology and rate/modulation boundary in the [linear-drive benchmark](../../02-architecture/linear-drive-boundary-benchmark.md).
- Do not use the contribution's 2027–2029 deployment language as a probability or adoption denominator.
- Keep the measured-versus-modeled distinction for `PAP-011`: the contribution explains why 212.5 GBaud is difficult, but it does not add a measured 400G/lane link.
