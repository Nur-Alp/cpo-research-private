# CPO Adoption Timeline Model

**Model horizon:** 2026 to 2032
**Status:** Evidence-calibrated milestone model; annual adoption probabilities are not yet numerically eligible
**Last updated:** 2026-08-07

## Decision discipline

The final question is not whether an architecture has a product announcement. It is which architecture first reaches commercial proof and then meaningful adoption in a defined deployment domain. Those are different observations and must use different denominators.

This model keeps eight architecture/domain combinations separate:

1. Retimed and advanced pluggables — Ethernet scale-out.
2. LPO — Ethernet scale-out, separated by 100G, 200G and 400G per lane.
3. Switch-side CPO — highly optically attached Ethernet scale-out.
4. Switch-side CPO — 100G/lane historical production baseline, kept separate from 200G/lane.
5. NPO/OBO — switch or XPU-adjacent scale-out/scale-up where a near-package electrical path is sufficient.
6. Accelerator optical I/O — scale-up chiplet/inter-XPU fabric.
7. MOSAIC wide-and-slow microLED links — rack-scale optical countercase.
8. Inter-rack scale-up CPO — accelerator-world-size expansion, distinct from switch-side Ethernet CPO and accelerator optical I/O chiplets.

Do not add their shares together. They have different electrical channels, service models, suppliers and adoption denominators.

## Terms and forecast units

- **Commercial proof** means repeat paid production from two independent customers, or sustained/repeated production by one major customer. [Terminology](../00-scope/terminology.md)
- **Meaningful adoption** means at least 10% of a clearly defined domain or revenue materiality to the relevant supplier. [Terminology](../00-scope/terminology.md)
- **Adoption rate** is the share of relevant *systems* using a precisely defined architecture in a stated year. It is not a port share, engine share, optical-dollar share or supplier revenue share.
- **Probability of commercial proof** is the likelihood, assessed before the period, that the definition above is met by year end. It is not the adoption rate.

## Current evidence snapshot

| Architecture and domain | Best current public evidence | Evidence-adjusted maturity state | What this establishes | What it does not establish |
|---|---|---:|---|---|
| Retimed / advanced pluggables, 102.4T Ethernet scale-out | Arista reports a live 102.4T demonstration with 1.6T linear, linear-receive and fully retimed optics. [CLM-001 to CLM-004] | 2 — integrated-system demonstration | A 102.4T pluggable path is technically plausible. | Qualification, full production, total cost or system adoption. |
| LPO, 100G/lane Ethernet scale-out | Meta’s reviewed academic work measures a 51.2T 100G/lane LPO system; later LPO literature reports an indirectly cited initial-production claim. [CLM-056; CLM-064] | 2 to 3 — system demonstration / indirect initial-production evidence | 100G LPO has stronger system evidence than 200G/400G LPO. | Named customer, repeat volume, field reliability or a broadly defined adoption rate. |
| LPO, 200G/lane Ethernet scale-out | Reviewed work supplies conditional models/design studies, not a matched measured complete system. [CLM-057; CLM-059; CLM-063; CLM-067] | 1 to 2 — component/system modelling | Electrical-loss and return-loss requirements are central. | Qualified 200G LPO production, durability or adoption timing. |
| LPO, 400G/lane Ethernet scale-out | 160/180-GBd components were measured; 212.5-GBd/400G link behaviour is modeled only. [CLM-065; CLM-066; CLM-067] | 1 — component demonstration | A short electrical path is likely important at this lane rate. | A complete 400G/lane LPO implementation. |
| Switch-side CPO, 100G/lane Ethernet scale-out | Broadcom reports TH5-Bailly as a 100G/lane volume-production CPO solution and cites Micas/Delta production systems. [CLM-199; CLM-200] | 4 — partner-reported volume-production baseline | A switch-side CPO product reached a reported production state at 100G/lane. | Audited units, repeat orders, customer identity, final-engine yield, margin and field/service economics. |
| Switch-side CPO, 200G/lane Ethernet scale-out | Broadcom documents TH6-Davisson’s 102.4T/16-engine configuration; NVIDIA claims 200G-SerDes CPO switches are in production. Broadcom separately reports a 100G/lane TH5-Bailly volume-production baseline with Micas/Delta partner systems. [CLM-076; CLM-077; CLM-079; CLM-199; CLM-200] | 3 to 4 — 100G/lane partner-reported volume baseline; 200G/lane vendor-asserted limited production | A credible integrated CPO product path exists, with historical 100G production evidence and 200G commercial progress. | Customer-confirmed 200G CPO units, repeat production, field reliability, economics or meaningful 200G system adoption. |
| NPO/OBO, 224G-class scale-up and scale-out | Lightmatter announced a 6.4-Tb/s-per-direction NPO/OBO engine and expected late-2026 sampling; a Huawei IEEE contribution proposes a short exposed NPO electrical boundary at 400G/lane. [CLM-086; CLM-091] | 0 — announced roadmap | A dated product milestone and a plausible interoperability direction exist. | Observed samples, qualification, production or customer deployment; an adopted interface. |
| Accelerator optical I/O, scale-up | Ayar Labs claims an 8-Tb/s UCIe optical-I/O chiplet; Marvell claims a 16-Tb/s Celestial Photonic Fabric chiplet and forecasts a FY28/FY29 commercial ramp. [CLM-085; CLM-094; CLM-095] | 1 — component/product announcement | Multiple credible public technical candidates and a dated management revenue case exist. | Customer-qualified production, system volume, yield, installed base or achieved revenue. |
| MOSAIC wide-and-slow microLED optical links, rack-scale countercase | Microsoft reports a measured 100-channel prototype and simulates an 800 Gb/s pluggable module to 50 m. [CLM-116; CLM-117; CLM-119] | 1 — prototype plus architecture simulation | A non-laser optical path could reduce link power and add channel redundancy. | No qualified 800 Gb/s module, CPO implementation, production yield, customer or ecosystem evidence. |
| Inter-rack scale-up CPO, NVIDIA roadmap | NVIDIA describes 200G CPO in Spectrum-6, a fully functional Polyphe NVL576 prototype using direct optical connections, and a Kyber/NVL1152 direct-optical roadmap. [CLM-189–CLM-191] | 2 — primary roadmap plus functional prototype; no observed production | A defined deployment domain, a first-party architecture boundary and a functional prototype exist. | No observed NVL576/NVL1152 production system, customer confirmation, firm shipment date, optical-engine content, yield, service or economics. |

