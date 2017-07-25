from subprocess import call
import os

basedir = os.getcwd()
homedir = os.path.expanduser("~")

call(['mkdir', '-p', homedir+'/.timelapse-catedral'])

f = open(homedir+'/.timelapse-catedral/basedir.txt','w')
f.write(basedir+'/')
f.close()
