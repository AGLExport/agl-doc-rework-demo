---
title: "Build Container integration"
content_status: authored
---

# Build Container integration

Build the host and guests as one selected integration profile. The [detailed guide](build-guide.md) covers Sparrow Hawk, NanoPC-T6, and Raspberry Pi 4/5 and describes variants and storage layouts.

1. Complete [host/source preparation](../../standalone/build/common.md).
2. Select a board and initialize its `agl-ic-container` build using the detailed guide.
3. Choose the profile option you need. The integrated demo target is:

```sh
bitbake agl-instrument-cluster-container-demo
```

The guide also lists `lxc-host-image-minimal` and the standalone cluster target; these serve different purposes.

4. Follow the matching assembly, storage, display, and deployment steps. Do not mix profile options.
5. On the target, list configured guests:

```sh
cmcontrol --get-guest-list
```

Check the cluster/IVI roles before switching guests. Continue with [Create and Run Guest Container](customize/guest-container.md) or read [Container Manager](../../components/extensions/container-manager.md).
