# Co-Packaged Optics Research Context

**Owner:** Nur Alpys  
**Project:** Co-Packaged Optics Research  
**Purpose:** Working context, research direction, project structure, and publication standard  
**Status:** In progress  
**Last updated:** 2026-08-06

---

## 1. Research objective

This project should not become only a general explanation of co-packaged optics. The objective is to build a falsifiable technology and investment view that connects:

\[
\text{Technical constraint}
\rightarrow
\text{Architecture choice}
\rightarrow
\text{Supplier content}
\rightarrow
\text{Revenue and margin}
\rightarrow
\text{Valuation}
\]

### Central research question

> Which CPO architecture, if any, will achieve commercially meaningful deployment first, in which application and year, and which company will capture the largest sustainable incremental profit pool when that happens?

### Final work should answer

1. Which architecture and deployment domain reach commercial proof first
2. The probability of commercial proof and meaningful adoption in each year from 2026 to 2032
3. Which technical, manufacturing, qualification, service, and economic gates determine timing
4. Which company is the technical, qualification, volume, platform, and profit-pool leader
5. Which public equity, if any, offers the strongest risk-adjusted opportunity relative to expectations
6. What the market appears to expect and where the research view differs
7. What evidence would prove the thesis wrong

### Canonical scope files

Use these files as the source of truth rather than duplicating working definitions:

- `00-scope/research-question.md`: decision objective, primary question, outputs, and boundaries
- `00-scope/terminology.md`: viability, adoption, commercial-stage, and leadership definitions
- `00-scope/hypothesis-register.md`: falsifiable hypotheses and revision history
- `00-scope/evidence-standard.md`: evidence hierarchy, claim labels, and forecast discipline
- `08-model/adoption-timeline.md`: annual timeline and probability model
- `07-companies/leader-scorecard.md`: operational leadership and investment-attractiveness scoring

---

## 2. Website and private research separation

The public website should contain cleaned, publishable work.

Private materials should remain outside the public website repository, including:

- Rough notes
- Source PDFs
- Interview notes
- Unpublished assumptions
- Working models
- Copyrighted documents
- Unverified claims
- Early drafts

### Suggested private folder structure

```text
cpo-research-private/
├── 00-scope/
│   ├── research-question.md
│   ├── hypothesis-register.md
│   ├── terminology.md
│   └── evidence-standard.md
├── 01-sources/
│   ├── source-log.csv
│   ├── claim-ledger.csv
│   ├── papers/
│   ├── standards/
│   ├── filings/
│   ├── product-materials/
│   ├── conference-presentations/
│   ├── videos/
│   └── newsletters/
├── 02-architecture/
├── 03-components/
├── 04-packaging/
├── 05-standards/
├── 06-industry-map/
├── 07-companies/
│   └── leader-scorecard.md
├── 08-model/
│   └── adoption-timeline.md
├── 09-primary-research/
├── 10-drafts/
└── 11-figures/
```

### Suggested public website structure

```text
projects/cpo-research/index.qmd
research/cpo/index.qmd
research/cpo/references.bib
research/cpo/figures/
```

Do not upload copyrighted PDFs to the public repository. Cite the original source instead.

---

## 3. Hypothesis discipline

The canonical hypotheses are maintained in `00-scope/hypothesis-register.md`. They cover adoption sequence, the binding constraints, coexistence with alternative architectures, standards, serviceability, economic value capture, leadership by layer, the lag between announcements and economics, and the difference between market leadership and equity returns.

Do not rewrite an original hypothesis after seeing new evidence. Append the evidence, revise confidence, and record when and why the view changed.

---

## 4. Evidence hierarchy

Rank sources approximately in this order:

1. Standards documents and regulatory filings
2. Peer-reviewed papers and conference proceedings
3. Official product specifications
4. Patents and technical presentations
5. Customer or supplier evidence
6. Management commentary
7. Trade publications
8. Consultant forecasts
9. Social media and anonymous commentary

A lower-ranked source may identify a useful question, but it should not independently support an important conclusion.

---

## 5. Source log

Use the following columns:

```text
source_id
title
author
organisation
publication_date
access_date
source_type
company
technology_area
priority
sequence
review_mode
review_status
main_claim
important_numbers
assumptions
limitations
relevance
confidence
citation
notes
```

---

## 6. Claim ledger

A source log records documents. A claim ledger records assertions.

Suggested columns:

```text
claim_id
claim
claim_type
source_id
exact_wording
comparison_baseline
independent_support
contradicting_evidence
confidence
status
notes
```

Suggested claim types:

- Fact
- Company claim
- Estimate
- Inference
- Opinion
- Unknown

