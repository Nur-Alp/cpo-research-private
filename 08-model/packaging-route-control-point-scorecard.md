# Packaging-route control-point scorecard

**Owner:** Nur Alpys  
**As of:** 2026-08-10  
**Status:** Evidence-matched qualitative scorecard; not a production forecast

## Decision question

Which packaging route is most likely to create a defensible control point in a scale-out optical engine, after optical performance, thermal behavior, manufacturing yield, serviceability and economics are considered together?

The scorecard compares FOWLP, TSV and TGV as packaging routes. It does not rank a PIC vendor or infer company profit from a route-level advantage. `PAP-049` is a review and source map; its cited prototype results remain separate from primary production evidence (`CLM-454`–`CLM-457`).

## Route comparison

| Dimension | FOWLP | TSV | TGV |
|---|---|---|---|
| Primary technical advantage | Reconstituted-wafer / fan-out integration, short EIC–PIC path and potential cost/yield scalability | Highest vertical interconnect density and strong silicon thermal conduction | Optical transparency, low-loss electrical path, large-area/panel scalability and thermal-expansion match to silicon |
| Strongest retained evidence | 51.2-Tb/s prototype at 0.9 pJ/bit summarized by `PAP-049`; full `PAP-045` reports a 1.6-Tb/s-class eight-channel engine with 112-Gbaud NRZ/PAM4 and direct-drive TDECQ around 2.08–2.32 dB | >67-GHz 3-dB interposer bandwidth in `PAP-048`; high-density 3D integration literature summarized by `PAP-049` | >110-GHz 3-dB interposer bandwidth and 128-Gbaud support in `PAP-048`; 400-Gbps engine boundary summarized by `PAP-044` and `PAP-049` |
| Thermal / mechanical risk | Lower thermal conductivity than silicon routes; warpage, mould and thermal-interface design remain open | Metal–silicon expansion mismatch, thermal stress and cost/area penalty | Lower thermal conductivity than silicon; thermal-expansion match can reduce stress, but heat extraction must be engineered |
| Optical coupling / fibre path | Edge coupling and mould-first process may reduce interfaces, but alignment and contamination control are critical | Requires auxiliary optical coupling structures in many implementations; PIC-area and process complexity matter | Glass transparency supports waveguides, grating/edge couplers and fibre routing; TGV and connector interfaces become part of the yield boundary |
| Serviceability potential | Can support separable or optics-last flows, but route-specific replacement data are not public | Dense 3D integration tends to make package-level replacement difficult; no public field-service dataset | Localized optical-module replacement and detachable routes are technically plausible; no public MTTR, failure or warranty data |
| Manufacturing-control opportunity | Wafer/panel process, mould/RDL, optical attach and known-good-die test | Via formation, wafer thinning, bonding, thermal control and high-density assembly | Glass processing, TGV metallization, waveguide/coupler formation, panel handling and fibre attach |
| Evidence status | **Promising technical/prototype route; production yield open** | **Promising density route; cost and thermal/yield gates open** | **Strongest current 400G-class packaging comparator; production and service gates open** |
| Profit-pool implication | Potential cost leverage if yield and panel throughput are demonstrated; not yet attributable to a supplier | Potential process/IP control point if density and thermal performance justify cost; no margin evidence | Potential control point across substrate, coupler, connector and service boundary; no proof that substrate supplier captures the economic rent |

## Control-point interpretation

1. **TGV currently has the strongest technical control-point case for the 400G-class engine**, because the retained record combines high-frequency bandwidth, optical transparency and a serviceability-compatible glass route. This is a technical hypothesis, not a production or profit conclusion (`PAP-044`, `PAP-048`, `CLM-451`–`CLM-453`).
2. **FOWLP remains the strongest cost/yield countercase** if its fan-out and known-good-die flows produce repeatable good engines at volume. The retained 51.2-Tb/s prototype and full 1.6-Tb/s-class `PAP-045` engine do not provide that production denominator (`PAP-045`, `PAP-049`, `CLM-455`, `CLM-487`–`CLM-490`).
3. **TSV remains the density/performance route**, but the control point may sit with advanced-package integration and thermal management rather than with the interposer material alone. The public evidence does not clear the cost, yield or service boundary (`PAP-048`, `PAP-049`, `CLM-454`, `CLM-457`).
4. **No route guarantees supplier profit.** The profit leader still depends on who owns the qualified BOM, process recipes, fibre attach, test/rework, customer qualification, price and warranty exposure.

## Gates required before a numeric route score

| Gate | Required evidence | Current status |
|---|---|---|
| Complete-engine performance | Same lane rate, reach, BER/TDECQ, temperature and power boundary | Open across all three routes |
| Manufacturing yield | Lot-level die-to-good-engine yield, attach Cpk, test escape, rework recovery and scrap | Open; prototype and development-run data are not sufficient (`CLM-312`–`CLM-314`, `CLM-421`–`CLM-423`) |
| Thermal/reliability | Qualification conditions, sample counts, pass/fail distributions, field returns and warranty allocation | Open; IBM stress work is a process anchor, not a fleet record (`CLM-357`–`CLM-359`) |
| Serviceability | Replaceable boundary, MTTR, spare inventory, downtime and failure-domain data | Open; detachable or localized replacement concepts are not field economics (`CLM-239`–`CLM-240`, `CLM-424`–`CLM-427`) |
| Profit capture | ASP, supplier share, price-down, second source, capex and attributable gross margin | Open for all routes (`CLM-070`, `CLM-073`, `CLM-083`) |

## Provisional conclusion

The current evidence supports a **route hierarchy for diligence**, not a winner:

- TGV: strongest 400G-class technical control-point hypothesis.
- FOWLP: strongest cost/yield and scalable-assembly countercase.
- TSV: strongest density route, with the largest unresolved thermal/cost integration burden.

The next research step is to map each route to named suppliers and a common cost-per-qualified-good-engine waterfall. Until that is done, route leadership must not be translated into company leadership, adoption share, ASP or public-equity upside.

## References

- [PAP-044 evidence note](../01-sources/papers/PAP-044-kang-tgv-400g-optical-engine-evidence-note.md)
- [PAP-045 evidence note](../01-sources/papers/PAP-045-li-fowlp-silicon-photonic-engine-2025-evidence-note.md)
- [PAP-048 evidence note](../01-sources/papers/PAP-048-ge-tsv-tgv-high-density-cpo-2026-evidence-note.md)
- [PAP-049 evidence note](../01-sources/papers/PAP-049-gao-heterogeneous-integration-cpo-review-2025-evidence-note.md)
- [Packaging, fibre-attach and serviceability benchmark](../03-components/packaging-reliability-benchmark.md)
- [Manufacturing cost per good engine gate](manufacturing-cost-per-good-engine-gate.md)
