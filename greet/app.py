from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def home():
    return f"<p> Welcome home! </p>"


@app.route("/welcome")
def welcome():
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    return "welcome back"
