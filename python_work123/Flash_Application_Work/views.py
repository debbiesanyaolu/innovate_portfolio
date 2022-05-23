from flask import render_template,redirect, Blueprint

# from app import app

my_view = Blueprint('my_veiw', __name__)



@my_view.route("/")
def home():
    return "<h1>Hello World<h1>"
