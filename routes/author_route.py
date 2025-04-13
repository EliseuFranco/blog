from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from forms.author_form import AuthorForm
from forms.password_form import PasswordForm
from forms.login_form import LoginForm
from models.user_model import Author
from models.post_model import Post
from db.db import db
from oauth_config import OauthConfig
from flask_login import login_user, logout_user, current_user, login_required
from extensions import login_manager
from forms.post_form import PostForm
from flask_ckeditor.utils import cleanify
from werkzeug.utils import secure_filename
import uuid as uuid
import os
from utils import check_file


author_bp = Blueprint("user", __name__)


#REGISTO DE USUÁRIO COM GOOGLE

@author_bp.route("/OauthRegister")
def OauthRegister():
    return OauthConfig.google.authorize_redirect(url_for("user.google_callback", _external=True))

#LOGIN COM GOOGLE
@author_bp.route("/OauthLogin")
def OauthLogin():
    return OauthConfig.google.authorize_redirect(url_for("user.google_callback", _external=True))


#Capturar o id do user na sessão

@login_manager.user_loader
def load_user(user_id):
    return Author.query.get(int(user_id))


#GOOGLE CALLBACK
@author_bp.route("/google_callback")
def google_callback():
    token = OauthConfig.google.authorize_access_token()

    if not token:
        flash("Não foi possível a autenticação com o google", "danger")
        return redirect(url_for("index.index"))
    try:
        user_info = OauthConfig.google.parse_id_token(token, None)
        author = Author.query.filter_by(email = user_info['email']).first()

        if not author:
            author = Author(
                name = user_info['name'],
                email = user_info['email']
            )
            db.session.add(author)
            db.session.commit()
           
        login_user(author)
        return redirect(url_for("user.dashboard"))
    
    except Exception as e:
        flash("Houve um erro ao recuperar dados da google", "danger")

    return redirect(url_for("user.dashboard"))
    

#Rota para registo de autor
@author_bp.route("/register", methods=["GET",'POST'])
def register():
    form = AuthorForm()

    if form.errors:
        for error in form.errors:
            print(error)
    if form.validate_on_submit():
       
        author = Author.query.filter_by(email = form.email.data).first()
        if not author:
            session['author_name'] = form.name.data
            session['author_email'] = form.email.data
            return redirect(url_for("user.create_password"))
        flash("User already registered, go to login", "warning")
        
    return render_template("register.html", form = form)


#Rota para a criação da palavra-passe
@author_bp.route("/create_password", methods=["GET","POST"])
def create_password():
    form = PasswordForm()

    if form.validate_on_submit():
        new_author = Author(
            name = session.get('author_name'),
            email = session.get('author_email'),
            password_hash = Author.password(form.password.data)
        )
        db.session.add(new_author)
        db.session.commit()
        login_user(new_author)
        return redirect(url_for("user.dashboard"))

    return render_template("create_password.html", form = form)


#Rota para a página de login
@author_bp.route("/login", methods = ["GET",'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        author = Author.query.filter_by(email = form.email.data).first()
        
        if author and Author.check_password(author.password_hash, form.password.data):
            login_user(author)
            return redirect(url_for("user.dashboard"))
        flash("Utilizador inexistente, tente novamente ou faça cadastro", "danger")
    return render_template("login.html", form = form)

#Rota de logout
@author_bp.route("/logout")
def logout():
    logout_user()
    flash("You where logged out")
    return redirect(url_for("user.login"))

@author_bp.route("/dashboard", methods=["GET","POST"])
@login_required
def dashboard():
    from extensions import UPLOAD_FOLDER
    
    form = PostForm()
    user_posts = Post.query.filter_by(author_id=current_user.id).all()

    filename = None  # Definir o filename antes de usá-lo

    if form.validate_on_submit():

        if form.image.data and not check_file(form.image.data.filename):
            flash("O ficheiro de imagem não é válido", "danger")
            return redirect(url_for("user.dashboard"))
        
        file = form.image.data

        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
       
        new_post = Post(
            title=form.title.data,
            content=cleanify(form.content.data),
            author_id=current_user.id,
            photo=filename
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Post created successfully", "success")  # Corrigido erro de digitação
        return redirect(url_for("user.dashboard"))

    return render_template("dashboard.html", form=form, posts=user_posts)
@author_bp.route("delete_post/<int:id>", methods=['POST'])
def delete_post(id):
    post_to_delete = Post.query.get_or_404(id)
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash("Post deletected, successfully", "success")
        return redirect(url_for("user.dashboard"))
    except Exception:
        flash("Houve um erro ao eliminar o post", "warning")
        return redirect(url_for("user.dashboard"))

