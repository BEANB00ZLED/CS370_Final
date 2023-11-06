class Gamestate():

    def __init__(self):
        self.gamestate = 0
        self.players = 0
        self.round = 0
        self.round_total = 0

    def updateToGameState(self, integer):
        if integer == 1:
            self.gamestate = 1
        return self.gamestate

    def amountOfPlayers(self, integer):
        if integer == 2:
            self.players = 2
            self.round_total = 2
        elif integer == 3:
            self.players = 3
            self.round_total = 3
        elif integer == 4:
            self.players = 4
            self.round_total = 4

    def currentAmountOfPlayers(self):
        return self.players

    def updateRound(self):
        self.round = self.round + 1
        if self.round == self.round_total:
            self.round = 0
            
    def currentGameState(self):
        return self.gamestate