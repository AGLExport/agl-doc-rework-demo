---
title: Table for APIs
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Table for APIs

Find the interface for the data or operation your application needs. Application explanations describe user behavior; API references describe software interaction.

| Area | Reference | Purpose |
| --- | --- | --- |
| Generic file data | [Redundancy file operation (librefop)](../generic/librefop/index.md) | Redundant file storage and recovery status. |
| IVI data | [Persistent storage API](../ivi/persistent-storage/index.md) | Retain demo settings across shutdown. |
| Dedicated cluster | [AGL Instrument Cluster API](../cluster/instrument-cluster-api/index.md) | Communicate with the cluster service. |
| Vehicle data on IVI/cluster/gateway | [Gateway APIs](../gateway/index.md) | Locate vehicle-data and CAN interfaces. |
| IVI demo backend interfaces | [AGL Services](../../services/index.md#ivi-demo-service-paths-on-master) | HVAC, audio mixer, radio and MPD client paths. |
| Window management | [The AGL compositor](../../services/graphics/agl-compositor/index.md) | Application surfaces and activation. |
| Audio | [Pipewire & Wireplumber](../../services/sound/pipewire-wireplumber/index.md) | Playback, capture, devices, and policy. |
| Application lifecycle | [Application Framework](../../application-framework/lifecycle-services/application-framework/index.md) | Application management and services. |
| Guest lifecycle | [Container Manager](../../../../../small-integrated/container-integration/components/platform-extensions/container-manager/index.md) | Manage configured containers. |

Check release-specific interface versions. The [original API coverage page](../reference/source-api-coverage.md) remains source material rather than a complete current catalog.
