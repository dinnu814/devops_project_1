from flask import Flask

app = Flask(__name__)

@app.route("/info")
def myinfo():
    return "I am from Hyderabad"

@app.route("/phone")
def myphone():
    return "9874928342"

app.run(host="0.0.0.0")