---
title: Service APIs and configuration
---
# Service APIs and configuration

Use this directory to find a service's detailed API, configuration, and integration documentation. For a system-level overview, read [How AGL services fit together](../../explanation/services.md).

| Area | Detailed documentation | Related task or concept |
| --- | --- | --- |
| Graphics | [AGL compositor](graphics/agl-compositor.md), [DRM lease manager](graphics/drm-lease-manager.md) | [System architecture](../../explanation/architecture.md) |
| Audio | [PipeWire and WirePlumber](audio/pipewire-wireplumber.md), [IC sound management](audio/instrument-cluster-sound.md) | [Services overview](../../explanation/services.md) |
| Policies | [Rule-based arbitrator](policies/rule-based-arbitrator.md) | [System architecture](../../explanation/architecture.md) |
| Persistent data | [Persistent Storage API](persistent-storage.md) | [Develop an application](../../develop/index.md#apps) |
| Voice | [Voice agent assistant](voice-agent.md) | [Image targets](../images.md) |
| Instrument Cluster | [API specification](instrument-cluster-api.md), [IC service](instrument-cluster-service.md) | [Build an IC demo](../../develop/demos/instrument-cluster.md) |
| Application lifecycle | [Application startup and applaunchd](../apps/application-startup.md) | [Application framework](../../explanation/application-framework.md), [Register an application](../../develop/apps/create-application.md) |
| Containers | [Container Manager](container-manager.md), [global configuration](../config/container/global.md), [container files](../config/container/containers.md) | [IC container profile](../../develop/demos/instrument-cluster.md) |
| Distributed HMI | [Unified HMI](unified-hmi.md) | [System architecture](../../explanation/architecture.md) |
| Simulated vehicle data | [Vehicle](../vehicle-signals/vehicle.md), [body](../vehicle-signals/body.md), [sensor](../vehicle-signals/sensors.md) signals | [Virtual car](../../develop/tools/virtual-car.md), [USB CAN adapter](../../develop/tools/usb-can-adapter.md) |

## Coverage and upstream sources

The source documentation contains a mixture of API specifications, configuration references, and integration instructions. The [original API overview](legacy-api-overview.md) identifies remaining gaps, while the [component directory](../components.md) provides another entry point.

Check each service's prerequisites and links to its upstream repository. A service appearing in this directory does not mean it is enabled in every AGL image.
