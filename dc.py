#!/Users/vmaliaev/venv1/bin/python

##!/usr/bin/python
import sys
import os
import errno
import pafy
from pydub import AudioSegment

# plurl = "https://www.youtube.com/playlist?list=PLC38Xa1H2ja2qU1LSzOHMfI7MFMkXHIjq"
# >>> playlist = pafy.get_playlist(plurl)
# >>> for i in playlist['items']: i['pafy'].getbestaudio().download()

# >>> from pydub import AudioSegment
# >>> AudioSegment.from_file("Life Begins at the End of Your Comfort Zone | Yubing Zhang | TEDxStanford.opus").export("test-11.mp3",format="mp3")


def get_title(arg):
    return pafy.get_playlist(arg)
  
def stru(arg):
#    print arg
    for i in arg:
        print i
        playlist = get_title(i)
        title = playlist["title"]
        print "Title=",title
        try:
            os.makedirs("Playlist="+title)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        try:
            os.makedirs("Playlist="+title+"/audio")
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
#        for k in playlist['items']: k['pafy'].getbestaudio().download()

if __name__ == "__main__":

    #Create Folder=Playlist
    #Create Folder=Playlistaudio
    stru(sys.argv[1:])
    #Download all the videos to Playlist Folder
    #Download all the audios to Playlist Folder audio
    #Convert all audio to mp3 


