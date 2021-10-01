import configparser
import glob
import os
import sys
from os.path import exists as file_exists
configparser = configparser.RawConfigParser()

def getConfig():
    configFilePath = 'config.txt'
    configparser.read(configFilePath)
    global soundBoardPath
    global boardButtonColor
    global currentBoardButtonColor
    global soundButtonColor
    global boardList
    soundBoardPath = configparser.get('Config File', 'soundBoardPath')
    boardButtonColor = configparser.get('Config File', 'boardButtonColor')
    currentBoardButtonColor = configparser.get('Config File', 'currentBoardButtonColor')
    soundButtonColor = configparser.get('Config File', 'soundButtonColor')
    print(soundBoardPath)
    boardList = glob.glob(soundBoardPath + "*" )

def checkExisting():
    testFilePath = soundBoardPath + "*.xml"
    testFileList = []
    testFileList = glob.glob(testFilePath)
    print(soundBoardPath + "*.xml")
    print("checking for existing board maps")
    i =0
    while i < len(testFileList):
        print (testFileList[i])
        i +=1
    if not testFileList:
        print("no existing board maps found")
    else:
        i = 0
        while i < len(testFileList):
            print("removing existing board map " + testFileList[i])
            os.remove(testFileList[i])
            i +=1

getConfig()
checkExisting()
