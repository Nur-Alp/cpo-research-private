# Current CPO Decision Memo

**Owner:** Nur Alpys  
**As of:** 2026-08-10  
**Status:** Provisional, evidence-gated; not an investment recommendation

## Current answer

| Required output | Current evidence-adjusted answer |
|---|---|
| Architecture | Switch-side CPO at 200G/lane has the strongest near-term commercial signal. Retimed/advanced pluggables remain the principal countercase; LPO at 200G/lane is not yet supported by a matched measured system. |
| Deployment domain | Ethernet scale-out switching is the best-supported early domain. Inter-rack scale-up CPO has a stronger strategic value case but a different product and supplier denominator. |
| Commercial-proof year and probability | **2027 is the central diligence year**, with a bounded prior of 65–82% for commercial proof by year-end; the current 2026 prior is 45–65%. These are analyst priors, not observed adoption rates. The event still requires repeat paid production from two independent customers or sustained/repeated production by one major customer. |
| Meaningful-adoption year and probability | Not numerically established. A 2028–2030 adoption window is a scenario to test, not a sourced forecast, because no exact customer/system denominator, accepted-unit numerator, matched TCO, yield or service bundle is public. |
| Technical leader | No single overall leader. Broadcom leads the disclosed merchant-switch CPO definition; NVIDIA leads the integrated system/customer route; TSMC is the clearest process/stacking control point. |
| Volume leader | Not established. Vendor “production” and limited-shipment statements do not provide a reconciled CPO SKU, accepted units, repeat shipments or field population (`CLM-345`–`CLM-350`, `CLM-411`–`CLM-420`, `CLM-435`–`CLM-437`). |
| Profit-pool leader | Not established. Coherent has the broadest disclosed optical-engine/component stack; Lumentum has the clearest external-laser order and capacity signal. Neither has public product allocation, qualified engine yield, supplier share, ASP or realised CPO margin. |
| Best public-equity opportunity | No decision. Earnings materiality, cannibalisation, capex, valuation expectations and downside remain unlinked to attributable CPO economics. |
| Evidence quality | Strong technical and process triangulation; weak customer-unit, final-yield, service-cost and supplier-economics evidence. |

## Why this is the current answer

NVIDIA states that Spectrum-X Ethernet Photonics is in full production and identifies a TSMC/SPIL/TFC/Foxconn manufacturing route, pre-shipment validation and first adopters. Broadcom separately defines a 102.4T, 200G/lane CPO product family. Those records materially improve timing and process confidence, but none identifies a customer-accepted CPO SKU, unit numerator, final-engine yield, repeat shipment record or supplier economics (`CLM-435`–`CLM-437`, `CLM-076`–`CLM-079`).

The strongest manufacturing evidence remains boundary-specific. imec reports 57%–75.5% optical-interface yield in a development run (`CLM-421`–`CLM-423`); OIF’s illustrative 99.865% per-connection assumption compounds to approximately 23.0% first-pass board yield at 1,088 connections (`CLM-397`–`CLM-400`); Teradyne/ficonTEC identifies production-oriented wafer-probe infrastructure without factory output (`CLM-432`–`CLM-434`); and the FOWLP/TGV engine papers demonstrate technical routes without production economics (`CLM-424`–`CLM-447`). PAP-046 adds an 8-inch wafer-level TGV interposer with 110 GHz/128-Gbaud and EML/driver flip-chip evidence, while PAP-048 adds a later abstract-level TSV/TGV boundary above 67/110 GHz and 128-Gbaud support (`CLM-445`–`CLM-447`, `CLM-451`–`CLM-453`). Neither changes the final-engine production boundary. PAP-047 adds the explicit system-level counterweight: packaging, thermal stability, compounded yield, standardization, serviceability and lifecycle robustness must be tested alongside PIC efficiency (`CLM-448`–`CLM-450`). These are reasons to keep final-engine yield and test/rework as hard gates, not reasons to declare a winner.

The latest academic additions sharpen rather than resolve the decision. Gao et al.'s PAP-049 review makes FOWLP, TSV and TGV the relevant packaging-route comparison, but its cited demonstrations remain separate from production yield, qualification and economics (`CLM-454`–`CLM-457`). Chung's PAP-050 preprint is a low-confidence lead that thermal drift may require workload-aware control in heterogeneous SoIC packages; it is not independent product evidence (`CLM-458`–`CLM-460`). Tran et al.'s PAP-051 full three-page paper provides measured 160/180-GBd component results but only a modeled 212.5-GBd/400G-lane boundary, not a measured end-to-end link (`CLM-461`–`CLM-463`). The later full-paper packet also upgrades PAP-028's detachable known-good-module mechanism, PAP-029's 224G/lambda FOWLP engine, PAP-030's +20 dBm polymer-waveguide stability, and PAP-044's 400-Gbps TGV engine/serviceability boundary (`CLM-495`–`CLM-513`). These strengthen the engineering comparator but still do not provide final-engine yield, qualification, service cost or supplier economics. The next highest-value work is therefore targeted full-text acquisition and matched system/production evidence—not a broad expansion of the paper count.

