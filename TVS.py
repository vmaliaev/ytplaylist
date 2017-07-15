#!/Users/vmaliaev/venv1/bin/python

# USAGE: ./TVS.py video_file
import os
import sys
from shutil import copyfile


from converter import Converter
from transliterate import translit, get_available_language_codes



if len(sys.argv[:])<2: exit(0)
oname = translit(unicode(sys.argv[1], "utf-8"),'ru', reversed=True)+"_TVS"

copyfile(sys.argv[1], oname)
c = Converter()
conv = c.convert(oname,oname+".mp4", {
'format': 'mp4',
'audio': {
    'codec': 'aac',
    'bitrate' : 2327925,
    'channels': 2
},
'video': {
    'codec': 'h264',
    'width': 1280,
    'height': 720,
    'fps': 30
}})

for timecode in conv:
    print "\033[K", "Converting for TVS (%f) ...\r" % timecode, "\r",
    sys.stdout.flush()

os.remove(oname)
