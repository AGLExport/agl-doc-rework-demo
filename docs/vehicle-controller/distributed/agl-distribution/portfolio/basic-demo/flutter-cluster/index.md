---
title: IVI based Flutter Cluster demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# IVI based Flutter Cluster demo

The IVI-derived Flutter Cluster demo displays vehicle information through `flutter-cluster-dashboard`. It is an example of an Instrument Cluster using COVESA VSS and KUKSA vehicle data.

The target is `agl-cluster-demo-flutter`. It builds on the AGL compositor image family and selects a cluster dashboard instead of the IVI homescreen. It is distinct from the dedicated Qt and Slint cluster profiles in [Extra demo system](../../extra-demo/index.md).

- [Flutter Cluster application](../../../components/reference-applications/flutter-cluster/index.md).
- [Basic architecture](../../../architecture/basic-demo/index.md).
- [Setup](../../../build/basic/setup/index.md), [build](../../../build/basic/image/index.md), and [deployment](../../../build/basic/deploy/index.md).
- [Target-specific build notes](../../../build/basic/reference/ivi/flutter-cluster.md).

The [upstream image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-cluster-demo-flutter.bb) selects the dashboard and vehicle-data components. Read the [coordinated image configuration](../../../build/reference/common/reference/images.md#coordinated-demo-configuration) before placing the databroker on another ECU.
