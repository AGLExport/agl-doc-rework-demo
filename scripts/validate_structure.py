"""Check the documentation hierarchy, titles, and article reachability against AGENTS.md."""
from __future__ import annotations
import argparse
import hashlib
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
    """Interpret quoted, scoped and unindented section content rules."""
    if '## Required Contents at Section' not in instructions:
        return {}
    section = instructions.split('## Required Contents at Section', 1)[1].split('\n## ', 1)[0]
    requirements, current, topic = {}, None, None
    lines = section.splitlines()
    for index, line in enumerate(lines):
        declaration = re.match(r'^(.+?) section must .*contents?:\s*$', line)
        bullet = re.match(r'^( *)(?:[*-] )(.+?)\s*$', line)
        if declaration:
            scoped = re.fullmatch(r'"([^"]+)" section under "([^"]+)"', declaration[1])
            name = scoped[1] if scoped else declaration[1].strip().strip(chr(34))
            parent = scoped[2] if scoped else None
            current = name + (' under ' + parent if parent else '')
            topic = None
            requirements[current] = {
                'section_title': name, 'parent': parent, 'headings': [], 'figures': [],
                'subsection_links': False, 'section_references': {}, 'paragraphs': [],
                'source_links': [], 'official_figure': False, 'required_assets': [],
            }
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
        elif current is not None and line.strip():
            # Plain outline topics use indentation for children, or precede a
            # same-level 'Figure out ...' instruction for an illustrated topic.
            outline = re.match(r'^( {2,})(\S.+\.)\s*$', line)
            following = next((item for item in lines[index + 1:] if item.strip()), '')
            following_indent = len(following) - len(following.lstrip(' '))
            if outline and (following_indent > len(outline[1]) or following.strip().startswith('Figure out ')):
                topic = outline[2].strip()
                requirements[current]['headings'].append((1 + len(outline[1]) // 2, topic))
                continue
            description = line.strip()
            if description == 'These contents should link to sub-sections.':
                requirements[current]['subsection_links'] = True
                continue
            requirements[current]['paragraphs'].append(description)
            if topic is not None and description.casefold().startswith('figure out ') and topic not in requirements[current]['figures']:
                requirements[current]['figures'].append(topic)
            reference = re.search(r'should refer to (.+?) section\.', description)
            if reference and topic is not None:
                requirements[current]['section_references'][topic] = reference[1]
            focus = re.fullmatch(r'(.+?) mainly focuses on this\.', description)
            if focus and topic is not None:
                requirements[current]['section_references'][topic] = focus[1]
            if 'official architecture diagram' in description.casefold():
                requirements[current]['official_figure'] = True
            if 'shall import from ' in description:
                requirements[current]['source_links'].extend(url.rstrip('.') for url in re.findall(r'https?://\S+', description))
            requirements[current]['required_assets'].extend(
                re.findall(r'architecture diagram "([^"]+)"', description, flags=re.IGNORECASE))
    return requirements


def local_document_links(body, page):
    targets = set()
    for url in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)', body):
        parsed = urlsplit(url.strip('<>'))
        if not parsed.scheme and not parsed.netloc and parsed.path:
            targets.add(posixpath.normpath(posixpath.join(posixpath.dirname(page), unquote(parsed.path))))
    return targets


# Content rules retain a historical coverage label and use hyphenated category names.
# Navigation always follows the exact spellings in Required Structure.
SECTION_ALIASES = {
    'AGL Coverage': 'Introduction',
    'Small-scale integrated system': 'Small scale integrated system',
    'AGL distributed system': 'Distributed system',
    'AGL small-scale integrated system': 'Small scale integrated system',
    'AGL large-scale integrated system': 'Large scale integrated system',
}


def section_paths(section, pages, structure, parent=None):
    titles = {title for title, _ in pages}
    if section not in titles:
        aliases = {alias.casefold(): title for alias, title in SECTION_ALIASES.items()}
        section = aliases.get(section.casefold(), section)
        platform_aliases = {
            'Distributed system': 'Base platform for the distributed system',
            'Small scale integrated system': 'Base platform for the small-scale integrated system',
            'Large scale integrated system': 'Base platform for the large-scale integrated system',
        }
        if section not in titles and platform_aliases.get(section) in titles:
            section = platform_aliases[section]
    # A content rule applies to every matching chapter, including repeated demo-group titles.
    paths = [path for title, path in pages if title == section]
    if parent is not None:
        scoped = {entry['page'] for entry in structure['required_pages']
                  if entry['heading'] == section and entry['breadcrumb'][-2:-1] == [parent]}
        paths = [path for path in paths if path in scoped]
    return paths


def validate_official_figure(project, docs, page, text):
    manifest = project / 'asset-sources.json'
    if not manifest.is_file():
        raise ValueError('Official architecture asset source manifest is missing')
    entries = json.loads(manifest.read_text(encoding='utf-8'))['assets']
    images = set()
    for url in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text):
        parsed = urlsplit(url)
        if not parsed.scheme and not parsed.netloc:
            images.add(posixpath.normpath(posixpath.join(posixpath.dirname(page), unquote(parsed.path))))
    for entry in entries:
        if entry['path'] in images and entry.get('publisher') == 'Automotive Grade Linux' and entry.get('source_url') and entry.get('source_page'):
            image = (docs / entry['path']).resolve()
            if not image.is_relative_to(docs.resolve()) or not image.is_file():
                raise ValueError('Official architecture asset is missing: ' + entry['path'])
            if hashlib.sha256(image.read_bytes()).hexdigest() != entry['sha256']:
                raise ValueError('Official architecture asset differs from its recorded source: ' + entry['path'])
            return
    raise ValueError('Required official architecture diagram is missing: ' + page)


