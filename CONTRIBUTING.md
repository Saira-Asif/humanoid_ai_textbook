# Contributing to Physical AI & Humanoid Robotics Textbook

Thank you for your interest in contributing to the Physical AI & Humanoid Robotics Textbook! This document outlines the guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Content Guidelines](#content-guidelines)
- [Technical Guidelines](#technical-guidelines)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)

## Code of Conduct

Please read and follow our Code of Conduct to ensure a welcoming and inclusive environment for all contributors.

## How to Contribute

### Reporting Issues

- Use the issue tracker to report bugs or suggest enhancements
- Search existing issues before creating a new one
- Provide detailed information about the problem or suggestion
- Include steps to reproduce bugs when possible

### Content Contributions

1. Fork the repository
2. Create a feature branch for your changes
3. Make your changes following the content guidelines
4. Submit a pull request with a clear description

### Documentation Improvements

- Fix typos and grammatical errors
- Improve clarity and readability
- Add missing explanations or examples
- Update outdated information

## Content Guidelines

### Writing Standards

- Maintain Flesch-Kincaid Grade 12-14 reading level
- Use active voice in ≥70% of sentences
- Include proper APA 7th edition citations for all claims
- Ensure content accuracy with peer-reviewed sources
- Follow the established chapter structure and frontmatter

### Chapter Structure

Each chapter should include:
- Title and description in frontmatter
- Prerequisites from previous chapters
- Learning objectives (3-5 specific outcomes)
- Content with proper headings and formatting
- Code examples with explanations
- References and citations
- Glossary term references

### Technical Accuracy

- Verify all code examples work as described
- Include error handling in example code
- Use consistent terminology throughout
- Follow ROS 2, Isaac, and other platform best practices
- Test all commands and procedures

## Technical Guidelines

### File Structure

- Chapters are in `textbook-site/docs/module-{number}-{name}/`
- Use `.mdx` extension for chapters with React components
- Use `.md` extension for standard markdown files
- Images go in `textbook-site/static/img/`
- Custom components go in `textbook-site/src/components/`

### Frontmatter Requirements

All content files must include proper frontmatter:

```yaml
---
title: "Chapter Title"
description: "Brief description of the chapter content"
estimated_time: 6  # hours to complete
week: 3  # week number in course sequence
module: "Module 1: ROS 2 Fundamentals"
prerequisites:
  - "intro"
  - "module-1-ros2/index"
learning_objectives:
  - "Specific learning objective"
  - "Another learning objective"
sidebar_label: "Sidebar display text"
difficulty: "Beginner|Intermediate|Advanced"
tags:
  - "tag1"
  - "tag2"
glossary_terms:
  - "term1"
  - "term2"
related_chapters:
  - "module-1-ros2/chapter2"
---
```

### Code Examples

- Use proper syntax highlighting
- Include comments explaining complex concepts
- Test all examples before submission
- Follow language-specific style guides (PEP 8 for Python, etc.)
- Include error handling where appropriate

## Pull Request Process

1. Ensure your changes address a specific issue or need
2. Follow the style guide and technical requirements
3. Update any related documentation
4. Submit your pull request with a clear description
5. Wait for review and address feedback
6. Your PR will be merged once approved

### PR Description Template

When submitting a pull request, please include:

- Summary of changes made
- Issue(s) addressed (if applicable)
- Testing performed
- Screenshots (if UI changes)
- Breaking changes (if any)

## Style Guide

### Writing Style

- Use clear, concise language
- Define technical terms when first introduced
- Use consistent terminology throughout
- Write in second person ("you" instead of "the user")
- Use active voice wherever possible

### Formatting

- Use proper heading hierarchy (H1, H2, H3, etc.)
- Include alt text for all images
- Use proper code block formatting with language specification
- Follow the existing document structure
- Use bullet points and numbered lists appropriately

### Technical Writing

- Explain concepts before providing examples
- Use practical examples relevant to humanoid robotics
- Include both theory and implementation details
- Provide context for why certain approaches are used
- Link to external documentation when appropriate

## Quality Standards

All contributions must meet these quality standards:

- **Readability**: Flesch-Kincaid Grade 12-14
- **Active Voice**: ≥70% of sentences
- **Citations**: All claims supported by sources
- **Code Quality**: All examples tested and functional
- **Accessibility**: Alt text for images, proper heading structure
- **Completeness**: All required frontmatter fields included

## Getting Help

- Check the existing documentation
- Search previous issues for similar questions
- Contact maintainers if you need clarification
- Join our community discussions if available

## Recognition

Contributors will be recognized in the project documentation and release notes. Significant contributions may be acknowledged in academic publications related to the textbook.

Thank you for contributing to the Physical AI & Humanoid Robotics Textbook!