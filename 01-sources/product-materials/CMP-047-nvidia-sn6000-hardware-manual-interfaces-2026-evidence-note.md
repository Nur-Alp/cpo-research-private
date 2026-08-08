# CMP-047 — NVIDIA Spectrum-6 SN6600-LD hardware-interface boundary

- **Primary record:** [retained NVIDIA documentation HTML](CMP-047-nvidia-sn6000-hardware-manual-interfaces-2026.html) | [canonical NVIDIA hardware manual page](https://networking-docs.nvidia.com/sn6000hw/data-interfaces-and-high-power-transceivers-support)
- **Documentation revision:** last updated 1 July 2026.

## Evidence extracted

NVIDIA's Spectrum-6 hardware manual lists the SN6600-LD data-interface capability as **128 × 800GbE**, 256 × 400GbE and 512 × 200GbE. In a separate high-power-transceiver table, it lists **64 SN6600-LD OSFP ports** with a maximum supported power of 30 W per port.

## Boundary and limitations

This is an official hardware-interface specification, not a CPO BOM or customer shipment record. The page does not state whether the 128 data interfaces represent physical optical cages, breakout/logical lanes, or a configuration abstraction relative to the 64 high-power OSFP ports. It does not identify CPO engine count, laser/ELS count, supplier, qualification, yield or margin.

## Research use

CMP-047 materially improves configuration reconciliation: CoreWeave's 64 × 1.6T description and its separate 128-port/800GbE description should not be treated as automatically contradictory or automatically identical. Preserve the physical-port, logical-interface and optical-engine boundaries separately until a product bill of materials or detailed system manual resolves them.
