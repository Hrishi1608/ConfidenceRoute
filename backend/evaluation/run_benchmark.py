import json
import os
from datasets import load_dataset
from backend.orchestrator.orchestrator import run_task
from backend.baseline.static_pipeline import run_static_task

def main():
    ds = load_dataset("hotpotqa/hotpot_qa", "distractor", split="validation[:20]")
    results = []
    
    # Ensure results directory exists
    os.makedirs("backend/evaluation/results", exist_ok=True)
    
    for row in ds:
        question, gold_answer = row["question"], row["answer"]
        log = []
        adaptive_answer = run_task(question, log)
        static_answer = run_static_task(question)
        
        results.append({
            "question": question,
            "gold": gold_answer,
            "adaptive_answer": adaptive_answer,
            "static_answer": static_answer,
            "adaptive_steps": len(log),
        })
        
    with open("backend/evaluation/results/benchmark_results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