The maturity state is deliberately conservative. A company’s use of “production” is recorded as a company claim unless customer-side evidence identifies the configuration, deployment and repeat volume.[CLM-077][CLM-079][CLM-081]

TSMC’s COUPE evidence should be read as a manufacturing-enabler checkpoint, not as a ninth adoption denominator. TSMC reports a 200G result with several customers, >99% 3D-stacking yield on engineering samples, and COUPE-on-substrate CPO beginning production in 2026. These records strengthen the process/stacking readiness of a 200G engine route, but they do not establish a shipped switch, final-engine yield, customer qualification or supplier revenue.[CLM-213][CLM-214][CLM-215][CLM-216]

## Evidence-calibrated critical path

| Architecture | Next observable milestone | Earliest source-supported timing | Gate affected | What would upgrade the state |
|---|---|---|---|---|
| 100G LPO | Named customer/system plus repeat production and field data | Not stated in reviewed source set | Commercial; reliability | Customer confirmation, units/ports, repair/failure evidence. |
| 200G LPO | Measured multi-vendor end-to-end system at disclosed loss, return loss, FEC, reach and temperature | No source-supported date | Technical; product | Full system data, qualification and deployment record. |
| 400G LPO | Measured 212.5-GBd end-to-end link and production-compatible package | No source-supported date | Technical; manufacturing | A completed link, rather than the present model, then qualification evidence. [CLM-065; CLM-066] |
| Switch CPO | Customer-side confirmation of a named TH6-Davisson or Spectrum-X Photonics deployment | No source-supported date | Commercial; reliability | Units/ports, customer, service history and repeat order/operating evidence. |
| NPO/OBO | Lightmatter Passage L20 sample availability | Late 2026 is the company’s expected date, not observed delivery. [CLM-086] | Product | Observed sample, named qualification and measured system evidence. |
| Accelerator optical I/O | Named production XPU/rack deployment using an optical chiplet | No source-supported date | Product; manufacturing; commercial | Customer, topology, qualified yield, repeat volume and field use. [CLM-085] |
| MOSAIC wide-and-slow optical | Simultaneous 800 Gb/s hardware with production microLED/CMOS bonding, imaging-fibre termination and reliability data | No source-supported date | Product; manufacturing; reliability | Measured aggregate module, qualified packaging, yield, service model and customer deployment. [CLM-116; CLM-118; CLM-119] |
| Inter-rack scale-up CPO | Customer or NVIDIA confirmation of an NVL576-class production deployment after the Polyphe prototype | NVIDIA primary roadmap and prototype evidence; no source-supported production date [CLM-190; CLM-191] | Commercial; manufacturing; serviceability | Named system, rack topology, optical endpoints, supplier content, qualification and repeat deployment. [CLM-190; CLM-191] |
| TSMC COUPE process / engine route | Actual conversion of the 2026 COUPE-on-substrate milestone into a qualified customer product | Beginning production is a company milestone; no source-supported shipped volume date [CLM-215; CLM-216] | Manufacturing; product; commercial | Named SKU, shipped units, final-engine yield, package responsibility, ASP and margin. |

## Why no annual percentage is populated yet

