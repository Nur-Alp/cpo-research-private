# CPO Adoption Timeline Model

**Model horizon:** 2026 to 2032
**Status:** Evidence-calibrated milestone model; commercial-proof probability priors are now explicit, while adoption-share probabilities remain denominator-gated
**Last updated:** 2026-08-10

Use the [substitution and falsification matrix](../02-architecture/substitution-and-falsification-matrix-2026-08-12.md)
before changing an architecture state: a vendor milestone does not advance
adoption unless the matched alternative and service/economic gates are tested.

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
| Retimed / advanced pluggables, 102.4T Ethernet scale-out | Arista reports a live 102.4T demonstration with 1.6T linear, linear-receive and fully retimed optics; OIF-EEI-112G-RTLR defines a hot-pluggable interoperable retimed-transmitter/linear-receiver boundary with 200 mm host-trace capability and explicit BER/FEC requirements. [CLM-001 to CLM-004; CLM-297–CLM-300] | 2 — integrated-system demonstration plus standards-defined RTLR comparator | A 102.4T pluggable path is technically plausible and a concrete RTLR interface exists for the 112G/200G-class boundary. | Qualification, full production, module power, total cost, field reliability or system adoption. |
| LPO, 100G/lane Ethernet scale-out | Meta’s reviewed academic work measures a 51.2T 100G/lane LPO system; later LPO literature reports an indirectly cited initial-production claim. [CLM-056; CLM-064] | 2 to 3 — system demonstration / indirect initial-production evidence | 100G LPO has stronger system evidence than 200G/400G LPO. | Named customer, repeat volume, field reliability or a broadly defined adoption rate. |
| LPO, 200G/lane Ethernet scale-out | Reviewed work supplies conditional models/design studies, not a matched measured complete system. [CLM-057; CLM-059; CLM-063; CLM-067] | 1 to 2 — component/system modelling | Electrical-loss and return-loss requirements are central. | Qualified 200G LPO production, durability or adoption timing. |
| LPO, 400G/lane Ethernet scale-out | The full three-page PAP-011 paper measures 160/180-GBd PAM4 component operation and models a 212.5-GBd implementation; the modeled result passes at ≤12 dB B2B loss but fails at 15 dB under the stated equalization assumptions. [CLM-065; CLM-066; CLM-067] | 1 — measured component plus modeled system boundary | A short electrical path is likely important at this lane rate, strengthening the case for NPO/CPO when host loss exceeds the modeled boundary. | A measured 212.5-GBd/400G end-to-end LPO link, qualification, production or adoption. |
| Switch-side CPO, 100G/lane Ethernet scale-out | Broadcom reports TH5-Bailly as a 100G/lane volume-production CPO solution and cites Micas/Delta production systems. [CLM-199; CLM-200] | 4 — partner-reported volume-production baseline | A switch-side CPO product reached a reported production state at 100G/lane. | Audited units, repeat orders, customer identity, final-engine yield, margin and field/service economics. |
| Switch-side CPO, 200G/lane Ethernet scale-out | Broadcom documents TH6-Davisson’s 102.4T/16-engine configuration and 200G/lane product line; NVIDIA's 2026 release states that 200Gb/s-SerDes Spectrum-X Ethernet Photonics CPO switches are now in production and names CoreWeave, Lambda and OCI among first ecosystem partners/adopters. NVIDIA's June production-ramp article adds a named TSMC/SPIL/TFC/Foxconn manufacturing chain and pre-shipment validation, but still no customer-unit numerator. NVIDIA's January 2026 technical blog adds final-stage fibre attachment, pre-attachment screening and a company-stated “100% yield” claim, but does not define the yield denominator. CoreWeave's separate Photonics-adopter statement is not linked to its named SN6600-LD deployment: CMP-048 classifies SN6600-LD as a pluggable RHS-transceiver switch, while SN6810-LD/SN6800-LD are the CPO families. Celestica reports an unnamed hyperscaler CPO-switch design/manufacturing program with a planned 2027 ramp. Lambda names Spectrum-X Photonics Ethernet only in preparation/roadmap language. Broadcom separately reports a 100G/lane TH5-Bailly volume-production baseline. [CLM-076; CLM-077; CLM-079; CLM-199; CLM-200; CLM-220–CLM-227; CLM-255–CLM-257; CLM-345–CLM-347; CLM-380–CLM-384; CLM-406–CLM-410; CLM-435–CLM-437] | 3 — vendor production/process claims and ecosystem/adopter statements, but no reconciled named customer-side Spectrum-X CPO SKU or unit numerator; separate planned 2027 hyperscaler CPO program | The 200G/lane timing and process signal remains strong at the platform level, but the “100% yield” language is insertion-point ambiguous and the earlier CoreWeave SN6600-LD CPO inference is withdrawn. Customer units, supplier allocation, final-engine yield and repeat volume remain unquantified. | Fleet size, repeat production, qualification, field reliability, economics or meaningful 200G system adoption share. |
| NPO/OBO, 224G-class scale-up and scale-out | Lightmatter announced a 6.4-Tb/s-per-direction NPO/OBO engine and expected late-2026 sampling; a Huawei IEEE contribution proposes a short exposed NPO electrical boundary at 400G/lane. [CLM-086; CLM-091] | 0 — announced roadmap | A dated product milestone and a plausible interoperability direction exist. | Observed samples, qualification, production or customer deployment; an adopted interface. |
| Accelerator optical I/O, scale-up | Ayar Labs claims an 8-Tb/s UCIe optical-I/O chiplet; Marvell claims a 16-Tb/s Celestial Photonic Fabric chiplet and forecasts a FY28/FY29 commercial ramp; Intel has a 4-Tb/s OCI prototype; NVIDIA/Lambda provide a separate Quantum-X production-scale claim. [CLM-085; CLM-094; CLM-095; CLM-304; CLM-224] | 1–3 by route — product announcements and prototypes, with customer production-scale evidence in the separate Quantum-X domain | Multiple credible technical candidates, a dated Marvell revenue case and a customer-side Quantum-X production-scale claim exist, but they are not the same product or numerator. | Exact customer-qualified production topology, system volume, yield, installed base, ASP, margin and achieved revenue. |
| MOSAIC wide-and-slow microLED optical links, rack-scale countercase | Microsoft reports a measured 100-channel prototype and simulates an 800 Gb/s pluggable module to 50 m. [CLM-116; CLM-117; CLM-119] | 1 — prototype plus architecture simulation | A non-laser optical path could reduce link power and add channel redundancy. | No qualified 800 Gb/s module, CPO implementation, production yield, customer or ecosystem evidence. |
| Inter-rack scale-up CPO, NVIDIA roadmap | NVIDIA describes 200G CPO in Spectrum-6, a fully functional Polyphe NVL576 prototype using direct optical connections, and a Kyber/NVL1152 direct-optical roadmap. Lambda separately claims a production-scale GB300 supercluster with Quantum-X InfiniBand Photonics CPO and 10,000+ GPUs. [CLM-189–CLM-191; CLM-224; CLM-225] | 3 — customer production-scale claim plus primary roadmap/prototype; exact SKU and fleet size remain undisclosed | A defined deployment domain now has customer-side production-scale evidence as well as a first-party architecture boundary. | Exact NVL576/NVL1152 or other production SKU, switch count, optical-engine content, yield, service, repeat deployment and economics. |

