---
title: "QEMU x86-64"
source_path: "01_Getting_Started/01_Quickstart/01_Using_Ready_Made_Images.md"
content_status: adapted
---

# QEMU x86-64

Use a Linux host with QEMU, KVM access, and a VNC client. This guide boots the Flutter IVI demo. Keep its image and kernel on the same release/build.

## Start AGL

1. Download the [compressed prebuilt image]({{ agl_download_base }}/latest/qemux86-64/deploy/images/qemux86-64/agl-ivi-demo-flutter-qemux86-64.ext4.xz).

2. Download the [compressed kernel image]({{ agl_download_base }}/latest/qemux86-64/deploy/images/qemux86-64/bzImage).

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
    $ cp ~/Downloads/agl-ivi-demo-flutter-qemux86-64.ext4.xz ~/agl-demo/
    $ cp ~/Downloads/bzImage ~/agl-demo/
    $ cd ~/agl-demo
    $ sync
    ```

6. Extract prebuilt compressed image :

    ```sh
    $ xz -v -d agl-ivi-demo-flutter-qemux86-64.ext4.xz
    ```

7. Launch QEMU with vinagre (for scaling), remove `- snapshot \` if you want to save changes to the image files :

  ```sh
    $ ( sleep 5 && vinagre --vnc-scale localhost ) > /tmp/vinagre.log 2>&1 &
    $ qemu-system-x86_64 -device virtio-net-pci,netdev=net0,mac=52:54:00:12:35:02 -netdev user,id=net0,hostfwd=tcp::2222-:22 \
      -drive file=agl-ivi-demo-flutter-qemux86-64.ext4,if=virtio,format=raw -show-cursor -usb -usbdevice tablet -device virtio-rng-pci \
      -snapshot -vga virtio \
      -vnc :0 -soundhw hda -machine q35 -cpu kvm64 -cpu qemu64,+ssse3,+sse4.1,+sse4.2,+popcnt -enable-kvm \
      -m 2048 -serial mon:vc -serial mon:stdio -serial null -kernel bzImage \
      -append 'root=/dev/vda rw console=tty0 mem=2048M ip=dhcp oprofile.timer=1 console=ttyS0,115200n8 verbose fstab=no'
  ```

  - Login into AGL :

    ```sh
    Automotive Grade Linux xx.x.x qemux86-64 ttyS1

    qemux86-64 login: root
    ```


  - Shutdown QEMU : `$ poweroff`, otherwise QEMU will run in the background.
  - To use vnc-viewer instead of vinagre :
    ```sh
    $ ( sleep 5 && vncviewer ) &
       qemu-system-x86_64 -device virtio-net-pci,netdev=net0,mac=52:54:00:12:35:02 -netdev user,id=net0,hostfwd=tcp::2222-:22 \
       -drive file=agl-ivi-demo-flutter-qemux86-64.ext4,if=virtio,format=raw -show-cursor -usb -usbdevice tablet -device virtio-rng-pci \
       -snapshot -vga virtio \
       -vnc :0 -soundhw hda -machine q35 -cpu kvm64 -cpu qemu64,+ssse3,+sse4.1,+sse4.2,+popcnt -enable-kvm \
       -m 2048 -serial mon:vc -serial mon:stdio -serial null -kernel bzImage \
       -append 'root=/dev/vda rw console=tty0 mem=2048M ip=dhcp oprofile.timer=1 console=ttyS0,115200n8 verbose fstab=no'
    ```

## Confirm the result

Confirm that the console or Flutter demo UI starts. Record the build identifier and launch command if it fails.

## Next steps

- [Flutter IVI demo](flutter.md)
- [Troubleshooting](../../troubleshooting/index.md)
- [Application development](../../standalone/applications/index.md)
