# Physical AI & Humanoid Robotics Textbook — Project Constitution (v1.0.0)

## Purpose
This constitution establishes the core principles, mandatory quality gates, and governance rules for producing the **Physical AI & Humanoid Robotics** textbook. It balances academic rigor with production-grade publishing standards for a Docusaurus-based educational resource covering ROS 2, Digital Twins, NVIDIA Isaac, and Vision-Language-Action models.

---

## I. Core Principles

### 1. Accuracy Through Primary Source Verification
- All technical claims, formulas, and research references must be accurate and verifiable.
- Every factual claim must be cited using APA 7th edition format.
- Minimum 50 authoritative sources across the textbook, with 50%+ from peer-reviewed sources.
- Code examples must be runnable, tested, and embedded directly in chapter markdown.
- Version specifications required for all software dependencies (ROS 2 Humble, Isaac Sim 4.0+, Python 3.10+).

### 2. Clarity for Academic Audience with CS Background
- Target readability: Flesch-Kincaid Grade 12-14 (graduate-level technical content).
- Active voice requirement: At least 70% of sentences.
- Each chapter declares 3-5 learning objectives (Bloom's taxonomy), prerequisites, and estimated time.
- Complex concepts introduced with: motivation, simple example, formal definition, and application.
- All technical terms defined on first use with APA citation and linked to glossary (100+ terms).

### 3. Reproducibility
- Every factual claim must be traceable to a verifiable source.
- Code examples include: purpose comment, expected output, and troubleshooting note.
- All code passes flake8 and black formatting.
- Zero-to-running time for each example: under 15 minutes.
- GPU-heavy examples must include cloud/simulation alternatives.

### 4. Rigor: Peer-Reviewed Sources
- Target: 50%+ of all sources must be peer-reviewed (journals, conferences, technical reports).
- Sources must include direct links where available.
- Citations managed in centralized bibliography (research-bibliography.md) with APA 7th edition format.

### 5. Consistency & Standards (NON-NEGOTIABLE)
- Single source of truth: `docs/references/glossary.md` and notation guide.
- Chapter structure: Learning Objectives → Prerequisites → Content (3000-5000 words) → Summary → References.
- Frontmatter required: `title`, `description`, `estimated_time`, `week`, `module`, `prerequisites`, `learning_objectives`, `sidebar_label`.
- Code style: PEP 8 for Python. All code blocks must include language tag.
- Assets stored under `textbook-site/static/img/` with descriptive names and alt text.

### 6. Docusaurus Structure & Publishing Quality
- Content organized into 4 modules (ROS 2, Digital Twin, Isaac, VLA) with 14 chapters total.
- Navigation: Single sidebar with nested collapsible categories organized by modules.
- Deployment target: GitHub Pages via Docusaurus v3.
- Performance requirements: Build time <5 minutes, initial page load <3 seconds, search response <300ms.
- SEO & accessibility: Open Graph metadata, sitemap, robots.txt, alt text for all images.

---

## II. Quality Gates & Review Process (Pre-Publication Requirements)

### Phase 4 Quality Assurance Checklist (Mandatory)

Every module must pass these gates before publication:

1. **Readability Assessment**
   - Flesch-Kincaid Grade 12-14 achieved for all chapters
   - Active voice ≥70% of sentences
   - All chapters meet 3000-5000 word target

2. **Citation Validation**
   - All factual claims have APA 7th edition citations
   - 50%+ sources are peer-reviewed (verified against research-bibliography.md)
   - All citations link to sources where possible

3. **Plagiarism Scan**
   - Zero plagiarism detected (0% unoriginal content)
   - Mandatory scan before any content publication
   - Flagged sections must be rewritten

4. **Code Quality**
   - All code examples pass flake8 and black formatting
   - All embedded code examples are syntactically correct
   - Zero-to-running time verified for representative examples

5. **Build Validation**
   - `npm run build` succeeds with zero errors
   - No broken links (internal or external)
   - All images load correctly

6. **Cross-Reference Validation**
   - Prerequisite chains work between all 14 chapters
   - Glossary term links validated
   - Inter-chapter references verified

7. **Accessibility Check**
   - Alt text for all images
   - Proper heading hierarchy (H1 → H2 → H3)
   - Contrast ratios meet WCAG 2.1 AA standards

### Quality Report Requirements
- Generate quality report with all metrics after Phase 4
- Document any deviations with justification
- Track metrics: readability scores, citation counts, plagiarism results, build status

---

## III. Content Development Workflow (6-Phase Implementation)

### Phase 1: Research & Requirements (2-4 hours)
- Research and identify 50+ authoritative sources (50%+ peer-reviewed)
- Create research-bibliography.md with APA 7th edition citations
- Extract key concepts for each module
- Create prerequisite-map.md and learning-objectives.md

### Phase 2: Foundation & Structure (1-2 hours)
- Initialize Docusaurus project in textbook-site/
- Configure docusaurus.config.js and sidebars.js
- Create directory structure for 4 modules
- Generate chapter templates with frontmatter schema

### Phase 3: Content Development (20-40 hours)
- Write all 14 chapters (3000-5000 words each, embedded code examples)
- Write 4 appendices (1000-2000 words each)
- Create glossary (100+ terms)
- Ensure all content has inline APA citations

**Checkpoint after each module**: Verify Flesch-Kincaid 12-14, active voice ≥70%, all claims cited, code functional

### Phase 4: Quality Assurance & Validation (4-8 hours)
- Run all quality gates (see Section II)
- Generate comprehensive quality report
- Revise content to meet all standards

**Checkpoint**: All quality gates pass before proceeding to Phase 5

### Phase 5: Integration & Polish (2-4 hours)
- Create homepage dashboard with 4 module cards
- Configure search functionality
- Refine navigation and test mobile responsiveness
- Add visual polish (module images, consistent styling)

### Phase 6: Deployment & Documentation (1-2 hours)
- Configure GitHub Pages deployment
- Create README.md with project overview and contribution guidelines
- Deploy to production and verify functionality
- Test live site (links, search, mobile, performance)

Artifacts persist under `specs/1-humanoid-ai-textbook/` for auditability:
- plan.md (implementation plan)
- research.md (research phase output)
- tasks.md (task breakdown)
- research-bibliography.md (all sources)
- learning-objectives.md (chapter objectives)
- prerequisite-map.md (dependency graph)

---

## IV. Module Structure & Organization

### 4 Modules, 14 Chapters

**Course Introduction (Weeks 1-2)**
- Physical AI Foundations

**Module 1: ROS 2 Fundamentals (Weeks 3-5, 5 chapters)**
- Nodes, Topics, Services
- Python & rclpy
- URDF for Humanoids
- Advanced Topics
- ROS 2 Integration

**Module 2: Digital Twin (Weeks 6-7, 3 chapters)**
- Gazebo Simulation
- Unity Integration
- Sensor Simulation

**Module 3: NVIDIA Isaac (Weeks 8-10, 3 chapters)**
- Isaac Sim
- Isaac ROS & VSLAM
- Nav2 Path Planning

**Module 4: Vision-Language-Action (Weeks 11-13, 3 chapters)**
- Voice-to-Action (Whisper)
- LLM Cognitive Planning
- Capstone Project

**Appendices**
- ROS 1 to ROS 2 Migration
- Advanced ROS 2 Patterns
- Custom Gazebo Plugins
- Math Deep-Dives (Kinematics, SLAM)

**References**
- Glossary (100+ terms)
- Troubleshooting Guide

### Module Dependencies
- Modules must be completed sequentially (Module 1 → 2 → 3 → 4)
- Each module builds on prerequisite knowledge from previous modules
- Appendices can be written in parallel with modules

---

## V. Technical Constraints & Standards

### Technology Stack
- **Platform**: Docusaurus v3, deployed to GitHub Pages
- **ROS Version**: ROS 2 Humble Hawksbill (LTS)
- **Simulators**: Gazebo Fortress, NVIDIA Isaac Sim 4.0+, Unity
- **Programming**: Python 3.10+
- **Operating System**: Ubuntu 22.04 LTS (primary)

### Hardware Tiers
- **Cloud**: AWS g4dn.xlarge/T4 or equivalent
- **Local**: 16GB RAM, RTX 4070 Ti (12GB VRAM) minimum
- **Edge**: NVIDIA Jetson Orin Nano (8GB)

### VLA Model Stack
- Voice: OpenAI Whisper
- Language: GPT-4 API or Claude API
- Vision: CLIP (OpenAI)
- Action: RT-2 or OpenVLA

### Format Requirements
- Chapters: 3000-5000 words each
- Appendices: 1000-2000 words each
- Total: ~50,000-70,000 words
- Docker images: <5GB per module
- Dataset downloads: <1GB per example

---

## VI. Edge Cases & Accessibility

### Students Without GPU
- Every GPU-heavy example includes Google Colab alternative
- Gazebo fallback for Isaac Sim examples
- Cloud deployment options documented

### Limited Internet
- Offline-first documentation approach
- Datasets under 1GB with torrent support
- All essential resources downloadable

### No Physical Hardware
- 100% of concepts have simulation equivalents
- Isaac Sim and Gazebo alternatives for all examples

### Windows-Only Environment
- WSL2 setup guide included
- Docker-based ROS 2 environments documented

---

## VII. Governance & Amendment

- This constitution is authoritative; all content development must reference relevant quality gates
- Amendments follow: issue → impact analysis → discussion → approval → version bump
- Quality audits performed at end of each module (after Phase 4 Quality Assurance)
- Final audit before Phase 6 deployment

---

## VIII. Roles & Responsibilities

### Content Development (AI-Assisted)
- **Primary Author**: Claude/AI agent drafting chapters per spec.md, plan.md, tasks.md
- **Research**: Gather 50+ authoritative sources (50%+ peer-reviewed)
- **Writing**: Draft all 14 chapters with embedded code examples and inline citations
- **Quality Checks**: Run Flesch-Kincaid, plagiarism scans, code validation

### Human Oversight
- **Project Owner**: Defines scope in spec.md, reviews quality reports, approves phases
- **Technical Reviewer**: Validates formulas, code accuracy, and technical claims
- **Final Approver**: Reviews quality report, approves deployment

---

## IX. Runtime Guidance for AI Agents

### AI Agent Responsibilities
- Follow the 6-phase workflow defined in plan.md strictly
- Reference spec.md for scope boundaries and success criteria
- Execute tasks.md sequentially, respecting phase dependencies
- Generate quality reports at checkpoints
- Flag any deviations from quality gates immediately

### Scope Boundaries
- Content limited to 4 modules, 14 chapters as defined in spec.md
- No expansion beyond defined chapter structure without spec amendment
- Code examples embedded in markdown only (no separate repository)
- No video content, interactive simulations, or LMS integration

### Quality Enforcement
- AI must run automated checks: Flesch-Kincaid, plagiarism scan, flake8, black
- AI must generate citation compliance reports
- AI must validate all prerequisites and cross-references
- AI must verify build succeeds before declaring phase complete

### Human Sign-Off Required For
- Publishing any module (after Phase 4 quality gates pass)
- Final deployment to GitHub Pages (after Phase 6)
- Any deviation from spec.md scope
- Amendment to this constitution

---

## X. Success Criteria Summary

### Content Completeness
- ✓ 14 chapters published (across 4 modules)
- ✓ Course introduction completed
- ✓ 4 appendices completed
- ✓ 100+ term glossary completed
- ✓ 50+ tested code examples (all runnable)
- ✓ 50+ authoritative sources (50%+ peer-reviewed)

### Quality Metrics (All Mandatory)
- ✓ Flesch-Kincaid Grade 12-14 for all chapters
- ✓ Active voice ≥70% for all chapters
- ✓ Zero plagiarism (0% unoriginal content)
- ✓ All code passes flake8 and black
- ✓ All citations in APA 7th edition
- ✓ Build succeeds with zero errors
- ✓ Zero broken links

### Deployment Requirements
- ✓ Site deployed to GitHub Pages
- ✓ Build time <5 minutes
- ✓ Initial page load <3 seconds
- ✓ Search response <300ms
- ✓ All GPU examples have cloud alternatives

---

## XI. Non-Negotiable Principles (Constitution Core)

These principles override all other considerations:

1. **Accuracy through primary source verification** — Every claim must be traceable
2. **Clarity for academic audience** — Flesch-Kincaid 12-14 maintained
3. **Reproducibility** — Every claim must have a verifiable source
4. **Rigor** — 50%+ peer-reviewed sources enforced
5. **Complete citation** — APA 7th edition for all factual claims
6. **Writing clarity** — Graduate-level technical standards
7. **Zero tolerance for plagiarism** — Mandatory scan before publication

**These principles cannot be amended or waived under any circumstances.**

---

## Version History
- **v1.0.0** (2025-12-10): Initial constitution aligned with 4-module, 14-chapter textbook structure