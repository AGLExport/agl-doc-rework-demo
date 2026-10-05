---
title: "Flutter Cluster"
content_status: authored
---

# Flutter Cluster

Flutter Cluster is the cluster reference application in the IVI-derived `agl-cluster-demo-flutter` image family. The [image catalog](../../standalone/build/common/reference/images.md#agl-cluster-demo-flutter) names its cluster dashboard application.

Use [IVI based Flutter Cluster](../../standalone/build/ivi/flutter-cluster.md) to build this family. The [Flutter instrument-cluster source](https://git.automotivelinux.org/apps/flutter-instrument-cluster/) is an implementation reference; application/package names vary by release.

For coordinated cockpits, check the [preconfigured topology](../../standalone/build/common/reference/images.md#2-preconfigured-demo-images) or [KVM guest configuration](../../integrated/kvm/images.md). Variants can obtain vehicle data from the IVI system or gateway.

This application is separate from [Instrument Cluster reference GUI (Qt)](cluster-dashboard.md) and the Slint profile. Match the image, services, and vehicle-signal source when comparing behavior.
