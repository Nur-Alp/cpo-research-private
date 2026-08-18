# CMP-059 — Supermicro / AMD / Micas TH5-Bailly CPO validated design

**Canonical source:** <https://micasnetworks.com/uploads/2026-04-24/SMCI-AMD-Micas-CPO-validared-design-Final.pdf>  
**Publisher:** Super Micro Computer, Inc. (with AMD and Micas Networks)  
**Publication date:** April 2026  
**Local file:** [full 18-page PDF](CMP-059-supermicro-micas-bailly-validated-design.pdf)

## Evidence extracted

- The document identifies the **Micas M2-W6940-128X1-FR4** CPO switch with 128 × 400G ports. It states that the system integrates Broadcom Tomahawk 5 Bailly (51.2Tb/s), co-packaged optical engines and remote laser modules (RLMs).
- Its physical validation topology is one CPO switch, two Supermicro GPU servers, 16 AMD Pensando Pollara 400 NIC ports and 16 optical links. It explicitly contrasts the CPO switch with a conventional Micas Tomahawk 5 switch using switch-side pluggables.
- The document reports 465.87 W for its Tomahawk 5 Bailly CPO configuration versus 754.85 W for the stated pluggable configuration: a 288.98 W / 38.28% difference under that publisher-defined test configuration.
- It reports a 73 ns (about 1.5%) two-node/single-switch latency reduction and a 0.7–0.9% RCCL AllReduce bus-bandwidth improvement in that small topology.

## Correct use

This is the best retained **specific 100G/lane TH5-Bailly CPO-versus-pluggable test boundary**. It makes the historical 51.2T product, server-side optics boundary, RLM service route, comparison topology and power number inspectable.

The result cannot be transferred to TH6-Davisson, NVIDIA Spectrum-X, 200G/lane, a full leaf-spine fabric, a different reach/FEC/cooling condition, or a full system TCO calculation. It strengthens the case that a CPO power benefit is possible in a defined TH5 configuration; it does not establish a general architecture winner.

## Limitations

- Vendor-partner validated design rather than independent operator field study.
- The actual power methodology, measurement points, port population, reaches, FEC, cooling allocation and variance are insufficiently specified for a universal comparison.
- The realised physical topology is one switch/two servers/16 links. The document says its proposed multi-switch comparison is future work.
- Its >1M port-hours / zero-link-flap statement is described as aligned with Broadcom qualification data; treat it as reused vendor qualification context, not an independent field-return distribution.
- No customer procurement, installed units, repeat shipments, ASP, supplier share, final-engine yield, rework, warranty reserve, margin or full replacement-cost disclosure is supplied.

**Use:** historical TH5-Bailly architecture and bounded power/latency comparator. Do not use for TH6 commercial proof or CPO profit-pool attribution. See `CLM-522`–`CLM-525`.

