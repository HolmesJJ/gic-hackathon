import pandas as pd
import hashlib
import mysql.connector

'''
MySQL
'''
config = {
    "user": "gic",
    "password": "gic-hackathon",
    "host": "gic.cwffb4xk8n0d.ap-southeast-1.rds.amazonaws.com",
}
mysql_db = mysql.connector.connect(**config)

cursor = mysql_db.cursor()

# Drop Database
cursor.execute("DROP DATABASE IF EXISTS gic_hackathon")

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS gic_hackathon")
cursor.execute("USE gic_hackathon")

# Create User Table
cursor.execute("CREATE TABLE IF NOT EXISTS role (id INT, name TEXT)")
insert_roles = "INSERT INTO role (id, name) VALUES (%s, %s)"
roles = [
    (1, "admin"),
    (2, "customer"),
]
cursor.executemany(insert_roles, roles)
cursor.execute("CREATE TABLE IF NOT EXISTS user (name TEXT, password TEXT, role INT)")
insert_users = "INSERT INTO user (name, password, role) VALUES (%s, %s, %s)"
users = [
    ("hjj", hashlib.sha256("123456".encode("utf-8")).hexdigest(), 1),
    ("kk", hashlib.sha256("123456".encode("utf-8")).hexdigest(), 2),
    ("lwk", hashlib.sha256("123456".encode("utf-8")).hexdigest(), 2),
    ("yzl", hashlib.sha256("123456".encode("utf-8")).hexdigest(), 2),
    ("hx", hashlib.sha256("123456".encode("utf-8")).hexdigest(), 2)
]
cursor.executemany(insert_users, users)
mysql_db.commit()
mysql_db.close()

if __name__ == "__main__":
    print("Import Data")
