---
title: Architecture
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Architecture

SoDeV combines AGL UCB with virtualization and other open source components. A hypervisor separates guests, while VirtIO interfaces connect guest workloads to device backends. The [official availability announcement](https://www.automotivelinux.org/announcements/automotive-grade-linux-releases-open-source-sodev-reference-platform-for-software-defined-vehicles-and-welcomes-five-new-members/) identifies Xen, containers, VirtIO, and Zephyr among its components.

## Platform overview

[![Official SoDeV overview showing control, driver and guest domains, a type 1 hypervisor, and adjacent microcontroller and hard real-time domains.](../../../../assets/diagrams/sodev-arch-overview.drawio.svg)](../../../../assets/diagrams/sodev-arch-overview.drawio.svg){ .sodev-architecture }

The overview places SoDeV's virtualized subsystem on a high-performance SoC. Control and driver domains support guest domains that host major functions and features. The guest examples distinguish general-purpose operating systems, such as AGL and Android, from soft real-time operating systems, such as Zephyr and RT Linux. Hard real-time domains and a microcontroller part appear alongside this subsystem.

## Domain and device architecture

[![Official SoDeV detailed design showing Dom 0, Dom D and functional Dom U guests, VirtIO frontends and backends, and Unified HMI.](../../../../assets/diagrams/sodev-arch-details.drawio.svg)](../../../../assets/diagrams/sodev-arch-details.drawio.svg){ .sodev-architecture }

*Official AGL SoDeV architecture overview and detailed design. Select either figure for a larger view.*

| Role | Responsibility and examples in the detailed design |
| --- | --- |
| Control domain (Dom 0) | VM management and monitoring; the figure shows a Zephyr control-domain kernel |
| Driver domain (Dom D) | Hardware access, a VirtIO-compliant SoC BSP and VirtIO backends; Linux and Zephyr/RT Linux are shown as driver-domain operating environments |
| Guest domains (Dom U) | Functional workloads: infotainment with AGL/AAOS, cluster and gateway with AGL, and ADAS/AD with RT Linux/Zephyr |
| VirtIO interfaces | Guest frontends communicate with the device backends supplied by driver domains |
| Unified HMI | HMI and display integration across functional guests |
| Type 1 hypervisor | Domain execution and isolation; Xen is an example shown in the figure |

This is the reference architecture, not a claim that every workspace enables every domain. The [Sparrow Hawk workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace) and [Raspberry Pi workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace-rpi) define concrete board and guest combinations.

Continue with [Build SoDeV](../build/index.md), [Create and Run Guest VM](../customize/guest-vm/index.md), and [Unified HMI](../components/platform-extensions/unified-hmi/index.md).
