import configparser
import glob
import os
import xml.etree.ElementTree as ET
import sys
from os.path import exists as file_exists
from ctypes import windll, Structure, c_long, byref
import time
configparser = configparser.RawConfigParser()

def getConfig():
    configFilePath = 'config.txt'
    configWindowLoc = 'windowConfig.txt'
    configparser.read(configFilePath)
    global soundBoardPath
    global boardButtonColor
    global currentBoardButtonColor
    global soundButtonColor
    global debug
    global xPosition
    global yPosition
    global setKeyboardShortCuts
    global rainbowButtons
    global getMousePositionForWindow
    soundBoardPath = configparser.get('Config File', 'soundBoardPath')
    boardButtonColor = configparser.get('Config File', 'boardButtonColor')
    currentBoardButtonColor = configparser.get('Config File', 'currentBoardButtonColor')
    soundButtonColor = configparser.get('Config File', 'soundButtonColor')
    debug = configparser.get('Config File', 'debug')
    xPosition = configparser.get('Config File', 'xPosition')
    yPosition = configparser.get('Config File', 'yPosition')
    setKeyboardShortCuts = configparser.get('Config File', 'setKeyboardShortCuts')
    rainbowButtons = configparser.get('Config File', 'rainbowButtons')
    getMousePositionForWindow = configparser.get('Config File', 'getMousePositionForWindow')
    if rainbowButtons == "True":
        soundButtonColor = 0
    if checkExistingWindowConfig():
        print("found window location config file: using these values")
        configparser.read(configWindowLoc)
        xPosition = configparser.get('Window Config', 'xPosition')
        yPosition = configparser.get('Window Config', 'yPosition')
def checkExistingWindowConfig():
    configFilePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'windowConfig.txt'))
    testFileList = []
    testFileList = glob.glob(configFilePath)
    if not testFileList:
        return False
    else:
        return True
def setBoardList():
    global boardList
    print(soundBoardPath)
    boardList = glob.glob(soundBoardPath + "*" )
def setWindow():
    global windowWidth
    windowWidth = 158 * len(boardList)
    print ("setting window to " + str(len(boardList)) + " columns with a width of " + str(windowWidth) + " pixels")
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
def fitToGrid(n, b):
    digits = ""
    if n == 0:
        digits = "0"
        digits = str(int(digits)+1)
        return digits
    while n:
        digits = str(n % b) + digits
        n //= b
    digits = str(int(digits)+1)
    return digits
def boardButton():
    MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index=indexNumber, type='0', color=buttonColor, key='0', ctrl='0', shift='0', alt='0', anyway='0', exclusive='0', trigger='0', xinput='0' )
    MB_MIDI = ET.SubElement( MacroButton, 'MB_MIDI', b1='00', b2='00', b3='00', b4='00', b5='00', b6='00')
    MB_TRIGGER = ET.SubElement( MacroButton, 'MB_TRIGGER', tchannel='0', tin='0.0', tout='0.0', tmsHold='100', tafterMute='0')
    MB_XINPUT = ET.SubElement( MacroButton, 'MB_XINPUT', nctrl='0', nbutton='0')
    MB_Name = ET.SubElement( MacroButton, 'MB_Name')
    MB_Name.text = os.path.basename(boardList[boardButtonLoop]) #todo first N letters of File Name
    MB_Subname = ET.SubElement( MacroButton, 'MB_Subname')
    #MB_Subname.text = soundPath[i] # todo remaining N letters of File Name
    MB_InitRequest = ET.SubElement( MacroButton, 'MB_InitRequest')
    MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
  #  MB_OnRequest.text = "Load(" + boardList[boardLoop] + os.path.basename(boardList[boardLoop]) + ".xml" + ")" #path to sound file.mp3
    MB_OnRequest.text = "Load(\"" + boardList[boardButtonLoop] + ".xml\"" + ")" #path to sound file.mp3
    MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')
def soundButton():
    global runs
    global button
    global ctrl
    global shift
    global alt
    if debug is True:
        print ("sound button index #: " + str(soundButtonLoop))
        print ("sound file is: " + soundList[soundButtonLoop])
        print ("sound board index number is:" +str(indexNumber))
    if setKeyboardShortCuts == "True":
        getButton()
    else:
        button = "0"
        ctrl = "0"
        shift = "0"
        alt = "0"
    MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index=indexNumber, type='0', color=str(soundButtonColor), key=str(button), ctrl=ctrl, shift=shift, alt=alt, anyway='0', exclusive='0', trigger='0', xinput='0' )
    MB_MIDI = ET.SubElement( MacroButton, 'MB_MIDI', b1='00', b2='00', b3='00', b4='00', b5='00', b6='00')
    MB_TRIGGER = ET.SubElement( MacroButton, 'MB_TRIGGER', tchannel='0', tin='0.0', tout='0.0', tmsHold='100', tafterMute='0')
    MB_XINPUT = ET.SubElement( MacroButton, 'MB_XINPUT', nctrl='0', nbutton='0')
    MB_Name = ET.SubElement( MacroButton, 'MB_Name')
    MB_Name.text = os.path.basename(soundList[soundButtonLoop]) #todo first N letters of File Name
    MB_Subname = ET.SubElement( MacroButton, 'MB_Subname')
    #MB_Subname.text = soundPath[i] # todo remaining N letters of File Name
    MB_InitRequest = ET.SubElement( MacroButton, 'MB_InitRequest')
    MB_InitRequest.text = 'Recorder.mode.PlayOnLoad=1'
    MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
    MB_OnRequest.text = 'Recorder.load=' + "\"" +soundList[soundButtonLoop] + "\""  #path to sound file.mp3
    MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')
