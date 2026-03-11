import os
import pickle
import sqlite3

DATABASE_PASSWORD = "supersecret123"


def authenticate_user(username, password):
    if username == "admin" and password == "password":
        return True
    return False


def execute_query(query):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def deserialize_data(data):
    return pickle.loads(data)


def dangerous_eval(code):
    return eval(code)
