# Commercial-proof probability priors

**Horizon:** 2026–2032  
**Status:** Explicit analyst priors for the commercial-proof event; not adoption-share or revenue forecasts  
**As of:** 2026-08-10

## Event definition

The event is **commercial proof by year-end**: repeat paid production from two independent customers, or sustained/repeated production by one major customer, for the precisely defined architecture and deployment domain. A company saying “production,” a demonstration, an early-access sample or a partner quotation is not enough by itself.

The probabilities below are bounded priors used to organize diligence. They are not observed frequencies and must be revised when a customer-side SKU, accepted-unit count, repeat shipment record or contrary evidence appears.

## Priors

Ranges are cumulative probability that the commercial-proof event has occurred by the end of the stated year.

| Architecture / domain | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | Evidence basis and principal uncertainty |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Retimed / advanced pluggables, Ethernet scale-out | 55–75% | 70–85% | 80–90% | 85–95% | 90–97% | 92–98% | 93–99% | Standards-defined RTLR boundary and live 102.4T demonstrations; customer repeat volume, matched power and field data remain open (`CLM-001`–`CLM-004`, `CLM-297`–`CLM-300`). |
| LPO, 100G/lane Ethernet scale-out | 35–55% | 50–70% | 65–80% | 75–88% | 82–92% | 85–95% | 88–97% | Measured 51.2T system evidence, but independent customer production and service history are not cleared (`CLM-056`, `CLM-064`). |
| LPO, 200G/lane Ethernet scale-out | 15–30% | 30–50% | 50–70% | 65–82% | 75–90% | 82–93% | 86–96% | Reviewed record is mainly modeled/component evidence; complete qualified 200G system and customer numerator are missing (`CLM-057`, `CLM-059`, `CLM-063`, `CLM-067`). |
| LPO, 400G/lane Ethernet scale-out | 5–15% | 10–25% | 25–45% | 45–65% | 60–80% | 72–88% | 80–93% | 212.5-GBd behavior remains modeled or component-level; the new full PAP-053/PAP-054 papers strengthen the advanced-pluggable countercase but do not establish a completed 400G/lane LPO system or commercial proof (`CLM-065`–`CLM-067`, `CLM-471`–`CLM-475`, `CLM-483`–`CLM-486`). |
| Switch-side CPO, 100G/lane Ethernet | 90–98% | 93–99% | 95–99% | 96–99% | 97–99% | 98–99% | 98–99% | Broadcom's partner-reported TH5-Bailly volume-production baseline; audited units and repeat economics remain open (`CLM-199`, `CLM-200`). |
| Switch-side CPO, 200G/lane Ethernet | 45–65% | 65–82% | 78–91% | 86–95% | 90–97% | 93–98% | 95–99% | NVIDIA reports full production and names a supply chain and first adopters; Broadcom has a defined 200G product and Celestica a planned 2027 program. No customer-accepted SKU, unit count, final-engine yield or repeat shipment is public (`CLM-345`–`CLM-350`, `CLM-435`–`CLM-437`). |
| NPO / OBO, 224G-class | 5–15% | 15–30% | 30–50% | 50–70% | 65–82% | 75–90% | 82–94% | Dated sampling roadmap and short electrical-boundary proposals, but no observed sample, qualification or customer production (`CLM-086`, `CLM-091`). |
| Accelerator optical I/O, scale-up chiplets | 15–30% | 25–45% | 40–60% | 55–75% | 68–85% | 78–91% | 85–95% | Ayar, Intel, Lightmatter and Marvell/Celestial routes have credible prototypes or roadmaps; product-specific customer production and yield remain unresolved (`CLM-085`, `CLM-094`, `CLM-095`, `CLM-304`). |
| Inter-rack scale-up CPO | 55–75% | 68–85% | 80–92% | 88–96% | 92–98% | 95–99% | 96–99% | Lambda reports a production-scale Quantum-X Photonics GB300 cluster, while exact SKU, switch count and repeat deployment remain undisclosed (`CLM-224`, `CLM-225`). |

## Calibration rules

1. **Do not multiply these probabilities by market size.** They describe only the binary commercial-proof event.
2. **Raise a range only when the evidence crosses a gate.** Customer SKU and accepted units should move a route more than a vendor roadmap; repeat shipments and field/service data should move it more than a single shipment.
3. **Apply a downward revision when architecture boundaries are corrected.** The SN6600-LD correction is an example: a confirmed pluggable deployment cannot be used as CPO proof.
4. **Keep technical and economic events separate.** A production-qualified engine can still lose on matched TCO, serviceability or supplier margin.
5. **Do not convert the ranges into earnings.** The profit-pool model additionally needs systems, engines/system, attributable content, qualified share, realised margin, cannibalisation, warranty/service cost, R&D and capex.

## Adoption-share gate

Annual adoption shares remain **not eligible for numeric population** until each architecture/domain has:

- a defined addressable-system denominator;
- an exact customer-side product/SKU boundary;
- accepted units, ports or systems for the numerator;
- repeat shipment or expansion evidence; and
- a matched TCO/service comparison against the relevant alternative.

Until those fields are present, use the cumulative commercial-proof ranges above and the state trajectory in [CPO Adoption Timeline](adoption-timeline.md), not a fabricated percentage of market adoption.
