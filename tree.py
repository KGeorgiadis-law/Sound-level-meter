import sounddevice as sd
from numpy import linalg as LA
import numpy as np

from gpiozero import LEDBoard, PingServer
from signal import pause
from time import sleep
import timeout_decorator

tree = LEDBoard(*range(2,28),pwm=True)

tree[0].pulse(2, 2)

duration = 60  # seconds

def light_up_tree(indata, outdata, frames, time, status):
    volume_norm = int(np.linalg.norm(indata)*10)
    
    max_volume = 100
    
    if volume_norm >= max_volume:
        volume_norm = max_volume
    
    volume_to_leds = int((volume_norm/max_volume)*25)

    print (volume_norm,volume_to_leds)
    
    if volume_to_leds == 0:
        volume_to_leds = 1
    
    for i in range(1, volume_to_leds):
        tree[i].on()
    sleep(0.005)
       
    for i in range(volume_to_leds,25):
        led[i].off()
    sleep(0.001)

with sd.Stream(callback=light_up_tree):
    sd.sleep(duration * 1000)
