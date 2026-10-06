---
title: "Build a virtio guest"
source_path: "01_Getting_Started/02_Building_AGL_Image/06_Building_the_AGL_Image/06_Building_for_Virtio.md"
content_status: adapted
---

# Build a virtio guest

The `virtio-aarch64` AGL machine builds an AArch64 guest for virtual hardware that provides virtio devices. This guide builds a guest, runs it with Yocto's QEMU wrapper, and shows a serial-console launch on an AArch64 AGL host. Hypervisor, graphics, and device availability must match the chosen host. For the complete integrated demo, use the [KVM build guide](../kvm/build.md).

## 1. Initialize the guest build

Complete [host preparation](../../standalone/build/common/prepare-host.md) and [source download](../../standalone/build/common/download-source.md). The latter defines `AGL_SOURCE` as the source checkout containing `meta-agl`.

```sh
cd "$AGL_SOURCE"
source meta-agl/scripts/aglsetup.sh -m virtio-aarch64 -b build-virtio-aarch64 agl-demo
```

The `-m` option selects the setup template, and `-b` selects a separate build directory. Add `-f` only when intentionally replacing existing configuration. See [build initialization](../../standalone/build/common/initialize-build.md).

## 2. Build a guest image

For a minimal guest:

```sh
bitbake agl-image-minimal
```

For a Qt IVI guest instead:

```sh
bitbake agl-ivi-demo-qt
```

Keep the guest's kernel and root filesystem from the same build. Inspect the actual deploy directory and formats rather than relying on a hard-coded recipe work directory:

```sh
bitbake-getvar -r agl-image-minimal DEPLOY_DIR_IMAGE
bitbake-getvar -r agl-image-minimal IMAGE_FSTYPES
```

Substitute `agl-ivi-demo-qt` if that is your guest. The build's deploy directory contains its `Image` kernel, root filesystem, and generated QEMU configuration. See [Yocto's variable inspection guide](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/debugging.html#viewing-variable-values).

## 3. Run the guest on a Linux PC

Restore the guest build environment if using a new shell:

```sh
source "$AGL_SOURCE/build-virtio-aarch64/agl-init-build-env"
runqemu virtio-aarch64 agl-image-minimal nographic slirp
```

Use the minimal image for a serial-console evaluation. For a graphical Qt guest, select that image and allow a graphical display:

```sh
runqemu virtio-aarch64 agl-ivi-demo-qt slirp
```

The generated `.qemuboot.conf` selects the guest kernel, filesystem, and devices. An x86-64 PC uses software emulation for an AArch64 guest. See [Yocto's QEMU guide](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/qemu.html#running-qemu) for host dependencies and display options.

## 4. Run a minimal guest on an AArch64 AGL host

Build and boot the host separately with its board-specific instructions, for example the [R-Car Gen3 guide](../../standalone/build/common/hardware/renesas-rcar-gen3.md). If the host image does not include QEMU, add this to that host build's `conf/local.conf` and rebuild:

```bitbake
IMAGE_INSTALL:append = " qemu"
```

For the guest, ensure its build generates an ext4 filesystem. If needed, add the following to the **guest** build's `conf/local.conf`, then rebuild `agl-image-minimal`:

```bitbake
IMAGE_FSTYPES:append = " ext4"
```

Copy the guest `Image` kernel and uncompressed `.ext4` filesystem from the guest deploy directory to the running host. Decompress `.ext4.xz` with `xz -dk` on the build host first if that is the supplied format. The example below assumes you have placed them at `/var/lib/agl-guests/minimal/Image` and `/var/lib/agl-guests/minimal/rootfs.ext4` on the AGL host. Use the matching files from your build and ensure adequate free storage.

On the **AGL host**, confirm QEMU is installed:

```sh
command -v qemu-system-aarch64
ls -lh /var/lib/agl-guests/minimal/Image /var/lib/agl-guests/minimal/rootfs.ext4
```

Start a serial-console guest using the filesystem as a virtual disk file:

```sh
qemu-system-aarch64 \
  -machine virt \
  -cpu cortex-a57 -m 2048 \
  -global virtio-mmio.force-legacy=false \
  -drive id=disk0,file=/var/lib/agl-guests/minimal/rootfs.ext4,if=none,format=raw \
  -device virtio-blk-device,drive=disk0 \
  -netdev user,id=net0 -device virtio-net-device,netdev=net0 \
  -object rng-random,filename=/dev/urandom,id=rng0 \
  -device virtio-rng-device,rng=rng0 \
  -nographic \
  -kernel /var/lib/agl-guests/minimal/Image \
  -append 'root=/dev/vda rw console=ttyAMA0 ip=dhcp'
```

This command uses software emulation and writes changes to the guest filesystem file. It does not require repartitioning the host's boot medium or modifying files inside BitBake's temporary rootfs directory. To discard guest disk changes on exit, add `-snapshot`.

For hardware acceleration on an AArch64 host with KVM enabled in the kernel and access to `/dev/kvm`, replace `-machine virt` with `-machine virt,accel=kvm` and replace `-cpu cortex-a57` with `-cpu host`. A KVM failure must be diagnosed against that host's kernel and QEMU version; the software-emulation command remains the starting point. The [QEMU Arm virt documentation](https://www.qemu.org/docs/master/system/arm/virt.html) describes CPU and accelerator support.

Log in using the guest image's configured account. Shut down from the guest with `poweroff`, or press `Ctrl+A`, then `X` to exit QEMU's `-nographic` session. For graphics and additional devices, use the generated QEMU configuration or the integrated KVM profile rather than assuming the minimal serial-console command supplies an IVI display.

## 5. Verify and record the result

Check the guest console, network, and required virtio devices. Record the guest build identifier, host board and kernel, QEMU version, complete command, and observed result. These commands have not been validated on target hardware as part of this documentation correction. See [Troubleshooting](../../troubleshooting/index.md).
