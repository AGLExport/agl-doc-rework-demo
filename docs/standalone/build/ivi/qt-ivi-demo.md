---
title: "Qt IVI demo"
content_status: authored
---

# Qt IVI demo

Build the Qt IVI demo with its homescreen, launcher, and Qt applications. See [Qt IVI homescreen](../../../components/applications/qt-homescreen.md) and [Qt application](../../applications/qt.md).

Follow [Common part](../common.md) first. Initialize your selected machine with the `agl-demo` feature, then run this command in the initialized build shell:

```sh
bitbake agl-ivi-demo-qt
```

Use the selected board's deployment instructions and output filenames in `tmp/deploy/images/<machine>/`. Confirm the UI starts and record the build identifier. The [image catalog](../common/reference/images.md) describes variants; do not select a preconfigured or guest image without its integration guide.