The maturity state is deliberately conservative. A company’s use of “production” is recorded as a company claim unless customer-side evidence identifies the configuration, deployment and repeat volume.[CLM-077][CLM-079][CLM-081]

Secondary July 2026 reporting adds a triangulation signal that shipments may have begun in limited volumes, while evaluation-versus-commercial use, shipment volume, yield and general availability remain unresolved. Because the underlying TrendForce records are not retained, this does not upgrade the 200G switch-CPO state or create a customer numerator (`NWS-011`, `CLM-411`–`CLM-415`).

TrendForce's retained July 27 press-center record provides a direct research-house corroboration: select-partner Spectrum-X shipments, limited Bailly shipments, optical-engine/SiPh/advanced-packaging bottlenecks and a 2027–2028 ramp view. It still supplies no named customer, SKU, units, repeat order or final-engine yield, so the state remains unchanged (`NWS-012`, `CLM-416`–`CLM-420`).

The OIF fibre-count example adds a manufacturing reason for this conservatism: even a 99.865% assumed per-connection first-pass yield compounds to only about 23.0% board fibre-assembly yield at 1,088 connections. That is an architecture sensitivity, not measured production output, but it means adoption timing must include the fibre-count/yield gate rather than only the switch announcement (`STD-014`, `CLM-397`–`CLM-400`).

The RTLR agreement changes the architecture decision rule but not the maturity score: it proves that the industry has formalized a retimed/linear, hot-pluggable alternative with explicit compliance points, not that the alternative wins on power, cost or field reliability. For 200G/lane, CPO should therefore be treated as one branch in a topology-dependent decision tree; the CPO branch becomes technically favored only when the validated host/channel boundary, power, service and cost gates are worse for RTLR/LPO.[CLM-297][CLM-298][CLM-299][CLM-300]

