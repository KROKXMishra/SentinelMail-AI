from flask import Blueprint, send_file, abort
from flask_login import login_required, current_user

from models.prediction import Prediction
from services.pdf.pdf_generator import generate_pdf
from services.llm.groq_service import explain_message

report_bp = Blueprint("report", __name__)


@report_bp.route("/report/<int:prediction_id>")
@login_required
def report(prediction_id):

    prediction = Prediction.query.filter_by(
        id=prediction_id,
        user_id=current_user.id
    ).first()

    if prediction is None:

        abort(404)

    try:

        explanation = explain_message(
            prediction.message,
            prediction.prediction
        )

    except Exception:

        explanation = (
            "AI Security Analysis could not be generated "
            "at the time of report creation."
        )

    pdf_path = generate_pdf(
        prediction,
        explanation
    )

    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=f"SentinelMail_Report_{prediction.id}.pdf"
    )