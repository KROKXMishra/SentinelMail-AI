from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import func
from datetime import date

from models.prediction import Prediction
from extensions import db

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    )

    total = predictions.count()

    spam = predictions.filter_by(
        prediction="Spam"
    ).count()

    safe = predictions.filter_by(
        prediction="Not Spam"
    ).count()

    avg_confidence = db.session.query(
        func.avg(Prediction.confidence)
    ).filter_by(
        user_id=current_user.id
    ).scalar()

    avg_confidence = round(avg_confidence, 2) if avg_confidence else 0

    today = date.today()

    today_scans = predictions.filter(
        func.date(Prediction.created_at) == today
    ).count()

    last_prediction = predictions.order_by(
        Prediction.created_at.desc()
    ).first()

    last_scan_time = last_prediction.created_at if last_prediction else None

    recent = predictions.order_by(
        Prediction.created_at.desc()
    ).limit(5).all()

    return render_template(
        "dashboard.html",
        user=current_user,
        total=total,
        spam=spam,
        safe=safe,
        avg_confidence=avg_confidence,
        today_scans=today_scans,
        last_scan_time=last_scan_time,
        recent=recent
    )