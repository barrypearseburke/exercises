__author__ = 'Barry'
##simple program to auto shutdown windows pc
#simple shutdown

import os

shutdown = input ("At what time do you want to shutdown your pc,in minutes")
shutdown = (shutdown*60)
time = ("shutdown -s -t {}".format(shutdown))
print (time)
os.system(time)