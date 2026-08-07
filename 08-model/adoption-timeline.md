# CPO Adoption Timeline Model

**Model horizon:** 2026 to 2032
**Status:** Evidence-calibrated milestone model; annual adoption probabilities are not yet numerically eligible
**Last updated:** 2026-08-07

## Decision discipline

The final question is not whether an architecture has a product announcement. It is which architecture first reaches commercial proof and then meaningful adoption in a defined deployment domain. Those are different observations and must use different denominators.

This model keeps five architecture/domain combinations separate:

1. Retimed and advanced pluggables — Ethernet scale-out.
2. LPO — Ethernet scale-out, separated by 100G, 200G and 400G per lane.
3. Switch-side CPO — highly optically attached Ethernet scale-out.
4. NPO/OBO — switch or XPU-adjacent scale-out/scale-up where a near-package electrical path is sufficient.
5. Accelerator optical I/O — scale-up chiplet/inter-XPU fabric.

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
| Switch-side CPO, 200G/lane Ethernet scale-out | Broadcom documents TH6-Davisson’s 102.4T/16-engine configuration; NVIDIA claims 200G-SerDes CPO switches are in production. [CLM-076; CLM-077; CLM-079] | 3 to 4 — sampling / vendor-asserted limited production | A credible integrated CPO product path exists and vendors claim commercial progress. | Customer-confirmed CPO units, repeat production, field reliability, economics or meaningful system adoption. |
| NPO/OBO, 224G-class scale-up and scale-out | Lightmatter announced a 6.4-Tb/s-per-direction NPO/OBO engine and expected late-2026 sampling. [CLM-086] | 0 — announced roadmap | A dated NPO/OBO product milestone exists. | Observed samples, qualification, production or customer deployment. |
| Accelerator optical I/O, scale-up | Ayar Labs claims an 8-Tb/s UCIe optical-I/O chiplet with a 16-wavelength source. [CLM-085] | 1 — component/product announcement | A credible public technical candidate exists. | Customer-qualified production, system volume, yield or installed base. |

The maturity state is deliberately conservative. A company’s use of “production” is recorded as a company claim unless customer-side evidence identifies the configuration, deployment and repeat volume.[CLM-077][CLM-079][CLM-081]

## Evidence-calibrated critical path

| Architecture | Next observable milestone | Earliest source-supported timing | Gate affected | What would upgrade the state |
|---|---|---|---|---|
| 100G LPO | Named customer/system plus repeat production and field data | Not stated in reviewed source set | Commercial; reliability | Customer confirmation, units/ports, repair/failure evidence. |
| 200G LPO | Measured multi-vendor end-to-end system at disclosed loss, return loss, FEC, reach and temperature | No source-supported date | Technical; product | Full system data, qualification and deployment record. |
| 400G LPO | Measured 212.5-GBd end-to-end link and production-compatible package | No source-supported date | Technical; manufacturing | A completed link, rather than the present model, then qualification evidence. [CLM-065; CLM-066] |
| Switch CPO | Customer-side confirmation of a named TH6-Davisson or Spectrum-X Photonics deployment | No source-supported date | Commercial; reliability | Units/ports, customer, service history and repeat order/operating evidence. |
| NPO/OBO | Lightmatter Passage L20 sample availability | Late 2026 is the company’s expected date, not observed delivery. [CLM-086] | Product | Observed sample, named qualification and measured system evidence. |
| Accelerator optical I/O | Named production XPU/rack deployment using an optical chiplet | No source-supported date | Product; manufacturing; commercial | Customer, topology, qualified yield, repeat volume and field use. [CLM-085] |

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

Switch-side CPO has the strongest current commercial-maturity signal at 200G/lane, but no public evidence set yet proves the commercial-proof threshold. 100G LPO has stronger system evidence than 200G or 400G LPO, while 200G/400G LPO remains bounded by incomplete/modeled electrical-link evidence. NPO and accelerator optical-I/O remain earlier public maturity states despite credible product announcements. This is a maturity ranking, not a forecast of adoption or a company investment conclusion.

## Evidence links

- [Switch CPO platform dossier](../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [External optical-engine supplier dossier](../07-companies/coherent-lumentum-external-optical-engine-dossier.md)
- [102.4T switch CPO versus advanced pluggables](../02-architecture/102.4t-cpo-vs-advanced-pluggables.md)
- [Linear-drive boundary benchmark](../02-architecture/linear-drive-boundary-benchmark.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Source log](../01-sources/source-log.csv) and [claim ledger](../01-sources/claim-ledger.csv)

All source IDs and claim IDs are defined in the linked records. Company announcements establish what companies say; they do not, by themselves, prove adoption, field performance or sustainable economics.
