import configparser
from glob import glob
import os

configparser = configparser.RawConfigParser()
configFilePath = 'config.txt'
configparser.read(configFilePath)
selfPath = configparser.get('Config File', 'soundBoardPath')
print(selfPath)

def soundButton():
   MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index=indexNumber, type='0', color='3', key='85', ctrl='0', shift='0', alt='0', anyway='0', exclusive='0', trigger='0', xinput='0' )
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
   MB_OnRequest.text = 'Recorder.load=' + "\"" +soundPath[i] + "\""  #path to sound file.mp3
   MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')

def boardButton():
   MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index=indexNumber, type='0', color='3', key='85', ctrl='0', shift='0', alt='0', anyway='0', exclusive='0', trigger='0', xinput='0' )
   MB_MIDI = ET.SubElement( MacroButton, 'MB_MIDI', b1='00', b2='00', b3='00', b4='00', b5='00', b6='00')
   MB_TRIGGER = ET.SubElement( MacroButton, 'MB_TRIGGER', tchannel='0', tin='0.0', tout='0.0', tmsHold='100', tafterMute='0')
   MB_XINPUT = ET.SubElement( MacroButton, 'MB_XINPUT', nctrl='0', nbutton='0')
   MB_Name = ET.SubElement( MacroButton, 'MB_Name')
   MB_Name.text = os.path.basename(soundPath[i]) #todo first N letters of File Name
   MB_Subname = ET.SubElement( MacroButton, 'MB_Subname')
   #MB_Subname.text = soundPath[i] # todo remaining N letters of File Name
   MB_InitRequest = ET.SubElement( MacroButton, 'MB_InitRequest')
   MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
   MB_OnRequest.text = 'Load(soundPath

   load xml files here

   )'  #path to sound file.mp3
   MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')


pathList = glob(selfPath + "*" )
i = 0

while i < len(pathList):
   print("found directory " + os.path.basename(pathList[i]))
   print("writing button map file: " + selfPath + os.path.basename(pathList[i])+".xml")
   i +=1

#board Loop writes each seperate board
boardLoop=0
while boardLoop < len(pathList):
    indexCounter = 1
    indexNumber = str(indexCounter)
    VBAudioVoicemeeterMacroButtonMap = ET.Element('VBAudioVoicemeeterMacroButtonMap')
    MacroButtonConfiguration = ET.SubElement(VBAudioVoicemeeterMacroButtonMap, 'MacroButtonConfiguration', x0='681', y0='304', dx='873', dy='576')
    boardButtonLoop = 0
    while boardButtonLoop < len(pathList):
        boardButton()
        indexCounter +=1
        indexNumber = str(indexCounter)

#
#   buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
#   ET.indent(buttonMap, space=" ", level=0)
#   buttonMap.write(selfPath+os.path.basename(pathList[i]), encoding='utf8', method='xml')
#   print("button map written to " + path)
