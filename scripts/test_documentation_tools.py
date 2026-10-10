"""Regression checks for required-section resolution and import preservation."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import posixpath
from unittest.mock import patch

import import_docs
import yaml
from validate_structure import content_requirements, section_paths, validate, validate_master_references
from import_transforms import remove_further_reading


class SectionResolutionTests(unittest.TestCase):
    def test_focus_references_resolve_to_current_vehicle_controller_systems(self):
        pages = [("Distributed system", "vehicle-controller/distributed/index.md"),
                 ("Small-scale integrated system", "vehicle-controller/small-integrated/index.md"),
                 ("Large-scale integrated system", "vehicle-controller/large-integrated/index.md")]
        for alias, expected in [("AGL distributed system", pages[0][1]),
                                ("AGL small-scale integrated system", pages[1][1]),
                                ("AGL large-scale integrated system", pages[2][1])]:
            with self.subTest(alias=alias):
                self.assertEqual(section_paths(alias, pages, {}), [expected])

    def test_historical_coverage_reference_resolves_to_introduction(self):
        self.assertEqual(section_paths("AGL Coverage", [("Introduction", "introduction/index.md")], {}), ["introduction/index.md"])

    def test_hyphenated_content_rule_resolves_to_exact_navigation_spelling(self):
        pages = [("Small scale integrated system", "vehicle-controller/small-integrated/index.md")]
        self.assertEqual(section_paths("Small-scale integrated system", pages, {}), ["vehicle-controller/small-integrated/index.md"])
        self.assertEqual(section_paths("AGL small-scale integrated system", pages, {}), ["vehicle-controller/small-integrated/index.md"])

    def test_ambiguous_sections_are_not_silently_selected(self):
        pages = [("SoDeV", "first.md"), ("SoDeV", "second.md")]
        self.assertEqual(section_paths("SoDeV", pages, {}), ["first.md", "second.md"])


class ContentRequirementTests(unittest.TestCase):
    def test_empty_content_declaration_requires_the_section_but_no_extra_content(self):
        with TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "docs").mkdir()
            instructions = ('## Required Structure\n- Home\n'
                            '## Required Contents at Section\n'
                            '"Home" section must include the following content:\n')
            (project / "AGENTS.md").write_text(instructions, encoding="utf-8")
            (project / "mkdocs.yml").write_text(yaml.safe_dump({"nav": [{"Home": "index.md"}], "not_in_nav": ""}), encoding="utf-8")
            (project / "structure-map.json").write_text(json.dumps({"required_pages": [
                {"heading": "Home", "page": "index.md", "breadcrumb": ["Home"]},
            ]}), encoding="utf-8")
            (project / "source-map.json").write_text(json.dumps({"pages": []}), encoding="utf-8")
            (project / "docs/index.md").write_text("# Home\n", encoding="utf-8")
            with redirect_stdout(StringIO()):
                validate(project)
            (project / "AGENTS.md").write_text(instructions.replace('"Home" section', '"Missing" section'), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Required content section is missing"):
                validate(project)

    def test_updated_instructions_require_figures_and_matching_system_links(self):
        instructions = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rules = content_requirements(instructions)
        self.assertIn("Home", rules)
        self.assertEqual(rules["Home"]["section_references"]["What is AGL."], "AGL Coverage")
        introduction = rules["Introduction"]
        self.assertEqual(introduction["figures"], [
            "Traditional distributed architecture.", "Domain architecture.", "Central/Zone architecture.",
        ])
        self.assertEqual(introduction["headings"], [
            (2, "Vehicle EE architectures."), (3, "Traditional distributed architecture."),
            (3, "Domain architecture."), (3, "Central/Zone architecture."),
            (2, "Vehicle Data Processing."),
        ])
        expected_paths = ["vehicle-controller/distributed/index.md", "vehicle-controller/small-integrated/index.md", "vehicle-controller/large-integrated/index.md"]
        pages = [("Distributed system", expected_paths[0]),
                 ("Small-scale integrated system", expected_paths[1]),
                 ("Large-scale integrated system", expected_paths[2])]
        self.assertEqual([section_paths(name, pages, {})[0]
                          for name in introduction["section_references"].values()], expected_paths)

    def test_official_figure_and_source_requirement_belong_to_large_scale(self):
        instructions = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rules = content_requirements(instructions)
        self.assertTrue(rules["Large-scale integrated system"]["official_figure"])
        self.assertEqual(len(rules["Large-scale integrated system"]["source_links"]), 1)
        self.assertFalse(rules["SoDeV"]["official_figure"])
        self.assertIn("Small-scale integrated system", rules)

    def test_scoped_rule_selects_architecture_and_requires_both_named_diagrams(self):
        instructions = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rule = content_requirements(instructions)["Basic demo system under Architecture"]
        self.assertEqual(rule["required_assets"], ["agl-flutter-ivi-architecture.svg", "agl-qt-ivi-architecture.svg"])
        pages = [("Basic demo system", "portfolio.md"), ("Basic demo system", "architecture.md")]
        structure = {"required_pages": [
            {"heading": "Basic demo system", "page": pages[0][1], "breadcrumb": ["Home", "Portfolio", "Basic demo system"]},
            {"heading": "Basic demo system", "page": pages[1][1], "breadcrumb": ["Home", "Architecture", "Basic demo system"]},
        ]}
        self.assertEqual(section_paths(rule["section_title"], pages, structure, rule["parent"]), ["architecture.md"])

    def test_repeated_sections_and_scoped_diagram_are_both_validated(self):
        with TemporaryDirectory() as directory:
            project = Path(directory)
            docs = project / "docs"
            docs.mkdir()
            instructions = """## Required Structure
