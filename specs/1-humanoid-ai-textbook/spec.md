# Humanoid AI Textbook: Physical AI & Embodied Intelligence

## Project Overview

- **Format**: Docusaurus-based web textbook (Markdown/MDX)
- **Target Course**: Physical AI & Humanoid Robotics (graduate/advanced undergraduate)
- **Timeline**: 13-week semester structure
- **Deployment**: GitHub Pages via Docusaurus v3

## Target Audience

- **Primary**: Graduate students in CS, Robotics, Mechatronics, AI
- **Secondary**: Educators/lab instructors, robotics practitioners
- **Prerequisites**: Python 3.x, basic Linux, linear algebra
- **Tone**: Conversational but rigorous (Flesch-Kincaid Grade 12-14)

## Content Structure

**4 modules, 14 chapters total:**

### Course Introduction (Weeks 1-2)
- Introduction to Physical AI and Embodied Intelligence

### Module 1: ROS 2 Fundamentals (Weeks 3-5, 5 chapters)
- Chapter 1: Nodes, Topics, Services
- Chapter 2: Python & rclpy
- Chapter 3: URDF for Humanoids
- Chapter 4: Advanced Topics
- Chapter 5: ROS 2 Integration

### Module 2: Digital Twin (Weeks 6-7, 3 chapters)
- Chapter 1: Gazebo Simulation
- Chapter 2: Unity Integration
- Chapter 3: Sensor Simulation

### Module 3: NVIDIA Isaac (Weeks 8-10, 3 chapters)
- Chapter 1: Isaac Sim
- Chapter 2: Isaac ROS & VSLAM
- Chapter 3: Nav2 Path Planning

### Module 4: Vision-Language-Action Models (Weeks 11-13, 3 chapters)
- Chapter 1: Voice-to-Action (Whisper)
- Chapter 2: LLM Cognitive Planning
- Chapter 3: Capstone Project

### Appendices
- **Appendix A**: ROS 1 to ROS 2 Migration Notes
- **Appendix B**: Advanced ROS 2 Patterns (Lifecycle Nodes, Component Composition)
- **Appendix C**: Custom Gazebo Plugins for Humanoids
- **Appendix D**: Math Deep-Dives (Kinematics, Dynamics, SLAM)

### References
- **Glossary**: 100+ robotics and AI terms with cross-references
- **Troubleshooting Guide**: Common issues and solutions

## User Scenarios & Testing

### User Story 1 - Navigate Complete Course Structure (Priority: P1)

As an **industry practitioner** learning Physical AI, I need to see the complete 13-week course structure organized by modules and weeks, so I can plan my learning journey and understand prerequisite relationships between topics.

**Independent Test**: Can be fully tested by viewing the table of contents, confirming all 13 weeks are represented, all 4 modules are clearly delineated, and prerequisite chains are visible.

**Acceptance Scenarios**:
1. **Given** I am a new student starting the course, **When** I open the textbook homepage, **Then** I see a dashboard with 4 module cards displaying titles and week ranges
2. **Given** I want to understand course progression, **When** I view the table of contents, **Then** I can see which chapters belong to which weeks and modules
3. **Given** I am on Week 5, **When** I navigate to Module 1 content, **Then** I can see all chapters for Weeks 3-5 grouped together
4. **Given** I need to review prerequisites, **When** I open any chapter, **Then** I see clearly stated prerequisite weeks/chapters

### User Story 2 - Access Foundational Setup Documentation (Priority: P1)

As an **industry practitioner**, I need immediate access to hardware setup guides, environment configuration, and glossary references before starting course content, so I can prepare my development environment and understand terminology.

**Independent Test**: Can be fully tested by accessing hardware setup guide, verifying all 3 hardware options are documented (Digital Twin Workstation, Edge Kit, Cloud setup), and confirming glossary is searchable.

**Acceptance Scenarios**:
1. **Given** I am setting up my learning environment, **When** I navigate to the setup section, **Then** I see detailed guides for all 3 hardware options (Workstation, Jetson Kit, Cloud)
2. **Given** I encounter unfamiliar robotics terminology, **When** I use the glossary search, **Then** I get instant term lookup with definitions and links to relevant chapters
3. **Given** I need to install ROS 2 and Isaac Sim, **When** I follow the setup guide, **Then** I have step-by-step instructions with version specifications
4. **Given** I have budget constraints, **When** I review hardware options, **Then** I can compare costs and capabilities to make an informed decision

### User Story 3 - Follow Module-Based Learning Path (Priority: P2)

