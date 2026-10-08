---
title: "Basic demo system"
content_status: authored
---

# Basic demo system

AGL provides an In-Vehicle Infotainment (IVI) platform with demo software and support for multiple GUI toolkits. Flutter is the current mainstream GUI toolkit for AGL IVI, and Qt 6 is also supported. These Basic demos use the IVI and compositor image family; select the GUI toolkit and image together so that the required runtime and services are installed.

The Flutter-based Instrument Cluster is built on the IVI platform and demonstrates vehicle data using COVESA Vehicle Signal Specification (VSS). It selects a cluster dashboard instead of an infotainment homescreen, with its own application and image target.

| Demo | Image target | Main role |
| --- | --- | --- |
| [Flutter IVI demo](flutter-ivi.md) | `agl-ivi-demo-flutter` | Infotainment with the Flutter homescreen |
| [Qt IVI demo](qt-ivi.md) | `agl-ivi-demo-qt` | Infotainment with Qt applications |
| [IVI based Flutter Cluster demo](flutter-cluster.md) | `agl-cluster-demo-flutter` | Instrument Cluster using Flutter and VSS/KUKSA vehicle data |

Read [Basic architecture](../../architecture/basic.md), then follow [Setup build environment](../../build/basic/setup.md), [Build target image](../../build/basic/image.md), and [Deploy to board](../../build/basic/deploy.md). The [original IVI build guides](../../build/ivi/index.md) provide supporting target-specific notes.

Use [Flutter application](../../applications/flutter.md) or [Qt application](../../applications/qt.md) for application development, and [AGL Reference Applications](../../../components/applications/index.md) for the supplied homescreens and Cluster GUI. [COVESA VSS](https://github.com/COVESA/vehicle_signal_specification) defines the signals used by the Flutter Cluster.
