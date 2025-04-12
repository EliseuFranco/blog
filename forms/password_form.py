from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class PasswordForm(FlaskForm):

    password = PasswordField("Palavra-passe", validators=[DataRequired(), Length(8,30), EqualTo("password_confirm", message="Palavra-passe precisa coincidir")], render_kw={
        'placeholder':"Palavra-passe"
    })

    password_confirm = PasswordField("Confirme a palavra passe", validators=[DataRequired()],render_kw={
        'placeholder': "Confirme a palavra-passe"
    })

    submit = SubmitField("Continuar")