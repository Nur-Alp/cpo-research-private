# Commercial-proof release-readiness audit — 12 August 2026

**Scope:** NVIDIA Spectrum-X Ethernet Photonics and Broadcom TH6-Davisson only. The exact-SKU search refresh on 12 August returned no customer-side record that changes a gate.  
**Status:** Private pre-publication audit. **Not release-ready.**  
**Method:** Each platform must independently clear product identity, named customer, dated acceptance, observed scale, repeatability, service/reliability and supplier economics. A platform product announcement, partner relationship or vendor “shipping” phrase cannot substitute for the customer-side fields.

## Gate result

| Required decision field | NVIDIA Spectrum-X Ethernet Photonics | Broadcom TH6-Davisson | Release implication |
|---|---|---|---|
| Exact CPO product | **Pass:** `SN6810` / `SN6800`; Dell's `-LD` CPO ordering families independently corroborate the SKU boundary (`CLM-514`–`CLM-515`, `CLM-519`). | **Pass:** `BCM78919` / TH6-Davisson is a 102.4T 200G/lane CPO product (`CLM-076`, `CLM-516`–`CLM-517`). | Product identity is sufficient for targeted diligence only. |
| Named customer tied to the exact CPO SKU | **Open.** CoreWeave's named system is `SN6600-LD`, which is pluggable, not the CPO SKU (`CLM-380`–`CLM-383`). | **Open.** Early-access customers and collaborators are unnamed or not stated as completed deployments (`CLM-077`, `CLM-246`–`CLM-249`). | Neither platform has a customer-side CPO numerator. |
| Dated acceptance / qualification | **Open.** | **Open.** | Vendor product/production language cannot be treated as acceptance. |
| Observed units, ports or systems | **Open.** | **Open.** | No basis for installed-base, revenue or adoption-share calculation. |
| Repeat shipment / expansion | **Open.** | **Open.** | No basis for commercial repeatability. |
| Field service / reliability | **Open.** Dell policy is a service promise, not observed CPO service performance (`CLM-520`). | **Partially scoped.** Field-replaceable ELSFP establishes a replaceable laser boundary, not field-return/MTTR/warranty evidence (`CLM-076`). | Service economics are not known. |
| Product-linked supplier allocation and economics | **Open.** TSMC, SPIL, TFC and Foxconn are responsibility signals, not a SKU-level commercial allocation. | **Open.** TSMC COUPE and Corning connectivity are technology/collaboration signals, not content share. | No CPO margin, EPS or profit-pool result is eligible. |

## Conclusion

Both companies clear only the **product-definition** gate. NVIDIA adds a first-party production/manufacturing-route narrative and a limited select-partner shipment signal; Broadcom adds an early-access/limited-release merchant-switch route. Neither clears the evidence needed to say that switch-side CPO has a publicly demonstrated volume leader or that any supplier captures the profit pool.

The controlled command below should remain part of every pre-publication review:

```bash
python3 scripts/audit-commercial-proof-readiness.py
```

Expected current output is `"release_ready": false`. Treat a change to that output as a prompt for analyst review, not an automatic upgrade: a new source must still be retained, traced in the claim ledger, reconciled to the exact product boundary and independently checked for forward-looking language.

## Next evidence that can change the result

1. A customer/operator/OEM record that names `SN6810`/`SN6800` (or controlled `-LD` equivalent) or `BCM78919`/TH6-Davisson and says it was deployed or accepted.
2. A dated unit, port, system, capacity or spend denominator tied to that exact configuration.
3. A later expansion, repeat order, sustained delivery or operating/service record.
4. A product-level BOM/contract/qualification source assigning PIC/engine, EIC, laser, fibre attach, package, connector and test content—and the share, ASP, margin, yield/rework and warranty terms necessary for profit capture.
