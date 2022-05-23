from flask import render_template, redirect, Blueprint, request

from favourites import fave_bands, add_to_list, del_from_list           #imported a local object from a local file

my_view = Blueprint('my_view', __name__)

# @my_view.route("/")
# def home():
#     return "<h1>Hello World</h1>"


@my_view.route("/")                             
def home():
    return render_template("index.html")

@my_view.route("/Page 1")                           # When the url is our_app/page1
def page1():
    return render_template("page1.html")

@my_view.route("/page2")                            # When the url is our_app/page2    
def page2():
    return render_template("page2.html")

@my_view.route("/page3")                            # When the url is our_app/page3
def page3():
    return render_template("page3.html")

@my_view.route("/page4")                            # When the url is our_app/page4
def page4():
    return render_template("page4.html")

@my_view.route("/page5")                            # When the url is our_app/page5
def page5():
    return render_template("page5.html")

@my_view.route("/admin")                            # When the url is our_app/admin
def admin():
    return render_template("admin.html")

# @my_view.route("/404")
# def 404():
#     return render_template("404.html", e=e)










# @my_view.route("/about", methods=["GET", "POST"])
# def about():
#     if request.method == "POST":
#         #Another bit of logic to determine add from remove
#         if not new_band:
#             old_band = request.form["band.entry"]
#             del_from_list(old_band)
#         new_band = request.form["add_band"]
#         add_to_list(new_band)
#         #Then I need to pass that input back to my favourite files
#     return render_template("about.html", bands=fave_bands)