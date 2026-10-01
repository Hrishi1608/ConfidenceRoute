import { useState } from "react";

export default function TaskInput({ onSubmit }) {
  const [task, setTask] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task.trim()) {
      onSubmit(task);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="Enter your task here..."
        style={{ width: "300px", padding: "8px" }}
      />
      <button type="submit" style={{ padding: "8px 16px", marginLeft: "8px" }}>
        Run Task
      </button>
    </form>
  );
}
