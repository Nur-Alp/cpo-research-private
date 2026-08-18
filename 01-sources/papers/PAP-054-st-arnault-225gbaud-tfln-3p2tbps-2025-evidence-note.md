# PAP-054 evidence note — 225-GBaud TFLN 3.2-Tb/s transmission

**Citation:** Charles St-Arnault et al., “Net 3.2 Tbps 225 Gbaud PAM4 O-Band IM/DD 2 km Transmission Using FR8 and DR8 with a CMOS 3 nm SerDes and TFLN Modulators,” OFC 2025, 8 pages. [arXiv record](https://arxiv.org/abs/2503.24147) · [local PDF](PAP-054-st-arnault-225gbaud-tfln-3p2tbps-2025.pdf)

## Measured boundaries

- The authors demonstrate 8-channel 225-GBaud PAM4 and PAM8 IM/DD using TFLN Mach–Zehnder modulators and a 3-nm CMOS SerDes/DAC (pp. 1, 4–7).
- At 2 km, both 8-WDM FR8 and parallel-fibre DR8 achieve 8 × 420.5 Gb/s net PAM4 under 7% HD-FEC, or 3.36 Tb/s aggregate (Table 1; pp. 6–7).
- At 2 km, PAM8 reaches 8 × 540 Gb/s net under 25% SD-FEC, or 4.32 Tb/s aggregate (Table 1; pp. 6–7).
- The DR8 configuration maintains 225-GBaud PAM4 under the HD-FEC threshold at 500 m while the uncooled quantum-dot DFB laser is swept from 30°C to 85°C (pp. 6–7).
- At 5 km, chromatic-dispersion effects reduce the best reported PAM4 result to 8 × 375 Gb/s under 20% SD-FEC, or 3.0 Tb/s aggregate (pp. 6–7).

## Decision relevance

This is a strong advanced-pluggable/PIC counterweight to a CPO-only lane-rate thesis. It shows that 400G-class net lanes can be achieved with TFLN modulators, a 3-nm SerDes and uncooled laser operation in a 500-m/2-km test boundary. It therefore raises the CPO adoption gate: CPO must win on complete system power, cost, reach, serviceability, density or qualification—not merely on 400G/lane feasibility.

## Limitations

This is a laboratory transmission demonstration, not a production-qualified module or CPO engine. The paper does not provide complete module/chassis power, package yield, fibre attach, manufacturing cycle time, field reliability, customer qualification, ASP, margin or supplier economics. The BER results rely on stated equalization and FEC assumptions; retain those boundaries in any comparison.

