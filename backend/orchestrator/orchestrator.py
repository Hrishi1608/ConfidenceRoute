import joblib
from backend.classifier.feature_extraction import extract_features
from backend.react.react_agent import ReActAgent
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "classifier", "model.pkl")

CLASSIFIER = joblib.load(MODEL_PATH)

CONFIDENCE_THRESHOLD_LOW = 0.4
CONFIDENCE_THRESHOLD_RETRY_LIMIT = 2

def score_confidence(question: str, answer: str) -> float:
    features = extract_features(question, answer)
    X = pd.DataFrame([features])
    return CLASSIFIER.predict_proba(X)[0][1]  # probability of "good"

def run_task(task: str, log: list) -> str:
    retries = 0
    agent = ReActAgent()
    result = agent.run_task(task)
    answer = result["answer"]
    confidence = score_confidence(task, answer)
    
    log.append({"step": "initial", "confidence": confidence, "model": "llama3:8b"})
    
    while confidence < CONFIDENCE_THRESHOLD_LOW and retries < CONFIDENCE_THRESHOLD_RETRY_LIMIT:
        retries += 1
        if retries == 1:
            agent = ReActAgent()
            result = agent.run_task(task)
            answer = result["answer"]
            model_used = "llama3:8b (retry)"
        else:
            escalated_agent = ReActAgent(model="mixtral-groq")
            result = escalated_agent.run_task(task)
            answer = result["answer"]
            model_used = "groq-mixtral (escalated)"
            
        confidence = score_confidence(task, answer)
        log.append({"step": f"retry_{retries}", "confidence": confidence, "model": model_used})
        
    import re
    if re.search(r"\d+", answer):
        from backend.agents.verifier import VerifierAgent
        verifier = VerifierAgent()
        verification = verifier.verify(answer)
        log.append({"step": "dynamic_verifier_inserted", "verification": verification, "model": "llama3:8b"})
        # We can append verification to the answer or just let the log capture it
        answer += f"\n\n[Auto-Verification Added]: {verification}"
        
    return answer

if __name__ == "__main__":
    log = []
    task = "What is the capital of Australia and its population?"
    print(f"Task: {task}")
    final_answer = run_task(task, log)
    print(f"Final Answer: {final_answer}")
    print(f"Log: {log}")
