# Figure candidate audit — 18 August 2026

**Status:** Private figure-selection workpaper; source-page previews are retained
for analysis only. Nothing in this folder is cleared for the public website.

## Decision rule

Use a retained source figure directly only when the publisher's licence or an
explicit reuse permission permits it. A DOI, open-access landing page or a
publicly viewable PDF is not, by itself, a public-reuse licence. The default
public treatment is therefore an original redraw that preserves the source's
measured inputs, cites the canonical source, and labels any added assumptions.

## Highest-value candidates

| Rank | Candidate | Best report use | Why it earns space | Public treatment |
|---|---|---|---|---|
| 1 | PAP-035, p. 6, optical-attach-first versus optical-attach-last process flow | Manufacturing and reliability | Directly explains where attach order changes defect containment, rework and late-stage scrap | Redraw the two flows; do not reproduce the source artwork without permission |
| 2 | PAP-015, pp. 5–6, GLP/OBR process-control and model-performance panels | Fibre attach and serviceability | Connects metrology choice to process control and correlation quality—the strongest evidence for an attach-control thesis | Redraw the decision logic and report the source's measured relationships; retain the source page privately |
| 3 | PAP-056, pp. 4 and 6, wafer-level optical test and 1.6T FOWLP interconnect measurements | Optical engines and PICs | Shows a manufacturable wafer/package test path and measured interconnect loss at the 1.6T boundary | Redraw the test flow and one bounded measurement chart; label 6.4T/12.8T extrapolations as modelled |
| 4 | PAP-044, p. 6, packaged 400G optical-engine photographs and assembly | Optical engines and PICs | A readable physical-engine exhibit makes the package boundary concrete and supports the TGV/serviceability discussion | Prefer a captioned schematic or licensed source image; no direct crop yet |
| 5 | PAP-055, p. 3, field-replacement and thermal-stress discussion | Architecture contest / serviceability | Gives the clearest source-backed explanation of why CPO changes the replaceable failure domain | Redraw as a simple failure-domain diagram; do not present the paper page as a public figure |
| 6 | PAP-051, p. 2, 180-GBaud driver/modulator assembly and measured responses | PIC/EIC boundary | Useful high-rate component evidence, but narrower than the top five and not a complete engine result | Redraw only if the component boundary is discussed; otherwise cite in text |

## Recommended public additions

Add four original exhibits in the next public edition:

1. **Attach-order decision tree** — redraw PAP-035 p. 6, with columns for
   defect detection, reworkability and expected scrap boundary.
2. **Fibre-attach control loop** — redraw PAP-015 pp. 5–6 as
   metrology → correlation → release decision; retain the measured source
   relationships but avoid copying its plots.
3. **Wafer-to-engine test path** — redraw PAP-056 p. 4 and p. 6 as wafer
   probe → vertical optical I/O → FOWLP/RDL → substrate → electrical/optical
   measurement, with the 1.6T measured boundary called out.
4. **CPO failure-domain map** — original diagram informed by PAP-055 p. 3,
   contrasting field-replaceable pluggable optics with external-light,
   connector/FAU and non-field-replaceable engine boundaries.

These four exhibits answer the report's unresolved manufacturing question more
directly than additional vendor photos: where defects are detected, what can be
reworked, and which boundary becomes economically difficult to service.

## Candidates not selected for immediate publication

- PAP-044 p. 9 is a useful measured-results table, but it is too dense for the
  main report; use it as a source note or a compact redraw if the 400G section
  expands.
- PAP-051 p. 2 is technically strong but only covers a driver/modulator
  subassembly. It should not visually stand in for full-engine evidence.
- Direct website screenshots and investor-deck images are not selected unless
  an explicit public-use basis is recorded. Recreate the analytical point and
  link the original page instead.

## Evidence and attribution requirements

Every approved public exhibit must record: source ID, canonical URL/DOI,
publication date, page/figure number, measured versus modelled boundary,
calculation/recreation method, and public-use status. The private page previews
in `pages/` are working references only and must never be linked from the
public site.
