import configparser
from glob import glob
import os
import xml.etree.ElementTree as ET
import sys

configparser = configparser.RawConfigParser()
configFilePath = 'config.txt'
configparser.read(configFilePath)
soundBoardPath = configparser.get('Config File', 'soundBoardPath')
boardButtonColor = configparser.get('Config File', 'boardButtonColor')
currentBoardButtonColor = configparser.get('Config File', 'currentBoardButtonColor')
soundButtonColor = configparser.get('Config File', 'soundButtonColor')
print(soundBoardPath)

def soundButton():
   MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index=indexNumber, type='0', color=buttonColor, key='85', ctrl='0', shift='0', alt='0', anyway='0', exclusive='0', trigger='0', xinput='0' )
   MB_MIDI = ET.SubElement( MacroButton, 'MB_MIDI', b1='00', b2='00', b3='00', b4='00', b5='00', b6='00')
   MB_TRIGGER = ET.SubElement( MacroButton, 'MB_TRIGGER', tchannel='0', tin='0.0', tout='0.0', tmsHold='100', tafterMute='0')
   MB_XINPUT = ET.SubElement( MacroButton, 'MB_XINPUT', nctrl='0', nbutton='0')
   MB_Name = ET.SubElement( MacroButton, 'MB_Name')
   MB_Name.text = os.path.basename(soundPath[i]) #todo first N letters of File Name
   MB_Subname = ET.SubElement( MacroButton, 'MB_Subname')
   #MB_Subname.text = soundPath[i] # todo remaining N letters of File Name
   MB_InitRequest = ET.SubElement( MacroButton, 'MB_InitRequest')
   MB_InitRequest.text = 'Recorder.mode.PlayOnLoad=1'
   MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
   MB_OnRequest.text = 'Recorder.load=' + "\"" +soundPath[soundButtonLoop] + "\""  #path to sound file.mp3
   MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')

def boardButton():
   MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index=indexNumber, type='0', color=buttonColor, key='85', ctrl='0', shift='0', alt='0', anyway='0', exclusive='0', trigger='0', xinput='0' )
   MB_MIDI = ET.SubElement( MacroButton, 'MB_MIDI', b1='00', b2='00', b3='00', b4='00', b5='00', b6='00')
   MB_TRIGGER = ET.SubElement( MacroButton, 'MB_TRIGGER', tchannel='0', tin='0.0', tout='0.0', tmsHold='100', tafterMute='0')
   MB_XINPUT = ET.SubElement( MacroButton, 'MB_XINPUT', nctrl='0', nbutton='0')
   MB_Name = ET.SubElement( MacroButton, 'MB_Name')
   MB_Name.text = os.path.basename(soundPath[i]) #todo first N letters of File Name
   MB_Subname = ET.SubElement( MacroButton, 'MB_Subname')
   #MB_Subname.text = soundPath[i] # todo remaining N letters of File Name
   MB_InitRequest = ET.SubElement( MacroButton, 'MB_InitRequest')
   MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
   MB_OnRequest.text = 'Load(boardList[BoardLoop]+ os.path.basename(boardList[boardLoop])+".xml")' #path to sound file.mp3
   MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')

def writeBoard():
    buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
    ET.indent(buttonMap, space=" ", level=0)
    buttonMap.write(soundBoardPath + os.path.basename(boardList[boardLoop])+".xml", encoding='utf8', method='xml')
    print("writing button map file: " + soundBoardPath + os.path.basename(boardList[boardLoop])+".xml")

boardList = glob(soundBoardPath + "*" )
i = 0

while i < len(boardList):
   print("found directory " + os.path.basename(boardList[i]))
   #print("writing button map file: " + soundBoardPath + os.path.basename(boardList[i])+".xml")
   i +=1

#board Loop writes each seperate board
boardLoop=0
while boardLoop < len(boardList):
    soundPath = boardList[boardLoop] + "*.*"
    soundList = glob(soundPath)
    indexCounter = 1
    indexNumber = str(indexCounter)
    VBAudioVoicemeeterMacroButtonMap = ET.Element('VBAudioVoicemeeterMacroButtonMap')
    MacroButtonConfiguration = ET.SubElement(VBAudioVoicemeeterMacroButtonMap, 'MacroButtonConfiguration', x0='681', y0='304', dx='873', dy='576')

    boardButtonLoop = 0
    while boardButtonLoop < len(boardList):
        buttonColor=boardButtonColor
        if boardList[boardLoop] == boardList[boardButtonLoop]:
            buttonColor = currentBoardButtonColor
        boardButton()
        indexCounter +=1
        indexNumber = str(indexCounter)
        boardButtonLoop +=1

    soundButtonLoop = 0
    while soundButtonLoop < len(soundList):
       buttonColor=soundButtonColor
       soundButton()
       indexCounter +=1
       indexNumber = str(indexCounter)
       soundButtonLoop +=1
    writeBoard()



#
#   buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
#   ET.indent(buttonMap, space=" ", level=0)
#   buttonMap.write(selfPath+os.path.basename(pathList[i]), encoding='utf8', method='xml')
#   print("button map written to " + path)
