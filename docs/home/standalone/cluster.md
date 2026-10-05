---
title: "Instrument Cluster"
content_status: authored
---

# Instrument Cluster

An Instrument Cluster presents vehicle information to the driver. AGL includes different cluster implementations; their image targets, display requirements, and service dependencies differ.

| Implementation | Read next |
| --- | --- |
| Qt reference GUI in the dedicated cluster profile | [Qt based Cluster](../../standalone/build/cluster/qt.md) |
| Rust application using Slint | [Slint based Cluster](../../standalone/build/cluster/slint.md) |
| Flutter cluster using the IVI-derived image family | [IVI based Flutter Cluster](../../standalone/build/ivi/flutter-cluster.md) |

The [Instrument Cluster reference GUI (Qt)](../../components/applications/cluster-dashboard.md) uses the [Instrument Cluster service](../../components/services/cluster/cluster-service.md) for vehicle signals. Choose the implementation before following a board's build guide.
