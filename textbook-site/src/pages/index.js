import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import ModuleCard from '@site/src/components/ModuleCard';
import styles from './index.module.css';

// Module data
const modules = [
  {
    id: 1,
    title: 'Module 1: ROS 2 Fundamentals',
    description: 'Understanding the fundamental communication patterns in ROS 2 for humanoid robot control',
    chapters: 5,
    path: '/docs/module-1-ros2',
    color: 'primary'
  },
  {
    id: 2,
    title: 'Module 2: Digital Twin',
    description: 'Gazebo simulation and Unity integration for humanoid robot modeling',
    chapters: 3,
    path: '/docs/module-2-digital-twin',
    color: 'success'
  },
  {
    id: 3,
    title: 'Module 3: NVIDIA Isaac',
    description: 'Isaac Sim, Isaac ROS & VSLAM, and Nav2 Path Planning',
    chapters: 3,
    path: '/docs/module-3-isaac',
    color: 'info'
  },
  {
    id: 4,
    title: 'Module 4: Vision-Language-Action Models',
    description: 'Voice-to-Action, LLM Cognitive Planning, and Capstone Project',
    chapters: 3,
    path: '/docs/module-4-vla',
    color: 'warning'
  }
];

const quickLinks = [
  { title: 'Course Introduction', path: '/docs/intro', description: 'Start your journey with Physical AI & Humanoid Robotics' },
  { title: 'Glossary', path: '/docs/references/glossary', description: 'Comprehensive glossary of robotics and AI terms' },
  { title: 'Troubleshooting', path: '/docs/references/troubleshooting', description: 'Common issues and solutions' },
  { title: 'Appendices', path: '/docs/appendices', description: 'Supplementary materials and reference guides' }
];

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h2" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link className="button button--secondary button--lg" to="/docs/intro">
            Start Learning - Introduction
          </Link>
        </div>
      </div>
    </header>
  );
}

function QuickLinkCard({ link }) {
  return (
    <div className="col col--3 margin-bottom--lg">
      <div className={clsx('card', styles.quickLinkCard)}>
        <div className="card__body">
          <h3>{link.title}</h3>
          <p>{link.description}</p>
        </div>
        <div className="card__footer">
          <Link className="button button--outline button--primary button--block" to={link.path}>
            Go to {link.title}
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Physical AI & Humanoid Robotics Textbook`}
      description="An advanced textbook covering ROS 2, Digital Twins, NVIDIA Isaac, and Vision-Language-Action Models">
      <HomepageHeader />
      <main>
        <section className={styles.modulesSection}>
          <div className="container padding-vert--lg">
            <Heading as="h2" className={clsx('margin-bottom--lg', styles.sectionTitle)}>
              Course Modules
            </Heading>
            <div className="row">
              {modules.map((module) => (
                <ModuleCard key={module.id} module={module} />
              ))}
            </div>
          </div>
        </section>

        <section className={styles.quickLinksSection}>
          <div className="container padding-vert--lg">
            <Heading as="h2" className={clsx('margin-bottom--lg', styles.sectionTitle)}>
              Quick Links
            </Heading>
            <div className="row">
              {quickLinks.map((link, index) => (
                <QuickLinkCard key={index} link={link} />
              ))}
            </div>
          </div>
        </section>

        <section className={styles.courseOverviewSection}>
          <div className="container padding-vert--lg">
            <div className="row">
              <div className="col col--6">
                <Heading as="h2" className={styles.sectionTitle}>
                  About This Course
                </Heading>
                <p>
                  This comprehensive textbook covers the essential concepts of Physical AI and humanoid robotics,
                  designed for advanced students and practitioners. The course is structured over 14 chapters
                  across 4 modules, with a focus on practical implementation and theoretical understanding.
                </p>
                <p>
                  Each module builds upon the previous one, following a carefully designed prerequisite chain
                  to ensure a solid foundation before advancing to more complex topics.
                </p>
              </div>
              <div className="col col--6">
                <Heading as="h2" className={styles.sectionTitle}>
                  Learning Path
                </Heading>
                <ol>
                  <li>Start with the Introduction to understand course structure</li>
                  <li>Complete Module 1: ROS 2 Fundamentals (5 chapters)</li>
                  <li>Proceed to Module 2: Digital Twin (3 chapters)</li>
                  <li>Advance to Module 3: NVIDIA Isaac (3 chapters)</li>
                  <li>Finish with Module 4: Vision-Language-Action Models (3 chapters)</li>
                  <li>Review Appendices and Glossary for additional reference</li>
                </ol>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
