---
title: Create/Modify an AGL image
source_path: 04_Developer_Guides/02_AGL_Platform_Development/02_Modify_AGL_by_Yourself/01_Customizing_AGL_Image.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Create/Modify an AGL image

Start from an initialized [AGL build environment](../../build/reference/common/initialize-build.md). This example customizes `agl-image-weston`; choose the image and graphics profile appropriate to your product. Run the commands from the build shell created by `aglsetup.sh`.

## Add a package for a local evaluation

To include the `glmark2` benchmark, add the following to `conf/local.conf`:

```conf
IMAGE_INSTALL:append = " glmark2"
```

The leading space separates the new package from the existing package list. Check that its recipe is available in your selected layers and build the image:

```sh
bitbake-layers show-recipes glmark2
bitbake agl-image-weston
```

## Retain the change in a custom layer

Use a `.bbappend` to modify an existing image recipe. A `.bbappend` keeps the existing image target; a new `.bb` defines a separate image target.

```sh
bitbake-layers create-layer "$AGL_SOURCE/meta-custom-agl"
bitbake-layers add-layer "$AGL_SOURCE/meta-custom-agl"
mkdir -p "$AGL_SOURCE/meta-custom-agl/recipes-core/images"
```

Create `meta-custom-agl/recipes-core/images/agl-image-weston.bbappend` with:

```bb
IMAGE_INSTALL:append = " glmark2"
```

Confirm that BitBake discovers the append, then build:

```sh
bitbake-layers show-appends
bitbake agl-image-weston
```

If the base image recipe is versioned, match its filename or use a suitable `%` pattern. Include the custom layer in your manifest and version control so another developer can reproduce the configuration.

## Reserve 2 GiB of additional root filesystem space

Yocto expresses these root filesystem size values in KiB. `2 GiB = 2,097,152 KiB`. To reserve this additional space on top of the estimated root filesystem contents, add the following to the image's `.bbappend`, or to `conf/local.conf` for a local evaluation:

```bb
IMAGE_ROOTFS_EXTRA_SPACE = "2097152"
```

This sets the extra-space allowance to 2 GiB. It does not promise that the complete disk image grows by exactly 2 GiB: filesystem overhead, `IMAGE_OVERHEAD_FACTOR`, alignment, minimum-size settings, and the WIC partition layout also affect the result. In `local.conf`, the assignment applies to image builds using that configuration; an image-specific `.bbappend` scopes it to that image.

`IMAGE_ROOTFS_SIZE` sets a minimum root filesystem size instead. If you deliberately need a minimum of 400 MiB plus 2 GiB, the calculation is `409600 + 2097152 = 2506752 KiB`:

```bb
IMAGE_ROOTFS_SIZE = "2506752"
```

Use the variable matching your goal. Rebuild without deleting the shared state cache:

```sh
bitbake agl-image-weston
```

Inspect the generated image in `tmp/deploy/images/<machine>/`. For WIC images, inspect the selected `.wks` file for partition sizes and fixed-size limits; adjust it when the root filesystem cannot fit. Confirm the available capacity on the booted target with `df -h /`.

Read the official [IMAGE_ROOTFS_EXTRA_SPACE](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/variables.html#term-IMAGE_ROOTFS_EXTRA_SPACE), [IMAGE_ROOTFS_SIZE](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/variables.html#term-IMAGE_ROOTFS_SIZE), and [image customization guide](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/customizing-images.html) for the sizing rules.
