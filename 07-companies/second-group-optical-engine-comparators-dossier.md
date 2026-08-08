# Second-group optical-engine comparators: Intel, Cisco/Acacia and Ranovus/Jabil

**Status:** Evidence-matched comparator dossier; not a leadership ranking  
**As of:** 2026-08-08  
**Scope:** Scale-out optical engines/PICs, adjacent LPO/NPO and accelerator optical-I/O routes

## Why this group matters

The primary comparison cannot be robust if it treats Broadcom, NVIDIA, Coherent and Lumentum as the only feasible routes. Intel, Cisco/Acacia and Ranovus/Jabil provide distinct countercases: a prior-volume PIC platform with an accelerator optical-I/O prototype, a 200G/lane silicon-photonic engine and LPO/system qualification route, and a monolithic EPIC engine paired with outsourced manufacturing.

These records are not directly interchangeable. Intel's OCI is an accelerator optical-I/O prototype; Cisco's 51.2T evidence is an LPO system comparator; Acacia's 200G/lane engine is a client-optics product route; Ranovus' ODIN is a planned CPO/NPO engine manufacturing route.

## Evidence-matched comparison

| Route | What is established | Evidence maturity | What it could control | What remains blocked |
|---|---|---|---|---|
| **Intel OCI / silicon photonics** | Live OCI chiplet co-packaged with an Intel CPU; 4 Tb/s bidirectional, 64×32 Gb/s per direction, up to 100 m SMF; on-chip DWDM lasers/amplifiers; Intel claims >8M PICs and >32M integrated lasers shipped in pluggables | Prototype/select-customer evaluation; prior pluggable volume is not OCI volume | PIC integration, on-chip lasers, accelerator optical-I/O architecture and prior process experience | OCI production units, 200G/lane implementation, final-engine yield, fibre attach, qualification, field reliability, ASP and margin |
| **Cisco system/LPO comparator** | 51.2T demonstration with 64×800G linear pluggables; Cisco reports 30% system-power reduction versus traditional retimed optics and states module/platform qualification plus multisource supply-chain work | System demonstration and company qualification claim | System architecture, customer qualification process, multisource procurement and LPO alternative | Controlled CPO comparison, 200G/400G lane evidence, production CPO units, engine supplier/content, yield, ASP and margin |
| **Acacia 200G/lane engine** | Official 200G/lane silicon-photonic engine family paired with 3 nm Kibo 1.6T PAM4 DSP; targets 1.6T/800G; >1M prior 100G/lane engines claimed shipped in 12 months | Product announcement with prior-volume baseline; 200G qualification unknown | Silicon-photonic engine and DSP co-design, prior manufacturing scale, client-optics route | 200G production units, matched power/BER/TDECQ, attach loss/yield, qualification, CPO attribution, ASP and margin |
| **Ranovus ODIN / Jabil** | Monolithic EPIC integrates lasers, modulators, photodetectors, drivers, TIAs and control loops; Jabil collaboration intended to enable high-volume CPO/NPO production at 800G/6.4T | Planned manufacturing route; no retained shipment evidence | Complete-engine function integration and contract-manufacturing scale | Customer SKU, production date, final-engine yield, Jabil content share, qualification, ASP, margin, service and field reliability |

## Economic interpretation

### Intel

Intel's prior PIC/laser shipment claim is useful evidence that silicon-photonic process capability can reach meaningful pluggable volume. It cannot be transferred to OCI/CPO because the chiplet is explicitly a prototype/select-customer evaluation and the reported 5 pJ/bit comparison has a different measurement boundary. Intel is therefore a credible accelerator optical-I/O technology route, not a currently evidenced scale-out CPO profit-pool leader.

### Cisco and Acacia

Cisco and Acacia should be separated even though Acacia is a Cisco company. Cisco's system demonstration and qualification language describe the customer/system boundary; Acacia's announcement describes the engine/DSP boundary. The public packet does not connect the 200G/lane Acacia engine to Cisco's 51.2T demonstration or to a CPO SKU. The prior 100G/lane shipment claim is a manufacturing baseline, not evidence of 200G/lane or CPO revenue.

### Ranovus/Jabil

ODIN is the clearest monolithic-engine countercase in this group because it integrates the analog optical functions and names a manufacturing partner. “Enable high-volume production” is a planned route, not a qualified-output observation. The key diligence question is whether Jabil captures value-added assembly/test economics or mainly provides capacity while Ranovus retains the PIC/engine value; no public contract or margin evidence answers it.

## Relative position against the core group

| Question | Second-group evidence-adjusted read |
|---|---|
| Earliest 200G/lane product route | Acacia has a direct 200G/lane engine announcement, but no qualification or shipped-volume proof; Broadcom/NVIDIA have stronger switch-side timing claims |
| Strongest prior PIC volume baseline | Intel's >8M PIC / >32M integrated-laser pluggable claim, but outside OCI/CPO |
| Strongest complete-engine integration concept | Ranovus ODIN's monolithic EPIC, but manufacturing and customer conversion are planned |
| Strongest service/multisource comparator | Cisco's LPO/system qualification and multisource approach, but not a controlled CPO result |
| Profit-pool leader | None established; content, share, ASP, yield and margin are missing for every route |

## Required next records

1. Intel OCI or Acacia 200G/lane qualification report with lane BER/TDECQ, temperature and package power.
2. Cisco/Acacia product BOM linking the engine, DSP, laser and package to a named 1.6T or 800G SKU.
3. Ranovus/Jabil line qualification, final-engine yield, customer SKU and supply agreement.
4. Customer-side shipment units, repeat orders and field-service data for any of these routes.
5. Product ASP, supplier share, warranty allocation, price-down and capex terms.

## Sources

- [Intel OCI and silicon-photonics platform record](../01-sources/product-materials/CMP-035-intel-oci-chiplet-ofc2024.md), `CMP-035`, `CLM-304`–`CLM-305`.
- [Ranovus/Jabil ODIN manufacturing record](../01-sources/product-materials/CMP-036-ranovus-jabil-odin-mass-production.md), `CMP-036`, `CLM-306`.
- [Cisco CPO/LPO supply-chain record](../01-sources/product-materials/CMP-037-cisco-ai-networking-cpo-supply-chain.md), `CMP-037`, `CLM-307`–`CLM-308`.
- [Acacia 200G/lane engine record](../01-sources/product-materials/CMP-038-acacia-200g-lane-optical-engine-2025.md), `CMP-038`, `CLM-309`–`CLM-311`.

Company announcements establish what each company claims. They do not independently establish production yield, customer qualification, supplier economics or sustainable profit.
