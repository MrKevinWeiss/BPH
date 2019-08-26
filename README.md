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
