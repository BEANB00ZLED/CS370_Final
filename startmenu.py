import pygame
import button

class Startmenu():

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
        self.image = pygame.image.load('MiscAssets/Scroll.png')
        self.arbitrary_number = 30
        self.image = pygame.transform.scale_by(self.image, .15)
        self.x = (self.screen.get_width() / 2) - (self.image.get_width() / 2)
        self.y = (self.screen.get_height() / 2) - (self.image.get_height() / 2) - self.arbitrary_number

    def drawStartMenu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.image, (self.x, self.y))


