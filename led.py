from sense_hat import SenseHat
from time import sleep
import time

#variabels
sense = SenseHat()
sense.clear()
volume = 0
paused = False
print("test")
teller = 0

#functies

def pause():
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
    

def toggle_pause(event):
    global paused
    global teller
    if teller == 0:
        
        print(paused)
        paused = not paused
        if paused and event.action == 'pressed' and event.direction == 'middle':
            pause()
        elif event.action == 'pressed' and event.direction == 'middle':
            play()
        teller = teller + 1
    else:
        teller = 0
    
    

def play():
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
    sleep(2)
    sense.clear()


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

def next_track():
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
    else:
        teller = 0



def previous_track():
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
        sense.clear()
    else:
        teller = 0
    

        
    #programma
    
    
sense.stick.direction_middle = toggle_pause
sense.stick.direction_down = volume_down
sense.stick.direction_up = volume_up
sense.stick.direction_right = next_track
sense.stick.direction_left = previous_track

while True:
    sleep(1)
