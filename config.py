import secrets
import os


class AppConfig:
    SECRET_KEY = os.environ["flask_app_password"]#secrets.token_urlsafe(16)
    #SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db" base de dados sqlite
    SQLALCHEMY_DATABASE_URI = "postgres://u7omos7cumhn0f:p6c45ea2609f481ddd29706453dc545580d6bd83e07246478918497b12d723613@c952v5ogavqpah.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d49o5ats6jrrqh" # base de dados remota do heroku

    SQLALCHEMY_TRACK_MODIFICATIONS = False

