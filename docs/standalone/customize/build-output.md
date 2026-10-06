---
title: "Configure caches and build output"
source_path: "01_Getting_Started/02_Building_AGL_Image/05_Customizing_Your_Build.md"
content_status: adapted
---

# Configure caches and build output

Build settings belong in the initialized build directory's `conf/local.conf`, or in `conf/site.conf` for shared local settings. [Download AGL source](../build/common/download-source.md) defines `AGL_TOP` as the parent workspace and `AGL_SOURCE` as the selected checkout. See [Initialize the build environment](../build/common/initialize-build.md) for configuration fragments.

## Capturing Build History

Add these BitBake assignments to `conf/local.conf`:

```conf
INHERIT += "buildhistory"
BUILDHISTORY_COMMIT = "1"
```

Build history records changes to packages and images. See [Maintaining Build Output Quality](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/build-quality.html#maintaining-build-output-quality).

## Deleting Temporary Workspace

To remove temporary task work directories after successful builds:

```conf
INHERIT += "rm_work"
```

Keep work directories for recipes you are debugging with `RM_WORK_EXCLUDE`. See [Conserving Disk Space](https://docs.yoctoproject.org/{{ yocto.codename }}/dev-manual/disk-space.html#conserving-disk-space-during-builds).

## Pointing at Shared State Cache Locations

Set an absolute cache path in BitBake configuration; replace `/home/you` with your actual home directory:

```conf
SSTATE_DIR = "/home/you/AGL/sstate-cache"
```

A shell's `AGL_TOP` is not automatically available as a BitBake variable. The shared `site.conf` example below expands shell paths before writing the configuration.

For an existing mirror, replace these example locations with your own:

```conf
SSTATE_MIRRORS ?= "file://.* https://sstate.example.org/PATH;downloadfilename=PATH \n file://.* file:///srv/sstate/PATH"
```

Only configure a mirror you operate or have verified for your release. See [Shared State Cache](https://docs.yoctoproject.org/{{ yocto.codename }}/overview-manual/concepts.html#shared-state-cache).

## Preserving the Download Directory

Set a shared directory for downloaded source archives:

```conf
DL_DIR = "/home/you/AGL/downloads"
```

This avoids downloading the same sources for each build directory. See [DL_DIR](https://docs.yoctoproject.org/{{ yocto.codename }}/ref-manual/variables.html#term-DL_DIR).

## Using a Shared State Mirror

If your release provides the AGL mirror, add its matching branch and target tune using current override syntax:

```conf
SSTATE_MIRRORS:append = " file://.* https://download.automotivelinux.org/sstate-mirror/{{ agl.codename }}/${DEFAULTTUNE}/PATH \n "
```

Use a mirror for the selected release and configuration. A mirror improves reuse when matching artifacts exist; it does not guarantee that every task is cached.

## Common Settings using Symbolic Link with site.conf

Run these commands from an initialized build shell. `BUILDDIR` points to that build directory:

```sh
mkdir -p "$AGL_TOP/downloads" "$AGL_TOP/sstate-cache"
if [ ! -e "$AGL_TOP/site.conf" ] && [ ! -L "$AGL_TOP/site.conf" ]; then
    cat > "$AGL_TOP/site.conf" <<EOF
DL_DIR = "$AGL_TOP/downloads"
SSTATE_DIR = "$AGL_TOP/sstate-cache"
EOF
fi
if [ ! -e "$BUILDDIR/conf/site.conf" ] && [ ! -L "$BUILDDIR/conf/site.conf" ]; then
    ln -s "$AGL_TOP/site.conf" "$BUILDDIR/conf/site.conf"
else
    printf '%s\n' "Keeping existing $BUILDDIR/conf/site.conf; review and merge shared settings manually."
fi
```

This creates the shared configuration file when it is absent and links it into the selected build directory when the build-local path is absent. Existing files and symbolic links are retained, including broken links. Review an existing build-local configuration and merge settings manually before deciding whether to replace it with the shared link. Use separate settings when builds require different local configuration.
