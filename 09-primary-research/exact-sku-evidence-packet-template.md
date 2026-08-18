# Exact-SKU commercial-proof evidence packet

**Status:** Private intake template; do not publish as a source or conclusion  
**Owner:** Nur Alpys  
**Purpose:** Capture a customer/OEM/integrator record without silently converting an ambiguous product, demo, platform or partner announcement into commercial proof.

Use one packet per candidate source bundle. A bundle may contain a customer
statement, OEM record, procurement/qualification document and a second dated
shipment or expansion record, but every item must preserve its own source ID,
date and product boundary.

## 1. Identity and provenance

| Field | Entry |
|---|---|
| Packet ID | `ESP-###` |
| Reviewer |  |
| Review date / evidence cut-off |  |
| Source IDs retained |  |
| Canonical URLs |  |
| Original format | HTML / PDF / filing / customer presentation / other |
| Access limitation |  |
| Primary or secondary |  |
| Company/product domain | NVIDIA Spectrum-X Ethernet / Broadcom TH6 / other |

## 2. Exact product boundary

| Required field | Entry | Evidence citation / page |
|---|---|---|
| Exact SKU and ordering label |  |  |
| CPO, NPO, LPO, retimed or pluggable |  |  |
| ASIC / SerDes and lane rate |  |  |
| Port, engine and fibre configuration |  |  |
| Optical-engine/PIC boundary |  |  |
| Laser / ELSFP boundary |  |  |
| Fibre attach / connector / package boundary |  |  |
| Test, burn-in and qualification boundary |  |  |
| Network position and topology |  |  |

**Boundary rule:** `Spectrum-X`, `Tomahawk 6`, `1.6T`, `AI networking`,
“optical,” a product family, or a platform image is not an exact CPO SKU. For
NVIDIA, keep `SN6800`/`SN6810` and `SN6800-LD`/`SN6810-LD` distinct until a
source joins the names. For Broadcom, require `BCM78919` or explicit
TH6-Davisson CPO wording; a copper/optical-capable Tomahawk platform is not
enough.

## 3. Customer and acceptance evidence

| Required field | Entry | Evidence citation / page |
|---|---|---|
| Named customer/operator |  |  |
| Customer role (operator, OEM, integrator, distributor) |  |  |
| Explicit accepted/deployed/qualified wording |  |  |
| Acceptance or qualification date |  |  |
| Production versus evaluation/sample/demo |  |  |
| Customer-owned or vendor-owned test environment |  |  |
| System/port/unit denominator |  |  |
| Defined measurement period |  |  |
| Service or operating history |  |  |

Do not treat a vendor “first adopter” list, partner quotation, planned demo,
“now shipping,” “Contact Sales,” “Limited Release,” sampling language or a
different CPO domain as customer acceptance.

## 4. Scale and repeatability

| Gate | Entry | Evidence citation / page |
|---|---|---|
| First accepted units/ports/systems |  |  |
| Shipment or installation date |  |  |
| Second dated shipment/expansion/renewal |  |  |
| Repeat units/ports/systems |  |  |
| Same customer and same exact SKU? | Yes / No / unclear |  |
| Repeat period and denominator |  |  |
| Field population or RMA/service record |  |  |

**State transition:**

```text
no exact-SKU evidence -> product/route signal -> exact-SKU customer evidence
  -> accepted-unit denominator -> repeat shipment / expansion
  -> commercial-proof gate cleared
```

The packet cannot advance beyond a product/route signal if the source does not
identify the customer and exact CPO configuration. It cannot clear the gate
without both a denominator and a second dated event.

## 5. Supplier-content and economics (separate gate)

| Layer | Named role | Exact-SKU linkage | Share / ASP / terms | Yield / warranty / margin | Status |
|---|---|---|---|---|---|
| ASIC / SerDes |  |  |  |  | confirmed / route / open |
| PIC / optical engine |  |  |  |  | confirmed / route / open |
| EIC / driver / TIA |  |  |  |  | confirmed / route / open |
| Laser / ELSFP |  |  |  |  | confirmed / route / open |
| Fibre attach / connector |  |  |  |  | confirmed / route / open |
| Package / assembly |  |  |  |  | confirmed / route / open |
| Test / burn-in / qualification |  |  |  |  | confirmed / route / open |

Supplier presence, a partnership, a capacity reservation or a demonstration
does not establish qualified share, transfer price, product margin, yield,
warranty responsibility or profit capture.

## 6. Evidence grade and decision impact

| Field | Entry |
|---|---|
| Evidence grade | A: exact customer + accepted denominator + repeat; B: exact customer/acceptance but no repeat; C: exact product/route only; D: ambiguous/secondary |
| Commercial-proof gate | Open / partial / cleared |
| Supplier-content gate | Open / route-level / exact-SKU role / cleared |
| Economic gate | Blocked / sensitivity-only / partially evidenced / cleared |
| Claim IDs created or updated |  |
| Dossier/registers updated |  |
| What this source changes |  |
| What it does not change |  |
| Falsification condition |  |

## 7. Required negative finding

If the packet fails, record the exact reason rather than discarding it:

- exact SKU absent;
- CPO versus pluggable/NPO/LPO ambiguous;
- customer is named but not tied to the SKU;
- acceptance is evaluation/demo only;
- unit/port denominator absent;
- repeat event absent;
- supplier role is partnership-only;
- economics are consolidated or unallocated; or
- source is inaccessible and cannot be independently verified.

**Disposition:** product/route lead / false-positive control / primary follow-up
request / no decision change.

## 8. Validation before promotion

Before moving a packet into a dossier or public-release manifest:

1. retain the readable original or canonical direct link and access limitation;
2. add a source-log row describing what the record proves and does not prove;
3. add only claims that change a decision gate;
4. reconcile every SKU, lane, port and topology label against the boundary
   controls;
5. update the customer-proof register and affected dossier;
6. run `python3 scripts/validate-private-research.py` and the commercial-proof
   validator; and
7. keep the release gate closed unless the full bundle clears.

See the [commercial-proof dossiers](../07-companies/commercial-proof-dossiers/README.md),
[customer-proof register](../08-model/customer-proof-register.md), and
[decision-changing evidence queue](decision-changing-evidence-acquisition-queue.md).

Completed negative-control examples: [CoreWeave `SN6600-LD`](evidence-packets/ESP-001-coreweave-sn6600-pluggable-negative.md), [Lambda `Q3450-LD`](evidence-packets/ESP-002-lambda-quantum-x-domain-negative.md), and [Broadcom OCP demo](evidence-packets/ESP-003-broadcom-ocp-demo-negative.md).
