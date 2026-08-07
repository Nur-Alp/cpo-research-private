# CPO Hypothesis Register

**Status:** Initial hypotheses, not conclusions
**Last updated:** 2026-08-07

## Update rules

- Do not rewrite an original hypothesis after evidence arrives.
- Add dated evidence and a separate revision note.
- Confidence begins as `Unrated` until evidence is logged.
- Supporting and contradicting evidence must use source or claim IDs.
- A milestone is not confirmation unless its success criteria were defined in advance.

## Initial register

| ID | Hypothesis | Current confidence | Observable milestone | Falsification condition |
|---|---|---|---|---|
| H1 | Switch-side CPO reaches commercial proof before accelerator-side optical I/O. | Unrated | Qualified production deployment in a defined switch platform | Accelerator-side optical I/O meets the commercial-proof definition first |
| H2 | Bandwidth density and electrical reach become stronger adoption drivers than transceiver power alone. | Unrated | Customer evidence identifies reach or density as the binding constraint | Customers meet target systems economically with improved pluggables or copper and cite no binding reach or density constraint |
| H3 | Packaging yield, serviceability, qualification, and warranty allocation determine adoption timing more than isolated photonic-device performance. | Unrated | Repeatable final-package yield and completed system qualification correlate with production orders | Products scale broadly despite unresolved yield and serviceability constraints, or device performance remains the dominant blocker |
| H4 | Linear pluggables, retimers, active electrical cables, and near-packaged optics continue to coexist with CPO across different network positions. | Unrated | Customers deploy different architectures by topology and reach | CPO rapidly displaces alternatives across most relevant domains |
| H5 | Proprietary vertical integration leads early deployments, while standards and practical multi-sourcing become more important as volume broadens. | Unrated | Early deployment uses tightly controlled interfaces followed by qualified alternatives | Broad multi-vendor interoperability leads initial deployments, or proprietary systems remain sufficient at scale |
| H6 | External laser architectures improve serviceability and failure isolation but do not remove package, optical-engine, fibre, or control-system reliability risk. | Unrated | Field design shows replaceable or redundant lasers alongside separate engine failure controls | Integrated lasers prove superior in system reliability and economics, or external lasers fail to improve service outcomes |
| H7 | The economic winner differs from the technical leader because profit capture depends on platform control, customer ownership, manufacturing scarcity, and cannibalisation. | Unrated | Company scorecards show different leaders across technology, volume, and incremental gross profit | The same company leads verified technology, volume, and sustainable profit capture |
| H8 | No single company leads both switch-side CPO and accelerator-side optical I/O across every critical value-chain layer. | Unrated | Architecture-specific scorecards show multiple control points and leaders | One company establishes durable leadership across both architectures and the majority of economic content |
| H9 | Announcements and demonstrations systematically precede economically relevant production by a material qualification and manufacturing interval. | Unrated | Product histories show measurable time between demonstration, qualification, and repeat volume orders | Multiple products progress from demonstration to meaningful adoption with no material interval |
| H10 | The best public-equity opportunity is determined by incremental earnings relative to priced expectations, not by optical market share alone. | Unrated | Valuation and earnings bridge produces a different ranking from technology or shipment share | Technology or shipment leadership consistently maps directly to the best risk-adjusted equity outcome |
| H11 | Within external scale-out photonics, complete optical-engine integration and manufacturing capability produces more durable economic differentiation than isolated PIC performance. | Unrated | Comparable products show persistent advantages in qualified yield, cost, reliability and retained gross margin | Standalone PIC leaders capture superior sustainable profit without controlling packaging, test or engine manufacturing |
| H12 | High-power InP lasers and serviceable ELSFP architectures form a scarce secondary profit pool across multiple silicon-photonics engines. | Unrated | Repeat multi-customer orders convert into attractive-margin revenue while qualified supply remains concentrated | Lasers become readily multisourced, integrated alternatives dominate, or price erosion eliminates excess returns |
| H13 | Platform owners capture the largest absolute CPO rent, while external optical-engine suppliers may offer greater CPO earnings materiality. | Unrated | Company-level content and margin work shows higher absolute profit for platform owners but greater earnings sensitivity for focused suppliers | External suppliers capture both the largest absolute profit and highest materiality, or platform owners retain little incremental value |
| H14 | Coherent and Lumentum belong in the core scale-out optical-engine/PIC comparison, while Meta belongs only in customer and adoption evidence. | Unrated | Comparable engine, PIC, packaging and commercial evidence is established for Coherent and Lumentum | Neither company controls economically meaningful engine or PIC design, or Meta discloses a directly controlled competitive design |

## Evidence log template

| Date | Hypothesis ID | Evidence ID | Direction | Evidence quality | Effect on confidence | Model change | Notes |
|---|---|---|---|---|---|---|---|
| 2026-08-07 | H3 | CLM-019; CLM-020 | Supports | Medium | Remains Unrated pending primary manufacturing data | None | The review identifies thermal pathways, yield, burn-in and test as scale constraints, but supplies no matched production economics. |
| 2026-08-07 | H11 | CLM-021; CLM-022; CLM-023; CLM-024 | Mixed | Medium | Remains Unrated | Add monolithic InP transmitter as a benchmark architecture | Nokia demonstrates substantial functional integration and controlled output, but full-engine yield, qualification, reliability and cost are unknown. |
| 2026-08-07 | H12 | CLM-021; CLM-022 | Mixed | Medium | Remains Unrated | Add integrated InP as an explicit ELS countercase | A capable integrated-laser transmitter architecture weakens any assumption that external lasers are the only viable high-power pathway; it does not establish comparative reliability or economics. |

Allowed directions:

- Supports
- Contradicts
- Mixed
- Context only

## Revision log

| Date | Hypothesis ID | Previous view | Revised view | Reason | Evidence IDs |
|---|---|---|---|---|---|
