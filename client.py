import pygame
import pygame.mixer
from tile import Tile
import button
from deck import Deck
from meeple import Meeple
from network import Network

def main():
    #Create out network
    n = Network()  
            
    #Initialize pygame module
    pygame.init()

    #Initalize the mizer for sound effect
    pygame.mixer.init()
    
    #Set window size
    screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    #Set window icon
    pygame.display.set_icon(pygame.image.load('MiscAssets/CarcasonneLogoTransparentBackground.png'))
    
    #For if game is running
    running = True

    #Loads in audio samples 
    meeple_spawn_sound = pygame.mixer.Sound('Sounds/horn-89801.mp3')
    tile_spawn_sound = pygame.mixer.Sound('Sounds/card-sounds-35956.mp3')
    tile_spawn_sound.set_volume(0.4)
    #Set the background music to play on loop
    background_music = pygame.mixer.music.load('Sounds/ancientstones.mp3')
    pygame.mixer.music.set_volume(0.40)
    pygame.mixer.music.play(loops=-1)

    #Game data from server
    game = n.receive()
    
    def processTile():
        drawn_tile = game.game_deck.drawTile()
        if len(game.tile_list) > 0:
            game.tile_list[0].locked = True
        game.tile_list.insert(0, drawn_tile)
        #play the tile spawn sound
        tile_spawn_sound.play() 

    #Create our button for drawing the deck
    draw_button = button.Button((screen.get_width() / 2) - 200, screen.get_height() - 150, 400, 100, "Draw Tile (72)", click_function=processTile, color="white",
                            hover_color="grey", click_color="red", font_size=30)
    
    #Clock so we arent sending/receiving info too often
    clock = pygame.time.Clock()
    
    #*********
    #Main game loop
    #*********
    while running:
        
        #Sync the client to the server
        game = n.receive()
        
        #Gets the events that are done
        event_list = pygame.event.get()
        #Check for event if user has made any sort of input
        for event in event_list:
            #Closes winow if X is pressed
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #Closes window if esc key pressed
                if event.key == pygame.K_ESCAPE:
                    running = False
                #Checks for WASD and calls the shift function on meeple and tile
                #105 is the grid size (grid isn't called in main just hardcode it fuggit)
                elif event.key == pygame.K_w:
                    for i in game.tile_list:
                        i.shift(screen, valueX=0, valueY=-105)
                    for i in game.meeple_list:
                        i.shift(screen, valueX=0, valueY=-105)
                elif event.key == pygame.K_a:
                    for i in game.tile_list:
                        i.shift(screen, valueX=-105, valueY=0)
                    for i in game.meeple_list:
                        i.shift(screen, valueX=-105, valueY=0)
                elif event.key == pygame.K_s:
                    for i in game.tile_list:
                        i.shift(screen, valueX=0, valueY=105)
                    for i in game.meeple_list:
                        i.shift(screen, valueX=0, valueY=105)
                elif event.key == pygame.K_d:
                    for i in game.tile_list:
                        i.shift(screen, valueX=105, valueY=0)
                    for i in game.meeple_list:
                        i.shift(screen, valueX=105, valueY=0)
                #Press 1 for purple meeple
                elif event.key == pygame.K_1:  
                    game.meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 'MiscAssets/Meeples/PurpleMeeple.png'))
                    #play sound
                    pygame.mixer.Channel(1).play(meeple_spawn_sound)
                #Press 2 for pink meeple
                elif event.key == pygame.K_2:
                    game.meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 'MiscAssets/Meeples/PinkMeeple.png'))
                    #play sound
                    pygame.mixer.Channel(1).play(meeple_spawn_sound)
                #Press 3 for blue meeple
                elif event.key == pygame.K_3:
                    game.meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 'MiscAssets/Meeples/BlueMeeple.png'))
                    #play sound
                    pygame.mixer.Channel(1).play(meeple_spawn_sound)
                #Press 4 for orange meeple
                elif event.key == pygame.K_4:
                    game.meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 'MiscAssets/Meeples/OrangeMeeple.png'))
                    #play sound
                    pygame.mixer.Channel(1).play(meeple_spawn_sound)

        #Set window color
        screen.fill("black")

        #Tile handling
        for i in game.tile_list:
            if i is not None and not i.locked:
                i.processInput(event_list)
        for i in reversed(game.tile_list):
            if i is not None:
                i.draw(screen)
        #Meeple handling
        for i in game.meeple_list:
            if i.show:
                i.process(screen, event_list)
            else: 
                #meeple2_sound.play()
                game.meeple_list.remove(i)
        draw_button.process(screen, event_list)

        #Update the display
        pygame.display.flip()
        
        #Update the server
        n.send(game)