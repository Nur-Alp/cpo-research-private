# Decision-changing evidence acquisition queue

**Status:** Private operating document; no publication, commit or push.  
**As of:** 12 August 2026  
**Decision:** What specific evidence could turn the current CPO work from a technology map into an investable, evidence-backed commercial conclusion?

## Operating rule

Do not add a source merely because it discusses CPO. An item enters the source log and claim ledger only if it can alter one of the following:

1. exact product/customer/acceptance/scale/repeatability for NVIDIA SN6800/SN6810 or Broadcom BCM78919/TH6-Davisson;
2. a product-matched supplier role for PIC/engine, EIC, laser, fibre attach, package, connector or test;
3. a production manufacturing input—yield, test, rework, reliability, service or warranty;
4. a commercial/economic input—content, share, ASP, price-down, margin, capacity commitment or cancellation protection; or
5. a matched CPO/LPO/NPO/retimed system comparison at the same bandwidth, topology and service boundary.

The current controlled result remains: **no platform clears the public customer-scale-repeatability gate, and no company clears the CPO profit-pool gate.** See the [commercial-proof audit](commercial-proof-readiness-audit-2026-08-11.md), [supplier reconciliation](../08-model/switch-cpo-sku-content-reconciliation.md) and [economic-disclosure audit](company-economic-disclosure-audit-2026-08-11.md).

## Priority 0 — exact switch-CPO commercial proof

## Next quarterly review packet

Use this packet at each evidence cut-off. A row may move only when the stated evidence bundle is retained and its product boundary matches the claim. If nothing changes, record **no change** rather than treating silence as confirmation or disconfirmation.

| Gate owner / packet item | Current state | Next evidence route | Allowed state transition | Downstream document |
|---|---|---|---|---|
| NVIDIA exact-SKU customer proof | Open | Customer/OEM record naming `SN6810`/`SN6800` or matching `-LD` label, acceptance date, units/ports and repeat event | Open → partial customer proof → cleared only after repeatability | NVIDIA dossier; customer-proof register; milestone tracker |
| Broadcom exact-SKU customer proof | Open | Customer/OEM/integrator record naming `BCM78919`/TH6-Davisson, acceptance date, units/ports and repeat event | Open → partial customer proof → cleared only after repeatability | Broadcom dossier; customer-proof register; milestone tracker |
| Supplier-content attribution | Open/route-level | Product-linked BOM or qualification record for PIC/engine, EIC, laser, attach, package, connector and test | Route → exact-SKU role; economics remain open until share/price | Content-attribution map; six-company register |
| Manufacturing yield/service | Open | Lot-level starts → screened → assembled → tested → accepted, plus rework, field returns, MTTR and warranty | Process signal → production evidence; never directly to profit leadership | Manufacturing checklist; yield reconciliation; service model |
| Matched architecture comparison | Open | Same ASIC/ports/lane/reach/FEC/ambient with inlet power, cooling, yield, service and cost | Technical partial → matched system evidence; no universal winner by one field | Architecture scorecard; TCO gate |
| Analyst overlay | Not eligible | Reconciled fiscal-period baseline plus product-matched CPO inputs and source-use status | Pending → derived private sensitivity only; never observed fact | Analyst register; scenario specification |

**Quarterly sign-off:** record the cut-off date, reviewer, sources searched, inaccessible routes, state changes, withdrawn claims and unchanged core conclusions. A scheduled event, unavailable page, unchanged roadmap or secondary repetition is a retrieval status—not a milestone outcome.

