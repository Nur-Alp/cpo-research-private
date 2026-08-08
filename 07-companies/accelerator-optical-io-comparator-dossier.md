# Accelerator optical-I/O and NPO comparator dossier

**Status:** Evidence-matched scale-up comparator; not a public-equity ranking  
**As of:** 2026-08-08  
**Deployment domain:** Accelerator scale-up, inter-XPU and near-package optical fabrics

## Domain separation

Accelerator optical I/O is not switch-side Ethernet CPO. The value proposition may be larger world size, lower collective-communication cost, or a package-level electrical-boundary change rather than a transceiver replacement. The denominator is an XPU/package/rack topology, not a 102.4T Ethernet switch.

## Evidence-matched comparison

| Route | Public record | Evidence state | Potential control point | Blocking evidence |
|---|---|---|---|---|
| **Ayar Labs TeraPHY / UCIe** | Claims an 8 Tb/s optical-I/O chiplet using UCIe and a 16-wavelength SuperNova light source | Company product announcement; private-company technical candidate | UCIe optical chiplet, light-source interface, connectorized known-good assembly | No named production customer, system topology, shipped units, yield, qualification, cost or margin |
| **Lightmatter Passage L20** | Claims 6.4 Tb/s per direction, standards-based 224G PAM4, NPO/OBO positioning and late-2026 sampling | Roadmap/sampling announcement | Unified optical engine and near-package/OBO form factor | Samples not independently observed; no qualification, customer, yield, power, ASP or margin |
| **Marvell/Celestial Photonic Fabric** | Marvell acquired Celestial; claims a 16 Tb/s first-generation photonic-fabric chiplet and forecasts meaningful revenue in H2 FY28, $500M annualized Q4 FY28 and $1B annualized Q4 FY29 | Strategic ownership plus management forecast | Accelerator connectivity platform, protocol/custom XPU integration and chiplet content | No customer, design win, shipped units, product margin, yield, topology or revenue conversion |
| **Intel OCI** | Live-data 4 Tb/s bidirectional OCI chiplet co-packaged with an Intel CPU; on-chip DWDM lasers/amplifiers; prior pluggable PIC volume claim | Prototype/select-customer evaluation with prior-volume baseline | PIC/laser integration and accelerator optical-I/O platform | No OCI production, 200G/lane implementation, complete-engine yield, qualification or economics |
| **NVIDIA Quantum-X / inter-rack CPO** | NVIDIA reference architecture gives engine/ELS denominators; Lambda reports production-scale Quantum-X Photonics in a >10,000-GPU GB300 cluster | First-party architecture plus customer production-scale claim, exact SKU undisclosed | Platform, topology, system software and customer route | No exact production SKU, switch count, supplier BOM, engine yield, ASP or margin |
| **TSMC COUPE / interposer** | 200G COUPE result, >99% engineering-sample 3D-stacking yield and CPO-on-substrate production milestone | Manufacturing/process checkpoint | EIC/PIC stacking, interposer/foundry process and package integration | No named accelerator SKU, final-engine yield, shipped units, supplier share, ASP or margin |

## Economic reading

The potentially largest value capture in this domain may sit at the protocol and package boundary: a supplier that controls the optical chiplet, host electrical interface, thermal path, fibre attach, test and customer qualification could capture more content than an isolated laser or PIC supplier. Conversely, a platform owner may internalize the interface and leave external suppliers with low-margin manufacturing.

The public evidence does not yet distinguish those outcomes. Ayar and Lightmatter are private-company technology routes; Marvell provides the clearest public-company revenue aspiration; Intel has the strongest prior PIC volume baseline; NVIDIA has the strongest platform/customer route; and TSMC has the strongest public process-control position. These are different leadership dimensions, not one ranking.

## Required matched records

1. XPU/package topology, optical endpoint count and protocol for each named product.
2. Complete optical-I/O power, latency, reach and collective-communication benchmark versus copper/AEC/NPO/CPO alternatives.
3. Chiplet, laser, interposer, fibre attach and package yield by lot, including rework and test escape.
4. Named customer qualification, production units, repeat deployment and field-service model.
5. Product ASP, supplier share, gross margin, capex and revenue conversion.

## Current conclusion

Accelerator optical I/O has credible technical and strategic routes, but no public record yet clears the production-economic gate. Marvell is the most explicit public-company revenue case; NVIDIA is the strongest platform route; TSMC is the strongest process-control route; Ayar and Lightmatter remain important private-company option value. None can be called the sustainable profit-pool leader on current evidence.

## Sources

- [Ayar Labs TeraPHY/UCIe announcement](../01-sources/product-materials/CMP-012-publisher-original.html), `CMP-012`, `CLM-085`.
- [Lightmatter Passage L20 announcement](../01-sources/product-materials/CMP-013-publisher-original.html), `CMP-013`, `CLM-086`.
- [Marvell/Celestial accelerator optical-I/O dossier](marvell-celestial-accelerator-optical-io-dossier.md), `CLM-093`–`CLM-096`.
- [Intel OCI comparator record](../01-sources/product-materials/CMP-035-intel-oci-chiplet-ofc2024.md), `CMP-035`, `CLM-304`–`CLM-305`.
- [NVIDIA CPO reference-content bridge](../08-model/nvidia-cpo-reference-content-bridge.md), `CLM-224`, `CLM-233`–`CLM-238`.
- [Silicon-interposer optical-I/O boundary](../02-architecture/interposer-optical-io-boundary.md), `PAP-005`.
