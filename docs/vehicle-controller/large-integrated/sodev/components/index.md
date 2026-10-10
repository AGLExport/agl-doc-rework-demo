---
title: AGL Components
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL Components

SoDeV combines platform domains, guest systems and graphical integration. The AGL guest guidance uses `master`; external hypervisor and board workspaces retain their own dependency configuration. The selected workspace determines which components run in the control, driver and guest domains.

- [Platform extension](platform-extensions/index.md) explains Unified HMI and the relationship between guest graphics and device backends.
- [Architecture](../architecture/index.md) explains the domain roles and VirtIO boundaries.
- [Create and Run Guest VM](../customize/guest-vm/index.md) explains integration of AGL master guest artifacts.

For services installed inside an AGL guest, consult the [shared component catalog](../../../distributed/agl-distribution/components/index.md) and that guest's actual recipe. A host or driver-domain service is not automatically available through a guest API.
