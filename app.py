"""
This should be using server side sessions and store it in a local db.sqlite
"""

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

app = Flask(__name__)


app.config["SECRET_KEY"] = "mysecret"
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SESSION_TYPE"] = "sqlalchemy"
app.config["SESSION_SQLALCHEMY"] = db


# initialize the app with the extension
sess = Session()
sess.init_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
@app.route("/index")
def index():
    return render_template("base.html.jinja", title="Index")


@app.route("/simple")
def simple():
    the_code = "asdf"
    session["simple_val"] = the_code
    return render_template("validation/simple.html.jinja", title="Simple Validation", validation_code=the_code)


@app.route("/simple_validation", methods=["POST"])
def simple_validation():
    # Get the info from the form
    user_input = request.form["validation"]
    if user_input == session["simple_val"]:  # they have passes the validation
        flash("Validation successful")
        return render_template("page.html.jinja", info=user_input)
    else:
        flash("Validation failed")
        return redirect(url_for("simple"))


@app.route("/hard")
def hard():
    return render_template("validation/hard.html.jinja", title="Harder Validation")


@app.route("/hardest")
def hardest():
    return render_template("validation/hardest.html.jinja", title="Hardest Validation")


@app.route("/set/<value>")
def set_session(value):
    session["value"] = value
    return f"The value is {value}"


@app.route("/get")
def get_session():
    return f'The session value is {session.get("value")}'
