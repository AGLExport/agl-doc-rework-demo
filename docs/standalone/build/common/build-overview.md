---
title: AGL image build workflow
source_path: 01_Getting_Started/02_Building_AGL_Image/01_Build_Process_Overview.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# AGL image build workflow

The AGL image development workflow consists of setting up
the system (i.e. the build host) that builds the image and finishes with
using the
[Yocto Project](https://yoctoproject.org) to create an image
targeted towards specific hardware.

The following figure and list overview the AGL image development
process.
You can learn about the steps in the process by reading through the
remaining sections.

**NOTE:** This procedure uses information from many other procedures
in the AGL Documentation set.
Links are provided when a set of steps is required that is documented
elsewhere.

![](../../../assets/source/01_Getting_Started/02_Building_AGL_Image/images/image-developer-workflow.png)

1. Prepare your build host to be able to use the tools needed to build your image.

2. Download the AGL software into a local Git repository on your build host.

3. Run the build environment script to initialize variables and paths needed for the build.

4. Make sure your build configuration is defined exactly how you want it for your build.

5. Use
   [BitBake](https://docs.yoctoproject.org/{{ yocto.codename }}/bitbake.html)
   to build your image.
