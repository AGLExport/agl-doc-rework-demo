---
title: Architecture
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Architecture

SoDeV combines AGL UCB with virtualization and other open source components. A hypervisor separates guests, while VirtIO interfaces connect guest workloads to device backends. The [official availability announcement](https://www.automotivelinux.org/announcements/automotive-grade-linux-releases-open-source-sodev-reference-platform-for-software-defined-vehicles-and-welcomes-five-new-members/) identifies Xen, containers, VirtIO, and Zephyr among its components.

[![Official SoDeV architecture with control, driver, and guest domains, VirtIO interfaces, Unified HMI, and a hypervisor.](../../assets/diagrams/sodev-official-architecture.png)](../../assets/diagrams/sodev-official-architecture.png)

*Official AGL figure, reproduced unchanged from the [launch announcement](https://www.automotivelinux.org/announcements/sodev/). [Original image](https://www.automotivelinux.org/wp-content/uploads/sites/61/2025/12/image.png).*

| Role | Responsibility |
| --- | --- |
| Control domain, when used | Platform management and domain lifecycle |
| Driver domain | Physical-device ownership and backend services |
| Guest/function domains | Selected workload and its guest operating environment |
| VirtIO interfaces | Guest-visible devices connected to backend implementations |
| Unified HMI | Graphical workload and display integration |

This is the reference architecture, not a claim that every workspace enables every domain. The [Sparrow Hawk workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace) and [Raspberry Pi workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace-rpi) define concrete board and guest combinations.

Continue with [Build SoDeV](build.md), [Create and Run Guest VM](customize/guest-vm.md), and [Unified HMI](../../components/extensions/unified-hmi.md).
