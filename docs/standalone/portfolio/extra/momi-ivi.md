---
title: "Momi IVI demo"
content_status: authored
---

# Momi IVI demo

Momi IVI is a small Qt/QML infotainment demonstration used as a container guest. It demonstrates graphics, sound, media, and network access without the full standard IVI application stack.

| Application | Purpose |
| --- | --- |
| [Momi Screen](../../../components/applications/momi-screen.md) | Homescreen and application selection |
| [Momi navigation](../../../components/applications/momi-navigation.md) | Map and navigation example |
| [Momi Weather](../../../components/applications/momi-weather.md) | Network-connected weather example |
| [Momi Player](../../../components/applications/momi-player.md) | Media playback example |

The [guest recipe](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/meta-agl-ic-container/recipes-platform/images/guest-image-ivi-demo.bb) is `guest-image-ivi-demo`. The type 2a [container host recipe](https://git.automotivelinux.org/AGL/meta-agl-devel/tree/meta-agl-ic-container/recipes-platform/images/agl-instrument-cluster-container-demo.bb) builds it together with the cluster guest.

Use `agl-ic-container` and build `agl-instrument-cluster-container-demo` for a complete bootable integration. A guest root filesystem alone does not supply the host kernel, container registration, or DRM leases.

Follow [Extra setup](../../build/extra/setup.md), [image build](../../build/extra/image.md), and [deployment](../../build/extra/deploy.md). Read [Container integration architecture](../../../integrated/containers/architecture.md) and the [detailed type 2a guide](../../../integrated/containers/build-guide.md) for storage and display allocation. Momi's Qt/multimedia package group includes PulseAudio; do not assume it has the same audio stack as the Basic IVI demos.
