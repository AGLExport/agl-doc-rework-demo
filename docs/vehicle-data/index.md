---
title: Base platform for Vehicle Data Processing
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Base platform for Vehicle Data Processing

Vehicle-data applications acquire signals, convert them into a common representation and make them available to local applications or connected services. [Introduction](../home/index.md#vehicle-data-processing) explains the E2E choice of processing in the vehicle, network and cloud.

The [Connected Gateway](gateway/index.md) chapter describes AGL's vehicle-side reference platform. Its [Architecture](gateway/architecture.md) follows the master gateway demo recipe: CAN integration feeds a KUKSA databroker, and IVI, Cluster or other clients access vehicle signals using the configured network interfaces.

| Processing stage | Platform responsibility | Reference |
| --- | --- | --- |
| Acquisition | Receive CAN frames through the configured Linux interface | [CAN message definition](../components/tools/virtual-car/index.md) |
| Signal conversion | Decode the configured DBC and map values to VSS paths | [Connected Gateway architecture](gateway/architecture.md#can-to-vss-data-path) |
| Vehicle-side sharing | Publish vehicle signals through the databroker and configure its clients | [Gateway APIs](../components/api/gateway.md) |
| Edge and cloud integration | Select data, manage buffering and add the application's network/cloud connector | [E2E processing context](../home/index.md#vehicle-data-processing) |

The standard gateway demo supplies vehicle-side signal infrastructure. A cellular link, a cloud backend and application-specific analytics are additional integration choices. Evaluate the resulting data quality, response time, connectivity behavior and resource use across the complete path.

For workload placement and guest isolation, use [Base platform for Vehicle Controller](../vehicle-controller/index.md). To generate demonstration inputs, use [AGL Development tools](../components/tools/index.md).
