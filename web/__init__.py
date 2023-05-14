"""
This should be using server side sessions and store it in a local db.sqlite
"""


from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from web.validator import generate_code_from_file, generate_simple_code

# CONFIG SETTINGS
CODE_LENGTH = 6  # This must be an integer
# These are keys used to both generate the public and private code as well as the font needed to easily decipher
# the correct code for authentication.
HARD_KEY = "./example/font1.txt"
HARDEST_KEY = "./example/dict.txt"
FLASK_SECRET = "mysecret"  # This should be in an .env file for security, but for the demo is intentionally left here


# create the extension
db = SQLAlchemy()

app = Flask(__name__)


app.config["SECRET_KEY"] = FLASK_SECRET
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
    return render_template("home.html.jinja", title="About")


@app.route("/simple")
def simple():
    the_code = generate_simple_code(CODE_LENGTH)
    session["simple_val"] = the_code
    return render_template(
        "authentication/simple.html.jinja", title="Simple Authentication", authentication_code=the_code
    )


@app.route("/simple_authentication", methods=["POST"])
def simple_authentication():
    # Get the info from the form
    user_input = request.form["authentication"]
    if user_input == session["simple_val"]:  # they have passes the authentication
        flash("Authentication successful")
        return render_template("page.html.jinja", v_name="simple")
    else:
        flash("Authentication failed")
        return redirect(url_for("simple"))


@app.route("/hard")
def hard():
    code_array = generate_code_from_file(CODE_LENGTH, HARD_KEY)
    private_code = code_array[0]
    public_code = code_array[1]
    session["hard_val"] = private_code
    return render_template(
        "authentication/hard.html.jinja", title="Hard Authentication", authentication_code=public_code
    )


@app.route("/hard_authentication", methods=["POST"])
def hard_authentication():
    # Get the info from the form
    user_input = request.form["authentication"]
    if user_input == session["hard_val"]:  # they have passes the authentication
        flash("Authentication successful")
        return render_template("page.html.jinja", v_name="hard")
    else:
        flash("Authentication failed")
        return redirect(url_for("hard"))


@app.route("/hardest")
def hardest():
    code_array = generate_code_from_file(CODE_LENGTH, HARDEST_KEY)
    private_code = code_array[0]
    public_code = code_array[1]
    session["hardest_val"] = private_code
    return render_template(
        "authentication/hardest.html.jinja", title="Hardest Authentication", authentication_code=public_code
    )


@app.route("/hardest_authentication", methods=["POST"])
def hardest_authentication():
    # Get the info from the form
    user_input = request.form["authentication"]
    if user_input == session["hardest_val"]:  # they have passes the authentication
        flash("Authentication successful")
        return render_template("page.html.jinja", v_name="hardest")
    else:
        flash("Authentication failed")
        return redirect(url_for("hardest"))


"""
@app.route("/set/<value>")
def set_session(value):
    session["value"] = value
    return f"The value is {value}"


@app.route("/get")
def get_session():
    return f'The session value is {session.get("value")}'
"""
