# Supplier-map completeness audit — NVIDIA and Broadcom exact CPO routes

**Status:** Private control document; not for the public report, supplier ranking, or revenue model  
**As of:** 2026-08-12  
**Scope:** NVIDIA Spectrum-X Ethernet Photonics `SN6800-LD`/`SN6810-LD` and Broadcom `BCM78919` / TH6-Davisson

## Purpose

This audit tests whether the supplier-content map covers every layer needed to
move from an announced CPO architecture to a commercial and economic claim. It
is deliberately stricter than a partner list. A source can establish a
technology route or manufacturing responsibility without establishing a
product-matched bill of materials, qualified supplier share, or profit pool.

## Classification legend

- **Exact product owner:** the source names ownership of the exact platform or
  ASIC/SKU.
- **Product-linked route:** a process, collaboration, validation or assembly
  role is tied to the product, but the sellable content boundary or share is not
  disclosed.
- **Family/technology route:** the company has a relevant capability or a
  broader platform/family relationship, but the exact SKU is not named.
- **Candidate:** the capability is commercially plausible and worth diligence,
  but no retained product-matched role is available.
- **Open:** no retained evidence supports an attribution at that layer.

No classification above unlocks ASP, margin, yield, warranty, or supplier-share
inputs. Those require a product-matched commercial or production record.

## Required layer coverage

| Required layer | NVIDIA `SN6800-LD`/`SN6810-LD` | Broadcom `BCM78919`/TH6-Davisson | Completeness verdict |
|---|---|---|---|
| ASIC / SerDes | Spectrum-6 / SN6800/SN6810 product owner | BCM78919 / Condor SerDes product owner | **Covered — exact owner** |
| PIC / optical engine | TSMC silicon-photonics/COUPE process route; complete engine supplier open | TSMC COUPE-based engine route; complete engine supplier open | **Covered — route only** |
| EIC / driver / TIA | No retained supplier allocation | No retained supplier allocation | **Covered — explicitly open** |
| Laser / external light | TFC laser-die packaging/validation route; Lumentum family-level role; source and commercial share open | Replaceable ELSFP boundary; qualified supplier and source open | **Covered — route/interface only** |
| Fibre attach | NVIDIA late-stage attach/screening process; owner, attempts and yield open | Corning faceplate-to-chip collaboration; attach scope and economics open | **Covered — process/collaboration only** |
| Connector / faceplate | SENKO detachable connector family role; exact supplied assembly open | Corning TH6 connectivity collaboration; supplied assembly/share open | **Covered — family or collaboration route** |
| Package / assembly | SPIL package/assembly/test and Foxconn system assembly routes | No exact TH6 OSAT/package owner retained | **Covered — NVIDIA route; Broadcom open** |
| Test / qualification | Pre-shipment validation and SPIL test route; coverage and acceptance distribution open | No exact TH6 test owner, lot acceptance, or qualification distribution | **Covered — NVIDIA process; Broadcom open** |
| System integration | Foxconn system-assembly route | ODM/partner routes (Celestica, Micas, HPE, Nexthop) without exact allocation | **Covered — route, not allocation** |
| Customer / accepted units / repeat | Platform/adopter records do not identify exact target-SKU acceptance, units, or repeat shipment | Early-access, partner-demo, and family-production records do not identify BCM78919 accepted volume | **Covered — decisive gate open** |
| Field service / warranty | Dell policy and detachable boundaries; no observed fleet or return data | ELSFP replaceability; no TH6 field or warranty record | **Covered — policy/interface only** |
| Supplier economics | ASP, qualified share, yield, rework, warranty, capex, and margin open | Same fields open | **Covered — blocked** |

## Corrections and non-overclaims

1. NVIDIA's TSMC, SPIL, TFC, and Foxconn references describe a disclosed
   production responsibility map. They do **not** prove a complete optical
   engine BOM, transfer price, customer allocation, or supplier margin for
   `SN6800-LD`/`SN6810-LD`.
2. Lumentum's laser statements and SENKO's detachable-connector statements are
   ecosystem or family-level evidence unless a retained source names the exact
   NVIDIA SKU and commercial boundary. They must not be used as exact-SKU
   supplier share.
3. Broadcom's Corning TH6 collaboration is a product-linked connectivity route,
   not proof that Corning supplies the complete faceplate, attach process,
   package, or economic content.
4. TSMC COUPE demonstrations and engineering-sample yield are technology or
   process evidence. They are not qualified TH6 or Spectrum-X engine yield,
   sellable-unit volume, or supplier economics.
5. Broadcom OCP demos and Celestica's unnamed hyperscaler award are diligence
   leads. They do not establish BCM78919 customer acceptance or repeat shipment.
6. Historical TH5 qualification/reliability evidence cannot be transferred to
   TH6 field performance without an explicit product-matched record.

## Missing records that keep the commercial thesis gated

The following fields remain missing for both exact-SKU routes:

- named customer acceptance tied to the exact SKU and configuration;
- accepted units or ports and a repeat-shipment/expansion event;
- product-matched PIC/engine, EIC, laser, attach, package, connector and test
  responsibility;
- qualified-good-engine denominator, first-pass yield, rework and escape rate;
- supplier share, ASP, price-down, warranty reserve, capex burden and product
  gross margin; and
- field-service procedure, failure-domain data, return rate and replacement
  economics.

Until these records are found, the private model may retain labelled scenario
ranges, but it must not rank NVIDIA, Broadcom, TSMC, Coherent, Lumentum,
Marvell, Corning, SPIL, TFC, Foxconn or SENKO as the proven CPO profit-pool
leader.

## Gate to promote a supplier role

Promotion from route/candidate to exact-SKU attribution requires one retained
record that names all of the following:

1. exact product and configuration;
2. physical responsibility boundary;
3. qualification or shipment status at that boundary; and
4. a product-matched output or economic boundary (share, price, yield, cost,
   warranty, or accepted-unit denominator).

An ecosystem list, MOU, capacity agreement, partner demonstration, adjacent
product, or broad family statement is insufficient.

## Linked controls

- [Exact-SKU attribution completeness](exact-sku-attribution-completeness-2026-08-12.md)
- [Supplier-attribution audit](supplier-attribution-audit-2026-08-12.md)
- [Switch-CPO SKU reconciliation](switch-cpo-sku-content-reconciliation.md)
- [NVIDIA commercial-proof dossier](../07-companies/commercial-proof-dossiers/nvidia-spectrum-x-photonics.md)
- [Broadcom commercial-proof dossier](../07-companies/commercial-proof-dossiers/broadcom-th6-davisson.md)
- [Profit-pool arithmetic audit](profit-pool-arithmetic-audit-2026-08-12.md)

**Current decision:** supplier-map coverage is complete as a control framework,
but exact-SKU attribution and economics remain incomplete. The commercial
proof dossier therefore remains private and not release-ready.
