---
title: Flutter IVI demo
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Flutter IVI demo

Build the Flutter IVI demo with its integrated homescreen. See [Flutter IVI demo](../../../../quick-start/prebuilt/reference/flutter.md) for the user-facing overview and [Flutter IVI homescreen](../../../../components/reference-applications/flutter-homescreen/index.md) for the application.

Follow [Common part](../../../reference/common.md) first. Initialize your selected machine with the `agl-demo` feature, then run this command in the initialized build shell:

```sh
bitbake agl-ivi-demo-flutter
```

Use the selected board's deployment instructions and output filenames in `tmp/deploy/images/<machine>/`. Confirm the UI starts and record the build identifier. The [image catalog](../../../reference/common/reference/images.md) describes variants; use the matching integration guide when selecting a guest image or changing service placement.
