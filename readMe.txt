Tool to generate xml button map from a directory of sound files & folders for Voicemeeter Macro Buttons

edit config file to directory with soundboard folders

example: ~\user\Google Drive\Game Files\soundBoard\Soundboards\

program will generate soundboards based on folders located in sound directory

example folder structure:
...\Soundboards\Apex\(sound files)
...\Soundboards\Tarkov\(sound files)
...\Soundboards\Valheim\(sound files)

example output:

...\Soundboards\Apex.xml
...\Soundboards\Tarkov.xml
...\Soundboards\Valheim.xml

Soundboards will have a button to switch between boards.
hotkeys start at F13

Ref
https://docs.python.org/3/library/xml.etree.elementtree.html
