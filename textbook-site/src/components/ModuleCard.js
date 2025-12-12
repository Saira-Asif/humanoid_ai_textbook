import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './ModuleCard.module.css';

export default function ModuleCard({ module }) {
  return (
    <div className="col col--3 margin-bottom--lg">
      <div className={clsx('card', styles.moduleCard)}>
        <div className="card__header">
          <Heading as="h3">{module.title}</Heading>
        </div>
        <div className="card__body">
          <p>{module.description}</p>
          <div className="margin-top--sm">
            <span className="badge badge--secondary">Chapters: {module.chapters}</span>
          </div>
        </div>
        <div className="card__footer">
          <Link className={clsx('button button--' + module.color, 'button--block')} to={module.path}>
            Explore Module
          </Link>
        </div>
      </div>
    </div>
  );
}