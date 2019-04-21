---
author: gbmhunter
date: 2013-05-29
tags: [ "heatsink", "circuit design", "component", "overheating", "thermal", "temperature", "packages" ]
title: "Heatsinks"
type: page
---

## Overview

Heatsinks are used in circuit design to conduct heat away from a component faster than what air would do, usually to prevent high-power components from overheating and failing.

{{< img src="typical-to-220-heatsink-with-fins.jpg" width="411px" caption="A typical TO-220 heatsink with fins. Image from www.digikey.com."  >}}

Typical components that require heatsinking are high current [linear regulators](/electronics/components/power-regulators), MOSFET's on [H-bridges](/electronics/circuit-design/h-bridges), power amplifier BJT's and [MOSFET's](/electronics/components/transistors/mosfets/), and power limiting resistors. Most heatsinks are made from black anodized aluminium.

Their heatsinking capability is rated with a thermal resistance, which has the units \( ^{\circ} C / W \). Common packages that heatsinks are made for include [TO-220](/pcb-design/component-packages/to-220ab-component-package/), [SOT-223](/pcb-design/component-packages/sot-23-component-package/).

You can get heatsinks with twisted fins, which gives better cooling due to increased air turbulance and convection flow.

Phase change compounds can be used as thermal pads. Phase change compounds are designed to be solid at room temperature but become liquid at the operating temperature, which gives a better bond between the component and heatsink, lowering it's thermal resistance.

For more information on thermal resistances, see the [Thermal Management page](/electronics/circuit-design/thermal-management).

## Where Does The Heat Go?

The following diagram is a thermal analysis of a SMD MOSFET mounted to a PCB.

{{< img src="thermal-analysis-of-smd-mosfet-on-pcb.png" width="687px" caption="Thermal analysis of a SMD MOSFET mounted on a PCB. Image from http://www.fairchildsemi.com/an/AN/AN-1029.pdf."  >}}

## List Of Component Package Thermal Resistances

See the [Component Packages page](/pcb-design/component-packages/). This has many of the common component packages and their thermal resistances.

## Forced Convection

The following image shows two graphs combined into one, the thermal performance of a heatsink with natural convection, and that with forced convection (e.g. a fan).

{{< img src="heat-dissipation-graph-for-natural-and-forced-convection.png" width="960px" caption="Heat dissipation graph for both natural and forced convection. Image from http://www.aavid.com/sites/default/files/products/boardlevel/aavid-standard-heatsinks.pdf."  >}}

## Packages

There is no standard package for heatsinks and the pitch for their support pins, although some more common pin spacings exist (such as 25.4mm (1inch) e.t.c).

{{< img src="to-220-pcb-mount-heatsink-hs22-technical-drawing.png" width="1364px" caption="The technical drawing of a typical TO-220 heatsink. Image from www.digikey.com."  >}}