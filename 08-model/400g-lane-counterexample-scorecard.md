# 400G/lane counterexample scorecard

**Owner:** Nur Alpys  
**As of:** 2026-08-10  
**Status:** Evidence comparison; not an adoption forecast or investment recommendation

## Purpose

This table prevents a common analytical error: treating 400G/lane capability as proof that CPO must win. The records below demonstrate different portions of the link and package boundary, so they are not directly interchangeable. The relevant question is which architecture clears the complete system, manufacturing, service and economic gates first.

| Architecture / record | What is actually demonstrated | Reach / FEC boundary | Thermal / packaging boundary | What remains unproven |
|---|---|---|---|---|
| Advanced pluggable / TFLN FR8-DR8 (`PAP-054`) | 225-GBaud PAM4 with TFLN MZMs and 3-nm SerDes; 8 × 420.5 Gb/s net at 2 km; 3.36 Tb/s aggregate | 2 km under 7% HD-FEC; DR8 also 500 m and 2 km; 5-km result falls to 3.0 Tb/s under 20% SD-FEC | Uncooled QD-DFB sweep 30–85°C at 500 m; laboratory packaged TFLN/laser setup | Module/chassis power, production yield, fibre attach, field qualification, serviceability, ASP and margin |
| Advanced pluggable / InP MZ PIC (`PAP-053`) | 100-GHz-class TEC-less eight-channel InP MZ PIC; full paper reports 400 Gb/s/lane over 500 m, broadly temperature-insensitive BER and adjacent-channel crosstalk below −30 dB to 90 GHz | Full paper still does not establish a complete FEC/TDECQ or end-to-end module boundary | 20–80°C; approximately 12 dB MZM insertion loss and approximately +8 dBm receiver sensitivity in the stated TIA-less test | Module power, driver/PIC co-package, yield, qualification, service, customer and economics |
| LPO, 400G component/model (`PAP-011`) | 160/180-GBd component measurements; 212.5-GBd model | Modeled 212.5-GBd case passes up to 12 dB B2B loss under stated assumptions; 15 dB fails | Electrical-path model; no complete package | Measured 212.5-GBd link, optical reach, chassis power, yield, reliability and cost |
| TGV/2.5D active package (`PAP-046`) | 110-GHz measured TGV/RDL bandwidth; 128-Gb/s OOK eyes; flip-chip EML integration | OOK interposer/active-chip test, not 400G/lane end-to-end | Single EML output falls from 4.9 dBm pre-package to −0.07 dBm post-package in reported test | Complete driver/EML link, fibre coupling distribution, yield, rework, thermal qualification and economics |
| CPO/FOWLP engine (`PAP-029`) | Full three-page paper reports a 1.6-Tb/s aggregate, eight-channel, 224-Gb/s/λ FOWLP engine with known-good dies, TMV/RDL and PAM4 eyes | 112-Gb/s NRZ and 224-Gb/s PAM4; 31-tap FFE TDECQ 2.08 dB | Fan-out package with <0.5 dB S21 at 50 GHz; laboratory engine | 400G/lane, full system reach, production yield, service and margin |
| CPO/FOWLP engine (`PAP-045`) | Full journal paper reports a 1.6-Tb/s-class eight-channel FOWLP engine, 112-Gbaud NRZ/PAM4, wafer-level testing and direct-drive PAM4 TDECQ around 2.08 dB with 31-tap equalization and 2.32 dB direct drive | 224-Gb/s/lane PAM4; no 400G/lane result | Reconstituted molded-wafer FOWLP; optical-edge protection and organic RF substrate; full-engine power not reported | Production yield, test/rework economics, thermal qualification, service, customer, ASP and margin |
| Full-module assembly (`PAP-036`) | Intel open-cavity EMIB package with three EIC-PIC stacks and 56 fibre couplers at 127-µm pitch | No complete lane-rate/link result | Prototype flow reports approximately 50% substrate loss after thermal pre-screening and approximately 90% cumulative loss after later attach exposures | Production yield denominator, Cpk, cycle time, complete link, field qualification and economics |
| Driver-modulator engine (`PAP-051`) | 76-GHz InP MZM with 224-GBd-class EML driver; 180-GBd PAM4 back-to-back below 20%-HD-FEC BER threshold | Back-to-back only; no fibre-attached reach | Measured at 40°C under TEC control; stated 1.45 pJ/bit excludes DSP, external laser and TEC | Complete engine/system power, fibre attach, qualification, yield and economics |

## Interpretation

1. **Lane-rate feasibility is no longer the deciding gate.** PAP-053 and PAP-054 show that advanced-pluggable PIC/transmitter paths can reach a 400G-class boundary in laboratory conditions.
2. **CPO’s burden is system-level.** It must demonstrate a complete advantage after including electrical reach, laser distribution, package loss, cooling, attach/test, rework and service.
3. **The most decision-relevant missing comparison is matched.** Use the same host SerDes, aggregate bandwidth, optical reach, FEC, temperature, inlet power, failure domain and service procedure for CPO, NPO, LPO and advanced pluggables.
4. **PAP-046 is a warning against abstract packaging optimism.** A fast TGV interposer does not guarantee a low-loss optical engine after active-chip attach and fibre coupling.
5. **Profit leadership remains separate from technical leadership.** Even a technically superior engine needs qualified yield, repeat customer volume, supplier share, ASP, margin and warranty evidence before entering the profit-pool model.

## Required next experiment / evidence request

The highest-value missing record is a matched 400G/lane system comparison with:

```text
same host SerDes and workload
same 500 m / 2 km reach options
same FEC threshold and BER/TDECQ reporting
same 20–80°C operating range
inlet power including laser, driver/TIA, DSP/equalization and cooling
package/attach/test/rework assumptions
service replacement time and failure-domain treatment
```

Until that record exists, the evidence-adjusted conclusion is: **advanced pluggables have a credible 400G-class technical countercase; CPO remains a system-integration and economics thesis, not a lane-rate inevitability thesis.**
