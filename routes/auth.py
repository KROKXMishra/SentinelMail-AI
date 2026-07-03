from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from extensions import db, bcrypt
from models.user import User
from forms.auth_forms import RegisterForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(username=username).first():

            flash("Username already exists.", "danger")

            return redirect(
                url_for("auth.register")
            )

        if User.query.filter_by(email=email).first():

            flash("Email already exists.", "danger")

            return redirect(
                url_for("auth.register")
            )

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration Successful!",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html",
        form=form
    )


@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            flash(
                "Welcome Back!",
                "success"
            )

            return redirect(
                url_for("dashboard.dashboard")
            )

        flash(
            "Invalid Email or Password",
            "danger"
        )

    return render_template(
        "login.html",
        form=form
    )


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged Out Successfully",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )