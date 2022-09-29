import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect("postgres://postgres:password@db-hw3.cahemnsyz5yw.us-east-2.rds.amazonaws.com:5432/postgres")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT VERSION();')
    x=cur.fetchone()
    return render_template('index.html', database_version=x[0])
    # return render_template('index.html')
    # return s
