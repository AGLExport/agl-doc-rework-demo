---
title: "IVI architecture diagram sources and scope"
content_status: authored
---

# IVI architecture diagram sources and scope

The [Basic demo system architecture](basic.md) uses the supplied `agl-flutter-ivi-architecture.svg` and `agl-qt-ivi-architecture.svg` diagrams. Both identify their baseline as Salmon, cite sources from 2024 onward, and record a review date of 2026-10-08. They are source-derived illustrations, not official AGL architecture figures.

## What the diagrams describe

The diagrams compare the Flutter and Qt HMI/toolkit layers above a common AGL IVI platform. They separate application startup through applaunchd/systemd from compositor surface activation, then show vehicle-data, media/audio and kernel/device paths. They are logical component views rather than exhaustive image-package inventories.

The default deployment places the databroker on IVI. Preconfigured gateway variants can relocate it, and CAN/demo I/O is hardware-dependent. Cluster streaming and container boundaries are outside these diagrams. Use [Container integration architecture](../../integrated/containers/architecture.md) for the shared-kernel IC/IVI host topology.

## Sources

| Diagram area | Primary references |
| --- | --- |
| Image families and service placement | [Salmon demo image catalog](https://docs.automotivelinux.org/en/salmon/01_Getting_Started/02_Building_AGL_Image/07_Available_Demo_Images/) |
| Rendering and shell extensions | [Salmon AGL compositor documentation](https://docs.automotivelinux.org/en/salmon/06_Component_Documentation/02_agl_compositor/) |
| Application startup | [Salmon applaunchd README](https://git.automotivelinux.org/src/applaunchd/tree/README.md`h=salmon), [Application startup and applaunchd](../../components/framework/lifecycle/application-startup.md) |
| Flutter clients and configuration | [Salmon homescreen data providers](https://git.automotivelinux.org/apps/flutter-ics-homescreen/tree/lib/data/data_providers`h=salmon), [Flutter IVI homescreen](../../components/applications/flutter-homescreen.md) |
| Qt shell, launcher and service clients | [Qt IVI homescreen](../../components/applications/qt-homescreen.md), including its primary source links |
| Audio platform | [Pipewire & Wireplumber](../../components/services/sound/pipewire-wireplumber.md) |

## Version and deployment selection

This site's build guides target the branch defined in `mkdocs.yml`. The diagrams retain their explicit Salmon baseline. For a concrete image, use the recipes and configuration from the same checkout as the built target: [Flutter image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-flutter.bb), [Qt image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-ivi-demo-qt.bb), and [image catalog](../build/common/reference/images.md). Installed applications, optional hardware adapters and service locations can differ by variant.

Follow [Releases & migration](../../releases/index.md) when selecting a different branch or release.
