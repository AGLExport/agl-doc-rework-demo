---
title: Build Platform
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build Platform

Build the master KVM host and guest images as one configuration. Start with [KVM demo images](../reference/images.md), [host preparation](../../../distributed/agl-distribution/build/reference/common/prepare-host.md) and [Download AGL source](../../../distributed/agl-distribution/build/reference/common/download-source.md).

## Initialize and inspect the profile

Use a fresh shell and a host machine supported by the KVM configuration. This example selects the reference H3ULCB machine; complete its [R-Car Gen3 prerequisites](../../../distributed/agl-distribution/build/reference/common/hardware/renesas-rcar-gen3.md) first.

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m h3ulcb -b build-kvm-h3ulcb agl-demo agl-kvm
bitbake-getvar -r agl-kvm-demo GUEST_MACHINE
bitbake-getvar -r agl-kvm-demo GUEST_IMAGES
bitbake-getvar -r agl-kvm-demo QEMU_GUEST_CONFIGS
```

The [master KVM feature](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/conf/include/agl-kvm.inc?h=master) enables the guest multiconfig. The [host recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/recipes-platform/images/agl-kvm-demo.bb?h=master) selects Flutter IVI and Cluster guest targets and stages their artifacts.

## Build and deploy

```sh
bitbake agl-kvm-demo
bitbake-getvar -r agl-kvm-demo DEPLOY_DIR_IMAGE
bitbake-getvar -r agl-kvm-demo IMAGE_LINK_NAME
```

Follow the board's host flashing and boot procedure with the resulting artifacts. Confirm the QEMU guests start, then check the IVI UI, Cluster UI and the broker connection between them. Record the resolved master manifest, host machine, guest machine, guest targets and QEMU configuration.

Display/input devices and network endpoints are configuration-specific. Inspect their packages in the selected checkout when adapting another board. Use [Troubleshooting](../../../../troubleshooting/index.md) to collect separate host/guest logs. This source-reviewed route does not report a new board runtime test.
