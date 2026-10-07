---
title: "Basic AGL system"
content_status: authored
---

# Basic AGL system

Basic demos use the AGL Linux distribution with a selected graphical runtime and application set. One kernel supplies the local system; communication with another ECU uses the configured vehicle-data and network interfaces.

![Basic AGL software composition: a selected Flutter IVI, Qt IVI, or Flutter Cluster application above profile-specific runtime and services, one Linux kernel, and the target board.](../../assets/diagrams/basic-system.svg)

| Demo | Application and runtime | Important boundaries |
| --- | --- | --- |
| Flutter IVI | Flutter homescreen and embedder | Infotainment applications use platform graphics, audio, lifecycle, and vehicle-data services. |
| Qt IVI | Qt homescreen and Qt applications | The Qt runtime changes the UI implementation; launcher and service integration still need the matching image. |
| IVI-based Flutter Cluster | Flutter dashboard on the compositor image family | The recipe selects cluster and VSS/KUKSA components; it does not install the entire IVI demo application set. |

The [AGL compositor](../../components/services/graphics/agl-compositor.md) manages graphical surfaces. Basic IVI audio uses [PipeWire and WirePlumber](../../components/services/sound/pipewire-wireplumber.md). Read [Application Framework](../../components/framework/lifecycle/application-framework.md) for lifecycle integration and [service relationships](../../components/services/runtime.md) for vehicle-data flow.

Software composition is controlled by the [image recipes](../build/common/reference/images.md) and [Yocto layers](../build/common/layers/overview.md). Do not infer that every Basic target includes every IVI service. Preconfigured multi-board variants can move vehicle-data responsibilities between IVI, cluster, and gateway systems.

Continue with the [Basic portfolio](../portfolio/basic/index.md) or [Basic build](../build/basic/index.md).
