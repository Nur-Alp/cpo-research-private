# PIC-design profit implications

**Status:** Evidence-backed thesis bridge; not a company ranking

**Scope:** 200G/lane and later 400G/lane scale-out optical engines

## Core conclusion

No PIC architecture guarantees the highest profit. The profit pool is more likely to accrue to the supplier that converts a technically credible PIC into the lowest-cost, qualification-ready and serviceable good engine while retaining a scarce part of the bill of materials.

The current evidence supports three distinct routes:

| Route | What the retained evidence supports | Where profit could accrue | What can destroy the profit |
|---|---|---|---|
| Monolithic InP transmitter | Nokia integrates DFB lasers, MZMs, SOAs and monitors in an eight-channel PIC; one representative channel reaches 106.25 GBd PAM4 at 60 °C [`PAP-025`, `CLM-021`–`CLM-024] | More optical functions and calibration may be retained by the PIC supplier; fewer optical interfaces can reduce assembly complexity | Compound-semiconductor yield, thermal/reliability qualification, separate electronics and incomplete eight-channel validation |
| Silicon photonics + external laser | Lumentum and Sumitomo demonstrate high-power InP external-laser paths, while splitter work shows the loss and amplification trade-off [`PAP-019`, `PAP-022`, `PAP-026`, `CLM-033`–`CLM-039] | Scarce high-power laser, ELSFP serviceability and repeat laser supply can support pricing power | Laser/attach loss, TEC and control power, fibre routing, lifetime, coupling yield and customer/platform margin capture |
| 3D CMOS/microring or optical-I/O chiplet | Lightmatter demonstrates a compact monolithic Tx/Rx circuit; Ayar demonstrates test-before-final-assembly connector flow [`PAP-021`, `PAP-013`, `CLM-028`–`CLM-032] | PIC density, known-good-chiplet testing and package/interface IP may control a future accelerator or dense CPO platform | Single-channel evidence, heater/laser boundary, connector cycle life, hybrid-bonding yield, package thermal density and customer qualification |

## Why the isolated PIC metric is not enough

1. A low pJ/bit number can exclude the laser, receiver, host SerDes, thermal tuning and control. PAP-012 explicitly models only a bounded transmitter/equalisation problem, so its 1.35 pJ/bit result cannot be treated as complete-engine power [`CLM-025`–`CLM-026`].
2. High optical output does not establish a low-cost engine. PAP-019 reports packaged ex-fibre output and efficiency, but no lifetime, yield, cost or field data; PAP-022 uses a different, incompletely defined PCE boundary [`CLM-033`–`CLM-036`].
3. Dense integration can move value into packaging rather than the PIC. PAP-021's 0.006 mm² active area and 1.51 pJ/bit result exclude the laser and do not demonstrate a packaged multi-wavelength engine [`CLM-028`–`CLM-030`].
4. A detachable known-good optical chiplet can improve yield economics even if its PIC is not the fastest. PAP-013's test-before-final-assembly mechanism is economically relevant, but ten mating cycles and simulated tolerances do not establish production yield or lifetime [`CLM-031`–`CLM-032`].

## Profit-pool decision rule

Rank a PIC route only after it can answer all five questions at the same product boundary:

1. **Delivered performance:** lane rate, modulation, reach, BER/FEC and temperature.
2. **Good-engine cost:** die yield, attach yield, test time, rework and scrap.
3. **Service boundary:** replaceable laser/engine, failure isolation, MTTR and warranty owner.
4. **Commercial control:** qualified customer, repeat volume, supplier share, ASP and price-down terms.
5. **Capital return:** attributable packaging/test capex and the margin retained after platform and manufacturing partners.

The current public record does not clear all five for any route. The immediate focus should therefore be the **cost per qualified good engine** and the **share of that cost pool retained by the supplier**, not a universal “best PIC” label.

## Model linkage

- [Scale-out optical-engine benchmark](optical-engine-benchmark.md)
- [Laser architecture benchmark](laser-architecture-benchmark.md)
- [Packaging, fibre-attach and serviceability benchmark](packaging-reliability-benchmark.md)
- [Optical-engine profit-pool input gates](../08-model/optical-engine-profit-pool-input-gates.md)
- [Claim ledger](../01-sources/claim-ledger.csv)
