#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103
"""
Created on Wed Jul 19 16:55:42 2017

@author: leo

Compiles the video of the day by taking the images as frames
"""

import datetime
import subprocess as sp
import os


def str2(num):
    """Completes one-digit numbers with a preceding 0"""
    if num < 10:
        return str(0)+str(num)
    return str(num)


home_dir = os.path.expanduser("~")
base_dir = open(home_dir+'/.timelapse-catedral/basedir.txt', 'r').read()
base_dir = base_dir.strip()

now = datetime.datetime.now()

path = os.path.join(base_dir, 'static/files', str(now.year), str2(now.month),
                    str2(now.day))

sp.call(['mkdir', '-p', os.path.join(path, 'images')])
os.chdir(os.path.join(path, 'images'))

filename = str(now.year)+'-'+str2(now.month)+'-'+str2(now.day)+'_timelapse.mp4'

try:
    sp.check_call("ffmpeg -pattern_type glob -i '*.jpg' -y "+filename,
                  shell=True)
    sp.check_call(['mv', filename, os.path.join('..', filename)])
except sp.CalledProcessError:
    print("ffmpeg required, please install")
