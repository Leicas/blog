---
author: gbmhunter
date: 2013-11-08
draft: false
title: Load Switches
type: page
---

## MOSFET Based

The following image shows a MOSFET based high-side switch:

{{< img src="high-side-mosfet-load-switch-schematic.png" width="678px" caption="A high-side load switch made from a N-Channel and P-Channel MOSFET."  >}}

## IC Based

The following image shows an IC based high-side switch.

{{< img src="high-side-load-switch-with-tps27082lddcr-ic-schematic.png" width="692px" caption="The TPS27082LDDCR, a high-side load switch IC."  >}}

Some load-switches have reverse-polarity protection. More information of how they exactly implement reverse-protection with only the one MOSFET can be found in the [The Substrate (Body) Connection section of the MOSFET page](/electronics/components/transistors/mosfets/#the-substrate-body-connection).


{{< img src="ncp380-ncv-380-load-switch-internal-block-diagram-with-reverse-current-protection.png" width="516px" caption="A functional diagram of the NCP380 high-side load switch. Note the switches connected to the MOSFET substrate which show how reverse-current protection is performed."  >}}

