#!/Users/vmaliaev/venv1/bin/python

#!#/usr/bin/env python

#USAGE: ./ht_cut.py [ cut seconds from begin [ cut seconds from end ]]
#       ./ht_cut.py 12 3 

import sys
from pydub import AudioSegment


def slice(arg):
    print "Slicing"
    track = AudioSegment.from_mp3(arg[0])
    
    first_sec = arg[1] + "000"
    last_sec  = 0
#    print arg[2]
    if len(arg)>2: last_sec = arg[2] + "000"
    
    print first_sec
    print int(last_sec)

    if int(last_sec) == 0:
        modified = track[int(first_sec):]
    else:
        modified = track[int(first_sec):-int(last_sec)]

    modified.export("testcut.mp3", format="mp3")




if __name__ == "__main__":
    if sys.argv[2:] == [] : print "Error: check arguments" ; exit()
    slice(sys.argv[1:])
    print "Finish"
