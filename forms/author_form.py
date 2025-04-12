from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class AuthorForm(FlaskForm):
    name = StringField("Nome completo", validators=[DataRequired()], render_kw={
        'placeholder': 'Nome completo'
    })
    email = EmailField("E-mail", validators=[DataRequired()], render_kw={
        'placeholder': "Email"
    })
    submit = SubmitField("Cadastrar")