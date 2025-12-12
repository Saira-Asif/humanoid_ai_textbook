# Implementation Plan: 1-humanoid-ai-textbook

**Branch**: `main` | **Date**: 2025-12-05 | **Spec**: specs/1-humanoid-ai-textbook/spec.md
**Input**: Feature specification from `/specs/1-humanoid-ai-textbook/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the strategy for developing the Humanoid AI Textbook, focusing on Physical AI and Embodied Intelligence, following a Docusaurus-based web textbook format. The technical approach aligns with a 13-week semester structure, organized into 4 modules covering ROS 2, Digital Twins, NVIDIA Isaac, and Vision-Language-Action models. Content delivery targets graduate students with embedded code examples and incremental publishing support.

## Technical Context

**Language/Version**: Python 3.10+
**Technology Stack/Dependencies Standards**:
- Frontend/Platform: Docusaurus v3
- Deployment: GitHub Pages
- Authoring Tools: Spec-Kit Plus + Claude Code
**Storage**: Filesystem (Markdown/MDX)
**Testing**: : Docusaurus build validation, Broken link checker, Flesch-Kincaid readability test, Plagiarism scan
**Target Platform**: GitHub Pages (static site hosting), responsive web design
**Project Type**:Technical Textbook / Documentation Site
**Performance Goals**: : Initial page load < 3 seconds, Search response < 300ms
**Constraints**: GitHub Pages deployment (free tier, static site only)
Incremental publishing (modules can deploy independently)
Build time < 5 minutes
**Scale/Scope**:
- 4 modules across 13 weeks
- 14 chapters total:
- Module 1: 5 chapters (ROS 2 Fundamentals)
- Module 2: 3 chapters (Digital Twin - Gazebo & Unity)
- Module 3: 3 chapters (NVIDIA Isaac)
- Module 4: 3 chapters (Vision-Language-Action)
- 100+ glossary terms
- 4 appendices (ROS 1 migration, Advanced patterns, Gazebo plugins, Math deep-dives)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x]**Accuracy through primary source verification:** Plan includes robust citation management and content validation.
- [x] **Clarity for an academic audience with a computer science background:** Plan addresses Flesch-Kincaid readability target.
- [x] **Reproducibility: every factual claim must be traceable to a verifiable source:** Plan specifies citation formats and testable code examples.
- [x] **Rigour: emphasis on peer-reviewed, high-quality sources:** Plan requires 50%+ peer-reviewed sources.
- [x] **All factual claims must be cited.**
- [x] **Citation format: APA 7th edition.**
- [x] **Minimum 50% peer-reviewed sources across all work
- [x] **Writing clarity: Flesch-Kincaid reading grade 12–14:** Aligned with spec.md target for graduate-level technical content.
- [x] **Zero tolerance for plagiarism; mandatory plagiarism scan before submission.**

## Project Structure

### Documentation (this feature)

```text
specs/1-humanoid-ai-textbook
├── checklists/          # Quality validation checklists
│   └── requirements.md
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```
humanoid_ai_book/
├── textbook-site/                # Docusaurus project root
│   ├── docs/                     # Main content directory
│   │   ├── intro.md              # Course introduction (Weeks 1-2)
│   │   ├── module-1-ros2/        # Module 1: ROS 2 (Weeks 3-5)
│   │   │   ├── index.md          # Module overview
│   │   │   ├── chapter1.mdx      # Nodes, Topics, Services
│   │   │   ├── chapter2.mdx      # Python & rclpy
│   │   │   ├── chapter3.mdx      # URDF for Humanoids
│   │   │   ├── chapter4.mdx      # Advanced Topics
│   │   │   └── chapter5.mdx      # ROS 2 Integration
│   │   ├── module-2-digital-twin/ # Module 2: Digital Twin (Weeks 6-7)
│   │   │   ├── index.md
│   │   │   ├── chapter1.mdx      # Gazebo Simulation
│   │   │   ├── chapter2.mdx      # Unity Integration
│   │   │   └── chapter3.mdx      # Sensor Simulation
│   │   ├── module-3-isaac/       # Module 3: NVIDIA Isaac (Weeks 8-10)
│   │   │   ├── index.md
│   │   │   ├── chapter1.mdx      # Isaac Sim
│   │   │   ├── chapter2.mdx      # Isaac ROS & VSLAM
│   │   │   └── chapter3.mdx      # Nav2 Path Planning
│   │   ├── module-4-vla/         # Module 4: VLA (Weeks 11-13)
│   │   │   ├── index.md
│   │   │   ├── chapter1.mdx      # Voice-to-Action (Whisper)
│   │   │   ├── chapter2.mdx      # LLM Cognitive Planning
│   │   │   └── chapter3.mdx      # Capstone Project
│   │   ├── appendices/           # Reference materials
│   │   │   ├── appendixA.mdx     # ROS 1 to ROS 2 Migration
│   │   │   ├── appendixB.mdx     # Advanced ROS 2 Patterns
│   │   │   ├── appendixC.mdx     # Custom Gazebo Plugins
│   │   │   └── appendixD.mdx     # Math Deep-Dives
│   │   └── references/           # Quick references
│   │       ├── glossary.md       # 100+ robotics terms
│   │       └── troubleshooting.md
│   │
│   ├── src/                      # Custom React components (optional)
│   │   ├── components/
│   │   │   └── ModuleCard.tsx    # Module navigation cards
│   │   └── pages/
│   │       └── index.tsx         # Custom homepage
│   │
│   ├── static/                   # Static assets
│   │   └── img/                  # Images by module
│   │
│   ├── docusaurus.config.js      # Main configuration
│   ├── sidebars.js               # Sidebar navigation
│   └── package.json              # Node dependencies
│
├── specs/                        # Feature specifications
├── history/                      # ADRs and prompts
└── .specify/                     # Spec-Kit Plus configuration
```
**Structure Decision:** Docusaurus-based documentation site with 4 modules containing 14 total chapters. All code examples embedded in markdown for maintenance simplicity.

