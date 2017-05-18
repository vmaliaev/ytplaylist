#!/Users/vmaliaev/venv1/bin/python

##!/usr/bin/python
import os
import sys
import errno

import pafy
from pydub import AudioSegment


def get_title(arg):
    return pafy.get_playlist(arg)
  
def stru(arg):
#    print arg
    for i in arg:
        print i
        try:
            playlist = get_title(i)
        except ValueError as e:
            print "\nERROR: Check url: "+i
            print e
            print "Continue next playlist\n"
            break
        title = playlist["title"]
        newpath_video = "Playlist="+title
        newpath_audio = newpath_video+"/audio"
        print "Playlist:",title
        try:
            os.makedirs(newpath_video)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        try:
            os.makedirs(newpath_audio)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        for k in playlist['items']:
            print k['pafy'].title
            if os.path.isfile(newpath_audio+"/"+k['pafy'].title+"."+k['pafy'].getbestaudio().extension): print "File already exists" ;continue
            k['pafy'].getbest().download(filepath=newpath_video)
            k['pafy'].getbestaudio().download(filepath=newpath_audio)
            break
            
        for (dirp, dirn, f) in os.walk(newpath_audio):
            break
        for fname in f:
            fext = fname.split(".")[-1]
            if fext == "mp3" and fext == "temp" : continue #print fname+"!."+fext
            AudioSegment.from_file(newpath_audio+"/"+fname).export(newpath_audio+"/"+fname[:-len(fext)]+"mp3" , format="mp3")

if __name__ == "__main__":

    #Create Folder=Playlist
    #Create Folder=Playlistaudio
    stru(sys.argv[1:])
    #Download all the videos to Playlist Folder
    #Download all the audios to Playlist Folder audio
    #Convert all audio to mp3 