An adoption percentage would require an addressable-system denominator plus a confirmed architecture numerator. The current evidence has neither for any of the CPO/NPO/accelerator optical-I/O lines. It also lacks the economic gates that determine whether a technical product converts into adoption: final-engine yield, warranty/service cost, content, supplier share and total cost versus credible alternatives.[CLM-074][CLM-082][CLM-084]

Assigning a percentage today would be a subjective investment view disguised as a fact. The model therefore uses a gated state trajectory first. It can be converted to numeric adoption-rate scenarios only after the relevant gates pass.

## Annual state trajectory — not an adoption forecast

The entries below are *highest evidence-supported state*, not probabilities or system shares. A dash means the current source set supports no date.

| Architecture and domain | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Retimed / advanced pluggables, 102.4T Ethernet | 2 | — | — | — | — | — | — |
| LPO, 100G/lane Ethernet | 2–3 | — | — | — | — | — | — |
| LPO, 200G/lane Ethernet | 1–2 | — | — | — | — | — | — |
| LPO, 400G/lane Ethernet | 1 | — | — | — | — | — | — |
| Switch-side CPO, 200G/lane Ethernet | 3–4 | — | — | — | — | — | — |
| NPO/OBO, 224G-class | 0; sampling expected late 2026 | — | — | — | — | — | — |
| Accelerator optical I/O, scale-up | 1 | — | — | — | — | — | — |
| MOSAIC wide-and-slow optical | 1 | — | — | — | — | — | — |
| Switch-side CPO, 100G/lane Ethernet | 4; partner-reported volume-production baseline | — | — | — | — | — | — |
| Inter-rack scale-up CPO | 2; primary roadmap plus functional prototype, no observed production | — | — | — | — | — | — |

## Conditions for scenario probabilities

Once a line has a confirmed numerator and denominator, populate bear/base/bull *adoption-rate* scenarios as ranges, not point estimates. Each scenario must identify the source, link to the relevant claim IDs, and state which gates have passed.

| Scenario | Required preconditions | Example output form |
|---|---|---|
| Bear | Technical/product milestone slips or qualification is not completed; alternatives remain viable. | `2028 CPO system adoption: 0–x%, contingent on no commercial proof` |
| Base | Defined customer deployment, repeat volume, yield/reliability at a stated boundary and positive total-cost case. | `2028 CPO system adoption: x–y%, source-defined domain` |
| Bull | Multiple customers, repeat production, reliable supply, second source where relevant and a demonstrated economic advantage. | `2028 CPO system adoption: y–z%, source-defined domain` |

Until the preconditions are met, a scenario belongs in a qualitative decision tree, not an earnings model.

## Required record for every change

```text
milestone_id
architecture
deployment_domain
system_generation / lane rate
company or customer
milestone
planned_date
observed_date
state_before
state_after
evidence_id
source_id
source_retained_or_canonical_link
gate_affected
probability_or_adoption_rate_before
probability_or_adoption_rate_after
reason_for_change
disconfirming_evidence
```

## Research conclusion today

Switch-side CPO has the strongest current commercial-maturity signal at 200G/lane, but no public evidence set yet proves the commercial-proof threshold. Broadcom's primary Meta characterization materially improves the reliability evidence while leaving field, population and service-cost gates open. TSMC's COUPE milestones strengthen the process/stacking route behind a 200G CPO engine, but remain a manufacturing checkpoint rather than customer-confirmed switch adoption. NVIDIA's primary Vera Rubin/NVLink material upgrades inter-rack scale-up CPO from a secondary roadmap interpretation to a first-party roadmap with a functional NVL576 prototype; it still does not establish customer production. SemiAnalysis adds an important economic distinction: scale-out CPO may face a TCO/serviceability and margin-stack hurdle, while inter-rack scale-up CPO has a stronger strategic rationale because it expands accelerator-domain size. 100G LPO has stronger system evidence than 200G or 400G LPO, while 200G/400G LPO remains bounded by incomplete/modeled electrical-link evidence. NPO and accelerator optical-I/O remain earlier public maturity states despite credible product announcements. This is a maturity and domain-value ranking, not a forecast of adoption or a company investment conclusion. [CLM-177; CLM-178; CLM-190; CLM-191; CLM-192; CLM-213–CLM-216]

## Evidence links

- [Switch CPO platform dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [External optical-engine supplier dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md)
- [102.4T switch CPO versus advanced pluggables](../02-architecture/102.4t-cpo-vs-advanced-pluggables.md)
- [Linear-drive boundary benchmark](../02-architecture/linear-drive-boundary-benchmark.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [MOSAIC microLED countercase](../02-architecture/mosaic-microled-countercase.md)
- [Source log](../01-sources/source-log.csv) and [claim ledger](../01-sources/claim-ledger.csv)

All source IDs and claim IDs are defined in the linked records. Company announcements establish what companies say; they do not, by themselves, prove adoption, field performance or sustainable economics.