TSMC’s COUPE evidence should be read as a manufacturing-enabler checkpoint, not as a ninth adoption denominator. TSMC reports a 200G result with several customers, >99% 3D-stacking yield on engineering samples, and COUPE-on-substrate CPO beginning production in 2026. These records strengthen the process/stacking readiness of a 200G engine route, but they do not establish a shipped switch, final-engine yield, customer qualification or supplier revenue.[CLM-213][CLM-214][CLM-215][CLM-216]

## Evidence-calibrated critical path

| Architecture | Next observable milestone | Earliest source-supported timing | Gate affected | What would upgrade the state |
|---|---|---|---|---|
| 100G LPO | Named customer/system plus repeat production and field data | Not stated in reviewed source set | Commercial; reliability | Customer confirmation, units/ports, repair/failure evidence. |
| 200G LPO | Measured multi-vendor end-to-end system at disclosed loss, return loss, FEC, reach and temperature | No source-supported date | Technical; product | Full system data, qualification and deployment record. |
| 400G LPO | Measured 212.5-GBd end-to-end link and production-compatible package | No source-supported date | Technical; manufacturing | A completed link, rather than the present model, then qualification evidence. [CLM-065; CLM-066] |
| Switch CPO | Customer-side confirmation of a named TH6-Davisson or Spectrum-X Photonics deployment, or conversion of Celestica's hyperscaler program into production | NVIDIA now states Spectrum-X Photonics is in production, but no unit numerator or repeat shipment record is source-supported; Celestica's planned ramp is 2027 | Commercial; reliability | Units/ports, customer, service history and repeat order/operating evidence. |
| NPO/OBO | Lightmatter Passage L20 sample availability | Late 2026 is the company’s expected date, not observed delivery. [CLM-086] | Product | Observed sample, named qualification and measured system evidence. |
| Accelerator optical I/O | Named production XPU/rack deployment using an optical chiplet | No source-supported date | Product; manufacturing; commercial | Customer, topology, qualified yield, repeat volume and field use. [CLM-085] |
| MOSAIC wide-and-slow optical | Simultaneous 800 Gb/s hardware with production microLED/CMOS bonding, imaging-fibre termination and reliability data | No source-supported date | Product; manufacturing; reliability | Measured aggregate module, qualified packaging, yield, service model and customer deployment. [CLM-116; CLM-118; CLM-119] |
| Inter-rack scale-up CPO | Customer or NVIDIA confirmation of a production deployment after the Polyphe prototype | Lambda customer-side production-scale evidence exists for Quantum-X Photonics in a GB300 cluster; it does not disclose an NVL576/NVL1152 SKU or unit count [CLM-190; CLM-191; CLM-224; CLM-225] | Commercial; manufacturing; serviceability | Exact system/SKU, switch count, rack topology, optical endpoints, supplier content, qualification and repeat deployment. |
| TSMC COUPE process / engine route | Actual conversion of the 2026 COUPE-on-substrate milestone into a qualified customer product | Beginning production is a company milestone; no source-supported shipped volume date [CLM-215; CLM-216] | Manufacturing; product; commercial | Named SKU, shipped units, final-engine yield, package responsibility, ASP and margin. |

## Why no annual adoption-share percentage is populated yet

An adoption percentage would require an addressable-system denominator plus a confirmed architecture numerator. The current evidence has neither for any of the CPO/NPO/accelerator optical-I/O lines. It also lacks the economic gates that determine whether a technical product converts into adoption: final-engine yield, warranty/service cost, content, supplier share and total cost versus credible alternatives.[CLM-074][CLM-082][CLM-084]

Assigning a percentage today would be a subjective investment view disguised as a fact. The model therefore uses a gated state trajectory first. It can be converted to numeric adoption-rate scenarios only after the relevant gates pass.

The separate [commercial-proof probability priors](commercial-proof-probability-priors.md) now provide bounded analyst ranges for the binary proof event. Those ranges must not be read as system adoption shares, supplier revenue probabilities or earnings forecasts.

## Manufacturing gate overlay

The state trajectory must not advance from “platform production claim” to “meaningful adoption” on announcement language alone. The architecture must also clear the cost-per-qualified-good-engine boundary:

