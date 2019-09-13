import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *

from sense_hat import SenseHat
from time import sleep
import time

sense = SenseHat()

root = Tk()
root.minsize(300,300)


listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

sense.clear()
volume = 0
paused = False
print("test")
teller = 0

def directorychooser():

    directory = "/home/pi/MusiPi/Music"
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.set_volume(0.20)
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname

def toggle_pause(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
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
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    global teller
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
        # ^^ VERDOMME HET WERKT
        updatelabel()
        # next
    else:
        teller = 0

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
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
    pygame.mixer.music.stop()
    v.set("")
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


def volume_up(event):
    global volume
    if event.action == 'pressed':
        volume += 1
        sense.set_pixel(volume, 3, (255, 255, 255))
        sense.set_pixel(volume, 4, (255, 255, 255))
        getvolume = pygame.mixer.music.get_volume()
        print(getvolume)
        pygame.mixer.music.set_volume(getvolume + 0.16)

def volume_down(event):
    global volume
    if event.action == 'pressed':
        volume -= 1
        sense.set_pixel(volume, 3, (255, 255, 255))
        sense.set_pixel(volume, 4, (255, 255, 255))
        getvolume = pygame.mixer.music.get_volume()
        print(getvolume)
        pygame.mixer.music.set_volume(getvolume - 0.16)


label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()
# realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
# listofsongs.reverse()

sense.stick.direction_middle = toggle_pause
sense.stick.direction_down = volume_down
sense.stick.direction_up = volume_up
sense.stick.direction_right = nextsong
sense.stick.direction_left = prevsong

nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",pausesong)

songlabel.pack()

root.mainloop()
