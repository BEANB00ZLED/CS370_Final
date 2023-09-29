import pygame

WHITE = (255, 255, 255)

class Meeples:
    def __init__(self, x, y, width, height, color_key):
        self.color_image = {
            1: 'meeple_character_red.png',
            2: 'meeple_character_green.png',
            3: 'meeple_character_orange.png',
            4: 'meeple_character_blue.png'
        }
        self.current_color = None
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None
        self.image_set = False

    def load_image(self, meeple_character):
        self.image = pygame.image.load(meeple_character)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.image_set = True

    def place_meeple(self, color_key):
        if color_key in self.color_image:
            self.current_color = color_key
            self.load_image(self.color_image[color_key])
    
        self.is_dragging = False
        self.offset_x = 0
        self.offset_y = 0

    def process(self, screen, event_list, meeple_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    self.place_meeple(event.key - pygame.K_1 + 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3 and self.image_set:
                    meeple_list.remove(self)
                    self.image = None
                    self.image_set = False
                elif event.button == 1 and self.rect.collidepoint(event.pos):
                    self.is_dragging = True
                    self.offset_x = event.pos[0] - self.rect.x
                    self.offset_y = event.pos[1] - self.rect.y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_dragging = False

        if self.is_dragging:
            # Update the position of the Meeple while dragging
            self.rect.x, self.rect.y = pygame.mouse.get_pos()
            self.rect.x -= self.offset_x
            self.rect.y -= self.offset_y
        elif self.image_set:
            screen.blit(self.image, self.rect.topleft)


