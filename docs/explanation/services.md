---
title: How AGL services fit together
---
# How AGL services fit together

The [AGL system architecture](architecture.md) separates applications and HMI, application lifecycle services, system services, and the operating system.

## Applications and lifecycle

Applications use the runtime provided by their image. The application framework discovers and launches applications, while the compositor manages their graphical presentation.

- [Application framework](application-framework.md)
- [Application startup reference](../reference/apps/application-startup.md)
- [Application packaging](../develop/apps/create-application.md)

## Graphics and audio

The compositor and DRM lease manager cover graphical presentation and display access. PipeWire, WirePlumber, and the Instrument Cluster sound manager cover the documented audio integration.

See the [service directory](../reference/services/index.md) for their detailed configuration and API pages.

## Vehicle data and demo tools

The supplied demo images describe their KUKSA.val databroker configuration. The virtual car, CAN tools, and demo control panel provide documented ways to drive demonstrations and simulated vehicle signals.

- [Image targets and network assumptions](../reference/images.md)
- [Virtual car](../develop/tools/virtual-car.md)
- [Vehicle signal references](../reference/vehicle-signals/vehicle.md)
- [Demo Control Panel](../develop/tools/demo-control-panel.md)

## Containers and distributed HMI

Container Manager, the Instrument Cluster container profile, and Unified HMI describe different integration areas. Read the relevant profile before choosing an image and board.

- [Container Manager reference](../reference/services/container-manager.md)
- [Instrument Cluster profile](../develop/demos/instrument-cluster.md)
- [Unified HMI reference](../reference/services/unified-hmi.md)