| Evidence request | Exact acceptable record | Best owner/source route | Gate that can move | Explicit non-qualifiers |
|---|---|---|---|---|
| NVIDIA customer acceptance | Named operator/OEM states it accepted or deployed SN6800, SN6810, SN6800-LD or SN6810-LD, with date and system/port range | Customer deployment engineering post, procurement/qualification release, Dell customer case study, NVIDIA customer announcement; follow up Supermicro on CMP-071 for exact SKU and customer denominator | Customer and acceptance | Spectrum-X generally; partner/adopter list; Supermicro's grouped Spectrum-X/Quantum-X integration statement; SN6600-LD; a product listing |
| NVIDIA repeatability | A second dated delivery, expansion, order or operating fleet record for the same exact CPO SKU/customer | Same customer plus OEM/platform release, service/RMA case or operator presentation | Repeat shipment / field service | Vendor “in production”; factory capacity; a one-time demo |
| Broadcom TH6 acceptance | Named customer or integrator identifies BCM78919/TH6-Davisson in a delivered/qualified configuration, with date and systems/ports | Customer, HPE, Celestica, Micas or Nexthop production release; qualified system BOM | Customer and acceptance | Tomahawk 6 family; 1.6T platform; copper/optical option; historical TH5 |
| Broadcom TH6 repeatability | Second delivery, expansion, recurring production record or bounded field population for the same TH6 configuration | Operator/OEM/integrator field record; warranty/RMA/service record | Repeat shipment / service | Sampling; Limited Release; collaboration quotation |

**Collection protocol:** retain the full original source where readable, create a companion Markdown evidence note for every HTML-only source, capture exact product labels and surrounding context, and complete the [exact-SKU evidence packet](exact-sku-evidence-packet-template.md) for every candidate customer/OEM result. Reconcile every positive result against the SKU-boundary controls in the [SKU customer-search audit](sku-customer-search-audit-2026-08-11.md). Do not count an ambiguous result.

## Priority 1 — product-matched supplier-content map

| Layer | Required evidence | Highest-value source types | Current control |
|---|---|---|---|
| ASIC / SerDes | Exact CPO SKU and responsible platform supplier | Product brief, hardware manual, customer BOM | Product boundary is known for NVIDIA and Broadcom; retained economics are not |
| PIC / optical engine | Named product, function, package boundary and qualified share | Supplier press release naming SKU, customer BOM, design-win/qualification statement, permitted teardown | TSMC is a process route; neither platform has a public complete-engine allocation |
| EIC / driver / TIA | Supplier, die/package boundary and whether integrated with PIC/ASIC | Engineering paper with commercial SKU, OSAT/test route, supplier qualification source | Open for NVIDIA and Broadcom |
| Laser / ELSFP | Supplier, engine/laser count, external-light topology, source-sharing and warranty boundary | ELSFP qualification, external-laser product record tied to SKU, supplier/customer service record | Candidate laser suppliers are not qualified-share evidence |
| Fibre attach / connector | Assembly owner, interface, yield/loss distribution, rework and service boundary | Connector/attach supplier qualification record, process-lot paper, system service procedure | NVIDIA has process language; Corning has TH6 collaboration—not content allocation |
| Package / test | OSAT/test owner, insertion points, coverage, test time, rework and acceptance yield | Contract-manufacturing disclosure, customer quality record, packaging/test engineering source | SPIL is named for NVIDIA package/test; final-engine metrics remain open |

**Acceptance test:** a source must say *who does what for which exact product*. An ecosystem list, trade-show demonstration, MOU or technology compatibility source moves no allocation gate.

## Priority 2 — production manufacturing and service economics

| Missing input | Minimum usable boundary | Best respondent / source | Model treatment until obtained |
|---|---|---|---|
| Yield waterfall | Known-good die → attach → package → test → final accepted engine, with numerator/denominator and rework | OSAT, engine supplier, fibre-attach/test engineer | Blank / blocked |
| Attach and test throughput | Automation boundary, cycle time, test coverage, false-fail/escape and rework recovery | OSAT, equipment provider, assembly engineer | Blank / blocked |
| Reliability / service | Environment, population, wall-clock period, failure definition, MTTR, replacement scope and warranty owner | Operator, OEM support, qualification report | Blank / blocked |
| External-light economics | Lasers per engine/system, delivered-power tree, redundancy, replacement cycle, source share and warranty | Laser/ELSFP supplier, platform owner, operator | Blank / blocked |
| Complete-engine economics | Content, ASP, price-down, product gross margin, capacity utilisation, capex and cancellation terms | Supplier financial disclosure, permitted interview, attributable contract record | Blank / blocked |

Use the existing [interview question bank](interview-question-bank.md) for a lawful, anonymised primary-research route. Record direct observation, estimate, non-response and confidentiality separately; no interview estimate becomes a public fact.

