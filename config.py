import secrets
import os


class AppConfig:
    SECRET_KEY = os.environ["flask_app_password"]#secrets.token_urlsafe(16)
    # SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db" 
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] #base de dados remota do heroku
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True  # Apenas se HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'