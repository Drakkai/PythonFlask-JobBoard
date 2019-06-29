from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def 

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')