from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'],
                            database=os.environ['POSTGRES_DB'],
                            password=os.environ['POSTGRES_PASSWORD'],
                            user=os.environ['POSTGRES_USER'])
    return conn

@app.route("/")
def hello_world():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM t;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data