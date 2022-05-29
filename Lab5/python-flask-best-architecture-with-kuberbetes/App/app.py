from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Python!"


@app.route("/health")
def check():
    return "ok", 200

