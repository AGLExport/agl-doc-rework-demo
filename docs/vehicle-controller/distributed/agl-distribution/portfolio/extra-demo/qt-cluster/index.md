---
title: Qt based Cluster demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Qt based Cluster demo

The Qt cluster demo uses `cluster-refgui` and `cluster-service` on a minimal cluster-oriented userland. The reference GUI renders with Qt EGLFS rather than the IVI homescreen and compositor workflow.

| Setting | Selection |
| --- | --- |
| Features | `agl-demo agl-ic` |
| Image | `agl-instrument-cluster-standalone-demo` |
| GUI service | `cluster.service` |
| Vehicle-data service | `cluster-service.service` |

Follow [Extra setup](../../../build/extra/setup/index.md), [image build](../../../build/extra/image/index.md), and [deployment](../../../build/extra/deploy/index.md). The [detailed Qt cluster guide](../../../build/extra/reference/cluster/qt.md) includes feature rationale, output names, and runtime checks.

See [Instrument Cluster reference GUI (Qt)](../../../components/reference-applications/cluster-dashboard/index.md) and [Instrument Cluster service](../../../components/services/cluster/cluster-service/index.md) before replacing demo signal input. This target is separate from the IVI-derived `agl-cluster-demo-qt` variant in the image catalog.
