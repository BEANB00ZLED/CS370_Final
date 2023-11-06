import pygame
import button

class Startmenu():

    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)
        self.image = pygame.image.load('MiscAssets/Scroll.png')

    def drawStartMenu(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont('', 40,)
        title = font.render('Carcassonne', True, 'gold')
        self.screen.blit(title, (self.screen.get_width() / 2 - title.get_width() / 2, self.screen.get_height() / 2 - title.get_height() / 2))
        self.screen.blit(self.image,  (self.screen.get_width() / 2 - title.get_width() / 2, self.screen.get_height() / 2 - title.get_height() / 2))