PAP-052 adds a simulation-led passive vertical-coupling hypothesis: optical fanout and self-alignment may reduce active-alignment burden and increase PIC density, but the paper supplies no fabricated package, process capability, final-engine yield or cost data (`CLM-464`–`CLM-467`). It is useful for interview questions about the packaging control point, not for ranking a route or company.

PAP-053 supplies an important counterweight: the full three-page paper reports a TEC-less 100-GHz-class eight-channel InP MZ PIC reaching net 400G/lane over 500 m from 20–80°C, with broadly temperature-insensitive BER and adjacent-channel crosstalk below −30 dB to 90 GHz. This strengthens the advanced-pluggable/PIC deferral case, but the paper does not disclose module power, complete driver/PIC co-package, fibre attach, yield, qualification or economic boundary (`CLM-468`–`CLM-470`, `CLM-483`–`CLM-486`). CPO therefore still cannot be declared inevitable on lane-rate capability alone.

PAP-054 raises that counterweight materially: a full open paper reports 225-GBaud TFLN PAM4 with a 3-nm SerDes at 3.36 Tb/s aggregate over 2 km, and DR8 operation at 500 m and 2 km, with an uncooled laser temperature sweep from 30–85°C (`CLM-471`–`CLM-475`). This is still a laboratory transmission demonstration, but it means the CPO thesis must win on complete system power, package density, serviceability, qualification, cost or customer deployment—not simply on 400G/lane capability. The newly reviewed full PAP-046 similarly exposes a TGV packaging loss boundary: the EML optical output falls from 4.9 dBm before packaging to −0.07 dBm after packaging in the reported single-device test (`CLM-476`–`CLM-478`).

The current commercial-proof ranges are recorded in [commercial-proof probability priors](../08-model/commercial-proof-probability-priors.md). They must not be multiplied by market size or translated into supplier revenue. The adoption model remains denominator-gated in [adoption timeline](../08-model/adoption-timeline.md).

## Main disconfirming evidence

The thesis should be downgraded if any of the following is observed:

1. Named customers continue deploying 200G/lane systems primarily with RTLR/LPO or advanced pluggables at acceptable power, reach, serviceability and cost.
2. CPO final-engine yield, fibre-attach rework or field-replacement cost remains materially worse than the pluggable alternative after production qualification.
3. “Production” CPO shipments resolve to evaluation quantities, non-CPO SKUs or platform announcements without repeat paid volume.
4. Supplier contracts show that optical-engine content is low-margin, heavily price-down exposed or captured mainly by the switch/platform owner rather than the PIC/engine supplier.
5. Inter-rack scale-up CPO or accelerator optical I/O captures the actual high-value deployment while switch-side scale-out CPO remains narrow.

## Next thesis-changing catalysts

The next evidence that would change the conclusion is, in priority order:

1. Customer-side confirmation of a named Spectrum-X Photonics or TH6-Davisson CPO SKU, ports/units, production date and repeat shipment.
2. A complete per-system content map: engine count, PIC, laser/ELSFP, driver/TIA, fibre attach, package, test owner and supplier share.
3. A final-engine yield waterfall with attach cycle time, test/rework, qualification lot, field replacement and warranty allocation.
4. Conversion evidence for Lumentum’s disclosed CPO order and Coherent/Lumentum capacity routes into attributable qualified engine or laser shipments.
5. Celestica’s planned 2027 hyperscaler CPO programme reaching an identified production system with volume and margin disclosure.

Until one of these gates is cleared, the correct conclusion is **strongest timing signal, no proven volume leader, no proven profit-pool leader, and not yet investable**. The academic packet is now sufficient for the technical architecture comparison; additional papers should be added only when they directly close a P0 gap (matched 400G/lane system data, final-engine yield, qualification or service economics). The highest-marginal-value next step is primary evidence collection from OSAT/test, fibre-attach, optical-engine/laser suppliers, platform owners and hyperscalers using the [interview question bank](../09-primary-research/interview-question-bank.md).
