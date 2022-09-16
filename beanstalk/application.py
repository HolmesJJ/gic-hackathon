import hashlib
import mysql.connector

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

application = Flask(__name__, static_url_path="", static_folder="web")
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"
config = {
    "user": "gic",
    "password": "gic-hackathon",
    "host": "gic.cwffb4xk8n0d.ap-southeast-1.rds.amazonaws.com",
    "database": "gic_hackathon",
}


@application.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello from API</p>"


@application.route("/logo")
@cross_origin()
def logo():
    return "<img src='https://gic-hackathon.s3.ap-southeast-1.amazonaws.com/logo.png' width='200'>"


@application.route("/login", methods=["POST"])
@cross_origin()
def login():
    content = request.json
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    name = content["name"]
    password = hashlib.sha256(content["password"].encode("utf-8")).hexdigest()
    cursor.execute("SELECT * FROM user AS u INNER JOIN role AS r ON u.role = r.id "
                   "WHERE u.name = '" + name + "' and u.password = '" + password + "'")
    result = cursor.fetchall()
    db.close()
    response = {
        "code": 1 if len(result) > 0 else 0,
    }
    if len(result) > 0:
        response["data"] = {
            "name": result[0][0],
            "role": result[0][2],
        }
    return response


if __name__ == "__main__":
    application.debug = True
    # application.run(host="0.0.0.0", port=5000)
    application.run()
