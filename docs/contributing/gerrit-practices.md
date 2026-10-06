---
title: "Gerrit recommended practices"
source_path: "07_How_To_Contribute/06_Gerrit_Recommended_Practices.md"
content_status: adapted
---

Use these practices to prepare changes, download patch sets, and update reviews.
The Bash examples use a remote named `origin` and a target branch named `master`;
replace these with the remote and branch used by your project. Run the commands
from the cloned repository. See [Work with Gerrit](gerrit.md) for account and hook setup.

## Commit Messages

Use a short subject, followed by a blank line and a description of the problem,
the change, and its validation. Keep the trailers together in the final paragraph:

```text
Explain the change in a short subject

Describe why the change is needed, how it works, and what was tested.
Include any related documentation changes. Wrap the text at 72 columns.

Bug-AGL: SPEC-1234
Change-Id: I0123456789abcdef0123456789abcdef01234567
Signed-off-by: Your Name <your.email@example.org>
```

Use the actual issue number and let the Gerrit `commit-msg` hook generate the
`Change-Id`. Preserve that identifier when amending or rebasing an existing
review; it identifies the same change across patch sets. See the official
[commit-msg hook documentation](https://gerrit-review.googlesource.com/Documentation/cmd-hook-commit-msg.html)
and the [AGL submission guidelines](submit-changes.md).

## Avoid Pushing Untested Work to a Gerrit Server

Run the project's required checks before uploading a change. Inspect the diff
and commit message, and explain the validation and any remaining limitations.

## Keeping Track of Changes

- Configure notifications in your Gerrit account's email preferences.
- Watch the projects you work on for new changes, patch sets, comments, and submissions.
- Use the review page and your dashboard to follow feedback on individual changes.

Also follow the [AGL development mailing list](https://lists.automotivelinux.org/g/agl-dev-community).

## Topic branches

Create local feature branches for logically related work. A Gerrit topic is a
label that groups changes; pushing a topic does not create a corresponding Git
branch on the server. Upload a set of dependent commits with a topic as follows:

```sh
git push origin HEAD:refs/for/master%topic=TopicName
```

Replace `master` with the target branch and `TopicName` with your topic.
The topic is shown in Gerrit's change list and review interface. See
[Gerrit's topic upload options](https://gerrit-review.googlesource.com/Documentation/user-upload.html#topic).

## Finding Available Topics

Set `LFID` to your Gerrit SSH username, then query open changes:

```sh
LFID=your-gerrit-username
ssh -p 29418 "$LFID@gerrit.automotivelinux.org" \
    gerrit query status:open branch:master | grep 'topic:' | sort -u
```

The query filters by change status and target branch; `sort -u` removes duplicate
topic lines. Add `project:PROJECT_NAME` or `topic:TOPIC_NAME` to narrow the query.
For query syntax, see the [Gerrit query command](https://gerrit-review.googlesource.com/Documentation/cmd-query.html).

## Downloading or Checking Out a Change

Copy the fetch or checkout command from the change's **Download** menu to select
the correct repository, change number, and patch set.

With `git-review`, download change 2464, patch set 4:

```sh
git review -d 2464,4
```

Without `git-review`, fetch the patch set and create a local branch:

```sh
git fetch origin refs/changes/64/2464/4
git checkout -b review-2464-4 FETCH_HEAD
```

The reference format is `refs/changes/NN/CHANGE_NUMBER/PATCH_SET`, where
`NN` is the last two digits of the change number, padded to two digits.
For change 2464, those digits are `64`. See Gerrit's
[refs/for and refs/changes documentation](https://gerrit-review.googlesource.com/Documentation/concept-refs-for-namespace.html).
Download commands and patch-set selection are also described in the
[git-review usage guide](https://docs.opendev.org/opendev/git-review/latest/usage.html).

## Using Sandbox Branches

Some AGL repositories allow personal branches under
`refs/heads/sandbox/USERNAME/BRANCHNAME`. Check the repository's permissions
before using this workflow.

Create a local sandbox branch and push it directly:

```sh
git checkout -b sandbox/USERNAME/BRANCHNAME
git push --set-upstream origin HEAD:refs/heads/sandbox/USERNAME/BRANCHNAME
```

Replace `USERNAME` and `BRANCHNAME` with your username and branch name.
This bypasses code review and requires push permission. Later fast-forward
updates can use:

```sh
git push origin HEAD:refs/heads/sandbox/USERNAME/BRANCHNAME
```

To request review against an existing sandbox branch instead, use:

```sh
git push origin HEAD:refs/for/sandbox/USERNAME/BRANCHNAME
```

These commands do not force an update. The distinction between direct pushes
and review uploads is explained in
[Gerrit's refs/for documentation](https://gerrit-review.googlesource.com/Documentation/concept-refs-for-namespace.html).

## Updating the Version of a Change

Each version of a reviewed change is a patch set. For a change at the tip of
your branch, stage the corrected files and amend its commit:

```sh
git add path/to/changed-file
git commit --amend --signoff
git push origin HEAD:refs/for/master%topic=TopicName
```

Keep the existing `Change-Id`. Gerrit matches that identifier, the repository,
and the target branch to update the same change. For changes earlier in a
dependent series, edit their commits with interactive rebase, preserve each
commit's `Change-Id`, rerun validation, and upload the series again.

The upload retains your local Git history. Gerrit keeps earlier patch sets
available in the review interface. New commits with new identifiers create
additional changes. See the official
[patch-set update workflow](https://gerrit-review.googlesource.com/Documentation/intro-user.html#upload-a-new-patch-set).

### Rebasing

Rebase only when needed, such as resolving a conflict with the target branch.
Do not rebase commits already merged into a shared branch.

Interactive rebase can edit a series:

```sh
git fetch origin
git rebase -i origin/master
```

- `squash` combines commits; retain the identifier of the review you intend to keep.
- `reword` changes a commit message.
- `edit` stops so that you can amend a commit.
- Reordering the lines changes the commit order.

Resolve any conflicts, stage the resolved files, and run `git rebase --continue`.
Preserve the `Change-Id` of each change that remains in the series.

## Rebasing During a Pull

Suppose the target branch ends at commit `a4` and your branch contains changes
`c0` through `c7` on top of it. The following command lists only your local
changes, in chronological order:

```sh
git log --reverse --oneline origin/master..HEAD
```

If the target branch advances to `a7`, update your branch with:

```sh
git pull --rebase origin master
```

This fetches the target branch and reapplies `c0` through `c7` on top of
`a7`. Their commit hashes may change, but their `Change-Id` trailers must
remain. The same log range still lists only `c0` through `c7`, since
`origin/master` now includes `a0` through `a7`.

Rerun the project's checks before uploading the resulting patch sets. See the
[Gerrit rebase workflow](https://gerrit-review.googlesource.com/Documentation/intro-user.html#rebase-a-change)
and [Git rebase documentation](https://git-scm.com/docs/git-rebase).

## Getting Better Logs from Git

Configure abbreviated hashes and a one-line default format for this repository:

```sh
git config log.abbrevCommit true
git config core.abbrev 7
git config format.pretty oneline
```

`core.abbrev` sets the preferred abbreviation length; Git may use more
characters to distinguish objects. `format.pretty` selects the default log
format. For a single command without changing configuration, use
`git log --oneline`. See the [Git configuration reference](https://git-scm.com/docs/git-config).
