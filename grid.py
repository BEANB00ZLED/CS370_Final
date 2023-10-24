import pygame
import numpy as np
from enum import Enum
from operator import add

class Grid:
    occupied_coords = []
    
    class Directions(Enum):
        N = [0, -1]
        NE = [1, -1]
        E = [1, 0]
        SE = [1, 1]
        S = [0, 1]
        SW = [-1, 1]
        W = [-1, 0]
        NW = [-1, -1]
    
    # uselss constructor
    def __init__(self):
        #Size of tile images approx
        self.SIZE = 105

    # draws the grid
    def drawGrid(self, w, rows, surface):
        # calculates the size between squares
        size_between = w // rows
        # draws the lines
        for i in range(0, w, size_between):
            x, y = i, i
            pygame.draw.line(surface, 'black', (x, 0), (x, w))
            pygame.draw.line(surface, 'black', (0, y), (w, y))

    #calculates the size between squares.
    def sizeBetween(self, w, rows):
        size_between = w // rows
        return size_between
    
    #Removes coordinate from 
    def removePoint(self, x, y):
        if [x, y] in Grid.occupied_coords:
            Grid.occupied_coords.remove([x, y])
        print(Grid.occupied_coords) 
    
    def computeNearest(self, x, y):
        #Prevent tile stacking
        #Only checks clockwise in 8 compass directions for nearest open square
        magnitude = 1
        while [x, y] in Grid.occupied_coords:
            for i in Grid.Directions:
                print('Direction: ',i)
                delta = [i.value[0] * self.SIZE * magnitude, i.value[1] * self.SIZE * magnitude]
                print(delta)
                print('Delta: ', delta)
                result = list(map(add, [x, y], delta))
                print('Result: ', result)
                if (result) not in Grid.occupied_coords:
                    return x + delta[0], y + delta[1]
            magnitude += 1
        return x, y
    
    #grabs size between, rounds x and y to nearest grid and returns x and y
    def computeSnap(self, x, y):
        x = self.SIZE * round(x / self.SIZE)
        y = self.SIZE * round(y / self.SIZE)
        if [x, y] in Grid.occupied_coords:
            x, y =  self.computeNearest(x, y)
        Grid.occupied_coords.append([x, y])
        print(Grid.occupied_coords)
        return x, y