As an **industry practitioner**, I need to progress through each module (ROS 2 → Digital Twin → Isaac → VLA) sequentially with clear module objectives and capstone integration points, so I understand how each module builds toward the final autonomous humanoid project.

**Independent Test**: Can be fully tested by navigating through each module, verifying module learning outcomes are stated, and confirming capstone integration points are documented.

**Acceptance Scenarios**:
1. **Given** I completed Module 1 (ROS 2), **When** I start Module 2 (Digital Twin), **Then** I see how ROS 2 concepts are applied in simulation
2. **Given** I am working on Module 3 (Isaac), **When** I review the module overview, **Then** I see clear learning outcomes and how this contributes to the capstone project
3. **Given** I am planning my study schedule, **When** I view module summaries, **Then** I can estimate time commitment for each module
4. **Given** I completed all modules, **When** I reach Module 4 final section, **Then** I have a clear integration guide for the capstone project

## Focus Areas

### Physical AI Content Balance
- **Humanoid-specific content (~40%)**: Bipedal locomotion, humanoid kinematics/dynamics, balance control, humanoid manipulation
- **Transferable Physical AI content (~60%)**: ROS 2, Gazebo, Isaac Sim, VSLAM, VLA, sensor fusion, sim-to-real

### Technology Stack
- **ROS 2**: Humble Hawksbill (pure ROS 2, no ROS 1 except migration appendix)
- **Simulation**: Gazebo Fortress, NVIDIA Isaac Sim 4.0+, Unity integration
- **VLA Models**: Practical application using pre-trained models (not deep theory)
  - **Voice**: OpenAI Whisper (for voice commands)
  - **Language**: GPT-4 API or Claude API (for cognitive planning and translating natural language to ROS 2 actions)
  - **Vision**: CLIP (OpenAI) for vision-language understanding
  - **Action**: RT-2 concepts demonstrated, or OpenVLA (open-source alternative)
  - **Integration**: Demonstrate how LLMs translate commands like "Clean the room" into ROS 2 action sequences
  - **Deployment**: All models must run efficiently on Jetson Orin Nano (8GB) for edge deployment

### Robot Platform Strategy
Multi-platform approach with adaptation notes:
- **Primary Simulation**: Generic URDF humanoid (transferable to any platform)
- **Advanced Simulation**: Unitree G1/H1 humanoid in Isaac Sim
- **Budget Examples**: Hiwonder TonyPi Pro adaptations ($600 alternative)
- **Deployment Target**: NVIDIA Jetson Orin Nano (8GB)
- **Proxy Robot Support**: Include Unitree Go2 (quadruped) examples (software principles transfer 90% to humanoids)
- **Simulation Compatibility**: All examples must work in both Isaac Sim and Gazebo
- **Platform Adaptation Notes**: Every example includes notes for Unitree G1/H1 (humanoid), Unitree Go2 (quadruped), and Hiwonder TonyPi (budget)

### Conversational AI
- GPT/Whisper integration for voice commands
- LLM-based cognitive planning for robot actions

## Requirements

### Functional Requirements

- **FR-001**: Book MUST organize content into 4 distinct modules aligned with course structure: Module 1 (ROS 2 - Weeks 3-5), Module 2 (Digital Twin - Weeks 6-7), Module 3 (NVIDIA Isaac - Weeks 8-10), Module 4 (VLA - Weeks 11-13)

- **FR-002**: Book MUST include a dedicated "Introduction" section covering Weeks 1-2 (Physical AI Foundations) before Module 1

- **FR-003**: Book MUST provide 3 hardware setup paths: (1) Digital Twin Workstation (RTX + Ubuntu), (2) Physical AI Edge Kit (Jetson Orin Nano), (3) Cloud-Native Setup (AWS/Azure)

- **FR-004**: Each module MUST state clear learning outcomes that map to course learning outcomes

- **FR-005**: Book MUST include a "Capstone Project Guide" section detailing the autonomous humanoid project architecture (voice → plan → navigate → perceive → manipulate)

- **FR-006**: Book MUST include reference materials: Glossary (100+ robotics terms with search), Notation Guide (mathematical symbols), ROS 2 Quick Reference, Troubleshooting Guide

- **FR-007**: Navigation structure MUST use a single sidebar with nested collapsible categories organized by modules, with cross-references enabling access by week (1-13), by module (1-4), and by topic

- **FR-008**: Each chapter MUST declare prerequisites (specific prior weeks/chapters or external knowledge)

- **FR-009**: Book structure MUST support incremental content delivery (Week 1-2 content can be published independently of later weeks)

