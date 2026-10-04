---
title: "Run AGL on QEMU aarch64"
source_path: "01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md"
content_status: imported
---

# Run AGL on QEMU aarch64

## Before you start

A Linux host with AArch64 QEMU emulation and a VNC client.

Use artifacts from the same AGL build. The configured channel is **{{ agl.codename }} / {{ artifact_kind }}**.

## Start AGL

1. Download the [compressed prebuilt image]({{ agl_download_base }}/latest/qemuarm64/deploy/images/qemuarm64/agl-ivi-demo-qt-qemuarm64.ext4.xz).

2. Download the [compressed kernel image]({{ agl_download_base }}/latest/qemuarm64/deploy/images/qemuarm64/Image).

3. Install [QEMU](https://www.qemu.org/download/) :

    ```sh
    $ apt-get install qemu
    ```

4. Install [vinagre](https://wiki.gnome.org/Apps/Vinagre) :

    ```sh
    $ sudo apt install vinagre
    ```

5. Create boot directory and copy compressed images (prebuilt & kernel) into them :

    ```sh
    $ mkdir ~/agl-demo/
    $ cp ~/Downloads/agl-ivi-demo-qt-qemuarm64.ext4.xz ~/agl-demo/
    $ cp ~/Downloads/Image ~/agl-demo/
    $ cd ~/agl-demo
    $ sync
    ```

6. Extract prebuilt compressed image :

    ```sh
    $ xz -v -d agl-ivi-demo-qt-qemuarm64.ext4.xz
    ```

7. Launch QEMU with vinagre (for scaling), remove `- snapshot \` if you want to save changes to the image files :

  ```sh
    $ ( sleep 5 && vinagre --vnc-scale localhost ) > /tmp/vinagre.log 2>&1 &
        qemu-system-aarch64 -cpu cortex-a57 -machine virt -nographic \
        -net nic,model=virtio,macaddr=52:54:00:12:34:58 \
        -net user -m 2048 -monitor none -smp 2 -soundhw hda -device usb-ehci \
        -device virtio-rng-pci -device VGA,vgamem_mb=64,edid=on \
        -device qemu-xhci -device usb-tablet -device usb-kbd -vnc :0 \
        -kernel Image -append "console=ttyAMA0,115200 root=/dev/vda verbose systemd.log_color=false " \
        -drive format=raw,file=agl-ivi-demo-qt-qemuarm64.ext4 \
        -snapshot
  ```

  - Login into AGL :

    ```sh
    Automotive Grade Linux xx.x.x qemuarm64 ttyS1

    qemuarm64 login: root
    ```


  - Shutdown QEMU : `$ poweroff`, otherwise QEMU will run in the background.
  - To use vnc-viewer instead of vinagre :
    ```sh
    $ ( sleep 5 && vncviewer ) &
        qemu-system-aarch64 -cpu cortex-a57 -machine virt -nographic \
        -net nic,model=virtio,macaddr=52:54:00:12:34:58 \
        -net user -m 2048 -monitor none -smp 2 -soundhw hda -device usb-ehci \
        -device virtio-rng-pci -device VGA,vgamem_mb=64,edid=on \
        -device qemu-xhci -device usb-tablet -device usb-kbd -vnc :0 \
        -kernel Image -append "console=ttyAMA0,115200 root=/dev/vda verbose systemd.log_color=false " \
        -drive format=raw,file=agl-ivi-demo-qt-qemuarm64.ext4 \
        -snapshot
    ```

## Confirm the result

Confirm that the AGL console or demo UI starts. Check the image and kernel names if boot fails, and record the build identifier before reporting a problem.

## Next steps

- [Troubleshooting](../troubleshooting/index.md)
- [Develop an application](../develop/index.md#apps)
- [Choose another environment](prebuilt-images.md)
