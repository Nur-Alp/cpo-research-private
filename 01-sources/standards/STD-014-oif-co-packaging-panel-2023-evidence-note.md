# STD-014 — OIF co-packaging panel: fibre-count yield compounding

**Canonical source:** <https://www.oiforum.com/wp-content/uploads/2023-OFC-sm-Co-Packaging-Panel.pdf>  
**Publisher:** Optical Internetworking Forum (OIF)  
**Panel date:** 2023-03-09  
**Local retention:** The original PDF link is preserved because the OIF server did not permit a complete local download in this environment.

## Evidence extracted

The panel's yield slide gives an explicit compounding example for a 51.2T Ethernet switch card:

- DR/PSM case: 512 transmit fibre connections, 512 receive connections and 64 laser-PM-fibre connections, or **1,088 total fibre connections**.
- FR4/CWDM case: 128 transmit, 128 receive and 32 laser-PM-fibre connections, or **288 total fibre connections**.
- Under an assumed **3-sigma per-fibre first-pass connection yield of 99.865%**, the calculated first-pass board fibre-assembly yield is shown as approximately **23.0%** for the 1,088-connection case and **67.8%** for the 288-connection case.

These figures are arithmetic/system-level examples in an interoperability panel, not measured HVM yields. They are nevertheless valuable because they expose the scaling penalty from multiplying many individually high-yield fibre connections.

## Model use

Use as a sensitivity anchor for the yield waterfall:

```text
board first-pass yield = per-connection yield ^ number of fibre connections
```

Do not treat 23.0% or 67.8% as a supplier's actual production yield. The panel does not disclose the measured per-connection distribution, rework recovery, connector type for each case, package yield, test escapes, qualification status or cost.

## Why it matters

This is direct support for the thesis that fibre count and connection architecture can dominate cost per accepted CPO assembly. A detachable, pre-tested, or lower-fibre architecture may create economic value even if its component coupling loss is not the absolute minimum.

**Use:** yield-compounding sensitivity and architecture comparison; not a production or company-specific forecast. See `CLM-397`–`CLM-400`.
