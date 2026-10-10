---
title: AGL Virtual Car definition
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Virtual Car definition

The AGL virtual car provides a common CAN-message and signal definition for demonstrations. It lets demo controllers, CAN providers and reference applications exchange consistent vehicle, body and sensor data.

Read [CAN message definition](../components/tools/virtual-car/index.md), then [AGL virtual car](../components/tools/virtual-car/virtual-car.md) for the signal specification. The supporting [vehicle](../components/tools/virtual-car/signals/vehicle.md), [body](../components/tools/virtual-car/signals/body.md) and [sensor](../components/tools/virtual-car/signals/sensors.md) pages provide detailed definitions.

Match the DBC and VSS mapping used by the selected master image. A CAN frame describes bus data; a VSS path describes the vehicle signal exposed through the data service. [Connected Gateway architecture](../vehicle-data/gateway/architecture.md) explains that conversion.

Use [Demo Control Panel](../components/tools/demo-control/panel.md) or [CARLA with AGL](../components/tools/demo-control/carla.md) to supply demonstration inputs. [Development & Usage](../development/index.md) provides the surrounding development workflow.
