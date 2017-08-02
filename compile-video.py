#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103
"""
Created on Wed Jul 19 16:55:42 2017

@author: leo

Compiles the video of the day by taking the images as frames
"""

import argparse
import datetime
import os
import subprocess as sp
import time


def str2(num):
    """Completes one-digit numbers with a preceding 0"""
    if num < 10:
        return str(0)+str(num)
    return str(num)


now = datetime.datetime.now()


parser = argparse.ArgumentParser(description="compile video")
parser.add_argument("-d", "--date", help="date in yyyy-mm-dd format",
                    default=str(now.year) +
                    '-'+str2(now.month)+'-'+str2(now.day))
parser.add_argument("-f", "--fps", type=int, help="frames per second",
                    default=25)
args = parser.parse_args()


date = datetime.datetime(*time.strptime(args.date, "%Y-%m-%d")[:3])


home_dir = os.path.expanduser("~")
base_dir = open(home_dir+'/.timelapse-catedral/basedir.txt', 'r').read()
base_dir = base_dir.strip()

path = os.path.join(base_dir, 'static/files', str(date.year), str2(date.month),
                    str2(date.day))


if not os.path.exists(path):
    print("No images exist from", args.date)
else:
    sp.call(['mkdir', '-p', os.path.join(path, 'images')])
    os.chdir(os.path.join(path, 'images'))

    filename = str(date.year)+'-'+str2(date.month)+'-'+str2(
        date.day)+'_timelapse_fps'+str(args.fps)+'.mp4'

    try:
        sp.check_call("ffmpeg -framerate "+str(args.fps) +
                      " -pattern_type glob -i '*.jpg' -y "+filename,
                      shell=True)
        sp.check_call(['mv', filename, os.path.join('..', filename)])
    except sp.CalledProcessError:
        print("ffmpeg required, please install")
