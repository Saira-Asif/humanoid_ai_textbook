# ADR 002: Docusaurus Component Strategy (Markdown-First vs TypeScript Components)

## Status
Accepted

## Date
2025-12-11

## Context
The Physical AI & Humanoid Robotics textbook requires a content delivery approach that balances academic rigor, maintainability, and searchability. The project constitution mandates Docusaurus v3 for deployment to GitHub Pages, with specific requirements for content structure, citation management, and accessibility. The decision affects how interactive elements, code examples, and specialized content components are implemented within the documentation framework.

## Problem Statement
Should the textbook rely primarily on pure Markdown/MDX for content delivery, or should we implement TypeScript-based interactive components for enhanced functionality? This decision impacts content maintainability, searchability, accessibility, and the ability to implement complex features like integrated glossary lookups, code execution environments, and interactive learning aids.

## Alternatives Considered

### Alternative 1: Pure Markdown-First Approach
- **Pros**:
  - Maximum simplicity and maintainability
  - Excellent searchability (all content is plain text)
  - Easy for authors to write and edit
  - Consistent rendering across all Docusaurus features
  - Minimal dependencies and faster builds
  - Full accessibility compliance by default
- **Cons**:
  - Limited interactivity and dynamic features
  - Cannot implement sophisticated glossary integration
  - No live code execution or playgrounds
  - Reduced ability to create custom learning aids
  - Less engaging for complex technical concepts

### Alternative 2: TypeScript-First Approach with Custom Components
- **Pros**:
  - Rich interactive features (code playgrounds, 3D viewers, etc.)
  - Sophisticated glossary integration with hover definitions
  - Custom learning aids (progress trackers, quizzes)
  - Dynamic content based on user preferences
  - Enhanced visual presentation for complex concepts
- **Cons**:
  - Reduced searchability (JS components not indexed as content)
  - Increased complexity and maintenance overhead
  - Potential accessibility issues with custom components
  - Longer build times with complex components
  - Higher skill requirements for content authors
  - Risk of component dependencies breaking over time

### Alternative 3: Hybrid Approach (Markdown-Primary with Selective Components)
- **Pros**:
  - Maintains searchability for core content
  - Selective enhancement where most beneficial
  - Balanced maintainability vs functionality
  - Core content remains editable in Markdown
  - Strategic use of components for key features
- **Cons**:
  - Requires careful decision-making about component usage
  - Potential inconsistency in user experience
  - Still requires some TypeScript knowledge
  - Complexity in maintaining both approaches

### Chosen Alternative: Markdown-First with Minimal Component Usage
- **Pros**:
  - Maintains excellent searchability and accessibility
  - Simple content authoring and maintenance
  - Fast build times and reliable deployment
  - Full compliance with constitution requirements
  - Easy collaboration and content updates
  - Future-proof content format
- **Cons**:
  - Limited interactive features
  - No live code execution environments
  - Less visual enhancement for complex concepts
- **Selective Component Use**: Only use components where absolutely necessary (e.g., tabbed code examples, expandable sections)

## Decision
We will adopt a Markdown-first strategy with minimal TypeScript component usage, focusing on:

1. **Primary Content**: Pure Markdown/MDX for all core textbook content
2. **Code Examples**: Embedded in Markdown with language-specific syntax highlighting
3. **Navigation**: Standard Docusaurus features (sidebars, breadcrumbs, pagination)
4. **Limited Components**: Only essential components like tabbed code examples, expandable sections, and basic layout helpers
5. **Glossary Integration**: Cross-references and linking rather than interactive components
6. **Search Optimization**: All content remains searchable text

## Rationale
This decision best supports the project constitution's requirements:

1. **Academic Rigor**: Focuses on content quality over presentation complexity
2. **Maintainability**: Simple Markdown format ensures long-term content management
3. **Accessibility**: Pure text content ensures compliance with WCAG 2.1 AA standards
4. **Search Performance**: All content remains indexable by Docusaurus search
5. **Build Performance**: Fast builds under 5-minute requirement
6. **Constitution Compliance**: Aligns with "Content organized into 4 modules" requirement
7. **Simplicity**: Reduces cognitive load for both authors and students
8. **Reliability**: Minimal dependencies reduce failure points

The constitution's emphasis on "Academic audience with CS background" and "Flesch-Kincaid Grade 12-14" suggests that content quality and clarity are more important than interactive features.

## Consequences

### Positive Impacts
- **High Searchability**: All content indexed by Docusaurus search
- **Fast Build Times**: Minimal components ensure quick builds
- **Simple Maintenance**: Content authors only need Markdown knowledge
- **Full Accessibility**: Compliance with accessibility standards
- **Reliable Deployment**: Fewer dependencies to break over time
- **Content Focus**: Emphasis on technical content quality
- **Collaboration**: Easy for multiple authors to contribute

### Negative Impacts
- **Limited Interactivity**: No sophisticated learning aids or playgrounds
- **Basic Presentation**: Less visually engaging than component-heavy approach
- **Static Examples**: Code examples cannot be executed in-browser
- **Reduced Engagement**: May be less engaging than interactive alternatives

### Neutral Impacts
- **Technology Stack**: Still uses Docusaurus v3 as required
- **Deployment**: Still deploys to GitHub Pages
- **Performance**: May require additional optimization for large code examples
- **User Experience**: Different from modern interactive learning platforms

## Validation Criteria
- Build time remains under 5 minutes
- All content is searchable via Docusaurus search
- Accessibility compliance maintained (WCAG 2.1 AA)
- Content authors can easily contribute using Markdown
- No TypeScript knowledge required for content creation
- Search response time under 300ms maintained
- All code examples properly formatted and highlighted

## Related Documents
- Project Constitution: Section VI (Technology Stack), Section II (Quality Gates)
- spec.md: Technology Stack, Format Requirements
- plan.md: Technical Context, Component Breakdown