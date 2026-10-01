from backend.react.react_agent import ReActAgent

def run_static_task(task: str) -> str:
    # Always one pass, always the same model, no retries/escalation
    agent = ReActAgent()
    result = agent.run_task(task)
    return result["answer"]
