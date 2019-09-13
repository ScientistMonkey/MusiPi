import os
import cgi
from mutagen.id3 import ID3

from pydub import AudioSegment
from pydub.playback import play

listofsongs = []
realnames = []

index = 0


def directorychooser():

    directory="/var/www/html/Music"
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            print(realdir)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)

    song = AudioSegment.from_mp3(listofsongs[0])
    play(song)


directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])

def nextsong(event):
    global index
    index += 1
    if(listofsongs[index]):
        song = AudioSegment.from_mp3(listofsongs[index])
        play(song)
        updatelabel()

def prevsong(event):
    global index
    index -= 1
    if(listofsongs[index]):
        song = AudioSegment.from_mp3(listofsongs[index])
        play(song)
        updatelabel()


def stopsong(event):

    v.set("")
