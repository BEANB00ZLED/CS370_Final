import pygame
from tile import Tile
import button
from deck import Deck

#WHITE = (255, 255, 255)

class Meeples:
    def __init__(self, x, y, width, height, color_key):
        self.color_image = {
            1: 'meeple_character_red.png',
            2: 'meeple_character_green.png',
            3: 'meeple_character_orange.png',
            4: 'meeple_character_blue.png'
        }
        #self.current_color = None
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None
        self.image_set = False # Declare it once, remove the duplicate
        self.color = color_key #set the initial color when created
        self.is_dragging = False # Initialize is_dragging
        #self.should_be_removed = False ##

    def load_image(self):
        if self.color in self.color_image:
            image_path = self.color_image[self.color]
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
            self.image_set = True


    def process(self, screen, event_list, meeple_list):
        self.load_image()  # Load the image with the correct color

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3 and self.image_set:
                    meeple_list.remove(self)
                    self.image = None
                    self.image_set = False
                    #self.should_be_removed = True ##
                elif event.button == 1 and self.rect.collidepoint(event.pos):
                    self.is_dragging = True
                    self.offset_x = event.pos[0] - self.rect.x
                    self.offset_y = event.pos[1] - self.rect.y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_dragging = False

        if self.is_dragging:
            # Update the position of the Meeple while dragging
            self.rect.x, self.rect.y = pygame.mouse.get_pos()
            self.rect.x -= self.offset_x
            self.rect.y -= self.offset_y
        
        if self.should_be_removed:
            meeple_list.remove(self)

        if self.image_set:
            screen.blit(self.image, self.rect.topleft)


