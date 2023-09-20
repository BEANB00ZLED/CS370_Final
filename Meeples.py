import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the game piece class
class Meeples:
    #initializes game peice attributes including position x,y
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        #initializes is dragging false so the peice cant be initally dragged
        self.is_dragging = False

    #this renders the game peice on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    #this allows for the mouse to click and move game peice 
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False

        if self.is_dragging:
            if event.type == pygame.MOUSEMOTION:
                self.rect.centerx, self.rect.centery = event.pos