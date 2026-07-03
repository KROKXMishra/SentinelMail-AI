from flask import Flask, render_template

from config import Config
from extensions import db, bcrypt, login_manager

from routes.auth import auth
from routes.dashboard import dashboard_bp
from routes.report import report_bp
from models import *
from routes.history import history_bp
from routes.predict import predict_bp

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(report_bp)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(history_bp)
    @app.route("/")
    def home():
        return render_template("index.html")

    with app.app_context():
        db.create_all()

    return app