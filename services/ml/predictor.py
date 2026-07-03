import pickle
from pathlib import Path

from services.ml.preprocess import transform_text

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open(BASE_DIR / "model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_message(message):

    transformed = transform_text(message)

    vector = vectorizer.transform([transformed])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    confidence = round(max(probability) * 100, 2)

    result = "Spam" if prediction == 1 else "Not Spam"

    if result == "Spam":

        if confidence >= 95:
            risk = "High"
        elif confidence >= 80:
            risk = "Medium"
        else:
            risk = "Low"

    else:

        if confidence >= 95:
            risk = "Very Safe"
        elif confidence >= 80:
            risk = "Safe"
        else:
            risk = "Uncertain"

    return {
        "prediction": result,
        "confidence": confidence,
        "risk": risk
    }