import { useState } from "react";
import TaskInput from "./components/TaskInput";
import AgentGraph from "./components/AgentGraph";

export default function App() {
  const [steps, setSteps] = useState([]);
  const [finalAnswer, setFinalAnswer] = useState("");
  const [isRunning, setIsRunning] = useState(false);

  const runTask = (task) => {
    setSteps([]);
    setFinalAnswer("");
    setIsRunning(true);
    const ws = new WebSocket("ws://localhost:8000/ws/run-task");
    
    ws.onopen = () => {
      ws.send(JSON.stringify({ task }));
    };
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.final_answer) {
        setFinalAnswer(data.final_answer);
        setIsRunning(false);
      } else {
        setSteps((prev) => [...prev, data]);
      }
    };
    
    ws.onerror = (error) => {
      console.error("WebSocket Error: ", error);
      setIsRunning(false);
    };
    
    ws.onclose = () => {
      setIsRunning(false);
    };
  };

  return (
    <div className="app-container">
      <h1 className="title animate-slide-up">ConfidenceRoute</h1>
      <p className="subtitle animate-slide-up stagger-1">
        Adaptive Multi-Agent Orchestration
      </p>
      
      <div className="animate-slide-up stagger-2">
        <TaskInput onSubmit={runTask} isRunning={isRunning} />
      </div>

      <div className="animate-slide-up stagger-3">
        <AgentGraph steps={steps} isRunning={isRunning} />
      </div>

      {finalAnswer && (
        <div className="final-answer animate-slide-up">
          <h3>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            Final Answer
          </h3>
          <p>{finalAnswer}</p>
        </div>
      )}
    </div>
  );
}
