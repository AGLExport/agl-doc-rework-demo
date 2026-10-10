---
title: IVI based Flutter Cluster
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# IVI based Flutter Cluster

This cluster image belongs to the IVI-derived demo image family. It uses the Flutter cluster application; it is distinct from the dedicated Qt and Slint cluster-profile targets. See [Flutter Cluster](../../../../components/reference-applications/flutter-cluster/index.md).

Follow [Common part](../../../reference/common.md) first. Initialize your selected machine with the `agl-demo` feature, then run this command in the initialized build shell:

```sh
bitbake agl-cluster-demo-flutter
```

Use the selected board's deployment instructions and output filenames in `tmp/deploy/images/<machine>/`. Confirm the UI starts and record the build identifier. The [image catalog](../../../reference/common/reference/images.md) describes variants; use the matching integration guide when selecting a guest image or changing service placement.
