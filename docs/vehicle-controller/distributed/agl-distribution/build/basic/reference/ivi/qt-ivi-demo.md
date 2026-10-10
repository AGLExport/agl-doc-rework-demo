---
title: Qt IVI demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Qt IVI demo

Build the Qt IVI demo with its homescreen, launcher, and Qt applications. See [Qt IVI homescreen](../../../../components/reference-applications/qt-homescreen/index.md) and [Qt application](../../../../applications/qt/index.md).

Follow [Common part](../../../reference/common.md) first. Initialize your selected machine with the `agl-demo` feature, then run this command in the initialized build shell:

```sh
bitbake agl-ivi-demo-qt
```

Use the selected board's deployment instructions and output filenames in `tmp/deploy/images/<machine>/`. Confirm the UI starts and record the build identifier. The [image catalog](../../../reference/common/reference/images.md) describes variants; use the matching integration guide when selecting a guest image or changing service placement.
