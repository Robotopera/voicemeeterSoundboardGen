#utility to check bitrate of sound Files
#voicemeeter will not properly playback files with non-standard bit rates
# standard kbps:
#32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320 kbps

from mutagen.mp3 import MP3

f = MP3(musicfile)
bitrate = f.info.bitrate / 1000
