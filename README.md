# AGL documentation for GitHub Pages

This English documentation site follows the exact headings, order, and hierarchy in [AGENTS.md](AGENTS.md). Home is the navigation root. Its seven child sections are AGL Coverage, AGL distributed system distribution, AGL integrated system development, AGL Components, Troubleshooting, Releases & migration, and Contribute. Quick start is inside AGL distributed system distribution, alongside Build Platform, Platform Customize, and Application development. Build chapters for integrated systems are also named Build Platform. Home explains AGL, the Unified Code Base, and its community, and directs readers to AGL Coverage for architecture and system details. AGL Coverage groups traditional distributed, domain, and central/zone designs under Vehicle EE architectures, with three original SVG figures. It introduces AGL as a base distribution for distributed ECUs and an integrated platform for domain or central/zone architectures, with links to their subsections.

The navigation contains 89 required headings. All 152 articles are reachable through those chapters, including 63 supporting articles linked from the relevant chapter rather than added to the required navigation. The original `../docs/` directory remains unchanged; all 84 source Markdown articles and 104 source assets are retained in the reconstructed site.

Quick start introduces the Flutter IVI demo as a complete system and provides prebuilt-image guides for QEMU x86-64 and Raspberry Pi 4/5. Individual application explanations are under AGL Components > AGL Reference Applications. Standalone builds and application development are separate from SoDeV, container, and KVM integration. New material cites official project documentation and source repositories, and identifies gaps where a complete procedure or API specification is unavailable.

## Contents

| Path | Purpose |
| --- | --- |
| `mkdocs.yml` | Navigation, theme, release variables, and build configuration |
| `docs/` | Documentation articles, task-oriented entry pages, and copied assets |
| `docs/assets/diagrams/` | Original SVG diagrams of distributed, domain, and central/zone architectures |
| `AGENTS.md` | Required documentation headings, hierarchy, language, and section content |
| `structure-map.json` | Required heading-to-page mapping and previous page locations |
| `source-map.json` | Source-to-destination mapping and SHA-256 hashes for the 84 imported articles |
| `scripts/import_docs.py` | Re-import the original articles and assets |
| `scripts/import_transforms.py` | Preserve required titles, adapted introductions, and Flutter quickstarts on re-import |
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
.\.venv\Scripts\python.exe scripts\validate_structure.py
.\.venv\Scripts\python.exe -m mkdocs build --strict --config-file mkdocs.yml
.\.venv\Scripts\python.exe scripts\validate_site.py site --site-url "$env:MKDOCS_SITE_URL"
```

Linux or macOS:

```bash
export MKDOCS_SITE_URL=http://127.0.0.1:8000/
.venv/bin/python scripts/validate_structure.py
.venv/bin/python -m mkdocs build --strict --config-file mkdocs.yml
.venv/bin/python scripts/validate_site.py site --site-url "$MKDOCS_SITE_URL"
```

The structure validator checks the navigation against AGENTS.md, first-level page titles, required section contents, architecture figures, subsection links, required references between sections, supporting-page declarations, article reachability, and source mappings. The build checks MkDocs configuration and document references. The validator checks generated local page links, images and other assets, and fragment anchors. External URLs are not checked. The workflow repeats these checks before deployment.

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

Edit articles in `docs/` while preserving the required navigation in AGENTS.md. Do not omit, rename, duplicate, or reorder its headings. Each required page uses its required heading as its first H1. Preserve the Home and AGL Coverage content specified in the Required Contents at Section rules, including the architecture figures and subsection links. Add supporting articles through relative Markdown links from the appropriate chapter and declare their paths in `not_in_nav` in `mkdocs.yml`; they remain available in search. Update `structure-map.json` when changing required page locations, and keep the importer mapping consistent. Update shared release values in `mkdocs.yml` when changing the documented AGL release or artifact channel. Rebuild and run both validators after changes.

The importer is a manual migration utility, not part of the normal site build. From this directory inside the original repository:

```bash
python scripts/import_docs.py --source ../docs
```

**Re-importing overwrites imported articles, copied assets, the prebuilt-image landing page, its two generated quickstart guides, and `source-map.json`.** Preserve local edits before running it. Update the importer's mapping and transformations when a change must survive later imports. Authored chapters and the Flutter IVI demo overview are maintained directly in `docs/` and preserved by the importer. The importer removes retired page locations listed in `structure-map.json` so obsolete headings do not reappear.

In a separate site repository, `../docs/` will not normally exist. Supply the original AGL documentation directory using `--source` only when deliberately re-importing it.

The source map records original source paths and content hashes. It documents where the source articles moved; it does not preserve the old website's URLs automatically. Existing external links require redirects at their original hosting location if the new site replaces that website.

## Build tooling

The site uses MkDocs 1.6.1, Material for MkDocs 9.7.7, mkdocs-macros-plugin 1.5.0, and PyMdown Extensions 12.1. GitHub.com deployment uses pinned official actions and the hosted `ubuntu-latest` runner.

See [GitHub's workflow location requirements](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [custom GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), and [publishing-source configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
