import glob
import os
import xml.etree.ElementTree as ET
import sys

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
   MB_InitRequest.text = 'Recorder.mode.PlayOnLoad=1'
   MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
   MB_OnRequest.text = 'Recorder.load=' + "\"" +soundPath[i] + "\""  #path to sound file.mp3
   MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')

path = r"C:\Users\rblum\Google Drive\Game Files\soundBoard\Soundboards\Apex\*.*"
soundPath = glob.glob( path )

i = 0
while i < len(soundPath):
#   print(soundPath[i])
   print(os.path.basename(soundPath[i]))
   i = i + 1


VBAudioVoicemeeterMacroButtonMap = ET.Element('VBAudioVoicemeeterMacroButtonMap')
MacroButtonConfiguration = ET.SubElement(VBAudioVoicemeeterMacroButtonMap, 'MacroButtonConfiguration', x0='681', y0='304', dx='873', dy='576')

i = 0
while i < len(soundPath):
   indexNumber = str(i+1)
   soundButton()
   i = i + 1

buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
ET.indent(buttonMap, space=" ", level=0)
buttonMap.write(r'C:\Users\rblum\Google Drive\Game Files\soundBoard\Soundboards\Apex\output.xml', encoding='utf8', method='xml')
print("button map written to " + path)

#Full Example
#<?xml version="1.0" encoding="utf-8"?>
#<VBAudioVoicemeeterMacroButtonMap>
#<MacroButtonConfiguration x0='681' y0='304' dx='873' dy='576' >
#	<MacroButton index='1' type='1' color='3' key='85' ctrl='0' shift='0' alt='0' anyway='0' exclusive='0' trigger='0' xinput='0' >
#		<MB_MIDI b1='00' b2='00' b3='00' b4='00' b5='00' b6='00' />
#		<MB_TRIGGER tchannel='0' tin='0.0' tout='0.0' tmsHold='100' tafterMute='0' />
#		<MB_XINPUT nctrl='0' nbutton='0' />
#		<MB_Name>Milk</MB_Name>
#		<MB_Subname>he need it</MB_Subname>
#		<MB_InitRequest>Recorder.mode.PlayOnLoad=1</MB_InitRequest>
#		<MB_OnRequest>Recorder.load="C:\Users\rblum\Google Drive\Game Files\Sounds & Songs\he-need-some-milk.mp3"</MB_OnRequest>
#		<MB_OffRequest>recorder.stop=1</MB_OffRequest>
#	</MacroButton>
#    macrobuttons 2-80
#</MacroButtonConfiguration>
#</VBAudioVoicemeeterMacroButtonMap>

#load alternate buttons example
#<MacroButton index='1' type='0' color='3' key='85' ctrl='0' shift='0' alt='0' anyway='0' exclusive='0' trigger='0' xinput='0' >
#		<MB_MIDI b1='00' b2='00' b3='00' b4='00' b5='00' b6='00' />
#		<MB_TRIGGER tchannel='0' tin='0.0' tout='0.0' tmsHold='100' tafterMute='0' />
#		<MB_XINPUT nctrl='0' nbutton='0' />
#		<MB_Name>Apex 1</MB_Name>
#		<MB_Subname></MB_Subname>
#		<MB_InitRequest></MB_InitRequest>
#		<MB_OnRequest>Load("C:\Users\rblum\Google Drive\Game Files\soundBoard\Apex\output.xml")</MB_OnRequest>
#		<MB_OffRequest></MB_OffRequest>
#	</MacroButton>
#	<MacroButton index='2' type='0' color='3' key='85' ctrl='0' shift='0' alt='0' anyway='0' exclusive='0' trigger='0' xinput='0' >
#		<MB_MIDI b1='00' b2='00' b3='00' b4='00' b5='00' b6='00' />
#		<MB_TRIGGER tchannel='0' tin='0.0' tout='0.0' tmsHold='100' tafterMute='0' />
#		<MB_XINPUT nctrl='0' nbutton='0' />
#		<MB_Name>Apex 2</MB_Name>
#		<MB_Subname></MB_Subname>
#		<MB_InitRequest></MB_InitRequest>
#		<MB_OnRequest>Load("C:\Users\rblum\Google Drive\Game Files\soundBoard\Apex\output2.xml")</MB_OnRequest>
#		<MB_OffRequest></MB_OffRequest>
#
