# CPO Research Question and Decision Scope

**Owner:** Nur Alpys
**Status:** Provisional conclusion issued; evidence gates remain open
**Scope horizon:** 2026 to 2032
**Last updated:** 2026-08-12

## Decision objective

This research is intended to produce a falsifiable view on three connected decisions:

1. Whether a specific co-packaged-optics architecture becomes technically and commercially viable
2. When it reaches commercially meaningful adoption in a defined deployment domain
3. Which company captures the largest sustainable incremental profit pool, and whether that outcome is mispriced

The project is not complete when it can explain CPO. It is complete when it can make a dated, probability-weighted judgement and show the evidence that would change that judgement.

## Primary research question

> Which CPO architecture, if any, will achieve commercially meaningful deployment first, in which application and year, and which company will capture the largest sustainable incremental profit pool when that happens?

## Current focused workstream

The active workstream narrows the broader question to scale-out optical engines and PIC design:

> Which company can manufacture the lowest-total-cost, qualification-ready 200G/lane and later 400G/lane scale-out optical engine, and how much sustainable gross profit can it retain after customers, switch-platform owners and manufacturing partners take their shares?

The current provisional view, economic logic, required evidence and falsification conditions are documented in [Scale-Out Optical Engine and PIC Profit-Pool Thesis](scale-out-optical-engine-profit-pool-thesis.md). The synthesized conclusion is in [CPO research conclusion — 2026-08-10](final-conclusion-2026-08-10.md).

## Three linked questions

### 1. Viability and timing

For each architecture and deployment domain:

- What technical constraint creates the need to move optics closer to compute or switch silicon?
- At what bandwidth, lane rate, electrical reach, topology, and system scale does that constraint become binding?
- Can the architecture meet all-in power, bandwidth density, link margin, thermal, reliability, yield, and service requirements?
- Does it beat the best available alternative on total cost per delivered bit?
- Which qualification, manufacturing, standards, and customer milestones form the critical path?
- What is the probability of commercial proof and meaningful adoption in each year from 2026 through 2032?

### 2. Company leadership and economic capture

- Which company leads technically within each architecture and value-chain layer?
- Which company has the strongest evidence of customer qualification and production volume?
- Who controls the architecture, customer relationship, manufacturing process, and scarce components?
- Which company captures the most incremental revenue and gross profit after cannibalisation, yield loss, warranty cost, research spending, and capital expenditure?
- Does the technical leader differ from the volume leader, profit-pool leader, or best public-equity opportunity?

### 3. Variant perception and investability

- What adoption timing and market structure does consensus appear to expect?
- Which technical, manufacturing, or commercial assumption may be misunderstood?
- Which observable milestone could change estimates before consensus reacts?
- How much probability-weighted revenue, gross profit, earnings, and valuation sensitivity follows from each scenario?
- What downside remains if CPO adoption is late, narrow, uneconomic, or captured by a different supplier?

## Architecture scope

Analyse these architectures separately:

1. Conventional retimed pluggable optics
2. Linear pluggable optics
3. Near-packaged optics
4. Switch-side CPO
5. Accelerator-side optical I/O
6. Active electrical cables, retimers, and improved copper where they are credible alternatives

Do not use CPO as a single category when technical interfaces, failure domains, customer motivations, or supplier economics differ.

## Deployment-domain scope

The timing model must specify the network position:

- Front-end scale-out switching
- Back-end scale-out switching
- Accelerator scale-up fabrics
- Rack-to-rack and multi-rack links
- Memory or disaggregated-compute links where relevant
- Other domains only when evidence supports inclusion

An architecture can be viable in one domain and unattractive in another.

## Required decision outputs

1. Architecture trigger matrix
2. Technical and commercial viability-gate assessment
3. Annual 2026 to 2032 probability-weighted adoption timeline
4. Critical-path milestone tracker
5. Manufacturing, yield, reliability, and serviceability model
6. Total-cost-per-delivered-bit comparison
7. Value-chain profit-pool map
8. Company operational-leadership scorecard by architecture and layer
9. Company investment-attractiveness scorecard
10. Revenue, gross-profit, earnings, and valuation bridge
11. Consensus and variant-perception tracker
12. Falsification dashboard and thesis-change log

The manufacturing output is now split into a [cost-per-qualified-good-engine gate](../08-model/manufacturing-cost-per-good-engine-gate.md) and a [fibre-count/yield sensitivity](../08-model/fibre-count-yield-sensitivity.md). This prevents an isolated PIC, laser or coupling result from being mistaken for a complete production-engine economics result.

The forecast layer now separates bounded [commercial-proof probability priors](../08-model/commercial-proof-probability-priors.md) from adoption-share estimates. Adoption shares remain gated until customer/system denominators, accepted units, repeat shipments and matched TCO/service evidence are available.

The active commercial/economic boundary is controlled through the [NVIDIA and Broadcom commercial-proof dossiers](../07-companies/commercial-proof-dossiers/README.md), the [six-company content-attribution register](../07-companies/six-company-content-attribution-register.md), and the [common architecture system-boundary scorecard](../02-architecture/system-boundary-comparison-scorecard.md). These documents exist to prevent platform, partnership or component evidence from being converted into supplier revenue without a matched SKU, content and economics record.

## Final answer format

The eventual conclusion must state:

```text
Architecture:
Deployment domain:
Commercial-proof year and probability:
Meaningful-adoption year and probability:
Critical-path milestones:
Technical leader:
Volume leader:
Profit-pool leader:
Best public-equity opportunity, if any:
Evidence quality:
Main disconfirming evidence:
Next thesis-changing catalyst:
```

Do not force a company winner when evidence is insufficient. `No decision`, `no durable leader`, and `not yet investable` are valid conclusions.

## Completion audit

The current requirement-by-requirement evidence status and research sequence are maintained in the [CPO Decision-Output Completion Audit](decision-output-completion-audit.md) and the [Final CPO Decision-Readiness Matrix](final-decision-readiness-matrix.md). These controls prevent the study from being treated as complete merely because its framework or source library is extensive.

## Scope controls

- Use public and compliant primary research only.
- Do not solicit material non-public or confidential information.
- Separate facts, company claims, estimates, inferences, opinions, and unknowns.
- Record assumptions before viewing outcomes where practical.
- Preserve the original wording of hypotheses and log later revisions separately.
- Treat every adoption date as a probability distribution, not a certain point estimate.
- Compare against the best improving alternative, not a static version of pluggable optics or copper.
- Never infer leadership from announcements alone.
