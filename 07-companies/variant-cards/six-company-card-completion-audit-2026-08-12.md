# Six-company variant-card completion audit — 12 August 2026

**Status:** Private control document; no target prices, publication or CPO earnings call is authorized.  
**Purpose:** Verify that each company card contains the same required fields and that unavailable analyst/CPO inputs are explicitly blocked rather than silently omitted.

## Field standard

Every card must distinguish:

1. reconciled consolidated baseline (fiscal period, currency, accounting basis and as-of date);
2. observed public CPO facts and their product boundary;
3. external expectations (management or analyst material, retained privately where restricted);
4. Nur Alpys’ variant view, confidence and rationale;
5. bear/base/bull CPO sensitivity, with every non-observed input labelled;
6. catalyst, downside risk and falsification trigger; and
7. source IDs, estimate IDs and public-use status.

The standardized downside-risk field is recorded in the core matrix under
[Standardized downside-risk field](core-company-variant-cards.md#standardized-downside-risk-field).
It remains a hypothesis until a dated public source converts it into observed
evidence.

“Pending” means the record must be obtained or reconciled. “Not eligible” means
the field must remain blank because the commercial/economic gate has not cleared.
Neither status is a zero estimate.

## Current field audit

| Company | Consolidated baseline | Observed CPO boundary | External expectation | Variant view/confidence | Bear/base/bull sensitivity | Catalyst / risk / falsification | Source and public-use controls | Card status |
|---|---|---|---|---|---|---|---|---|
| NVIDIA | Pending fiscal-period/share/margin reconciliation for the restricted analyst layer | Defined `SN6810-LD`/`SN6800-LD`; customer numerator and economics open | Public production/adopter language; no cleared CPO estimate | Positive strategic exposure; medium confidence | **Not eligible** until exact-SKU customer, content and economics gates clear | Present; exact-SKU acceptance and repeat shipment are upgrade tests | Public claim IDs retained; restricted analyst inputs remain private | Relative stance complete; earnings layer pending |
| Broadcom | Pending fiscal-period/share/margin reconciliation for the restricted analyst layer | Defined `BCM78919`/TH6-Davisson; Limited Release/early access; customer numerator open | Product announcement and family-level production language; no cleared CPO estimate | Positive enabling exposure; medium confidence | **Not eligible** until TH6 acceptance, repeatability and economics clear | Present; named TH6 customer and repeat shipment are upgrade tests | Public claim IDs retained; analyst material restricted | Relative stance complete; earnings layer pending |
| Coherent | Pending baseline reconciliation and product-family allocation | SiPh/InP/VCSEL and engine routes; no exact customer allocation | Capacity/purchase-access signals; no cleared CPO estimate | Constructive component exposure; medium confidence | **Not eligible** until product-linked output/share/margin clear | Present; allocation and qualified output are upgrade tests | Public claims retained; agreement scope bounded | Relative stance complete; earnings layer pending |
| Lumentum | Pending baseline reconciliation and order-to-revenue bridge | UHP/ELSFP/external-light route; orders lack customer/SKU/quantity | Disclosed order and capacity signals; no cleared CPO estimate | Constructive/watch external-light exposure; medium confidence | **Not eligible** until order conversion and margin boundary clear | Present; product/customer/quantity conversion is upgrade test | Public order claims retained; no proprietary estimate published | Relative stance complete; earnings layer pending |
| Marvell | Pending baseline reconciliation and Celestial segment treatment | Celestial Photonic Fabric accelerator optical-I/O comparator, not switch CPO | Management FY28/FY29 targets; not observed production | Strategic watch; low-to-medium confidence | **Not eligible** until named XPU/customer and production economics clear | Present; qualification and reported revenue/margin conversion are upgrade tests | Public management claims labelled; no target price | Relative stance complete; earnings layer pending |
| TSMC | Pending baseline reconciliation and package/capex allocation | COUPE SiPh/EIC integration; engineering-sample yield is not final-engine yield | 2026 production milestone and customer-linked demonstrations | Manufacturing-control watch; medium confidence | **Not eligible** until customer SKU, output and attributable economics clear | Present; qualified output and package allocation are upgrade tests | Public process/roadmap claims bounded; consolidated margins excluded | Relative stance complete; earnings layer pending |

## Analyst-layer controls

- The consolidated baseline must be reconciled before adding any CPO overlay:
  fiscal year, currency, GAAP/non-GAAP basis, diluted shares, stock splits/ADR
  conversion, revenue, gross margin, operating margin, capex and valuation
  convention.
- Restricted analyst reports may provide scenario inputs only. Exact proprietary
  estimates, analyst names where licence terms are uncertain and model pages do
  not enter the public report.
- CPO systems, engines, PICs, lasers, packaging and test must use one economic
  boundary. No company-wide margin may be applied to a CPO layer.
- Bear/base/bull sensitivity remains a private harness until at least one
  product-matched customer/production denominator and one attributable economic
  input are available. Until then, the correct output is “not eligible,” not a
  point estimate.

## Completion result

The six cards are complete enough for **relative, evidence-gated stances** and
watchlists. They are not complete for numeric CPO revenue, EPS, valuation or
profit-pool rankings. The controlling next actions remain in the [six-company
commercial-proof queue](../six-company-commercial-proof-queue-2026-08-12.md)
and the [analyst-estimate register](../../08-model/analyst-estimate-register.md).

Related controls: [core-company variant cards](core-company-variant-cards.md),
[estimates-to-variant reconciliation](../../08-model/analyst-variant/estimates-to-variant-reconciliation-2026-08-12.md),
[optical-engine profit-pool gates](../../08-model/optical-engine-profit-pool-input-gates.md),
and the [public-release manifest](../../00-scope/public-release-manifest-2026-08-12.md).

The latest public-evidence refresh is recorded in [six-company commercial-proof
refresh — 12 August 2026](../../09-primary-research/six-company-commercial-proof-refresh-2026-08-12.md).
