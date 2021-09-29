import os
import xml.etree.ElementTree as ET

soundList = os.listdir("C:\Users\rblum\Google Drive\Game Files\Sounds & Songs\")


VBAudioVoicemeeterMacroButtonMap = ET.Element('VBAudioVoicemeeterMacroButtonMap')
   MacroButtonConfiguration = ET.SubElement(VBAudioVoicemeeterMacroButtonMap, 'MacroButtonConfiguration', x0='681' y0='304' dx='873' dy='576')

   for i in range (1,80)
      MacroButton = ET.SubElement(MacroButtonConfiguration, 'MacroButton', index='i' type='1' color='3' key='85' ctrl='0' shift='0' alt='0' anyway='0' exclusive='0' trigger='0' xinput='0' )
         MB_MIDI = ET.SubElement( MacroButton, 'MB_MIDI', b1='00' b2='00' b3='00' b4='00' b5='00' b6='00')
         MB_TRIGGER = ET.SubElement( MacroButton, 'MB_TRIGGER', tchannel='0' tin='0.0' tout='0.0' tmsHold='100' tafterMute='0')
         MB_XINPUT = ET.SubElement( MacroButton, 'MB_XINPUT', nctrl='0' nbutton='0')
         MB_Name = ET.SubElement( MacroButton, 'MB_Name')
         MB_Name.text = soundList(i) #first N letters of File Name
         MB_Subname = ET.SubElement( MacroButton, 'MB_Subname')
         MB_Subname.text = soundList(i) ##remaining N letters of File Name
         MB_InitRequest = ET.SubElement( MacroButton, 'MB_InitRequest')
         MB_InitRequest.text = 'Recorder.mode.PlayOnLoad=1'
         MB_OnRequest = ET.SubElement( MacroButton, 'MB_OnRequest')
         MB_OnRequest.text = soundList(i) #path to sound file.mp3
         MB_OffRequest = ET.SubElement( MacroButton, 'MB_OffRequest')

tree.write('output.xml')


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
