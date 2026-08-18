# Laser delivered-power waterfall

**Status:** Evidence-bounded sensitivity model; not a supplier ranking  
**Scope:** External-light-source versus integrated-source boundaries for scale-out optical engines  
**As of:** 2026-08-09

## Why this model exists

Laser papers report different boundaries: chip or submount power, packaged ex-fibre output, modulated per-channel output, and post-splitter branch power. These values cannot be ranked directly. The relevant operating variable is usable optical power at the engine input after coupling, fan-out, connector, redundancy and aging losses.

## Conversion

For a measured source output `P_source` in dBm and a distribution loss `L_distribution` in dB:

```text
P_branch(dBm) = P_source(dBm) − L_distribution(dB)
P_branch(mW) = 10 ^ (P_branch(dBm) / 10)
```

This is a first-order optical-power calculation. It excludes source electrical power, TEC/control power, amplifier power, receiver sensitivity, wavelength allocation, redundancy and lifetime degradation.

## Evidence-bounded example

Lumentum's PAP-019 record reports up to 720 mW ex-fibre at 25°C (about 28.6 dBm). Furukawa/AIST PAP-026 reports approximately 10.5–15 dB total loss through its polymer 1×4 fan-out demonstration and used a booster amplifier. Applying that measured prototype loss to the Lumentum source gives the following **sensitivity only**:

| Source boundary | Distribution loss | Calculated branch power | Interpretation |
|---|---:|---:|---|
| 720 mW ex-fibre (28.6 dBm) | 10.5 dB | 18.1 dBm ≈ 64.2 mW | Upper end of the PAP-026 prototype-loss range; not a qualified production branch |
| 720 mW ex-fibre (28.6 dBm) | 15.0 dB | 13.6 dBm ≈ 22.8 mW | Lower end of the PAP-026 prototype-loss range; still before connector, aging and redundancy penalties |
| 500 mW source (27.0 dBm) | 10.5 dB | 16.5 dBm ≈ 44.6 mW | Illustrative external-source case; PAP-022's >500 mW is not stated at the same fibre-coupled boundary |
| 3–5 dBm modulated channel | No distribution loss applied | 3–5 dBm ≈ 2.0–3.2 mW | Nokia PAP-025 is a modulated per-channel output, not comparable to the high-power CW source rows |

The first two rows are arithmetic implications of separately reported boundaries, **not a demonstrated Lumentum-plus-Furukawa production configuration**. The 500 mW row must not be treated as a fibre-coupled Sumitomo output because PAP-022 does not disclose that boundary.

## Architecture implications

- High ex-fibre CW output can be consumed by fan-out and connector loss before reaching the PIC/engine.
- External sources may still win on serviceability and thermal isolation if distribution loss, redundancy and replacement logistics are controlled.
- Monolithic InP can remove high-power fan-out interfaces, but it moves heat, laser failure and yield correlation into the transmitter package.
- A branch-power advantage is not an energy-per-bit advantage until source electrical power, TEC/control, amplifier use and delivered optical requirement are measured at the same engine boundary.

## Required production evidence

To replace this sensitivity model with a supplier comparison, obtain:

1. Ex-fibre output and electrical input at the same temperature and aging point.
2. Coupler, splitter, connector and fibre loss distributions over all channels.
3. Redundancy and spare-source policy, including power penalty.
4. Engine-input power and receiver/link margin at the required BER/FEC boundary.
5. Lifetime, feedback tolerance, replacement procedure and field-return cost.
6. Production yield and test/rework cost for source, fan-out and engine attachment.

The current sources provide device and prototype boundaries, not this complete delivered-power and economic bundle (`PAP-019`, `PAP-022`, `PAP-025`, `PAP-026`; `CLM-033`–`CLM-043`).

## Linked controls

- [Laser architecture benchmark](../03-components/laser-architecture-benchmark.md)
- [Optical-engine benchmark](../03-components/optical-engine-benchmark.md)
- [Coherent versus Lumentum matched engine bridge](coherent-lumentum-matched-engine-profit-bridge.md)
- [Manufacturing cost per qualified good engine](manufacturing-cost-per-good-engine-gate.md)
