---
title: KVM demo images
source_path: 01_Getting_Started/03_Build_and_Boot_guide_Profile/02_KVM_Demo_Images.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# KVM demo images

This catalog follows the [master KVM image directory](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/recipes-platform/images/?h=master). Select the host and both guests together. Their configuration includes guest kernels, root filesystems, QEMU device assignments and network/service placement.

## Host and guest targets

| Target | Composition |
| --- | --- |
| `agl-ivi-demo-flutter-guest` | Flutter IVI guest, with cluster-support and remoting packages |
| `agl-cluster-demo-flutter-guest` | Flutter Cluster guest, with a remote KUKSA client configuration |
| `agl-kvm-demo` | Linux KVM/QEMU host that builds and stages both guests |

The [IVI guest recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/recipes-platform/images/agl-ivi-demo-flutter-guest.bb?h=master) requires the regular Flutter IVI image and adds cluster-support, PipeWire remoting and compositor configuration. The [Cluster guest recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/recipes-platform/images/agl-cluster-demo-flutter-guest.bb?h=master) removes its local databroker feature and selects `kuksa-conf-kvm-demo`.

The [host recipe](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/recipes-platform/images/agl-kvm-demo.bb?h=master) defaults to these two guests through `GUEST_VM1_IMAGE`, `GUEST_VM2_IMAGE` and `GUEST_IMAGES`. It adds multiconfig dependencies and stages their ext4 images and kernels under `/var/lib/machines/`. QEMU configuration packages are derived from the selected guest names.

## Machine and resource configuration

The [master KVM feature include](https://git.automotivelinux.org/AGL/meta-agl-demo/tree/meta-agl-kvm-demo/conf/include/agl-kvm.inc?h=master) selects the `agl-kvm-guest` multiconfig and defaults `AGL_GUEST_MACHINE` to `virtio-aarch64`, with a hook for machine-specific overrides. Inspect the host machine, QEMU configuration, display/input assignments and guest broker endpoint in the resolved checkout before deployment.

The old `*-preconfigured` KVM targets are absent from this master image directory. For coordinated deployments, configure the current host/guest recipes and service endpoints. Use [Build Platform](build.md) for initialization and image inspection; a different board needs its own device and boot configuration.
