# Public manufacturing-readiness dossier — qualified CPO optical engines

**Status:** Private, public-source decision dossier; not for public release  
**As of:** 2026-08-13  
**Decision question:** Which part of producing a qualified, serviceable CPO optical engine is most likely to constrain scale and capture value?

## Executive decision

**Current answer — inference, medium confidence:** the likely scale constraint is
the *coupled fibre-interface and final-engine qualification loop*, not the PIC
alone. Fibre attach / connector architecture determines whether a technically
functional optical die survives packaging with acceptable loss and recovery;
known-good-die, wafer/package test and burn-in determine whether that loss is
found early enough to avoid scrapping a much more expensive package. Neither
link has a public, product-matched production yield waterfall.

There are two different investment implications:

1. **Most likely physical scale constraint:** fibre attach, coupling and the
   package-interface boundary. The retained record has measured development
   interface yields, connection-count compounding and multiple package-loss
   mechanisms, but no production Cpk, recovery or accepted-engine denominator.
2. **Most visible near-term manufacturing control point:** electro-optical
   wafer/package test and burn-in. Teradyne/ficonTEC and Aehr provide public
   evidence of production-oriented equipment and follow-on capacity orders.
   That establishes an insertion point and capacity direction, **not** a
   customer CPO shipment, output, test cost, supplier revenue allocation or
   durable profit capture.

**No supplier is a proven manufacturing-profit leader.** A technical control
point becomes economically investable only when the same named engine has
accepted-output, test/rework, warranty and attributable-economics evidence.

## Evidence hierarchy and non-negotiable boundary

| Rank | Evidence class | What it can establish | What it cannot establish |
|---|---|---|---|
| 1 | Product-matched production record | Starts, accepted units, process yield, disposition and field exposure | Another supplier's economics or a different architecture's cost |
| 2 | Qualified module / process study | Failure mechanisms, screening sequence, reflow and stress boundary | HVM yield, throughput or gross margin |
| 3 | Equipment / capacity disclosure | Available capability, likely test insertion and capacity direction | Customer identity, CPO allocation, good-unit output or pricing |
| 4 | Vendor product / partnership claim | Proposed service boundary and route map | Adoption, production yield, service cost or supplier share |

The public record below is mostly ranks 2–4. The absence of rank-1 evidence is
not evidence of no deployment; it means the output is a ranked diligence view,
not a manufacturing-cost ranking.

## Ranked readiness and constraint map

| Rank | Process / service boundary | What is publicly demonstrated | What is not public | Scale constraint assessment | Value-capture assessment | Evidence quality |
|---:|---|---|---|---|---|---|
| 1 | Fibre attach, coupling and connector boundary | Development interface yield varies materially with edge-coupler geometry (75.5%, 68%, 57% in one imec development run); OIF shows connection-count yield compounding; detachable FAU routes exist | Automated first-pass yield, Cpk, recovery/scrap, mating-life distribution, accepted-engine yield and cost | **Highest unresolved physical scale risk.** Small attach defects multiply across dense interfaces and can be discovered late | Potentially valuable only if qualified attachment/service IP is scarce and tied to accepted-engine economics | Medium — mechanisms measured; no HVM denominator |
| 2 | Electro-optical wafer/package test and known-good components | Production-oriented double-sided wafer probe is available; NVIDIA describes pre-screening; wafer-level burn-in follow-on systems have been ordered | Seconds/test, coverage, escape rate, utilisation, cost/test, yield delta, named CPO customer and output | **Highest observable scale-enabling control point.** It can shift defect discovery earlier | Possible equipment/process value capture, but no CPO-specific revenue, margin or switching-cost proof | Medium — equipment and capacity signals, not output |
| 3 | Package, reflow and thermal assembly | IBM full-module OTVs show reflow/JEDEC learning; FOWLP and TGV research show package integration routes and coupling/thermal loss risks | Lot yield, Cpk, cycle time, rework, stress pass distribution and cost | High: the package joins expensive components and creates late-loss exposure | Potential OSAT/package control point, but no attributable CPO supplier economics | Medium-low — credible technical records, no HVM |
| 4 | External laser and engine service boundary | ELSFP / detachable-FAU architectures create separable laser or fibre-interface service concepts; Lumentum has accelerated laser-life data | Engine/laser failure allocation, field returns, MTTR, spare ratio, warranty owner/cost and customer acceptance | Material serviceability variable, especially when repair avoids switch/ASIC replacement | Could protect laser/connector content, but service economics are entirely open | Low-medium — component/vendor evidence |
| 5 | Rework, burn-in and qualification | Wafer-level burn-in capacity is expanding; IBM documents qualification workflow | Rework rate/recovery, burn-in duration/coverage, lot pass/fail, post-rework reliability and warranty reserve | Important cost amplifier; cannot yet rank versus attach or package | No attributable value proof | Low-medium |

