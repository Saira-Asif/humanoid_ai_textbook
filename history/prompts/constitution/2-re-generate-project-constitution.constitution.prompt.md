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

Project: Research paper on AI-native software development.

Core principles:
- Accuracy through primary source verification.
- Clarity for an academic audience with a computer science background.
- Reproducibility: every factual claim must be traceable to a verifiable source.
- Rigour: emphasis on peer-reviewed, high-quality sources.

Quality standards:
- All factual claims must be cited.
- Citation format: APA 7th edition.
- Minimum 50% peer-reviewed sources across all work.
- Writing clarity: Flesch-Kincaid reading grade 10–12.
- Active voice: at least 70% of the time.
- Zero tolerance for plagiarism; mandatory plagiarism scan before submission.
- All citations must link directly to the exact part of the source used.
- Definitions must originate from primary or authoritative literature.

Constraints:
- Word count range: 5,000–7,000 words.
- Minimum 15 sources for each full paper.
- Final output format: PDF with embedded citations.
- Full traceability: each section must reference its source list.

Success criteria:
- All claims pass source verification.
- All citations are APA compliant.
- Plagiarism report shows 0% unoriginal content before final submission.
- Document passes internal fact-check review.

Generate the full Constitution file and store it in .specify/memory/constitution.md.
Show me the file once created.

## Response snapshot

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
