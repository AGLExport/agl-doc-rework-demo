---
title: "AI coding assistants"
source_path: "07_How_To_Contribute/08_AI-coding-assistants.md"
content_status: imported
---

Coding Assistants
=================
This document provides guidance for AI tools and developers using AI
assistance when contributing to Automotive Grade Linux.

AI tools helping with AGL development should follow the standard
AGL Development process:
https://git.automotivelinux.org/AGL/meta-agl/docs/contributing.md

Licensing
---------
AGL uses different licenses for code and recipes.

*   Apache-v2 (Source Code developed by AGL as a project):
    Ensure AI-generated code does _not_
    inadvertently copy verbatim blocks of code from GPL-only or
    proprietary sources that would violate Apache-v2 compatibility.

*   MIT (Yocto Recipes/Layers): When using AI to generate Yocto
    recipes (.bb, .bbappend), ensure that the AI does not misapply
    license headers or introduce restrictive license requirements
    into MIT-governed layers.

Signed-off-by and Developer Certificate of Origin
-------------------------------------------------
AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the
Developer Certificate of Origin (DCO). The human submitter is responsible for:
*   Reviewing all AI-generated code
*   Ensuring compliance with licensing requirements
*   Adding their own Signed-off-by tag to certify the DCO
*   Taking full responsibility for the contribution

Attribution
-----------
When AI tools contribute to AGL development, proper attribution helps track
the evolving role of AI in the development process. Contributions should
include an Assisted-by tag in the following format:
Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]

Where:
AGENT_NAME is the name of the AI tool or framework
MODEL_VERSION is the specific model version used
[TOOL1] [TOOL2] are optional specialized analysis tools used (e.g., coccinelle, sparse, smatch, clang-tidy)

Basic development tools (git, gcc, make, editors) should not be listed.

Example:
----------
Fix bug in ABC-feature

This fixes a bug found by SomeGPT in the XYZ-function of ABC-feature.
The variable was not properly validated.
Testsuite passed and image booted.

Bug-AGL: <insert jira ID>
Change-Id: <added by git review>

Signed-off-by: <responsible developer, --> DCO >
Assisted-by: SomeGPT (GPTver-1234) [GitHub Copilot] [Coccinelle]
----------

Responsibility
--------------
The human contributor is solely responsible for all code committed to
AGL repositories. AI-generated code is treated as human-written code
and needs to be correct, readable, maintainable.

"The AI suggested it" is not an acceptable justification for:
*   Introduction of functional bugs.
*   Introduction of security vulnerabilities.
*   Violation of AGL coding standards.
*   Violation of license compatibility.

The human must fully understand and validate the logic, side effects,
and security implications of any AI-suggested code before submission.

Review and Validation
---------------------
All AI-assisted code must undergo the standard AGL peer-review
process. Reviewers should be extra vigilant for "hallucinated"
logic or non-existent API calls that AI assistants often suggest.

