from flask import Flask, render_template, session, redirect
import pymongo
from pymongo import MongoClient

# cluster = MongoClient("mongodb+srv://aieng:<Pagalalone42!>@cluster0.s23zp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# db = cluster("aieng")
# collection = ("aieng")

# create routes
from user import routes


# Create instance of Flask model is app
app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database connection
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system


# create decorator is @app
@app.route("/")
def index():
    return render_template("index.html")


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


# Debugger Mode is ON when we check any errors in runtime And when the site is complete then the Debugger Mode is OFF
app.run(debug=True)