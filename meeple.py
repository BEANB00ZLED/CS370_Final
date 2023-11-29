#meeple.py

import pygame

class Meeple:   
    def __init__(self, x, y, file_path):
        self.image = pygame.image.load(file_path)
        #Make the image smaller
        self.image = pygame.transform.scale_by(self.image, .15)
        self.x = x - (self.image.get_width() / 2)
        self.y = y - (self.image.get_width() / 2)
        self.show = True
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.delete_sound = pygame.mixer.Sound('Sounds/wilhelmscream.mp3')
        self.meeple_spawn_sound = pygame.mixer.Sound('Sounds/horn-89801.mp3')
        pygame.mixer.Channel(1).play(self.meeple_spawn_sound)
    
    def process(self, screen, event_list):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #For right click within image detection
                if event.button == 3 and self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.show = False
                    pygame.mixer.Channel(1).play(self.delete_sound)

    #shifts position of meeple
    def shift(self, screen, valueX, valueY):
        #gets new values
        self.rect.x = self.rect.x + valueX
        self.rect.y = self.rect.y + valueY
        #draws meeple again
        screen.blit(self.image, (self.rect.x, self.rect.y))

        