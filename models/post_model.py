from db.db import db
from sqlalchemy.sql import func



class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    published_date = db.Column(db.DateTime, default = func.now())
    photo = db.Column(db.String(), nullable = True)
    
    author_id = db.Column(db.Integer, db.ForeignKey("author.id", ondelete="CASCADE"), nullable = False)
    author = db.relationship('Author', backref=db.backref('post', cascade="all, delete-orphan")) 
