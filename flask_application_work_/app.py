from flask import Flask, render_template     #importing flask. -These are some properties that is a class and some methods from the flask libarary that we are going to need
from views import my_view    #importing local imports

app = Flask(__name__)                                   #Making a version of flask
app.register_blueprint(my_view)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e)



if __name__ == "__main__":                              #__main__ is the name of the global space
    app.run(debug=True, port=8000)                      #These codes are going to handle the running of our application