- Home
  - Portfolio
    - Basic demo system
  - Architecture
    - Basic demo system
## Required Contents at Section
"Basic demo system" section must include the following content:
  A shared IVI platform supplies the runtime.
"Basic demo system" section under "Architecture" section must include the following content:
Show the architecture diagram "required.svg".
"""
            (project / "AGENTS.md").write_text(instructions, encoding="utf-8")
            nav = [{"Home": ["index.md", {"Portfolio": ["portfolio.md", {"Basic demo system": "portfolio-basic.md"}]},
                             {"Architecture": ["architecture.md", {"Basic demo system": "architecture-basic.md"}]}]}]
            (project / "mkdocs.yml").write_text(yaml.safe_dump({"nav": nav, "not_in_nav": ""}), encoding="utf-8")
            entries = []
            def record(items, parents=()):
                for item in items:
                    title, value = next(iter(item.items()))
                    entries.append({"heading": title, "page": value[0] if isinstance(value, list) else value,
                                    "breadcrumb": [*parents, title]})
                    if isinstance(value, list):
                        record(value[1:], (*parents, title))
            record(nav)
            (project / "structure-map.json").write_text(json.dumps({"required_pages": entries}), encoding="utf-8")
            (project / "source-map.json").write_text(json.dumps({"pages": []}), encoding="utf-8")
            for entry in entries:
                (docs / entry["page"]).write_text("# " + entry["heading"] + "\n\nThis chapter explains the shared IVI platform.\n", encoding="utf-8")
            (docs / "required.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
            architecture = docs / "architecture-basic.md"
            original = architecture.read_text(encoding="utf-8")
            architecture.write_text(original + "\n![Architecture](required.svg)\n", encoding="utf-8")
            with redirect_stdout(StringIO()):
                validate(project)
            architecture.write_text(original, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Required architecture diagram is missing"):
                validate(project)
            architecture.write_text(original + "\n![Architecture](required.svg)\n", encoding="utf-8")
            (docs / "portfolio-basic.md").write_text("# Basic demo system\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Required narrative content is missing"):
                validate(project)


class MasterBaselineTests(unittest.TestCase):
    def test_named_release_links_are_rejected_but_recipe_selected_components_are_allowed(self):
        validate_master_references({"current.md":
            "[Docs](https://docs.automotivelinux.org/en/master/) "
            "[Recipe](https://git.automotivelinux.org/AGL/meta-agl/tree/?h=master) "
            "[Component](https://git.automotivelinux.org/src/applaunchd/tree/?id=abc)"})
        for url in ["https://docs.automotivelinux.org/en/unagi/guide/",
                    "https://git.automotivelinux.org/AGL/meta-agl/tree/?h=vimba/22.0.0"]:
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, "Non-master"):
                validate_master_references({"outdated.md": url})

    def test_legacy_content_names_resolve_to_updated_platform_chapters(self):
        pages = [("Base platform for the distributed system", "vehicle-controller/distributed/index.md"),
                 ("Base platform for the small-scale integrated system", "vehicle-controller/small-integrated/index.md"),
                 ("Base platform for the large-scale integrated system", "vehicle-controller/large-integrated/index.md")]
        for name, destination in [("AGL distributed system", "vehicle-controller/distributed/index.md"),
                                  ("AGL small-scale integrated system", "vehicle-controller/small-integrated/index.md"),
                                  ("AGL large-scale integrated system", "vehicle-controller/large-integrated/index.md")]:
            with self.subTest(name=name):
                self.assertEqual(section_paths(name, pages, {}), [destination])


class SectionCleanupTests(unittest.TestCase):
    def test_sections_end_at_siblings_and_headings_in_code_are_preserved(self):
        fence = chr(96) * 3
        before = "# Guide\n\n" + fence + "\n## Further reading\nexample\n" + fence + "\n\n## Work\nKeep this procedure.\n\n"
        section = "## Further reading\n\n[Unused](unused.md)\n\n### Nested references\nRemove these too.\n\n"
        after = "## Next task\nKeep the next task.\n"
        self.assertEqual(remove_further_reading(before + section + after), before + after)
        self.assertEqual(remove_further_reading("Text without a section"), "Text without a section")


class ImportPreservationTests(unittest.TestCase):
    def test_import_destinations_match_the_current_source_map(self):
        project = Path(__file__).resolve().parents[1]
        manifest = json.loads((project / "source-map.json").read_text(encoding="utf-8"))
        destinations = {entry["source"]: entry["destination"]
                        for entry in manifest["pages"] + manifest["excluded_pages"]}
        self.assertEqual(import_docs.MAPPING, destinations)

    def test_reimport_preserves_moved_pages_and_links_between_platforms(self):
        with TemporaryDirectory() as directory:
            base = Path(directory)
            source, project = base / "source", base / "project"
            source.mkdir()
            project.mkdir()
            mapping = {"quickstart.md": "vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md",
                       "distributed.md": "distributed/guide.md",
                       "small.md": "small-integrated/guide.md",
                       "large.md": "large-integrated/guide.md"}
            (project / "structure-map.json").write_text(json.dumps({
                "required_pages": [], "moved_pages": [
                    {"old": "standalone/guide.md", "new": "distributed/guide.md"},
                    {"old": "integrated/guide.md", "new": "small-integrated/guide.md"},
                ],
            }), encoding="utf-8")
            (source / "quickstart.md").write_text(
                "### QEMU x86-64\n[Distributed](distributed.md)\n"
                "[Small](small.md)\n[Large](large.md)\n", encoding="utf-8")
            preserved = {}
            for origin, destination in mapping.items():
                if origin == "quickstart.md":
                    continue
                (source / origin).write_text("# Upstream guide\nUpdated source.\n", encoding="utf-8")
                target = project / "docs" / destination
                target.parent.mkdir(parents=True, exist_ok=True)
                curated = ("---\ncontent_status: adapted\nsource_path: " + origin
                           + "\n---\n# Curated guide\nKeep local corrections.\n")
                target.write_text(curated, encoding="utf-8")
                preserved[target] = curated
            with patch.object(import_docs, "PROJECT", project), patch.object(import_docs, "MAPPING", mapping), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", {}), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            for target, curated in preserved.items():
                self.assertEqual(target.read_text(encoding="utf-8"), curated)
            qemu = (project / "docs/vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/qemu-x86-64/index.md").read_text(encoding="utf-8")
            for destination in list(mapping.values())[1:]:
                self.assertIn("(" + posixpath.relpath(destination, "vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/qemu-x86-64") + ")", qemu)
            self.assertFalse((project / "docs/standalone").exists())
            self.assertFalse((project / "docs/integrated").exists())

    def test_default_import_preserves_adaptations_and_refreshes_unadapted_pages(self):
        with TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source"
            project = base / "project"
            project.mkdir()
            (project / "structure-map.json").write_text(json.dumps({"required_pages": [], "moved_pages": []}), encoding="utf-8")
            mapping = {"quickstart.md": "vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md", "ordinary.md": "ordinary.md"}
            source.mkdir()
            (source / "quickstart.md").write_text("### QEMU x86-64\nqemu-system-x86_64 --version\n", encoding="utf-8")
            (source / "ordinary.md").write_text("# Updated source\nNew imported content.\n", encoding="utf-8")
            overview = project / "docs/vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md"
            overview.parent.mkdir(parents=True)
            curated = "---\ncontent_status: adapted\nsource_path: quickstart.md\n---\n# Curated overview\nPreserve the corrected procedure.\n"
            overview.write_text(curated, encoding="utf-8")
            qemu = project / "docs/vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/qemu-x86-64/index.md"
            corrected = "---\ncontent_status: adapted\nsource_path: quickstart.md\n---\n# Corrected QEMU\nModern command.\n"
            qemu.parent.mkdir(parents=True, exist_ok=True)
            qemu.write_text(corrected, encoding="utf-8")
            ordinary = project / "docs/ordinary.md"
            ordinary.write_text("---\ncontent_status: imported\nsource_path: ordinary.md\n---\nOld content.\n", encoding="utf-8")
            with patch.object(import_docs, "PROJECT", project), patch.object(import_docs, "MAPPING", mapping), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", {}), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            self.assertEqual(overview.read_text(encoding="utf-8"), curated)
            self.assertEqual(qemu.read_text(encoding="utf-8"), corrected)
            self.assertIn("New imported content.", ordinary.read_text(encoding="utf-8"))
            self.assertTrue((project / "docs/vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/raspberry-pi/index.md").is_file())
            manifest = json.loads((project / "source-map.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["source_markdown_count"], 2)
            self.assertEqual({page["source"] for page in manifest["pages"]}, set(mapping))

    def test_reimport_keeps_excluded_pages_and_assets_removed(self):
        with TemporaryDirectory() as directory:
            base = Path(directory)
            source, project = base / "source", base / "project"
            source.mkdir()
            project.mkdir()
            (project / "structure-map.json").write_text(json.dumps({
                "required_pages": [], "moved_pages": [],
                "removed_files": [{"path": "ordinary.md"}, {"path": "assets/source/unused.png"}],
            }), encoding="utf-8")
            (source / "quickstart.md").write_text("### QEMU x86-64\n[Old overview](ordinary.md)\n![Old image](unused.png)\n", encoding="utf-8")
            (source / "ordinary.md").write_text("# Old overview\nUnused content.\n", encoding="utf-8")
            (source / "unused.png").write_bytes(b"excluded asset")
            (source / "retained.png").write_bytes(b"retained asset")
            (project / "docs").mkdir()
            (project / "docs/ordinary.md").write_text("# Stale output\n", encoding="utf-8")
            with patch.object(import_docs, "PROJECT", project), patch.object(import_docs, "MAPPING", {
                    "quickstart.md": "vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md", "ordinary.md": "ordinary.md",
                }), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", {}), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            self.assertFalse((project / "docs/ordinary.md").exists())
            self.assertFalse((project / "docs/assets/source/unused.png").exists())
            self.assertTrue((project / "docs/assets/source/retained.png").is_file())
            quickstart = (project / "docs/vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/qemu-x86-64/index.md").read_text(encoding="utf-8")
            self.assertIn("https://docs.automotivelinux.org/en/{{ agl.codename }}/ordinary/", quickstart)
            self.assertIn("https://docs.automotivelinux.org/en/{{ agl.codename }}/unused.png)", quickstart)
            manifest = json.loads((project / "source-map.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["source_markdown_count"], 2)
            self.assertEqual(manifest["imported_markdown_count"], 1)
            self.assertEqual(manifest["imported_asset_count"], 1)
            self.assertEqual(manifest["excluded_pages"][0]["destination"], "ordinary.md")
            self.assertEqual(manifest["excluded_assets"][0]["destination"], "assets/source/unused.png")

    def test_generated_quickstart_uses_the_current_required_title(self):
        with TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source"
            project = base / "project"
            source.mkdir()
            project.mkdir()
            title = "Run Flutter IVI demo pre-build image"
            required = {"vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md": title}
            (project / "structure-map.json").write_text(json.dumps({
                "required_pages": [{"page": path, "heading": heading} for path, heading in required.items()],
                "moved_pages": [],
            }), encoding="utf-8")
            (source / "quickstart.md").write_text("### QEMU x86-64\nqemu-system-x86_64 --version\n", encoding="utf-8")
            with patch.object(import_docs, "PROJECT", project), patch.object(import_docs, "MAPPING", {"quickstart.md": "vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md"}), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", required), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            from validate_structure import first_heading
            self.assertEqual(first_heading((project / "docs/vehicle-controller/distributed/agl-distribution/quick-start/prebuilt/index.md").read_text(encoding="utf-8")), title)

    def test_overwriting_an_adaptation_requires_the_explicit_option(self):
        with TemporaryDirectory() as directory:
            target = Path(directory) / "page.md"
            target.write_text("---\ncontent_status: adapted\nsource_path: source.md\n---\nCurated content.\n", encoding="utf-8")
            self.assertFalse(import_docs.write_imported_page(target, "New content", "source.md"))
            self.assertTrue(import_docs.write_imported_page(target, "New content", "source.md", overwrite_adapted=True))
            self.assertEqual(target.read_text(encoding="utf-8"), "New content")

    def test_an_adapted_page_with_different_provenance_is_not_overwritten(self):
        with TemporaryDirectory() as directory:
            target = Path(directory) / "page.md"
            target.write_text("---\ncontent_status: adapted\nsource_path: another.md\n---\nCurated content.\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "source_path"):
                import_docs.write_imported_page(target, "New content", "source.md")
            self.assertIn("Curated content.", target.read_text(encoding="utf-8"))



class DirectoryLayoutTests(unittest.TestCase):
    def test_required_directories_follow_the_navigation_parent(self):
        from validate_structure import validate_directory_layout
        validate_directory_layout([{"Home": ["index.md", {"Platform": ["platform/index.md", {"Build": "platform/build/index.md"}]}]}])
        with self.assertRaisesRegex(ValueError, "navigation parent"):
            validate_directory_layout([{"Home": ["index.md", {"Platform": ["platform/index.md", {"Build": "elsewhere/build/index.md"}]}]}])
        with self.assertRaisesRegex(ValueError, "index.md"):
            validate_directory_layout([{"Home": ["index.md", {"Build": "build.md"}]}])

    def test_rebased_markdown_keeps_assets_queries_fragments_and_fenced_examples(self):
        from documentation_paths import rebase_links
        fence = chr(96) * 3
        body = '[Guide](../guide.md?mode=1#step "Title")\n![Image](../assets/figure_(1).svg)\n[External](https://example.com/a)\n[ref]: <../guide.md#step>\n' + fence + '\n[Example](../guide.md)\n' + fence + '\n'
        rebased = rebase_links(body, 'old/page.md', 'platform/chapter/index.md', {'guide.md': 'platform/guide/index.md'})
        self.assertIn('[Guide](../guide/index.md?mode=1#step "Title")', rebased)
        self.assertIn('![Image](../../assets/figure_(1).svg)', rebased)
        self.assertIn('[External](https://example.com/a)', rebased)
        self.assertIn('[ref]: <../guide/index.md#step>', rebased)
        self.assertIn(fence + '\n[Example](../guide.md)\n' + fence, rebased)

    def test_html_urls_are_relative_to_rendered_pages(self):
        from documentation_paths import rebase_links
        body = '<a href="../../guide/#step">Guide</a><img src="../../assets/image.svg">'
        rebased = rebase_links(body, 'old/page.md', 'platform/chapter/index.md', {'guide.md': 'platform/guide/index.md'})
        self.assertIn('href="../guide/#step"', rebased)
        self.assertIn('src="../../assets/image.svg"', rebased)


if __name__ == "__main__":
    unittest.main()
