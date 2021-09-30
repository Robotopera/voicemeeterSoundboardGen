import configparser
from glob import glob
import os

configparser = configparser.RawConfigParser()
configFilePath = 'config.txt'
configparser.read(configFilePath)
selfPath = configparser.get('Config File', 'soundBoardPath')
print(selfPath)

pathList = glob(selfPath + "*" )
i = 0

while i < len(pathList):
   print("found directory " + os.path.basename(pathList[i]))
   print("writing button map file: " + selfPath + os.path.basename(pathList[i])+".xml")
   i +=1

#while i < len(pathList):
#   VBAudioVoicemeeterMacroButtonMap = ET.Element('VBAudioVoicemeeterMacroButtonMap')
#   MacroButtonConfiguration = ET.SubElement(VBAudioVoicemeeterMacroButtonMap, 'MacroButtonConfiguration', x0='681', y0='304', dx='873', dy='576')
#   buttonMap = ET.ElementTree(VBAudioVoicemeeterMacroButtonMap)
#   ET.indent(buttonMap, space=" ", level=0)
#   buttonMap.write(selfPath+os.path.basename(pathList[i]), encoding='utf8', method='xml')
#   print("button map written to " + path)
