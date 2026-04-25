import { useEffect, useState } from "react";

export default function App() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/services")
      .then(res => res.json())
      .then(data => setServices(data));
  }, []);

  return (
    <div>
      <h1>Global Command Center</h1>

      <h2>Services</h2>
      <ul>
        {services.map((s, i) => (
          <li key={i}>
            {s.name} — {s.status}
          </li>
        ))}
      </ul>
    </div>
  );
}