## Implementation Phases

The book creation process is broken down into 4-6 phases focused on how the AI builds the textbook, not what content goes into it.

### Phase 1: Research & Requirements (Estimated: 2-4 hours)
****Objective:** Gather authoritative sources and establish content requirements for all 4 modules.

### AI Tasks:
**Research and identify 50+ authoritative sources (50%+ peer-reviewed):**
- ROS 2 documentation and academic papers
- Gazebo/Unity simulation research
- NVIDIA Isaac technical documentation
- VLA model papers (Whisper, GPT integration)
**Create bibliography with APA 7th edition citations**
**Extract key concepts for each module**
**Identify prerequisite chains between chapters**
***Define learning objectives for all 14 chapters**

### Deliverables:

- **research-bibliography.md** - Complete source list with citations
- **learning-objectives.md** - Chapter-by-chapter learning outcomes
- **prerequisite-map.md** - Dependency graph between chapters

### Checkpoint:
Review source quality, verify 50%+ peer-reviewed, confirm prerequisite logic

### Phase 2: Foundation & Structure (Estimated: 1-2 hours)
**Objective**: Set up Docusaurus project and establish content templates.

### AI Tasks:
1. **Initialize Docusaurus project in** textbook-site/
2. **Configure** docusaurus.config.js:
  - Site metadata (title, tagline, URL)
  - Theme configuration
  - Plugin setup (search, syntax highlighting)
3. **Create sidebars.js with 4-module structure:**
- Module 1: 5 chapters
- Module 2: 3 chapters
- Module 3: 3 chapters
- Module 4: 3 chapters
4.  **Generate chapter templates with frontmatter metadata schema**
5. **Create directory structure for all modules**
6. **Set up glossary and appendices structure**

### Deliverables:

