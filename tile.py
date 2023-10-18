#tile.py

import pygame
import os

class Tile():
    #Static variable, keeps track of whether any tile is being moved or not
    cursor_occupied = False
    
    def __init__(self, x, y, tile_folder):
        self.is_picked_up = False
        self.x = x
        self.y = y
        self.tile_folder = tile_folder
        self.frames = []
        self.current_frame = 0
        for i in os.listdir(self.tile_folder):
            file = self.tile_folder + "/" + i
            self.frames.append(pygame.image.load(file))
        self.width = self.frames[self.current_frame].get_width()
        self.height = self.frames[self.current_frame].get_height()
        self.rect = self.frames[self.current_frame].get_rect(topleft=(self.x, self.y))
    
    #The double underscore sorta makes it private, cuz abstraction n stuff
    def __rotate(self, clockwise: bool):
        if clockwise:
            self.current_frame += 1
        else:
            self.current_frame -= 1
        #Prevent out of bound, implement circular looping through list
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        elif self.current_frame < 0:
            self.current_frame = len(self.frames) -1
        
    def process_input(self, event_list):
        for event in event_list:
            #Looking for pressing left click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint(event.pos) and not Tile.cursor_occupied:
                    self.is_picked_up = True
                    Tile.cursor_occupied = True
            #Looking for releasing left click
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_picked_up = False
                    Tile.cursor_occupied = False
            elif event.type == pygame.KEYDOWN:
                #Rotates 90 degrees clockwise if e is pressed
                if event.key == pygame.K_e and self.rect.collidepoint(pygame.mouse.get_pos()) and self.is_picked_up:
                    self.__rotate(clockwise=True)
                #Rotates 90 degrees counter clockwise if q is pressed
                elif event.key == pygame.K_q and self.rect.collidepoint(pygame.mouse.get_pos()) and self.is_picked_up:
                    self.__rotate(clockwise=False)
                    
            #Handles the movement part if the mouse button is down and no other tiles is being moved   
            if event.type == pygame.MOUSEMOTION and self.is_picked_up:
                self.rect.move_ip(event.rel)
                self.x = self.rect.x
                self.y = self.rect.y

    def draw(self, screen):
        #Attatch tile to screen
        screen.blit(self.frames[self.current_frame], (self.x, self.y))

        
                    

                
        
        
    