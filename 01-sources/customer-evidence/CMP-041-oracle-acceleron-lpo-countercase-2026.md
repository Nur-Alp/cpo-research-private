# CMP-041 — Oracle Acceleron LPO/LRO scale-out countercase

- **Publisher:** Oracle Cloud Infrastructure
- **Canonical source:** https://blogs.oracle.com/cloud-infrastructure/first-principles-acceleron-multiplanar-networking
- **Publication:** 2026-03-04
- **Evidence class:** Hyperscaler/operator architecture post

Oracle describes its Acceleron AI networking architecture as a multiplanar fabric using high-radix switching, shuffle/breakout cabling and power-saving LPO/LRO optics. Oracle states that LPOs can save 4–7 W per module directly, translating to roughly 250–500 W on a 64-module switch, and says its fabrics support 400G or 800G links. The post emphasizes independent planes, modular replacement and bounded fault blast radius.

**Evidence boundary:** This is a customer/operator architecture countercase to assuming CPO is universally required. The power and throughput statements are Oracle claims without a retained matched test setup, product SKU, lane-loss distribution, BER, qualification, field reliability, ASP or margin. It does not establish that LPO wins every topology.
