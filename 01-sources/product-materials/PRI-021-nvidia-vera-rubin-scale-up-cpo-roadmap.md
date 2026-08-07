# NVIDIA Vera Rubin and NVLink scale-up CPO roadmap — primary-source review

- **Publisher:** NVIDIA Developer Technical Blog
- **Publication dates:** 16 March 2026 (Vera Rubin POD) and 20 July 2026 (NVLink)
- **Canonical sources:**
  - <https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/>
  - <https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/>
- **Local retention:** Canonical HTML links retained; no local archive is required for this primary web material.
- **Reviewed:** 7 August 2026

## What the sources establish

NVIDIA's Vera Rubin POD post states that the Spectrum-6 SPX networking rack includes a 102.4-Tb/s Spectrum-6 switch with 512 lanes and 200-Gb/s co-packaged optics in single- and multi-chip switch offerings. The same post says Vera Rubin Ultra NVL576 combines eight racks into one 576-GPU NVLink domain using copper and direct optical connections, and identifies Polyphe as a fully functional GB200-based prototype of that multirack topology. It then describes Kyber as a future NVL1152 design using similar direct optical interconnects for rack-to-rack scale-up.

The NVLink post separately states that NVIDIA's technology roadmap includes scale-up domains up to 1,152 GPUs and connectivity through CPO. It also describes NVLink 6 as production-deployed at scale, but that maturity statement applies to NVLink generally and does not prove production deployment of the future NVL576/NVL1152 CPO topology.

## Evidence boundary

These are first-party architecture and roadmap claims. They establish a specific deployment domain and a functional prototype, plus a stated product direction. They do **not** disclose NVL576/NVL1152 shipment dates, units, customer deployments, optical-engine suppliers, final-engine yield, qualification results, field failure rates, service procedures, ASP, or CPO-specific margin.

## Research use

Upgrade inter-rack scale-up CPO from a secondary-only roadmap hypothesis to a primary NVIDIA roadmap with a functional prototype. Keep its commercial state below production until a named system, customer deployment, qualification record, or repeat shipment is documented.
