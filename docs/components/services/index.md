---
title: AGL Services
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Services

Applications depend on graphics, sound, policy, voice, and cluster services. Choose an area below, or use [Table for APIs](../api/table.md) for interface requirements.

- [Graphics](graphics/index.md)
- [Sound](sound/index.md)
- [Policies](policies/index.md)
- [Misc](misc/index.md)
- [Instrument Cluster](cluster/index.md)

## IVI demo service paths on master

The [master IVI service package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-ivi-services.bb?h=master) and [databroker package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-kuksa-val-databroker.bb?h=master) select the demo backends. Check the image's resolved recipe configuration before assuming a service is installed.

| Function | Backend and connection | Read next |
| --- | --- | --- |
| Vehicle signals | KUKSA.val databroker; VSS paths via gRPC | [Gateway vehicle-data interfaces](../api/gateway.md) |
| CAN mapping | kuksa-can-provider with DBC/VSS configuration | [Image and provider configuration](../../standalone/build/common/reference/images.md#coordinated-demo-configuration) |
| HVAC | agl-service-hvac consumes databroker actuator targets | [Flutter homescreen clients](../applications/flutter-homescreen.md) |
| Audio volume and routing controls | agl-service-audiomixer connects VSS controls to the audio stack | [PipeWire and WirePlumber](sound/pipewire-wireplumber.md) |
| Music | MPD protocol and playback streams | [Basic IVI architecture](../../standalone/architecture/basic.md) |
| Radio | agl-service-radio gRPC backend | [Basic IVI architecture](../../standalone/architecture/basic.md) |
| Application startup | applaunchd gRPC and systemd units | [Application startup](../framework/lifecycle/application-startup.md) |

These services can also run inside an AGL guest. Host/container/SoDeV extensions have their own execution and device boundaries, described in their system chapters.
