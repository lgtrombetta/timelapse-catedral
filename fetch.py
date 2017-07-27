#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103
"""
Created on Wed Jul 19 16:55:42 2017

@author: leo

Fetches the image from an URL
"""

import urllib.request
import datetime
from subprocess import call
import os


def str2(num):
    """Completes one-digit numbers with a preceding 0"""
    if num < 10:
        return str(0)+str(num)
    return str(num)


u = urllib.request.urlopen('https://catedralaltapatagonia.com/partediario/' +
                           'images_webcams/foto_cam_06.jpg')
raw_data = u.read()
u.close()

home_dir = os.path.expanduser("~")
base_dir = open(home_dir+'/.timelapse-catedral/basedir.txt', 'r').read()
base_dir = base_dir.strip()

now = datetime.datetime.now()

path = os.path.join(base_dir, 'static/files', str(now.year), str2(now.month),
                    str2(now.day))

call(['mkdir', '-p', os.path.join(path, 'images')])

f = open(os.path.join(path, 'images', str(now.year)+'-'+str2(now.month)+'-' +
                      str2(now.day)+'_'+str2(now.hour)+'-'+str2(now.minute) +
                      '-'+str2(now.second)+'.jpg'), 'wb')
f.write(raw_data)
f.close()
