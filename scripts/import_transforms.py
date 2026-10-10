"""Content adaptations retained when source articles are re-imported."""
import json
import re


def remove_further_reading(text):
    """Remove a Markdown section through the next heading of equal or lower level."""
    lines = text.splitlines(keepends=True)
    headings, fence = [], None
    for index, line in enumerate(lines):
        marker = re.match(r'^\s*(' + chr(96) + r'{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = (marker[1][0], len(marker[1]))
            elif marker[1][0] == fence[0] and len(marker[1]) >= fence[1]:
                fence = None
        elif fence is None:
            heading = re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', line)
            if heading:
                headings.append((index, len(heading[1]), heading[2].casefold()))
    removed = set()
    for offset, (start, level, title) in enumerate(headings):
        if title == 'further reading':
            stop = next((index for index, depth, _ in headings[offset + 1:] if depth <= level), len(lines))
            removed.update(range(start, stop))
    if not removed:
        return text
    return ''.join(line for index, line in enumerate(lines) if index not in removed).rstrip() + '\n'


def frontmatter(title, source):
    return '---\ntitle: '+json.dumps(title)+'\nsource_path: '+json.dumps(source)+'\ncontent_status: adapted\n---\n\n'


def adapt_page(body, path):
    prefixes = {
        'components/applications/flutter-homescreen.md': '''The Flutter IVI homescreen is the main application in `agl-ivi-demo-flutter`. The [complete demo overview](../../start/prebuilt/flutter.md) explains the user experience; the [Flutter application guide](../../distributed/applications/flutter.md) explains development.

The [image catalog](../../distributed/build/common/reference/images.md#agl-ivi-demo-flutter) identifies `flutter-ics-homescreen`. Its [upstream source](https://git.automotivelinux.org/apps/flutter-ics-homescreen/) is the implementation reference. The imported source records a pending detailed-documentation issue below.

''',
        'components/applications/qt-homescreen.md': '''The Qt IVI image uses a homescreen and launcher together with Qt applications. See the [image catalog](../../distributed/build/common/reference/images.md#agl-ivi-demo-qt), [Qt IVI build](../../distributed/build/ivi/qt-ivi-demo.md), and [Qt application development](../../distributed/applications/qt.md).

Read [Application Framework](../framework/lifecycle/application-framework.md) for lifecycle integration. The imported source records a pending detailed-documentation issue below.

''',
        'distributed/applications/qt.md': '''Use the SDK and target image from the same AGL release. Read the [SDK setup](setup-sdk.md) and [build applications guide](build-apps.md), then [package/register the application](create-application.md).

For the reference UI and image, see [Qt IVI homescreen](../../components/applications/qt-homescreen.md) and [Qt IVI demo build](../build/ivi/qt-ivi-demo.md). The supplied Qt-specific source page is incomplete; the SDK guides provide the documented preparation and deployment route.

'''}
    body = body.replace('IMAGE_INSTALL_append', 'IMAGE_INSTALL:append')
    body = body.replace('SSTATE_MIRRORS_append', 'SSTATE_MIRRORS:append')
    body = body.replace('devtool update-recipce', 'devtool update-recipe')
    body = body.replace('stream-properties="p,media.role=Multimedia""', 'stream-properties="p,media.role=Multimedia"')
    return prefixes.get(path, '')+body


def render_quickstarts(imported, source):
    match = re.search(r'^### QEMU x86-64\s*\n(.*?)(?=^#{2,3} |\Z)', imported, re.M|re.S)
    if not match:
        raise ValueError('QEMU x86-64 source section not found')
    body = match[1].strip().replace('agl-ivi-demo-qt-', 'agl-ivi-demo-flutter-')
    qemu = frontmatter('QEMU x86-64',source)+'# QEMU x86-64\n\n'
    qemu += 'Use a Linux host with QEMU, KVM access, and a VNC client. This guide boots the Flutter IVI demo. Keep its image and kernel on the same release/build.\n\n## Start AGL\n\n'+body+'\n\n'
    qemu += '## Confirm the result\n\nConfirm that the console or Flutter demo UI starts. Record the build identifier and launch command if it fails.\n\n## Next steps\n\n- [Flutter IVI demo](flutter.md)\n- [Troubleshooting](../../troubleshooting/index.md)\n- [Application development](../../distributed/applications/index.md)\n'
    raspberry = frontmatter('Raspberry Pi 4/5',source)+'''# Raspberry Pi 4/5

Use a Raspberry Pi 4 or 5, a suitable display, network access, and a microSD card. Select the image for the exact board; Pi 4 and Pi 5 images are not interchangeable.

## Download the Flutter IVI image

The configured channel is **{{ agl.codename }} / {{ artifact_kind }}**. The following artifact directories were checked on 5 October 2026; select matching files from your chosen release/build.

| Board | Artifact directory | Image |
| --- | --- | --- |
| Raspberry Pi 4 | [Pi 4 images]({{ agl_download_base }}/latest/raspberrypi4/deploy/images/raspberrypi4-64/) | `agl-ivi-demo-flutter-raspberrypi4-64.wic.zst` |
| Raspberry Pi 5 | [Pi 5 images]({{ agl_download_base }}/latest/raspberrypi5/deploy/images/raspberrypi5/) | `agl-ivi-demo-flutter-raspberrypi5.wic.zst` |

Download the selected compressed WIC image. This disk image includes the board's boot files and filesystem. Use the filenames and compression provided by your release.

## Write the microSD card

Run these commands on the **host**. Identify the removable card with `lsblk` and unmount its mounted partitions.

```sh
lsblk
```

!!! warning "Choose the card device carefully"
    Writing the image replaces the selected device's contents. Confirm the device every time. Replace `/dev/sdX` with the whole microSD device, not a partition or the host's system disk.

Set the downloaded filename and verified card device, then write the image:

```sh
IMAGE=agl-ivi-demo-flutter-raspberrypi4-64.wic.zst  # use the Pi 5 filename for Pi 5
SD_DEVICE=/dev/sdX                             # replace after checking lsblk
zstd -dc "$IMAGE" | sudo dd of="$SD_DEVICE" bs=4M conv=fsync status=progress
sync
```

## Boot and check

Insert the card, connect the display/network, and power on the board. Confirm that the Flutter homescreen appears. Use the [board build/boot guide](../../distributed/build/common/hardware/raspberry-pi.md) for display and board-specific notes. The presence of a downloaded artifact does not establish validation for every display or peripheral combination.

When the target has a network address, connect from the host if the image's login configuration permits it:

```sh
ssh root@<target-ip-address>
```

See [Flutter IVI demo](flutter.md) for an explanation of the UI and [Troubleshooting](../../troubleshooting/index.md) for logs and boot diagnosis.
'''
    overview = frontmatter('Run Flutter IVI demo pre-build image', source)+'''# Run Flutter IVI demo pre-build image

Evaluate AGL with the Flutter IVI demo before preparing a full source build. Read the demo overview, then choose your boot environment.

- [Flutter IVI demo](flutter.md): understand the complete demo and its services.
- [QEMU x86-64](qemu-x86-64.md): run the image on a Linux host.
- [Raspberry Pi 4/5](raspberry-pi.md): write the board-specific image to a microSD card.

Use [Releases & migration](../../releases/index.md) to choose a version and the [board/image reference](../../distributed/build/common/reference/matrix.md) to check target requirements.

<span id="qemu-x86-64"></span>
<span id="raspberry-pi-4"></span>
'''
    return {'start/prebuilt/index.md':overview,'start/prebuilt/qemu-x86-64.md':qemu,'start/prebuilt/raspberry-pi.md':raspberry}

def normalize_page(text, title):
    """Use a required chapter title without modifying headings inside code blocks."""
    match = re.match(r'\A---\s*\n(.*?)\n---\s*\n', text, re.S)
    metadata = match[1] if match else ''
    body = text[match.end():] if match else text
    replacement = 'title: '+json.dumps(title)
    if re.search(r'^title:.*$', metadata, re.M):
        metadata = re.sub(r'^title:.*$', lambda m: replacement, metadata, count=1, flags=re.M)
    else:
        metadata = replacement+('\n'+metadata if metadata else '')
    lines = body.splitlines()
    fence = None
    found = False
    for index,line in enumerate(lines):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
            continue
        if fence is None and re.match(r'^#\s+',line):
            lines[index] = '# '+title
            found = True
            break
    if not found:
        lines = ['# '+title,'',*lines]
    return '---\n'+metadata+'\n---\n\n'+'\n'.join(lines).strip()+'\n'
