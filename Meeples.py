import pygame

WHITE = (255, 255, 255)
#RED = (255, 0, 0)

# Define the game piece class
class Meeples:
    #initializes game peice attributes including position x,y
    def __init__(self, x, y, width, height, color_key):
        #self.image = None
        #self.rect = pygame.Rect(x, y, width, height)
        #self.rect.topleft = (x, y)
        self.color_image = {
            1: 'meeple_character_red.png',
            2: 'meeple_character_green.png',
            3: 'meeple_character_orange.png',
            4: 'meeple_character_blue.png'
        }
        self.current_color = None
        self.rect = pygame.Rect(0, 0, width, height)
        self.image = None
        self.image_set = False
        self.rect.topleft = (x, y)
        #added new code here:
        #if color_key in self.color_image:
           #self.load_image(self.color_image[color_key])
        #initializes is dragging false so the peice cant be initally dragged
        #self.is_dragging = False
    
    #this renders the game peice on the screen
    #def draw(self, screen):
    def load_image(self, meeple_character):
        self.image = pygame.image.load(meeple_character)
        #scale meeple down 
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        #self.rect = self.image.get_rect()
        #self.image_set = True
        self.image_set = False

    #this allows for the mouse to click and move game peice 
    def process(self, screen, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN: 
                #if event.button == 1: #and self.rect.collidepoint(event.pos)
                    #screen.blit(self.image, self.rect.topleft)
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    #color_key = int(event.unicode)
                    color_key = event.key - pygame.K_1 + 1
                    if color_key in self.color_image:
                        self.load_image(self.color_image[color_key])
                        self.current_color = color_key
                        #set the position to the current mouse postition
                        #self.rect.topleft = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN: #and event.button == 1 and not self.image_set:
                if event.button == 1: #and not self.image_set:
                 self.rect.topleft = pygame.mouse.get_pos()
                 #replaced by code above#meeple = Meeples(0, 0, self.rect.width, self.rect.height, self.current_color)
                 self.image_set = True
                 #repalced by code above#meeple.rect.topleft = pygame.mouse.get_pos()
                 #mouse_x, mouse_y = pygame.mouse.get_pos()
                 self.meeple_list.append(self)
                 ##self.rect.topleft = pygame.mouse.get_pos()
                 #Left -click places the meeple image at the current mouse potion
                 ##screen.blit(self.image, self.rect.topleft)
                 ##self.image_set = True
                elif event.button == 3: # and self.image_set:
                    self.meeple_list = [m for m in self.meeple_list if not m.rect.collidepoint(event.pos)]
                    #rght click: delete the meeple image if it's already placed
                    ##self.image = None
                    ##self.image_set = False
        if self.image_set:
            screen.blit(self.image, self.rect.topleft)
        '''if self.current_color is not None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.topleft = (mouse_x, mouse_y)
            #elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #self.is_dragging = False'''
        for meeple in self.meeple_list:
            if self.image and not self.image_set:
                screen.blit(meeple.image, meeple.rect.topleft)
            #if self.is_dragging:
                #if event.type == pygame.MOUSEMOTION:
                    #self.rect.centerx, self.rect.centery = event.pos