---
title: Deploy to board
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Deploy to board

Deploy the output from [Build target image](../image/index.md) with the chosen profile's complete board procedure.

| Profile | Deployment and expected result |
| --- | --- |
| Qt cluster | [Qt cluster guide](../reference/cluster/qt.md): write the board-specific WIC image and confirm the EGLFS gauges. |
| Slint cluster | [Slint guide](../reference/cluster/slint.md): write its WIC image and attach the documented display. |

Raspberry Pi output uses `raspberrypi4-64` for Pi 4 and `raspberrypi5` for Pi 5. Verify the compressed image's name before decompression and writing. For NanoPC-T6 or Sparrow Hawk, follow the matching board/profile procedure.

## Verify startup

Use the serial console to check boot. Run only the checks for the deployed profile.

Qt cluster:

~~~sh
systemctl status cluster-service.service cluster.service
journalctl -b -u cluster-service.service -u cluster.service
~~~

Slint cluster:

~~~sh
systemctl status cluster-service.service agl-slint-cluster.service
journalctl -b -u cluster-service.service -u agl-slint-cluster.service
~~~

Deploy and verify Momi using the [Container integration Momi guide](../../../../../small-integrated/container-integration/demo-image/momi-ivi/index.md), including its host and guest checks.

Record the source revision, profile, machine, image filename, and logs. Read [Troubleshooting](../../../../../../troubleshooting/index.md) before changing graphics devices or guest registration.
