from Player import Player
from ElectronicDie import ElectronicDie
from sense_hat import SenseHat
import time
import csv

sense = SenseHat()

Die = ElectronicDie()
Player1 = Player(1)
Player2 = Player(2)

startTime = time.time()
finalTime = None
winner = None

while Player1.getPoints() < 30 or Player2.getPoints() < 30:
    sense.show_message("Player 1 Roll", scroll_speed=0.05)
    checked = False
    while checked is False:
        number1 = Die.roll()
        if number1 is not None:
            sense.show_message(str(number1))
            Player1.addPoints(number1)
            checked = True
            
    if Player1.getPoints() > 30:
        sense.show_message("Player 1 Wins!", scroll_speed=0.05)
        endTime = time.time()
        finalTime = round(endTime - startTime, 2)
        winner = Player1
        break
    
    sense.show_message("Player 2 Roll", scroll_speed=0.05)
    checked = False
    while checked is False:
        number2 = Die.roll()
        if number2 is not None:
            sense.show_message(str(number2))
            Player2.addPoints(number2)
            checked = True
    
    if Player2.getPoints() > 30:
        sense.show_message("Player 2 Wins!", scroll_speed=0.05)
        endTime = time.time()
        finalTime = round(endTime - startTime,2)
        winner = Player2
        break
    
        
with open('winner.csv', mode='a') as winners_file:
    file_writer = csv.writer(winners_file, delimiter=':')
    file_writer.writerow([winner.getID(), "Points-" + str(winner.getPoints()), "Time-" + str(finalTime) + "s"])