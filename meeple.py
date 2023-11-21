#meeple.py

import pygame

class Meeple:   
    def __init__(self, x, y, file_path):
        self.image = pygame.image.load(file_path)
        self.image = pygame.transform.scale_by(self.image, .15)
        self.x = x - (self.image.get_width() / 2)
        self.y = y - (self.image.get_width() / 2)
        self.show = True
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.delete_sound = pygame.mixer.Sound('Sounds/wilhelmscream.mp3')
        self.__wrap()
    
    def process(self, screen, event_list):
        self.__unwrap()
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #For right click within image detection
                if event.button == 3 and self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.show = False
                    pygame.mixer.Channel(1).play(self.delete_sound)
        self.__wrap()

    #shifts position of meeple
    def shift(self, screen, valueX, valueY):
        self.__unwrap()
        #gets new values
        self.rect.x = self.rect.x + valueX
        self.rect.y = self.rect.y + valueY
        #draws meeple again
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.__wrap()
    
    #Convert data to a string of bytes so that it can be sent over the network
    def __wrap(self):
        self.image = pygame.image.tobytes(self.image, "RGB")
        #self.rect = pygame.image.tostring(self.rect) 
    
    #Convert data from a string of bytes so that it can be used in code
    def __unwrap(self):
        self.image = pygame.image.frombytes(self.image, (self.width, self.height), "RGB")
        #self.rect = pygame.image.fromstring(self.rect)

        