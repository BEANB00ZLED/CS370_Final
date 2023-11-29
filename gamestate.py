#class that governs the state of the game.
class Gamestate():

    #constructor that defaults all values to 0
    def __init__(self):
        self.gamestate = 0
        self.players = 0
        self.round = 0
        self.round_total = 0

    #updates the gamestate depending on the integer passed in
    def updateToGameState(self, integer):
        if integer == 1:
            self.gamestate = 1
    #defines the amount of players and rounds depending on the integer passed in
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
    #returns the current amount of players
    def currentAmountOfPlayers(self):
        return self.players
    #updates the current round and resets it if total is reached
    def updateRound(self):
        self.round = self.round + 1
        if self.round == self.round_total:
            self.round = 0
    #returns current gamestate
    def currentGameState(self):
        return self.gamestate