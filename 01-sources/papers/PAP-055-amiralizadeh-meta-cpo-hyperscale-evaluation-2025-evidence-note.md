# PAP-055 — Amiralizadeh et al., Meta/Broadcom 51.2T CPO evaluation

## Citation

Siamak Amiralizadeh *et al.*, “Co-Packaged Optics Technology Evaluation for Hyperscale Data Center Fabric Switches,” *ECOC 2025*, pp. 1–4, DOI [10.1109/ECOC66593.2025.11263202](https://doi.org/10.1109/ECOC66593.2025.11263202).

## What was reviewed

The complete four-page IEEE-authorized PDF was retrieved through university access, visually checked page by page, and retained locally on 2026-08-13.

## Full-paper evidence

- The authors describe a 51.2 Tb/s Bailly CPO switch built around a Broadcom Tomahawk 5 ASIC, with eight 6.4-Tb/s silicon-photonic optical engines and 128 × 400G FR4 ports in a 4RU system.
- In the reported comparison, 120 optical engines and 240 pluggable laser sources across 15 CPO systems were measured at 40°C ambient; 48 retimed 2 × 400G FR4 pluggables from four vendors were measured at 70°C module-case temperature. The authors report 65% lower optics power for the CPO configuration and more than 500 W savings relative to a fully populated Minipack3 system.
- The CPO units were operated in 128 × 400G self-loopback at 40°C ambient, with key metrics recorded every five minutes. The authors report no uncorrectable codewords over more than one million 400G-port device-hours; 75% of ports had a maximum non-zero KP4-FEC bin below 7 after 1.05 million device-hours.
- The paper states that Bailly optical-engine failure requires whole-chassis replacement, while pluggable laser sources are field-replaceable. It therefore treats removable lasers as a service and supply-risk boundary, not a field-replaceable optical-engine result.

## Evidence boundary

This is a historically important **system-test and reliability record**, but it is not evidence of current Tomahawk 6/102.4T deployment, external customer procurement, accepted-unit volume, field-return rate, final-engine production yield, supplier content allocation, ASP, warranty reserve or margin. Its CPO-versus-pluggable power comparison is informative but not matched on the same temperature boundary, so it must not be used as an all-in chassis-power or total-cost result. Claims are recorded as `CLM-574`–`CLM-577`.

## Research use

Use PAP-055 to anchor the historical switch-CPO lab/prototype route and to sharpen the serviceability test. It raises the evidence floor above a single lab component result, while leaving the 2026–27 commercial-proof and profit-capture gates open.
