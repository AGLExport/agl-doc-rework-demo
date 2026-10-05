---
title: "Code contribution guidelines"
source_path: "07_How_To_Contribute/08_Code_contribution_guidelines.md"
content_status: imported
---

Your patches to AGL are very welcome. Please review the guidelines below:

Change Requirements

This section contains guidelines for submitting code changes for review.
For more information on how to submit a change using Gerrit,
please see Working with Gerrit.

Changes are submitted as Git commits. Each commit must contain:

    a short and descriptive subject line that is 72 characters or
      fewer, followed by a blank line.
    a change description with your logic or reasoning for the changes,
      followed by a blank line
    a Signed-off-by line, followed by a colon (Signed-off-by:)
    a Change-Id identifier line, followed by a colon (Change-Id:).
      Gerrit won't accept patches without this identifier.

A commit with the above details is considered well-formed.
This page is a very useful for the same.

All changes and topics sent to Gerrit must be well-formed.
Informationally, commit messages must include:

    what the change does,
    why you chose that approach, and
    how you know it works -- for example, which tests you ran.

For example: One commit fixes whitespace issues, another renames a function and
a third one changes the code's functionality. An example commit file is
illustrated below in detail:

A short description of your change with no period at the end

You can add more details here in several paragraphs, but please keep each line
width less than 80 characters. A bug fix should include the issue number.

Bug-AGL: [SPEC-<JIRA-ID>]
Change-Id: IF7b6ac513b2eca5f2bab9728ebd8b7e504d3cebe1
Signed-off-by: Your Name <commit-sender@email.address>

Include the issue ID in the one line description of your commit message for
readability. Gerrit will link issue IDs automatically to the corresponding
entry in Jira.

Each commit must also contain the following line at the bottom of the
commit message:

Signed-off-by: Your Name <your@email.address>

The name in the Signed-off-by line and your email must match the change
authorship information. Make sure your :file:.git/config is set up correctly.
Always submit the full set of changes via Gerrit.

When a change is included in the set to enable other changes, but it will
not be part of the final set, please let the reviewers know this.



Open Source Code Contribution Checklist
General

    Does the component have a name ? (Pick one fitting the purpose and
    the project.)
    Is a separate git repo required for the component ?
    Does the component have a README.md containing all basic information
    about it ?
        Description.
        Dependencies.
        Build instructions.
        Installation instructions.
        Usage instructions.
        Example invocations.
    Does the component have a CONTRIBUTIONS.md file? (Containing all necessary
    information on how to contribute, e.g. pointing to project website? )

License

    Is the license an OSI approved open source software license?
    Are all files under an OSI approved open source license?
    Does the component have a LICENSE (or COPYING) file detailing the
    license of the code?
    Do the source code files have the license mentioned in the header?
    Do the source code files have an SPDX tag? (Note: An SPDX tag can
    be used in a file header instead of the license note)
    Are there files with other licenses in their header?
        If so, LICENSE should be the for the majority of the files and
        LICENSE.xyz for the exceptions.

docs/

    Are there docs/ folder for the component ?
        e.g. Are all APIs described inclusive description, usage and
             example invocations ?
        e.g. Are all cmdline tools or options described in the documentation ?
        e.g. Is the program flow described ?
    Contain Changelog.md ? (Keep track of major changes in the changelog.)

tests/

    Must have tests available.
    Must have simple invocation scripts available.
    Must have instructions for CI available.
    Must contribute CI test definitions.

Git repository

    Must have: a .gitreview file.
        Option: Can have a .gitignore file.
        Option: Can have a .editorconfig file.
    All code needs to build against master.
    Is a backport to a release branch required ?
    Code contributions submitted need to have a Sign-off-by! (Follow DCO.)

Yocto/OE

    Recipes need to follow the guidelines of : new-recipe-writing-a-new-recipe.
    Recipes follow the bitbake style guide.
    Your 'meta-*' layer needs to pass the yocto-check-layer tool.

Gerrit Reviews

All gerrit reviews need to be addressed. All issues are to be discussed with the experts.

    Issues are to be discussed in the EG first.
    Consent needs to be reached.
    Gerrit commits need two upvotes (not from authors!) to be merged.
    Uploads should be 'ready for review' or marked 'WIP'.
