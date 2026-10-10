---
title: QEMU x86-64
source_path: 01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# QEMU x86-64

Use an x86-64 Linux host with QEMU 7.1 or newer, access to `/dev/kvm`, and a VNC client. This guide boots the Flutter IVI demo directly from its kernel and ext4 filesystem. Keep both files on the same release/build.

## Prepare the host and image

On Debian or Ubuntu, install the host tools:

```sh
sudo apt install qemu-system-x86 xz-utils tigervnc-viewer
```

For other host distributions, install the equivalent packages. The launch command uses QEMU's PulseAudio backend; a PulseAudio server or PipeWire's PulseAudio compatibility service must be running for sound. See the [QEMU audio options](https://www.qemu.org/docs/master/system/qemu-manpage.html) for available backends.

Download these two files from the [same artifact directory]({{ agl_download_base }}/latest/qemux86-64/deploy/images/qemux86-64/):

- [Compressed Flutter filesystem]({{ agl_download_base }}/latest/qemux86-64/deploy/images/qemux86-64/agl-ivi-demo-flutter-qemux86-64.ext4.xz)
- [Kernel (`bzImage`)]({{ agl_download_base }}/latest/qemux86-64/deploy/images/qemux86-64/bzImage)

`latest` moves as new builds are published. For repeatable evaluation, record the timestamped image filename and build directory, and download the matching kernel before that directory changes.

Copy the downloaded files into a boot directory, then decompress the filesystem:

```sh
mkdir -p ~/agl-demo
cp ~/Downloads/agl-ivi-demo-flutter-qemux86-64.ext4.xz ~/agl-demo/
cp ~/Downloads/bzImage ~/agl-demo/
cd ~/agl-demo
xz -dk agl-ivi-demo-flutter-qemux86-64.ext4.xz
```

The launch command needs the extracted `.ext4` file. The separately provided `.wic.zst` image contains a partitioned disk and uses a different boot procedure; see [Build and boot on x86](../../../build/reference/common/hardware/x86.md).

## Start AGL

Run QEMU from `~/agl-demo`:

```sh
qemu-system-x86_64 \
  -machine q35 -enable-kvm -cpu host -m 2048 \
  -drive file=agl-ivi-demo-flutter-qemux86-64.ext4,if=virtio,format=raw \
  -device virtio-net-pci,netdev=net0,mac=52:54:00:12:35:02 \
  -netdev user,id=net0,hostfwd=tcp:127.0.0.1:2222-:22 \
  -device qemu-xhci -device usb-tablet -device virtio-rng-pci \
  -vga virtio -vnc 127.0.0.1:0 \
  -audiodev pa,id=audio0 -device ich9-intel-hda -device hda-duplex,audiodev=audio0 \
  -snapshot -serial mon:stdio \
  -kernel bzImage \
  -append 'root=/dev/vda rw console=tty0 console=ttyS0,115200n8 ip=dhcp'
```

Open the graphical display from another host terminal:

```sh
vncviewer 127.0.0.1:0
```

Another VNC client can connect to `127.0.0.1`, TCP port `5900`. QEMU's VNC display is local to the host.

The `-snapshot` option discards guest disk changes when QEMU exits. Remove it to save changes. If host audio is unavailable, replace `-audiodev pa,id=audio0` with `-audiodev none,id=audio0` to boot without sound. The explicit HDA device options replace `-soundhw`, which [QEMU removed in 7.1](https://www.qemu.org/docs/master/about/removed-features.html#creating-sound-card-devices-using-soundhw-removed-in-7-1).

If KVM is unavailable, remove `-enable-kvm` and replace `-cpu host` with `-cpu qemu64,+ssse3,+sse4.1,+sse4.2,+popcnt`. Software emulation is slower. If KVM exists but access fails, check the host's `/dev/kvm` permissions and virtualization configuration.

## Confirm the result

Confirm that the Flutter demo UI and serial login prompt appear. Use the image's configured account; development demo images normally permit `root` login. If SSH is enabled, the forwarded port can be used from the host:

```sh
ssh -p 2222 root@127.0.0.1
```

To stop the guest, run `poweroff` at its console. For a launch failure, record the build identifier, host QEMU version (`qemu-system-x86_64 --version`), full command, and error output.

## Next steps

- [Flutter IVI demo](../reference/flutter.md)
- [Troubleshooting](../../../../../../troubleshooting/index.md)
- [Application development](../../../applications/index.md)
