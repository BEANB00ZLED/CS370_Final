import pygame
import pygame.mixer
from tile import Tile
from deck import Deck
from meeple import Meeple
from network import Network


class Game():
    def __init__(self):
        self.game_deck = Deck()
        self.tile_list = []
        self.meeple_list = []
        
