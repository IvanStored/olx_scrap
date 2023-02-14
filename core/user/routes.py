from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import ValidationError

from core import db
from core.models import User
from core.user.forms import LoginForm, RegistrationForm

users = Blueprint("users", __name__, template_folder="templates")


@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit:
            hashed_password = generate_password_hash(form.password.data)

            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_password,
            )
            try:
                form.validate_email(form.email)
                form.validate_username(form.username)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("users.login"))
            except ValidationError as e:
                flash(str(e))

    return render_template("user/register.html", form=form)


@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit:
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                cph = check_password_hash(user.password, form.password.data)
                if cph:
                    login_user(user)
                    return redirect(url_for("main.index"))
                else:
                    flash("Wrong password!")
            else:
                flash("User not found!")

    return render_template("user/login.html", form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))
