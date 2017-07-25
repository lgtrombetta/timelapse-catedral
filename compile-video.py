import datetime
from subprocess import call
import os

def str2(n):
    if n<10:
        return str(0)+str(n)
    else:
        return str(n)


now = datetime.datetime.now()

homedir = os.path.expanduser("~")
basedir = open(homedir+'/.timelapse-catedral/basedir.txt','r').read().strip()
if basedir[-1] != '/': basedir = basedir+'/'

dir = basedir+str(now.year)+'/'+str2(now.month)+'/'+str2(now.day)

call(['mkdir', '-p', dir+'/images'])
os.chdir(dir+'/images')

filename=str(now.year)+'-'+str2(now.month)+'-'+str2(now.day)+'_timelapse.mp4'

call("ffmpeg -pattern_type glob -i '*.jpg' -y "+filename,shell=True)
call(['mv', filename, '../'+filename])
