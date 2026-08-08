# Architecture trigger matrix: when optics move inward

**Status:** Evidence-gated architecture decision tool; not an adoption forecast  
**As of:** 2026-08-08  
**Scope:** 100G, 200G and 400G per lane across scale-out Ethernet and accelerator fabrics

## Decision rule

No lane rate alone makes CPO inevitable. The architecture trigger is the first point at which a candidate meets the same link, service and cost requirements as its alternatives. A trigger is therefore a **conditional boundary**, not a market-share claim.

## Trigger matrix

| Lane/domain | Retimed/advanced pluggable | LPO | NPO/OBO | Switch-side CPO | Current evidence-adjusted trigger |
|---|---|---|---|---|---|
| **100G Ethernet scale-out** | Strong serviceability/interoperability route; RTLR-style boundaries and mature pluggable ecosystem | Direct 51.2T system evidence, but non-uniform BER outcomes across preliminary designs | Usually unnecessary unless host electrical reach is unusually constrained | Technically possible but integration benefit is less binding | LPO/pluggables remain credible; CPO must earn adoption through power density, attach rate or service economics, not lane rate alone [PAP-007; CLM-297–CLM-300] |
| **200G Ethernet scale-out, short host channel** | Retimed pluggables preserve margin and replaceability | Conditional; models span roughly 22–31 dB under non-matched assumptions | Plausible if the module can shorten the channel while preserving replaceability | Plausible where optical attach rate, power and stability dominate | Coexistence zone; require matched channel, return-loss, FEC, power and service data before declaring CPO necessary [PAP-007; PAP-008; PAP-010] |
| **200G Ethernet scale-out, long/high-loss channel** | Retiming may be required | Meta's modeled ~30 dB cabled path required a Tx retimer | Shorter NPO/CPO boundary becomes more attractive | CPO can be favored if package/service gates close | Electrical loss is the trigger, not aggregate switch capacity; compare RTLR versus NPO/CPO on delivered cost [CLM-057; CLM-297–CLM-300] |
| **400G Ethernet scale-out** | Retimed route remains possible but power/interface cost is unresolved | Current end-to-end evidence is modeled only; 212.5 GBd margin fails above 12 dB B2B in the reviewed model. Tower/Coherent add a 420 Gb/s PAM4 silicon-MZM open-eye demonstration in a stated production-ready SiPho process, but no complete 400G/lane link boundary [CMP-045; CLM-367–CLM-369] | Stronger current technical direction if a replaceable short module is qualified | Stronger direction where package density and channel loss bind | CPO/NPO remain technically favored hypotheses only where the measured electrical/thermal/service boundary binds; CMP-045 strengthens the silicon/pluggable countercase, so require measured 212.5-GBd link, full power/loss and final-package data [PAP-011; STD-009; CMP-045] |
| **Accelerator/inter-rack scale-up** | Copper/AEC and pluggables may preserve serviceability at shorter reaches | LPO is topology-dependent and not the same as switch-side Ethernet | Optical chiplets/NPO can change XPU world-size and package boundary | Quantum-X/other CPO routes have strategic world-size rationale | Compare optical endpoints, collective-communication benefit, thermal/package yield and replacement cost; do not import switch-CPO thresholds [CLM-177; CLM-178; CLM-224; CLM-354] |

## Gate hierarchy

1. **Electrical gate:** measured channel loss, return loss, crosstalk, FEC/BER and temperature at the exact lane rate.
2. **System gate:** complete power/cooling, reach, port count, workload utilisation and failure-domain boundary.
3. **Manufacturing gate:** final-engine/package yield, attach cycle time, test escape, rework and qualification.
4. **Service gate:** replacement procedure, MTTR, spares, warranty allocation and field failure rate.
5. **Economic gate:** module/engine ASP, supplier share, price-down, capex, cannibalisation and cost per delivered bit.

Failure at an earlier gate cannot be repaired by a favorable later-stage assumption. For example, a modeled 400G electrical margin does not clear manufacturing or serviceability gates, and a production claim does not clear supplier economics.

## Current decision read

- **100G:** LPO and advanced pluggables have the strongest direct system evidence.
- **200G:** coexistence is the base technical view; CPO becomes favored only after a matched channel/service/TCO result.
- **400G:** NPO/CPO are the stronger technical hypotheses because the reviewed conventional-LPO evidence is modeled and loss-sensitive, but no production winner is established.
- **Accelerator scale-up:** evaluate world-size and topology value separately; CPO may create strategic value even when switch-side Ethernet CPO is only a power/service trade.

## Evidence still needed to turn triggers into adoption probabilities

- One measured multi-vendor 200G/lane system with complete electrical and optical boundaries.
- One measured 212.5 GBd/400G/lane end-to-end system, not a component or model result.
- Matched NPO/CPO/pluggable TCO including yield, repair, cooling, spares and capex.
- Customer-qualified production units and repeat deployment for each domain.

## References

- [102.4T CPO versus advanced pluggables](102.4t-cpo-vs-advanced-pluggables.md).
- [Linear-drive optics boundary benchmark](linear-drive-boundary-benchmark.md).
- [NPO interoperability and serviceability boundary](npo-interoperability-boundary.md).
- [Accelerator optical-I/O and NPO comparator](../07-companies/accelerator-optical-io-comparator-dossier.md).
- `PAP-007`, `PAP-008`, `PAP-010`, `PAP-011`, `STD-009`, `STD-012`; see the source log and claim ledger.
