from ctypes import windll, Structure, c_long, byref
import time
from  configparser import *
import os
import sys
import glob
configparser = ConfigParser(comment_prefixes='/', allow_no_value=True)


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def checkExistingWindowConfig():
    configFilePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'windowConfig.txt'))
    testFileList = []
    testFileList = glob.glob(configFilePath)
    if not testFileList:
        return False
    else:
        return True

def queryMousePosition():
    global pt
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def writeConfig():
    configFilePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'windowConfig.txt'))
    if checkExistingWindowConfig():
        print("existing window config file found: updating")
        configparser.read(configFilePath)
        curxPosition = configparser.get('Window Config', 'xPosition')
        curyPosition = configparser.get('Window Config', 'yPosition')
        print( "changing current x position: " + str(curxPosition) + " to " + str(pt.x))
        print( "changing current y position: " + str(curyPosition) + " to " + str(pt.y))
        configparser.set('Window Config' , 'xPosition' , str(pt.x))
        configparser.set('Window Config' , 'yPosition' , str(pt.y))
    else:
        print("existing window config file not found: creating")
        configparser.add_section('Window Config')
        configparser.set('Window Config' , 'xPosition' , str(pt.x))
        configparser.set('Window Config' , 'yPosition' , str(pt.y))

    f = open(configFilePath, "w")
    print("writing Window Config to " + configFilePath)
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
