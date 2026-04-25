import { useEffect, useState } from "react";

export default function Metrics() {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    fetch("http://localhost:8000/metrics")
      .then(res => res.json())
      .then(data => setMetrics(data));
  }, []);

  return (
    <div>
      <h2>Metrics</h2>
      <pre>{JSON.stringify(metrics, null, 2)}</pre>
    </div>
  );
}
