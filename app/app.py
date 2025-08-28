from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Unbox Robotics!"

@app.route("/health")
def health():
    return "OK"

@app.route("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password=os.getenv("POSTGRES_PASSWORD", "postgres"),
            host="db"
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"DB Time: {result}"
    except Exception as e:
        return f"Error: {e}"

