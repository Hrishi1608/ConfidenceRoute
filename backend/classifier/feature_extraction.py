import re

HEDGE_WORDS = ["maybe", "possibly", "not sure", "i think", "perhaps"]

def extract_features(question: str, answer: str) -> dict:
    return {
        "length": len(answer.split()),
        "hedge_count": sum(w in answer.lower() for w in HEDGE_WORDS),
        "keyword_overlap": len(set(question.lower().split()) & set(answer.lower().split())),
        "num_count": len(re.findall(r"\d+", answer)),
        "sentence_count": answer.count(".")
    }
