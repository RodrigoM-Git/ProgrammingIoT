from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = (250, 250, 0) #yellow
bl = (0, 0, 250) #blue
r = (250, 0, 0) #red
b = (0, 0, 0) #black

class emoji():
    
    def getHappy(self, color):
        c = color
        
        face = [
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, b, b, c, c, b, b, c,
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, c, c, b, b, c, c, c,
            c, c, c, c, c, c, c, c
        ] 
        return face

    def getSad(self, color):
        c = color
        
        face = [
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, b, b, c, c, b, b, c,
            c, c, c, c, c, c, c, c,
            c, c, c, b, b, c, c, c,
            c, b, b, c, c, b, b, c,
            c, c, c, c, c, c, c, c
        ]
        return face
    
    def getWink(self, color):
        c = color
        
        face = [
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, c, c, c,
            c, b, b, c, c, c, c, c,
            c, b, b, c, c, b, b, c,
            c, c, c, c, c, c, c, c,
            c, c, c, c, c, b, b, c,
            c, b, b, b, b, c, c, c,
            c, c, c, c, c, c, c, c
        ] 
        return face
     
    
while True:
    happy = emoji()
    sad = emoji()
    wink = emoji()
    
    sense.set_pixels(happy.getHappy(y))
    sleep(3)
    sense.set_pixels(sad.getSad(r))
    sleep(3)
    sense.set_pixels(wink.getWink(bl))
    sleep(3)
    
    
    
    
    
