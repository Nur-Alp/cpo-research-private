# CMP-048 — NVIDIA Spectrum-6 SN6000 hardware manual: CPO versus pluggable SKU boundary

## Bibliographic record

- **Publisher:** NVIDIA Corporation
- **Document:** NVIDIA Spectrum-6 SN6000 Ethernet Switch Systems Hardware User Manual
- **Canonical PDF:** https://docs.nvidia.com/nvidia-spectrum-6-sn6000-ethernet-switch-systems-hardware-user-manual.pdf
- **Local retained copy:** `CMP-048-nvidia-sn6000-hardware-manual-full.pdf`
- **Reviewed:** 2026-08-08

## What the manual establishes

The manual distinguishes the 102.4 Tb/s SN6000 family by physical optical architecture:

- **SN6600-LD:** fully liquid-cooled, 64 RHS-type OSFP cages, 128 ports up to 800 Gb/s, and a **pluggable RHS-transceiver ecosystem** in a 2RU chassis.
- **SN6810-LD:** single Spectrum-6 ASIC, 102.4 Tb/s, silicon photonics and **co-packaged optics (CPO)** in a 2RU liquid-cooled design.
- **SN6800-LD:** four-ASIC, 409.6 Tb/s class platform using high-density optical connectors and CPO.

The document was created/modified in May 2026 and is a product-family hardware manual, not a marketing-only CPO overview.

## Bounded within-family power specification

The manual's specifications table lists **1.96 kW typical / 2.2 kW maximum**
global power for the `SN6810-LD` CPO system. It separately lists **3.3 kW
typical with fully retimed optics (FRO)** and **3.2 kW typical with transmit
retimed optics (TRO)** for the pluggable `SN6600-LD` system. This is a useful
same-family vendor specification at 102.4 Tb/s, but it is **not** a matched
fleet measurement: the optical configuration, traffic, ambient, pump/fan
allocation, external-light boundary, measurement method and service economics
are not reconciled. It may inform the power evidence column only; it must not
be treated as a complete CPO-versus-pluggable TCO or margin result.

## Critical correction to the customer-proof register

The manual means a customer statement that it deployed an **SN6600-LD** establishes deployment of a liquid-cooled 102.4 Tb/s switch with pluggable optical cages, not deployment of an SN6810-LD/SN6800-LD CPO switch. CoreWeave's separate statement that it is an early adopter of NVIDIA Photonics CPO remains relevant, but the public records do not tie that CPO statement to the SN6600-LD SKU. The two claims must not be merged.

## Evidence boundary

## Deployment and service-procedure boundary

The current manual also supplies a narrower operational fact for the CPO
systems: its liquid-cooling deployment section requires nitrogen-pressure
verification before installation. It describes a pressure-hold procedure that
refills the system to 50 psi, waits 12 hours and requires pressure above 48 psi;
it warns that powering on before liquid has fully flooded the cooling system can
cause damage and void the warranty.[CLM-564]

This establishes a documented deployment-handling control, not a customer
acceptance, engine replacement procedure, achieved MTTR, field-failure rate,
warranty reserve or installed-base denominator. It makes the CPO service gate
more specific, but it does not close it.

The manual does not disclose customer units, qualification lots, optical-engine suppliers, final yield, ASP, margin, field reliability or repeat shipments. It does, however, resolve the prior ambiguity about treating SN6600-LD's 64 OSFP cages as a CPO-engine denominator.

## Investment-model use

Use CMP-048 to downgrade CoreWeave/SN6600-LD from named switch-side CPO deployment evidence to a pluggable-platform deployment record, and to preserve SN6810-LD/SN6800-LD as the relevant NVIDIA CPO SKU families until customer-side evidence identifies their deployment.
