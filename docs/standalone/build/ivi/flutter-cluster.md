---
title: "IVI based Flutter Cluster"
content_status: authored
---

# IVI based Flutter Cluster

This cluster image belongs to the IVI-derived demo image family. It uses the Flutter cluster application; it is distinct from the dedicated Qt and Slint cluster-profile targets. See [Flutter Cluster](../../../components/applications/flutter-cluster.md).

Follow [Common part](../common.md) first. Initialize your selected machine with the `agl-demo` feature, then run this command in the initialized build shell:

```sh
bitbake agl-cluster-demo-flutter
```

Use the selected board's deployment instructions and output filenames in `tmp/deploy/images/<machine>/`. Confirm the UI starts and record the build identifier. The [image catalog](../common/reference/images.md) describes variants; do not select a preconfigured or guest image without its integration guide.
