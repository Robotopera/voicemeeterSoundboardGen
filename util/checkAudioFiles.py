#utility to check bitrate of sound Files
#voicemeeter will not properly playback files with non-standard bit rates
# standard kbps:
#32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320 kbps

import wave

musicfile = r"C:\Users\rblum\Google Drive\Game Files\soundBoard\Soundboards\Apex\moooore.wav"

track = wave.open(musicfile)
bitrate = track.getframerate() / 1000
print(str(bitrate) + " kbps")
