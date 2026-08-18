# Public-data boundary register

**As of:** 2026-08-10  
**Purpose:** Separate genuinely unavailable commercial inputs from research tasks that can still be solved with public evidence.

The absence of a public number is recorded as an evidence boundary. It is not converted into a fabricated point estimate.

| Field | Current public evidence | Boundary | Evidence that would change the status | Current anchors |
|---|---|---|---|---|
| Customer CPO SKU and accepted units | Vendor production claims, named ecosystem partners and customer-scale statements exist, but no reconciled CPO SKU/unit numerator | Generally not publicly disclosed at product level | Customer filing, named deployment record, repeat shipment record or permitted primary interview | `CLM-077`, `CLM-220`–`CLM-223`, `CLM-345`–`CLM-350`, `CLM-411`–`CLM-420` |
| Final-engine yield | Academic/test-vehicle papers report interface, module or illustrative connection yields; no supplier lot waterfall | Generally private manufacturing data | Lot-level good-die → attach → package → test → accepted-engine yield with denominator | `CLM-312`–`CLM-314`, `CLM-397`–`CLM-400`, `CLM-479`–`CLM-482`, `CLM-509`–`CLM-513` |
| Fibre-attach cycle time and rework | Papers report losses, alignment mechanisms and serviceability concepts; automated factory timing is absent | Generally private process data | OSAT/fibre-attach process record, Cpk/cycle-time range or anonymised supplier interview | `CLM-239`–`CLM-240`, `CLM-315`, `CLM-495`–`CLM-499` |
| Qualification and field reliability | JEDEC/test-vehicle stress and standards provide requirements; field-return distributions are absent | Customer/supplier-confidential | Qualification summary, MTBF/FIT range, field-return data or warranty reserve | `CLM-287`–`CLM-290`, `CLM-357`–`CLM-359`, `CLM-479`–`CLM-482`, `CLM-506`, `CLM-511`–`CLM-513` |
| Replacement economics | Detachable connectors and localized laser soldering demonstrate mechanisms; MTTR, spares and downtime cost are absent | Generally private service data | Service procedure, replacement-cycle distribution, spare policy and warranty allocation | `CLM-426`, `CLM-498`–`CLM-499`, `CLM-504`–`CLM-508` |
| Optical-engine ASP and supplier share | Company revenue and strategic agreements establish broad denominators; product allocation and transfer prices are absent | Contract-confidential | Product-level filing, contract disclosure, supplier interview or reconciled teardown | `CLM-068`–`CLM-073`, `CLM-197`–`CLM-198`, `CLM-250`–`CLM-251` |
| CPO gross margin and price-down | Consolidated company margins are public but not CPO-specific | Not separately disclosed | Product-line margin, realised ASP, price-down schedule and attributable cost stack | `CLM-070`, `CLM-073`, `CLM-083`, `CLM-335`–`CLM-340` |
| Incremental CPO capex and utilization | Fab/line announcements and broad capex are public; CPO-attributable qualified capacity is not | Partly public, product allocation private | Line allocation, qualified monthly good-engine output, utilization and depreciation burden | `CLM-069`, `CLM-073`, `CLM-196`–`CLM-198` |
| Matched CPO/LPO/NPO TCO | Power models and component demonstrations exist; matched system ASP/service/yield denominator is absent | Requires cross-company and customer data | Same host ASIC, lane rate, reach, FEC, temperature, service and cost comparison | `CLM-057`–`CLM-067`, `CLM-177`–`CLM-178`, `CLM-471`–`CLM-486` |
| Adoption denominator | Architecture definitions and commercial-proof priors exist; system/port/rack denominator is not reconciled | Not publicly standardized | Operator fleet inventory, shipment denominator or market dataset with architecture classification | `CLM-074`, `CLM-077`, `CLM-082`, `CLM-084`, `CLM-411`–`CLM-420` |

## Working rule

Continue advancing what public evidence can answer—architecture boundaries, measured PIC/engine performance, standards, process mechanisms, supplier capacity and falsification conditions. Mark the fields above as **not publicly disclosed** until stronger evidence arrives. Do not let a vendor roadmap, abstract, aggregate company margin or illustrative yield sensitivity silently clear a commercial gate.

## Linked controls

- [Decision-output completion audit](decision-output-completion-audit.md)
- [Evidence-gate register](evidence-gate-register.md)
- [Customer-scale repeatability gate](customer-scale-repeatability-gate.md)
- [Primary-research question bank](../09-primary-research/interview-question-bank.md)
