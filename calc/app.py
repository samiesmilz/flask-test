# Put your app in here.
from flask import Flask, request
import operations
app = Flask(__name__)


# Make base route
@app.route("/")
def home():
    return "Welcome to the simple flask calc!"


@app.route("/add")
def add():
    """Add a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    sum = operations.add(a, b)
    return str(sum)


@app.route("/sub")
def sub():
    """Substract b from a."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = operations.sub(a, b)
    return str(result)


@app.route("/mult")
def mult():
    """Multiply a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    prod = operations.mult(a, b)
    return str(prod)


@app.route("/div")
def div():
    """Divide a by b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    div = operations.div(a, b)
    return str(div)


@app.route("/math/<operation>")
def do_math(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    math = {"add": operations.add(a, b),
            "sub": operations.sub(a, b),
            "mult": operations.mult(a, b),
            "div": operations.div(a, b)

            }
    return f"{math[operation]}"
