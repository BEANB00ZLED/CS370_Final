#tile.py

import pygame

class Tile():
    #Static variable
    is_picked_up = False
    
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
    def process(self, screen, event_list):
        for event in event_list:          
            #Looking for pressing left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    Tile.is_picked_up = True
            #Looking for releasing left click
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.rect.collidepoint(event.pos):
                    Tile.is_picked_up = False
            elif event.type == pygame.KEYDOWN:
                #Rotates 90 degrees clockwise if e is pressed
                if event.key == pygame.K_e:
                    self.image = pygame.transform.rotate(self.image, -90)
                #Rotates 90 degrees counter clockwise if q is pressed
                elif event.key == pygame.K_q:
                    self.image = pygame.transform.rotate(self.image, 90)
                    
            #Looking for mouse movement    
            if event.type == pygame.MOUSEMOTION and Tile.is_picked_up:
                self.rect.move_ip(event.rel)
                self.x = self.rect.x
                self.y = self.rect.y
                
                    
                    
        #Attatch tile to screen
        screen.blit(self.image, (self.x, self.y))
        
                    

                
        
        
    