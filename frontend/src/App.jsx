import { useState } from "react";
import TaskInput from "./components/TaskInput";
import AgentGraph from "./components/AgentGraph";

export default function App() {
  const [steps, setSteps] = useState([]);
  const [finalAnswer, setFinalAnswer] = useState("");

  const runTask = (task) => {
    setSteps([]);
    setFinalAnswer("");
    const ws = new WebSocket("ws://localhost:8000/ws/run-task");
    
    ws.onopen = () => {
      ws.send(JSON.stringify({ task }));
    };
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.final_answer) {
        setFinalAnswer(data.final_answer);
      } else {
        setSteps((prev) => [...prev, data]);
      }
    };
    
    ws.onerror = (error) => {
      console.error("WebSocket Error: ", error);
    };
  };

  return (
    <div style={{ maxWidth: "800px", margin: "0 auto", padding: "20px", fontFamily: "sans-serif" }}>
      <h1>ConfidenceRoute Dashboard</h1>
      <TaskInput onSubmit={runTask} />
      <AgentGraph steps={steps} />
      {finalAnswer && (
        <div style={{ padding: "20px", backgroundColor: "#e6ffe6", border: "1px solid #b3ffb3", borderRadius: "8px" }}>
          <h3>Final Answer</h3>
          <p>{finalAnswer}</p>
        </div>
      )}
    </div>
  );
}
