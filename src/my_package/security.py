import os
import pickle
import sqlite3

# Security issue: hardcoded password
DATABASE_PASSWORD = "supersecret123"


def authenticate_user(username, password):
    # Security issue: storing passwords in plain text
    if username == "admin" and password == "password":
        return True
    return False


def execute_query(query):
    # Security issue: SQL injection vulnerability
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    cursor.execute(query)  # Direct execution without parameterization
    results = cursor.fetchall()
    conn.close()
    return results


def deserialize_data(data):
    # Security issue: using pickle for deserialization (insecure)
    return pickle.loads(data)


def dangerous_eval(code):
    # Security issue: using eval (code injection)
    return eval(code)
