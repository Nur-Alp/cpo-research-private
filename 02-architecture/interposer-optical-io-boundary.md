# Silicon-Interposer Optical I/O Boundary

**Status:** Migration hypothesis; not a current product ranking

**Scope:** Optical engines on a silicon interposer or local silicon bridge, beyond package-adjacent CPO

**Last updated:** 2026-08-07

## Decision question

Could moving optics onto the silicon interposer create a higher-value profit pool than package-adjacent CPO, and what evidence would show that the value migrates to the interposer, foundry, packaging or optical-engine supplier?

## What PAP-005 establishes

The NVIDIA-authored paper identifies a physical scaling mechanism: an organic CPO substrate has more package edge (“beachfront”) for fibres, but its electrical routing density can constrain the ASIC-to-optics interface. A silicon interposer or local silicon bridge can provide denser wiring and permit slower, wider electrical links. The same move makes the optical fibre edge more constrained, so optical edge bandwidth density and fibre routing become first-order limits.

This is an architecture argument supported by demonstrations and simulations. It is not evidence that NVIDIA, a foundry or any optical supplier has a qualified interposer product.

## Evidence boundary

| Claim | Evidence class | Correct interpretation |
|---|---|---|
| 112G XSR at 1.24-1.7 pJ/b and 475-870 Gb/s/mm | Cited measured demonstrations | Electrical-interface reference points, not a complete interposer optical link |
| 250-350 W for 100T CPO-on-MCM XSR links | Paper model | Electrical portion only; optical link and complete cooling boundary excluded |
| 0.25 pJ/b electrical + 1 pJ/b optical + 2 pJ/b remote laser | Paper design target | Future architecture budget, not a product specification |
| 1.5-2 pJ/b at about 28-33 Gb/s/channel for 800 Gb/s link | Paper simulation | Thermal-tuning/ring-link model; not a 200G/400G-per-lane engine result |

## Value-chain implications

Interposer integration could shift economic control toward whichever supplier owns the coupled process window across:

1. silicon-interposer or bridge design rules and yield;
2. EIC/PIC placement, bonding and thermal path;
3. dense fibre attach and optical-edge routing;
4. remote-laser distribution, control and redundancy;
5. test access before expensive host-die assembly; and
6. final package qualification, rework and warranty allocation.

The optical-engine supplier does not automatically capture this pool. A platform owner or foundry could internalize the interposer and leave the engine vendor with a narrower content share. Conversely, a specialist that owns the qualified PIC-to-interposer-to-fibre process could become a scarce manufacturing partner. Current public evidence does not resolve which outcome applies.

## Diligence gates before treating this as an investable transition

- Demonstrated interposer package at the target aggregate bandwidth with measured electrical and optical links.
- Die-to-interposer and PIC-to-interposer first-pass yield, rework and known-good-die flow.
- Fibre edge density, connector count, supply-fibre overhead and complete delivered optical-power budget.
- Thermal map and control-power distribution under the actual host ASIC workload.
- Wafer, interposer, assembly and test capacity with attributable capex and depreciation.
- Customer qualification, production shipments, second source and warranty ownership.
- Content, ASP, gross margin and whether the interposer displaces or adds to the optical-engine supplier's legacy revenue.

## Conclusion

Interposer optics are a credible post-CPO scaling hypothesis and a potential value-chain migration. The paper strengthens the case for studying foundries and advanced-packaging owners, but it does not yet justify moving the primary 2026-2032 profit-pool focus away from qualification-ready scale-out optical engines.

## Source

- `PAP-005`: Benjamin G. Lee et al., [*Beyond CPO: A Motivation and Approach for Bringing Optics Onto the Silicon Interposer*](../01-sources/papers/PAP-005-lee-beyond-cpo-silicon-interposer-2023.pdf), *Journal of Lightwave Technology* 41(4), 2023, DOI `10.1109/JLT.2022.3219379`. NVIDIA-authored invited architecture study; modeled and cited results are kept separate from product evidence.
