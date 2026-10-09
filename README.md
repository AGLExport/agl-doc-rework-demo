# AGL documentation for GitHub Pages

This English site follows the exact headings, order and hierarchy in [AGENTS.md](AGENTS.md). Home contains Introduction, the three Base platform chapters, AGL Development tools, Troubleshooting, Releases & migration and Contribute. Introduction connects vehicle E/E architectures and end-to-end vehicle data processing to those platform choices.

The navigation contains 102 required headings. All 161 articles are reachable, including 59 supporting articles linked from the chapters. The original `../docs/` directory remains unchanged. `source-map.json` records 84 original articles: 73 active mappings and 11 excluded articles, plus 101 imported assets and three excluded screenshots. `structure-map.json` records current navigation and prior moves/removals; removed pages remain removed.

All AGL implementation guidance uses **master**. The 73 active original article sources were checked against official documentation master on 10 October 2026. Current recipe inspection governs image availability and composition where the upstream prose still lists older targets. [The source-review record](docs/assets/source-reviews/master-2026-10-10.json) contains checked URLs, content hashes and the reviewed manifest/layer commits. Component implementation links can use the SRCREV selected by a master recipe. External SoDeV platform workspaces retain their own integration pins, and the SoDeV guide makes the required master guest adaptation explicit.

The distributed base platform contains the Basic/Extra portfolios, architecture, build sequence, shared components, platform customization and application development. Momi remains an Extra portfolio example; its complete build/deployment procedure is maintained under Container integration > Demo image for container integration. Momi application references and host extensions are under that integration's AGL Components chapter. SoDeV has its own AGL Components > Platform extension chapter for Unified HMI.

The Introduction figures and editable Flutter/Qt IVI and Container integration SVGs accompany the platform explanations. The IVI figures and container source references use reviewed master recipes. The official SoDeV figure is reproduced unchanged with its announcement attribution. The shared page banner displays the master baseline and source-review date. Source inspection and documentation checks do not report hardware or emulator runtime validation.

## Contents

| Path | Purpose |
| --- | --- |
| `mkdocs.yml` | Navigation, theme, master variables, and build configuration |
| `docs/` | Documentation articles, task-oriented entry pages, and copied assets |
| `docs/assets/diagrams/` | Vehicle and runtime architecture SVGs and the official SoDeV image |
| `asset-sources.json` | Attribution and SHA-256 for the official SoDeV image and authored IVI/container diagrams |
| `AGENTS.md` | Required documentation headings, hierarchy, language, and section content |
| `structure-map.json` | Required heading-to-page mapping, previous page locations, and explicitly removed files |
| `source-map.json` | Active source-to-destination mappings, excluded files, and SHA-256 hashes for the 84 source articles |
| `scripts/import_docs.py` | Re-import the original articles and assets |
| `scripts/import_transforms.py` | Preserve required titles, adapted introductions, and Flutter quickstarts on re-import |
| `scripts/test_documentation_tools.py` | Regression checks for section resolution and import preservation |
| `scripts/validate_structure.py` | Check the exact required hierarchy, article reachability, and source mappings |
| `scripts/validate_site.py` | Check generated local links, assets, and anchors |
| `requirements.txt` | Pinned Python build dependencies |
| `.github/workflows/pages.yml` | GitHub Actions build, validation, and deployment workflow |
| `site/` | Generated static HTML site, excluded from Git |

The generated `site/` directory is included in the initial workspace delivery for inspection. It is reproducible from the source files and does not need to be committed. Serve the site locally to preview it in a browser; MkDocs search and directory URLs work best over HTTP.

## Local preview

Use Python 3.12. Run these commands from this directory.

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:MKDOCS_SITE_URL = 'http://127.0.0.1:8000/'
.\.venv\Scripts\python.exe -m mkdocs serve --config-file mkdocs.yml
```

Linux or macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
export MKDOCS_SITE_URL=http://127.0.0.1:8000/
.venv/bin/python -m mkdocs serve --config-file mkdocs.yml
```

Open <http://127.0.0.1:8000/> in a browser. Stop the preview server with Ctrl+C.

## Build and validate

From this directory, use the same site URL for the build and link validator.

PowerShell:

```powershell
$env:MKDOCS_SITE_URL = 'http://127.0.0.1:8000/'
.\.venv\Scripts\python.exe scripts\test_documentation_tools.py
.\.venv\Scripts\python.exe scripts\validate_structure.py
.\.venv\Scripts\python.exe -m mkdocs build --strict --config-file mkdocs.yml
.\.venv\Scripts\python.exe scripts\validate_site.py site --site-url "$env:MKDOCS_SITE_URL"
```

Linux or macOS:

```bash
export MKDOCS_SITE_URL=http://127.0.0.1:8000/
.venv/bin/python scripts/test_documentation_tools.py
.venv/bin/python scripts/validate_structure.py
.venv/bin/python -m mkdocs build --strict --config-file mkdocs.yml
.venv/bin/python scripts/validate_site.py site --site-url "$MKDOCS_SITE_URL"
```

The structure validator rejects Further reading sections and files recorded as removed, and checks the navigation against AGENTS.md, first-level page titles, required section contents, architecture figures, subsection links, required references between sections, supporting-page declarations, article reachability, and source mappings. The build checks MkDocs configuration and document references. The validator checks generated local page links, images and other assets, and fragment anchors. External URLs are not checked. The workflow repeats these checks before deployment.

## Publish on GitHub Pages

All files prepared for this site are kept under `GitHubPages/` in the original documentation workspace. GitHub Actions only discovers workflows in the repository-root `.github/workflows/` directory. A workflow nested at `GitHubPages/.github/workflows/pages.yml` is not active in the existing repository.

