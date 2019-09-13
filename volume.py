import pyaudio
import pygame
import numpy as np

CHUNK = 2**11
RATE = 44100


p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

for i in range(int(1000*44100/1024)): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    volume = int(50*peak/2**16)
    print(volume)
    bars="#"*int(50*peak/2**16)
    


while True:
    
    sleep(1)
    if volume <= 5:
        pygame.mixer.music.set_volume(0.2)

    if volume >=6 and volume <=10:
        pygame.mixer.music.set_volume(0.36)

    if volume >=11 and volume <=15:
        pygame.mixer.music.set_volume(0.52)

    if volume >=16 and volume <=20:
        pygame.mixer.music.set_volume(0.68)

    if volume >=21 and volume <=25:
        pygame.mixer.music.set_volume(0.84)

    if volume >=26:
        pygame.mixer.music.set_volume(1.0)


    
        
stream.stop_stream()
stream.close()
p.terminate()

#install pulseaudio
#install sounddevice
#install libasound2-dev
#install alsaaudio