- Fully configured Docusaurus project
- Chapter templates with metadata schema
- Complete directory structure
- sidebars.js with navigation hierarchy

**Checkpoint:** Verify Docusaurus builds successfully (npm start works), validate directory structure

### Phase 3: Content Development (Estimated: 20-40 hours)
**Objective:** Write all 14 chapters, 4 appendices, and glossary content.

### AI Tasks:
1. **Module 1 (ROS 2)** - 
  - Write 5 chapters:Draft content using research sources
  - Embed code examples with explanations
  - Include learning objectives, prerequisites
  - Add inline citations (APA 7th edition)


2. **Module 2 (Digital Twin)** - Write 3 chapters:
  - Gazebo simulation techniques
  - Unity integration workflows
  - Sensor simulation (LiDAR, cameras, IMUs)

3. **Module 3 (NVIDIA Isaac)** - Write 3 chapters:
  - Isaac Sim setup and usage
  - Isaac ROS and VSLAM
  - Nav2 path planning for humanoids

4. **Module 4 (VLA)** - Write 3 chapters:
  - Whisper voice-to-action integration
  - LLM cognitive planning with GPT
  - Capstone project guide

5. **Appendices** - Write 4 reference documents:
  - ROS 1 to ROS 2 migration guide
  - Advanced ROS 2 patterns
  - Custom Gazebo plugins
  - Math fundamentals (kinematics, SLAM)

6. **Glossary** - Define 100+ robotics terms with cross-references

### Deliverables:
- 14 complete chapters (3000-5000 words each)
- 4 appendices (1000-2000 words each)
- Glossary with 100+ terms
- All content with embedded code examples and citations

**Checkpoint:** After each module, verify:
- Flesch-Kincaid Grade 12-14
- Active voice ≥70%
- All claims cited
- Code examples functional


### Phase 4: Quality Assurance & Validation (Estimated: 4-8 hours)
**Objective:** Run comprehensive quality checks and fix identified issues.

### AI Tasks:
1. **Readability Assessment:**
 - Run Flesch-Kincaid test on all chapters
 - Target: Grade 12-14
 - Revise any chapters outside range

2. **Citation Validation:**
- Verify all factual claims have citations
- Check APA 7th edition formatting
- Ensure 50%+ sources are peer-reviewed

3. **Plagiarism Scan:**
- Run plagiarism detection on all content
- Target: 0% unoriginal content
- Rewrite flagged sections

4. **Active Voice Check:**
- Analyze sentence structure
- Target: ≥70% active voice
- Revise passive constructions

5. **Build Validation:**
- Run npm run build - ensure no errors
- Check for broken links
- Validate all images load correctly

6. **Cross-Reference Check:**
- Verify prerequisite chains work
- Check glossary term links
- Validate inter-chapter references

### Deliverables:
- Quality report with all metrics
- Revised content meeting all standards
- Validated build with zero errors

**Checkpoint:** All quality gates pass (Flesch-Kincaid 12-14, 0% plagiarism, ≥70% active voice, build succeeds)

### Phase 5: Integration & Polish (Estimated: 2-4 hours)
**Objective:** Finalize navigation, search, and user experience.

### AI Tasks:
1. **Homepage Creation:**
- Design module overview dashboard
- Add quick links to key sections
- Create visual module cards

2. **Search Configuration:**
- Configure Docusaurus search
- Add glossary search functionality
- Test search accuracy

3. **Navigation Refinement:**
- Optimize sidebar labels
- Add breadcrumbs
- Ensure mobile responsiveness

4. **Visual Polish:**
- Add module images/diagrams
- Optimize image sizes (<500KB)
- Ensure consistent styling

5. **Final Content Pass:**
- Proofread for typos
- Check formatting consistency
- Verify all metadata complete

### Deliverables:
- Polished homepage
- Functional search
- Optimized navigation
- Production-ready site

