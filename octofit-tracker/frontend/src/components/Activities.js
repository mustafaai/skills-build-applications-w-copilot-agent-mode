import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [data, setData] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Activities API endpoint:', endpoint);
        console.log('Fetched activities data:', results);
      });
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-header bg-primary text-white">
        <h2 className="h4">Activities</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              {data[0] && Object.keys(data[0]).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((item, idx) => (
              <tr key={item.id || idx}>
                {Object.values(item).map((val, i) => (
                  <td key={i}>{val}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
