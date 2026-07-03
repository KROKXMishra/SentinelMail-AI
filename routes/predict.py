from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import markdown
from email import policy
from email.parser import BytesParser

from extensions import db
from models.prediction import Prediction

from services.ml.predictor import predict_message
from services.llm.groq_service import explain_message

predict_bp = Blueprint("predict", __name__)


@predict_bp.route("/predict", methods=["GET", "POST"])
@login_required
def predict():

    result = None
    explanation = None
    prediction_id = None
    message = ""

    if request.method == "POST":

        message = request.form.get("message", "").strip()

        uploaded_file = request.files.get("file")

        # ================= FILE UPLOAD ================= #

        if uploaded_file and uploaded_file.filename != "":

            filename = uploaded_file.filename.lower()

            if filename.endswith(".txt"):

                message = uploaded_file.read().decode(
                    "utf-8",
                    errors="ignore"
                )

            elif filename.endswith(".eml"):

                email_message = BytesParser(
                    policy=policy.default
                ).parse(uploaded_file)

                subject = email_message.get("Subject", "")

                body = ""

                if email_message.is_multipart():

                    for part in email_message.walk():

                        if part.get_content_type() == "text/plain":

                            body += part.get_content()

                else:

                    body = email_message.get_content()

                message = f"Subject: {subject}\n\n{body}"

        # ================================================= #

        if message:

            # ML Prediction
            result = predict_message(message)

            # AI Explanation
            try:

                explanation = explain_message(
                    message,
                    result["prediction"]
                )

                explanation = markdown.markdown(explanation)

            except Exception:

                explanation = markdown.markdown("""
## ⚠️ AI Explanation Unavailable

The spam detection model completed successfully.

However, the AI explanation service is currently unavailable.

Please try again later.
""")

            # Save only a preview to DB (prevents TEXT overflow)
            preview = message[:5000]

            prediction = Prediction(
                user_id=current_user.id,
                message=preview,
                prediction=result["prediction"],
                confidence=float(result["confidence"]),
                risk=result["risk"]
            )

            db.session.add(prediction)
            db.session.commit()

            prediction_id = prediction.id

    return render_template(
        "predict.html",
        result=result,
        explanation=explanation,
        prediction_id=prediction_id,
        message=message
    )