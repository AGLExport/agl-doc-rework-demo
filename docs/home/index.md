---
title: "AGL Artifact"
content_status: authored
---

# AGL Artifact

AGL artifacts include a Linux distribution for individual vehicle roles and a base platform for integrating several workloads. The vehicle E/E architectures below explain the relationship between distributed deployments and integrated systems.

## Vehicle EE architectures.

Vehicle electrical/electronic (E/E) architecture determines where software runs and how controllers communicate. The figures illustrate three ways to organize vehicle computing. Controller placement and network choices vary by vehicle. Select a figure to open a larger view.

### Traditional distributed architecture.

In a traditional distributed design, individual electronic control units (ECUs) handle specific functions and exchange data over vehicle networks. Adding features can add controllers and connections, increasing the work needed to coordinate software across the vehicle.

[![Traditional distributed architecture: separate function-specific ECUs connected through a vehicle network.](../assets/diagrams/traditional-distributed.svg)](../assets/diagrams/traditional-distributed.svg)

*Figure 1. Functions run on separate ECUs that communicate over the vehicle network.*

[Linux Distribution](standalone/index.md) introduces the use of standalone AGL environments for individual vehicle roles.

### Domain architecture.

A domain design groups related functions, such as cockpit, body control, or powertrain, under domain controllers. Computation is consolidated by functional responsibility, while communication between domains remains part of system integration.

[![Domain architecture: cockpit, body, and powertrain controllers coordinate their devices and communicate over a backbone.](../assets/diagrams/domain.svg)](../assets/diagrams/domain.svg)

*Figure 2. Functions are grouped into logical domains with their own controllers.*

[Base platform for integrated system](integrated/index.md) introduces platforms for bringing several workloads together on shared computing resources.

### Central/Zone architecture.

A central/zone design combines central computing with controllers organized by physical location. Zone controllers connect nearby sensors and actuators to the vehicle network; central computers host consolidated workloads. This separates local device connections from software placement and can reduce wiring complexity. [NXP's architecture overview](https://www.nxp.com/company/about-nxp/smarter-world-blog/BL-HOW-ZONAL-EE-ARCHITECTURES) explains the shift from separate functions to domains and zones.

[![Central and zonal architecture: central computing connects to physical zone controllers, which connect to nearby sensors and actuators.](../assets/diagrams/central-zone.svg)](../assets/diagrams/central-zone.svg)

*Figure 3. Central computing hosts workloads while zones organize local device connections.*

[SoDeV](integrated/sodev.md), [Container integration](integrated/containers.md), and [KVM based integration](integrated/kvm.md) describe the integration approaches covered by AGL.

## AGL distributed system.

AGL provides a base distribution for distributed ECUs. A standalone AGL environment supplies the operating system, services, and applications for a selected role. Separate deployments can communicate through vehicle data interfaces while retaining their own software environments.

The [Linux Distribution](standalone/index.md) section introduces these roles:

- [In-Vehicle Infotainment](standalone/ivi.md) supplies the cabin user experience.
- [Instrument Cluster](standalone/cluster.md) presents driving information.
- [Connected Gateway](standalone/gateway.md) connects vehicle data and external services.

## AGL integrated system.

AGL integrated systems provide a base platform for domain or central/zone architecture by bringing several automotive workloads together through guest environments and shared platform resources. This relationship describes their role in system design; the chosen integration determines workload placement, resource allocation, and communication.

The [Base platform for integrated system](integrated/index.md) section covers three approaches:

- [SoDeV](integrated/sodev.md) provides a reference platform for software-defined vehicles. See the [official SoDeV announcement](https://www.automotivelinux.org/announcements/automotive-grade-linux-releases-open-source-sodev-reference-platform-for-software-defined-vehicles-and-welcomes-five-new-members/).
- [Container integration](integrated/containers.md) separates guest environments that share a host kernel.
- [KVM based integration](integrated/kvm.md) uses virtual machines with their own guest kernels.

## Further reading

- [About Automotive Grade Linux](about-source.md)
- [AGL system architecture](architecture.md)
- [Build host, target, image, and SDK](build-and-runtime.md)
- [AGL glossary](glossary.md)
- [Understand AGL](reading-guide.md)
