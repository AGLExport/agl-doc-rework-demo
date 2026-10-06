---
title: "Download AGL source"
source_path: "01_Getting_Started/02_Building_AGL_Image/03_Downloading_AGL_Software.md"
content_status: adapted
---

# Download AGL source

Complete [Prepare a build host](prepare-host.md) first. AGL uses the `repo` tool to download the pinned repositories in an AGL manifest. See the [official source-code guide](https://wiki.automotivelinux.org/agl-distro/source-code).

## Define the workspace directories

Use these meanings throughout the build guides:

| Variable | Meaning | Development example |
| --- | --- | --- |
| `AGL_TOP` | Parent directory for source workspaces and shared caches | `$HOME/AGL` |
| `AGL_SOURCE` | Root of one manifest checkout, containing `meta-agl` and `.repo` | `$HOME/AGL/{{ agl.codename }}` |

Set the parent directory in your host shell:

```sh
export AGL_TOP="$HOME/AGL"
mkdir -p "$AGL_TOP"
```

`AGL_SOURCE` is set when selecting a branch below. Keep these variables in the shell used for subsequent commands; set them again when opening a new shell. Shell variables are not automatically BitBake configuration variables.

## Install the repo tool

```sh
mkdir -p "$HOME/bin"
curl -fL https://storage.googleapis.com/git-repo-downloads/repo -o "$HOME/bin/repo"
chmod a+x "$HOME/bin/repo"
export PATH="$HOME/bin:$PATH"
repo --version
```

For requirements and command details, read the [official repo documentation](https://source.android.com/docs/setup/reference/repo).

## Select a source revision

### Development branch

This site documents `{{ agl.codename }}`. Its manifest and snapshots change over time.

```sh
AGL_BRANCH={{ agl.codename }}
export AGL_SOURCE="$AGL_TOP/$AGL_BRANCH"
mkdir -p "$AGL_SOURCE"
cd "$AGL_SOURCE"
repo init -b "$AGL_BRANCH" -u https://gerrit.automotivelinux.org/gerrit/AGL/AGL-repo
repo sync
```

### Stable release

Choose a release branch or manifest tag from the [official release notes](https://wiki.automotivelinux.org/agl-distro/release-notes). Replace `release-ref` below with that exact reference; `master` is the development branch. Use the matching release documentation, image, and SDK.

```sh
AGL_REF=release-ref
export AGL_SOURCE="$AGL_TOP/$AGL_REF"
mkdir -p "$AGL_SOURCE"
cd "$AGL_SOURCE"
repo init -b "$AGL_REF" -u https://gerrit.automotivelinux.org/gerrit/AGL/AGL-repo
repo sync
```

A maintained release branch can receive updates. For a reproducible checkout, choose a published manifest tag or record the resolved revisions after synchronization:

```sh
repo manifest -r -o "$AGL_SOURCE/manifest-pinned.xml"
```

## Confirm the checkout

```sh
test -f "$AGL_SOURCE/meta-agl/scripts/aglsetup.sh"
repo status
```

The source root contains the layers and board support selected by the manifest. Continue with [Initialize the AGL build environment](initialize-build.md). Run board setup commands from `AGL_SOURCE`, and keep shared downloads and caches under `AGL_TOP` if desired.
