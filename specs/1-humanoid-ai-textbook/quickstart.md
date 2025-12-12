# Quickstart: Physical AI & Humanoid Robotics Textbook

## Overview

This quickstart guide provides instructions for setting up, running, and contributing to the Physical AI & Humanoid Robotics textbook project. The textbook is built using Docusaurus v3 and deployed to GitHub Pages, following the project constitution's technical requirements.

## Prerequisites

Before starting, ensure you have the following installed:

- **Node.js**: Version 18.0 or higher
- **npm**: Version 8.0 or higher (usually bundled with Node.js)
- **Git**: Version control system
- **Python 3.10+**: For code example validation
- **Git Bash** (Windows): For command-line operations

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-organization/humanoid-ai-textbook.git
cd humanoid-ai-textbook
```

### 2. Navigate to the Docusaurus Project

```bash
cd textbook-site
```

### 3. Install Dependencies

```bash
npm install
```

This command installs all necessary dependencies defined in `package.json`.

### 4. Start the Development Server

```bash
npm start
```

This command starts a local development server and opens the textbook in your default browser at `http://localhost:3000`. Most changes are reflected live without restarting the server.

## Project Structure

Understanding the key directories and files:

```
textbook-site/
├── docs/                    # All textbook content (Markdown/MDX)
│   ├── intro.md            # Course introduction (Weeks 1-2)
│   ├── module-1-ros2/      # Module 1: ROS 2 (Weeks 3-5)
│   ├── module-2-digital-twin/ # Module 2: Digital Twin (Weeks 6-7)
│   ├── module-3-isaac/     # Module 3: NVIDIA Isaac (Weeks 8-10)
│   ├── module-4-vla/       # Module 4: VLA (Weeks 11-13)
│   ├── appendices/         # Reference materials
│   └── references/         # Glossary and troubleshooting
├── src/                    # Custom React components
├── static/                 # Static assets (images, files)
├── docusaurus.config.js    # Main site configuration
├── sidebars.js            # Navigation sidebar configuration
└── package.json           # Project dependencies and scripts
```

## Creating New Content

### Adding a New Chapter

1. **Create the markdown file** in the appropriate module directory:

```bash
# Example: Adding a new chapter to Module 1
touch docs/module-1-ros2/new-chapter.mdx
```

2. **Add frontmatter metadata** following the constitution requirements:

```markdown
---
title: "Your Chapter Title"
description: "Brief description of chapter content"
estimated_time: 3
week: 4
module: "Module 1: ROS 2 Fundamentals"
prerequisites:
  - "module-1-ros2/chapter1"
learning_objectives:
  - "Objective 1"
  - "Objective 2"
  - "Objective 3"
sidebar_label: "Short Label"
---
```

3. **Add content** using Markdown/MDX syntax with embedded code examples:

```markdown
## Introduction

Your chapter content here...

### Code Examples

All code examples must include language specification:

import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

<Tabs>
<TabItem value="python" label="Python">
```python
# Python code example
def example_function():
    print("Hello, Humanoid AI!")
```
</TabItem>
<TabItem value="bash" label="Bash">
```bash
# Bash command example
ros2 run example_package example_node
```
</TabItem>
</Tabs>
```

4. **Update the sidebar** in `sidebars.js` to include your new chapter:

```javascript
module.exports = {
  textbook: [
    {
      type: 'category',
      label: 'Module 1: ROS 2 Fundamentals',
      items: [
        'module-1-ros2/chapter1',
        'module-1-ros2/chapter2',
        'module-1-ros2/new-chapter', // Add your chapter here
      ],
    },
  ],
};
```

## Configuration Files

### docusaurus.config.js

This file contains the main site configuration. Key settings include:

- **Site metadata**: title, tagline, URL
- **Theme configuration**: navbar, footer, prism syntax highlighting
- **Plugin configuration**: search, sitemap, Google Analytics
- **Deployment settings**: base URL, trailing slash

### sidebars.js

Defines the navigation structure with:
- Hierarchical organization by modules
- Collapsible categories
- Custom sidebar labels
- Navigation ordering

## Building for Production

To build the textbook for deployment:

```bash
npm run build
```

This command generates a static site in the `build/` directory that can be served by any static hosting service.

## Testing and Validation

### Local Build Test

Always test your changes with a production build before committing:

```bash
npm run build && npm run serve
```

This builds the site and serves it locally at `http://localhost:3000` to simulate production conditions.

### Content Quality Checks

Before submitting changes, ensure:

1. **Readability**: Flesch-Kincaid Grade 12-14
2. **Citations**: All claims properly cited in APA 7th edition
3. **Code examples**: Functional and properly formatted
4. **Links**: No broken internal or external links
5. **Images**: Optimized and include alt text

## Deployment

The textbook is automatically deployed to GitHub Pages when changes are merged to the `main` branch. The deployment process includes:

1. **Build validation**: Ensures `npm run build` succeeds
2. **Quality checks**: Validates content against constitution requirements
3. **Performance testing**: Verifies build time <5 minutes
4. **Deployment**: Publishes to GitHub Pages

### Manual Deployment (if needed)

```bash
GIT_USER=<Your GitHub username> \
  CURRENT_BRANCH=main \
  USE_SSH=true \
  npm run deploy
```

## Development Best Practices

### Content Creation

- **Frontmatter compliance**: Always include required metadata fields
- **Consistent formatting**: Follow the established style guide
- **Progressive disclosure**: Motivation → Example → Definition → Application
- **Cross-references**: Link to related content using `@site` paths

### Code Examples

- **Language specification**: Always include language tag for syntax highlighting
- **Purpose comments**: Explain what the code does
- **Expected output**: Show expected results where applicable
- **Troubleshooting notes**: Include common issues and solutions

### Writing Style

- **Active voice**: Maintain ≥70% active voice sentences
- **Technical accuracy**: Verify all technical claims against authoritative sources
- **Graduate-level readability**: Target Flesch-Kincaid Grade 12-14
- **APA citations**: Format all references according to APA 7th edition

## Troubleshooting

### Common Issues

**Problem**: Development server doesn't start
**Solution**: Clear npm cache and reinstall dependencies:
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
npm start
```

**Problem**: Build fails with errors
**Solution**: Check for syntax errors in Markdown files and verify all frontmatter is valid YAML

**Problem**: Images not loading
**Solution**: Ensure images are in the `static/img/` directory and use absolute paths

### Performance Optimization

- **Image optimization**: Keep images under 500KB
- **Code splitting**: Break large code examples into smaller chunks
- **Lazy loading**: Use Docusaurus' built-in lazy loading for large components

## Contributing

### Development Workflow

1. **Create a branch** for your changes
2. **Make your changes** following the constitution requirements
3. **Test locally** with `npm start` and `npm run build`
4. **Commit with clear messages** following conventional commits
5. **Submit a pull request** for review

### Quality Gates

All contributions must pass:
- ✅ Build validation (`npm run build` succeeds)
- ✅ Content quality (APA citations, readability metrics)
- ✅ Code example functionality
- ✅ Link validation (no broken links)
- ✅ Constitution compliance

## Getting Help

- **Documentation**: Refer to [Docusaurus documentation](https://docusaurus.io/docs)
- **Community**: Check the project's issue tracker for similar problems
- **Support**: Contact the project maintainers through the designated channels

This quickstart guide provides the essential information to begin working with the Physical AI & Humanoid Robotics textbook project. For more detailed information about specific aspects of development, refer to the detailed documentation in the `specs/` directory.