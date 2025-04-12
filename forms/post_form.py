from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    title = StringField("Título do post", validators=[DataRequired()], render_kw={
        'placeholder':"Título do post"
    })
    content = CKEditorField('Conteúdo do post', validators=[DataRequired()], render_kw={
        'placeholder':"Conteúdo do post"
    })
    image = FileField("Imagem do post")
    submit = SubmitField("Publicar")