#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=I0011,C0103
"""
Created on Wed Jul 19 16:55:42 2017

@author: leo

Run only once from the working dir to create a config file with its path
"""

from subprocess import call
import os

base_dir = os.getcwd()
home_dir = os.path.expanduser("~")

call(['mkdir', '-p', home_dir+'/.timelapse-catedral'])

f = open(home_dir+'/.timelapse-catedral/basedir.txt', 'w')
f.write(base_dir+'/')
f.close()
