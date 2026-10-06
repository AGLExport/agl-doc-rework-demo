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
    section = text.split('## Required Structure', 1)[1].split('\n## ', 1)[0]
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


def markdown_sections(text):
    lines = text.splitlines()
    headings, fence = [], None
    for index, line in enumerate(lines):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif fence == marker[1][0]:
                fence = None
        elif fence is None:
            heading = re.match(r'^(#{1,6})\s+(.+?)\s*$', line)
            if heading:
                headings.append((len(heading[1]), heading[2], index))
    return [(level, title, '\n'.join(lines[start + 1:headings[i + 1][2] if i + 1 < len(headings) else len(lines)])) for i, (level, title, start) in enumerate(headings)]


def markdown_headings(text):
    return [(level, title) for level, title, _ in markdown_sections(text)]


def first_heading(text):
    return next((title for level, title in markdown_headings(text) if level == 1), None)


def content_requirements(instructions):
    """Interpret content topics, including indented figure and overview descriptions."""
    if '## Required Contents at Section' not in instructions:
        return {}
    section = instructions.split('## Required Contents at Section', 1)[1].split('\n## ', 1)[0]
    requirements, current, topic = {}, None, None
    for line in section.splitlines():
        declaration = re.match(r'^(.+?) section must .*contents:\s*$', line)
        bullet = re.match(r'^( *)(?:[*-] )(.+?)\s*$', line)
        if declaration:
            current = declaration[1]
            topic = None
            requirements[current] = {'headings': [], 'figures': [], 'subsection_links': False}
        elif current is not None and bullet:
            title = bullet[2]
            figure = title.endswith(' with figure.')
            if figure:
                title = title.removesuffix(' with figure.') + '.'
            if ". It's " in title:
                title = title.split(". It's ", 1)[0] + '.'
            topic = title
            requirements[current]['headings'].append((2 + len(bullet[1]) // 2, title))
            if figure:
                requirements[current]['figures'].append(title)
        elif current is not None and topic is not None and line[:1].isspace() and line.strip():
            if line.strip().casefold().startswith('figure out for ') and topic not in requirements[current]['figures']:
                requirements[current]['figures'].append(topic)
        elif current is not None and line.strip() == 'These contents should link to sub-sections.':
            requirements[current]['subsection_links'] = True
        elif line.strip():
            current, topic = None, None
    return requirements


def validate(project):
    project = project.resolve()
    docs = project / 'docs'
    instructions = (project/'AGENTS.md').read_text(encoding='utf-8-sig')
    expected = required_tree(instructions)
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
    for section, rules in content_requirements(instructions).items():
        paths = [path for title, path in pages if title == section]
        required = rules['headings']
        if len(paths) != 1 or not required:
            raise ValueError('Required content section is missing or ambiguous: ' + section)
        path = paths[0]
        required_titles = {title for _, title in required}
        blocks = markdown_sections(text_by_path[path])
        actual_content = [(level, title) for level, title, _ in blocks if title in required_titles]
        if actual_content != required:
            raise ValueError('Required section content differs: ' + section + ' (headings, order, or levels changed)')
        by_title = {title: body for _, title, body in blocks}
        for title in rules['figures']:
            if not re.search(r'!\[[^\]]*\]\(|<img\b', by_title[title]):
                raise ValueError('Required architecture figure is missing: ' + title)
        if rules['subsection_links']:
            for index, (level, title) in enumerate(required):
                if index + 1 < len(required) and required[index + 1][0] > level:
                    continue
                targets = set()
                for url in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)', by_title[title]):
                    parsed = urlsplit(url.strip('<>'))
                    if not parsed.scheme and not parsed.netloc and parsed.path:
                        targets.add(posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(parsed.path))))
                descendants = {p for p in nav_paths if p != path and p.startswith(posixpath.dirname(path) + '/')}
                if not targets & descendants:
                    raise ValueError('Required subsection link is missing: ' + title)
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
