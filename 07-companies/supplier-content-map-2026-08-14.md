# CPO supplier-content map — confirmed roles versus attribution gaps

**Status:** Private attribution control; not a bill of materials, share estimate or revenue model  
**As of:** 2026-08-14

## Status convention

- **Confirmed:** a retained source names a company and its role at the stated system boundary.
- **Partnered:** a partnership, technology route or ecosystem relation is named, but product allocation/share is not.
- **Unknown:** no retained source identifies the role for the exact system.

Confirmed role is never confirmation of supplier share, ASP, yield, warranty ownership, revenue or margin.

## NVIDIA Spectrum-X Ethernet Photonics (`SN6810` / `SN6800`)

| System boundary | Status | Companies / evidence | Attribution limit |
|---|---|---|---|
| ASIC / SerDes / platform | **Confirmed** | NVIDIA owns the product/platform boundary. | CPO-specific ASP and margin unknown. |
| EIC | **Unknown** | NVIDIA describes integrated architecture but no EIC allocation. | Design, fabrication and economic owner unknown. |
| PIC / engine | **Confirmed process role** | TSMC is named for silicon photonics and COUPE EIC/PIC integration. | Wafer/die/engine scope, qualified share and price unknown. |
| External laser | **Confirmed shared process roles** | TFC: laser-module packaging/validation; Lumentum, Sumitomo and Coherent: shared ELS assembly/alignment/test ecosystem. | Laser-die source, module allocation, number per SKU, redundancy and margin unknown. |
| Fibre / FAU / connector | **Partnered** | NVIDIA states final fibre attach; SENKO identifies detachable photonic connectors for the product family. | Exact-SKU allocation, attach owner, loss/yield/rework and service responsibility unknown. |
| Package / OSAT | **Confirmed process role** | SPIL: bumping, wafer sort, assembly and test for CPO multi-chip module. | Scope, final yield, test time, cost and warranty allocation unknown. |
| System assembly | **Confirmed route** | Foxconn is named for system assembly; Dell is an OEM/channel route. | Exact SKU/customer allocation, unit volume and retained system economics unknown. |
| Test / qualification | **Confirmed process role** | SPIL and NVIDIA pre-shipment validation; shared ELS alignment/test roles. | Test coverage, escape, rework, accepted-output and field-return data unknown. |

**Plausible capture points:** NVIDIA platform/ASIC; TSMC SiPh/EIC process; SPIL package/test; external-light suppliers; connector/FAU suppliers. **None has public same-SKU content share or profit attribution.**

## Broadcom TH6-Davisson / `BCM78919`

| System boundary | Status | Companies / evidence | Attribution limit |
|---|---|---|---|
| ASIC / SerDes / platform | **Confirmed** | Broadcom owns BCM78919 and Condor SerDes product boundary. | CPO-specific price/margin unknown. |
| EIC | **Unknown** | No retained component allocation. | Owner, package boundary and economics unknown. |
| PIC / engine | **Partnered process route** | Broadcom specifies integrated engines and names TSMC COUPE technology. | Engine/PIC supplier, share and transfer price unknown. |
| External laser / ELSFP | **Confirmed interface; unknown supplier** | Field-replaceable ELSFP is defined. | Laser/ELSFP vendor, allocation, lifetime, ASP and warranty unknown. |
| Fibre / FAU / connector | **Partnered** | Corning describes faceplate-to-chip optical-assembly collaboration. | Attach/FAU scope, qualified share, yield, rework and cost unknown. |
| Package / OSAT | **Unknown** | CPO is integrated but no OSAT/package owner is named. | Assembly, thermal qualification, final yield and capex unknown. |
| Test / qualification | **Unknown** | Historical TH5 records and partner qualification dashboards do not establish TH6 test ownership. | Test owner, coverage, acceptance population and economics unknown. |

**Plausible capture points:** Broadcom platform/SerDes; TSMC process; Corning interconnect; unnamed laser/OSAT/test suppliers. **Attribution beyond platform silicon remains speculation.**

## Six-company investment relevance

| Company | Most plausible control point | Publicly confirmed at exact CPO SKU? | Investment implication |
|---|---|---|---|
| NVIDIA | Platform/ASIC and system integration | Product route, not customer-scale economics | Strategic positive exposure; CPO profit capture unproven. |
| Broadcom | Merchant switch/SerDes | Product definition, not customer-scale economics | Positive enabling exposure; engine profit capture unproven. |
| Coherent | Laser/PIC/engine capability | No exact-SKU content allocation | Component watch, not a proven content winner. |
| Lumentum | External light / UHP laser | Product-family ecosystem role; order boundary broad | Strongest component conversion signal, but content/margin unproven. |
| TSMC | SiPh/EIC integration and advanced packaging process | Process route, not complete-engine ownership | Manufacturing-control watch. |
| Marvell | Accelerator optical-I/O chiplet | Outside switch-CPO boundary | Separate scale-up optionality watch. |

## Promotion rule

Assign a company an economic role only after one product-matched record provides supplier, layer, qualified share/volume, commercial term or attributable economics. Until then, preserve **confirmed role**, **partnered route** and **unknown** separately.
