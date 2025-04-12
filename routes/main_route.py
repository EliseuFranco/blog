from flask import Blueprint, render_template
from models.post_model import Post

main_bp = Blueprint('index',__name__)



@main_bp.route("/")
def index():
    posts = Post.query.all()

    return render_template("index.html", posts = posts)