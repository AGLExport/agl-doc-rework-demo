---
title: "Background"
content_status: authored
---

# Background

AGL covers individual automotive Linux systems and platforms that consolidate several workloads. The vehicle E/E architectures below explain the main focus of the three system categories used in this documentation. They describe deployment patterns; a product can combine them across a vehicle.

## Vehicle EE architectures.

Vehicle electrical/electronic (E/E) architecture determines where software runs and how controllers communicate. Controller placement and network choices vary by vehicle. Select a figure to open a larger view.

### Traditional distributed architecture.

In a traditional distributed design, individual electronic control units (ECUs) handle specific functions and exchange data over vehicle networks. Adding features can add controllers and connections, increasing the work needed to coordinate software across the vehicle.

[![Traditional distributed architecture: separate function-specific ECUs connected through a vehicle network.](../assets/diagrams/traditional-distributed.svg)](../assets/diagrams/traditional-distributed.svg)

*Figure 1. Functions run on separate ECUs that communicate over the vehicle network.*

AGL's [Distributed system](../standalone/index.md) mainly focuses on this architecture. Each standalone deployment supplies one Linux kernel and userland for its selected role, and several deployments can exchange vehicle data.

### Domain architecture.

A domain design groups related functions, such as cockpit, body control, or powertrain, under domain controllers. Computation is consolidated by functional responsibility, while communication between domains remains part of system integration.

[![Domain architecture: cockpit, body, and powertrain controllers coordinate their devices and communicate over a backbone.](../assets/diagrams/domain.svg)](../assets/diagrams/domain.svg)

*Figure 2. Functions are grouped into logical domains with their own controllers.*

AGL's [Small scale integrated system](../integrated/index.md) mainly focuses on this architecture. Container integration and KVM combine two or more features, such as IVI and Instrument Cluster, on shared computing resources.

### Central/Zone architecture.

A central/zone design combines central computing with controllers organized by physical location. Zone controllers connect nearby sensors and actuators to the vehicle network; central computers host consolidated workloads. This separates local device connections from software placement and can reduce wiring complexity. [NXP's architecture overview](https://www.nxp.com/company/about-nxp/smarter-world-blog/BL-HOW-ZONAL-EE-ARCHITECTURES) explains the shift from separate functions to domains and zones.

[![Central and zonal architecture: central computing connects to physical zone controllers, which connect to nearby sensors and actuators.](../assets/diagrams/central-zone.svg)](../assets/diagrams/central-zone.svg)

*Figure 3. Central computing hosts workloads while zones organize local device connections.*

AGL's [Large scale integrated system](../integrated/large-scale.md) mainly focuses on this architecture. SoDeV provides a platform for consolidating guest systems and workloads with different criticality requirements. Distributed systems and small-scale integrations can be incorporated as part of that larger system.

## Further reading

- [About Automotive Grade Linux](about-source.md)
- [AGL system architecture](architecture.md)
- [Build host, target, image, and SDK](build-and-runtime.md)
- [AGL glossary](glossary.md)
- [Understand AGL](reading-guide.md)
