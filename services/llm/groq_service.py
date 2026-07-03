import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def explain_message(message, prediction):

    prompt = f"""
You are SentinelMail AI's explanation engine.

Your job is NOT to classify the message again.

The machine learning model has already made the final decision.

ML Prediction: {prediction}

Message:
{message}

Your task is ONLY to explain WHY the machine learning model may have produced this prediction.

IMPORTANT:
- Never contradict the ML prediction.
- If ML Prediction is "Not Spam", explain why it is likely legitimate, even if there are minor suspicious-looking words.
- If ML Prediction is "Spam", explain why it is suspicious.
- Your explanation MUST always be consistent with the ML prediction.

Return your answer in Markdown:

## 📌 Why Classified

...

## 🚨 Indicators

- ...
- ...

## ✅ Recommendation

- ...
- ...
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content