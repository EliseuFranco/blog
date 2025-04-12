from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):

    email = EmailField("E-mail", validators=[DataRequired()], render_kw={
        'placeholder': "Email"
    })

    password = PasswordField("Palavra-passe", validators=[DataRequired()],render_kw={
        'placeholder': "Palavra-passe"
    })

    submit = SubmitField("Iniciar sessão")