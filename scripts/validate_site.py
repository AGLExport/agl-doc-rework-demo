#!/usr/bin/env python3
"""Validate generated HTML links without accessing the network.

Usage: python scripts/validate_site.py SITE_DIR [--site-url URL]
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
import os
import sys
from urllib.parse import unquote, urlsplit


@dataclass
class Page:
    anchors: set[str] = field(default_factory=set)
    links: list[tuple[str, str]] = field(default_factory=list)


def srcset_urls(value: str) -> list[str]:
    """Read srcset candidates, retaining commas inside data URLs."""
    urls: list[str] = []
    pos = 0
    while pos < len(value):
        while pos < len(value) and (value[pos].isspace() or value[pos] == ","):
            pos += 1
        start = pos
        while pos < len(value) and not value[pos].isspace():
            pos += 1
        token = value[start:pos]
        if not token:
            break
        trailing_comma = token.endswith(",")
        token = token.rstrip(",")
        if token:
            if token.lower().startswith("data:"):
                urls.append(token)
            else:
                urls.extend(part for part in token.split(",") if part)
        if trailing_comma:
            continue
        # Skip width/density descriptors until the next candidate.
        parentheses = 0
        while pos < len(value):
            char = value[pos]
            pos += 1
            if char == "(":
                parentheses += 1
            elif char == ")" and parentheses:
                parentheses -= 1
            elif char == "," and not parentheses:
                break
    return urls


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.page = Page()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if value is None:
                continue
            if name == "id" or (tag == "a" and name == "name"):
                self.page.anchors.add(value)
            if name in {"href", "src"}:
                self.page.links.append((name, value))
            elif name == "srcset":
                self.page.links.extend(("srcset", url) for url in srcset_urls(value))

    handle_startendtag = handle_starttag


def is_inside(path: Path, root: Path) -> bool:
    return path.is_relative_to(root)


class Validator:
    def __init__(self, root: Path, site_url: str | None) -> None:
        self.root = root.resolve()
        self.pages: dict[Path, Page] = {}
        self.html_pages: dict[Path, Page] = {}
        self.files: set[str] = set()
        self.directories: set[str] = set()
        self.targets: dict[str, tuple[Path | None, str | None]] = {}
        self.errors: list[tuple[str, str, str]] = []
        self.counts: Counter[str] = Counter()
        self.site = urlsplit(site_url) if site_url else None
        self.prefix = (self.site.path.rstrip("/") + "/") if self.site else "/"

    def error(self, source: Path, url: str, reason: str) -> None:
        try:
            label = source.relative_to(self.root).as_posix()
        except ValueError:
            label = str(source)
        self.errors.append((label, url, reason))

    @staticmethod
    def path_key(path: Path) -> str:
        # Lexical normalization does not issue filesystem requests on UNC paths.
        return os.path.normcase(os.path.normpath(str(path)))

    def read_pages(self) -> None:
        sources: list[Path] = []
        # Collect file/directory names once; do not stat every navigation target.
        for directory, children, filenames in os.walk(self.root, followlinks=False):
            parent = Path(directory)
            resolved_parent = parent.resolve()
            if not is_inside(resolved_parent, self.root):
                children[:] = []
                self.error(parent, "", "directory link resolves outside the site directory")
                continue
            self.directories.add(self.path_key(parent))
            self.directories.add(self.path_key(resolved_parent))
            for filename in filenames:
                source = parent / filename
                self.files.add(self.path_key(source))
                if source.suffix.lower() in {".html", ".htm"}:
                    sources.append(source)
        for source in sorted(sources):
            resolved = source.resolve()
            if not is_inside(resolved, self.root):
                self.error(source, "", "HTML symlink resolves outside the site directory")
                self.targets[self.path_key(source)] = (
                    None, "HTML symlink resolves outside the site directory"
                )
                continue
            try:
                parser = PageParser()
                parser.feed(source.read_text(encoding="utf-8"))
                parser.close()
                self.pages[source] = parser.page
                self.html_pages[resolved] = parser.page
                self.targets[self.path_key(source)] = (resolved, None)
            except (OSError, UnicodeError) as exc:
                self.error(source, "", f"cannot read HTML: {exc}")

    def resolve_target(self, candidate: Path) -> tuple[Path | None, str | None]:
        key = self.path_key(candidate)
        cached = self.targets.get(key)
        if cached is not None:
            return cached
        try:
            target = Path(os.path.normpath(str(candidate))).resolve()
            if not is_inside(target, self.root):
                result = (None, "target resolves outside the site directory")
            else:
                if self.path_key(target) in self.directories:
                    target = (target / "index.html").resolve()
                if not is_inside(target, self.root):
                    result = (None, "index symlink resolves outside the site directory")
                elif self.path_key(target) not in self.files:
                    result = (None, "target does not exist")
                else:
                    result = (target, None)
        except (OSError, ValueError) as exc:
            result = (None, f"invalid local target: {exc}")
        self.targets[key] = result
        return result

    def strip_prefix(self, path: str) -> str | None:
        """Map host-root paths into this site's project directory."""
        if not self.site:
            return path.lstrip("/")
        if path == self.prefix.rstrip("/"):
            return ""
        if path.startswith(self.prefix):
            return path[len(self.prefix):]
        self.counts["outside_prefix"] += 1
        return None

    def check_link(self, source: Path, attr: str, raw_url: str) -> None:
        url = raw_url.strip()
        if not url:
            return
        if any(marker in url for marker in ("{{", "{%", "{#")):
            self.error(source, raw_url, f"unexpanded template in {attr}")
            return
        try:
            parts = urlsplit(url)
        except ValueError as exc:
            self.error(source, raw_url, f"invalid URL: {exc}")
            return

        if parts.scheme or parts.netloc:
            same_host = (
                self.site is not None
                and parts.scheme.lower() in {"", "http", "https"}
                and parts.netloc.lower() == self.site.netloc.lower()
            )
            if not same_host:
                self.counts["external"] += 1
                return
            relative = self.strip_prefix(parts.path or "/")
            if relative is None:
                return
            candidate = self.root / unquote(relative)
        elif parts.path.startswith("/"):
            relative = self.strip_prefix(parts.path)
            if relative is None:
                return
            candidate = self.root / unquote(relative)
        elif parts.path:
            candidate = source.parent / unquote(parts.path)
        else:
            candidate = source

        self.counts["local"] += 1
        target, failure = self.resolve_target(candidate)
        if failure:
            self.error(source, raw_url, failure)
            return
        assert target is not None

        fragment = unquote(parts.fragment)
        if fragment and target.suffix.lower() in {".html", ".htm"}:
            page = self.html_pages.get(target)
            if page is None:
                self.error(source, raw_url, "target HTML could not be parsed")
            elif fragment not in page.anchors:
                self.error(source, raw_url, f"anchor #{fragment} does not exist")

    def run(self) -> int:
        self.read_pages()
        if not self.pages:
            self.error(self.root, "", "no HTML pages found")
        for source, page in self.pages.items():
            # Repeated navigation links in a page need only one check.
            for attr, url in sorted(set(page.links)):
                self.check_link(source, attr, url)
        for source, url, reason in self.errors[:100]:
            print(f"ERROR {source}: {url!r}: {reason}")
        if len(self.errors) > 100:
            print(f"... {len(self.errors) - 100} additional errors omitted")
        print(
            f"Checked {len(self.pages)} HTML pages, "
            f"{self.counts['local']} unique local links; "
            f"skipped {self.counts['external']} external links and "
            f"{self.counts['outside_prefix']} links outside the site URL prefix. "
            f"Errors: {len(self.errors)}."
        )
        return 1 if self.errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site_dir", type=Path, help="directory containing generated HTML")
    parser.add_argument("--site-url", help="canonical site URL, e.g. https://org.github.io/repo/")
    args = parser.parse_args()
    if not args.site_dir.is_dir():
        parser.error(f"site directory does not exist: {args.site_dir}")
    if args.site_url:
        try:
            site = urlsplit(args.site_url)
        except ValueError as exc:
            parser.error(f"invalid --site-url: {exc}")
        if site.scheme.lower() not in {"http", "https"} or not site.netloc:
            parser.error("--site-url must be an absolute HTTP(S) URL")
        if site.query or site.fragment:
            parser.error("--site-url must not include a query or fragment")
    return Validator(args.site_dir, args.site_url).run()


if __name__ == "__main__":
    sys.exit(main())
