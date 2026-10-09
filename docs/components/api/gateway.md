---
title: "Gateway APIs"
content_status: authored
---

# Gateway APIs

The gateway demo hosts the KUKSA.val databroker and CAN-input integration described in the [image catalog](../../standalone/build/common/reference/images.md#agl-gateway-demo). Preconfigured variants participate in a coordinated IVI/cluster network.

| Need | Reference |
| --- | --- |
| Databroker placement and networking | [Preconfigured images](../../standalone/build/common/reference/images.md#2-preconfigured-demo-images) |
| Demo CAN data | [Virtual Car CAN definition](../tools/virtual-car/index.md) |
| Generate demonstration data | [Demo Control Panel](../tools/demo-control/panel.md) |
| Platform services | [AGL Services](../services/index.md) |

The imported source does not define an independent gateway request/response API. Use the selected release's [KUKSA interface documentation](https://github.com/eclipse-kuksa/kuksa-databroker) and the feeder's CAN definitions. Keep signal names and schema versions consistent between gateway and clients.
