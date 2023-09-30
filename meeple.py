#meeple.py

import pygame

class Meeple:
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.show = True
        
    def __del__(self):
        pass
        
    
    def process(self, screen, eventlist) -> None:
        circle = pygame.draw.circle(surface=screen, color=self.color, center=(self.x, self.y), radius=12.5)
        for event in eventlist:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                #For right click
                if event.button == 3 and circle.collidepoint(event.pos):
                    self.show = False