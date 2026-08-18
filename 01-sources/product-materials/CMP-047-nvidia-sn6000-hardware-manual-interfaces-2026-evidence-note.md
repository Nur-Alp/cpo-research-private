# CMP-047 — NVIDIA Spectrum-6 SN6600-LD hardware-interface boundary

- **Primary record:** [retained NVIDIA documentation HTML](CMP-047-nvidia-sn6000-hardware-manual-interfaces-2026.html) | [canonical NVIDIA hardware manual page](https://networking-docs.nvidia.com/sn6000hw/data-interfaces-and-high-power-transceivers-support)
- **Documentation revision:** last updated 1 July 2026.

## Evidence extracted

NVIDIA's Spectrum-6 hardware manual lists the SN6600-LD data-interface capability as **128 × 800GbE**, 256 × 400GbE and 512 × 200GbE. In a separate high-power-transceiver table, it lists **64 SN6600-LD OSFP ports** with a maximum supported power of 30 W per port.

## Boundary and limitations

This is an official hardware-interface specification, not a CPO BOM or customer shipment record. The page does not state whether the 128 data interfaces represent physical optical cages, breakout/logical lanes, or a configuration abstraction relative to the 64 high-power OSFP ports. The full 61-page family manual retained as [CMP-048](CMP-048-nvidia-sn6000-hardware-manual-full-evidence-note.md) resolves the product architecture: SN6600-LD uses pluggable RHS transceivers, while SN6810-LD/SN6800-LD are the CPO families. CMP-047 itself does not identify CPO engine count, laser/ELS count, supplier, qualification, yield or margin.

## Research use

CMP-047 materially improved interface reconciliation; CMP-048 now adds the stronger architecture boundary. CoreWeave's 64 × 1.6T description and its separate 128-port/800GbE description remain different interface descriptions of a pluggable SN6600-LD record, not evidence of a CPO engine count. Preserve physical-port, logical-interface and optical-engine boundaries separately.
