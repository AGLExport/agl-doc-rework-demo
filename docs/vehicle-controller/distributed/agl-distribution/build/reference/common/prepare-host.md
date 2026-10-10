---
title: Prepare a build host
source_path: 01_Getting_Started/02_Building_AGL_Image/02_Preparing_Your_Build_Host.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Prepare a build host

Preparing your build host so that it can build an AGL image means
making sure your system is set up to use the
[Yocto Project](https://yoctoproject.org) OpenEmbedded build system,
which is based on
[BitBake](https://docs.yoctoproject.org/{{ yocto.codename }}/bitbake.html).

This section presents minimal information so you can prepare the build host
to use the "{{ yocto.codename | capitalize }}" version of the Yocto Project (i.e. version {{ yocto.version }}).
If you want more details on how the Yocto Project works, you can reference
the Yocto Project documentation
[here](https://www.yoctoproject.org/docs/).

**NOTE:** This entire section presumes you want to build an image.
You can skip the entire build process if you want to use a ready-made
development image.
The [supported images]({{ agl_download_base }}/latest/) exist for several boards as
well as for the Quick EMUlator (QEMU).
See the
"[Quickstart](../../../quick-start/prebuilt/index.md)"
section for more information on the ready-made images.

1. **Use a Supported Linux Distribution:** To use the AGL software, it is
   recommended that your build host is a native Linux machine that runs a
   Yocto Project supported distribution as described by the
   "[Supported Linux Distributions](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/system-requirements.html#supported-linux-distributions)"
   section in the Yocto Project Reference Manual.
   Basically, you should be running a recent version of Ubuntu, Fedora, openSUSE,
   CentOS, or Debian.

2. **Be Sure Your Build Host Has Enough Free Disk Space:**
   Your build host should have at least 100 Gbytes of free disk space for minimal images. For full demo images with Flutter support (e.g. agl-ivi-demo-flutter), plan for at least 300 Gbytes.

3. **Be Sure Tools are Recent:**  You need to have recent versions for the following tools:

      - Git 1.8.3.1 or greater
      - Tar 1.28 or greater
      - Python 3.9.0 or greater
      - GNU make 4.0 or greater
      - GCC 10.1 or greater

   If your distribution does not meet these minimal requirements, see the
   "[Required Git, tar, and Python Versions](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/system-requirements.html#required-git-tar-python-make-and-gcc-versions)"
   section in the Yocto Project Reference Manual for steps that you can
   take to be sure you have these tools.

4. **Install Essential, Graphical, and Eclipse Plug-in Build Host Packages:**
   Your build host needs certain host packages.
   Depending on the Linux distribution you are using, the list of
   host packages differ.
   See
   "[The Build Host Packages](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/system-requirements.html#required-packages-for-the-build-host)"
   section of the Yocto Project Quick Start for information on the packages you need.

   **NOTE:** If you are using the CentOS distribution, you need to
   separately install the epel-release package and run the `makecache` command as
   described in
   "[The Build Host Packages](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/system-requirements.html#required-packages-for-the-build-host)"
   section of the Yocto Project Quick Start.

   Aside from the packages listed in the previous section, you need the following:

   * **Ubuntu and Debian:** curl
   * **Fedora:** curl
   * **OpenSUSE:** glibc-locale curl
   * **CentOS:** curl