Example:

| Claim | Source | Comparison baseline | Independent support | Confidence |
|---|---|---|---|---|
| CPO reduces optical power by X | Vendor presentation | Versus which architecture? | Not yet found | Low |
| Architecture is shipping | Company announcement | Samples or production units? | Customer evidence needed | Medium |
| Yield is commercially acceptable | No public source | Undefined | None | Very low |

---

## 7. Research sequence

Do not begin with company revenue modelling. First understand the physical system.

| Phase | Main task | Required output |
|---|---|---|
| 0 | Decision scope and definitions | Canonical question, definitions, hypotheses, and evidence standard |
| 1 | System architecture | Five architecture diagrams |
| 2 | Photonics fundamentals | Optical-engine component map |
| 3 | Packaging and reliability | Manufacturing flow and yield tree |
| 4 | Standards | Standards and interface matrix |
| 5 | Industry structure | Supplier and value-chain map |
| 6 | Company research | Standardised dossiers and evidence-adjusted leader scorecards |
| 7 | Adoption model | Annual 2026-2032 probability timeline and financial model |
| 8 | Primary research | Interview evidence and contradiction log |
| 9 | Investment synthesis | Thesis, consensus, variant view, catalysts, risks, and valuation implications |

Each phase should produce a visible deliverable.

---

# Phase 1: System architecture

## 8. Architectures to map

Draw these architectures yourself:

1. Retimed pluggable optics
2. Linear pluggable optics
3. Near-packaged optics
4. Switch-side CPO
5. Accelerator-side optical I/O

### Generic signal path

```text
ASIC SerDes
→ package
→ PCB or substrate channel
→ connector
→ DSP or linear electronics
→ driver
→ modulator
→ optical fibre
→ photodetector
→ TIA
→ receiving SerDes
```

### Questions to answer for every architecture

- How far does the high-speed electrical signal travel?
- Where is clock recovery performed?
- Is there a module DSP?
- Where is forward error correction implemented?
- What can be replaced in the field?
- What happens when one optical lane fails?
- Where is the laser located?
- How is heat removed?
- How many optical engines surround the host ASIC?
- Who tests the complete assembly?
- Who carries warranty liability?
- What system constraint is the architecture solving?

### Required comparison table

| Architecture | Electrical path | Module DSP | Replaceability | Main advantage | Main weakness |
|---|---:|---:|---:|---|---|
| Retimed pluggable | Longest | Yes | High | Mature and serviceable | Power and faceplate density |
| Linear pluggable | Long | No or reduced | High | Lower power and cost | Tighter host-channel requirements |
| Near-packaged optics | Short | Architecture-dependent | Moderate | Less electrical loss | Packaging and board complexity |
| Switch CPO | Very short | Usually reduced or relocated | Low | Density and power potential | Yield and serviceability |
| XPU optical I/O | Die or package scale | Architecture-dependent | Very low | Scale-up reach and density | Deep package integration |

Do not copy a vendor diagram. Redraw it and cite the underlying sources.

---

# Phase 2: Photonics fundamentals

## 9. Topics to understand

Learn enough to evaluate commercial implications, not to reproduce a full photonics degree.

- Silicon photonic integrated circuits
- Mach-Zehnder modulators
- Microring modulators
- Electro-absorption modulators
- Germanium photodetectors
- Drivers
- Transimpedance amplifiers
- Wavelength-division multiplexing
- Continuous-wave lasers
- External laser sources
- Fibre coupling
- Thermal tuning
- Optical power budgets
- Link budgets
- Bit-error rates
- Forward error correction

### Four questions for every component

1. What does it do?
2. What determines its performance?
3. What makes it expensive or difficult to manufacture?
4. Which public or private companies may supply it?

Focus technical study on properties that affect:

- Power
- Yield
- Area
- Temperature sensitivity
- Reliability
- Cost
- Supplier differentiation

---

# Phase 3: Packaging, yield, and serviceability

## 10. Manufacturing process

Map the process:

```text
ASIC fabrication
→ PIC fabrication
→ EIC fabrication
→ wafer testing
→ known-good-die selection
→ die attach
→ electrical interconnect
→ fibre attach
→ laser integration
→ thermal solution
→ package test
→ burn-in
→ system qualification
```

### Simplified yield framework

\[
Y_{\text{system}}
=
Y_{\text{ASIC}}
\times
Y_{\text{assembly}}
\times
Y_{\text{test}}
\times
\prod_{i=1}^{n}
\left(
Y_{\text{PIC},i}
\times
Y_{\text{EIC},i}
\right)
\]

This is simplified. Real economics may also depend on:

