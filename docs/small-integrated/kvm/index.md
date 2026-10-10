---
title: KVM based integration
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# KVM based integration

KVM based integration is a small-scale integrated system that combines IVI and Instrument Cluster virtual machines on a Linux host using KVM and QEMU. Each guest has its own kernel and userland. Host configuration controls virtual devices, display and input access, and networking.

Keep image variants, service placement, and internal networking together. The [master KVM demo images](images.md) describe host/guest composition and machine-specific configuration.

- [Build Platform](build.md)
