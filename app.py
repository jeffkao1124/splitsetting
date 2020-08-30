from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

app.run()







