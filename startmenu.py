import pygame
import button
#classs that governs the start menu because putting it in main makes it ugly
class Startmenu():

    #constuctor that makes sure the title is set correctly to the screen
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
        self.image = pygame.image.load('MiscAssets/Scroll.png')
        self.arbitrary_number = 30 #funny
        self.image = pygame.transform.scale_by(self.image, .15)
        self.x = (self.screen.get_width() / 2) - (self.image.get_width() / 2)
        self.y = (self.screen.get_height() / 2) - (self.image.get_height() / 2) - self.arbitrary_number

    #draws the start menu when called
    def drawStartMenu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.image, (self.x, self.y))


