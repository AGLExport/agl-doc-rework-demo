---
title: Momi IVI demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Momi IVI demo

Momi is the minimal-footprint IVI example in the Extra portfolio. It uses Qt/QML applications in a container guest and has a different runtime composition from the full Flutter/Qt IVI demos.

| Portfolio distinction | Deployment |
| --- | --- |
| Lightweight IVI application set | Momi Screen, navigation, weather and player |
| Guest execution | Shares the container host kernel and receives leased display access |
| Complete bootable image | `agl-instrument-cluster-container-demo`, with Cluster and Momi guest filesystems |

The complete procedure is maintained under [Container integration > Demo image for container integration > Momi IVI demo](../../../small-integrated/containers/demo/momi-ivi.md). Use that master-based build and deployment route. Read [Extra architecture](../../architecture/extra.md) for the portfolio comparison and [Container integration architecture](../../../small-integrated/containers/architecture.md) for host/guest boundaries.
