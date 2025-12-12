# Tasks: Humanoid AI Textbook

**Input**: Design documents from `/specs/1-humanoid-ai-textbook/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by implementation phase to align with the 6-phase structure in plan.md.

## Format: `[ID] [P?] [Phase] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Phase]**: Which phase this task belongs to (Phase 1-6)
- Include exact file paths in descriptions

## Path Conventions

Based on plan.md structure:
- Docusaurus project: `textbook-site/`
- Content: `textbook-site/docs/`
- Code examples: Embedded in markdown files

---

## Phase 1: Research & Requirements (2-4 hours)

**Objective**: Gather authoritative sources and establish content requirements for all 4 modules.

- [x] T001 Research and identify 50+ authoritative sources (50%+ peer-reviewed) for ROS 2, Gazebo/Unity, NVIDIA Isaac, and VLA models
- [x] T002 Create `specs/1-humanoid-ai-textbook/research-bibliography.md` with APA 7th edition citations
- [x] T003 Extract key concepts for each of the 4 modules and document in research.md
- [x] T004 Create `specs/1-humanoid-ai-textbook/prerequisite-map.md` showing dependency graph between 14 chapters
- [x] T005 Create `specs/1-humanoid-ai-textbook/learning-objectives.md` with chapter-by-chapter learning outcomes for all 14 chapters

**Checkpoint**: Review source quality, verify 50%+ peer-reviewed, confirm prerequisite logic

---

## Phase 2: Foundation & Structure (1-2 hours)

**Objective**: Set up Docusaurus project and establish content templates.

- [x] T006 Initialize Docusaurus project: Run `npx create-docusaurus@latest textbook-site classic` in the `humanoid_ai_book/` directory
- [x] T007 Configure `textbook-site/docusaurus.config.js` with site metadata, theme, and plugins
- [x] T008 Create `textbook-site/sidebars.js` with 4-module navigation hierarchy (5+3+3+3 chapters)
- [x] T009 [P] Create directory structure: `docs/intro.md`
- [x] T010 [P] Create directory structure: `docs/module-1-ros2/` with 5 chapter placeholders
- [x] T011 [P] Create directory structure: `docs/module-2-digital-twin/` with 3 chapter placeholders
- [x] T012 [P] Create directory structure: `docs/module-3-isaac/` with 3 chapter placeholders
- [x] T013 [P] Create directory structure: `docs/module-4-vla/` with 3 chapter placeholders
- [x] T014 [P] Create directory structure: `docs/appendices/` with 4 appendix placeholders
- [x] T015 [P] Create directory structure: `docs/references/glossary.md` and `docs/references/troubleshooting.md`
- [x] T016 Generate chapter template with frontmatter metadata schema (title, description, learning_objectives, prerequisites)
- [x] T017 [P] Test Docusaurus build: Run `npm start` and verify site loads

**Checkpoint**: Verify Docusaurus builds successfully, validate directory structure

---

## Phase 3: Content Development (20-40 hours)

**Objective**: Write all 14 chapters, 4 appendices, and glossary content.

### Module 1: ROS 2 Fundamentals (5 chapters)

- [x] T018 Draft `docs/intro.md` - Course introduction (Weeks 1-2)
- [x] T019 Draft `docs/module-1-ros2/index.md` - Module 1 overview
- [x] T020 Draft `docs/module-1-ros2/chapter1.mdx` - Nodes, Topics, Services (3000-5000 words, embedded code examples, inline APA citations)
- [x] T021 Draft `docs/module-1-ros2/chapter2.mdx` - Python & rclpy
- [x] T022 Draft `docs/module-1-ros2/chapter3.mdx` - URDF for Humanoids
- [x] T023 Draft `docs/module-1-ros2/chapter4.mdx` - Advanced Topics
- [x] T024 Draft `docs/module-1-ros2/chapter5.mdx` - ROS 2 Integration

### Module 2: Digital Twin (3 chapters)

- [x] T025 Draft `docs/module-2-digital-twin/index.md` - Module 2 overview
- [x] T026 Draft `docs/module-2-digital-twin/chapter1.mdx` - Gazebo Simulation
- [x] T027 Draft `docs/module-2-digital-twin/chapter2.mdx` - Unity Integration
- [x] T028 Draft `docs/module-2-digital-twin/chapter3.mdx` - Sensor Simulation

