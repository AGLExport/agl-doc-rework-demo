---
title: "Base platform for integrated system"
content_status: authored
---

# Base platform for integrated system

AGL develops and provides a base platform for automotive integrated systems. It brings multiple functions into one system by integrating one or more AGL Linux distributions and/or other platforms.

The integration defines how workloads share computing resources, access devices, exchange data, and start or stop. A system can use containers with a shared host kernel or virtual machines with separate guest kernels, depending on its integration approach.

- [SoDeV](sodev.md) provides the software-defined vehicle reference platform and its official architecture.
- [Container integration](containers.md) provides lightweight Linux-based integration using isolated guest userlands.
- [KVM based integration](kvm.md) provides another example of the SoDeV approach using Linux virtual machines.

Continue with [AGL integrated system development](../../integrated/index.md) for platform builds and guest customization.
