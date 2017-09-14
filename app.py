import os, datetime
from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.sqlite")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Models

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    content = db.Column(db.String(140))

    def __init__(self, owner, content):
        self.owner = ownerself.content = content

# decorator below
@app.route("/", methods=["GET"])
def index():
    return "Hi there from app.py"
