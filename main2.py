import os
import cgi
from mutagen.id3 import ID3

from sense_hat import SenseHat
from time import sleep
import time

sense = SenseHat()
from pydub import AudioSegment
from pydub.playback import play

listofsongs = []
realnames = []

index = 0

sense.clear()
volume = 0
paused = False
teller = 0

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

def toggle_pause(event):
    global index
    index += 1
    global paused
    global teller
    if teller == 0:
        
        print(paused)
        paused = not paused
        if paused and event.action == 'pressed' and event.direction == 'middle':
            pausesong(event)
        elif event.action == 'pressed' and event.direction == 'middle':
            play(event)
        teller = teller + 1
    else:
        teller = 0


def play(event):
    global index
    index
    pygame.mixer.music.play()
    sense.clear()
    sense.set_pixel(1, 1, (255, 255, 255))
    sense.set_pixel(2, 2, (255, 255, 255))
    sense.set_pixel(1, 2, (255, 255, 255))
    sense.set_pixel(1, 3, (255, 255, 255))
    sense.set_pixel(1, 4, (255, 255, 255))
    sense.set_pixel(1, 5, (255, 255, 255))
    sense.set_pixel(1, 6, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 255, 255))
    sense.set_pixel(2, 3, (255, 255, 255))
    sense.set_pixel(2, 4, (255, 255, 255))
    sense.set_pixel(2, 5, (255, 255, 255))
    sense.set_pixel(2, 6, (255, 255, 255))
    sense.set_pixel(5, 1, (255, 255, 255))
    sense.set_pixel(5, 2, (255, 255, 255))
    sense.set_pixel(5, 3, (255, 255, 255))
    sense.set_pixel(5, 4, (255, 255, 255))
    sense.set_pixel(5, 5, (255, 255, 255))
    sense.set_pixel(5, 6, (255, 255, 255))
    sense.set_pixel(6, 1, (255, 255, 255))
    sense.set_pixel(6, 2, (255, 255, 255))
    sense.set_pixel(6, 3, (255, 255, 255))
    sense.set_pixel(6, 4, (255, 255, 255))
    sense.set_pixel(6, 5, (255, 255, 255))
    sense.set_pixel(6, 6, (255, 255, 255))
    sleep(2)
    sense.clear()
    
    
def nextsong(event):
    global index
    global teller

    index += 1
    if(listofsongs[index]):
        song = AudioSegment.from_mp3(listofsongs[index])
        play(song)
        updatelabel()
    if teller == 0:
        sense.clear()
        sense.set_pixel(0, 1, (255, 255, 255))
        sense.set_pixel(0, 2, (255, 255, 255))
        sense.set_pixel(0, 3, (255, 255, 255))
        sense.set_pixel(0, 4, (255, 255, 255))
        sense.set_pixel(0, 5, (255, 255, 255))
        sense.set_pixel(0, 6, (255, 255, 255))
        sense.set_pixel(1, 2, (255, 255, 255))
        sense.set_pixel(1, 3, (255, 255, 255))
        sense.set_pixel(1, 4, (255, 255, 255))
        sense.set_pixel(1, 5, (255, 255, 255))
        sense.set_pixel(2, 3, (255, 255, 255))
        sense.set_pixel(2, 4, (255, 255, 255))
        sense.set_pixel(5, 1, (255, 255, 255))
        sense.set_pixel(5, 2, (255, 255, 255))
        sense.set_pixel(5, 3, (255, 255, 255))
        sense.set_pixel(5, 4, (255, 255, 255))
        sense.set_pixel(5, 5, (255, 255, 255))
        sense.set_pixel(5, 6, (255, 255, 255))
        sense.set_pixel(6, 2, (255, 255, 255))
        sense.set_pixel(6, 3, (255, 255, 255))
        sense.set_pixel(6, 4, (255, 255, 255))
        sense.set_pixel(6, 5, (255, 255, 255))
        sense.set_pixel(7, 3, (255, 255, 255))
        sense.set_pixel(7, 4, (255, 255, 255))
        teller = teller + 1
        sleep(2)
        sense.clear()
        index -= 1 
        updatelabel()
        # next
    else:
        teller = 0
        
def prevsong(event):
    global index
    index -= 1

    if(listofsongs[index]):
        song = AudioSegment.from_mp3(listofsongs[index])
        play(song)
        updatelabel()


def stopsong(event):

