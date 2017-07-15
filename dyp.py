#!/Users/vmaliaev/venv1/bin/python

##!/usr/bin/python
# https://github.com/mps-youtube/pafy
# http://pydub.com
# http://stackoverflow.com/questions/38110384/convert-any-audio-file-to-mp3-with-python 



# USAGE: ./dyp.py playlist_url1 playlist_url2 playlist_urlN [ --audioonly | --videoonly | --noTVS | --all ]
import os
import sys
import errno
from shutil import copyfile


import pafy
from pydub import AudioSegment

from converter import Converter
from transliterate import translit, get_available_language_codes

_condit = '--all'
error_list = []

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
        newpath_video_TVS = newpath_video+"/TVS"
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
            os.makedirs(newpath_video_TVS)
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
            try:
                if os.path.isfile(newpath_video+"/"+k['pafy'].title+"."+k['pafy'].getbest().extension): print "File video already exists" #;continue
                else: 
                    if _condit in ['--all', '--videoonly', '--noTVS']: k['pafy'].getbest().download(filepath=newpath_video) # Video

                if _condit not in ['--noTVS','--audioonly']:
                    if os.path.isfile(newpath_video_TVS+"/"+translit(k['pafy'].title,'ru', reversed=True)+"_TVS"+".mp4"): print "File TVS already exists" ;continue
                    copyfile(newpath_video+"/"+k['pafy'].title+"."+k['pafy'].getbest().extension, translit(k['pafy'].title,'ru', reversed=True)+".mp4")
#                    if os.path.isfile(translit(newpath_video_TVS+"/"+k['pafy'].title+"_TVS"+".mp4",'ru', reversed=True)): print "File TVS already exists" ;continue
                    c = Converter()
#                    conv = c.convert(newpath_video+"/"+k['pafy'].title+"."+k['pafy'].getbest().extension, newpath_video_TVS+"/"+k['pafy'].title+"_TVS"+".mp4", {
                    conv = c.convert(translit(k['pafy'].title,'ru', reversed=True)+".mp4",translit(k['pafy'].title,'ru', reversed=True)+"_TVS"+".mp4", {
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


                    copyfile(translit(k['pafy'].title,'ru', reversed=True)+"_TVS"+".mp4", newpath_video_TVS+"/"+translit(k['pafy'].title,'ru', reversed=True)+"_TVS"+".mp4")
                    os.remove(translit(k['pafy'].title,'ru', reversed=True)+"_TVS"+".mp4")                    
                    os.remove(translit(k['pafy'].title,'ru', reversed=True)+".mp4")                    


                if os.path.isfile(newpath_audio+"/"+k['pafy'].title+"."+k['pafy'].getbestaudio().extension): print "File audio already exists" ;continue
                if _condit in ['--all', '--audioonly', '--noTVS']: k['pafy'].getbestaudio().download(filepath=newpath_audio) #Audio
            except IOError as er:
                error_list.append((er, k['pafy'].title))
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
    if sys.argv[-1] in ["--audioonly","--videoonly","--noTVS","--all"] : _condit = sys.argv.pop() 
    if sys.argv[-1][0:2] == '--' : print "ERROR: Check argument" ; exit()
    stru(sys.argv[1:])
    #Download all the videos to Playlist Folder
    #Download all the audios to Playlist Folder audio
    #Convert all audio to mp3 
    for i in error_list: print i[0],"Track:", i[1]
    print "Work completed."


#from converter import Converter
#c = Converter()

#info = c.probe('autonal.mp4')
#print info

#conv = c.convert('Nicki.mp4', 'Noutput.mp4', {
#    'format': 'mp4',
#    'audio': {
#        'codec': 'aac',
#        'bitrate' : 2327925,
#        'channels': 2
#    },
#    'video': {
#        'codec': 'h264',
#        'width': 1280,
#        'height': 720,
#        'fps': 30
#    }})

#for timecode in conv:
#    print "Converting (%f) ...\r" % timecode
