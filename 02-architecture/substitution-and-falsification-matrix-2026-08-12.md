# Architecture substitution and falsification matrix

**Status:** Private decision control; not an adoption forecast
**As of:** 2026-08-12
**Scope:** Same-domain Ethernet scale-out comparison of retimed pluggables, LPO/RTLR, NPO/OBO and switch-side CPO

## Purpose

This matrix tests whether CPO is actually necessary at a given lane rate and
topology. It prevents a component power claim or a CPO product announcement
from being treated as proof that alternatives have lost.

## Common boundary required for every comparison

Hold constant: ASIC generation, port count, lane rate, reach, fibre/cable type,
pre-FEC BER/FEC mode, host loss and return loss, temperature, cooling boundary,
installation labour, spares, repair policy and failure-domain accounting. If a
field is not matched, the result is a scenario or mechanism—not a route winner.

## Substitution matrix

| Route | What it must beat | Evidence that would make it win | Evidence currently available | What would falsify the CPO timing thesis | Current read |
|---|---|---|---|---|---|
| Retimed pluggable | Higher module/retimer power and faceplate density | Matched 200G/400G system meets BER/FEC/reach with lower cost per restored port, repeatable yield and materially simpler service | RTLR/retimed standards boundary and established hot-plug/service model; no matched 200G/400G economics | A qualified retimed system closes the electrical gap while preserving modular replacement and lower lifecycle cost | Strong serviceability benchmark; not yet a measured 200G/400G winner |
| LPO / RTLR | Host electrical margin and receive-side DSP/retimer burden | Measured end-to-end link at target lane rate with acceptable BER/FEC, thermal load, module yield, field diagnostics and lower total cost | 100G system evidence and 200G/400G models; RTLR provides a defined modular boundary | A 200G or 400G LPO/RTLR product reaches repeat production with matched margin and service economics | Live countercase; higher-rate proof open |
| NPO / OBO | Interoperability and serviceability of pluggables, plus CPO integration risk | Qualified short-channel optical module remains replaceable, interoperable and materially cheaper/easier to repair than fixed CPO | Product announcements and roadmap/sample signals; no public qualified customer fleet | A qualified NPO/OBO module closes the channel/power gap without CPO’s package/failure-domain burden | Plausible CPO-deferral route; production proof open |
| Switch-side CPO | Integration, package, yield and service burden | Exact-SKU customer acceptance, repeat shipments, final-engine yield, field-service data and positive matched TCO versus alternatives | Defined NVIDIA/Broadcom products, vendor production/early-access language, partial process routes; no exact customer numerator | Continued evaluation-only status, poor service/yield, or an alternative clearing the same system boundary at lower lifecycle cost | Strongest 200G timing signal, but commercial/economic gates open |

## Decision tree by lane rate

| Domain | CPO can be preferred only if… | Alternative can remain preferred if… | Current evidence state |
|---|---|---|---|
| 100G Ethernet scale-out | power density or host reach creates a measured system constraint that modular optics cannot solve economically | LPO/advanced pluggables meet power, BER and service requirements | 100G LPO and historical CPO evidence are stronger than higher-rate records; no universal winner |
| 200G Ethernet scale-out | exact topology fails matched RTLR/LPO/NPO electrical or power gates, and CPO clears yield/service/TCO gates | RTLR/LPO retains margin and modular replacement at acceptable total cost | Coexistence zone; CPO timing signal is stronger than proof of adoption |
| 400G Ethernet scale-out | package/host electrical loss and power bind, while CPO/NPO achieve qualified production and serviceability | a measured 212.5-GBd alternative closes the channel and cost gap | Component/model evidence only; no production architecture winner |

## Falsification checklist

Downgrade the current view—switch-side 200G CPO has the strongest commercial
timing signal—if, at the same product boundary:

1. An exact-SKU customer deployment is shown to use pluggable optics rather than CPO.
2. A qualified RTLR/LPO/NPO system achieves the same port count, reach, BER/FEC and cooling boundary with lower lifecycle cost.
3. CPO final-engine yield, rework or warranty makes cost per accepted/restored port worse than the modular alternative.
4. CPO service requires board/chassis replacement while the alternative is a field-replaceable module with materially lower outage and spare burden.
5. Customer qualification remains evaluation-only while an alternative enters repeat production at the target lane rate.

Upgrade only when exact-SKU customer, acceptance, repeatability, service and
economic gates clear together. Production language, sampling, Contact Sales,
platform benchmarks and component pJ/bit claims cannot satisfy this condition.

## Evidence priority

1. Same-ASIC/port-count 200G system report with channel loss, BER/FEC,
   temperature, inlet power and cooling boundary.
2. Exact-SKU customer acceptance and repeat shipment for CPO or an alternative.
3. Final-engine/module yield, test time, rework and qualification population.
4. Field-service MTTR, spare ratio, warranty and failure-domain data.
5. Product-linked ASP, supplier share, price-down and margin evidence.

Until these records exist, the proper output is **conditional coexistence**,
not a universal CPO winner or annual adoption-share forecast.

Related controls: [common system-boundary scorecard](system-boundary-comparison-scorecard.md), [architecture trigger matrix](architecture-trigger-matrix.md), [adoption timeline](../08-model/adoption-timeline.md), and [commercial-proof decision memo](../07-companies/commercial-proof-dossiers/commercial-proof-decision-memo.md).
