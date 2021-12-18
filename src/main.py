from flask import Flask
from flask import request
import sqlite3
import time
import json

app = Flask(__name__)
db_file = './clipboard.db3'


@app.route("/")
def index():
    return "<p>Clip Board Center.</p>"


@app.route("/upload", methods=['POST'])
def upload():
    content = request.form['content']
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute('insert into `board` (`timestamp`, `content`) values ({}, "{}")'
                ''.format(int(time.time()), content))
    conn.commit()
    cur.close()
    conn.close()
    return json.dumps({'code': 0, 'msg': 'success'})


@app.route("/download", methods=["GET"])
def download():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    rows = cur.execute('select `content` from `board` order by `id` desc limit 1')
    content = ''
    for r in rows:
        content = r[0]
    cur.close()
    conn.close()
    return content


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
