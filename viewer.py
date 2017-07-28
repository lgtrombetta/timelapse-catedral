#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103
"""
Web viewer
"""

import os
import datetime
import json
from flask import Flask, render_template, url_for


def str2(num):
    """Completes one-digit numbers with a preceding 0"""
    if num < 10:
        return str(0)+str(num)
    return str(num)


home_dir = os.path.expanduser("~")
base_dir = open(home_dir+'/.timelapse-catedral/basedir.txt', 'r').read()
base_dir = base_dir.strip()


viewer = Flask(__name__, static_url_path='/static')


@viewer.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@viewer.route('/today/')
def today():
    """Show today's video and pictures"""
    now = datetime.datetime.now()

    return show(str(now.year), str2(now.month), str2(now.day))
    # redirect(os.path.join(str(now.year), str2(now.month), str2(now.day)),
    # code=302)


@viewer.route('/<year>/<month>/<day>/')
def show(year, month, day):
    """Show pictures and video of a given day"""
    rel_path = os.path.join('files', year, month, day)
    abs_path = os.path.join(base_dir, 'static', rel_path)

    rp_img = os.path.join(rel_path, 'images')
    ap_img = os.path.join(abs_path, 'images')

    images = [url_for('static', filename=os.path.join(rp_img, f))
              for f in os.listdir(ap_img) if
              os.path.isfile(os.path.join(ap_img, f))]

    video = [url_for('static', filename=os.path.join(rel_path, f))
             for f in os.listdir(abs_path) if
             os.path.isfile(os.path.join(abs_path, f))]

    data = json.dumps({'date': os.path.join(year, month, day),
                       'images': images, 'video': video[0]},
                      ensure_ascii=False)

    return render_template('show.html', data=data)


if __name__ == '__main__':
    viewer.run(debug=True, host='0.0.0.0')
