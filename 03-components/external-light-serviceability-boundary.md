# External-Light Serviceability Boundary

**Status:** Architecture and management review; not a field-service or reliability result
**Last updated:** 2026-08-07

## Bottom line

An external light source (ELS), including a pluggable ELSFP, can isolate and make the **light-source resource** more manageable. It does not make the full co-packaged optical engine, its passive delivery fibre, couplers, package or host-board control system serviceable by default.

OIF's informative management architecture assigns the host-board controller—not the OE or ELS—to map, coordinate and control CW light between external source and optical engine.[CLM-097]

## What moves outside the optical engine

| Resource / failure domain | With internal laser | With external light source | Investment implication |
|---|---|---|---|
| Laser/source | Managed inside OE | Source sits outside OE and can be selected/managed separately | Potentially improves laser replacement, redundancy and inventory flexibility. |
| CW-light control | OE controls laser directly | Host controller must map ELS/OE relationship and command the source | Adds system software/control, verification, latency and fault-management dependencies. [CLM-097] |
| Passive fibre/coupler path | Not applicable or shorter internal path | Added delivery path to OE | A power-delivery fibre fault can be observed at the OE but is not generally detectable by the ELS. [CLM-097] |
| OE/PIC/package failure | OE replacement/repair remains an architecture-specific issue | Still an OE/PIC/package issue | ELS does not repair the engine, attach or package. |

## Scale and topology boundary

The OIF document presents a 3.2T OE with four or eight CW-light inputs and ELSFP with up to sixteen outputs. It envisages one ELS powering one or two OEs in the near term, while allowing more flexible relationships.[CLM-098]

This is not a 102.4T switch bill of materials. It must not be converted into a 16-engine fanout, laser-content figure, yield calculation or customer deployment assumption.

## Commercial implications to test

An external-light architecture can be economically superior only if the benefit of source-level replaceability/redundancy exceeds the new costs and risks:

```text
ELS value
= avoided laser-related outage / replacement cost
+ possible source utilisation and redundancy benefit
- source module, fibre distribution, loss and control cost
- passive-path, connectivity-map and host-controller fault exposure
- any OE/package failure cost still borne by the system
```

No reviewed OIF, company or academic record quantifies that all-in comparison today.

## Diligence questions

1. What exact ELS-to-OE mapping, input-port count and redundancy scheme does the product use?
2. Is the ELS faceplate-replaceable in the deployed chassis, and what is the safe replacement procedure?
3. Which faults can be isolated to source, fibre, connector, OE, PIC, driver/TIA and host package?
4. What are field failure rate, MTTR, spare ratio, warranty owner and service labour for each failure domain?
5. How much optical distribution loss and laser-power headroom are consumed by the delivery path?
6. Does the host controller manage discovery/verification automatically, and what happens on a map/control-path fault?

## References

- OIF, [*Management of External Light Sources and Co-Packaged Optical Engines*](../01-sources/standards/STD-006-oif-elsfp-management.pdf), OIF-MGT-Co-Packaging-ELSFP-01.0, 2022.
- [Laser Architecture Benchmark](laser-architecture-benchmark.md).
- [Coherent and Lumentum External Optical-Engine Dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md).
- [Claim ledger](../01-sources/claim-ledger.csv), CLM-097 and CLM-098.
