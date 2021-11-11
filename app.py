import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


if __name__ == '__main__':
    print("\nStarting...")
    app.run(host='0.0.0.0')
