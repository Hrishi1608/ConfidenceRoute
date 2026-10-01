export default function AgentGraph({ steps }) {
  return (
    <div style={{ padding: "20px", border: "1px solid #ccc", borderRadius: "8px", minHeight: "200px", marginBottom: "20px" }}>
      <h3>Live Agent Graph</h3>
      {steps.length === 0 ? (
        <p>No steps yet...</p>
      ) : (
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {steps.map((step, index) => (
            <li key={index} style={{ marginBottom: "10px", padding: "10px", backgroundColor: "#f9f9f9", borderRadius: "4px" }}>
              <strong>Step:</strong> {step.step} <br />
              <strong>Model:</strong> {step.model} <br />
              <strong>Confidence:</strong> {step.confidence !== undefined ? step.confidence.toFixed(2) : "N/A"}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
