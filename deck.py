import os

import pygame
import numpy as np
from tile import Tile

#Deck class that will allow for the shuffling, drawing, and storing of tiles
class Deck:

    #Shuffles the Deck
    def shuffle(self):
        np.random.shuffle(self.game_deck)

    #constructor that loads the tiles into an array
    def __init__(self):
        self.game_deck = []

        for i in (os.listdir('TileAssets')):
            i = "TileAssets\\{}".format(i)
            print(i)
            for j in range(int(i[-5])):
                print(j)
                self.game_deck.append(Tile(500,500, i))

        self.shuffle()

    #pops the tile on the bottom of the array out, shifting everything over, and returns it.
    def drawTile(self):
        drawnTile = self.game_deck.pop(0)
        print("drawn tile", drawnTile)
        return drawnTile



