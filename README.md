# Download playlists from YOUTxBx 
 You can easily download video/audio playlists and convert tracks to mp3

## USAGE:
 Just create your own playlists on youtxbx or take other's public playlists and copypast their URLs:
```
 ./dyp.py playlist1_url [ playlis2_url ... playlistN_url ] [ --all | --audioonly | --videoonly ]

 playlistX_url - just a playlist link in format like  https://www.yXXtXbX.com/playlist?list=PLC38Xa1H2ja2Vl14wKQedQ7n7vLr_OOcw
 --audioonly - download only audio 
 --videoonly - download only video
 --all - download both, this is default
```

### INSTALLATION:
 There are no specific requirements to install the script, you just need to have several additional modules installed in virtual environment or wide-system.

 If you want to install venv: 
 `curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz # X - is a preferable version number`

 Example:

```curl -O https://pypi.python.org/packages/d4/0c/9840c08189e030873387a73b90ada981885010dd9aea134d6de30cd24cb8/virtualenv-15.1.0.tar.gz#md5=44e19f4134906fe2d75124427dc9b716

 tar xvfz virtualenv-15.1.0.tar.gz#md5\=44e19f4134906fe2d75124427dc9b716

 virtualenv venv1

 source venv1/bin/activate 
```
 Inside virtual environment run: 
```
 pip install pafy
 pip install youtube-dl # This is preferable backend for pafy
 pip install pydub # To convert audio tracks
 ? pip install ffmpeg
 ? pip install avconv
 ? apt-get install ffmpeg
```
