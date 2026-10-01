import pandas as pd
from datasets import load_dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
import joblib

from feature_extraction import extract_features

def load_halueval():
    ds = load_dataset("pminervini/HaluEval", "qa")
    rows = []
    for row in ds["data"]:
        rows.append({"q": row["question"], "a": row["right_answer"], "label": 1})
        rows.append({"q": row["question"], "a": row["hallucinated_answer"], "label": 0})
    return pd.DataFrame(rows)

def main():
    df = load_halueval()
    features = df.apply(lambda r: extract_features(r["q"], r["a"]), axis=1)
    X = pd.DataFrame(list(features))
    y = df["label"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, preds))
    print("F1:", f1_score(y_test, preds))
    print(classification_report(y_test, preds))
    
    joblib.dump(model, "model.pkl")

if __name__ == "__main__":
    main()