- **FR-010**: Each chapter MUST include frontmatter metadata: `estimated_time` (hours), `week`, `module`, `prerequisites` (array), `learning_objectives` (array), `sidebar_label`

- **FR-011**: Homepage MUST use a dashboard-style layout featuring: (1) grid of 4 module cards showing title, week range, and learning outcomes, (2) quick links sidebar for hardware setup and glossary, (3) recent updates section for content changes

### Key Entities

- **Module**: Represents a major course section (4 total: ROS 2, Digital Twin, Isaac, VLA). Contains learning outcomes, week ranges, chapters, and integration points with capstone

- **Chapter**: Represents a single topic within a module. Metadata includes: estimated_time (hours), week number, module number, prerequisites (array of prior chapters/weeks), learning_objectives (array), sidebar_label. Contains content sections, code examples, and references

- **Part**: High-level grouping of content. Parts include: Introduction, Modules 1-4, Capstone Guide, References

- **Hardware Configuration**: Represents one of three setup paths. Contains hardware requirements, software installation steps, cost estimates, and limitations

- **Reference Material**: Includes glossary entries, notation definitions, quick reference commands, troubleshooting solutions

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can locate any week's content within 2 clicks from the homepage (navigation efficiency)

- **SC-002**: 95% of prerequisite references are correctly linked (no broken internal links to prior chapters)

- **SC-003**: Each of the 4 modules has clearly stated learning outcomes that align with course learning outcomes

- **SC-004**: All 3 hardware setup paths are documented with complete step-by-step instructions

- **SC-005**: Students can identify which chapters contribute to each capstone project component within 5 minutes of reviewing the capstone guide

- **SC-006**: Table of contents shows estimated time commitment for each chapter, enabling students to plan a 13-week study schedule

- **SC-007**: Glossary contains at least 100 robotics terms with definitions and chapter cross-references, accessible via search

- **SC-008**: Book structure supports publishing Week 1-2 content independently as a functional mini-textbook (Introduction + Setup + Glossary)

### Content Quality Metrics

- **14 chapters published** (across 4 modules)
- **Course introduction completed** (Weeks 1-2)
- **4 appendices completed**
- **100+ term glossary completed**
- **50+ tested code examples** (embedded in chapters, all runnable)
- **Minimum 50 authoritative sources** (50%+ peer-reviewed, APA 7th edition)
- **Flesch-Kincaid Grade 12-14** achieved across all chapters
- **Active voice: At least 70%** of sentences
- **Zero plagiarism detected** (mandatory scan before completion)
- **All code passes** flake8 and black formatting
- **Zero-to-running time** for each example: under 15 minutes

### Student Success Metrics

- 80% of students complete Module 1 ROS 2 setup in under 2 hours
- 90% of students successfully run sim-to-real pipeline on edge kits
- 70% of students implement at least one VLA-driven action pipeline

### Deployment Requirements

- All GPU examples have cloud/simulation alternatives
- Site deployed to GitHub Pages
- Build time under 5 minutes
- Initial page load under 3 seconds
- Search response under 300ms

## Technical Constraints

### Operating Environment
- **Operating System**: Ubuntu 22.04 LTS (primary), Docker/WSL2 (Windows/macOS)
- **ROS Version**: ROS 2 Humble Hawksbill (LTS)
- **Simulators**: Gazebo Fortress (primary), NVIDIA Isaac Sim 4.0+ (advanced), Unity
- **Programming**: Python 3.10+

### Hardware Tiers
- **Cloud**: AWS g4dn.xlarge/T4 or equivalent
- **Local**: 16GB RAM, RTX 4070 Ti (12GB VRAM) minimum for simulation
- **Edge**: NVIDIA Jetson Orin Nano (8GB)

### Format Requirements
- **Platform**: Docusaurus v3
- **Content**: Markdown/MDX format
- **Diagrams**: Mermaid diagrams (no external image dependencies where possible)
- **Length**: 3000-5000 words per chapter, total ~50,000-70,000 words
- **Docker images**: Under 5GB per module
- **Dataset downloads**: Under 1GB per example

## Quality Standards

