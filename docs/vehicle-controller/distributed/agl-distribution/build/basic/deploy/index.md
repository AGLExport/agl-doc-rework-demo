---
title: Deploy to board
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Deploy to board

Deploy the artifacts generated in [Build target image](../image/index.md), using the selected board's procedure. A WIC disk image, an ext4 filesystem, and a kernel serve different purposes.

| Target | Deployment procedure |
| --- | --- |
| QEMU x86-64 | [x86 build and boot guide](../../reference/common/hardware/x86.md): use matching kernel/filesystem artifacts and its QEMU command. |
| Raspberry Pi 4/5 | [Raspberry Pi build and boot guide](../../reference/common/hardware/raspberry-pi.md): decompress the selected WIC image and write the board's boot medium. |
| Another board | [Supported the other boards](../../other-boards/index.md): check its BSP, firmware, storage, and display requirements. |

Substitute the image selected in the Basic build table into the board guide. Do not flash a compressed archive directly or use an IVI image filename for the Flutter Cluster.

## Verify the running system

1. Observe boot on the serial console or QEMU console.
2. Confirm that the selected homescreen or cluster dashboard appears.
3. Check the network and any graphics, audio, or vehicle-data interfaces used by that demo.
4. Save the source revision, image filename, machine, and boot logs.

On the target console:

~~~sh
cat /etc/os-release
systemctl --failed
journalctl -b -p err
~~~

Use [Troubleshooting](../../../../../../troubleshooting/index.md) when the UI or a service fails. Continue with [Platform Customize](../../../customize/index.md) or [Application development](../../../applications/index.md) under Distributed system.