### Why rank 1 and rank 2 are coupled

The engine is not economically qualified merely because the PIC works at wafer
test. The high-value sequence is:

```text
screened PIC/EIC/laser → attach or connector interface → package / reflow
→ optical + electrical test → burn-in / qualification → accepted engine
→ service return / warranty
```

Fibre attach creates a potentially high-multiplicity defect opportunity;
test/burn-in determines whether the defect is caught before the next expensive
step. A detachable fibre-array or laser boundary may reduce the cost of failure,
but it introduces connector qualification and field-service requirements. The
right investment question is therefore not “who has the lowest coupling loss?”
but “who controls the qualified good-engine cost after attach, test, recovery
and service?”

## Evidence by workstream

### 1. Fibre attach and connector architecture

- **imec / Chip Scale Review (`PAP-043`; `CLM-421`–`CLM-423`)** reported
  75.5%, 68% and 57% overall optical yield for three *development-run*
  edge-vertical-coupler lengths. It attributes losses to collective assembly,
  edge voids and lateral misalignment. This is the best retained direct signal
  that interface geometry changes yield; it is not final-engine yield.
- **OIF (`STD-014`)** illustrates how 1,088 versus 288 connections at an
  assumed 99.865% per-connection yield imply about 23.0% versus 67.8%
  first-pass board fibre-assembly yield. This is sensitivity arithmetic, not
  a production dataset, but supports treating connection count as an economic
  variable.
- **Lightmatter / SENKO / ASE (`CMP-050`; `CLM-401`–`CLM-405`)** provides a
  current detachable-FAU design route: vendor-reported below-1.5 dB insertion
  and re-insertion loss, passive assembly, and a known-good-engine concept.
  It does not provide mating-cycle population, environmental qualification,
  output or field-service evidence.
- **SENKO (`CMP-068`; `CLM-537`)** confirms a detachable connector ecosystem
  role in NVIDIA photonics, without an exact-SKU allocation or share.

**Decision implication:** treat fibre count, attach geometry, passive/active
alignment, recovery and service boundary as first-order diligence variables.
Do not promote a connector or attachment supplier on low insertion loss alone.

### 2. Known-good die, wafer/package test and burn-in

- **Teradyne (`CMP-049`; `CLM-393`–`CLM-396`)** identifies distinct wafer,
  engine, package/CPO and system test insertion points and flags alignment,
  thermal and high-speed electrical handling as scaling requirements.
- **Teradyne / ficonTEC (`CMP-052`; `CLM-432`–`CLM-434`)** announced a
  production-oriented double-sided wafer-probe cell for hybrid-bonded
  PIC/EIC wafers. It demonstrates available capability, not an installed
  customer line or an observed yield improvement.
- **Aehr (`CMP-056`, `CMP-080`; `CLM-518`)** reports follow-on automated
  multi-wafer silicon-photonics burn-in orders. The named product/customer,
  CPO allocation, wafer starts, pass rate and capacity utilisation remain
  undisclosed.
- **NVIDIA (`CMP-051`)** describes optical screening before fibre attachment
  and says only known-good components are integrated. Its “100% yield” wording
  has no disclosed stage denominator, and therefore cannot stand for final
  accepted-engine yield.

**Decision implication:** test/burn-in is the most observable place where
capital and process control are being prepared for scale. The next decisive
record is one named engine with test time, coverage, escape/rework and final
acceptance denominator—not another equipment order.

### 3. Package, reflow, thermal and reliability boundary

- **IBM (`PAP-042`; `CLM-479`–`CLM-482`)** is the strongest retained
  full-module process/reliability record. Its optical test vehicles document
  reflow compatibility and later JEDEC stress success after material/process
  changes; early samples failed. This makes package learning real, while the
  lack of HVM lot yield or field FIT prevents a cost conclusion.
