from sense_hat import SenseHat
import random

sense = SenseHat()
sense.set_imu_config(False, False, True)


class ElectronicDie:
    
    def roll(self):
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)
        
        if x > 3 or y > 3 or z > 3:
            number = random.randint(1,6)
            return number
            