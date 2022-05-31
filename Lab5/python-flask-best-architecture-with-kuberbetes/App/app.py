from flask import Flask
app = Flask(__name__)
import math
import random
import os


@app.route("/")
def hello():
    _ = random.randint(1, 100000)
    number = math.sqrt(_)
    return "Hello from Python! " + str(number) + os.getenv("name", "default")


@app.route("/health")
def check():
    return "ok", 200

