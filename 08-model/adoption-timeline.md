# CPO Adoption Timeline Model

**Model horizon:** 2026 to 2032
**Status:** Framework only, no forecast populated
**Last updated:** 2026-08-06

## Modelling unit

Build one adoption curve for each combination of:

```text
Architecture
Deployment domain
System generation
Customer type
Geography, if material
```

Do not combine switch-side CPO with accelerator-side optical I/O.

## Maturity states

| State | Description |
|---:|---|
| 0 | Concept or roadmap only |
| 1 | Component demonstration |
| 2 | Integrated-system demonstration |
| 3 | Customer sampling or qualification |
| 4 | Limited production |
| 5 | Commercial proof |
| 6 | Meaningful adoption |

Use the working definitions in `../00-scope/terminology.md`.

## Viability gates

An architecture cannot advance to commercial proof until evidence supports all material gates:

| Gate | Required evidence | Failure implication |
|---|---|---|
| Technical performance | Defined bandwidth, reach, BER, link margin, and workload boundary | Architecture cannot meet the use case |
| All-in power | Host, optics, lasers, control electronics, and cooling included | Power advantage may be overstated |
| Thermal behaviour | Performance across realistic gradients and workloads | Reliability or control cost may be unacceptable |
| Manufacturing yield | Final-package, engine, fibre-attach, test, rework, and scrap evidence | Cost and capacity do not scale |
| Reliability | Qualification, burn-in, lifetime, failure-mode, and field evidence | Operational risk remains unacceptable |
| Serviceability | Failure isolation, replacement unit, spares, and MTTR | System TCO may favour alternatives |
| Supply chain | Capacity, qualified suppliers, and critical bottlenecks | Volume timing is constrained |
| Interoperability | Defined interfaces and practical multi-sourcing where required | Customer adoption may remain narrow |
| Customer motivation | Binding problem and purchasing criteria confirmed | Technology may solve a non-urgent problem |
| Economics | Total cost per delivered bit beats credible alternatives | Adoption remains technically possible but uneconomic |

## Critical-path milestones

For every architecture, track:

```text
milestone_id
architecture
deployment_domain
company
milestone
planned_date
observed_date
status
evidence_id
gate_affected
probability_before
probability_after
notes
```

Examples include qualification completion, published system power, final-package yield improvement, second-source qualification, repeat production orders, customer deployment, and field-reliability evidence.

## Annual forecast table

Populate only after the denominator and evidence are defined.

| Architecture and domain | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Switch-side CPO, defined domain | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Accelerator optical I/O, defined domain | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Near-packaged optics, defined domain | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

Each cell should ultimately contain adoption rate, probability range, or both. Never mix system share, port share, and revenue share.

## Adoption logic

For a defined domain:

$$
\text{CPO systems}
=
\text{Relevant systems shipped}
\times
\text{CPO adoption rate}
$$

$$
\text{Optical engines}
=
\text{CPO systems}
\times
\text{Optical engines per system}
$$

$$
\text{Probability-weighted supplier revenue}
=
\text{Optical engines}
\times
\text{Supplier share}
\times
\text{ASP}
\times
\text{Scenario probability}
$$

## Scenario requirements

Every bear, base, and bull case must state:

- Technical trigger
- Critical-path milestone dates
- Qualification and production status
- Adoption denominator
- Unit volume
- Supplier content and share
- Revenue and gross-profit effect
- Cannibalisation
- Research and capital requirements
- Warranty and inventory risk
- Valuation consequence
- Evidence that invalidates the case

## Review cadence

- Update the milestone tracker when new evidence arrives.
- Review probabilities monthly or after a thesis-changing event.
- Record every probability change.
- Compare forecast versus observed milestones quarterly.
- Preserve prior model versions for calibration.
