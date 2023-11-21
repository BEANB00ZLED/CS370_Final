import pygame

pygame.mixer.init()
tile_rotate_sound = pygame.mixer.Sound('Sounds/stonerotate.mp3')
tile_drop_sound = pygame.mixer.Sound('Sounds/stone-dropping-6843.mp3')
tile_drop_sound.set_volume(.6)
meeple_delete_sound = pygame.mixer.Sound('Sounds/wilhelmscream.mp3')