### Module 3: NVIDIA Isaac (3 chapters)

- [x] T029 Draft `docs/module-3-isaac/index.md` - Module 3 overview
- [x] T030 Draft `docs/module-3-isaac/chapter1.mdx` - Isaac Sim
- [x] T031 Draft `docs/module-3-isaac/chapter2.mdx` - Isaac ROS & VSLAM
- [x] T032 Draft `docs/module-3-isaac/chapter3.mdx` - Nav2 Path Planning

### Module 4: Vision-Language-Action (3 chapters)

- [x] T033 Draft `docs/module-4-vla/index.md` - Module 4 overview
- [x] T034 Draft `docs/module-4-vla/chapter1.mdx` - Voice-to-Action (Whisper)
- [x] T035 Draft `docs/module-4-vla/chapter2.mdx` - LLM Cognitive Planning
- [x] T036 Draft `docs/module-4-vla/chapter3.mdx` - Capstone Project

### Appendices & References

- [x] T037 [P] Draft `docs/appendices/appendix-a.mdx` - ROS 1 to ROS 2 Migration (1000-2000 words)
- [x] T038 [P] Draft `docs/appendices/appendix-b.mdx` - Advanced ROS 2 Patterns
- [x] T039 [P] Draft `docs/appendices/appendix-c.mdx` - Custom Gazebo Plugins
- [x] T040 [P] Draft `docs/appendices/appendix-d.mdx` - Math Deep-Dives (kinematics, SLAM)
- [x] T041 [P] Draft `docs/references/glossary.md` - Define 100+ robotics terms with cross-references
- [x] T042 [P] Draft `docs/references/troubleshooting.md` - Common issues and solutions

**Checkpoint after each module**: Verify Flesch-Kincaid Grade 12-14, Active voice ≥70%, All claims cited, Code examples functional

---

## Phase 4: Quality Assurance & Validation (4-8 hours)

**Objective**: Run comprehensive quality checks and fix identified issues.

### Readability Assessment

- [x] T043 Run Flesch-Kincaid test on all 14 chapters (target: Grade 12-14)
- [x] T044 Run Flesch-Kincaid test on all 4 appendices
- [x] T045 Revise any content outside Grade 12-14 range

### Citation Validation

- [x] T046 Verify all factual claims have APA 7th edition citations across all chapters
- [x] T047 Verify all factual claims have citations in appendices
- [x] T048 Check that 50%+ sources are peer-reviewed (cross-reference with research-bibliography.md)

### Plagiarism Scan

- [x] T049 Run plagiarism detection on Module 1 chapters (target: 0% unoriginal)
- [x] T050 Run plagiarism detection on Module 2 chapters
- [x] T051 Run plagiarism detection on Module 3 chapters
- [x] T052 Run plagiarism detection on Module 4 chapters
- [x] T053 Run plagiarism detection on appendices
- [x] T054 Rewrite any flagged sections

### Active Voice Check

- [x] T055 Analyze sentence structure for all content (target: ≥70% active voice)
- [x] T056 Revise passive constructions across all chapters

### Build Validation

- [X] T057 Run `npm run build` - ensure no errors
- [X] T058 Check for broken links across entire site
- [X] T059 Validate all embedded code examples are syntactically correct
- [X] T060 Validate all images load correctly (if any added)

### Cross-Reference Check

- [X] T061 Verify prerequisite chains work between all 14 chapters
- [X] T062 Check glossary term links from chapters
- [X] T063 Validate inter-chapter references

### Quality Report

- [X] T064 Generate quality report with all metrics (readability, citations, plagiarism, active voice, build status)

**Checkpoint**: All quality gates pass (Flesch-Kincaid 12-14, 0% plagiarism, ≥70% active voice, build succeeds)

---

## Phase 5: Integration & Polish (2-4 hours)

**Objective**: Finalize navigation, search, and user experience.

### Homepage Creation

- [X] T065 Design module overview dashboard in `textbook-site/src/pages/index.tsx` (or custom homepage)
- [X] T066 Add quick links to key sections (modules, glossary, appendices)
- [X] T067 [P] Create visual module cards component in `textbook-site/src/components/ModuleCard.tsx`

### Search Configuration

