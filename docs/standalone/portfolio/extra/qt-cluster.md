---
title: "Qt based Cluster demo"
content_status: authored
---

# Qt based Cluster demo

The Qt cluster demo uses `cluster-refgui` and `cluster-service` on a minimal cluster-oriented userland. The reference GUI renders with Qt EGLFS rather than the IVI homescreen and compositor workflow.

| Setting | Selection |
| --- | --- |
| Features | `agl-demo agl-ic` |
| Image | `agl-instrument-cluster-standalone-demo` |
| GUI service | `cluster.service` |
| Vehicle-data service | `cluster-service.service` |

Follow [Extra setup](../../build/extra/setup.md), [image build](../../build/extra/image.md), and [deployment](../../build/extra/deploy.md). The [detailed Qt cluster guide](../../build/cluster/qt.md) includes feature rationale, output names, and runtime checks.

See [Instrument Cluster reference GUI (Qt)](../../../components/applications/cluster-dashboard.md) and [Instrument Cluster service](../../../components/services/cluster/cluster-service.md) before replacing demo signal input. This target is separate from the IVI-derived `agl-cluster-demo-qt` variant in the image catalog.