- Correlated failures
- Rework
- Redundancy
- Binning
- Partial-good configurations
- Test coverage
- Package salvage
- Warranty returns

### Questions to investigate

- Can the PIC and EIC be fully tested before assembly?
- Can a defective optical engine be replaced?
- Is fibre attach passive or actively aligned?
- How many assembly steps are automated?
- Does the package require optical access during testing?
- Can bad lanes be disabled without scrapping the package?
- Is redundancy included?
- What happens if a laser fails?
- Does a failure require replacing a module, board, switch, or expensive host package?
- Who bears warranty and field-service costs?

### Required outputs

1. Manufacturing-flow diagram
2. Yield sensitivity model
3. Failure-mode table
4. Field-service comparison
5. List of commercially important undisclosed variables

---

# Phase 4: Standards and interoperability

## 11. Standards to track

- OIF Co-Packaging Framework
- OIF 3.2T Co-Packaged Module implementation agreement
- OIF external-laser management documents
- OIF ELSFP implementation agreement
- CEI-224G materials
- CEI-448G framework and project work
- IEEE P802.3dj public materials

### Standards matrix

| Interface | Standards body | Status | Reach | Lane rate | Relevant architecture | Investment significance |
|---|---|---|---:|---:|---|---|
| CPO module | OIF | Verify | Package level | Verify | Switch CPO | Interoperability framework |
| CEI-224G VSR | OIF | Verify | Chip to module | 224G | Pluggable, NPO, CPO | Electrical-reach economics |
| CEI-448G VSR | OIF | Verify | Chip to module | 448G | Future architectures | Future electrical scaling |
| P802.3dj | IEEE | Verify | Multiple media | 200G or greater | Ethernet | Future Ethernet physical layers |

Do not treat a standard as a binary variable. Record what it covers:

- Electrical signalling
- Optical wavelength
- Mechanical footprint
- Fibre connector
- Laser management
- Thermal boundary
- Management interface
- Test methodology
- Replaceability
- Interoperability

---

# Phase 5: Industry value chain

## 12. Value-chain framework

| Layer | Product | Existing value pool | Potential CPO effect |
|---|---|---|---|
| Switch silicon | Ethernet or InfiniBand ASIC | Switch-chip revenue | Greater system integration |
| SerDes | Electrical I/O | ASIC content | Higher importance at package boundary |
| Optical DSP | Retiming and equalisation | Pluggable-module content | Potential displacement in some links |
| PIC | Modulation and detection | Optical-engine content | Potential growth |
| EIC | Drivers and TIAs | Optical-engine content | Potential growth |
| Laser | Optical source | Module or external-laser content | Architecture-dependent growth |
| Pluggable module | Complete transceiver | Large existing pool | Potential cannibalisation |
| Packaging | Substrate, assembly, fibre attach | Smaller existing pool | Greater complexity and value |
| Fibre and connectors | Optical connectivity | Network content | Higher-density opportunity |
| Test | Optical and electrical test | Manufacturing equipment | Greater test complexity |

### Initial company set

Start with:

- Broadcom
- NVIDIA
- Marvell
- Coherent
- Lumentum

Then expand selectively to:

- Arista Networks
- Credo
- Astera Labs
- TSMC
- Fabrinet
- Corning
- Relevant Asian optical-module suppliers
- Relevant private optical-I/O companies

Do not build complete financial models for every company immediately.

---

# Phase 6: Company dossiers

## 13. Standard company template

Use the same structure for every company:

```text
1. Business overview
2. Current optical and networking exposure
3. Product architecture
4. Position in the value chain
5. Customers and routes to market
6. Potential CPO opportunity
7. Potential cannibalisation
8. Manufacturing dependencies
9. Competitive advantages
10. Risks
11. Evidence required
12. Financial variables
13. Valuation sensitivity
14. Claims requiring verification
15. Upcoming milestones
16. Commercial stage and proof of volume
17. Independent customer evidence
18. Operational leadership score and evidence multiplier
19. Investment-attractiveness score
20. Consensus expectation and variant view
```

### Filing review sequence

For each public company, review:

1. Latest annual report or 10-K
2. Latest quarterly filing or 10-Q
3. Last eight earnings releases
4. Investor-day presentations
5. Product announcements
6. Relevant acquisition documents
7. Risk factors
8. Capital-expenditure disclosures
9. Inventory disclosures
10. Customer-concentration disclosures

### Search terms

```text
optical
photonics
laser
transceiver
DSP
data centre
AI
networking
packaging
yield
qualification
customer concentration
inventory
warranty
capacity
capital expenditure
```

### Commercial-stage terminology

