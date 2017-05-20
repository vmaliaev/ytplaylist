#!/Users/vmaliaev/venv1/bin/python

##!/usr/bin/python

# USAGE: ./dyp.py playlist_url1 playlist_url2 playlist_urlN [ --audioonly | --videoonly | --all ]
import os
import sys
import errno

import pafy
from pydub import AudioSegment

_condit = '--all'

def get_title(arg):
    return pafy.get_playlist(arg)
  
def stru(arg):
#    print arg
    for i in arg:
        print "\n",i
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
        no_list = len(playlist['items'])
        print "Playlist:",title
        print "Items:",no_list

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
        for no,k in enumerate(playlist['items']):
            print 1+no," of ",no_list,":",k['pafy'].title
            if os.path.isfile(newpath_video+"/"+k['pafy'].title+"."+k['pafy'].getbest().extension): print "File video already exists" ;continue
            if _condit in ['--all', '--videoonly']: k['pafy'].getbest().download(filepath=newpath_video) # Video
            if os.path.isfile(newpath_audio+"/"+k['pafy'].title+"."+k['pafy'].getbestaudio().extension): print "File audio already exists" ;continue
            if _condit in ['--all', '--audioonly']: k['pafy'].getbestaudio().download(filepath=newpath_audio) #Audio
 #           break

        if _condit in ['--videoonly']: continue
        print "\nConverting audio..."    
        for (dirp, dirn, f) in os.walk(newpath_audio):
            break
        for fname in f:
            fext = fname.split(".")[-1]
            if fname[0] == '.': continue
            if fname[:-len(fext)]+"mp3" in f: continue
            if fext == "mp3" or fext == "temp" : continue #print fname+"!."+fext
            print fname
            AudioSegment.from_file(newpath_audio+"/"+fname).export(newpath_audio+"/"+fname[:-len(fext)]+"mp3" , format="mp3")


if __name__ == "__main__":

    #Create Folder=Playlist
    #Create Folder=Playlistaudio
    if sys.argv[-1] in ["--audioonly","--videoonly","--all"] : _condit = sys.argv.pop() 
    if sys.argv[-1][0:2] == '--' : print "ERROR: Check argument" ; exit()
    stru(sys.argv[1:])
    #Download all the videos to Playlist Folder
    #Download all the audios to Playlist Folder audio
    #Convert all audio to mp3 
    print "Work completed."

