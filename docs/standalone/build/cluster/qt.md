---
title: "Qt based Cluster"
content_status: authored
---

# Qt based Cluster

This route builds the dedicated Qt Instrument Cluster reference profile, using `cluster-refgui` and the cluster service. It differs from the IVI-derived `agl-cluster-demo-qt` image in the general image catalog.

1. Complete [Common part](../common.md).
2. Follow the board setup in the [cluster profile guide](../../../integrated/containers/build-guide.md). That guide's `agl-ic-container` feature also provides the standalone target.
3. Choose its **standalone Instrument Cluster** option and build:

```sh
bitbake agl-instrument-cluster-standalone-demo
```

4. Deploy the matching WIC image and check the guide's display requirements.

Read [Instrument Cluster reference GUI (Qt)](../../../components/applications/cluster-dashboard.md) for demo/CAN behavior and [Instrument Cluster service](../../../components/services/cluster/cluster-service.md) for signal handling. A standalone target does not require you to select an IVI-container image.
