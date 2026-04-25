import { useEffect, useState } from "react";

export default function AIControl() {
  const [decisions, setDecisions] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/ai-decisions")
      .then(res => res.json())
      .then(data => setDecisions(data));
  }, []);

  const approve = (id) => {
    fetch(`http://localhost:8000/approve/${id}`, { method: "POST" });
  };

  return (
    <div>
      <h1>AI Control Room</h1>

      {decisions.map(d => (
        <div key={d.id} style={{ border: "1px solid gray", margin: 10 }}>
          <p><b>Action:</b> {d.action}</p>
          <p><b>Reason:</b> {d.reason}</p>
          <button onClick={() => approve(d.id)}>Approve</button>
        </div>
      ))}
    </div>
  );
}
