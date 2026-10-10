---
title: Create and Run Guest Container
content_status: authored
agl_branch: master
last_reviewed: '2026-10-10'
---

# Create and Run Guest Container

Start from a working [container build](../../build/index.md). A guest needs a root filesystem and host-side configuration; packaging an application does not register a guest with Container Manager.

1. Follow the **additional IVI guest** procedure in the [profile guide](../../reference/build-guide.md). It describes the `agl-demo` and `agl-container-guest-demo` features and Qt/Flutter image targets.
2. Deploy the guest files to the storage layout for your profile.
3. Define its identity, role, root filesystem, mounts, devices, graphics/audio access, and resources in the [container configuration](../../components/platform-extensions/container-manager/reference/containers.md). Include it in the [manager-wide configuration](../../components/platform-extensions/container-manager/reference/global.md).
4. Boot the host and inspect registered guests:

```sh
cmcontrol --get-guest-list
```

5. For the guide's registered Flutter IVI guest, its switching sequence is:

```sh
cmcontrol --change-active-guest-name=agl-flutter-ivi-demo
cmcontrol --shutdown-guest-role=ivi
```

The second command shuts down the active IVI guest so the requested replacement can start. Check that the selected name exists in your configuration.

Verify the UI, audio, network, and restart behavior. Use [Container Manager](../../components/platform-extensions/container-manager/index.md) for lifecycle details and [Troubleshooting](../../../../../troubleshooting/index.md) for logs.
