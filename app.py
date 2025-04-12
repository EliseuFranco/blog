from flask import Flask, render_template, request, url_for
from routes.main_route import main_bp
from routes.author_route import author_bp
from config import AppConfig
from db.db import db
from oauth_config import oauth
from extensions import login_manager, ck_editor, UPLOAD_FOLDER


app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object(AppConfig)


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

oauth.init_app(app)# Registrando o google oauth na aplicação
db.init_app(app) # Inicializa a base de dados

ck_editor.init_app(app) # Registar o ckeditor na aplicação

#Registando o administrador de sessão
login_manager.init_app(app)
login_manager.login_view = "user.login"

with app.app_context():
    db.create_all()



app.register_blueprint(main_bp, url_prefix="/") #Regista a rota principal na aplicação
app.register_blueprint(author_bp, url_prefix = "/user") #registo da rota de usuários


if __name__ == "__main__":
    app.run(debug=True)