"""Check the documentation hierarchy, titles, and article reachability against AGENTS.md."""
from __future__ import annotations
import argparse
import json
import posixpath
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
import yaml


def required_tree(text):
    section = text.split('## Required Structure', 1)[1]
    roots, stack = [], []
    for line in section.splitlines():
        match = re.match(r'^( *)(?:- )(.+?)\s*$', line)
        if not match:
            continue
        depth = len(match[1]) // 2
        node = {'title': match[2].strip(), 'children': []}
        if depth == 0:
            roots.append(node)
            stack = [node]
        else:
            if depth > len(stack):
                raise ValueError('Invalid hierarchy indentation in AGENTS.md')
            stack = stack[:depth]
            stack[-1]['children'].append(node)
            stack.append(node)
    return roots


def navigation_tree(items, pages):
    result = []
    for item in items:
        if not isinstance(item, dict) or len(item) != 1:
            raise ValueError('Navigation headings must use one named entry each')
        title, value = next(iter(item.items()))
        if isinstance(value, list):
            if not value or not isinstance(value[0], str):
                raise ValueError('Chapter has no index page: '+title)
            pages.append((title, value[0]))
            children = navigation_tree(value[1:], pages)
        elif isinstance(value, str):
            pages.append((title, value))
            children = []
        else:
            raise ValueError('Invalid navigation value for '+title)
        result.append({'title':title, 'children':children})
    return result


def first_heading(text):
    fence = None
    for line in text.splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})',line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif fence == marker[1][0]:
                fence = None
        elif fence is None and re.match(r'^#\s+',line):
            return re.sub(r'^#\s+','',line).strip()
    return None


def validate(project):
    project = project.resolve()
    docs = project / 'docs'
    expected = required_tree((project/'AGENTS.md').read_text(encoding='utf-8-sig'))
    config = yaml.load((project/'mkdocs.yml').read_text(encoding='utf-8-sig'), Loader=yaml.BaseLoader)
    pages = []
    actual = navigation_tree(config['nav'],pages)
    if actual != expected:
        raise ValueError('Navigation differs from AGENTS.md: headings, order, or nesting changed')
    nav_paths = [path for _,path in pages]
    if len(set(nav_paths)) != len(nav_paths):
        raise ValueError('A document is duplicated in the required navigation')
    text_by_path = {p.relative_to(docs).as_posix():p.read_text(encoding='utf-8-sig') for p in docs.rglob('*.md')}
    for title,path in pages:
        if path not in text_by_path:
            raise ValueError('Required document is missing: '+path)
        if first_heading(text_by_path[path]) != title:
            raise ValueError('Required page heading differs: '+path)
    secondary = set(text_by_path)-set(nav_paths)
    declared = {line.strip().removeprefix('/') for line in config.get('not_in_nav','').splitlines() if line.strip()}
    if secondary != declared:
        raise ValueError('Supporting-page declarations do not match the actual documents')
    reachable = set(nav_paths)
    pending = list(nav_paths)
    while pending:
        path = pending.pop()
        for url in re.findall(r'\]\(([^\s)]+)',text_by_path[path]):
            if '{{' in url:
                continue
            parsed = urlsplit(url.strip('<>'))
            if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith('/'):
                continue
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path),unquote(parsed.path)))
            if target in text_by_path and target not in reachable:
                reachable.add(target)
                pending.append(target)
    if reachable != set(text_by_path):
        raise ValueError('Documents are not reachable from chapter pages: '+', '.join(sorted(set(text_by_path)-reachable)))
    manifest = json.loads((project/'source-map.json').read_text(encoding='utf-8'))
    destinations = [p['destination'] for p in manifest['pages']]
    if len(set(destinations)) != len(destinations) or not set(destinations).issubset(text_by_path):
        raise ValueError('Source article mappings are missing or duplicated')
    structure = json.loads((project/'structure-map.json').read_text(encoding='utf-8'))
    if [(p['heading'],p['page']) for p in structure['required_pages']] != pages:
        raise ValueError('Structure map differs from navigation')
    print(f'Validated {len(pages)} required headings, {len(text_by_path)} reachable articles, and {len(destinations)} source mappings.')
    return len(pages),len(text_by_path),len(destinations)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project',nargs='?',type=Path,default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        validate(args.project)
    except (ValueError,KeyError,IndexError) as error:
        parser.exit(1,'Structure validation failed: '+str(error)+'\n')
