"""Regression checks for required-section resolution and import preservation."""
from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import import_docs
import yaml
from validate_structure import content_requirements, section_paths, validate
from import_transforms import remove_further_reading


class SectionResolutionTests(unittest.TestCase):
    def test_historical_coverage_reference_resolves_to_background(self):
        self.assertEqual(section_paths("AGL Coverage", [("Background", "home/index.md")], {}), ["home/index.md"])

    def test_hyphenated_content_rule_resolves_to_exact_navigation_spelling(self):
        pages = [("Small scale integrated system", "integrated/index.md")]
        self.assertEqual(section_paths("Small-scale integrated system", pages, {}), ["integrated/index.md"])
        self.assertEqual(section_paths("AGL small-scale integrated system", pages, {}), ["integrated/index.md"])

    def test_ambiguous_sections_are_not_silently_selected(self):
        pages = [("SoDeV", "first.md"), ("SoDeV", "second.md")]
        self.assertEqual(section_paths("SoDeV", pages, {}), ["first.md", "second.md"])


class ContentRequirementTests(unittest.TestCase):
    def test_updated_instructions_require_figures_and_matching_system_links(self):
        instructions = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rules = content_requirements(instructions)
        self.assertIn("Home", rules)
        self.assertEqual(rules["Home"]["section_references"]["What is AGL."], "AGL Coverage")
        background = rules["Background"]
        self.assertEqual(background["figures"], [
            "Traditional distributed architecture.", "Domain architecture.", "Central/Zone architecture.",
        ])
        expected_paths = ["standalone/index.md", "integrated/index.md", "integrated/large-scale.md"]
        pages = [("Distributed system", expected_paths[0]),
                 ("Small scale integrated system", expected_paths[1]),
                 ("Large scale integrated system", expected_paths[2])]
        self.assertEqual([section_paths(name, pages, {})[0]
                          for name in background["section_references"].values()], expected_paths)

    def test_official_figure_and_source_requirement_belong_to_large_scale(self):
        instructions = (Path(__file__).resolve().parents[1] / "AGENTS.md").read_text(encoding="utf-8-sig")
        rules = content_requirements(instructions)
        self.assertTrue(rules["Large scale integrated system"]["official_figure"])
        self.assertEqual(len(rules["Large scale integrated system"]["source_links"]), 1)
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


class SectionCleanupTests(unittest.TestCase):
    def test_sections_end_at_siblings_and_headings_in_code_are_preserved(self):
        fence = chr(96) * 3
        before = "# Guide\n\n" + fence + "\n## Further reading\nexample\n" + fence + "\n\n## Work\nKeep this procedure.\n\n"
        section = "## Further reading\n\n[Unused](unused.md)\n\n### Nested references\nRemove these too.\n\n"
        after = "## Next task\nKeep the next task.\n"
        self.assertEqual(remove_further_reading(before + section + after), before + after)
        self.assertEqual(remove_further_reading("Text without a section"), "Text without a section")


class ImportPreservationTests(unittest.TestCase):
    def test_default_import_preserves_adaptations_and_refreshes_unadapted_pages(self):
        with TemporaryDirectory() as directory:
            base = Path(directory)
            source = base / "source"
            project = base / "project"
            project.mkdir()
            (project / "structure-map.json").write_text(json.dumps({"required_pages": [], "moved_pages": []}), encoding="utf-8")
            mapping = {"quickstart.md": "start/prebuilt/index.md", "ordinary.md": "ordinary.md"}
            source.mkdir()
            (source / "quickstart.md").write_text("### QEMU x86-64\nqemu-system-x86_64 --version\n", encoding="utf-8")
            (source / "ordinary.md").write_text("# Updated source\nNew imported content.\n", encoding="utf-8")
            overview = project / "docs/start/prebuilt/index.md"
            overview.parent.mkdir(parents=True)
            curated = "---\ncontent_status: adapted\nsource_path: quickstart.md\n---\n# Curated overview\nPreserve the corrected procedure.\n"
            overview.write_text(curated, encoding="utf-8")
            qemu = project / "docs/start/prebuilt/qemu-x86-64.md"
            corrected = "---\ncontent_status: adapted\nsource_path: quickstart.md\n---\n# Corrected QEMU\nModern command.\n"
            qemu.write_text(corrected, encoding="utf-8")
            ordinary = project / "docs/ordinary.md"
            ordinary.write_text("---\ncontent_status: imported\nsource_path: ordinary.md\n---\nOld content.\n", encoding="utf-8")
            with patch.object(import_docs, "PROJECT", project), patch.object(import_docs, "MAPPING", mapping), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", {}), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            self.assertEqual(overview.read_text(encoding="utf-8"), curated)
            self.assertEqual(qemu.read_text(encoding="utf-8"), corrected)
            self.assertIn("New imported content.", ordinary.read_text(encoding="utf-8"))
            self.assertTrue((project / "docs/start/prebuilt/raspberry-pi.md").is_file())
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
                    "quickstart.md": "start/prebuilt/index.md", "ordinary.md": "ordinary.md",
                }), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", {}), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            self.assertFalse((project / "docs/ordinary.md").exists())
            self.assertFalse((project / "docs/assets/source/unused.png").exists())
            self.assertTrue((project / "docs/assets/source/retained.png").is_file())
            quickstart = (project / "docs/start/prebuilt/qemu-x86-64.md").read_text(encoding="utf-8")
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
            required = {"start/prebuilt/index.md": title}
            (project / "structure-map.json").write_text(json.dumps({
                "required_pages": [{"page": path, "heading": heading} for path, heading in required.items()],
                "moved_pages": [],
            }), encoding="utf-8")
            (source / "quickstart.md").write_text("### QEMU x86-64\nqemu-system-x86_64 --version\n", encoding="utf-8")
            with patch.object(import_docs, "PROJECT", project), patch.object(import_docs, "MAPPING", {"quickstart.md": "start/prebuilt/index.md"}), patch.object(import_docs, "TITLES", {}), patch.object(import_docs, "REQUIRED_TITLES", required), redirect_stdout(StringIO()):
                import_docs.import_all(source)
            from validate_structure import first_heading
            self.assertEqual(first_heading((project / "docs/start/prebuilt/index.md").read_text(encoding="utf-8")), title)

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


if __name__ == "__main__":
    unittest.main()
