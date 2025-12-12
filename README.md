# Physical AI & Humanoid Robotics Textbook

An advanced textbook covering ROS 2, Digital Twins, NVIDIA Isaac, and Vision-Language-Action Models for humanoid robotics applications.

## Project Overview

This comprehensive textbook provides an in-depth exploration of Physical AI and humanoid robotics, structured across 4 modules with 14 chapters total. The content covers fundamental concepts through advanced applications in humanoid robot development.

### Modules Structure

1. **Module 1: ROS 2 Fundamentals** (5 chapters)
   - Nodes, Topics, Services
   - Python & rclpy
   - URDF for Humanoids
   - Advanced Topics
   - ROS 2 Integration

2. **Module 2: Digital Twin** (3 chapters)
   - Gazebo Simulation
   - Unity Integration
   - Sensor Simulation

3. **Module 3: NVIDIA Isaac** (3 chapters)
   - Isaac Sim
   - Isaac ROS & VSLAM
   - Nav2 Path Planning

4. **Module 4: Vision-Language-Action Models** (3 chapters)
   - Voice-to-Action (Whisper)
   - LLM Cognitive Planning
   - Capstone Project

## Local Setup Instructions

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn package manager
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd humanoid-ai-textbook
   ```

2. Navigate to the textbook site directory:
   ```bash
   cd textbook-site
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

### Running the Development Server

1. Start the development server:
   ```bash
   npm start
   ```

2. Open your browser to [http://localhost:3000](http://localhost:3000)

### Building for Production

To build the static site for deployment:

```bash
npm run build
```

The built files will be in the `build/` directory.

## Quality Standards

This textbook adheres to the following quality standards:

- **Readability**: Content targets Flesch-Kincaid Grade 12-14 reading level
- **Active Voice**: ≥70% of sentences written in active voice
- **Citations**: All factual claims include APA 7th edition citations
- **Peer Review**: ≥50% of sources are peer-reviewed academic papers
- **Code Quality**: All code examples follow best practices and include error handling
- **Accessibility**: All content meets WCAG 2.1 AA standards

## Contribution Guidelines

We welcome contributions to improve the textbook content. Please follow these guidelines:

### Content Contributions

1. Fork the repository and create a feature branch
2. Make your changes following the existing content structure
3. Ensure all new content includes proper citations
4. Test all code examples to ensure they work as described
5. Submit a pull request with a clear description of changes

### Technical Requirements

- All chapters must include learning objectives in the frontmatter
- Prerequisites must be clearly defined for each chapter
- Glossary terms must be referenced in chapter metadata
- Code examples should be tested and include error handling
- All images should be optimized and include appropriate alt text

### Writing Style

- Use active voice whenever possible
- Maintain consistent terminology throughout the textbook
- Include practical examples relevant to humanoid robotics
- Ensure all concepts are explained at the appropriate technical level

## Project Status

### Completed Modules
- ✅ Module 1: ROS 2 Fundamentals (5/5 chapters)
- ✅ Module 2: Digital Twin (3/3 chapters)
- ✅ Module 3: NVIDIA Isaac (3/3 chapters)
- ✅ Module 4: Vision-Language-Action Models (3/3 chapters)
- ✅ Appendices (4/4 sections)
- ✅ References (Glossary, Troubleshooting)

### Features Implemented
- ✅ Responsive Docusaurus-based textbook site
- ✅ Module dashboard with visual cards
- ✅ Search functionality with Algolia integration
- ✅ Breadcrumb navigation
- ✅ Mobile-optimized design
- ✅ Consistent styling across all pages
- ✅ GitHub Actions deployment workflow

### Deployment

The site is configured for deployment to GitHub Pages using the included GitHub Actions workflow. To deploy:

1. Push changes to the `main` branch
2. The workflow will automatically build and deploy to GitHub Pages
3. Site will be available at `https://<username>.github.io/humanoid-ai-textbook/`

## License

This textbook is licensed under [specify license] for educational and research purposes.

## Support

For questions or issues, please open an issue in the GitHub repository.