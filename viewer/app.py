from flask import Flask, render_template, url_for
from subprocess import call
from shutil import move
from time import sleep
import os, sys
import json
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('capture.html')

@app.route('/capture/')
def capture():
    mypath='/home/marco/Desktop'
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    data=json.dumps(onlyfiles,ensure_ascii=False)

    return (data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
