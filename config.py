import secrets
import os


class AppConfig:
    SECRET_KEY = os.environ["flask_app_password"]#secrets.token_urlsafe(16)
    # SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db" 
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #os.environ['DATABASE_URL'] #os.environ.get('ps_data_base_url') # base de dados remota do heroku
    SQLALCHEMY_TRACK_MODIFICATIONS = False

