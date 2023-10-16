import pygame


class Grid:

    # uselss constructor
    def __init__(self):
        self.occupied_square = set()

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

    #grabs size between, rounds x and y to nearest grid and returns x and y
    def computeSnap(self, x, y):
        grid_square_size = self.sizeBetween(1050, 10)
        x = ((round(x / grid_square_size)) * grid_square_size)
        y = ((round(y / grid_square_size)) * grid_square_size)
        return x, y
