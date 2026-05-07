import React from 'react';

const Teams = () => {
  const [teams, setTeams] = React.useState([]);
  React.useEffect(() => {
    const endpoint = `${process.env.REACT_APP_CODESPACE_NAME ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/` : '/api/teams/'}`;
    console.log('Fetching Teams from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched Teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, []);
  return (
    <div className="card mb-4">
      <div className="card-header bg-primary text-white">
        <h2 className="h4 mb-0">Teams</h2>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                {teams[0] && Object.keys(teams[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {teams.map((team, idx) => (
                <tr key={team.id || idx}>
                  {Object.values(team).map((value, i) => (
                    <td key={i}>{String(value)}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {teams.length === 0 && <div className="alert alert-info">Nenhuma equipe encontrada.</div>}
        </div>
      </div>
    </div>
  );
};

export default Teams;
