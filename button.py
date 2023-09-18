import pygame

#Button Class that allows us to create a custom size, color, and text on a button with a custom function.

#Constant white color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Button:
    #Constructor function that sets size, color, function, text, and font size of the button
    def __init__(self, x, y, width, height, text, click_function, color, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.click_function = click_function
        self.color = color
        self.font = pygame.font.Font(None, font_size)

    #process function that takes in the screen from main, draws the button, and checks for a click
    def process(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)

        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.click_function()

