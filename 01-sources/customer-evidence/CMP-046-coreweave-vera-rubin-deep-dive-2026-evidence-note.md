# CMP-046 — CoreWeave Vera Rubin NVL72 operational and Spectrum-X deployment boundary

- **Primary record:** [retained customer HTML](CMP-046-coreweave-vera-rubin-deep-dive-2026.html) | [canonical CoreWeave page](https://www.coreweave.com/blog/a-deep-dive-on-coreweave-innovations-for-nvidia-vera-rubin-nvl72)
- **Publisher/date:** CoreWeave, 17 June 2026.

## Evidence extracted

CoreWeave says it was the first cloud provider to bring up and validate NVIDIA Vera Rubin NVL72. It describes a **100% liquid-cooled NVIDIA Spectrum-X SN6600 Ethernet switch** with 102.4 Tb/s total switching capacity across 128 ports of up to 800 Gb/s, used as the scale-out fabric connecting NVL72 racks. It also describes a rack-control and cooling stack with per-rack telemetry, leak detection and service isolation, and a multi-rail, multi-plane fabric that can scale beyond 120,000 GPUs.

## Boundary and limitations

This is strong customer/operator evidence for a deployed Vera Rubin/Spectrum-X system boundary and for the operational consequences of liquid-cooled networking. The page does not explicitly identify the optical implementation inside every SN6600, CPO engine supplier, unit count, qualification lot, repeat order, field-return rate, ASP or margin. The 128-port SN6600 description also differs from other CoreWeave/NVIDIA records that describe 64 × 1.6T ports; preserve both configurations rather than silently reconciling them.

## Research use

Use CMP-046 to strengthen the customer deployment and service/operations evidence while keeping CPO attribution conditional. It is not a CPO unit numerator or an optical-engine profit-pool record until the SKU's optical configuration and supplier content are disclosed.
