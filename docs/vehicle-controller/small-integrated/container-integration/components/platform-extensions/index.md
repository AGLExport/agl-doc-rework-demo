---
title: Platform extension
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Platform extension

Container integration uses host services to coordinate guests and physical resources.

| Extension | Purpose |
| --- | --- |
| [DRM lease manager](drm-lease-manager/index.md) | Assign display resources to guest graphics clients. |
| [Container Manager](container-manager/index.md) | Configure, start, stop, and switch guest containers. |

Use the [architecture](../../architecture/index.md) to identify host and guest responsibilities. Read [global manager configuration](container-manager/reference/global.md) and [container configuration](container-manager/reference/containers.md) before changing resource allocation.

Build a working [integration profile](../../build/index.md) before customizing [guest containers](../../customize/guest-container/index.md).
