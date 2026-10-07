---
title: "Platform extension"
content_status: authored
---

# Platform extension

Container integration uses host services to coordinate guests and physical resources.

| Extension | Purpose |
| --- | --- |
| [DRM lease manager](../../components/services/graphics/drm-lease-manager.md) | Assign display resources to guest graphics clients. |
| [Container Manager](../../components/extensions/container-manager.md) | Configure, start, stop, and switch guest containers. |

Use the [architecture](architecture.md) to identify host and guest responsibilities. Read [global manager configuration](../../components/extensions/container-settings/global.md) and [container configuration](../../components/extensions/container-settings/containers.md) before changing resource allocation.

Build a working [integration profile](build.md) before customizing [guest containers](customize/guest-container.md).