Choose one of these layouts when enabling deployment.

### Option A: Use a separate site repository

1. Copy the contents of `GitHubPages/` into the root of a new GitHub repository. Include hidden files, especially `.github/` and `.gitignore`. Exclude `.venv/` and `site/`.
2. Ensure `mkdocs.yml`, `requirements.txt`, `docs/`, and `scripts/` are at that repository's root, with the workflow at `.github/workflows/pages.yml`.
3. In GitHub, open **Settings > Pages > Build and deployment** and set **Source** to **GitHub Actions**.
4. Push to the default branch or run **Build and deploy AGL documentation** manually from the Actions tab.

### Option B: Keep the site inside the existing repository

1. Keep the site sources under `GitHubPages/`.
2. When enabling deployment, copy `GitHubPages/.github/workflows/pages.yml` to the existing repository's root `.github/workflows/pages.yml`. This root-level copy is required for GitHub Actions to detect the workflow.
3. Set **Settings > Pages > Build and deployment > Source** to **GitHub Actions**.
4. Push to the default branch or run the workflow manually.

The workflow supports both layouts by locating either `GitHubPages/mkdocs.yml` or root-level `mkdocs.yml`. It builds into an ephemeral repository-root `_site/` directory and uploads only the generated site. It does not overwrite the local `GitHubPages/site/` delivery.

Deployment follows the repository's actual default branch, without a fixed `main` or `master` name. Pull requests run build and internal-link validation without publishing. Manual runs publish only when the selected branch is the default branch.

`actions/configure-pages` supplies the published base URL through `MKDOCS_SITE_URL`, supporting repository sites, user/organization sites, and custom domains. Configure a custom domain in GitHub's Pages settings if needed.

This delivery does not create the root-level workflow copy, publish the site, commit changes, or push to GitHub.

## Troubleshoot Pages configuration errors

If the **Read GitHub Pages configuration** step reports `HttpError: Not Found` or `Get Pages site failed`, the Pages site has not been enabled or the workflow cannot access it. This failure occurs before MkDocs builds the documentation.

1. Open the publishing repository's **Settings > Pages**. For `AGLExport/agl-doc-rework-demo`, use <https://github.com/AGLExport/agl-doc-rework-demo/settings/pages>.
2. Under **Build and deployment > Source**, select **GitHub Actions**. A repository administrator or maintainer must perform this initial setup. The existing workflow is sufficient; no additional template is needed.
3. In **Actions**, open the failed run and choose **Re-run all jobs**, or run **Build and deploy AGL documentation** on the default branch.

If GitHub Actions is already selected, check that the repository's plan and organization policy allow Pages and that the build job retains `pages: read`. Keep the deploy job's `pages: write` and `id-token: write` permissions.

The workflow deliberately uses `enablement: false` and the standard `GITHUB_TOKEN`. Adding `enablement: true` alone does not solve initial setup: [the action requires a separate token for automatic enablement](https://github.com/actions/configure-pages/blob/v6.0.0/action.yml). Enabling Pages once through repository settings avoids adding an administrator token to the workflow. See [GitHub's publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

When updating an existing parent repository, copy the revised workflow to its root `.github/workflows/pages.yml` before committing it. Updating only the nested workflow does not update the active workflow.

## Edit and maintain the documentation

Edit articles in docs/ while preserving the required navigation in AGENTS.md. Do not omit, rename, duplicate, or reorder its headings. Each required page uses its required heading as its first H1. Preserve every Required Contents at Section rule, including the Introduction E/E architecture figures and their links to the corresponding system categories, E2E Vehicle Data Processing, the Home coverage reference, and the official SoDeV diagram and source in Large scale integrated system. The historical AGL Coverage reference resolves to Introduction, and the hyphenated Small-scale integrated system content rule resolves to the exact Small scale integrated system navigation heading. Add supporting articles through relative Markdown links from the appropriate chapter and declare their paths in not_in_nav in mkdocs.yml. Update structure-map.json when changing required page locations, and keep the importer mapping consistent. Update shared release values in mkdocs.yml when changing the documented AGL release or artifact channel. Rebuild and run both validators after changes.

The importer is a manual migration utility, not part of the normal site build. From this directory inside the original repository:

```bash
python scripts/import_docs.py --source ../docs
```

Re-importing honors the explicit removed_files list in structure-map.json, excludes those pages/assets from output, and strips Further reading sections. It refreshes unadapted articles (`content_status: imported`), copied assets, and `source-map.json`. Articles marked `content_status: adapted` retain their local corrections and must keep a matching `source_path`; this includes the corrected prebuilt guides and SDK, Qt, board, and contribution procedures. Mark an imported article as adapted when maintaining local changes. Authored chapters and the Flutter IVI demo overview are maintained directly in `docs/`. Use `--overwrite-adapted` only when deliberately replacing curated pages with reviewed upstream material, then reapply any remaining local adaptations and run all checks. The importer removes retired page locations and explicitly excluded files listed in `structure-map.json` so they do not reappear.

In a separate site repository, `../docs/` will not normally exist. Supply the original AGL documentation directory using `--source` only when deliberately re-importing it.

The source map records original source paths and content hashes. It documents where the source articles moved; it does not preserve the old website's URLs automatically. Existing external links require redirects at their original hosting location if the new site replaces that website.

## Build tooling

The site uses MkDocs 1.6.1, Material for MkDocs 9.7.7, mkdocs-macros-plugin 1.5.0, and PyMdown Extensions 12.1. GitHub.com deployment uses pinned official actions and the hosted `ubuntu-latest` runner.

See [GitHub's workflow location requirements](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [custom GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), and [publishing-source configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
