---
title: "IVI based Flutter Cluster demo"
content_status: authored
---

# IVI based Flutter Cluster demo

The IVI-derived Flutter Cluster demo displays vehicle information through `flutter-cluster-dashboard`. It is an example of an Instrument Cluster using COVESA VSS and KUKSA vehicle data.

The target is `agl-cluster-demo-flutter`. It builds on the AGL compositor image family and selects a cluster dashboard instead of the IVI homescreen. It is distinct from the dedicated Qt and Slint cluster profiles in [Extra demo system](../extra/index.md).

- [Flutter Cluster application](../../../components/applications/flutter-cluster.md).
- [Basic architecture](../../architecture/basic.md).
- [Setup](../../build/basic/setup.md), [build](../../build/basic/image.md), and [deployment](../../build/basic/deploy.md).
- [Target-specific build notes](../../build/ivi/flutter-cluster.md).

The [upstream image recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/recipes-platform/images/agl-cluster-demo-flutter.bb) selects the dashboard and vehicle-data components. Read the [preconfigured image topology](../../build/common/reference/images.md#2-preconfigured-demo-images) before placing the databroker on another ECU.
