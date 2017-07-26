import datetime
import subprocess as sp
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

sp.call(['mkdir', '-p', dir+'/images'])
os.chdir(dir+'/images')

filename=str(now.year)+'-'+str2(now.month)+'-'+str2(now.day)+'_timelapse.mp4'

try:
    sp.check_call("ffmpeg -pattern_type glob -i '*.jpg' -y "+filename,shell=True)
    sp.check_call(['mv', filename, '../'+filename])
except sp.CalledProcessError:
    print("ffmpeg required, please install")
