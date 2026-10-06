---
title: "Build Platform"
content_status: authored
---

# Build Platform

Use the [KVM image catalog](images.md) to select a complete host/guest configuration. The supplied catalog targets Renesas H3ULCB hardware and documents hard-coded networking and input-device assumptions.

1. Complete [Common part](../../standalone/build/common.md) and choose the matching release and board.
2. Enable `agl-kvm` during initialization. The [feature reference](../../standalone/build/common/initialize-build.md) describes multiconfig KVM/QEMU support.
3. For the catalog's base combination, build:

```sh
bitbake agl-kvm-demo
```

4. Follow the board's host boot procedure and check the IVI/cluster guests. The base topology uses host `172.16.10.1`, IVI `172.16.10.2`, and cluster `172.16.10.3`.

Preconfigured variants move services among the host, IVI guest, and gateway. Retain those targets and configuration as a set. The source does not provide generic deployment for other boards; adapt host configuration and validate device access before selecting another target.
