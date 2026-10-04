"""Add the GitHub Pages marker after a successful MkDocs build."""
from pathlib import Path

def on_post_build(config, **kwargs):
    (Path(config["site_dir"]) / ".nojekyll").write_text("", encoding="utf-8")
