---
title: Get started
---

# Get started

Start by booting a prebuilt image. If you want to build an image from source, follow the [platform development guide](../develop/index.md#platform).

## 1. Choose a version and an environment

This site targets the **{{ agl.full_name }} / `{{ agl.codename }}` development branch**. For a stable release, use [Releases & migration](../releases/index.md) to choose a version and find its documentation and artifacts.

For unfamiliar terms, use the [glossary](../reference/glossary.md). Check the [board and image matrix](../reference/matrix.md) for the environment and demo you want to use. Keep a record of the board, image, and source branch; these details will also help during development or when asking for support.

## 2. Boot a prebuilt image

### Starting point: QEMU x86-64

For a Linux host, start with the [QEMU x86-64 instructions](qemu-x86-64.md). Download the image and kernel for your version, prepare QEMU, and follow the launch steps.

This route points to the existing instructions. Check that the host requirements, QEMU options, and available artifacts match the version you are using.

### Other environments

Choose a separate guide for your environment:

| Environment | Setup guide |
| --- | --- |
| QEMU x86-64 | [Run on QEMU x86-64](qemu-x86-64.md) |
| QEMU AArch64 | [Run on QEMU AArch64](qemu-arm64.md) |
| VirtualBox | [Run on VirtualBox](virtualbox.md) |
| Physical x86-64 system | [Run on x86-64 hardware](x86-hardware.md) |
| Raspberry Pi 4 | [Run on Raspberry Pi 4](raspberry-pi.md) |

Use the [prebuilt image overview](prebuilt-images.md) to compare the environments. For hardware, first check [hardware support](../reference/hardware.md) and [image types](../reference/images.md).

## 3. Check the result

Confirm that the login prompt or demo screen described in your chosen instructions appears. When running commands, distinguish between the terminal on your host and the console on the AGL target.

If the expected screen does not appear, record the version, downloaded filenames, launch command, and console messages, then use [Diagnose common problems](../troubleshooting/diagnostics.md) for initial checks and log collection.

## Next steps

- [Develop an application](../develop/index.md#apps): work with Flutter or an SDK.
- [Build an image](../develop/index.md#platform): build a configuration of your own.
- [Understand AGL](../explanation/index.md): learn how applications and services fit together.
- [API & configuration](../reference/index.md): find the specifications for a feature.
