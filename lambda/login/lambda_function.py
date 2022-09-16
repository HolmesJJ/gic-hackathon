import hashlib
import mysql.connector

config = {
    "user": "gic",
    "password": "gic-hackathon",
    "host": "gic.cwffb4xk8n0d.ap-southeast-1.rds.amazonaws.com",
    "database": "gic_hackathon",
}


def lambda_handler(event, context):
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    name = event["name"]
    password = hashlib.sha256(event["password"].encode("utf-8")).hexdigest()
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