Track wording carefully:

```text
demonstrating
sampling
qualifying
shipping
production
volume production
material revenue
```

These terms are not interchangeable.

---

# Phase 7: Adoption and financial modelling

## 14. Physical model first

Build one annual path from 2026 to 2032 for each architecture, deployment domain, system type, customer type, and geography. Model commercial proof separately from meaningful adoption, and express uncertain timing as a probability distribution rather than a single date.

### System demand

\[
\text{CPO systems}
=
\text{Relevant systems shipped}
\times
\text{CPO adoption rate}
\]

### Optical-engine demand

\[
\text{Optical engines}
=
\text{CPO systems}
\times
\text{Optical engines per system}
\]

### Supplier revenue

\[
\text{Revenue}
=
\text{Optical engines}
\times
\text{Supplier share}
\times
\text{ASP}
\]

### Cannibalisation

\[
\text{Net revenue effect}
=
\text{New CPO revenue}
-
\text{Lost pluggable revenue}
-
\text{Lost DSP revenue}
\]

### Gross profit

\[
\text{Gross profit}
=
\text{Revenue}
\times
\text{Gross margin}
-
\text{Yield loss}
-
\text{Warranty cost}
\]

Keep switch-side CPO and accelerator-side optical I/O separate.

### Inputs to model explicitly

- Switch generation
- Aggregate switch bandwidth
- Port rate
- Number of ports
- Lane rate
- Optical engines per switch
- Wavelengths per engine
- CPO attach rate
- Average selling price
- Laser content
- Fibre and connector content
- Packaging content
- Final-package yield
- Supplier share
- Qualification timing
- Pluggable cannibalisation
- Gross margin
- Warranty expense
- Critical-path milestones
- Commercial maturity stage
- Technical and commercial gate status
- Scenario probability
- Evidence quality
- Consensus expectations
- Valuation and earnings sensitivity

### Input format

For uncertain inputs, use:

```text
Low
Base
High
Source
Reasoning
Sensitivity
```

Avoid unsupported point estimates.

---

## 15. Scenario definitions

### Bear case

- Electrical solutions improve faster than expected
- Linear pluggables, retimers, active electrical cables, and NPO remain sufficient
- CPO qualification is slow
- Packaging yields remain difficult
- Customers resist reduced serviceability
- CPO remains limited to selected proprietary systems

### Base case

- CPO becomes meaningful in the highest-bandwidth switches
- Pluggables remain important elsewhere
- External lasers and removable fibre connections improve serviceability
- Switch-side CPO develops before widespread accelerator optical I/O
- Adoption remains concentrated among leading systems vendors

### Bull case

- Optical I/O becomes necessary inside scale-up systems
- CPO expands from switches into XPU and memory packages
- Manufacturing yield improves sufficiently for high-volume production
- Large optical scale-up domains become commercially attractive
- Optical content per accelerator system rises materially

For each scenario, specify:

- Technical trigger
- Probability
- Commercial-proof year
- Meaningful-adoption year
- Unit volume
- Supplier content
- Technical, qualification, volume, platform, and profit-pool leaders
- Consensus expectation and variant view
- Revenue consequence
- Margin consequence
- Valuation consequence
- Evidence that would invalidate it

---

# Phase 8: Primary research

## 16. Potential interview targets

- Network architects
- Switch engineers
- Signal-integrity engineers
- Silicon-photonics engineers
- Packaging engineers
- Optical-module suppliers
- Laser suppliers
- OSAT and contract-manufacturing personnel
- Fibre and connector suppliers
- Test-equipment specialists
- Former product managers
- Datacentre operators

Do not solicit confidential information or material non-public information.

### High-value diligence questions

1. What is the all-in power per delivered terabit, including lasers and cooling?
2. What electrical-channel problem forces the move to CPO?
3. At what lane rate does the current pluggable architecture become unattractive?
4. What is the largest source of final-package yield loss?
5. Can optical engines be tested before attachment to the host ASIC?
6. What proportion of fibre attachment is automated?
7. Which optical failures can be repaired?
8. What component determines lifetime reliability?
9. How is laser redundancy implemented?
10. How long does customer qualification take?
11. What would cause a customer to choose NPO or LPO instead?
12. Who carries warranty liability for an integrated package?
13. Is the product shipping in volume or only to qualification customers?
14. What limits second sourcing?
15. Which component captures more dollar content under CPO?
16. Which existing component loses content?
17. What is the cost per delivered bit compared with a pluggable system?
18. Is the purchasing decision based on cost, power, density, reliability, or necessity?
19. What has to improve before accelerator-side optical I/O scales?
20. Which vendor claim is most commonly misunderstood by investors?

