"""Import the local AGL documentation into the GitHub Pages information structure.

Run from any directory with Python 3.12. Only the destination project is written.
Unadapted imported pages are refreshed. Locally adapted pages are preserved unless
--overwrite-adapted is supplied; authored landing pages and configuration are not touched.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit
from import_transforms import adapt_page, render_quickstarts, normalize_page

PROJECT = Path(__file__).resolve().parents[1]
REQUIRED_TITLES = {p["page"]: p["heading"] for p in json.loads((PROJECT / "structure-map.json").read_text(encoding="utf-8"))["required_pages"]}
MAPPING: dict[str, str] = {}
TITLES: dict[str, str] = {}

def group(prefix: str, rows: str) -> None:
    for row in rows.strip().splitlines():
        source, target, *title = row.strip().split("|")
        MAPPING[prefix + source] = target
        if title:
            TITLES[target] = title[0]

group("", """
index.md|home/about-source.md|About Automotive Grade Linux
""")
group("01_Getting_Started/", """
01_Quickstart/01_Using_Ready_Made_Images.md|start/prebuilt/index.md|Choose a prebuilt image
02_Building_AGL_Image/01_Build_Process_Overview.md|standalone/build/common/build-overview.md|AGL image build workflow
02_Building_AGL_Image/02_Preparing_Your_Build_Host.md|standalone/build/common/prepare-host.md|Prepare a build host
02_Building_AGL_Image/03_Downloading_AGL_Software.md|standalone/build/common/download-source.md|Download AGL source
02_Building_AGL_Image/04_Initializing_Your_Build_Environment.md|standalone/build/common/initialize-build.md|Initialize the AGL build environment
02_Building_AGL_Image/05_Customizing_Your_Build.md|standalone/customize/build-output.md|Configure caches and build output
02_Building_AGL_Image/06_Building_the_AGL_Image/01_Building_the_AGL_Image.md|standalone/build/common/build-image.md|Build an AGL image
02_Building_AGL_Image/06_Building_the_AGL_Image/02_Building_for_x86_(Emulation_and_Hardware).md|standalone/build/common/hardware/x86.md|Build and boot on x86
02_Building_AGL_Image/06_Building_the_AGL_Image/03_Building_for_Raspberry_Pi_x.md|standalone/build/common/hardware/raspberry-pi.md|Build and boot on Raspberry Pi
02_Building_AGL_Image/06_Building_the_AGL_Image/04_01_Building_for_Renesas_RCar_Gen3_Boards.md|standalone/build/common/hardware/renesas-rcar-gen3.md|Build and boot on R-Car Gen3
02_Building_AGL_Image/06_Building_the_AGL_Image/04_Building_for_Retronix_Sparrow_Hawk_Board.md|standalone/build/common/hardware/sparrow-hawk.md|Build and boot on Sparrow Hawk
02_Building_AGL_Image/06_Building_the_AGL_Image/05_Building_for_Supported_Rockchip_Boards.md|standalone/build/common/hardware/rockchip.md|Build and boot on Rockchip boards
02_Building_AGL_Image/06_Building_the_AGL_Image/06_Building_for_Virtio.md|integrated/sodev/virtio-guest.md|Build a virtio guest
02_Building_AGL_Image/06_Building_the_AGL_Image/07_Building_for_EC2_arm64_and_x86-64.md|standalone/build/common/hardware/aws-ec2.md|Build and run on AWS EC2
02_Building_AGL_Image/06_Building_the_AGL_Image/08_Building_for_VisionFive2_Boards.md|standalone/build/common/hardware/visionfive2.md|Build and boot on VisionFive2
02_Building_AGL_Image/07_Available_Demo_Images.md|standalone/build/common/reference/images.md|AGL image targets
03_Build_and_Boot_guide_Profile/01_Instrument_Cluster_(IC-IVI_with_Container_isolation).md|integrated/containers/build-guide.md|Instrument Cluster with container isolation
03_Build_and_Boot_guide_Profile/02_KVM_Demo_Images.md|integrated/kvm/images.md|KVM demo images
03_Build_and_Boot_guide_Profile/03_Slint_Demo_Image.md|standalone/build/cluster/slint.md|Rust and Slint Instrument Cluster demo
""")
group("02_Hardware_Support/", """
01_Supported_Hardware_Overview.md|standalone/build/common/reference/hardware.md|Hardware support levels and boards
02_Supported_Hardware_Images.md|standalone/build/common/reference/hardware-images.md|Hardware image configurations
""")
group("03_Architecture_Guides/01_Introduction/", """
01_Overview.md|home/architecture.md|AGL system architecture
""")
group("04_Developer_Guides/", """
01_Basic/01_Overview.md|standalone/applications/sdk-overview.md|Application development and SDK workflow
01_Basic/02_Setting_Up_AGL_SDK.md|standalone/applications/setup-sdk.md|Set up the AGL SDK
01_Basic/03_How_to_Build.md|standalone/applications/build-apps.md|Build applications with the SDK
02_AGL_Platform_Development/01_AGL_Yocto_Layers/01_Overview.md|standalone/build/common/layers/overview.md|AGL Yocto layer structure
02_AGL_Platform_Development/01_AGL_Yocto_Layers/02_meta_agl.md|standalone/build/common/layers/meta-agl.md
02_AGL_Platform_Development/01_AGL_Yocto_Layers/03_meta_agl_demo.md|standalone/build/common/layers/meta-agl-demo.md
02_AGL_Platform_Development/01_AGL_Yocto_Layers/04_meta_agl_devel.md|standalone/build/common/layers/meta-agl-devel.md
02_AGL_Platform_Development/02_Modify_AGL_by_Yourself/01_Customizing_AGL_Image.md|standalone/customize/image.md|Customize an AGL image
02_AGL_Platform_Development/02_Modify_AGL_by_Yourself/02_Creating_a_New_Service.md|standalone/customize/service.md|Create a service
02_AGL_Platform_Development/02_Modify_AGL_by_Yourself/03_Creating_a_custom_recipe.md|standalone/customize/recipe.md|Create a custom recipe
03_AGL_Application_Development/Develop_using_Qt/01_AGL-SDK_for_Qt.md|standalone/applications/qt.md|Qt application development
03_AGL_Application_Development/Develop_using_Flutter/01_Flutter_Workspace.md|standalone/applications/flutter.md|Set up a Flutter workspace
10_Board_Specific_Guide/04_Raspberry_Pi/01_Generic_devices_setup.md|standalone/build/common/hardware/raspberry-pi/devices.md|Raspberry Pi peripheral setup
10_Board_Specific_Guide/04_Raspberry_Pi/02_Camera_setup.md|standalone/build/common/hardware/raspberry-pi/camera.md|Raspberry Pi camera setup
10_Board_Specific_Guide/04_Raspberry_Pi/03_Display_Setup.md|standalone/build/common/hardware/raspberry-pi/display.md|Raspberry Pi display setup
20_Tools_Guide/01_CAN/01_USB_CAN_Adaptor.md|components/tools/usb-can-adapter.md|Use a USB CAN adapter
""")
group("05_APIs_and_Services/", """
01_Introduction.md|components/api/source-api-coverage.md|Original API coverage overview
instrument-cluster/AGL-Instrument-Cluster-API-en.md|components/api/cluster/instrument-cluster-api.md|Instrument Cluster API specification
""")
group("06_Component_Documentation/", """
00_AGL_components.md|components/source-directory.md|AGL component directory
01_Graphics_Service/01_agl_compositor.md|components/services/graphics/agl-compositor.md|AGL compositor
01_Graphics_Service/02_drm_lease_manager.md|components/services/graphics/drm-lease-manager.md|DRM lease manager
02_Sound_Service/01_pipewire_wireplumber.md|components/services/sound/pipewire-wireplumber.md|PipeWire and WirePlumber
02_Sound_Service/02_Instrument_Cluster_Sound_Management.md|components/services/sound/cluster-sound.md|Instrument Cluster sound management
03_Policies_Service/01_Rule_Based_Arbitrator.md|components/services/policies/rule-based-arbitrator.md|Rule-based arbitrator
04_Misc_Service/01_AGL_Persistent_Storage_API.md|components/api/ivi/persistent-storage.md|Persistent Storage API
04_Misc_Service/02_agl_voice_agent_assistant.md|components/services/misc/voice-agent.md|Voice agent assistant
10_IC_Service/01_Instrument_Cluster_Service.md|components/services/cluster/cluster-service.md|Instrument Cluster service
20_IVI_Application_Framework/01_Introduction.md|components/framework/lifecycle/application-framework.md|AGL application framework
20_IVI_Application_Framework/02_Application_Startup.md|components/framework/lifecycle/application-startup.md|Application startup and applaunchd
20_IVI_Application_Framework/03_Creating_a_New_Application.md|standalone/applications/create-application.md|Package and register an AGL application
20_IVI_Application_Framework/04_Application_Sandboxing.md|components/framework/sandboxing.md|Application sandboxing
40_Demo_Application/01_Flutter_Demo_IVI/01_Flutter_Homescreen.md|components/applications/flutter-homescreen.md|Flutter IVI homescreen
40_Demo_Application/02_Qt_Demo_IVI/01_Qt_Homescreen.md|components/applications/qt-homescreen.md|Qt IVI homescreen
40_Demo_Application/03_Instrument_Cluster/01_Cluster_Ref_GUI.md|components/applications/cluster-dashboard.md|Instrument Cluster reference GUI
40_Demo_Application/04_Momi_IVI_Demo/01_Momi_Screen.md|components/applications/momi-screen.md|Momi Screen
40_Demo_Application/04_Momi_IVI_Demo/02_Momi_Navi.md|components/applications/momi-navigation.md|Momi navigation
40_Demo_Application/04_Momi_IVI_Demo/04_Momi_Weather.md|components/applications/momi-weather.md|Momi Weather
60_Unified_HMI/01_Unified_HMI.md|components/extensions/unified-hmi.md|Unified HMI
61_Container/01_Container_Manager.md|components/extensions/container-manager.md|Container Manager
61_Container/01_Container_Manager/01_Container_manager_global_config.md|components/extensions/container-settings/global.md|Container Manager global configuration
61_Container/01_Container_Manager/02_Container_configuration_files.md|components/extensions/container-settings/containers.md|Container configuration files
80_DevTools/01_AGL_Demo_Control_Panel.md|components/tools/demo-control/panel.md|AGL Demo Control Panel
80_DevTools/02_CARLA_with_AGL.md|components/tools/demo-control/carla.md|Use CARLA with AGL
80_DevTools/03_AGL_Virtual_Car_CAN/01_agl-vcar.md|components/tools/virtual-car/virtual-car.md|AGL virtual car
80_DevTools/03_AGL_Virtual_Car_CAN/02_vehicle_signal.md|components/tools/virtual-car/signals/vehicle.md|Virtual car vehicle signals
80_DevTools/03_AGL_Virtual_Car_CAN/03_body.md|components/tools/virtual-car/signals/body.md|Virtual car body signals
80_DevTools/03_AGL_Virtual_Car_CAN/04_sensor.md|components/tools/virtual-car/signals/sensors.md|Virtual car sensor signals
""")
group("07_How_To_Contribute/", """
01_Getting_Linux_Foundation_account.md|contributing/linux-foundation-account.md|Get a Linux Foundation account
02_Using_Jira_for_current_work_items.md|contributing/jira.md|Track work in Jira
03_Working_with_Gerrit.md|contributing/gerrit.md|Work with Gerrit
04_Submitting_Changes.md|contributing/submit-changes.md|Submit a change
05_Reviewing_Changes.md|contributing/review-changes.md|Review changes
06_Gerrit_Recommended_Practices.md|contributing/gerrit-practices.md|Gerrit recommended practices
07_General_Guidelines.md|contributing/general-guidelines.md|Contribution guidelines
08_Reporting_bugs.md|troubleshooting/reporting-bugs.md|Report a bug
08_Getting_help.md|troubleshooting/getting-help.md|Get community help
08_Code_contribution_guidelines.md|contributing/code-guidelines.md|Code contribution guidelines
08_AI-coding-assistants.md|contributing/ai-coding-assistants.md|AI coding assistants
09_Adding_Documentation.md|contributing/documentation.md|Contribute to the original AGL documentation
10_Contribution_Checklist.md|contributing/checklist.md|Contribution checklist
11_Setup_AGL_LAVA_Lab.md|contributing/lava-lab.md|Set up an AGL LAVA lab
""")

def frontmatter(title: str, source: str) -> str:
    return "---\ntitle: " + json.dumps(title, ensure_ascii=False) + "\nsource_path: " + json.dumps(source) + "\ncontent_status: imported\n---\n\n"

def write_imported_page(target: Path, page: str, source: str, overwrite_adapted: bool = False) -> bool:
    """Preserve a curated adaptation of the same source; return whether it was written."""
    if target.is_file() and not overwrite_adapted:
        existing = target.read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", existing, re.S)
        metadata = match.group(1) if match else ""
        status = re.search(r"^content_status:\s*(.+)$", metadata, re.M)
        origin = re.search(r"^source_path:\s*(.+)$", metadata, re.M)
        if status and status.group(1).strip("\"'") in {"adapted", "authored"}:
            if not origin or origin.group(1).strip("\"'") != source:
                raise ValueError("Adapted page has a different or missing source_path: " + str(target))
            return False
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page, encoding="utf-8")
    return True


def import_all(source_root: Path, overwrite_adapted: bool = False) -> None:
    files = {p.relative_to(source_root).as_posix(): p for p in source_root.rglob("*") if p.is_file()}
    markdown = {name for name in files if name.endswith(".md")}
    if markdown != set(MAPPING):
        raise SystemExit("Source mapping mismatch. Unmapped: " + str(sorted(markdown - set(MAPPING))) + "; missing: " + str(sorted(set(MAPPING) - markdown)))
    folded = {name.casefold(): name for name in files}
    route_map = {name.removesuffix(".md").casefold(): name for name in MAPPING}
    assets = {name: "assets/source/" + name for name in files if not name.endswith(".md")}
    docs_root = PROJECT / "docs"

    def destination(url: str, old: str, new: str) -> str:
        old_url = url
        if re.match(r"^127\.0\.0\.1:\d+/?$", url):
            return "http://" + url
        self_link = re.match(r"https?://docs\.automotivelinux\.org/en/[^#]+/#([^?#]+)(?:#(.*))?$", url)
        if self_link:
            route = unquote(self_link.group(1)).strip("/")
            canonical = route_map.get(route.removesuffix(".md").casefold())
            fragment = (self_link.group(2) or "").strip("/")
            if canonical:
                if canonical.endswith("01_Supported_Hardware_Overview.md"):
                    fragment = ""
                if fragment in ("_top", ""):
                    fragment = ""
                if fragment in ("3-r-car-h3sk-h3ulcb-board",):
                    canonical = next(k for k, v in MAPPING.items() if v == "standalone/build/common/hardware/renesas-rcar-gen3.md")
                    fragment = ""
                if fragment == "2-raspberry-pi-4":
                    fragment = "raspberry-pi-4"
                relative = posixpath.relpath(MAPPING[canonical], posixpath.dirname(new) or ".")
                return relative + ("#" + fragment if fragment else "")
            return old_url
        if "{{" in url or re.match(r"^[a-zA-Z][\w+.-]*:", url) or url.startswith(("#", "//", "/")):
            return old_url
        parsed = urlsplit(url)
        old_target = posixpath.normpath(posixpath.join(posixpath.dirname(old), unquote(parsed.path)))
        canonical = folded.get(old_target.casefold())
        if not canonical:
            return old_url
        target = MAPPING.get(canonical) or assets.get(canonical)
        if not target:
            return old_url
        relative = posixpath.relpath(target, posixpath.dirname(new) or ".")
        return relative + ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")

    def rewrite(text: str, old: str, new: str) -> str:
        edits: list[tuple[int, int, str]] = []
        for match in re.finditer(r"\]\(", text):
            start = match.end()
            cursor, depth = start, 1
            while cursor < len(text) and depth:
                if text[cursor] == "\\":
                    cursor += 2
                    continue
                if text[cursor] == "(":
                    depth += 1
                elif text[cursor] == ")":
                    depth -= 1
                cursor += 1
            if depth:
                continue
            inner = text[start:cursor - 1]
            leading = len(inner) - len(inner.lstrip())
            value = inner[leading:]
            if value.startswith("<") and ">" in value:
                end = value.index(">")
                url_start, url_end = leading + 1, leading + end
            else:
                j = 0
                while j < len(value):
                    if value[j:j + 2] == "{{":
                        close = value.find("}}", j + 2)
                        if close == -1:
                            break
                        j = close + 2
                    elif value[j].isspace():
                        break
                    else:
                        j += 1
                url_start, url_end = leading, leading + j
            url = inner[url_start:url_end]
            converted = destination(url, old, new)
            if converted != url:
                edits.append((start + url_start, start + url_end, converted))
        for start, end, value in sorted(edits, reverse=True):
            text = text[:start] + value + text[end:]
        def attr(match: re.Match[str]) -> str:
            original = match.group(2)
            converted = destination(original, old, new)
            if converted != original and not re.match(r"^[a-zA-Z][\w+.-]*:", converted):
                if not new.endswith("/index.md") and new != "index.md":
                    converted = "../" + converted
                converted = re.sub(r"index\.md(?=[?#]|$)", "", converted)
                converted = re.sub(r"\.md(?=[?#]|$)", "/", converted)
            return match.group(1) + converted + match.group(3)
        return re.sub(r"""((?:href|src)\s*=\s*["'])([^"']+)(["'])""", attr, text)

    for old, new in assets.items():
        target = docs_root / new
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(files[old], target)
    manifest = []
    preserved = set()
    quickstart_input = None
    for old, new in MAPPING.items():
        original = files[old].read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", original, re.S)
        metadata = match.group(1) if match else ""
        body = original[match.end():] if match else original
        existing_title = re.search(r"^title:\s*(.+)$", metadata, re.M)
        heading = re.search(r"^#+\s+(.+)$", body, re.M)
        title = TITLES.get(new) or (existing_title.group(1).strip("\"'") if existing_title else heading.group(1) if heading else Path(new).stem)
        TITLES[new] = title
        body = rewrite(body, old, new)
        if new == "standalone/build/common/prepare-host.md":
            body = body.replace("Tar 1.27 or greater", "Tar 1.28 or greater").replace("Python 3.4.0 or greater", "Python 3.9.0 or greater")
            body = body.replace("- Python 3.9.0 or greater", "- Python 3.9.0 or greater\n      - GNU make 4.0 or greater\n      - GCC 10.1 or greater")
        target = docs_root / new
        target.parent.mkdir(parents=True, exist_ok=True)
        page = frontmatter(title, old) + adapt_page(body, new)
        if new in REQUIRED_TITLES:
            page = normalize_page(page, REQUIRED_TITLES[new])
        if new == "start/prebuilt/index.md":
            quickstart_input = page
        if not write_imported_page(target, page, old, overwrite_adapted):
            preserved.add(new)
        manifest.append({"source": old, "destination": new, "source_sha256": hashlib.sha256(files[old].read_bytes()).hexdigest()})

    # Generate the Flutter prebuilt routes and preserve the authored demo overview.
    overview = docs_root / "start/prebuilt/index.md"
    source = next(old for old, new in MAPPING.items() if new == "start/prebuilt/index.md")
    if quickstart_input is None:
        raise ValueError("Prebuilt quickstart source is missing")
    pages = render_quickstarts(quickstart_input, source)
    for relative, page in pages.items():
        target = docs_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if not write_imported_page(target, page, source, overwrite_adapted):
            preserved.add(relative)
    structure = json.loads((PROJECT / "structure-map.json").read_text(encoding="utf-8"))
    retired_paths = {p["old"] for p in structure["moved_pages"]}
    retired_paths.update({"start/qemu-arm64.md", "start/virtualbox.md", "start/x86-hardware.md"})
    current_paths = set(MAPPING.values()) | set(pages) | {p["page"] for p in structure["required_pages"]}
    for relative in retired_paths - current_paths:
        retired = (docs_root / relative).resolve()
        if not retired.is_relative_to(docs_root.resolve()):
            raise ValueError("Retired page path is outside the documentation directory")
        retired.unlink(missing_ok=True)
    (PROJECT / "source-map.json").write_text(json.dumps({"source_markdown_count": len(manifest), "source_asset_count": len(assets), "pages": manifest}, indent=2) + "\n", encoding="utf-8")
    print(f"Mapped {len(manifest)} Markdown pages and copied {len(assets)} assets; preserved {len(preserved)} adapted pages.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=PROJECT.parent / "docs", help="Original AGL docs directory")
    parser.add_argument("--overwrite-adapted", action="store_true", help="Replace locally adapted pages with freshly imported source; review source compatibility first")
    args = parser.parse_args()
    import_all(args.source.resolve(), overwrite_adapted=args.overwrite_adapted)
