class Player:
    def __init__(self, playerNumber):
        self.playerNumber = playerNumber
        self.points = 0
        
    def addPoints(self, points):
        self.points += points
        
    def getPoints(self):
        return self.points
    
    def getID(self):
        return "Player-" + str(self.playerNumber)