---
title: "Build"
content_status: authored
---

# Build

Select a published SoDeV workspace for your board before building. SoDeV workspaces have their own orchestration and pinned dependencies; the standalone distribution's `master` examples do not replace those pins.

## Sparrow Hawk workspace

The [official README](https://github.com/automotive-grade-linux/sodev-demo-workspace) lists `moulin` v0.28 and `ninja` as prerequisites and provides board-specific deployment. Install its prerequisites, then:

```sh
git clone --recurse-submodules https://github.com/automotive-grade-linux/sodev-demo-workspace
cd sodev-demo-workspace
./build.sh
```

The [build script](https://github.com/automotive-grade-linux/sodev-demo-workspace/blob/main/build.sh) coordinates AGL guest builds and target integration. Record the workspace commit and submodule revisions; do not substitute an unrelated AGL branch.

## Raspberry Pi workspace

The [Raspberry Pi workspace](https://github.com/automotive-grade-linux/sodev-demo-workspace-rpi) supplies a separate Docker-based build and board/guest selection. Read its current requirements and use `./build.sh -h` to check options at your revision. Its documented default is a guest-less control/driver-domain image; a visible cockpit needs selected guest options.

Follow that workspace's flashing and boot instructions for the exact board. Confirm the host domains and requested guests started. Continue with [Create and Run Guest VM](customize/guest-vm.md) when changing guest composition.