## Priority 3 — alternatives and architecture substitution

| Comparison needed | Matched boundary requirement | Result that changes a decision |
|---|---|---|
| Retimed pluggable versus CPO | Same port count/rate, traffic load, reach, FEC, cooling and service/spares boundary | Measured system power and replacement burden that can test whether CPO’s claimed power advantage survives the full system |
| LPO/NPO versus CPO | Same electrical reach/channel-loss budget, qualification condition, repair boundary and topology | Evidence that a lower-integration alternative meets the required margin or fails on it |
| 400G/lane route | Same lane-rate, modulation, BER/FEC, temperature, reach, power and package boundary | A measured rather than roadmap-only trigger for CPO/NPO migration |

Component pJ/bit, a vendor power assertion or an unbounded lab link never substitutes for this system-level comparison. See the [architecture scorecard](../02-architecture/system-boundary-comparison-scorecard.md).

## Event watchlist

| Event / source | Current status | Next action | Can it move |
|---|---|---|---|
| Foxconn FY26 Q2 conference | Event listed; no FY26 Q2 deck or transcript was attached at the conference index. A third same-day check of Foxconn's quarterly-earnings and financial-reports routes returned a bot challenge rather than readable results materials. | Recheck only after official materials are attached; a normal browser session may be required. Apply the [Q2 checklist](foxconn-q2-cpo-verification-checklist-2026-08-12.md). Do not infer a result from an event listing or inaccessible route. | Generic actual manufacturing milestone at most; no NVIDIA/Broadcom allocation without exact product link |
| Lumentum FY26 Q4 results | SEC-filed release identifies an initial ELS-module order and demand for ultra-high-power CPO lasers; no customer/product/quantity/economics are disclosed | Recheck presentation/transcript and future filing for an order-to-product/customer conversion record; see `FIL-014` / `CLM-531` | External-light commercial route advanced; CPO economics remain blocked |
| Coherent FY26 Q4 results | Coherent's official financial-release index continues to expose the 12 August 4:30 p.m. ET webcast while its published “Press Release” endpoint resolves to the 22 July scheduling announcement. The live SEC company-submissions feed also contained no filing dated 1–12 August 2026 at the retrieval time. | Recheck the official release, presentation, transcript and SEC filing after posting; do not treat the scheduled webcast as an outcome. Do not treat absence of a filing at one retrieval time as an outcome. | Capacity, customer route or CPO product/order boundary—but consolidated margin remains ineligible absent allocation |
| NVIDIA / OEM customer materials | No exact customer-SKU numerator located in 12 August refresh | SKU-first search of customer/OEM domains only | NVIDIA commercial proof |
| Broadcom partner/customer materials | No TH6 customer numerator located in 12 August refresh | Search exact BCM78919/TH6 terms across named partner/customer channels only | Broadcom commercial proof |

### 12 August exact-label retrieval note

The direct customer/OEM refresh searched CoreWeave, Lambda, Microsoft, Oracle,
Dell and Broadcom channels for `SN6800-LD`, `SN6810-LD`, `BCM78919` and
`TH6-Davisson` with deployment, units, production and repeat-shipment terms.
It returned Dell product/orderability material, CoreWeave Spectrum-X platform
benchmark material, Lambda Quantum-X/InfiniBand hardware material and
Broadcom's Limited Release catalogue. None names an accepted exact CPO SKU
with a dated units/ports denominator and repeat event. This is a documented
negative retrieval result, not proof that non-public deployments do not exist;
no duplicate source or claim was added.

## Update discipline

For a source that passes a boundary:

1. save the complete readable source or its permitted PDF and a canonical URL note;
2. add a source-log row with what it proves and does **not** prove;
3. add a claim-ledger item with claim type, date, evidence boundary and falsification condition;
4. update only the affected dossier, content map, economic gate or alternative scorecard;
5. run python3 scripts/validate-private-research.py; and
6. do not publish, commit or push until Nur Alpys explicitly requests it.

If a source does not pass a boundary, record it only in the relevant retrieval log when it prevents a likely false positive. Avoid expanding the claim ledger with generic CPO material.