**Checkpoint:** Manual review of full site, test on multiple devices, verify user experience

### Phase 6: Deployment & Documentation (Estimated: 1-2 hours)
**Objective:** Deploy to GitHub Pages and create usage documentation.

### AI Tasks:
1. **Deployment Setup:**
- Configure GitHub Pages settings
- Set up deployment workflow
- Test deployment process

2. **Build & Deploy:**
- Run production build: npm run build
- Deploy to GitHub Pages
- Verify live site functionality

3. **Documentation:**
- Create README.md with: 
  - Project overview
  - How to run locally
  - How to contribute
  - Quality standards
- Document project status
- List completed vs. pending work

4. **Final Verification:**
- Test all links on live site
- Verify search works
- Check mobile responsiveness
- Confirm all images load

### Deliverables:
- Live site on GitHub Pages
- Complete README.md
- Project status documentation
- Deployment verified

**Checkpoint:** Site live and accessible, all features working, documentation complete

## Dependencies and Sequencing
### Phase Dependencies:
- Phase 2 depends on Phase 1 (need research before building structure)
- Phase 3 depends on Phase 2 (need structure before writing content)
- Phase 4 depends on Phase 3 (need content before quality checks)
- Phase 5 depends on Phase 4 (need validated content before polish)
- Phase 6 depends on Phase 5 (need polished site before deployment)

### Module Content Dependencies:

- Module 1 (ROS 2) is foundational - must complete first
- Module 2 (Digital Twin) builds on ROS 2 concepts
- Module 3 (Isaac) requires ROS 2 and simulation knowledge
- Module 4 (VLA) integrates all previous modules

### Parallel Opportunities:

- Appendices can be written in parallel with modules
- Glossary can be populated throughout content development
- Quality checks can run per-module rather than waiting for all content


## Component Breakdown

-   **Module Structure**: The textbook is organized into 4 modules, encompassing 14 chapters. 4 appendices (ROS 1 migration, Advanced patterns, Gazebo plugins, Math deep-dives). Content will be written in Markdown/MDX within the `docs/modules/` directory.

-   **Citation Management**: A rigorous system will be implemented to ensure 50+ authoritative sources (50%+ peer-reviewed) are cited using APA 7th edition format. This will involve tracking citations and ensuring direct links to sources.
-   **Quality Validation Strategy**: Regular checks for Flesch-Kincaid readability (target 12-14), mandatory plagiarism scans, and comprehensive code ex ecution tests will be integrated throughout the development phases.

## Design Decisions for ADRs

The following architecturally significant decisions are highlighted for potential Architectural Decision Records (ADRs) due to their cross-module impact, existence of alternatives, and influence on the textbook's development:

1.  **Multi-Platform Robotics Example Strategy**:
    *   **Description**: Decision: Generic URDF primary + Platform Adaptation Notes
    *   **Rationale for ADR**: This decision impacts the complexity of all code examples, student setup, and aligns with the course's diverse hardware requirements. It involves tradeoffs between broad compatibility and specific platform optimizations.
    *   **ADR Suggestion**: See: history/adr/001-multi-platform-robotics-strategy.md

2.  **Textbook Citation Management and Verification Workflow**:
    *   **Description**: Defining the definitive process and tooling for managing, integrating, and verifying 50+ authoritative APA 7th edition citations, ensuring 50%+ are peer-reviewed and all claims are traceable.
    *   **Rationale for ADR**:  Robust citation management with APA compliance and direct linking

3.  **Sim-to-Real Deployment Strategy for Edge Robotics**:
    *   **Description**: Establishing the standardized approach for documenting and implementing sim-to-real pipelines, specifically targeting NVIDIA Jetson Orin Nano, and providing cloud/simulation alternatives for GPU-heavy examples.
    *   **Rationale for ADR**: This is a critical success criterion (90% of students successfully run sim-to-real) impacting Module 7 and requires careful planning for hardware, software, and documentation.
 