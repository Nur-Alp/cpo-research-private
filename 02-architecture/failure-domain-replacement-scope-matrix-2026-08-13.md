# Failure-domain and replacement-scope matrix

**Status:** Evidence-gated architecture comparison; no field-cost ranking  
**As of:** 2026-08-13

| Architecture | Normally replaceable unit | What is isolated | What is not isolated | Public evidence | Economic conclusion |
|---|---|---|---|---|---|
| Retimed pluggable | Faceplate transceiver | Module/DSP/optics service boundary | Host ASIC, board and cooling | Mature modular architecture; exact field-cost data open | Serviceability benchmark, not a monetary winner |
| LPO / RTLR | Faceplate module | Module-level optic replacement; RTLR retains hot-plug boundary | Host/channel diagnostics and electrical-margin qualification | OIF RTLR boundary | Likely smaller blast radius than CPO; cost open |
| NPO / OBO | Near-package module, if implemented | Potential short-channel replaceable optical unit | Host package, connector, thermal and interface uncertainty | IEEE/OIF proposed/framework boundary | Plausible compromise; production/service proof open |
| Fixed switch CPO | Usually system/package boundary | Short electrical link and dense integration | Failed PIC/engine/package/ASIC can share a large replacement scope | Product architecture and prototype process evidence | Largest potential blast radius; actual rates/cost open |
| CPO + ELSFP | External laser module | Laser thermal/replacement domain | Fibre delivery, FAU, optical engine, package/ASIC and control map | OIF ELSFP | Laser service improvement only |
| CPO + detachable FAU | FAU/fibre interface, if qualified | Fibre-array/connector boundary | Fixed PIC-side optics, engine/package/ASIC | Patents/vendor designs | Potential scrap/service reduction, no fleet evidence |
| Socketed optical engine | Engine or subassembly, if qualified | Pre-final integration test/replacement | Socket, package/thermal and system failure domains | Intel/academic concepts | Potential isolation; no HVM service economics |

## Serviceability tests

1. **ELSFP:** does isolate the laser, not the engine.
2. **Detachable FAU:** can isolate fibre interface, but only with post-mating qualification and service procedure.
3. **Engine replacement:** not proven for NVIDIA or Broadcom target CPO SKUs.
4. **OEM warranty:** Dell promises system repair/replacement by next business day for relevant NVIDIA CPO SKUs; it does not disclose engine-level repair scope, MTTR achieved or cost.

## Required restored-port evidence

Failure domain, return rate, replacement unit, MTTR, spares, labour, downtime, warranty owner and a product-matched field population. None is public for a target 200G/lane CPO SKU.

**Anchors:** `STD-006`, `STD-011`, `STD-012`, `STD-015`; `CMP-050`, `CMP-058`; `PAP-003`; `PRI-001`, `PRI-002`.
