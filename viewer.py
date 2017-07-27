#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103
"""
Web viewer
"""

import os
import json
from flask import Flask, render_template, url_for


app = Flask(__name__, static_url_path='/static')


home_dir = os.path.expanduser("~")
base_dir = open(home_dir+'/.timelapse-catedral/basedir.txt', 'r').read()
base_dir = base_dir.strip()

if base_dir[-1] != '/':
    base_dir = base_dir+'/'


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/capture/')
def capture():
    """Capture"""
    """mypath = '/home/marco/Desktop'

    onlyfiles = [f for f in os.listdir(mypath) if
                 os.path.isfile(os.path.join(mypath, f))]

    data = json.dumps(onlyfiles, ensure_ascii=False)"""

    ###return data
    return render_template('capture.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