| Adoption transition | Required manufacturing evidence | Current status |
|---|---|---|
| Demonstration → product qualification | Complete engine boundary; measured optical/electrical test; reflow and environmental qualification; connection-count and yield definition | Open for the current 200G/lane CPO numerator; IBM OTV and Teradyne test-flow records are process anchors, not customer qualification (`PAP-042`, `CMP-049`). |
| Product qualification → repeat production | Final-engine yield waterfall, attach/test cycle time, rework recovery, field-replaceable boundary and repeat shipment evidence | Open across the public CPO/NPO set; OIF's 23.0%/67.8% examples are illustrative yield sensitivities, not line output (`STD-014`, `CLM-397`–`CLM-400`). |
| Repeat production → meaningful adoption | Positive matched TCO versus LPO/retimed optics/copper, stable supply, warranty/service economics and a defined system denominator | Open; no architecture currently has a public, matched cost-per-good-engine and service-cost bundle. |

This overlay is why the 2026 switch-CPO state remains **3** rather than **4**: the platform-level production signal is strong, but the public record does not yet reconcile a named customer CPO SKU, repeat units, final-engine yield and service economics. It also prevents a low-loss academic PIC result from being treated as a commercial adoption forecast.

## Annual state trajectory — not an adoption forecast

The entries below are *highest evidence-supported state*, not probabilities or system shares. A dash means the current source set supports no date.

| Architecture and domain | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Retimed / advanced pluggables, 102.4T Ethernet | 2 | — | — | — | — | — | — |
| LPO, 100G/lane Ethernet | 2–3 | — | — | — | — | — | — |
| LPO, 200G/lane Ethernet | 1–2 | — | — | — | — | — | — |
| LPO, 400G/lane Ethernet | 1 | — | — | — | — | — | — |
| Switch-side CPO, 200G/lane Ethernet | 3 | 3; Celestica ramp checkpoint planned, no numeric adoption | — | — | — | — | — |
| NPO/OBO, 224G-class | 0; sampling expected late 2026 | — | — | — | — | — | — |
| Accelerator optical I/O, scale-up | 1 | — | — | — | — | — | — |
| MOSAIC wide-and-slow optical | 1 | — | — | — | — | — | — |
| Switch-side CPO, 100G/lane Ethernet | 4; partner-reported volume-production baseline | — | — | — | — | — | — |
| Inter-rack scale-up CPO | 3; customer production-scale claim for Quantum-X Photonics plus primary roadmap/prototype; exact SKU and fleet size undisclosed | — | — | — | — | — | — |

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

Switch-side CPO has the strongest current commercial-maturity signal at 200G/lane, and NVIDIA's 2026 production announcement upgrades the timing evidence, but no public evidence set yet proves the commercial-proof threshold. Broadcom's primary Meta characterization materially improves the reliability evidence while leaving field, population and service-cost gates open. TSMC's COUPE milestones strengthen the process/stacking route behind a 200G CPO engine, but remain a manufacturing checkpoint rather than customer-confirmed switch adoption. NVIDIA's primary Vera Rubin/NVLink material upgrades inter-rack scale-up CPO from a secondary roadmap interpretation to a first-party roadmap with a functional NVL576 prototype; it still does not establish customer production for that specific architecture. SemiAnalysis adds an important economic distinction: scale-out CPO may face a TCO/serviceability and margin-stack hurdle, while inter-rack scale-up CPO has a stronger strategic rationale because it expands accelerator-domain size. 100G LPO has stronger system evidence than 200G or 400G LPO, while 200G/400G LPO remains bounded by incomplete/modeled electrical-link evidence. NPO and accelerator optical-I/O remain earlier public maturity states despite credible product announcements. This is a maturity and domain-value ranking, not a forecast of adoption or a company investment conclusion. [CLM-177; CLM-178; CLM-190; CLM-191; CLM-192; CLM-213–CLM-216; CLM-345–CLM-350]

## Evidence links

- [Critical-path milestone tracker](critical-path-milestone-tracker.md)
- [CPO customer-proof register](customer-proof-register.md)
- [Switch CPO platform dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [External optical-engine supplier dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md)
- [102.4T switch CPO versus advanced pluggables](../02-architecture/102.4t-cpo-vs-advanced-pluggables.md)
- [Linear-drive boundary benchmark](../02-architecture/linear-drive-boundary-benchmark.md)
- [OIF RTLR standards comparator](../01-sources/standards/STD-012-oif-eei-112g-rtlr-2025.pdf)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [MOSAIC microLED countercase](../02-architecture/mosaic-microled-countercase.md)
- [Source log](../01-sources/source-log.csv) and [claim ledger](../01-sources/claim-ledger.csv)

All source IDs and claim IDs are defined in the linked records. Company announcements establish what companies say; they do not, by themselves, prove adoption, field performance or sustainable economics.
