---
title: "Instrument Cluster"
content_status: authored
---

# Instrument Cluster

AGL provides an Instrument Cluster platform with demo software for presenting vehicle information to the driver. The Flutter, Qt, and Slint implementations have different platform and userland requirements.

| Implementation | Platform characteristics | Read next |
| --- | --- | --- |
| Flutter | Built on the IVI platform. This cluster demonstrates the use of COVESA Vehicle Signal Specification (VSS) for vehicle data. | [IVI based Flutter Cluster](../../standalone/build/ivi/flutter-cluster.md) and [Flutter Cluster application](../../components/applications/flutter-cluster.md) |
| Qt | The dedicated Qt cluster profile starts from minimal userland, providing a foundation for a small-footprint cluster environment. | [Qt based Cluster](../../standalone/build/cluster/qt.md) and [Instrument Cluster reference GUI (Qt)](../../components/applications/cluster-dashboard.md) |
| Slint | An early example of an Instrument Cluster implemented in Rust using the Slint UI toolkit. | [Slint based Cluster](../../standalone/build/cluster/slint.md) |

[COVESA VSS](https://github.com/COVESA/vehicle_signal_specification) defines vehicle signals independently of the GUI toolkit. The [image catalog](../../standalone/build/common/reference/images.md) distinguishes the IVI-derived cluster targets from the dedicated cluster profiles. The [Instrument Cluster service](../../components/services/cluster/cluster-service.md) describes the service used by the Qt reference GUI.

Choose the implementation before following a board's build guide; its kernel, userland, vehicle-data interface, and display configuration must match the selected profile.
