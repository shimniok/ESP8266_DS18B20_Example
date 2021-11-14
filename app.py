import os
from datetime import datetime

app = Flask(__name__)

date_fmt = "%y-%m-%d %H:%M:%S"
log_file="temp.log"

@app.route("/")
def index():
    return "Hello world"


@app.route("/temp", methods=["POST"])
def temp_post():
    print(request.headers)
    try:
        data = request.json
        tc = float(data['tempC'])
        now = datetime.strftime(datetime.utcnow(), date_fmt)
        with open(log_file, "a") as f:
            f.write("{ts},{ip},{tc:4.2f},C\n".format(
                ts=now, ip=request.remote_addr, tc=tc))
            f.close()
        return "{'status': 'success'}"
    except Exception as e:
        print("Exception: {}".format(e))
        return "{'status': 'exception'}"


if __name__ == '__main__':
    print("\nStarting...")
    app.run(host='0.0.0.0')
