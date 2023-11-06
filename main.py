import pygame
from tile import Tile
import button
from deck import Deck
from meeple import Meeple
from startmenu import Startmenu
from gamestate import Gamestate

def main():
    #Initialize pygame module
    pygame.init()


    #Set window size
    screen = pygame.display.set_mode((0, 0),pygame.RESIZABLE, pygame.FULLSCREEN)
    
    #Set window name
    pygame.display.set_caption('Carcassonne')
    #Set window icon
    pygame.display.set_icon(pygame.image.load('MiscAssets/CarcasonneLogoTransparentBackground.png'))
    
    #For if game is running
    running = True


    start = Startmenu()
    gamestate = Gamestate()
    game_deck = Deck()
    tile_list = []
    meeple_list = []
    button_list = []
    def processTile():
        drawn_tile = game_deck.drawTile()
        tile_list.insert(0, drawn_tile)
        draw_button.clickable = False
        round_button.clickable = True

    def endRound():
        if len(tile_list) > 0:
            tile_list[0].locked = True
        draw_button.clickable = True
        round_button.clickable = False

    def gameStart():
         gamestate.updateToGameState(1)


    #Create our button for drawing the deck
    start_button = button.Button((screen.get_width() / 2) - 200, screen.get_height() - 150, 400, 100,
                                 "Start Game",
                                 click_function=gameStart, color="white",
                                 hover_color="grey", click_color="red", font_size=30)
    draw_button = button.Button((screen.get_width() / 2) - 200, screen.get_height() - 150, 200, 100, "Draw Tile (72)", click_function=processTile, color="white",
                               hover_color="grey", click_color="red", font_size=30)
    round_button = button.Button((screen.get_width() / 2), screen.get_height() - 150, 200, 100, "End Round",
                                click_function=endRound, color="white",
                                hover_color="grey", click_color="red", font_size=30)
    button_list.append(draw_button)
    button_list.append(round_button)
    round_button.clickable = False

    #Creating the tile that starts in play
    #starting_tile = Tile((screen.get_width() / 2.0) -50, (screen.get_height() / 2.0) - 150, "TileAssets/Tile8_3")
    #tile_list.insert(0, starting_tile)
    #*********
    #Main game loop
    #*********
    # *********
    while running:
        if gamestate.currentGameState() == 0:
            # Gets the events that are done
            event_list = pygame.event.get()
            # Check for event if user has made any sort of input
            for event in event_list:
                # Closes window if X is pressed
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Closes window if esc key pressed
                    if event.key == pygame.K_ESCAPE:
                        running = False
            start.drawStartMenu()
            start_button.process(screen, event_list)

        if gamestate.currentGameState() == 1:
            # Gets the events that are done
            event_list = pygame.event.get()
            # Check for event if user has made any sort of input
            for event in event_list:
                # Closes window if X is pressed
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Closes window if esc key pressed
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # Checks for WASD and calls the shift function on meeple and tile
                    # 105 is the grid size (grid isn't called in main just hardcode it fuggit)
                    elif event.key == pygame.K_w:
                        for i in tile_list:
                            i.shift(screen, valueX=0, valueY=-105)
                        for i in meeple_list:
                            i.shift(screen, valueX=0, valueY=-105)
                    elif event.key == pygame.K_a:
                        for i in tile_list:
                            i.shift(screen, valueX=-105, valueY=0)
                        for i in meeple_list:
                            i.shift(screen, valueX=-105, valueY=0)
                    elif event.key == pygame.K_s:
                        for i in tile_list:
                            i.shift(screen, valueX=0, valueY=105)
                        for i in meeple_list:
                            i.shift(screen, valueX=0, valueY=105)
                    elif event.key == pygame.K_d:
                        for i in tile_list:
                            i.shift(screen, valueX=105, valueY=0)
                        for i in meeple_list:
                            i.shift(screen, valueX=105, valueY=0)
                    # Press 1 for purple meeple
                    elif event.key == pygame.K_1:
                        meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                                     'MiscAssets/Meeples/PurpleMeeple.png'))
                    # Press 2 for pink meeple
                    elif event.key == pygame.K_2:
                        meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                                     'MiscAssets/Meeples/PinkMeeple.png'))
                    # Press 3 for blue meeple
                    elif event.key == pygame.K_3:
                        meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                                     'MiscAssets/Meeples/BlueMeeple.png'))
                    # Press 4 for orange meeple
                    elif event.key == pygame.K_4:
                        meeple_list.insert(0, Meeple(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],
                                                     'MiscAssets/Meeples/OrangeMeeple.png'))

            # Set window color
            screen.fill("black")

            # Tile handling
            for i in tile_list:
                if i is not None and not i.locked:
                    i.processInput(event_list)
            for i in reversed(tile_list):
                if i is not None:
                    i.draw(screen)
            # Meeple handling
            for i in meeple_list:
                if i.show:
                    i.process(screen, event_list)
                else:
                    meeple_list.remove(i)
            #Button handling
            for i in button_list:
                i.process(screen, event_list)


        #Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
