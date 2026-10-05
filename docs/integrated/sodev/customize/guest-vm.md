---
title: "Create and Run Guest VM"
content_status: authored
---

# Create and Run Guest VM

Start with a working [SoDeV build](../build.md). Customization must account for the workspace's hypervisor, board, and device-backend configuration.

1. Select the guest's purpose. The [virtio guest guide](../virtio-guest.md) explains the generic AGL `virtio-aarch64` target.
2. Inspect existing guest recipes and integration configuration. The [Sparrow Hawk build script](https://github.com/automotive-grade-linux/sodev-demo-workspace/blob/main/build.sh) shows how AGL guest images are built before system assembly.
3. Add the guest kernel/root filesystem and define memory, virtual CPUs, storage, networking, and required VirtIO backends in the target configuration. Preserve compatible guest/kernel pins.
4. Rebuild and deploy through the workspace. The [Raspberry Pi options](https://github.com/automotive-grade-linux/sodev-demo-workspace-rpi#build-configuration) select existing guests; that differs from defining a new workload.
5. Inspect domains and the guest console from the domain that owns the Xen toolstack:

```sh
xl list
xl console <domain-name>
```

These commands follow the [Xen guest-management guide](https://handbook.xenproject.org/users/guests/index.html). The toolstack can be in a control or driver domain depending on the workspace; do not assume it is inside the application guest.

Verify device access, connectivity, and restart behavior. Collect host and guest logs separately. The supplied material does not define a board-independent SoDeV guest manifest; use the selected workspace as the configuration authority.
