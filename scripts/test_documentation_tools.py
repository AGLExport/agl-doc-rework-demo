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
from validate_structure import section_paths


class SectionResolutionTests(unittest.TestCase):
    def test_shared_titles_resolve_to_the_artifact_overview(self):
        pages = [("SoDeV", "home/integrated/sodev.md"), ("SoDeV", "integrated/sodev/index.md")]
        structure = {"required_pages": [
            {"heading": "SoDeV", "page": pages[0][1], "breadcrumb": ["Home", "AGL Artifact", "Base platform for integrated system", "SoDeV"]},
            {"heading": "SoDeV", "page": pages[1][1], "breadcrumb": ["Home", "AGL integrated system", "SoDeV"]},
        ]}
        self.assertEqual(section_paths("SoDeV", pages, structure), [pages[0][1]])

    def test_historical_coverage_reference_resolves_to_the_required_artifact(self):
        self.assertEqual(section_paths("AGL Coverage", [("AGL Artifact", "home/index.md")], {}), ["home/index.md"])


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
