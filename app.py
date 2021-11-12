import os
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


@app.route('/postplain', methods=["POST"])
def postplain():
    data = request.json
    print(data)
    return "Success"

if __name__ == '__main__':
    print("\nStarting...")
    app.run(host='0.0.0.0')