#    pygame.mixer.music.load(listofsongs[index])
 #   pygame.mixer.music.play()
    global teller
    if teller == 0:
        sense.clear()
        sense.set_pixel(0, 3, (255, 255, 255))
        sense.set_pixel(0, 4, (255, 255, 255))
        sense.set_pixel(1, 2, (255, 255, 255))
        sense.set_pixel(1, 3, (255, 255, 255))
        sense.set_pixel(1, 4, (255, 255, 255))
        sense.set_pixel(1, 5, (255, 255, 255))
        sense.set_pixel(2, 1, (255, 255, 255))
        sense.set_pixel(2, 2, (255, 255, 255))
        sense.set_pixel(2, 3, (255, 255, 255))
        sense.set_pixel(2, 4, (255, 255, 255))
        sense.set_pixel(2, 5, (255, 255, 255))
        sense.set_pixel(2, 6, (255, 255, 255))
        sense.set_pixel(5, 3, (255, 255, 255))
        sense.set_pixel(5, 4, (255, 255, 255))
        sense.set_pixel(6, 2, (255, 255, 255))
        sense.set_pixel(6, 3, (255, 255, 255))
        sense.set_pixel(6, 4, (255, 255, 255))
        sense.set_pixel(6, 5, (255, 255, 255))
        sense.set_pixel(7, 1, (255, 255, 255))
        sense.set_pixel(7, 2, (255, 255, 255))
        sense.set_pixel(7, 3, (255, 255, 255))
        sense.set_pixel(7, 4, (255, 255, 255))
        sense.set_pixel(7, 5, (255, 255, 255))
        sense.set_pixel(7, 6, (255, 255, 255))
        teller = teller + 1
        sleep(2)
        index += 1
        sense.clear()
        updatelabel()
    else:
        teller = 0


def pausesong(event):
  #  pygame.mixer.music.stop()
   # v.set("")
    sense.clear()
    sense.set_pixel(1, 0, (255, 255, 255))
    sense.set_pixel(2, 0, (255, 255, 255))
    sense.set_pixel(1, 1, (255, 255, 255))
    sense.set_pixel(1, 2, (255, 255, 255))
    sense.set_pixel(1, 3, (255, 255, 255))
    sense.set_pixel(1, 4, (255, 255, 255))
    sense.set_pixel(1, 5, (255, 255, 255))
    sense.set_pixel(1, 6, (255, 255, 255))
    sense.set_pixel(1, 7, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 255, 255))
    sense.set_pixel(2, 2, (255, 255, 255))
    sense.set_pixel(2, 3, (255, 255, 255))
    sense.set_pixel(2, 4, (255, 255, 255))
    sense.set_pixel(2, 5, (255, 255, 255))
    sense.set_pixel(2, 6, (255, 255, 255))
    sense.set_pixel(2, 7, (255, 255, 255))
    sense.set_pixel(3, 1, (255, 255, 255))
    sense.set_pixel(3, 2, (255, 255, 255))
    sense.set_pixel(3, 3, (255, 255, 255))
    sense.set_pixel(3, 4, (255, 255, 255))
    sense.set_pixel(3, 5, (255, 255, 255))
    sense.set_pixel(3, 6, (255, 255, 255))
    sense.set_pixel(4, 1, (255, 255, 255))
    sense.set_pixel(4, 2, (255, 255, 255))
    sense.set_pixel(4, 3, (255, 255, 255))
    sense.set_pixel(4, 4, (255, 255, 255))
    sense.set_pixel(4, 5, (255, 255, 255))
    sense.set_pixel(4, 6, (255, 255, 255))
    sense.set_pixel(5, 2, (255, 255, 255))
    sense.set_pixel(5, 3, (255, 255, 255))
    sense.set_pixel(5, 4, (255, 255, 255))
    sense.set_pixel(5, 5, (255, 255, 255))
    sense.set_pixel(6, 3, (255, 255, 255))
    sense.set_pixel(6, 4, (255, 255, 255))
    # return songname

def volume_control():
    sense.set_pixel(volume + 1, 3, (255, 255, 255))
    sense.set_pixel(volume + 1, 4, (255, 255, 255))

def volume_up(event):
    global volume
    volume_control()
    if event.action == 'pressed':
        volume += 1

def volume_down(event):
    global volume
    if event.action == 'pressed':
        volume -= 1
        sense.set_pixel(6, 3, 0, 0, 0)
        sense.set_pixel(6, 4, 0, 0, 0)

# listofsongs.reverse()

sense.stick.direction_middle = toggle_pause
sense.stick.direction_down = volume_down
sense.stick.direction_up = volume_up
sense.stick.direction_right = nextsong
sense.stick.direction_left = prevsong
