---
title: Build an AGL image
source_path: 01_Getting_Started/02_Building_AGL_Image/06_Building_the_AGL_Image/01_Building_the_AGL_Image.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Build an AGL image

Building the AGL image involves running BitBake with a specified target.
Depending on whether you are building the image for the first time or if this
is a subsequent build, the time needed for the build could be significant.

It is critical that you specify the correct options and configurations for the
build before executing the `bitbake` command.
The previous sections in the "Image Development Workflow" have treated this setup
in a generic fashion. AGL has both `Qt` based and `HTML5` based IVI demos, where the build process is almost the same except for a few changes in the build environment.

This section, provides links to topics with instructions needed to create images for
three types of supported platforms and for emulation/virtualization using Quick
EMUlator (QEMU) or VirtualBox:

* [x86 (Emulation and Hardware)](hardware/x86.md)
* [Raspberry Pi 5 and 4](hardware/raspberry-pi.md)
* [R Car Gen 3](hardware/renesas-rcar-gen3.md)
* [Sparrow Hawk](hardware/sparrow-hawk.md)
* [Rockchip/NanoPC T6](hardware/rockchip.md)
* [Virtio](../../../large-integrated/sodev/virtio-guest.md)
* [AWS EC2 (arm64 or x86-64)](hardware/aws-ec2.md)
