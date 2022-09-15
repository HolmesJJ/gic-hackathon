import json
import hashlib
import mysql.connector

from flask import Flask
from flask import request
from waitress import serve
from pymongo import MongoClient

app = Flask(__name__)
config = {
    "user": "gic",
    "password": "gic",
    "host": "localhost",
    "database": "gic_hackathon",
}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=["POST"])
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


@app.route("/train", methods=["GET"])
def read_train():
    content = request.args
    client = MongoClient("mongodb://localhost:27017/")
    db = client.sample
    collection = db.train
    if content.get("id") is None:
        result = json.dumps(list(collection.find({}, {"_id": 0})))
    else:
        result = json.dumps(list(collection.find({"Id": int(content.get("id"))}, {"_id": 0})))
    client.close()
    return result


@app.route("/test", methods=["GET"])
def read_test():
    content = request.args
    client = MongoClient("mongodb://localhost:27017/")
    db = client.sample
    collection = db.test
    if content.get("id") is None:
        result = json.dumps(list(collection.find({}, {"_id": 0})))
    else:
        result = json.dumps(list(collection.find({"Id": int(content.get("id"))}, {"_id": 0})))
    client.close()
    return result


if __name__ == "__main__":
    print("Run App")
    serve(app, host="127.0.0.1", port=8080)
