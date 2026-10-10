---
title: Gateway APIs
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Gateway APIs

The gateway demo hosts the KUKSA.val databroker and CAN-input integration described in the [image catalog](../../../build/reference/common/reference/images.md#agl-gateway-demo). Coordinated IVI/cluster deployments configure the current master images and their network endpoints.

| Need | Reference |
| --- | --- |
| Databroker placement and networking | [Coordinated demo configuration](../../../build/reference/common/reference/images.md#coordinated-demo-configuration) |
| Demo CAN data | [CAN message definition](../../../../../../development/virtual-car/can-messages/index.md) |
| Generate demonstration data | [Demo Control Panel](../../../../../../development/tools/demo-control/panel/index.md) |
| Platform services | [AGL Services](../../services/index.md) |

The imported source does not define an independent gateway request/response API. Use the component revision selected by the master recipe and its [KUKSA interface documentation](https://github.com/eclipse-kuksa/kuksa-databroker) and the CAN provider's DBC/VSS mappings. Keep signal names and schema versions consistent between gateway and clients.

[Connected Gateway architecture](../../../../../../vehicle-data/connected-gateway/architecture/index.md) is TBD.

## Current master interface sources

The [master databroker package group](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/packagegroups/packagegroup-agl-kuksa-val-databroker.bb?h=master) selects the broker, CAN provider and AGL mappings. Vehicle-data access is shared with IVI and Cluster clients; select the protobuf/API version from the broker recipe and component revision used by the resolved master manifest.

For a client, record the broker address, TLS/authorization settings and VSS paths. For CAN integration, record the interface name, DBC and mapping configuration. The [master default provider configuration](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-connectivity/kuksa-val/kuksa-can-provider-conf-agl/config.ini?h=master) is a concrete configuration reference. Use the [service catalog](../../services/index.md#ivi-demo-service-paths-on-master) to distinguish signal transport from the hardware-specific HVAC/audio backends.
