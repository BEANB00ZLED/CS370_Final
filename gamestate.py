class Gamestate():

    def __init__(self):
        self.gamestate = 0

    def updateToGameState(self, integer):
        if integer == 1:
            self.gamestate = 1
        return self.gamestate

    def currentGameState(self):
        return self.gamestate