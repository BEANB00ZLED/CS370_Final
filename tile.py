#tile.py

import pygame
from grid import Grid


class Tile():
    #Static variable, keeps track of whether any tile is being moved or not
    cursor_occupied = False
    grid = Grid()

    
    def __init__(self, x, y, image_path):
        self.is_picked_up = False
        self.x = x
        self.y = y
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        
    def process(self, screen, event_list):
        grid_square_size = Tile.grid.sizeBetween(1050, 10)
        for event in event_list:
            #Looking for pressing left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos) and not Tile.cursor_occupied:
                    if self.is_picked_up == False:
                        print("picking up tile: removing point")
                        Tile.grid.removePoint(self.x, self.y)
                    self.is_picked_up = True
                    Tile.cursor_occupied = True
            #Looking for releasing left click
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.is_picked_up:
                    print('tile dropped: adding point')
                    self.x, self.y = Tile.grid.computeSnap(self.x, self.y)
                    self.is_picked_up = False
                    Tile.cursor_occupied = False
            elif event.type == pygame.KEYDOWN:
                #Rotates 90 degrees clockwise if e is pressed
                if event.key == pygame.K_e and self.rect.collidepoint(pygame.mouse.get_pos()) and self.is_picked_up:
                    self.image = pygame.transform.rotate(self.image, -90)
                #Rotates 90 degrees counter clockwise if q is pressed
                elif event.key == pygame.K_q and self.rect.collidepoint(pygame.mouse.get_pos()) and self.is_picked_up:
                    self.image = pygame.transform.rotate(self.image, 90)
                    
            #Handles the movement part if the mouse button is down and no other tiles is being moved   
            if event.type == pygame.MOUSEMOTION and self.is_picked_up:
                self.rect.move_ip(event.rel)
                self.x = self.rect.x
                self.y = self.rect.y
        
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        #Attatch tile to screen
        screen.blit(self.image, (self.x, self.y))

        
                    

                
        
        
    