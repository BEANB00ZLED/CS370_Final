import pygame

WHITE = (255, 255, 255)
#RED = (255, 0, 0)

# Define the game piece class
class Meeples:
    #initializes game peice attributes including position x,y
    def __init__(self, x, y, width, height, color):
        self.image = None
        self.rect = pygame.Rect(x, y, width, height)
        #self.rect.topleft = (x, y)
        self.color_image = {
            1: 'meeple_character_red.png',
            2: 'meeple_character_green.png',
            3: 'meeple_character_orange.png',
            4: 'meeple_character_blue.png'
        }
        self.current_color = None
        #initializes is dragging false so the peice cant be initally dragged
        #self.is_dragging = False

    #this renders the game peice on the screen
    #def draw(self, screen):
    def load_image(self, meeple_character):
        self.image = pygame.image.load(meeple_character)
        self.rect = self.image.get_rect()
        

    #this allows for the mouse to click and move game peice 
    def process(self, screen, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN: 
                #if event.button == 1: #and self.rect.collidepoint(event.pos)
                    #screen.blit(self.image, self.rect.topleft)
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    color_key = int(event.unicode)
                    if color_key in self.color_image:
                        self.load_image(self.color_image[color_key])
                        self.current_color = color_key
                    self.rect.topleft = pygame.mouse.get_pos()
        
        if self.current_color is not None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.topleft = (mouse_x, mouse_y)
            #elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #self.is_dragging = False
        if self.image:
            screen.blit(self.image, self.rect.topleft)
            #if self.is_dragging:
                #if event.type == pygame.MOUSEMOTION:
                    #self.rect.centerx, self.rect.centery = event.pos