def writeBoard():
    buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
    ET.indent(buttonMap, space=" ", level=0)
    buttonMap.write(soundBoardPath + os.path.basename(boardList[boardLoop])+".xml", encoding='utf8', method='xml')
    print("writing button map file: " + soundBoardPath + os.path.basename(boardList[boardLoop])+".xml")
def printFoundDirs():
    i = 0
    while i < len(boardList):
        print("found directory " + os.path.basename(boardList[i]))
        #print("writing button map file: " + soundBoardPath + os.path.basename(boardList[i])+".xml")
        i +=1
def setBoardHeight():
    global boardHeight
    boardHeight = len(soundList)
def getButton():
    global runs
    global button
    global ctrl
    global shift
    global alt
    global soundButtonColor
    global rainbowButtons
    ctrl = "0"
    shift = "0"
    alt = "0"
    #f13 = button 85
    button = str(85 + runs)
    runs +=1
    if runs > 11:
        ctrl = "1"
        shift = "0"
        alt = "0"
        button = str(85 + runs - 11)
    if runs > 22:
        ctrl = "0"
        shift = "1"
        alt = "0"
        button = str(85 + runs - 22)
    if runs > 33:
        ctrl = "0"
        shift = "0"
        alt = "1"
        button = str(85 + runs - 33)
    if runs > 44:
        button = "0"
        ctrl = "0"
        shift = "0"
        alt = "0"
    if rainbowButtons == "True":
        soundButtonColor +=1
        if soundButtonColor > 8:
            soundButtonColor = 0
    if debug == "True":
        print(button)
        print(ctrl)
        print(shift)
        print(alt)
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
def getMouse():
    seconds = 0
    print ("getting mouse position, place mouse where you want the top left of the button panel to be located")
    while seconds < 5:
        pos = queryMousePosition()

        print ("writing location " + str(pos) + " to config in " + str(5-seconds) + " seconds")
        seconds += 1
        time.sleep(1)
    print ("writing location " + str(pos) +" to config")
    writeConfig()

getConfig()
checkExisting()
setBoardList()
if getMousePositionForWindow == "True":
     getMouse()
setWindow()
printFoundDirs()

#board Loop writes each seperate board
boardLoop=0
while boardLoop < len(boardList):
    runs = 0
    soundPathMP3 = boardList[boardLoop] + "\\" + "*.mp3"
    soundPathWAV = boardList[boardLoop] + "\\" + "*.wav"
    soundList = glob.glob(soundPathMP3) + glob.glob(soundPathWAV)
    if debug is True:
        print ("generating soundboard for directory: " + os.path.basename(boardList[boardLoop]) + " containing " + str(len(soundList)) + " sound files")
    #print ("search directory for sound files " + soundPath)
    indexCounter = 1
    indexNumber = str(indexCounter)
    VBAudioVoicemeeterMacroButtonMap = ET.Element('VBAudioVoicemeeterMacroButtonMap')
    MacroButtonConfiguration = ET.SubElement(VBAudioVoicemeeterMacroButtonMap, 'MacroButtonConfiguration', x0=xPosition, y0=yPosition, dx=str(windowWidth), dy='576')

    boardButtonLoop = 0
    while boardButtonLoop < len(boardList):
        buttonColor=boardButtonColor
        #print ('comparing to find current board')
        #print (boardList[boardLoop])
        #print (boardList[boardButtonLoop])
        if boardList[boardLoop] == boardList[boardButtonLoop]:
            buttonColor = currentBoardButtonColor
            #print("current board found")
        boardButton()
        indexNumber = fitToGrid(indexCounter,len(boardList))
        indexCounter +=1
        boardButtonLoop +=1

    soundButtonLoop = 0
    while soundButtonLoop < len(soundList):
       buttonColor=soundButtonColor
       soundButton()
       indexNumber = fitToGrid(indexCounter,len(boardList))
       indexCounter +=1
       soundButtonLoop +=1
    writeBoard()

    boardLoop +=1



#
#   buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
#   ET.indent(buttonMap, space=" ", level=0)
#   buttonMap.write(selfPath+os.path.basename(pathList[i]), encoding='utf8', method='xml')
#   print("button map written to " + path)