- **FOWLP engine research (`PAP-045`; `CLM-487`–`CLM-490`)** demonstrates a
  1.6-Tb/s-class engine, wafer-level test and direct-drive measurements. It
  has no production yield, qualification, rework or cost waterfall.
- **TGV/interposer research (`PAP-046`; `CLM-476`–`CLM-478`)** shows a
  wafer-scale integration route but also reports large post-package optical
  output loss in its limited active-chip validation. It is a mechanism warning,
  not a production distribution.

**Decision implication:** package/process control is likely co-equal with
attach risk but has less direct public capacity evidence. Treat it as a
late-loss / reliability gate until data tie an OSAT flow to accepted engines.

### 4. External laser and service boundary

- **Lumentum (`CMP-082`)** reports accelerated reliability data for a
  CPO-targeted UHP laser / ELSFP context. It improves the component
  qualification signal but is neither an engine field-reliability record nor a
  warranty-cost datapoint.
- **Lumentum / NVIDIA (`CMP-067`; `CLM-536`)** and **Coherent / NVIDIA
  (`CMP-069`)** identify strategic laser/advanced-optics routes, but neither
  discloses exact CPO SKU allocation, share, unit volume or margin.

**Decision implication:** external laserization can create a more serviceable
architecture, but it shifts—not removes—the burden of qualified connectors,
interface losses, spares and warranty ownership.

## What would change the ranking

| New public record | Effect on conclusion |
|---|---|
| Production fibre-attach attempts, first-pass yield, recovery/scrap and cycle time for a named engine | Could establish whether attach is actually the dominant scale constraint |
| Test seconds, coverage, escapes and cost per accepted die/engine on a named production line | Could quantify whether test is a meaningful recurring value pool rather than an enabling tool |
| Package starts-to-accepted-engine and post-qualification distribution | Could elevate package/reflow above attach as the key cost driver |
| Fleet field returns, MTTR, spare ratio and warranty allocation for a detachable service boundary | Could show whether external lasers/connectors improve total replacement economics |
| Supplier contract / filing allocating SKU, share, ASP and gross margin | Required before assigning durable manufacturing profit capture |

## Immediate desk-research queue

1. Search patents, OIF/IEEE/OCP material and service manuals for detachable
   FAU/ELSFP mating, contamination, repair and management boundaries.
2. Recheck Teradyne, ficonTEC and Aehr quarterly materials for named customer,
   installed-base, test-throughput or SiPh-specific financial allocation.
3. Search OSAT/foundry presentations for optical assembly, active alignment,
   known-good die, hybrid-bonded SiPh and reliability process metrics.
4. Map each result to the same denominator: attempted component → accepted
   engine → field service. Do not add generic CPO articles that do not change a
   gate.

## Bottom line

The next focused thesis is **not** “fibre attach will be the winner.” It is:

> **A qualified optical engine is likely constrained by the interaction of
> high-density fibre interface yield and the ability to test, burn-in and
> recover defects before expensive final integration. Public evidence makes
> test/burn-in the clearest observable scaling control point, but it leaves
> fibre attach as the most important unresolved physical-yield risk. Neither
> has public evidence sufficient to assign a CPO profit-pool leader.**

This conclusion is an inference from the public records above and is falsified
by a product-matched production waterfall showing another stage dominates the
cost per accepted, serviceable engine.

## Source and claim anchors

All records are retained privately with their source-log entry and companion
evidence note. Canonical public sources are recorded there; use the IDs below
to retrieve the full source rather than treating this dossier as a source.

| Topic | Source / claim anchors |
|---|---|
| Fibre-interface mechanisms | `PAP-043`; `CLM-421`–`CLM-423`; `STD-014` |
| Detachable interface / connector routes | `CMP-050`; `CMP-068`; `CLM-401`–`CLM-405`; `CLM-537` |
| Test and known-good routes | `CMP-049`, `CMP-051`, `CMP-052`, `CMP-056`, `CMP-080`; `CLM-393`–`CLM-396`; `CLM-432`–`CLM-434`; `CLM-518` |
| Package / reliability routes | `PAP-042`, `PAP-045`, `PAP-046`; `CLM-476`–`CLM-490` |
| Laser / external service boundary | `CMP-067`, `CMP-069`, `CMP-082`; `CLM-536` |

## Release control

This is a private synthesis. A public derivative may state the evidence-gated
conclusion and cite the original public source, but must not expose private
claim IDs, local paths, source archives, restricted material or unverified
production assumptions.
