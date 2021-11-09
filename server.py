from flask import Flask, render_template
from flask import redirect, url_for, request
import os 

PORT = 8000

app = Flask("__main__")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/signUp")
def signUp():
    return render_template('signUp.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = PORT, debug = True)