# CPO Network-Topology Value Boundary

**Status:** Mechanism review; not a CPO demand forecast or product comparison
**Last updated:** 2026-08-07

## Question

Can CPO create value through a higher-radix, more-local network topology even if its direct optical-power advantage over LPO is modest?

## Evidence-led answer

**Yes, as a modeled mechanism; no, not yet as a demonstrated commercial outcome.** IBM researchers model higher-radix networks enabled by CPO and find that switch count, locality and simulated collective-workload throughput can improve materially under stated architectures and traffic patterns.[CLM-089][CLM-090]

This matters because the current 102.4T switch power scenario has only a narrow central CPO-versus-LPO advantage. If a customer can use CPO to raise radix, reduce topology layers or keep more communicating accelerators under one leaf, the economic case could be stronger than the optical module power comparison alone. Conversely, the model does not show that the customer can buy, manufacture, qualify, service or operate that CPO configuration more economically.

## What the paper actually models

| Modeled case | CPO placement | Reported result | Boundary |
|---|---|---|---|
| AI-supercomputer comparison | Both switch and accelerator points | 100T CPO architecture: 48 versus 132 switches (64% fewer); >90% higher mean server throughput at 256 nodes and messages >=128 KiB | Discrete-event simulation with all-to-all/all-reduce traffic. [CLM-089] |
| Data-center locality comparison | Higher-radix CPO switch topology | 160 versus 272 switches (41% fewer); up to 68% higher completion time when an all-to-all application spans switches at 1.25-us stack latency | Modeled fat-tree/topology and latency condition. [CLM-090] |

The first result cannot be credited to switch-side CPO alone because the model co-packages at accelerator points as well. The second is more directly relevant to switch radix, but is still a simulation rather than a customer deployment.

### PAP-020 switch-radix and locality model

IBM's earlier MOTION study provides a more explicit scale-out topology boundary. It compares a baseline 25.6 Tb/s spine / 6.4 Tb/s leaf network with 272 switch ASICs against a modeled 51.2 Tb/s, 128-port, 400 Gb/s CPO-enabled network. Under the paper's 12,288-endpoint, 3:1-oversubscribed configuration, the CPO topology has four times the bisection bandwidth and 41% fewer switches; VM-trace placement puts some applications under up to 50% fewer first-level switches. All-to-all simulations report speedup up to 7.1 in a specific 96-node/16 KiB case and application execution-time reductions up to 26% or 42.7% at stated communication ratios.[CLM-129][CLM-130][CLM-131][CLM-132]

These results are **system simulations**, not production CPO measurements. They demonstrate a plausible customer value mechanism beyond optical power, but the model does not price CPO engines, cooling, service, transition cost, qualification or supplier share. It also assumes a MOTION hardware path whose first generation was 56 Gb/s NRZ and whose second generation was a 112 Gb/s PAM4 target—not a measured 200G/400G-per-lane commercial engine. The correct investment use is a topology/workload diligence gate, not a switch-unit or optical-supplier revenue forecast.

## Investment implication

Topology/locality should be a separate adoption gate, alongside electrical channel loss and total cost:

```text
Customer CPO benefit
= optical / electrical power effect
+ topology and locality benefit
+ density / cooling benefit
- serviceability, supply-chain and qualification cost
- any loss of modularity or pluggable optionality
```

A customer case becomes investable only after this is evaluated for a defined topology and workload. Do not use a generic “CPO enables 64% fewer switches” statistic in a company revenue forecast.

## Evidence needed to upgrade the conclusion

1. A customer-side topology choice that identifies CPO as the enabling constraint.
2. Measured application/network performance at matched hardware, workload and availability targets.
3. All-in network capital, optical, energy, cooling, spares and service cost.
4. Evidence that advanced pluggables, NPO or optical I/O cannot achieve the same topology benefit.
5. A bill of materials showing which supplier captures the added topology value.

## References

- Pavlos Maniotis and Daniel M. Kuchta, [*Exploring the benefits of using co-packaged optics in data center and AI supercomputer networks: a simulation-based analysis*](../01-sources/papers/PAP-006-maniotis-cpo-network-benefits-2024.pdf), *Journal of Optical Communications and Networking* 16(2), 2024, DOI 10.1364/JOCN.501427.
- [102.4T Switch-Side CPO Versus Advanced Pluggables](102.4t-cpo-vs-advanced-pluggables.md).
- [102.4T Switch-Side Power Model](../08-model/102.4t-switch-side-power-model.md).
- [Claim ledger](../01-sources/claim-ledger.csv), CLM-089 and CLM-090.
- `PAP-020`: Pavlos Maniotis et al., [*Toward higher-radix switches with co-packaged optics for improved network locality in data center and HPC networks*](../01-sources/papers/PAP-020-maniotis-higher-radix-cpo-2022.pdf), *Journal of Optical Communications and Networking* 14(6), 2022, DOI `10.1364/JOCN.451449`; see `CLM-129` through `CLM-133`.
