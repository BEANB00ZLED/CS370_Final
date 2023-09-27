import pygame

WHITE = (255, 255, 255)
#RED = (255, 0, 0)

# Define the game piece class
class Meeples:
    #initializes game peice attributes including position x,y
    def __init__(self, x, y, meeple_character):
        self.image = pygame.image.load(meeple_character)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        #initializes is dragging false so the peice cant be initally dragged
        #self.is_dragging = False

    #this renders the game peice on the screen
    #def draw(self, screen):
        

    #this allows for the mouse to click and move game peice 
    def process(self, screen, event_list):
      
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: #and self.rect.collidepoint(event.pos)
                    screen.blit(self.image, self.rect.topleft)
            #elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #self.is_dragging = False

            #if self.is_dragging:
                #if event.type == pygame.MOUSEMOTION:
                    #self.rect.centerx, self.rect.centery = event.pos