### Interview-note template

```text
Role
Date
Topic
Main observations
Claims supported
Claims contradicted
Confidence
Possible bias
Follow-up questions
Publishable or not publishable
```

---

# Phase 9: Writing and publication

## 17. Three-layer report structure

### Layer 1: Two-minute view

At the top of the report:

- Research question
- Preliminary conclusion
- Variant perception
- Three key pieces of evidence
- Main catalyst
- Main risk
- What would prove the view wrong

### Layer 2: Investment analysis

- Architecture
- Adoption
- Industry structure
- Company exposure
- Financial implications
- Valuation
- Catalysts
- Risks

### Layer 3: Technical appendix

- Signal paths
- Optical-engine components
- Packaging
- Standards
- Yield model
- Source tables
- Assumption details

---

## 18. Labelling evidence and judgement

Use clear labels in notes and drafts:

### FACT

Directly supported by a cited source.

### COMPANY CLAIM

Stated by a company but not independently verified.

### ESTIMATE

Calculated from disclosed data and explicit assumptions.

### INFERENCE

A conclusion drawn from several facts.

### OPINION

Personal judgement.

### UNKNOWN

Important information not publicly available.

---

## 19. Publication standard

Do not publish the full report until it includes:

- A clear central question
- A complete architecture comparison
- A value-chain map
- At least five company dossiers
- A three-scenario adoption model
- An annual 2026-2032 milestone and probability timeline
- Explicit technical, manufacturing, qualification, service, supply-chain, and economic viability gates
- Explicit cannibalisation analysis
- Separate operational-leadership and investment-attractiveness scorecards
- An evidenced consensus and variant-perception section
- A source log
- A claim ledger
- A list of unresolved questions
- Falsification conditions
- Proper disclosures

The first published version does not need to include a stock recommendation.

A rigorous industry framework with transparent uncertainty is stronger than an unsupported buy or sell conclusion.

---

## 20. Eight-week workflow

| Week | Focus | Deliverable |
|---|---|---|
| 1 | Scope, definitions, and architectures | Decision framework and five architecture diagrams |
| 2 | Photonics and link fundamentals | Component map and glossary |
| 3 | Packaging, reliability, yield, and service | Manufacturing and critical-path memo |
| 4 | Standards, interfaces, and viability gates | Standards matrix and gate assessment |
| 5 | Value chain and companies | Industry map, five dossiers, and initial leader scores |
| 6 | Adoption and financial modelling | 2026-2032 probability timeline and three scenarios |
| 7 | Primary research, consensus, and contradiction testing | Interview log, consensus map, and revised hypotheses |
| 8 | Investment synthesis and publication | First complete report and variant view |

Write a two-page memo at the end of every week.

---

## 21. Immediate next actions

1. Populate an architecture-by-deployment-domain decision matrix.
2. Create and begin populating `01-sources/claim-ledger.csv`.
3. Verify the current OIF and IEEE documents relevant to co-packaging and high-speed interfaces.
4. Map every viability gate and identify the present critical path for each architecture.
5. Build the 2026-2032 milestone tracker and assign initial evidence-based probabilities.
6. Select at least five company dossiers across different value-chain layers.
7. Collect independent customer, qualification, manufacturing, and volume evidence.
8. Establish an evidenced consensus baseline before writing a variant view.
9. Write a two-page decision memo titled:

```text
What problem is co-packaged optics actually solving?
```

End that memo with:

```text
What I believe
What I know
What I do not know
What evidence I need next
What would change my view
```

---

## 22. Context for future AI or Codex sessions

When using this file as context, the assistant should:

- Treat the project as ongoing research, not a completed thesis
- Use the canonical scope, definitions, hypotheses, evidence standard, timeline, and scorecard files
- Avoid inventing technical facts, market shares, shipment status, or forecasts
- Separate facts, company claims, estimates, inferences, opinions, and unknowns
- Prefer primary sources
- Keep switch-side CPO separate from accelerator-side optical I/O
- Compare CPO against retimed pluggables, linear pluggables, NPO, retimers, and AECs
- Analyse both opportunity and cannibalisation
- Distinguish technical, qualification, volume, platform, and profit-pool leadership
- Never convert an announcement, demonstration, sample, or qualification into evidence of volume production
- Express 2026-2032 timing as dated probabilities tied to observable milestones
- Compare investment attractiveness with an evidenced consensus baseline
- State what evidence would disprove each conclusion
- Use British English
- Avoid em dash characters
- Preserve the broader personal portfolio structure of the website
- Treat co-packaged optics as one project within that portfolio