- [X] T068 Configure Docusaurus search plugin
- [X] T069 Add glossary to search index
- [X] T070 Test search accuracy with sample queries

### Navigation Refinement

- [X] T071 Optimize sidebar labels in `textbook-site/sidebars.js`
- [X] T072 Add breadcrumbs configuration
- [X] T073 Test mobile responsiveness on 3+ devices

### Visual Polish

- [X] T074 [P] Add module overview images to `textbook-site/static/img/`
- [X] T075 [P] Optimize all images (<500KB each)
- [X] T076 Ensure consistent styling across all pages (CSS/theme check)

### Final Content Pass

- [X] T077 Proofread all chapters for typos
- [X] T078 Check formatting consistency (headings, code blocks, citations)
- [X] T079 Verify all frontmatter metadata is complete

**Checkpoint**: Manual review of full site, test on multiple devices, verify user experience

---

## Phase 6: Deployment & Documentation (1-2 hours)

**Objective**: Deploy to GitHub Pages and create usage documentation.

### Deployment Setup

- [X] T080 Configure GitHub Pages settings in repository
- [X] T081 Set up GitHub Actions deployment workflow (`.github/workflows/deploy.yml`)
- [X] T082 Test deployment process in staging environment

### Build & Deploy

- [X] T083 Run production build: `npm run build`
- [X] T084 Deploy to GitHub Pages
- [X] T085 Verify live site functionality at GitHub Pages URL

### Documentation

- [X] T086 Create `README.md` with project overview, local setup instructions, contribution guidelines, quality standards
- [X] T087 Document project status (completed modules, pending work)
- [X] T088 Create `CONTRIBUTING.md` with guidelines for future content additions

### Final Verification

- [X] T089 Test all links on live site
- [X] T090 Verify search works on deployed site
- [X] T091 Check mobile responsiveness on live site
- [X] T092 Confirm all images load on deployed site
- [X] T093 Test site performance (initial page load < 3 seconds, search < 300ms)

**Checkpoint**: Site live and accessible, all features working, documentation complete

---

## Dependencies & Execution Order

### Phase Dependencies (Sequential)

1. **Phase 1 (Research)** → Must complete before Phase 2
2. **Phase 2 (Foundation)** → Must complete before Phase 3
3. **Phase 3 (Content Development)** → Must complete before Phase 4
4. **Phase 4 (Quality Assurance)** → Must complete before Phase 5
5. **Phase 5 (Integration & Polish)** → Must complete before Phase 6
6. **Phase 6 (Deployment)** → Final phase

### Within-Phase Parallelization

- **Phase 2**: Tasks T009-T015 (directory creation) can run in parallel
- **Phase 3**: Module writing can be partially parallelized (after Module 1 completes, Modules 2-4 can proceed)
- **Phase 3**: Appendices (T037-T042) can be written in parallel with modules
- **Phase 4**: Plagiarism scans (T049-T053) can run in parallel by module
- **Phase 5**: Homepage, search, navigation work can overlap with visual polish

### Content Dependencies

- Module 1 must be completed before Module 2 (ROS 2 foundation required)
- Module 2 must be completed before Module 3 (simulation concepts required)
- Module 3 must be completed before Module 4 (Isaac knowledge required for VLA integration)

---

## Implementation Strategy

### Sequential Execution (Recommended for Solo Developer)

1. Complete Phase 1 (Research) fully
2. Complete Phase 2 (Foundation) fully
3. Complete Phase 3 (Content) sequentially: Module 1 → Module 2 → Module 3 → Module 4 → Appendices
4. Complete Phase 4 (Quality Assurance) fully
5. Complete Phase 5 (Integration & Polish) fully
6. Complete Phase 6 (Deployment) fully

### Incremental Delivery Strategy

- After Phase 2: Deploy empty structure to verify infrastructure
- After each module in Phase 3: Run mini quality checks and deploy incrementally
- After Phase 4: Full validation checkpoint before polish
- After Phase 6: Final production deployment

---

## Notes

- [P] tasks = different files, no dependencies, can run in parallel
- Tasks are organized by 6 implementation phases from plan.md
- Each phase has clear objectives and checkpoints
- Commit after completing each task or logical group
- Module content must be developed sequentially due to prerequisite dependencies
- Total estimated time: 30-60 hours across all phases