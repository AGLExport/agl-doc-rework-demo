---
title: "Flutter IVI demo"
content_status: authored
---

# Flutter IVI demo

Build the Flutter IVI demo with its integrated homescreen. See [Flutter IVI demo](../../../start/prebuilt/flutter.md) for the user-facing overview and [Flutter IVI homescreen](../../../components/applications/flutter-homescreen.md) for the application.

Follow [Common part](../common.md) first. Initialize your selected machine with the `agl-demo` feature, then run this command in the initialized build shell:

```sh
bitbake agl-ivi-demo-flutter
```

Use the selected board's deployment instructions and output filenames in `tmp/deploy/images/<machine>/`. Confirm the UI starts and record the build identifier. The [image catalog](../common/reference/images.md) describes variants; do not select a preconfigured or guest image without its integration guide.
