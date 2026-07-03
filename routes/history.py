from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from extensions import db
from models.prediction import Prediction

history_bp = Blueprint("history", __name__)


@history_bp.route("/history")
@login_required
def history():

    predictions = Prediction.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Prediction.created_at.desc()
    ).all()

    return render_template(
        "history.html",
        predictions=predictions
    )


@history_bp.route("/history/delete", methods=["POST"])
@login_required
def delete_history():

    Prediction.query.filter_by(
        user_id=current_user.id
    ).delete()

    db.session.commit()

    return redirect(
        url_for("history.history")
    )


@history_bp.route("/history/delete/<int:id>", methods=["POST"])
@login_required
def delete_single(id):

    prediction = Prediction.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first()

    if prediction:

        db.session.delete(prediction)

        db.session.commit()

    return redirect(
        url_for("history.history")
    )