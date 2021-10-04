from ctypes import windll, Structure, c_long, byref
import time
from  configparser import *
import os
import sys
configparser = ConfigParser()


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    global pt
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def writeConfig():
    configFilePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config.txt'))
    configparser.read(configFilePath)
    curxPosition = configparser.get('Config File', 'xPosition')
    curyPosition = configparser.get('Config File', 'yPosition')
    print( "changing current x position: " + str(curxPosition) + " to " + str(pt.x))
    print( "changing current y position: " + str(curyPosition) + " to " + str(pt.y))
    configparser.set('Config File' , 'xPosition' , str(pt.x))
    configparser.set('Config File' , 'yPosition' , str(pt.y))
    f = open(configFilePath, "w")
    print("writing config file to " + configFilePath)
    configparser.write(f)

seconds = 0
print ("getting mouse position, place mouse where you want the top left of the button panel to be located")
while seconds < 5:
    pos = queryMousePosition()

    print ("writing location " + str(pos) + " to config in " + str(5-seconds) + " seconds")
    seconds += 1
    time.sleep(1)
print ("writing location " + str(pos) +" to config")
writeConfig()
