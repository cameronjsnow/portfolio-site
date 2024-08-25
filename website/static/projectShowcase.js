const ProjectCard = ({ title, description, technologies, link }) => (
    <div className="card mb-3">
      <div className="card-body">
        <h5 className="card-title">{title}</h5>
        <p className="card-text">{description}</p>
        <p className="card-text"><small className="text-muted">Technologies: {technologies.join(', ')}</small></p>
        <a href={link} className="btn btn-primary" target="_blank" rel="noopener noreferrer">View Project</a>
      </div>
    </div>
  );
  
  const ProjectShowcase = ({ projects }) => (
    <div>
      {projects.map((project, index) => (
        <ProjectCard key={index} {...project} />
      ))}
    </div>
  );
  
  // Render the component
  ReactDOM.render(
    <ProjectShowcase projects={JSON.parse(document.getElementById('project-data').textContent)} />,
    document.getElementById('project-showcase')
  );