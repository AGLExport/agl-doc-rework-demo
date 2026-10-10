---
title: Contribute to the documentation
source_path: 07_How_To_Contribute/09_Adding_Documentation.md
content_status: adapted
agl_branch: master
last_reviewed: '2026-10-10'
---

# Contribute to the documentation

This guide covers the English documentation site built with MkDocs and Material
for MkDocs and published on GitHub Pages. Edit this site's `docs/` directory,
validate the result locally, and submit a pull request to the repository that
publishes the site.

The original AGL documentation has its own repository and review workflow.
See [Contribute to the original AGL documentation](#contribute-to-the-original-agl-documentation)
when the change should go upstream.

## Choose the repository and working directory

The current publishing repository is
[AGLExport/agl-doc-rework-demo](https://github.com/AGLExport/agl-doc-rework-demo).
Clone that repository, or your fork if you do not have permission to push a
feature branch there. For the current repository:

```sh
git clone https://github.com/AGLExport/agl-doc-rework-demo.git
cd agl-doc-rework-demo
git checkout -b docs/improve-guide
```

If you already have a checkout, create the feature branch there.
Run the documentation commands below from the **site directory** containing
`mkdocs.yml`, `requirements.txt`, and `AGENTS.md`. In a standalone site
repository, this is the repository root. In the original documentation workspace,
change into `GitHubPages/` first.

## Directory structure

| Path in the site directory | Purpose |
| --- | --- |
| `AGENTS.md` | Required English headings, hierarchy, and section content |
| `mkdocs.yml` | Exact navigation, Material theme, shared release values, and supporting-page declarations |
| `docs/index.md` | Home page |
| `docs/introduction/` | Introduction, vehicle E/E architecture context and E2E data processing |
| `docs/vehicle-controller/distributed/agl-distribution/` | Quickstarts, demo portfolios, architecture, builds, components, customization and application development |
| `docs/vehicle-controller/small-integrated/` | Container and KVM integration, including their components |
| `docs/vehicle-controller/large-integrated/sodev/` | SoDeV architecture, builds, customization and Unified HMI |
| `docs/vehicle-data/` | Connected Gateway and vehicle data processing |
| `docs/development/` | Development tools and demo control |
| `docs/virtual-car/` | CAN definitions and virtual-car signal references |
| `docs/troubleshooting/`, `docs/community/` | Troubleshooting, releases, migration and contribution guides |
| `docs/assets/` | Site images and other assets |
| `structure-map.json` | Required heading-to-page mapping |
| `source-map.json` | Original article paths and source hashes |
| `scripts/` | Import utilities and structure/link validators |
| `requirements.txt` | Pinned Python build dependencies |
| `.github/workflows/pages.yml` | Build, validation, and Pages deployment workflow |
| `site/` | Generated HTML output; excluded from Git |

Use descriptive, lowercase paths. Each required heading has a directory with
`index.md` directly below its navigation parent; Home uses `docs/index.md`.
Keep supporting articles in the relevant chapter's `reference/` directory and
shared assets in `docs/assets/`.

## Install the build environment

Install Git and Python 3.12 with `pip` and `venv` support. Create an isolated
environment and install the pinned dependencies from the site directory.

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Linux or macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

These commands do not require administrator privileges.

## Edit an article

Read `AGENTS.md` before editing. Preserve every required navigation heading,
their spelling, order, and hierarchy. Each required page must use its required
heading as its first H1. Preserve the required section contents, architecture
figures, references, and links to subsections.

Keep the front matter at the start of an article and write the body in English:

```markdown
---
title: "Required heading"
---

# Required heading
```

For an imported article, keep its existing `source_path` and mark a locally
adapted procedure with `content_status: adapted`. This records that its content
has been maintained for this site.

Use relative Markdown links, including a fragment when linking to a section:

```markdown
[Contribution gide](../index.md)
[Collect diagnostic information](../../../troubleshooting/reference/diagnostics.md)
```

Include prerequisites, the relevant AGL release or source revision, exact
commands, and a way to check the result when changing a procedure. Check
technical claims against official project documentation or source code.

If a supporting article is necessary, link it from its chapter and declare
its path in `not_in_nav` in `mkdocs.yml`. Do not add an extra heading to the
required navigation. Update `structure-map.json` if a required page moves.
Change shared release and artifact-channel values in `mkdocs.yml` rather
than inserting conflicting release values into individual guides.

The importer is a manual migration utility and is not part of the normal edit
or build workflow. It preserves articles marked `content_status: adapted`;
`--overwrite-adapted` deliberately replaces them. Keep source provenance and
import mappings consistent when maintaining imported material.

## Preview the site

PowerShell:

```powershell
$env:MKDOCS_SITE_URL = 'http://127.0.0.1:8000/'
.\.venv\Scripts\python.exe -m mkdocs serve --config-file mkdocs.yml
```

Linux or macOS:

```bash
export MKDOCS_SITE_URL=http://127.0.0.1:8000/
.venv/bin/python -m mkdocs serve --config-file mkdocs.yml
```

Open <http://127.0.0.1:8000/>. Check the edited pages, code blocks, tables,
images, and the route from their chapter page. Stop the preview with Ctrl+C
before running the build below.

## Build and validate

Use the same site URL for the build and generated-link validator.

PowerShell:

```powershell
$env:MKDOCS_SITE_URL = 'http://127.0.0.1:8000/'
.\.venv\Scripts\python.exe scripts\test_documentation_tools.py
.\.venv\Scripts\python.exe scripts\validate_structure.py
.\.venv\Scripts\python.exe -m mkdocs build --strict --config-file mkdocs.yml
.\.venv\Scripts\python.exe scripts\validate_site.py site --site-url "$env:MKDOCS_SITE_URL"
git diff --check
```

Linux or macOS:

```bash
export MKDOCS_SITE_URL=http://127.0.0.1:8000/
.venv/bin/python scripts/test_documentation_tools.py
.venv/bin/python scripts/validate_structure.py
.venv/bin/python -m mkdocs build --strict --config-file mkdocs.yml
.venv/bin/python scripts/validate_site.py site --site-url "$MKDOCS_SITE_URL"
git diff --check
```

All commands must complete successfully. The structure validator checks the
required hierarchy, matching directory ancestry, chapter indexes, supporting
reference locations, content, article reachability, and mappings. The strict
MkDocs build checks configuration and document references. The generated-site
validator checks internal links, assets, and anchors. External URLs and AGL
target behavior require separate verification; record the relevant checks for
the procedure you changed.

## Submit a pull request

Review `git status --short` and `git diff`, then stage only the files belonging
to your change. Replace the example path with the edited source paths:

```sh
git status --short
git diff
git add docs/path/to/edited-guide.md
git commit --signoff
git push --set-upstream origin docs/improve-guide
```

Do not commit `.venv/` or generated `site/` output. If you cloned a fork,
`origin` should be your fork; open the pull request against the publishing
repository's default branch.

On GitHub, choose **Compare & pull request**, select the intended base branch,
and describe the problem, the corrected behavior, and the checks run. See
[GitHub's pull request guide](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).
The Pages workflow runs the structure, build, and internal-link checks for pull
requests. Default-branch changes are deployed by the configured Pages workflow.

GitHub Actions discovers workflows only at the repository-root
`.github/workflows/` directory. If this site is kept under `GitHubPages/`,
the publishing repository needs the workflow at its root as well. Follow the
repository's `README.md` for deployment setup and Pages configuration.

## Contribute to the original AGL documentation

The [original AGL documentation repository](https://gerrit.automotivelinux.org/gerrit/admin/repos/AGL/documentation)
publishes [docs.automotivelinux.org](https://docs.automotivelinux.org).
Changes intended for that project go through AGL Gerrit, not this site's GitHub
pull request workflow.

Follow [Work with Gerrit](gerrit.md) to clone the original repository and install
its `commit-msg` hook. Use that checkout's own `README.md`, `requirements.txt`,
directory layout, and release branch for its build and preview. Do not apply
this site's Material theme or path conventions to the original repository.

Follow the [AGL contribution guidelines](general-guidelines.md) and
[submission guidelines](submit-changes.md). Validate the change in the original
checkout, make a signed-off commit with a `Change-Id`, and upload it with
`git review <target-branch>`. Keep the same `Change-Id` and amend the commit
when submitting a replacement patch set.
