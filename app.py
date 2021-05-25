# app.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mycashless!"

@app.route("/countries")
def get_countries():
    return "Hello Mycashless!"