#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:55:42 2017

@author: leo
"""

import urllib.request
import datetime
from subprocess import call


def str2(n):
    if n<10:
        return str(0)+str(n)
    else:
        return str(n)

u = urllib.request.urlopen('https://catedralaltapatagonia.com/partediario/images_webcams/foto_cam_06.jpg')
raw_data = u.read()
u.close()

now = datetime.datetime.now()

homedir = os.path.expanduser("~")
basedir = open(homedir+'/.timelapse-catedral/basedir.txt','r').read().strip()
if basedir[-1] != '/': basedir = basedir+'/'

dir = basedir+str(now.year)+'/'+str2(now.month)+'/'+str2(now.day)

call(['mkdir', '-p', dir+'/images'])

f = open(dir+'/images/'+str(now.year)+'-'+str2(now.month)+'-'+str2(now.day)+'_'+str2(now.hour)+'-'+str2(now.minute)+'-'+str2(now.second)+'.jpg','wb')
f.write(raw_data)
f.close()
