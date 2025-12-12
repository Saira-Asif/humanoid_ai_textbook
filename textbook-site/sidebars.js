// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the docs folder structure, or explicitly defined here.

 Create as many sidebars as you want.

 @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  textbookSidebar: [
    {
      type: 'category',
      label: 'Introduction',
      items: ['intro'],
      link: {
        type: 'doc',
        id: 'intro',
      },
    },
    {
      type: 'category',
      label: 'Module 1: ROS 2 Fundamentals',
      collapsed: false,
      items: [
        'module-1-ros2/index',
        'module-1-ros2/chapter1',
        'module-1-ros2/chapter2',
        'module-1-ros2/chapter3',
        'module-1-ros2/chapter4',
        'module-1-ros2/chapter5',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin',
      collapsed: false,
      items: [
        'module-2-digital-twin/index',
        'module-2-digital-twin/chapter1',
        'module-2-digital-twin/chapter2',
        'module-2-digital-twin/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: NVIDIA Isaac',
      collapsed: false,
      items: [
        'module-3-isaac/index',
        'module-3-isaac/chapter1',
        'module-3-isaac/chapter2',
        'module-3-isaac/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action Models',
      collapsed: false,
      items: [
        'module-4-vla/index',
        'module-4-vla/chapter1',
        'module-4-vla/chapter2',
        'module-4-vla/chapter3',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      collapsed: true,
      items: [
        'appendices/appendix-a',
        'appendices/appendix-b',
        'appendices/appendix-c',
        'appendices/appendix-d',
      ],
    },
    {
      type: 'category',
      label: 'References',
      collapsed: true,
      items: [
        'references/glossary',
        'references/troubleshooting',
      ],
    },
  ],
};

export default sidebars;