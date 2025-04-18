import secrets
import os


class AppConfig:
    SECRET_KEY = os.environ["flask_app_password"]#secrets.token_urlsafe(16)
    # SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db" 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    # "postgresql://uaoi0ubraqa42n:pf45cf0d4f4082adac30d86251a2252cc81a14bf8e13d041fcb7e520c4a821f1b@ca932070ke6bv1.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d2vtel0qjj66o9"#os.environ['DATABASE_URL'] #base de dados remota do heroku
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True  # Apenas se HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'