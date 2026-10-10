---
title: Connected Gateway
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Connected Gateway

The AGL Connected Gateway reference image, `agl-gateway-demo`, provides vehicle-signal acquisition and sharing. It brings CAN input into the KUKSA databroker and allows configured IVI, Cluster and other clients to access VSS data. The [master image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-gateway-demo.bb?h=master) is the source for the image's composition.

Read [Architecture](architecture.md) for the data path, installed components and configuration boundaries. Use the [gateway image catalog](../../distributed/build/common/reference/images.md#agl-gateway-demo) and [coordinated demo configuration](../../distributed/build/common/reference/images.md#coordinated-demo-configuration) when selecting the image and client endpoints. Shared source and build preparation remains in [Build AGL system](../../distributed/build/index.md).

This role can run on a separate gateway ECU while providing signals to other systems. Vehicle-side processing can also be incorporated into an integrated system with suitable device and network access. The [Vehicle Controller platform comparison](../../vehicle-controller/index.md) explains those placement choices.

Use [Gateway APIs](../../components/api/gateway.md) for interface references, the [AGL Virtual Car definition](../../virtual-car/index.md) for demonstration CAN signals and [Demo Control](../../components/tools/demo-control/index.md) to generate inputs. Keep the image, DBC/VSS mappings, client protocols and network configuration aligned to one resolved master source baseline.
