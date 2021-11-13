import os
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


@app.route("/temp", methods=["POST"])
def temp_post():
    print(request.headers)
    try:
        data = request.json
        tc = data['tempC']
        tf = float(tc) * 9.0 / 5.0 + 32.0
        print(tc, tf)
        return "{'status': 'success'}"
    except Exception as e:
        print("Exception: {}".format(e))
        return "{'status': 'exception'}"


if __name__ == '__main__':
    print("\nStarting...")
    app.run(host='0.0.0.0')
