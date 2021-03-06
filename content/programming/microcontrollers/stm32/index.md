---
author: "gbmhunter"
date: 2020-06-19
description: "Info about the STM32 range of microcontrollers."
categories: [ "Programming", "Microcontrollers", "STM32" ]
lastmod: 2020-08-03
tags: [ "programming", "microcontrollers", "STM32", "STM32F0", "Cortex-M0", "ARM", "STM32CubeIDE", "Nucleo", "STM32WLEx", "LoRa", "LoRaWAN" ]
title: "STM32 Microcontrollers"
type: "page"
---

{{% warning-is-notes %}}

## Overview

`STM32` is a family of 32-bit, ARM Cortex-M microcontrollers manufactured by ST Mircoelectronics. 

All `STM32` micros are supported by ST's own {{% link text="STM32CubeIDE" src="/programming/integrated-development-environments-ides/stm32cubeide" %}}.

## Development Kits

A very popular range of development kits using the STM32 microcontrollers is the STM32 Nucleo. 

A Windows machine is required to update the firmware on the Nucleo programmer/debugger IC (the IC which emulates an ST-Link).

## STM32F0

The `STM32F0` is a family of "general purpose" STM32 microcontrollers. The family uses a 48MHz ARM Cortex-M0 CPU architecture.

Low-power modes:

* Sleep mode: Only the CPU is stopped. All peripherals continue to operate and can wake-up the CPU.
* Stop mode: A mode designed to put everything into a low-power state but retain the content of SRAM and the registers.
* Standby mode: The lowest-power mode. Everything is stopped and SRAM/register content is lost, except for the registers in the RTC domain and standby circuitry

GPIO capabilities:

GPIO can be configured as one of the following outputs:

* Push-pull
* Open-drain

Or as the following inputs:

* High-impedance
* Pull-up
* Pull-down

Reference schematic for the STM32F030 (just power, clock and programming):

{{% img src="stm32f030-reference-schematic.png" width="800px" caption="The reference schematic for the STM32F030 microcontroller. Image from https://www.st.com/resource/en/application_note/dm00089834-getting-started-with-stm32f030xx-and-stm32f070xx-series-hardware-development-stmicroelectronics.pdf." %}}

## STM32WLEx

The `STM32WLEx` is a family of "SoC" microcontrollers featuring a STM32L4 coupled with a wireless radio IC that supports LoRaWAN (both of these are in the same physical IC).