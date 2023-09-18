#tile.py

import pygame

class Tile():
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
    def process(self, screen, event_list):
        #End updating everything
        screen.blit(self.image, (self.x, self.y))
        
        mouse_motion = None
        
        for event in event_list:    
            if event.type == pygame.MOUSEMOTION:
                mouse_motion = event.rel           
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    if mouse_motion != None:
                        self.rect.move_ip(mouse_motion[0], mouse_motion[1])
                        self.x += mouse_motion[0]
                        self.y += mouse_motion[1]
                    

                
        
        
    