#button.py

import pygame
import deck
from deck import Deck

#Button Class that allows us to create a custom size, color, and text on a button with a custom function.

#Constant white color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Button:

    button_color = (0, 0, 0)
    #Constructor function that sets size, color, function, text, and font size of the button
    #if you don't want a hover color or click color, then set them the same as color.
    def __init__(self, x, y, width, height, text, click_function, color, hover_color, click_color, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.click_function = click_function
        self.color = color
        self.button_color = color
        self.click_color = click_color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, font_size)
        
    def updateText(self, tiles_left):
        self.text = 'Draw Tile ({})'.format(tiles_left)

    #process function that takes in the screen from main, draws the button, and checks for a click
    def process(self, screen, event_list):
        pygame.draw.rect(screen, self.color, self.rect)
        self.updateText(Deck.tiles_left)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)
        for event in event_list:
            #checks if the button is being hovered and changes the color
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.color = self.hover_color
            else:
                self.color = self.button_color
            #checks if button is clicked and runs the custom function if it is
            #also adds a click color if one is chosen
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
                self.color = self.click_color
                self.click_function()


