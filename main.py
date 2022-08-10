from flask import Flask
from werkzeug.datastructures import _omd_bucket

app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to python gprs test"

@app.route("/get")
def get_data():
    return "Its working"

if __name__ == "__main__":
    app.run(debug=True)