### Writing Standards
- All technical terms defined on first use with APA citation
- Active voice: At least 70% of sentences
- Flesch-Kincaid Grade 12-14 (graduate-level technical content)
- Progressive skill building: Chapter N assumes only Chapters 1 to N-1
- Each chapter has 3-5 learning objectives (Bloom's taxonomy)

### Code Standards
- Every code block includes: purpose comment, expected output, troubleshooting note
- All code passes flake8 and black formatting
- All code examples embedded in Markdown/MDX (no separate code repository)
- Zero-to-running time: under 15 minutes per example
- GPU-heavy examples include cloud/simulation alternatives

### Citation Standards
- APA 7th edition format for all citations
- Minimum 50 authoritative sources total
- 50%+ sources must be peer-reviewed
- All factual claims must be cited
- Direct links to sources where possible

## Edge Cases & Requirements

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

### Cloud vs Local
- Budget matrix provided (under $50 = local only, $50-200 = hybrid, $200+ = cloud-first)
- Provider-agnostic cloud instructions (AWS and Google Colab)
- No vendor lock-in

## Non-Goals (Explicitly NOT Building)

The following are **out of scope** for this textbook:

- Deep RL theory internals (PPO, SAC algorithms) beyond high-level overviews
- Commercial SDKs (Boston Dynamics, Tesla Optimus) unless open-source
- Extensive ethical debates (ethics covered in context, not as separate chapter)
- ROS 1 workflows (migration notes in appendix only, not main content)
- Custom hardware PCB design or motor selection
- Production CI/CD, Kubernetes orchestration for robotics
- Computer vision model training from scratch (use pre-trained models)
- NLP transformer training from scratch (use Hugging Face/OpenAI APIs)
- Non-humanoid platforms unless pedagogically necessary
- Separate code example repository (code embedded in chapters)
- Interactive simulations embedded in textbook (students use external tools)
- Automated grading systems for assessments
- Student progress tracking or LMS integration
- Video content or multimedia beyond static diagrams/images
- Translation to languages other than English
- Mobile app version (responsive web design only)
- Offline PDF export
- Community forum or discussion board (external to textbook)

## Acceptance Tests (Per Module)

### Module 1: ROS 2 Fundamentals
**Test**: Student can set up ROS 2 Humble and run `ros2 topic list`

### Module 2: Digital Twin
**Test**: Student spawns humanoid in Gazebo, runs 10-second simulation, creates basic digital twin mirroring sensor data

### Module 3: NVIDIA Isaac
**Test**: Student spawns humanoid in Isaac Sim, implements VSLAM, runs Nav2 path planning for 10+ seconds

### Module 4: Vision-Language-Action
**Test**: Student uses pre-trained VLA model (Whisper + LLM) for one voice-driven action task with 80%+ accuracy

## Assumptions

- Students are industry practitioners with programming knowledge (Python) as stated in course requirements
- Course duration is fixed at 13 weeks with 10-12 hours/week commitment
- Capstone project is the culminating assessment and all modules build toward it
- Hardware requirements follow NVIDIA Isaac Sim specifications (RTX GPU for workstation path)
- Content will be delivered via Docusaurus static site deployed to GitHub Pages
- ROS 2 version is Humble (Ubuntu 22.04 compatible)
- Isaac Sim is the primary simulation environment for Modules 3-4
- Students have access to at least one of the three hardware configurations
- Book will be continuously updated as hardware/software evolves

## Scope Boundaries

### In Scope

- Complete textbook structure covering all 13 weeks of course content
- 4 modules aligned with course syllabus
- Hardware setup documentation for all 3 configuration options
- Capstone project guide with detailed architecture
- Reference materials (glossary, notation, quick references, troubleshooting)
- Navigation structure supporting multiple access patterns (week, module, topic)
- Prerequisite tracking and dependency documentation

### Out of Scope

- Actual chapter content (covered in separate specs for each chapter/module)
- Separate code example repository (code examples embedded in chapters)
- Video content or multimedia beyond static diagrams/images
- Interactive simulations embedded in the textbook
- Automated grading systems for assessments
- Student progress tracking or LMS integration
- Translation to languages other than English
- Mobile app version
- Offline PDF export
- Community forum or discussion board

## Constitution

This textbook must uphold the following principles at all times:

1. **Accuracy through primary source verification**: All technical content must be traceable to authoritative sources
2. **Clarity for an academic audience with CS background**: Target Flesch-Kincaid Grade 12-14
3. **Reproducibility**: Every factual claim must be traceable to a verifiable source
4. **Rigor**: Emphasis on peer-reviewed, high-quality sources (50%+ peer-reviewed minimum)
5. **Complete citation**: All factual claims must be cited in APA 7th edition format
6. **Writing clarity**: Maintain graduate-level technical writing standards
7. **Zero tolerance for plagiarism**: Mandatory plagiarism scan before completion

These principles are non-negotiable and must be verified before any content is considered complete.