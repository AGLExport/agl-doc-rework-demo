---
title: "KVM based integration"
content_status: authored
---

# KVM based integration

KVM based integration is a small-scale integrated system that combines IVI and Instrument Cluster virtual machines on a Linux host using KVM and QEMU. Each guest has its own kernel and userland. Host configuration controls virtual devices, display and input access, and networking.

Keep image variants, service placement, and internal networking together. The [KVM demo images](images.md) describe reference-hardware assumptions and the standard and preconfigured variants.

- [Build Platform](build.md)

## Further reading

- [KVM demo images](images.md)
