"""Rebase local Markdown and HTML URLs when documentation pages move."""
from __future__ import annotations
import posixpath
import re
from urllib.parse import quote, unquote, urlsplit


def page_route(page):
    if page == "index.md":
        return ""
    if page.endswith("/index.md"):
        return page.removesuffix("index.md")
    return page.removesuffix(".md") + "/"


def rebase_links(text, old_page, new_page, mapping=None):
    """Preserve targets, fragments, titles and fenced examples while relocating a page."""
    mapping = mapping or {}
    def convert(url, html=False):
        if "{{" in url or url.startswith(("#", "//", "/")):
            return url
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return url
        old_base = page_route(old_page) if html else posixpath.dirname(old_page)
        target = posixpath.normpath(posixpath.join(old_base, unquote(parsed.path)))
        if html:
            candidates = [target, target.rstrip("/") + "/index.md", target.rstrip("/") + ".md"]
            canonical = next((path for path in candidates if path in mapping), None)
            target = page_route(mapping[canonical]) if canonical else target
        else:
            target = mapping.get(target, target)
        new_base = page_route(new_page) if html else posixpath.dirname(new_page)
        relative = posixpath.relpath(target or ".", new_base or ".")
        if html and (target.endswith("/") or target == ""):
            relative = "./" if relative == "." else relative.rstrip("/") + "/"
        relative = quote(relative, safe="/()%:@!$&'*,;=+~-._")
        return relative + ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")

    def rewrite(block):
        edits = []
        for match in re.finditer(r"\]\(", block):
            start = match.end()
            cursor, depth = start, 1
            while cursor < len(block) and depth:
                if block[cursor] == chr(92):
                    cursor += 2
                    continue
                if block[cursor] == "(":
                    depth += 1
                elif block[cursor] == ")":
                    depth -= 1
                cursor += 1
            if depth:
                continue
            inner = block[start:cursor - 1]
            leading = len(inner) - len(inner.lstrip())
            value = inner[leading:]
            if value.startswith("<") and ">" in value:
                url_start, url_end = leading + 1, leading + value.index(">")
            else:
                end = 0
                while end < len(value):
                    if value[end:end + 2] == "{{":
                        close = value.find("}}", end + 2)
                        if close < 0:
                            break
                        end = close + 2
                    elif value[end].isspace():
                        break
                    else:
                        end += 1
                url_start, url_end = leading, leading + end
            url = inner[url_start:url_end]
            converted = convert(url)
            if converted != url:
                edits.append((start + url_start, start + url_end, converted))
        for start, end, replacement in sorted(edits, reverse=True):
            block = block[:start] + replacement + block[end:]
        block = re.sub(r"(?m)^( {0,3}\[[^]\n]+\]:[ \t]*)(<[^>]+>|\S+)",
                       lambda m: m[1] + ("<" + convert(m[2][1:-1]) + ">" if m[2].startswith("<") else convert(m[2])), block)
        return re.sub(r"((?:href|src)\s*=\s*[\"'])([^\"']+)([\"'])",
                      lambda m: m[1] + convert(m[2], html=True) + m[3], block)

    result, prose, fence = [], [], None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                result.append(rewrite("".join(prose)))
                prose = []
                fence = (marker[1][0], len(marker[1]))
            elif marker[1][0] == fence[0] and len(marker[1]) >= fence[1]:
                fence = None
            result.append(line)
        elif fence is not None:
            result.append(line)
        else:
            prose.append(line)
    result.append(rewrite("".join(prose)))
    return "".join(result)
