from sense_hat import SenseHat
import json
from time import sleep

sense = SenseHat()

class temperature:
    def __init__(self, temp):
        self.temp = temp
        
        with open('/home/pi/Desktop/SenseHat Code/GitHub Repository/ProgrammingIoT/Assignment 1/config.json') as f:
            data = json.load(f)
            
        self.cold_max = data['cold_max']
        self.comfortable_min = data['comfortable_min']
        self.comfortable_max = data['comfortable_max']
        self.hot_min = data['hot_min']
        
    def compareTemp(self):
        
        blue = (0, 0, 250) #blue
        green = (0, 250, 0) #green
        red = (250, 0, 0) #red
        
        if self.temp <= self.cold_max:
            sense.clear(blue)
        elif self.temp > self.comfortable_min and self.temp < self.comfortable_max:
            sense.clear(green)
        elif self.temp >= self.hot_min:
            sense.clear(red)


while True:
    tempNow = temperature(sense.get_temperature())
    tempNow.compareTemp()
    sleep(10)
    sense.clear()
    sleep(1)
    
