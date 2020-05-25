BPH (Bluepill Hat)
==================

## Description

The BPH is a hat for the Raspberry Pi 3 designed to connect
[PHiLIP-b](https://github.com/riot-appstore/PHiLIP) to a
DUT (Device Under Test) which typically consists of a micro-controller
development board.

It provides connections to communicate with PHiLIP, a convenient 20 pin ribbon
cable for the pinout to the DUT and some power control and monitoring. The
purpose is to make an easy to assembly and maintain setup for
HiL (hardware in the loop) testing at a low cost.

## Building the BPH

The BPH was designed so a skilled hobbiest can reproduce it.
The [gerber files](BPH-2C/PCB) and [BOM](BPH-2C/Assembly) for the PCB should be
enough to build a board.
[Board design files](https://workspace.circuitmaker.com/Projects/Details/Kevin-Weiss-2/bph) are also available.
Manufacturing costs for 100 board units range between 1000 to 2000 EUR for a turnkey solution.

Along with the BPH board, a [PHiLIP-b](https://github.com/riot-appstore/PHiLIP) is needed.

## Using the BPH

A [BPH interface](bph_pal/) is provided to make usage easier.

## Wiring

Using a standard ribbon cable to connect the BPH to the DUT the following wiring should be followed

BPH Pin | Color  | DUT Pin
--------|--------|----------
1       | BLACK  | DUT_NSS
2       | WHITE  | DUT_SCK
3       | GREY   | DUT_MISO
4       | PURPLE | DUT_MOSI
5       | BLUE   | DUT_IC
6       | GREEN  | DUT_SCL
7       | YELLOW | GND
8       | ORANGE | DUT_SDA
9       | RED    | DUT_RST
10      | BROWN  | DUT_PWM
11      | BLACK  | DUT_CTS
12      | WHITE  | DUT_DAC
13      | GREY   | DUT_RTS
14      | PURPLE | EXT_V_OUT
15      | BLUE   | DUT_RX
16      | GREEN  | DEBUG2
17      | YELLOW | DUT_TX
18      | ORANGE | DEBUG1
19      | RED    | DUT_ADC
20      | BROWN  | DEBUG0
