---
title: "Work with Gerrit"
source_path: "07_How_To_Contribute/03_Working_with_Gerrit.md"
content_status: adapted
---

Follow these instructions to collaborate on AGL projects through the Gerrit review
system. For changes to this GitHub Pages site, first follow
[Contribute to the documentation](documentation.md) to select its repository and submission route.

Subscribe to the [AGL development mailing list](https://lists.automotivelinux.org/g/agl-dev-community).
You can also reach the community on IRC at the #automotive channel on irc.libera.chat.

Gerrit assigns the following roles to users:

- **Submitters**: Upload changes for consideration, review other changes, and vote +1 or -1.
- **Maintainers**: Approve or reject changes after review, with +2 or -2 votes.

The project configuration determines the labels and permissions needed to submit a change.

## Getting deeper into Gerrit

Read the official [Gerrit user guide](https://gerrit-review.googlesource.com/Documentation/intro-user.html)
and [Gerrit walkthrough for GitHub users](https://gerrit-review.googlesource.com/Documentation/intro-gerrit-walkthrough-github.html).

## Working with a local clone of the repository

1. Open the [AGL Gerrit repository list](https://gerrit.automotivelinux.org/gerrit/admin/repos/).
2. Select the repository you wish to work on.
3. Copy the SSH clone URL from Gerrit. The following Bash example clones the original
   AGL documentation repository and installs its commit message hook. Set `LFID` to
   your Linux Foundation account's Gerrit SSH username before running it:

    ```sh
    LFID=your-gerrit-username
    git clone "ssh://$LFID@gerrit.automotivelinux.org:29418/AGL/documentation"
    cd documentation
    curl --fail --location --output .git/hooks/commit-msg \
        https://gerrit.automotivelinux.org/gerrit/tools/hooks/commit-msg
    chmod u+x .git/hooks/commit-msg
    ```

    The [commit-msg hook](https://gerrit-review.googlesource.com/Documentation/cmd-hook-commit-msg.html)
    inserts a `Change-Id` in new commit messages and preserves it when an existing commit is amended.

4. Configure the identity for this repository:

    ```sh
    git config user.name "Your Full Name"
    git config user.email "your@email.com"
    ```

    Add `--global` if these values should apply to all your Git repositories.

5. Fetch the target branch and create a descriptively named branch. Select the
   appropriate target branch for the project; `master` is an example, not an AGL release codename:

    ```sh
    TARGET_BRANCH=master
    git fetch origin
    git checkout -b issue-name "origin/$TARGET_BRANCH"
    ```

## Using git review

[git-review](https://docs.opendev.org/opendev/git-review/latest/) automates the
Gerrit upload and download workflow. Follow its installation instructions and then run:

```sh
# First-time setup, from the cloned repository
git review -s
```

The repository's `.gitreview` file identifies the Gerrit host, project, and
default branch. If it is absent, confirm these values with the project maintainer
and configure a Gerrit remote; for the original AGL documentation repository:

```sh
git remote add gerrit "ssh://$LFID@gerrit.automotivelinux.org:29418/AGL/documentation"
git review -s
```

If the `gerrit` remote already exists, inspect `git remote -v` and use
`git remote set-url gerrit <SSH-clone-URL>` to correct its URL.

Upload a committed change to the chosen target branch:

```sh
git review "$TARGET_BRANCH"
```

When updating a patch, stage the changes, use `git commit --amend --signoff`,
keep the existing `Change-Id`, and repeat the same `git review` command.

## Typical Review Workflow

### New change

Run these commands from the repository root. Set `TARGET_BRANCH` to the branch
that will receive the change:

```sh
TARGET_BRANCH=master
git fetch origin
git checkout -b mytopicbranch "origin/$TARGET_BRANCH"
# Edit the files and run the project's required checks.
git add path/to/changed-file
git commit --signoff
git review "$TARGET_BRANCH"
```

### Updating an existing Gerrit review

Replace `25678` with the change number and select that change's target branch:

```sh
TARGET_BRANCH=master
git review -d 25678
# Apply the review feedback and rerun the required checks.
git add path/to/changed-file
git commit --amend --signoff
git review "$TARGET_BRANCH"
git checkout -
```

Amending the existing commit preserves its `Change-Id` and lets Gerrit create
a new patch set for the same project and target branch. See
[Gerrit's patch set workflow](https://gerrit-review.googlesource.com/Documentation/intro-user.html#upload-a-new-patch-set).

## Reviewing Using Gerrit

- **Add reviewer**: A change owner can select registered users to request a review.
  Gerrit sends those users a review notification.
- **Abandon**: A change can be abandoned when it should no longer be considered.
  Availability depends on change ownership and project permissions.
- **Change-Id**: Gerrit uses this commit-message footer, together with the project
  and target branch, to associate updated commits with an existing change.
- **Status and votes**: Reviewers and maintainers use the project's review labels
  to record feedback and approval. Required verification and submit rules are
  visible on the change page.

Check the email preferences in your Gerrit account and your
[Gerrit dashboard](https://gerrit.automotivelinux.org/gerrit/dashboard/self) to
follow changes. The change's history shows patch sets, comments, and votes.
