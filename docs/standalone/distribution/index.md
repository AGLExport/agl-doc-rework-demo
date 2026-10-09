---
title: AGL Distribution
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Distribution

The AGL Unified Code Base (UCB) is a Linux distribution built with the Yocto Project for automotive software. It provides the operating-system foundation, platform services and reference applications used by the [Base platform for the distributed system](../index.md). An image selects the packages and configuration needed for a particular vehicle role and board. See the official [Unified Code Base overview](https://www.automotivelinux.org/software/unified-code-base/).

This documentation follows **AGL master**. The [master manifest](https://git.automotivelinux.org/AGL/AGL-repo/tree/default.xml?h=master) selects the AGL layers and external dependencies. AGL layers follow master; external projects retain the revisions selected by that manifest. Build the image, SDK and separately assembled AGL guests from one resolved source manifest, or take matching prebuilt artifacts from one master snapshot. [Releases & migration](../../releases/index.md) explains the reviewed baseline and how to record and update it.

## Choose a task

| Goal | Chapter |
| --- | --- |
| Run a ready-made Flutter IVI image | [Quick start](../../start/index.md) |
| Compare demos and their intended roles | [Portfolio](../portfolio/index.md) |
| Understand runtimes, services and display access | [Architecture](../architecture/index.md) |
| Prepare source, build an image and boot a target | [Build AGL system](../build/index.md) |
| Understand reference applications, services, lifecycle and APIs | [AGL Components](../../components/index.md) |
| Change image contents, recipes and services | [Platform Customize](../customize/index.md) |
| Build and deploy Flutter or Qt applications | [Application development](../applications/index.md) |

## Select an image family

[Basic demo system](../portfolio/basic/index.md) covers Flutter IVI, Qt IVI and the IVI-derived Flutter Cluster. Flutter and Qt IVI share the same IVI platform; their toolkit-specific runtime packages differ. [Basic architecture](../architecture/basic.md) shows the corresponding component diagrams.

[Extra demo system](../portfolio/extra/index.md) covers dedicated Qt and Slint Cluster examples and the lightweight Momi IVI guest. Build the dedicated cluster images through [Extra AGL system](../build/extra/index.md). For Momi, use [Container integration's Momi IVI demo](../../integrated/containers/demo/momi-ivi.md), which assembles its host and guest together.

Basic and Extra are documentation groups, not names of `aglsetup.sh` features. Select the machine, features and image target specified by the chosen build guide. The [board and image matrix](../build/common/reference/matrix.md) describes supported combinations.
