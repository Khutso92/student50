from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<br>Hello world<br>"


@app.route('hello/')
def hello():
    return "hello there"

