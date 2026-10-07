---
title: "KVM based integration"
content_status: authored
---

# KVM based integration

KVM based integration provides another example of the SoDeV approach to consolidating automotive functions. The AGL KVM demo combines IVI and Instrument Cluster virtual machines on a Linux host using KVM and QEMU.

Guest images have their own kernels and userlands. Host configuration controls virtual devices, display and input access, and networking. The imported [KVM image catalog](../../integrated/kvm/images.md) describes reference-hardware assumptions and the demo's internal network addresses; standard and preconfigured variants place services differently.

Continue with [KVM based integration development](../../integrated/kvm/index.md) and [Build Platform](../../integrated/kvm/build.md). Select a compatible host and guest set from the same release.
