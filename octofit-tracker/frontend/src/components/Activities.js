import React from 'react';

const Activities = () => {
  const [activities, setActivities] = React.useState([]);
  React.useEffect(() => {
    const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/` : '/api/activities/'}`;
    console.log('Fetching Activities from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched Activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, []);
  return (
    <div className="card mb-4">
      <div className="card-header bg-primary text-white">
        <h2 className="h4 mb-0">Activities</h2>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                {activities[0] && Object.keys(activities[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, idx) => (
                <tr key={activity.id || idx}>
                  {Object.values(activity).map((value, i) => (
                    <td key={i}>{String(value)}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {activities.length === 0 && <div className="alert alert-info">Nenhuma atividade encontrada.</div>}
        </div>
      </div>
    </div>
  );
};

export default Activities;
