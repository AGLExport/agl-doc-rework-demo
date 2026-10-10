---
title: AGL Virtual Car definition
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Virtual Car definition

The AGL virtual car provides a common CAN-message and signal definition for demonstrations. It lets demo controllers, CAN providers and reference applications exchange consistent vehicle, body and sensor data.

Read [CAN message definition](can-messages/index.md), then [AGL virtual car](can-messages/agl-virtual-car/index.md) for the signal specification. The supporting [vehicle](can-messages/agl-virtual-car/reference/signals/vehicle.md), [body](can-messages/agl-virtual-car/reference/signals/body.md) and [sensor](can-messages/agl-virtual-car/reference/signals/sensors.md) pages provide detailed definitions.

Match the DBC and VSS mapping used by the selected master image. A CAN frame describes bus data; a VSS path describes the vehicle signal exposed through the data service. [Connected Gateway architecture](../../vehicle-data/connected-gateway/architecture/index.md) explains that conversion.

Use [Demo Control Panel](../tools/demo-control/panel/index.md) or [CARLA with AGL](../tools/demo-control/carla/index.md) to supply demonstration inputs. [Development & Usage](../index.md) provides the surrounding development workflow.
