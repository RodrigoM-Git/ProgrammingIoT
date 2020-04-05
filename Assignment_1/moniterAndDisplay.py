from sense_hat import SenseHat
import json
import time
import os

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
        white = (250, 250, 250) #white
        
        if self.temp <= self.cold_max:
            sense.show_message("Temp=%.1fC" % self.temp, text_colour=white, back_colour=blue)
        elif self.temp > self.comfortable_min and self.temp < self.comfortable_max:
            sense.show_message("Temp=%.1fC" % self.temp, text_colour=white, back_colour=green)
        elif self.temp >= self.hot_min:
            sense.show_message("Temp=%.1fC" % self.temp, text_colour=white, back_colour=red)
        
        
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))


def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
    
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    
    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3


while True:
    temp1 = sense.get_temperature_from_humidity()
    temp2 = sense.get_temperature_from_pressure()
    tempCPU = get_cpu_temp()
    
    temp = (temp1 + temp2) / 2
    realTemp = temp - ((tempCPU - temp) / 1.5)
    realTemp = get_smooth(realTemp)
    
    tempToCompare = temperature(realTemp)
    tempToCompare.compareTemp()
    
    time.sleep(10)
    
    sense.clear()

    
