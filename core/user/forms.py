from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    EmailField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError,
)
from core.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=20)]
    )
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Done")

    @staticmethod
    def validate_username(username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "That username is taken. Please choose a different one"
            )

    @staticmethod
    def validate_email(email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "That email is taken. Please choose a different one"
            )


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
