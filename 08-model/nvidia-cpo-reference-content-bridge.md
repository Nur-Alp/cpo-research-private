# NVIDIA CPO reference-content bridge

**Status:** Company-architecture denominator; not a shipment or revenue forecast  
**Owner:** Nur Alpys  
**Scope:** NVIDIA Quantum-X InfiniBand Photonics and Spectrum-X Ethernet Photonics  
**As of:** 2026-08-08

## Purpose

NVIDIA's technical material provides unusually specific reference counts for engines, subassemblies, lanes and external-laser modules. This bridge turns those disclosures into auditable architecture denominators while keeping three things separate:

1. a reference product configuration;
2. a customer-deployed system claim; and
3. a supplier revenue/profit attribution.

Only the first is populated from the current public record. The other two remain evidence gates.

## Quantum-X InfiniBand Photonics reference configuration

| Level | NVIDIA-stated content | Derived denominator | Evidence boundary |
|---|---|---:|---|
| One optical engine | 8 Tx + 8 Rx 200G PAM4 lanes; 2 laser-input fibres; 1.6 Tb/s Tx + 1.6 Tb/s Rx | 16 bidirectional 200G lanes; 3.2 Tb/s full-duplex | Company technical claim; no engine ASP, supplier, yield or production lot [CLM-233] |
| One optical subassembly | 3 COUPE-based optical engines | 4.8 Tb/s Tx + 4.8 Tb/s Rx | Company reference architecture [CLM-233] |
| One Quantum-X ASIC | 6 optical subassemblies | 18 engines; 28.8 Tb/s full-duplex | Company reference architecture [CLM-234] |
| Q3450-LD system | 4 Quantum-X ASICs; 144 ports at 800 Gb/s | 24 subassemblies; 72 engines; 115.2 Tb/s full-duplex | Company product boundary; not a customer-unit count [CLM-234] |

### Quantum-X external-light boundary

NVIDIA says one ELS contains eight lasers and can power 32 of the Quantum-X switch's 576 transmit lanes.[CLM-237] The public record does not provide enough information to derive a complete Q3450 ELS-module count without making an unstated mapping between the reference lane count and the system configuration. Do not infer that count from the Spectrum-X 16/64 ELS-module statement.

NVIDIA's May 2026 production release states that Spectrum-X Ethernet Photonics is a 200Gb/s-SerDes CPO switch now in production and names CoreWeave, Lambda and OCI among early ecosystem partners/adopters. This upgrades the timing evidence for the Spectrum-X reference architecture, but it does not establish that every named partner uses the 32-engine/16-ELS reference boundary or reveal supplier content, units or margin.[CLM-346]

Lambda's customer announcement says a production-scale GB300 supercluster with more than 10,000 GPUs uses Quantum-X Photonics CPO, but it does not disclose switch count, engine count or ELS count.[CLM-224] Therefore:

```text
Quantum-X reference denominator ≠ Lambda shipped-unit denominator
```

## Spectrum-X Ethernet Photonics reference configuration

| Level | NVIDIA-stated content | Derived denominator | Evidence boundary |
|---|---|---:|---|
| One optical engine | 16 Tx + 16 Rx 200G lanes | 3.2 Tb/s full-duplex | Company technical claim [CLM-235] |
| One Spectrum-X package | 32 silicon-photonics engines | 512 x 200G electrical lanes; 102.4 Tb/s aggregate lane rate | Company reference package; not automatically the CoreWeave SN6600-LD BOM [CLM-235] |
| Single-ASIC ELS boundary | 16 ELS modules; 8 lasers per ELS | 128 laser sources per reference package | Company technical claim; laser supplier and lifetime unknown [CLM-237] |
| Quad-ASIC ELS boundary | 64 ELS modules; 8 lasers per ELS | 512 laser sources per reference package | Company technical claim; does not establish a shipped quad-ASIC system [CLM-237] |

CoreWeave independently claims deployment of the 102.4T SN6600-LD with 64 x 1.6T ports and 200G SerDes.[CLM-221; CLM-223] That customer record confirms a named system boundary, but it does **not** establish that the deployed SN6600-LD uses NVIDIA's 32-engine Spectrum-X reference package, the 16-ELS single-ASIC boundary, or any particular supplier. Those relationships require a product BOM or customer qualification record.

## Supplier and profit-pool bridge

The architecture denominator can be connected to a supplier model only after these fields are filled:

| Required field | Current state | Why it matters |
|---|---|---|
| Exact customer SKU and configuration | CoreWeave names SN6600-LD; Lambda names GB300/Quantum-X production-scale cluster; exact optical BOM missing | Prevents applying a reference count to the wrong product |
| PIC/EIC/COUPE supplier | TSMC is named as a COUPE collaborator; transfer boundary is unknown | Determines wafer, bonded-die, engine or process revenue |
| Laser/ELS supplier | NVIDIA names an ELS architecture; Coherent/Lumentum are candidate ecosystem suppliers | Determines laser/ELS content, serviceability and supplier share |
| Fibre attach / connector / package supplier | NVIDIA describes detachable connector and wafer-level microlens mechanisms; partner list is not a BOM | Determines attach yield, rework, test and package economics |
| Qualified share and ASP | Not disclosed | Converts architecture counts into supplier revenue |
| Final-engine yield and warranty | Not disclosed | Converts theoretical content into gross profit |

The only permitted bridge at this stage is a symbolic identity:

```text
supplier revenue
= confirmed customer systems
× engines or ELS modules per confirmed SKU
× supplier content per unit
× qualified supplier share
```

No numeric term may be inserted from a company-wide margin, a strategic investment, a partner logo or a vendor roadmap.

## Decision use

- Use the Quantum-X table for inter-rack scale-up CPO content diligence.
- Use the Spectrum-X table for switch-side Ethernet CPO content diligence.
- Do not combine either table with Broadcom's TH6 sixteen-engine architecture; the platforms have different denominators and packaging boundaries.[CLM-076]
- Do not assign NVIDIA's reference counts to Coherent, Lumentum or TSMC without a supplier-linked shipment or qualification record.[CLM-197; CLM-198; CLM-229]

## Linked controls

- [CPO content-attribution map](cpo-content-attribution-map.md)
- [Optical-engine yield waterfall](engine-yield-waterfall-template.md)
- [Optical-engine profit-pool input gates](optical-engine-profit-pool-input-gates.md)
- [Adoption timeline](adoption-timeline.md)
- [Claim ledger](../01-sources/claim-ledger.csv)

## Primary source

NVIDIA, [*How Industry Collaboration Fosters NVIDIA Co-Packaged Optics*](../01-sources/product-materials/CMP-027-nvidia-cpo-industry-collaboration.html), 26 August 2025, `CMP-027`; canonical original: <https://developer.nvidia.com/blog/how-industry-collaboration-fosters-nvidia-co-packaged-optics/>.
