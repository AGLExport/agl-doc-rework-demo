---
title: Home
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Home

## What is AGL.

Automotive Grade Linux (AGL) is a collaborative open source project hosted by the Linux Foundation. Automakers, suppliers, and technology companies develop a shared Linux-based platform for automotive software. Sharing common infrastructure reduces fragmentation and lets teams reuse software across projects while developing their own applications and user experiences. The [AGL project introduction](https://www.automotivelinux.org/about/) explains this collaborative approach.

The AGL Unified Code Base (UCB) is the project's common Linux distribution, built using the Yocto Project. It combines a base operating system with automotive software components, including application infrastructure, audio services, and vehicle data interfaces. It provides a starting point that developers can configure for their hardware and product requirements. See the [Unified Code Base overview](https://www.automotivelinux.org/software/unified-code-base/).

AGL began with infotainment and has a broader goal of supporting automotive software across vehicle roles. This documentation covers In-Vehicle Infotainment, Instrument Cluster, and Connected Gateway, alongside platforms that integrate several workloads. A product team selects the relevant software, adds its own applications, and integrates it with the intended vehicle environment.

Read [Introduction](home/index.md) for AGL coverage and the relationship between vehicle E/E architecture and [Vehicle Data Processing](home/index.md#vehicle-data-processing). [Base platform for Vehicle Controller](vehicle-controller/index.md) groups distributed, small-scale and large-scale vehicle systems; [Base platform for Vehicle Data Processing](vehicle-data/index.md) introduces Connected Gateway and its data interfaces. [AGL Distribution](distributed/distribution/index.md) provides the demo, build, component and application guides for a distributed Linux system.

## AGL Community information.

The AGL community develops software, discusses requirements, and maintains the project's documentation. Expert Groups focus on particular technical areas, and community meetings provide a place to follow ongoing work. The [AGL Wiki](https://wiki.automotivelinux.org/) explains the project's organization and collaboration.

- [Mailing lists](https://lists.automotivelinux.org/g/agl-main) provide topic-specific discussions and public archives.
- [Community meetings](https://www.automotivelinux.org/developer-meetings/) provide meeting information and ways to participate.
- [AGL Expert Groups](https://lf-automotivelinux.atlassian.net/wiki/spaces/HOME/overview) provide technical collaboration spaces.
- [Community standard](community/index.md) groups source-version guidance and the [Contribution gide](contributing/index.md) for accounts, code review and documentation contributions.
- [Get community help](troubleshooting/getting-help.md) explains how to ask questions and report useful diagnostic information.

## Develop and operate an AGL system

Use [Development & Usage](development/index.md) to select development workflows and demo-control tools. The [AGL Virtual Car definition](virtual-car/index.md) describes the CAN data shared by the demonstrations. Use [Troubleshooting](troubleshooting/index.md) to diagnose setup, boot and service problems.
