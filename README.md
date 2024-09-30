# DIY Oximeter

## Project Overview
This repository contains the code and documentation for a DIY oximeter project, developed as part of a university coursework. The oximeter measures the oxygen saturation level in the blood and heart rate using a combination of hardware sensors and software algorithms.
Two PCBs are used, one housing the dual LED emitter that emits red and infrared light. The other PCB houses the photodiode that continuously measures the modulated light that has passed through the blood vessels of the finger. A Pico MCU ADC picks up this signal and interprets it as the heart rate and SpO2.

## Table of Contents
- [Features](#features)
- [Hardware Used](#hardware-requirements)
- [Software Requirements](#software-requirements)

## Features
- Measures blood oxygen saturation (SpO2)
- Measures heart rate
- Sends readings to the connected PC to display data

## Hardware Used
- vemd8080 Silicon PIN Photodiode
- vsmd66694 Dual Color Emitting Diodes, 660 nm and 940 nm
- OPA2380 Precision, High-Speed Transimpedance Amplifier
- MMBT2222A Switching transistor
- Raspberry Pi Pico W Microcontroller

## Software Requirements
- Python3
- pip install -r requirements.txt

## Dual LED Emitter Circuit Schematic
<img src="resources\images\dual_led_emitter_sch.jpg" width="400" >


## Photodiode Circuit Schematic
<img src="resources\images\photodiode_sch.jpg" width="400" >

## Showcase
<iframe width="560" height="315" src="resources\videos\demo.mp4" frameborder="0" allowfullscreen></iframe>

<!-- ![demo](resources\videos\demo.mp4) -->
