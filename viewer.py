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

    today_rp = os.path.join('files', str(now.year), str2(now.month),
                            str2(now.day))
    today_ap = os.path.join(base_dir, 'static', today_rp)

    today_rp_img = os.path.join(today_rp, 'images')
    today_ap_img = os.path.join(today_ap, 'images')

    images = [url_for('static', filename=os.path.join(today_rp_img, f))
              for f in os.listdir(today_ap_img) if
              os.path.isfile(os.path.join(today_ap_img, f))]

    video = [url_for('static', filename=os.path.join(today_rp, f))
             for f in os.listdir(today_ap) if
             os.path.isfile(os.path.join(today_ap, f))]

    data = json.dumps({'images': images, 'video': video[0]},
                      ensure_ascii=False)

    return render_template('show.html', data=data)


if __name__ == '__main__':
    viewer.run(debug=True, host='0.0.0.0')
