from flask import Flask, render_template, session, redirect
import pymongo
from pymongo import MongoClient
from functools import wraps


# create routes
from user import routes

# cluster = MongoClient("mongodb+srv://aieng:12345678m@cluster0.s23zp.mongodb.net/aieng?retryWrites=true&w=majority")

# db = cluster["aieng"]
# collection = ["aieng"]




# Create instance of Flask model is app
app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database connection
client = pymongo.MongoClient('localhost', 27017)
db = client.aieng

# Decorators

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


# create decorator is @app
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/single-courses")
def single_courses():
    return render_template("single-courses.html")


@app.route("/single-post")
def single_post():
    return render_template("single-post.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/forgot-password")
def forgot_password():
    return render_template("forgot-password.html")

@app.route("/page-not-found")
def page_not_found():
    return render_template("404.html")

@app.route("/blank")
def blank():
    return render_template("blank.html")

@app.route("/buttons")
def buttons():
    return render_template("buttons.html")

@app.route("/cards")
def cards():
    return render_template("cards.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/tables")
def tables():
    return render_template("tables.html")

@app.route("/animation")
def animation():
    return render_template("animation.html")

@app.route("/border")
def border():
    return render_template("border.html")

@app.route("/color")
def color():
    return render_template("color.html")

@app.route("/other")
def other():
    return render_template("other.html")







# Debugger Mode is ON when we check any errors in runtime And when the site is complete then the Debugger Mode is OFF
app.run(debug=True)