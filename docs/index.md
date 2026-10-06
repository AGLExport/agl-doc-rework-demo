---
title: "Home"
content_status: authored
---

# Home

## What is AGL

Automotive Grade Linux (AGL) is a collaborative open source project hosted by the Linux Foundation. Automakers, suppliers, and technology companies develop a shared Linux-based platform for automotive software. Common infrastructure enables software reuse across projects while leaving room for product-specific applications and integration. See the [AGL project introduction](https://www.automotivelinux.org/).

## Background

Vehicle electrical/electronic (E/E) architecture determines where software runs and how controllers communicate. The following designs provide context for the distributed and integrated systems covered by this documentation.

### Traditional distributed architecture.

In a traditional distributed design, individual electronic control units (ECUs) handle specific functions and exchange data over vehicle networks. Adding features can add controllers and connections, increasing the work needed to coordinate software across the vehicle.

### Domain architecture.

A domain design groups related functions, such as infotainment, body control, or driver assistance, under domain controllers. Computation is consolidated by functional responsibility, while communication between domains remains part of system integration.

### Central/Zone architecture.

A central/zone design combines central computing with controllers organized by physical location. Zone controllers connect nearby sensors and actuators to the vehicle network; central computers host consolidated workloads. This separates local device connections from software placement and can reduce wiring complexity. [NXP's architecture overview](https://www.nxp.com/company/about-nxp/smarter-world-blog/BL-HOW-ZONAL-EE-ARCHITECTURES) explains the shift from separate functions to domains and zones.

## AGL distributed system overview.

In this documentation, an AGL distributed system uses AGL software for distinct vehicle roles, with a standalone distribution providing the environment for a selected role. In-Vehicle Infotainment supplies the cabin user experience; Instrument Cluster presents driving information; Connected Gateway connects vehicle data and external services. These roles can communicate while remaining separate deployments.

The [AGL distributed system.](home/standalone/index.md) chapter introduces each role within [AGL Coverage](home/index.md).

## AGL integrated system overview.

An AGL integrated system brings multiple workloads together through guest environments and shared platform resources. This documentation covers SoDeV, container integration, and KVM based integration. Containers share the host kernel, while virtual machines run guest kernels; the chosen integration defines resource allocation and communication between workloads.

SoDeV provides an AGL reference platform for software-defined vehicles, as described in the [official SoDeV announcement](https://www.automotivelinux.org/announcements/automotive-grade-linux-releases-open-source-sodev-reference-platform-for-software-defined-vehicles-and-welcomes-five-new-members/). The [AGL integrated system](home/integrated/index.md) chapter introduces the three integration approaches. Their relationship to central computing is a conceptual framing used here; a particular vehicle architecture depends on its system design.
