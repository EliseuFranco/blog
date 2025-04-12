from db.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Author(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique  = True)
    email = db.Column(db.String(100), nullable = False)
    password_hash = db.Column(db.String(), nullable = True)

    def __repr__(self):
        return f"< Author {self.name}"
    
    @staticmethod
    def password(password):
        return generate_password_hash(password)
    
    @staticmethod
    def check_password(hash, password):
        return check_password_hash(hash, password)


