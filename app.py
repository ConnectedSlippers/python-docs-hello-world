from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Preuve de concept (2023-08-02)"
