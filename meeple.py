#meeple.py

import pygame

class Meeple:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.show = True    
    
    def process(self, screen, event_list):
        circle = pygame.draw.circle(surface=screen, color=self.color, center=(self.x, self.y), radius=12.5)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                #For right click
                if event.button == 3 and circle.collidepoint(event.pos):
                    self.show = False