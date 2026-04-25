import { useEffect, useState } from "react";

export default function Logs() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/logs")
      .then(res => res.json())
      .then(data => setLogs(data));
  }, []);

  return (
    <div>
      <h1>Observability Skyline</h1>

      <h2>Logs</h2>
      {logs.map((log, i) => (
        <div key={i}>
          [{log.level}] {log.message}
        </div>
      ))}
    </div>
  );
}
