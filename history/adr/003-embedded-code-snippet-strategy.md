# ADR 003: Embedded Code Snippet Strategy (No External Code Directory)

## Status
Accepted

## Date
2025-12-11

## Context
The Physical AI & Humanoid Robotics textbook requires a code example management strategy that supports the constitution's requirements for embedded code examples, reproducibility, and content integration. The project constitution mandates that "All code examples embedded in chapter markdown" and "Every factual claim must be traceable to a verifiable source." The decision affects content maintainability, build complexity, learning continuity, and the implementation workflow for /sp.implement.

## Problem Statement
Should code examples be stored in a separate `/code_examples` directory and referenced from chapters, or should they be embedded directly within the Markdown content? This decision impacts content cohesion, maintenance complexity, learning flow, and the ease of implementation for the automated content generation process.

## Alternatives Considered

### Alternative 1: External Code Directory Approach (`/code_examples`)
- **Pros**:
  - Code can be tested independently from documentation
  - Reusable code snippets across multiple chapters
  - Separate version control for code vs content
  - Easier to maintain complex code examples
  - Better integration with IDEs and testing frameworks
- **Cons**:
  - Breaks content-flow during learning (students must navigate between docs and code)
  - Increases project complexity with multiple directories
  - More complex implementation for /sp.implement automation
  - Risk of code-content desynchronization
  - Additional maintenance overhead for cross-references
  - Students may miss code context without surrounding explanation

### Alternative 2: Embedded Code Snippets in Markdown
- **Pros**:
  - Seamless learning experience (code with explanation context)
  - Single-source content (no directory switching)
  - Simplified implementation for /sp.implement
  - Easier to maintain code-content synchronization
  - Better for step-by-step tutorials
  - Reduced cognitive load for students
- **Cons**:
  - Code harder to test independently
  - Potential duplication of common snippets
  - Larger Markdown files
  - May not work well for very large code examples

### Alternative 3: Hybrid Approach (Embedded Primary, External Reference)
- **Pros**:
  - Best of both worlds - embedded context with external testing
  - Can reference external files when appropriate
  - Maintains learning flow while enabling testing
- **Cons**:
  - Increased complexity in implementation
  - Risk of synchronization issues
  - More complex for /sp.implement automation
  - Potential confusion about which approach to use when

### Chosen Alternative: Embedded Code Snippets in Markdown
- **Pros**:
  - Maintains seamless learning experience
  - Simplifies /sp.implement workflow significantly
  - Ensures code is always in proper educational context
  - Reduces project complexity and cognitive load
  - Aligns with constitution requirement for embedded examples
  - Easier for students to follow along
  - Better integration with Docusaurus features
- **Cons**:
  - Code harder to test in isolation
  - Potential for duplication
  - Larger content files
- **Mitigation Strategy**: Use Docusaurus code inclusion features where appropriate for common patterns

## Decision
We will embed all code examples directly within the Markdown/MDX content files, following these principles:

1. **Embedded Context**: All code examples appear within the educational context where they're discussed
2. **Self-Contained**: Each code example includes necessary explanations, expected output, and troubleshooting notes
3. **Language Tagging**: All code blocks include proper language tags for syntax highlighting
4. **Purpose Comments**: Each example includes comments explaining its purpose and functionality
5. **Testing Integration**: Code examples are validated as part of the content development workflow
6. **No External References**: Avoid creating a separate `/code_examples` directory

## Rationale
This decision best supports the project constitution's requirements:

1. **Constitution Alignment**: "All code examples embedded in chapter markdown" (Section 5, Constitution)
2. **Learning Continuity**: Students can read and understand code in proper educational context
3. **Implementation Simplicity**: Significantly reduces complexity for /sp.implement automation
4. **Content Cohesion**: Code and explanation remain tightly coupled
5. **Academic Clarity**: Supports "Clarity for academic audience" requirement
6. **Reproducibility**: Code examples are directly available within their explanation context
7. **Quality Assurance**: Easier to validate code functionality within content context

The embedded approach supports the constitution's emphasis on "Reproducibility" and "Academic audience with CS background" by ensuring code examples are always presented in their proper educational context.

## Consequences

### Positive Impacts
- **Learning Flow**: Students don't need to navigate between content and code directories
- **Implementation Simplicity**: /sp.implement can generate complete chapters with embedded code
- **Content Synchronization**: Code and explanation always remain in sync
- **Educational Context**: Code examples are presented with proper surrounding explanation
- **Reduced Complexity**: No need to manage separate code and content repositories
- **Maintainability**: Updates to code automatically update within educational context
- **Accessibility**: All code is searchable and accessible within content

### Negative Impacts
- **Testing Complexity**: Code examples harder to test independently
- **Potential Duplication**: Common code patterns may be repeated across chapters
- **Larger Files**: Markdown files become larger with embedded code
- **Version Control**: Changes to code appear as content changes
- **Isolation**: Cannot easily extract code for separate execution environments

### Neutral Impacts
- **Build Process**: Docusaurus handles embedded code normally
- **Search**: Code remains searchable within content
- **Accessibility**: Code examples remain accessible with proper markup
- **Performance**: May require optimization for large code blocks

## Validation Criteria
- All code examples appear within their educational context in Markdown files
- No separate `/code_examples` directory exists
- Code examples include purpose comments and expected output
- /sp.implement can generate complete chapters with embedded code
- Code functionality validated as part of content quality checks
- Students can follow along without navigating between directories
- All code blocks have proper syntax highlighting language tags

## Related Documents
- Project Constitution: Section V (Technical Constraints), Section 3 (Reproducibility)
- spec.md: Code Standards, Format Requirements
- plan.md: Implementation Phases, Component Breakdown