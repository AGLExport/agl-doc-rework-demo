---
title: "Connected Gateway"
content_status: authored
---

# Connected Gateway

A connected gateway provides a place to receive and distribute vehicle data. The AGL demo image target is `agl-gateway-demo`; the image catalog describes a KUKSA.val databroker and a `kuksa-dbc-feeder` for CAN input.

In coordinated demonstrations, the IVI and cluster systems can obtain vehicle data from the gateway instead of running their own databroker. Use the [image catalog](../../standalone/build/common/reference/images.md#agl-gateway-demo) to check the topology and network configuration.

Read [Gateway APIs](../../components/api/gateway.md) for interface scope and [Virtual Car CAN definition](../../components/tools/virtual-car/index.md) for the demo CAN data.
