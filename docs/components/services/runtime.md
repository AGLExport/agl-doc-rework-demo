---
title: How AGL services fit together
---
# How AGL services fit together

The [AGL system architecture](../../home/architecture.md) separates applications and HMI, application lifecycle services, system services, and the operating system.

## Applications and lifecycle

Applications use the runtime provided by their image. The application framework discovers and launches applications, while the compositor manages their graphical presentation.

- [Application framework](../framework/lifecycle/application-framework.md)
- [Application startup reference](../framework/lifecycle/application-startup.md)
- [Application packaging](../../standalone/applications/create-application.md)

## Graphics and audio

The compositor and DRM lease manager cover graphical presentation and display access. PipeWire, WirePlumber, and the Instrument Cluster sound manager cover the documented audio integration.

See the [service directory](index.md) for their detailed configuration and API pages.

## Vehicle data and demo tools

The supplied demo images describe their KUKSA.val databroker configuration. The virtual car, CAN tools, and demo control panel provide documented ways to drive demonstrations and simulated vehicle signals.

- [Image targets and network assumptions](../../standalone/build/common/reference/images.md)
- [Virtual car](../tools/virtual-car/virtual-car.md)
- [Vehicle signal references](../tools/virtual-car/signals/vehicle.md)
- [Demo Control Panel](../tools/demo-control/panel.md)

## Containers and distributed HMI

Container Manager, the Instrument Cluster container profile, and Unified HMI describe different integration areas. Read the relevant profile before choosing an image and board.

- [Container Manager reference](../extensions/container-manager.md)
- [Instrument Cluster profile](../../integrated/containers/build-guide.md)
- [Unified HMI reference](../extensions/unified-hmi.md)