def validate_master_references(text_by_path):
    """Reject named-release documentation and layer branch links on a master site."""
    for path, text in text_by_path.items():
        for match in re.finditer(r"https://docs\.automotivelinux\.org/en/([^/]+)/", text):
            if match[1] not in ("master", "{{ agl.codename }}"):
                raise ValueError("Non-master AGL documentation reference: " + path + " -> " + match[1])
        for url in re.findall(r'https://git\.automotivelinux\.org/AGL/[^\s<>"\)]+', text):
            branch = re.search(r'[?&]h=([^&#]+)', url)
            if branch and branch[1] != "master":
                raise ValueError("Non-master AGL layer reference: " + path + " -> " + branch[1])
            if chr(96) + "id=" in url:
                raise ValueError("Malformed AGL source reference: " + path)


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
    if config.get('extra', {}).get('agl', {}).get('codename') == 'master':
        validate_master_references(text_by_path)
        validate_master_references({p.relative_to(docs).as_posix(): p.read_text(encoding='utf-8')
                                    for p in (docs / 'assets/diagrams').glob('*.svg')})
    for title,path in pages:
        if path not in text_by_path:
            raise ValueError('Required document is missing: '+path)
        if first_heading(text_by_path[path]) != title:
            raise ValueError('Required page heading differs: '+path)
    for path, body in text_by_path.items():
        if sum(level == 1 for level, _ in markdown_headings(body)) != 1:
            raise ValueError('Each article must have exactly one H1: ' + path)
        if any(title.casefold() == 'further reading' for _, title in markdown_headings(body)):
            raise ValueError('Further reading section must be removed: ' + path)
    structure = json.loads((project/'structure-map.json').read_text(encoding='utf-8'))
    removed = {entry['path'] for entry in structure.get('removed_files', [])}
    if removed & set(nav_paths):
        raise ValueError('A required navigation page is listed as removed')
    for path in removed:
        target = (docs / path).resolve()
        if not target.is_relative_to(docs.resolve()):
            raise ValueError('Removed file path is outside docs: ' + path)
        if target.exists():
            raise ValueError('An explicitly removed file has reappeared: ' + path)
    for section, rules in content_requirements(instructions).items():
        paths = section_paths(rules['section_title'], pages, structure, rules['parent'])
        required = rules['headings']
        if not paths or not (required or rules['paragraphs']):
            raise ValueError('Required content section is missing: ' + section)
        for path in paths:
            required_titles = {title for _, title in required}
            blocks = markdown_sections(text_by_path[path])
            actual_content = [(level, title) for level, title, _ in blocks if title in required_titles]
            if actual_content != required:
                raise ValueError('Required section content differs: ' + section + ' (headings, order, or levels changed)')
            if rules['paragraphs'] and not any(len(line.split()) >= 5 and not line.lstrip().startswith(('#', '!', '[', '-', '*', '<', '|', '```')) for _, _, body in blocks for line in body.splitlines()):
                raise ValueError('Required narrative content is missing: ' + section)
            for source_url in rules['source_links']:
                if source_url not in text_by_path[path]:
                    raise ValueError('Required source attribution is missing: ' + section)
            if rules['official_figure']:
                validate_official_figure(project, docs, path, text_by_path[path])
            for filename in rules['required_assets']:
                images = []
                for url in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text_by_path[path]):
                    parsed = urlsplit(url)
                    if not parsed.scheme and not parsed.netloc:
                        image = (docs / posixpath.dirname(path) / unquote(parsed.path)).resolve()
                        if image.is_relative_to(docs.resolve()):
                            images.append(image)
                if not any(image.name == filename and image.is_file() for image in images):
                    raise ValueError('Required architecture diagram is missing: ' + section + ' -> ' + filename)
            by_title = {title: body for _, title, body in blocks}
            for title in rules['figures']:
                if not re.search(r'!\[[^\]]*\]\(|<img\b', by_title[title]):
                    raise ValueError('Required architecture figure is missing: ' + title)
            for topic, referenced_section in rules['section_references'].items():
                referenced_paths = section_paths(referenced_section, pages, structure)
                if len(referenced_paths) != 1 or referenced_paths[0] not in local_document_links(by_title[topic], path):
                    raise ValueError('Required section reference is missing: ' + topic + ' -> ' + referenced_section)
            if rules['subsection_links']:
                for index, (level, title) in enumerate(required):
                    if index + 1 < len(required) and required[index + 1][0] > level:
                        continue
                    targets = local_document_links(by_title[title], path)
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
    excluded = manifest.get('excluded_pages', [])
    if any(entry['destination'] not in removed for entry in excluded):
        raise ValueError('Excluded source page is not recorded as removed')
    if manifest.get('source_markdown_count', len(destinations) + len(excluded)) != len(destinations) + len(excluded):
        raise ValueError('Source article count differs from active and excluded mappings')
    if manifest.get('imported_markdown_count', len(destinations)) != len(destinations):
        raise ValueError('Imported article count differs from active mappings')
    excluded_assets = manifest.get('excluded_assets', [])
    if any(entry['destination'] not in removed for entry in excluded_assets):
        raise ValueError('Excluded source asset is not recorded as removed')
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
