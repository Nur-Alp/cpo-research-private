# NWS-002 — OCP Global Summit 2025 recap

**Publisher:** Irrational Analysis  
**Date:** 2025-10-24  
**Type:** Secondary conference recap  
**Canonical source:** [OCP Global Summit 2025: Irrational Recap](https://irrationalanalysis.substack.com/p/ocp-global-summit-2025-irrational)

## How to use this source

This recap is useful for identifying which conference claims require retrieval and primary-source checking. It mixes author opinion, booth observations, hearsay and technical interpretation. The original article is retained by hyperlink rather than reproduced locally.

## Decision-relevant observations

1. The author reports Broadcom reliability/power material and describes a zero-failure observation over approximately one million device-hours, with an asserted statistical MTBF boundary. This is potentially high-value evidence, but the original Broadcom presentation, sample definition, stress conditions, censoring method and confidence calculation must be obtained before it enters the reliability benchmark.
2. The recap treats external, serviceable laser sources as a way to isolate one failure domain, while noting that PIC, photodiode, fibre-attach and package failures remain. This is directionally consistent with the project’s external-light boundary, but the article’s “intrinsically more reliable” language is not accepted as a universal result.
3. It reports that Marvell showed little public quantitative CPO data at the event and criticizes optimistic 400G electrical-SerDes assumptions. These are conference observations, not proof of Marvell product weakness or of a universal 400G electrical limit.
4. It highlights test equipment and large-lane BERT capability as a possible yield-enabling control point. This is a useful diligence prompt for final-package test economics, but the claimed ecosystem yield improvements need primary customer or supplier evidence.

## Claims and limitations

- `CLM-141`: secondary report of Broadcom reliability evidence; primary slide/source required before scoring.
- `CLM-142`: serviceability/failure-domain interpretation; not a measured universal CPO reliability result.
- `CLM-143`: secondary report of sparse Marvell quantitative disclosure and skepticism about 400G electrical SerDes; not a product verdict.
- `CLM-144`: test-equipment/yield-control hypothesis; no independently verified yield data in this source.

## Primary-source follow-ups

1. Locate the Broadcom OCP/Hot Chips reliability presentation and record device-hour denominator, FEC/BER conditions, temperature, population and statistical confidence.
2. Reconcile external-laser serviceability with the OIF ELSFP management boundary and the packaging benchmark’s engine failure modes.
3. Obtain Marvell’s actual CPO/SerDes conference material before making any maturity comparison.
4. Verify any backplane-test yield claims with the equipment vendor, rack integrator or customer.

## Cross-checks

- [External-light serviceability boundary](../../03-components/external-light-serviceability-boundary.md)
- [Packaging and fibre-attach benchmark](../../03-components/packaging-reliability-benchmark.md)
- [Linear-drive optics boundary](../../02-architecture/linear-drive-boundary-benchmark.md)
- [Broadcom and NVIDIA dossier](../../07-companies/broadcom-nvidia-switch-cpo-platform-dossier.md)
- [Claim ledger](../claim-ledger.csv)
