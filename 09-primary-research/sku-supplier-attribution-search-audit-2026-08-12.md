# SKU-bound supplier-attribution search audit — 12 August 2026

**Status:** Private retrieval log. This is a documented no-change result, not evidence that undisclosed supply relationships do not exist.  
**Question:** Do public primary sources assign a physical supplier role to an exact NVIDIA `SN6810`/`SN6800` or Broadcom TH6-Davisson/`BCM78919` product boundary?

## Acceptance standard

An attribution can move only if a record identifies **who does what for which exact SKU**. A generic CPO capability, ecosystem list, corporate relationship, trade-show display, technical roadmap or partner quotation remains a route/candidate signal. It cannot be converted into qualified content share, revenue, ASP, yield or margin.

## Targeted retrieval results

| Search route | Product/layer tested | Result | Permitted conclusion |
|---|---|---|---|
| TSMC official routes | `SN6810` / `SN6800`, `BCM78919` / TH6-Davisson; PIC/EIC/COUPE/package | TSMC results describe COUPE/CPO roadmap, system integration capability and generic advanced packaging, but no record names either exact switch SKU or allocates wafer, die, engine, package, test or economics. | Retain TSMC as a process/control route only. No completed-engine or economic attribution. |
| SPIL and TFC/TFCI routes | `SN6810` / `SN6800`; package/test and laser-module roles | No accessible manufacturer-authored SKU-bound responsibility statement was located. The existing NVIDIA record remains the only retained map: SPIL assembly/test and TFC laser-die-module packaging/validation. | Preserve the NVIDIA platform-owner role map; do not convert it into supplier share, accepted yield, warranty or margin. |
| Broadcom product and investor routes | `BCM78919`; engines, PIC/EIC, ELSFP, package/test | Broadcom repeats the architecture: 16 engines, 512 fibres, ELSFP interface and TSMC COUPE-based technology. The catalogue remains Limited Release. No product-level BOM or package/test ownership appears. | Architecture and service-boundary evidence only; EIC, laser supplier, OSAT, test, share and economics remain open. |
| Corning / TH6 collaboration | `TH6-Davisson`; faceplate-to-chip / fibre attach | The retained Broadcom release remains the primary direct statement: Corning is collaborating on complete faceplate-to-chip optical assemblies for TH6-Davisson systems. No supplied component scope, qualified share, commercial terms, yield, loss distribution, warranty or customer programme is disclosed. | Keep **route-specific collaboration**. Do not label Corning a confirmed production content supplier or assign it economics. |
| Coherent strategic/capacity routes | NVIDIA, CPO engines, lasers and InP capacity | Coherent’s NVIDIA agreement covers non-exclusive advanced laser/networking capacity and future access to multiple product families. Its CPO demonstrations and proposed InP-facility expansion establish technical/capacity routes, not a named `SN6810`/`SN6800` or TH6 content allocation. | Keep Coherent as a component/engine candidate. Financing, capacity or a demonstration does not identify CPO revenue, complete-engine share, qualified output, price or margin. |
| Lumentum order routes | CPO laser / ELSFP content | Lumentum’s disclosed CPO order and later ELS-module order signal commercial interest, but neither supplies the customer, exact switch SKU, quantity, laser count, allocation, supplier share, realised price, yield or margin. | Keep an external-light/order-conversion watch case only. Do not attach the order to NVIDIA or Broadcom or use it as an engine-economic input. |

## Result

The public record continues to support a **platform/process responsibility map**, not a product-matched bill of materials. The unresolved layers are material:

1. NVIDIA: EIC/driver/TIA ownership; laser-die supplier and ELS topology; fibre-attach supplier/first-pass yield; final package/test economics; and all supplier shares.
2. Broadcom: PIC/EIC ownership and engine supplier; laser/ELSFP qualification; faceplate/attach scope; package/OSAT/test ownership; and all supplier shares.
3. Both: customer-linked accepted-unit denominator, final-engine yield/rework, field replacement/warranty cost, ASP and realised margin.

The Coherent/Lumentum evidence is therefore useful to rank **diligence priority**, not investment exposure: it increases the value of obtaining product-specific conversion records, but leaves the supplier-economics gate open.

The correct modelling treatment remains **blank / blocked**, not a scenario input presented as a fact. See the [SKU content reconciliation](../08-model/switch-cpo-sku-content-reconciliation.md) and [optical-engine profit-pool gates](../08-model/optical-engine-profit-pool-input-gates.md).

The follow-up evidence fields, acceptable record holders and prohibited proxies
are now operationalised in the [supplier-content evidence-packet register](supplier-content-evidence-packet-register-2026-08-13.md).

## Next higher-value records

1. Customer/OEM BOM, qualification record or manufacturing contract tying a named layer to `SN6810`/`SN6800` or `BCM78919`.
2. Supplier filing or earnings material that identifies product/customer, quantity/capacity commitment and scope of work.
3. OSAT/engine supplier evidence with final-engine yield, test/rework and warranty boundary.
4. Product-specific service/RMA or field-replacement procedure linking the replaceable boundary to cost ownership.

No source-log or claim-ledger entry was added: this retrieval did not change a decision gate.

## External primary-source rerun — 12 August 2026

The official-source rerun rechecked TSMC COUPE pages, Lumentum's NVIDIA
Spectrum-X ecosystem announcement, Broadcom's TH6-Davisson release and the
current product pages. The results are consistent with the controlled map:

- TSMC describes COUPE architecture and a 2026 CPO production milestone, but
  does not name `SN6810-LD`, `SN6800-LD` or `BCM78919` as a supplied product,
  nor disclose complete-engine responsibility, output or economics.
- Lumentum explicitly says its high-power lasers are integrated into NVIDIA's
  Spectrum-X and Quantum-X Photonics switches. This is stronger than a generic
  capability statement, but it still does not identify a specific ordering
  label, laser count, qualified share, realised price, yield, warranty or
  margin. It remains a product-family route signal, not an exact-SKU economic
  allocation.
- Broadcom continues to name TSMC COUPE-based optical-engine technology and
  Corning's TH6 faceplate-to-chip collaboration, while leaving EIC, laser,
  attach, package/OSAT, test ownership and commercial shares open.

This rerun adds no new source or claim because the reviewed records are already
retained as `PRI-030`, `CMP-067` and `CMP-018`/`CLM-529`. It does not promote
any layer to exact-SKU confirmed and does not change the profit-pool gate.
