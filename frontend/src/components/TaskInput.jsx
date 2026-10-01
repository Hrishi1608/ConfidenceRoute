import { useState } from "react";

export default function TaskInput({ onSubmit, isRunning }) {
  const [task, setTask] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task.trim() && !isRunning) {
      onSubmit(task);
    }
  };

  return (
    <div className="card">
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            type="text"
            className="input-field"
            value={task}
            onChange={(e) => setTask(e.target.value)}
            placeholder="Ask a complex question..."
            disabled={isRunning}
          />
          <button type="submit" className="btn" disabled={!task.trim() || isRunning}>
            {isRunning ? (
              <>
                <div className="spinner animate-spin"></div>
                Thinking...
              </>
            ) : (
              "Run Task"
            )}
          </button>
        </div>
      </form>
    </div>
  );
}
