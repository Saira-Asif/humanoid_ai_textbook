---
id: 2
title: Re-Generate Project Constitution
stage: constitution
date: 2025-12-04
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: ["project-setup", "constitution"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

/sp.constitution

Physical AI & Humanoid Robotics — Project Constitution (v1.0.0)

Purpose
This constitution establishes the core principles, mandatory quality gates, and governance rules for producing the **Physical AI & Humanoid Robotics** textbook and its supporting systems (RAG assistant, Docusaurus site, example code). It balances academic rigour with production-grade engineering and publishing standards.

 I. Core Principles
1. Content Accuracy & Technical Rigor
- All technical claims, formulas, and research references must be accurate and verifiable.
- Claims require: (a) citation to an authoritative source, (b) derivation/proof, or (c) experimental validation.
- Code examples must be runnable, tested, and explicitly versioned where applicable.
- Version specifications are required for software dependencies.

 2. Scholarly Integrity & Reproducibility
- Citations must use APA 7th (or project-approved variant) with links to sources where available.
- Target proportion of peer-reviewed sources should be defined per chapter (advisory baseline: 50% where feasible).
- Mandatory plagiarism scanning prior to merge; incidence of unoriginal content must be documented and cleared.

 3. Educational Clarity & Accessibility
- Each chapter declares learning objectives, prerequisites, and a short summary.
- Complex concepts introduced with: motivation, simple example, formal definition, and application.
- Diagrams and worked examples required for spatial or multi-step topics.
- Glossary terms linked on first use.

 4. Consistency & Standards (NON-NEGOTIABLE)
- Single source of truth: `docs/glossary.md` and `docs/notation.md`.
- Chapter template: Learning Objectives → Prerequisites → Content → Summary → Exercises → References.
- Code style: language-specific style guides (e.g., PEP 8 for Python). Code blocks must include language tag and dependency list.

 5. Docusaurus Structure & Publishing Quality
- One concept per page (recommended max ~2000 words).
- Frontmatter required: `title`, `description`, `keywords`, `sidebar_position`.
- Assets stored under `/static/img/<chapter>/` with descriptive names and alt text.
- Internal links must be relative.

 6. Deployment & Performance Standards
- `main` branch is production only; feature branches via PR.
- Pre-merge build gates (see Quality Gates).
- Basic SEO & accessibility settings (Open Graph, sitemap, robots.txt) should be configured.

 II. Quality Gates & Review Process (Pre-Merge Requirements)

Every PR must include:
1. Docusaurus build passes with no errors.
2. Broken links check passes.
3. Spell and terminology checks (technical dictionary).
4. Technical review by a domain expert for factual/code accuracy.
5. Peer review for pedagogy and clarity.
6. Accessibility check: alt text, headings, contrast ratios.
7. Performance baseline: Lighthouse checks (advisory thresholds documented).

Additional checks for code examples:
- Each example includes dependency versions, README with usage, and a basic validation script.

---
 III. Content Development Workflow (Spec-Driven)

1. `/sp.specify` — Chapter spec (scope, objectives, key concepts).
2. `/sp.plan` — Content plan (diagrams, examples, milestones).
3. `/sp.tasks` — Task breakdown (writing tasks, code examples, reviews).
4. Implementation → Technical Review → Peer Review → Merge → Publish.
5. ADRs recommended for cross-cutting architectural choices.

Artifacts persist under `specs/[chapter]/` and `history/` for auditability.

 IV. Governance & Amendment

- This constitution is authoritative; all PRs must reference the relevant checklist items.
- Amendments follow: issue → impact analysis → discussion → vote/approval → migration plan → version bump.
- Quarterly audits will validate compliance.


 V. Roles & Responsibilities

- **Author(s)**: Draft chapters and code examples.
- **Technical Reviewer**: Validates formulas, code, and claims.
- **Peer Reviewer**: Reviews pedagogy and clarity.
- **Editor**: Enforces style, metadata and accessibility.
- **Maintainer**: Final merge approval.

 VI. Runtime Guidance for AI Agents (CLAUDE.md / Automation)

- AI agents must follow the spec files (spec.md, plan.md, tasks.md) and the checks defined here.
- Avoid expanding the scope beyond defined chapter/spec boundaries.
- Agents may propose ADRs or content changes but require human sign-off for anything outside the spec.


Generate the full Constitution file and store it in .specify/memory/constitution.md.
Show me the file once created.


### Response snapshot

The Project Constitution file was successfully generated and stored in `.specify/memory/constitution.md`. The file outlines core principles, quality standards, constraints, and success criteria for the research paper on AI-native software development.

## Outcome

- ✅ Impact: Project constitution file re-created successfully.
- 🧪 Tests: No tests were applicable for this task.
- 📁 Files: 1 file created: .specify/memory/constitution.md
- 🔁 Next prompts: Awaiting further instructions from the user.
- 🧠 Reflection: Successfully re-created the project constitution file based on user requirements and stored it in the specified location.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
